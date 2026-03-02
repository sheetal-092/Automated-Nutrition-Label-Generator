"""
Recipe Parser and Nutrition Calculator
Parses recipe ingredients and calculates nutritional values
"""

from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
import re


@dataclass
class ParsedIngredient:
    """Represents a parsed ingredient with quantity"""
    name: str
    weight_g: float
    original_text: str


class RecipeParser:
    """Parses recipe text and extracts ingredients with quantities"""
    
    # Common units and their conversion to grams
    UNIT_CONVERSIONS = {
        'kg': 1000,
        'g': 1,
        'gram': 1,
        'grams': 1,
        'kilogram': 1000,
        'kilograms': 1000,
        'ml': 1,  # Approximation for most liquids
        'l': 1000,
        'liter': 1000,
        'liters': 1000,
        'cup': 240,  # Standard cup
        'cups': 240,
        'tbsp': 15,
        'tablespoon': 15,
        'tablespoons': 15,
        'tsp': 5,
        'teaspoon': 5,
        'teaspoons': 5,
    }
    
    def parse_ingredient_line(self, line: str) -> ParsedIngredient:
        """
        Parse a single ingredient line
        Expected format: "quantity unit ingredient_name" or "quantity ingredient_name"
        Examples: "200g chicken breast", "2 cups rice flour", "100 grams onion"
        """
        line = line.strip()
        
        # Pattern: number (optional decimal) unit ingredient
        pattern = r'(\d+\.?\d*)\s*(kg|g|gram|grams|ml|l|cup|cups|tbsp|tsp|tablespoon|teaspoon|tablespoons|teaspoons|kilogram|kilograms|liter|liters)?\s*(.+)'
        
        match = re.match(pattern, line, re.IGNORECASE)
        
        if match:
            quantity = float(match.group(1))
            unit = match.group(2).lower() if match.group(2) else 'g'
            ingredient_name = match.group(3).strip()
            
            # Convert to grams
            weight_g = quantity * self.UNIT_CONVERSIONS.get(unit, 1)
            
            return ParsedIngredient(
                name=ingredient_name,
                weight_g=weight_g,
                original_text=line
            )
        else:
            raise ValueError(f"Could not parse ingredient line: {line}")
    
    def parse_recipe(self, recipe_text: str) -> List[ParsedIngredient]:
        """Parse entire recipe text (one ingredient per line)"""
        lines = [line.strip() for line in recipe_text.split('\n') if line.strip()]
        parsed_ingredients = []
        
        for line in lines:
            try:
                parsed = self.parse_ingredient_line(line)
                parsed_ingredients.append(parsed)
            except ValueError as e:
                print(f"Warning: {e}")
                
        return parsed_ingredients


class NutritionCalculator:
    """Calculates nutritional values for recipes"""
    
    # FSSAI requires these nutrients in labels
    REQUIRED_NUTRIENTS = [
        'energy_kcal',
        'protein_g',
        'total_fat_g',
        'saturated_fat_g',
        'trans_fat_g',
        'carbohydrates_g',
        'total_sugars_g',
        'added_sugars_g',
        'dietary_fiber_g',
        'sodium_mg',
        'cholesterol_mg'
    ]
    
    def calculate_nutrition(self, ingredients: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Calculate total nutrition for a recipe
        ingredients: List of dicts with ingredient data and weight_g
        """
        nutrition = {nutrient: 0.0 for nutrient in self.REQUIRED_NUTRIENTS}
        
        for ingredient in ingredients:
            weight_g = ingredient['weight_g']
            # All nutritional values are per 100g in database
            factor = weight_g / 100.0
            
            for nutrient in self.REQUIRED_NUTRIENTS:
                value = ingredient.get(nutrient, 0) or 0  # Handle None values
                nutrition[nutrient] += value * factor
                
        return nutrition
    
    def calculate_per_serving(self, total_nutrition: Dict[str, float], 
                             servings: int) -> Dict[str, float]:
        """Calculate nutrition per serving"""
        return {
            nutrient: value / servings 
            for nutrient, value in total_nutrition.items()
        }
    
    def calculate_per_100g(self, total_nutrition: Dict[str, float], 
                          total_weight_g: float) -> Dict[str, float]:
        """Calculate nutrition per 100g"""
        factor = 100.0 / total_weight_g
        return {
            nutrient: value * factor 
            for nutrient, value in total_nutrition.items()
        }
    
    def format_nutrition_value(self, value: float, nutrient: str) -> str:
        """Format nutritional value according to FSSAI standards"""
        # Energy in kcal, no decimal needed
        if nutrient == 'energy_kcal':
            return f"{round(value)}"
        
        # Nutrients in mg (sodium, cholesterol)
        elif nutrient.endswith('_mg'):
            if value < 1:
                return f"{value:.2f}"
            else:
                return f"{round(value, 1)}"
        
        # Nutrients in grams
        else:
            if value < 0.5:
                return f"{value:.2f}"
            elif value < 10:
                return f"{round(value, 1)}"
            else:
                return f"{round(value, 1)}"
    
    def get_nutrition_summary(self, nutrition: Dict[str, float], 
                             total_weight_g: float) -> str:
        """Generate human-readable nutrition summary"""
        summary_lines = [
            "Nutritional Information:",
            f"Per 100g serving:",
            f"  Energy: {self.format_nutrition_value(nutrition['energy_kcal'], 'energy_kcal')} kcal",
            f"  Protein: {self.format_nutrition_value(nutrition['protein_g'], 'protein_g')} g",
            f"  Total Fat: {self.format_nutrition_value(nutrition['total_fat_g'], 'total_fat_g')} g",
            f"    - Saturated Fat: {self.format_nutrition_value(nutrition['saturated_fat_g'], 'saturated_fat_g')} g",
            f"    - Trans Fat: {self.format_nutrition_value(nutrition['trans_fat_g'], 'trans_fat_g')} g",
            f"  Carbohydrates: {self.format_nutrition_value(nutrition['carbohydrates_g'], 'carbohydrates_g')} g",
            f"    - Total Sugars: {self.format_nutrition_value(nutrition['total_sugars_g'], 'total_sugars_g')} g",
            f"    - Added Sugars: {self.format_nutrition_value(nutrition['added_sugars_g'], 'added_sugars_g')} g",
            f"  Dietary Fiber: {self.format_nutrition_value(nutrition['dietary_fiber_g'], 'dietary_fiber_g')} g",
            f"  Sodium: {self.format_nutrition_value(nutrition['sodium_mg'], 'sodium_mg')} mg",
            f"  Cholesterol: {self.format_nutrition_value(nutrition['cholesterol_mg'], 'cholesterol_mg')} mg"
        ]
        
        return '\n'.join(summary_lines)
