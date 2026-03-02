"""
Example: Custom Recipe Processing
Shows how to use the Nutrition Label Generator programmatically
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from main import NutritionLabelApp


def example_1_simple_recipe():
    """Example 1: Process a simple recipe"""
    
    print("\n" + "="*60)
    print("Example 1: Simple Recipe")
    print("="*60 + "\n")
    
    app = NutritionLabelApp()
    
    recipe = """
    200g Whole Wheat Flour
    100ml Whole Milk
    10g Butter
    2g Salt
    """
    
    result = app.process_recipe(
        recipe_name="Simple Wheat Pancakes",
        recipe_text=recipe,
        description="Easy pancakes with whole wheat",
        servings=4
    )
    
    print(f"\n✓ Recipe processed!")
    print(f"  Energy: {result['nutrition_per_100g']['energy_kcal']:.0f} kcal/100g")
    print(f"  Protein: {result['nutrition_per_100g']['protein_g']:.1f} g/100g")
    print(f"  FSSAI Compliant: {result['is_fssai_compliant']}")
    print(f"  Label: {result['html_file']}")


def example_2_batch_processing():
    """Example 2: Process multiple recipes"""
    
    print("\n" + "="*60)
    print("Example 2: Batch Processing")
    print("="*60 + "\n")
    
    app = NutritionLabelApp()
    
    recipes = [
        {
            "name": "Protein Shake",
            "ingredients": "200ml Whole Milk\n50g Almonds\n30g Honey",
            "servings": 1
        },
        {
            "name": "Vegetable Soup",
            "ingredients": "100g Tomato\n100g Onion\n50g Carrot\n2g Salt",
            "servings": 2
        },
        {
            "name": "Energy Bars",
            "ingredients": "100g Oats\n50g Peanuts\n30g Honey\n20g Butter",
            "servings": 6
        }
    ]
    
    results = []
    
    for recipe in recipes:
        try:
            result = app.process_recipe(
                recipe_name=recipe["name"],
                recipe_text=recipe["ingredients"],
                servings=recipe["servings"]
            )
            results.append({
                'name': recipe['name'],
                'energy': result['nutrition_per_100g']['energy_kcal'],
                'compliant': result['is_fssai_compliant']
            })
            print(f"✓ {recipe['name']}: {result['nutrition_per_100g']['energy_kcal']:.0f} kcal/100g")
        except Exception as e:
            print(f"✗ {recipe['name']}: Error - {e}")
    
    print(f"\n✓ Processed {len(results)} recipes successfully!")


def example_3_add_custom_ingredient():
    """Example 3: Add a custom ingredient and use it"""
    
    print("\n" + "="*60)
    print("Example 3: Custom Ingredient")
    print("="*60 + "\n")
    
    app = NutritionLabelApp()
    app.db.connect()
    
    # Add custom ingredient
    try:
        ingredient_id = app.db.add_ingredient({
            'name': 'Brown Rice',
            'category': 'Grains',
            'energy_kcal': 370,
            'protein_g': 7.9,
            'total_fat_g': 2.9,
            'saturated_fat_g': 0.6,
            'trans_fat_g': 0.0,
            'carbohydrates_g': 77.2,
            'total_sugars_g': 0.7,
            'added_sugars_g': 0.0,
            'dietary_fiber_g': 3.5,
            'sodium_mg': 7,
            'cholesterol_mg': 0
        })
        print(f"✓ Added 'Brown Rice' with ID: {ingredient_id}")
    except Exception as e:
        print(f"Note: Ingredient may already exist - {e}")
    
    app.db.disconnect()
    
    # Use the custom ingredient in a recipe
    recipe = """
    200g Brown Rice
    100g Chickpeas
    50g Carrot
    10ml Olive Oil
    2g Salt
    """
    
    result = app.process_recipe(
        recipe_name="Brown Rice Bowl",
        recipe_text=recipe,
        servings=3
    )
    
    print(f"\n✓ Recipe with custom ingredient processed!")
    print(f"  Energy: {result['nutrition_per_100g']['energy_kcal']:.0f} kcal/100g")


def example_4_database_queries():
    """Example 4: Query the ingredient database"""
    
    print("\n" + "="*60)
    print("Example 4: Database Queries")
    print("="*60 + "\n")
    
    app = NutritionLabelApp()
    app.db.connect()
    
    # Search for ingredients
    print("Searching for 'milk':")
    results = app.db.search_ingredients("milk")
    for ing in results:
        print(f"  - {ing['name']} ({ing['category']}): {ing['protein_g']}g protein/100g")
    
    # Get all dairy products
    print("\nAll Dairy Products:")
    dairy = app.db.get_ingredients_by_category("Dairy")
    for ing in dairy:
        print(f"  - {ing['name']}: {ing['energy_kcal']} kcal/100g")
    
    # Get specific ingredient
    print("\nSpecific Ingredient (Oats):")
    oats = app.db.get_ingredient_by_name("Oats")
    if oats:
        print(f"  Energy: {oats['energy_kcal']} kcal")
        print(f"  Protein: {oats['protein_g']} g")
        print(f"  Fiber: {oats['dietary_fiber_g']} g")
    
    app.db.disconnect()


def example_5_compliance_checking():
    """Example 5: Check FSSAI compliance"""
    
    print("\n" + "="*60)
    print("Example 5: FSSAI Compliance Checking")
    print("="*60 + "\n")
    
    app = NutritionLabelApp()
    
    # High-fat recipe
    high_fat_recipe = """
    100g Butter
    50g Cheddar Cheese
    30g Sugar
    """
    
    result = app.process_recipe(
        recipe_name="High Fat Sample",
        recipe_text=high_fat_recipe,
        servings=1
    )
    
    print(f"Recipe: High Fat Sample")
    print(f"  Compliant: {result['is_fssai_compliant']}")
    print(f"  Warnings: {len(result['warnings'])}")
    
    if result['warnings']:
        print("\n  Compliance Warnings:")
        for warning in result['warnings']:
            print(f"    ⚠ {warning}")
    
    if result['errors']:
        print("\n  Compliance Errors:")
        for error in result['errors']:
            print(f"    ✗ {error}")


def main():
    """Run all examples"""
    
    print("\n" + "="*70)
    print("NUTRITION LABEL GENERATOR - CODE EXAMPLES")
    print("="*70)
    
    examples = [
        ("Simple Recipe Processing", example_1_simple_recipe),
        ("Batch Processing", example_2_batch_processing),
        ("Custom Ingredients", example_3_add_custom_ingredient),
        ("Database Queries", example_4_database_queries),
        ("FSSAI Compliance", example_5_compliance_checking)
    ]
    
    for idx, (name, func) in enumerate(examples, 1):
        print(f"\n{'#'*70}")
        print(f"# Example {idx}: {name}")
        print(f"{'#'*70}")
        
        try:
            func()
        except Exception as e:
            print(f"\n✗ Error in example: {e}")
    
    print("\n" + "="*70)
    print("All examples completed!")
    print("="*70)
    print("\nCheck the 'output/' folder for generated labels.")
    print("\n")


if __name__ == "__main__":
    main()
