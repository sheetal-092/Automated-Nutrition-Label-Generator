"""
Main Application - Automated Nutrition Label Generator
Integrates all components to generate FSSAI-compliant nutrition labels
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

from database_manager import DatabaseManager
from recipe_parser import RecipeParser, NutritionCalculator
from fssai_compliance import FSSAIValidator, FSSAICategory
from label_generator import LabelGenerator
from llm_mapper import LLMIngredientMapper
from nutrition_analyzer import NutritionAnalyzer


class NutritionLabelApp:
    """Main application for nutrition label generation"""
    
    def __init__(self, db_path: str = "nutrition.db", use_llm: bool = False):
        """
        Initialize the application
        
        Args:
            db_path: Path to SQLite database
            use_llm: Whether to use LLM for ingredient mapping
        """
        self.db = DatabaseManager(db_path)
        self.parser = RecipeParser()
        self.calculator = NutritionCalculator()
        self.validator = FSSAIValidator()
        self.label_gen = LabelGenerator()
        self.llm_mapper = LLMIngredientMapper() if use_llm else None
        
        # Initialize database if it doesn't exist
        if not Path(db_path).exists():
            self._initialize_database()
    
    def _initialize_database(self):
        """Initialize database with schema and seed data"""
        schema_file = Path(__file__).parent / "database" / "schema.sql"
        seed_file = Path(__file__).parent / "database" / "seed_data.sql"
        
        self.db.initialize_database(str(schema_file), str(seed_file))
    
    def process_recipe(self,
                      recipe_name: str,
                      recipe_text: str,
                      description: str = "",
                      servings: int = 1) -> dict:
        """
        Process a recipe and generate nutrition label
        
        Args:
            recipe_name: Name of the recipe
            recipe_text: Recipe ingredients (one per line: "quantity unit ingredient")
            description: Recipe description
            servings: Number of servings
        
        Returns:
            dict with recipe_id, nutrition data, label files, compliance info
        """
        
        print(f"\n{'='*60}")
        print(f"Processing Recipe: {recipe_name}")
        print(f"{'='*60}\n")
        
        # Step 1: Parse recipe
        print("Step 1: Parsing ingredients...")
        parsed_ingredients = self.parser.parse_recipe(recipe_text)
        
        if not parsed_ingredients:
            raise ValueError("No ingredients could be parsed from recipe")
        
        print(f"  ✓ Parsed {len(parsed_ingredients)} ingredients")
        
        # Step 2: Map to database ingredients
        print("\nStep 2: Mapping ingredients to database...")
        self.db.connect()
        
        total_weight = 0
        mapped_ingredients = []
        
        for parsed in parsed_ingredients:
            # Try to find ingredient in database
            ingredient = self.db.get_ingredient_by_name(parsed.name)
            
            # If not found, use LLM or fuzzy matching
            if not ingredient and self.llm_mapper:
                print(f"  ? '{parsed.name}' not found, using LLM mapper...")
                all_ingredients = self.db.get_all_ingredients()
                ingredient = self.llm_mapper.map_ingredient(parsed.name, all_ingredients)
            elif not ingredient:
                # Fuzzy search
                search_results = self.db.search_ingredients(parsed.name)
                if search_results:
                    ingredient = search_results[0]
                    print(f"  ? Using fuzzy match: '{parsed.name}' -> '{ingredient['name']}'")
            
            if ingredient:
                ingredient['weight_g'] = parsed.weight_g
                mapped_ingredients.append(ingredient)
                total_weight += parsed.weight_g
                print(f"  ✓ {parsed.weight_g}g {ingredient['name']}")
            else:
                print(f"  ✗ Warning: Could not find '{parsed.name}' in database")
        
        if not mapped_ingredients:
            raise ValueError("No ingredients could be mapped to database")
        
        # Step 3: Calculate nutrition
        print("\nStep 3: Calculating nutritional values...")
        total_nutrition = self.calculator.calculate_nutrition(mapped_ingredients)
        nutrition_per_100g = self.calculator.calculate_per_100g(total_nutrition, total_weight)
        nutrition_per_serving = self.calculator.calculate_per_serving(total_nutrition, servings)
        
        print(self.calculator.get_nutrition_summary(nutrition_per_100g, total_weight))
        
        # Step 4: FSSAI Validation
        print("\nStep 4: Validating FSSAI compliance...")
        is_compliant, warnings, errors = self.validator.validate_label(nutrition_per_100g)
        compliance_report = self.validator.generate_compliance_report(nutrition_per_100g)
        print(compliance_report)
        
        # Step 4.5: Enhanced Analysis (NEW FEATURES)
        print("\n" + "="*60)
        print("ENHANCED NUTRITION ANALYSIS")
        print("="*60)
        
        # Compliance Status Indicator
        compliance_status = NutritionAnalyzer.get_compliance_status(is_compliant, warnings, errors)
        print(f"\n{compliance_status['badge']} COMPLIANCE STATUS: {compliance_status['level']}")
        print(f"   {compliance_status['message']}")
        
        # Batch vs Per Serving Output
        print(NutritionAnalyzer.format_batch_nutrition(total_nutrition, total_weight))
        print(f"🔹 PER 100g NUTRITION")
        print(f"   Energy: {nutrition_per_100g.get('energy_kcal', 0):.0f} kcal")
        print(f"   Protein: {nutrition_per_100g.get('protein_g', 0):.1f}g")
        print(f"   Fat: {nutrition_per_100g.get('total_fat_g', 0):.1f}g")
        print(f"   Carbs: {nutrition_per_100g.get('carbohydrates_g', 0):.1f}g")
        
        print(f"\n🔹 PER SERVING NUTRITION ({total_weight/servings:.0f}g)")
        print(f"   Energy: {nutrition_per_serving.get('energy_kcal', 0):.0f} kcal")
        print(f"   Protein: {nutrition_per_serving.get('protein_g', 0):.1f}g")
        print(f"   Fat: {nutrition_per_serving.get('total_fat_g', 0):.1f}g")
        print(f"   Carbs: {nutrition_per_serving.get('carbohydrates_g', 0):.1f}g")
        
        # % Daily Values
        daily_values = NutritionAnalyzer.calculate_daily_values(nutrition_per_serving)
        print("\n📊 % DAILY VALUE (per serving):")
        if daily_values.get('energy_kcal', 0) > 0:
            print(f"   Energy: {daily_values['energy_kcal']:.1f}% of daily needs")
        if daily_values.get('protein_g', 0) > 0:
            print(f"   Protein: {daily_values['protein_g']:.1f}% of daily needs")
        if daily_values.get('total_fat_g', 0) > 0:
            print(f"   Fat: {daily_values['total_fat_g']:.1f}% of daily needs")
        if daily_values.get('total_sugars_g', 0) > 0:
            print(f"   Sugar: {daily_values['total_sugars_g']:.1f}% of daily limit")
        if daily_values.get('sodium_mg', 0) > 0:
            print(f"   Sodium: {daily_values['sodium_mg']:.1f}% of daily limit")
        
        # Create ingredients list string
        ingredients_list = ", ".join([ing['name'] for ing in mapped_ingredients])
        
        # Allergen Declaration
        allergens = NutritionAnalyzer.detect_allergens(ingredients_list)
        if allergens:
            print(f"\n🔸 ALLERGEN DECLARATION:")
            print(f"   Contains: {', '.join(allergens)}")
        else:
            print(f"\n✓ No common allergens detected")
        
        # Nutritional Insights (Smart Analysis)
        insights = NutritionAnalyzer.generate_nutritional_insights(nutrition_per_100g)
        
        if insights['highlights']:
            print(f"\n✨ NUTRITIONAL HIGHLIGHTS:")
            for highlight in insights['highlights']:
                print(f"   {highlight}")
        
        if insights['concerns']:
            print(f"\n🔸 COMPLIANCE WARNINGS:")
            for concern in insights['concerns']:
                print(f"   {concern}")
        
        if insights['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in insights['recommendations']:
                print(f"   • {rec}")
        
        print("="*60)
        
        # Step 5: Generate labels
        print("\nStep 5: Generating nutrition labels...")
        
        # Generate HTML label
        html_label = self.label_gen.generate_html_label(
            product_name=recipe_name,
            nutrition_per_100g=nutrition_per_100g,
            nutrition_per_serving=nutrition_per_serving,
            serving_size=f"{total_weight/servings:.0f}g",
            servings_per_package=servings,
            ingredients_list=ingredients_list,
            manufacturer_info={
                "name": "Your Company Name",
                "address": "Your Address Here",
                "contact": "Contact Information"
            },
            fssai_license="XXXXXXXXXXXXXXXXXX"
        )
        
        # Generate JSON label
        json_label = self.label_gen.generate_json_label(
            product_name=recipe_name,
            nutrition_per_100g=nutrition_per_100g,
            nutrition_per_serving=nutrition_per_serving,
            serving_size=f"{total_weight/servings:.0f}g",
            servings_per_package=servings,
            ingredients_list=ingredients_list,
            fssai_compliant=is_compliant,
            compliance_warnings=warnings
        )
        
        # Save to database
        recipe_id = self.db.create_recipe(recipe_name, description, total_weight, servings)
        
        for ingredient in mapped_ingredients:
            self.db.add_recipe_ingredient(recipe_id, ingredient['id'], ingredient['weight_g'])
        
        label_id = self.db.save_nutrition_label(recipe_id, json_label, is_compliant)
        
        # Save files
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        safe_name = recipe_name.replace(" ", "_").replace("/", "_")
        html_file = output_dir / f"{safe_name}_label.html"
        json_file = output_dir / f"{safe_name}_data.json"
        
        self.label_gen.save_html_label(html_label, str(html_file))
        self.label_gen.save_json_label(json_label, str(json_file))
        
        self.db.disconnect()
        
        print(f"\n✓ Labels generated successfully!")
        print(f"  - HTML: {html_file}")
        print(f"  - JSON: {json_file}")
        
        return {
            'recipe_id': recipe_id,
            'label_id': label_id,
            'total_weight_g': total_weight,
            'total_nutrition': total_nutrition,
            'nutrition_per_100g': nutrition_per_100g,
            'nutrition_per_serving': nutrition_per_serving,
            'is_fssai_compliant': is_compliant,
            'warnings': warnings,
            'errors': errors,
            'html_file': str(html_file),
            'json_file': str(json_file),
            # Enhanced features
            'compliance_status': compliance_status,
            'daily_values': daily_values,
            'allergens': allergens,
            'nutritional_insights': insights,
            'ingredients_list': ingredients_list
        }


def main():
    """Main entry point"""
    
    print("=" * 60)
    print("Automated Nutrition Label Generator")
    print("FSSAI Compliant | Powered by Python & SQLite")
    print("=" * 60)
    
    # Initialize app
    app = NutritionLabelApp(use_llm=False)
    
    # Example: Process a sample recipe
    recipe_name = "Whole Wheat Chapati"
    recipe_text = """
    300g Whole Wheat Flour
    150ml Water
    2g Salt
    10ml Sunflower Oil
    """
    
    result = app.process_recipe(
        recipe_name=recipe_name,
        recipe_text=recipe_text,
        description="Traditional Indian flatbread made with whole wheat flour",
        servings=6
    )
    
    print("\n" + "=" * 60)
    print("Processing Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
