"""
LLM Integration for Intelligent Ingredient Mapping
Uses LLM APIs to map user ingredients to database entries
"""

from typing import List, Dict, Any, Optional, Tuple
import json
import os


class LLMIngredientMapper:
    """
    Uses LLM to intelligently map ingredient names to database entries
    Supports multiple LLM providers (OpenAI, Anthropic, etc.)
    """
    
    def __init__(self, api_key: Optional[str] = None, provider: str = "openai"):
        """
        Initialize LLM mapper
        
        Args:
            api_key: API key for LLM service (if None, tries to get from env)
            provider: LLM provider ('openai', 'anthropic', 'local')
        """
        self.provider = provider
        self.api_key = api_key or os.getenv(f"{provider.upper()}_API_KEY")
        self.client = None
        
        # Initialize client based on provider
        if self.api_key and provider == "openai":
            try:
                import openai
                self.client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                print("Warning: openai package not installed. Install with: pip install openai")
        elif self.api_key and provider == "anthropic":
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                print("Warning: anthropic package not installed. Install with: pip install anthropic")
    
    def map_ingredient(self, 
                      user_ingredient: str,
                      available_ingredients: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Map user's ingredient name to best matching database ingredient
        
        Args:
            user_ingredient: Ingredient name from user's recipe
            available_ingredients: List of available ingredients from database
        
        Returns:
            Best matching ingredient dict or None
        """
        
        # If LLM is not available, use fuzzy matching
        if not self.client:
            return self._fuzzy_match(user_ingredient, available_ingredients)
        
        # Use LLM for intelligent matching
        return self._llm_match(user_ingredient, available_ingredients)
    
    def _fuzzy_match(self, 
                    user_ingredient: str,
                    available_ingredients: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Fallback fuzzy matching without LLM"""
        user_ingredient_lower = user_ingredient.lower().strip()
        
        # Exact match
        for ing in available_ingredients:
            if ing['name'].lower() == user_ingredient_lower:
                return ing
        
        # Partial match
        for ing in available_ingredients:
            if user_ingredient_lower in ing['name'].lower() or \
               ing['name'].lower() in user_ingredient_lower:
                return ing
        
        # Word-based matching
        user_words = set(user_ingredient_lower.split())
        best_match = None
        best_score = 0
        
        for ing in available_ingredients:
            ing_words = set(ing['name'].lower().split())
            common_words = user_words.intersection(ing_words)
            score = len(common_words)
            
            if score > best_score:
                best_score = score
                best_match = ing
        
        return best_match if best_score > 0 else None
    
    def _llm_match(self,
                  user_ingredient: str,
                  available_ingredients: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Use LLM to find best ingredient match"""
        
        # Create ingredient list for LLM
        ingredient_names = [ing['name'] for ing in available_ingredients]
        
        prompt = f"""Given a user's ingredient "{user_ingredient}", find the best matching ingredient from this list:

{json.dumps(ingredient_names, indent=2)}

Return ONLY the exact name of the best matching ingredient from the list, or "NONE" if no good match exists.
Consider common names, synonyms, and cooking terminology.

Examples:
- "chicken" matches "Chicken Breast"
- "atta" matches "Whole Wheat Flour"
- "dahi" matches "Yogurt (Plain)"
- "aloo" matches "Potato"

Best match:"""
        
        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a food ingredient matching assistant. Be precise and only return ingredient names from the given list."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0,
                    max_tokens=50
                )
                match_name = response.choices[0].message.content.strip()
                
            elif self.provider == "anthropic":
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=50,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                match_name = response.content[0].text.strip()
            
            # Find the matched ingredient
            if match_name and match_name != "NONE":
                for ing in available_ingredients:
                    if ing['name'].lower() == match_name.lower():
                        return ing
            
            # Fallback to fuzzy match
            return self._fuzzy_match(user_ingredient, available_ingredients)
            
        except Exception as e:
            print(f"LLM error: {e}. Falling back to fuzzy matching.")
            return self._fuzzy_match(user_ingredient, available_ingredients)
    
    def suggest_missing_ingredient(self, ingredient_name: str) -> Dict[str, Any]:
        """
        Use LLM to suggest nutritional data for missing ingredient
        Returns estimated nutritional values
        """
        
        if not self.client:
            return self._default_nutrition_estimate(ingredient_name)
        
        prompt = f"""Provide estimated nutritional information per 100g for: {ingredient_name}

Return a JSON object with these fields (numeric values only):
{{
    "energy_kcal": <number>,
    "protein_g": <number>,
    "total_fat_g": <number>,
    "saturated_fat_g": <number>,
    "trans_fat_g": <number>,
    "carbohydrates_g": <number>,
    "total_sugars_g": <number>,
    "added_sugars_g": <number>,
    "dietary_fiber_g": <number>,
    "sodium_mg": <number>,
    "cholesterol_mg": <number>
}}

Base your estimates on standard nutritional databases like USDA or IFCT.
Return ONLY the JSON object, no other text."""
        
        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a nutritional data expert. Provide accurate nutritional estimates."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0,
                    max_tokens=300
                )
                nutrition_json = response.choices[0].message.content.strip()
                
            elif self.provider == "anthropic":
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=300,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                nutrition_json = response.content[0].text.strip()
            
            # Parse JSON response
            nutrition_data = json.loads(nutrition_json)
            nutrition_data['name'] = ingredient_name
            nutrition_data['category'] = 'LLM-Generated'
            
            return nutrition_data
            
        except Exception as e:
            print(f"LLM error generating nutrition data: {e}")
            return self._default_nutrition_estimate(ingredient_name)
    
    def _default_nutrition_estimate(self, ingredient_name: str) -> Dict[str, Any]:
        """Provide conservative default estimates"""
        return {
            'name': ingredient_name,
            'category': 'Estimated',
            'energy_kcal': 50,
            'protein_g': 1.0,
            'total_fat_g': 0.5,
            'saturated_fat_g': 0.1,
            'trans_fat_g': 0.0,
            'carbohydrates_g': 10.0,
            'total_sugars_g': 1.0,
            'added_sugars_g': 0.0,
            'dietary_fiber_g': 1.0,
            'sodium_mg': 10,
            'cholesterol_mg': 0
        }
