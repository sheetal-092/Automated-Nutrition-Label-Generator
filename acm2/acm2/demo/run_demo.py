"""
Demo Script - Nutrition Label Generator
Demonstrates the system with multiple sample recipes
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from main import NutritionLabelApp


class Demo:
    """Demo class with sample recipes"""
    
    # Sample recipes following FSSAI guidelines
    SAMPLE_RECIPES = {
        "Healthy Oatmeal Bowl": {
            "ingredients": """
            100g Oats
            200ml Whole Milk
            50g Almonds
            30g Honey
            100g Carrot
            """,
            "description": "Nutritious breakfast bowl with oats, milk, nuts and vegetables",
            "servings": 2
        },
        
        "Paneer Butter Masala": {
            "ingredients": """
            250g Paneer
            100g Tomato
            50g Onion
            20g Butter
            10ml Sunflower Oil
            2g Salt
            5g Red Chili Powder
            3g Turmeric Powder
            100ml Yogurt (Plain)
            """,
            "description": "Popular Indian curry dish with cottage cheese in rich tomato gravy",
            "servings": 4
        },
        
        "Protein Chickpea Salad": {
            "ingredients": """
            200g Chickpeas
            100g Tomato
            50g Onion
            50g Carrot
            30g Spinach
            10ml Olive Oil
            2g Salt
            """,
            "description": "High-protein vegetarian salad with chickpeas and fresh vegetables",
            "servings": 3
        },
        
        "Energy Trail Mix": {
            "ingredients": """
            100g Almonds
            100g Cashews
            50g Peanuts
            50g Honey
            10g Jaggery
            """,
            "description": "Energy-dense snack mix with nuts and natural sweeteners",
            "servings": 10
        },
        
        "Classic Cheese Sandwich": {
            "ingredients": """
            100g White Bread
            50g Cheddar Cheese
            20g Butter
            50g Tomato
            30g Onion
            """,
            "description": "Simple grilled cheese sandwich with vegetables",
            "servings": 2
        }
    }
    
    def __init__(self, use_llm: bool = False):
        """Initialize demo with nutrition label app"""
        self.app = NutritionLabelApp(use_llm=use_llm)
        self.results = []
    
    def run_all_demos(self):
        """Process all sample recipes"""
        
        print("\n" + "=" * 80)
        print("NUTRITION LABEL GENERATOR - DEMO")
        print("=" * 80)
        print(f"\nProcessing {len(self.SAMPLE_RECIPES)} sample recipes...")
        print("This will generate FSSAI-compliant nutrition labels for each recipe.\n")
        
        for idx, (recipe_name, recipe_data) in enumerate(self.SAMPLE_RECIPES.items(), 1):
            print(f"\n{'#' * 80}")
            print(f"Demo {idx}/{len(self.SAMPLE_RECIPES)}")
            print(f"{'#' * 80}")
            
            try:
                result = self.app.process_recipe(
                    recipe_name=recipe_name,
                    recipe_text=recipe_data["ingredients"],
                    description=recipe_data["description"],
                    servings=recipe_data["servings"]
                )
                
                self.results.append({
                    'name': recipe_name,
                    'result': result
                })
                
                print(f"\n✓ Successfully processed: {recipe_name}")
                
            except Exception as e:
                print(f"\n✗ Error processing {recipe_name}: {str(e)}")
        
        # Generate summary
        self._print_summary()
    
    def run_single_demo(self, recipe_name: str):
        """Process a single recipe by name"""
        
        if recipe_name not in self.SAMPLE_RECIPES:
            print(f"Recipe '{recipe_name}' not found in samples.")
            print(f"Available recipes: {', '.join(self.SAMPLE_RECIPES.keys())}")
            return
        
        recipe_data = self.SAMPLE_RECIPES[recipe_name]
        
        try:
            result = self.app.process_recipe(
                recipe_name=recipe_name,
                recipe_text=recipe_data["ingredients"],
                description=recipe_data["description"],
                servings=recipe_data["servings"]
            )
            
            print(f"\n✓ Successfully processed: {recipe_name}")
            
        except Exception as e:
            print(f"\n✗ Error processing {recipe_name}: {str(e)}")
    
    def _print_summary(self):
        """Print summary of all processed recipes"""
        
        print("\n" + "=" * 80)
        print("DEMO SUMMARY")
        print("=" * 80)
        
        print(f"\nTotal recipes processed: {len(self.results)}")
        
        # Compliance summary
        compliant = sum(1 for r in self.results if r['result']['is_fssai_compliant'])
        print(f"FSSAI Compliant: {compliant}/{len(self.results)}")
        
        # Energy comparison
        print("\n" + "-" * 80)
        print("Energy Comparison (per 100g):")
        print("-" * 80)
        
        for result in self.results:
            energy = result['result']['nutrition_per_100g']['energy_kcal']
            status = "✓" if result['result']['is_fssai_compliant'] else "⚠"
            print(f"{status} {result['name']:.<50} {energy:.0f} kcal")
        
        # Protein comparison
        print("\n" + "-" * 80)
        print("Protein Content (per 100g):")
        print("-" * 80)
        
        for result in self.results:
            protein = result['result']['nutrition_per_100g']['protein_g']
            print(f"  {result['name']:.<50} {protein:.1f} g")
        
        # Files generated
        print("\n" + "-" * 80)
        print("Generated Files:")
        print("-" * 80)
        
        print("\nAll labels saved in 'output/' directory:")
        for result in self.results:
            safe_name = result['name'].replace(" ", "_")
            print(f"  • {safe_name}_label.html")
            print(f"  • {safe_name}_data.json")
        
        print("\n" + "=" * 80)
        print("Demo Complete!")
        print("=" * 80)
        print("\nYou can now:")
        print("  1. Open the HTML files in a browser to view nutrition labels")
        print("  2. Review the JSON files for programmatic access to nutrition data")
        print("  3. Check the database (nutrition.db) for stored recipes")
        print("\n")


def main():
    """Main demo entry point"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description="Nutrition Label Generator Demo")
    parser.add_argument(
        "--recipe",
        type=str,
        help="Process a specific recipe by name",
        default=None
    )
    parser.add_argument(
        "--llm",
        action="store_true",
        help="Enable LLM-based ingredient mapping (requires API key)"
    )
    
    args = parser.parse_args()
    
    # Create demo instance
    demo = Demo(use_llm=args.llm)
    
    if args.recipe:
        # Process single recipe
        demo.run_single_demo(args.recipe)
    else:
        # Process all recipes
        demo.run_all_demos()


if __name__ == "__main__":
    main()
