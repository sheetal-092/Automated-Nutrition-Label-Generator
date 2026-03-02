"""
Recipe Input Interface - User-Friendly Recipe Entry
Allows non-technical users to input recipes easily
"""

import sys
from pathlib import Path
import json
import csv

sys.path.append(str(Path(__file__).parent.parent))
from main import NutritionLabelApp


class RecipeInputInterface:
    """Interactive recipe input for non-technical users"""
    
    def __init__(self):
        self.app = NutritionLabelApp()
    
    def interactive_recipe_input(self):
        """Interactive step-by-step recipe creation"""
        
        print("\n" + "="*60)
        print("NUTRITION LABEL GENERATOR - RECIPE INPUT")
        print("="*60)
        
        # Get recipe name
        recipe_name = input("\n📝 Recipe Name (e.g., 'Chocolate Chip Cookies'): ").strip()
        if not recipe_name:
            print("Error: Recipe name is required!")
            return
        
        # Get description
        description = input("📝 Description (optional, press Enter to skip): ").strip()
        
        # Get number of servings
        try:
            servings = int(input("🍽️  Number of servings (default: 1): ").strip() or "1")
        except ValueError:
            servings = 1
        
        # Get ingredients
        print("\n" + "-"*60)
        print("ADD INGREDIENTS")
        print("Format: <quantity> <unit> <ingredient name>")
        print("Example: 200 g Whole Wheat Flour")
        print("Example: 2 cups Rice Flour")
        print("Example: 100 ml Whole Milk")
        print("Type 'done' when finished")
        print("-"*60 + "\n")
        
        ingredients = []
        while True:
            ingredient_input = input(f"Ingredient {len(ingredients)+1}: ").strip()
            
            if ingredient_input.lower() == 'done':
                if not ingredients:
                    print("Error: At least one ingredient is required!")
                    continue
                break
            
            if ingredient_input:
                ingredients.append(ingredient_input)
        
        # Combine ingredients into recipe text
        recipe_text = "\n".join(ingredients)
        
        # Process recipe
        print("\n" + "="*60)
        print("Processing your recipe...")
        print("="*60)
        
        try:
            result = self.app.process_recipe(
                recipe_name=recipe_name,
                recipe_text=recipe_text,
                description=description,
                servings=servings
            )
            
            print("\n" + "="*60)
            print("✓ SUCCESS!")
            print("="*60)
            print(f"\nYour label files:")
            print(f"  📄 HTML Label: {result['html_file']}")
            print(f"    → Open this in your browser to view")
            print(f"\n  📊 JSON Data: {result['json_file']}")
            print(f"    → Raw nutritional data")
            print(f"\nFSSAI Compliance: {'✓ COMPLIANT' if result['is_fssai_compliant'] else '⚠ WITH WARNINGS'}")
            
            if result['warnings']:
                print(f"\n⚠️  Warnings ({len(result['warnings'])}):")
                for warning in result['warnings'][:3]:  # Show first 3
                    print(f"  • {warning[:70]}...")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


def load_from_csv(csv_file):
    """Load recipes from CSV file
    
    CSV Format (with header):
    Recipe Name, Description, Servings, Ingredient1, Ingredient2, ...
    
    Example:
    Oatmeal Bowl, Healthy breakfast, 2, 100g Oats, 200ml Whole Milk, 50g Almonds
    """
    
    app = NutritionLabelApp()
    
    print(f"\nLoading recipes from {csv_file}...")
    print("="*60)
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Skip header
            
            for row_num, row in enumerate(reader, 2):
                if not row or not row[0].strip():
                    continue
                
                recipe_name = row[0].strip()
                description = row[1].strip() if len(row) > 1 else ""
                
                try:
                    servings = int(row[2].strip()) if len(row) > 2 and row[2].strip() else 1
                except ValueError:
                    servings = 1
                
                # Remaining columns are ingredients
                ingredients = [ing.strip() for ing in row[3:] if ing.strip()]
                recipe_text = "\n".join(ingredients)
                
                if not ingredients:
                    print(f"⚠️  Skipping row {row_num}: No ingredients found")
                    continue
                
                print(f"\n📝 Processing: {recipe_name}")
                
                try:
                    result = app.process_recipe(
                        recipe_name=recipe_name,
                        recipe_text=recipe_text,
                        description=description,
                        servings=servings
                    )
                    print(f"   ✓ Generated: {result['html_file']}")
                    
                except Exception as e:
                    print(f"   ❌ Error: {str(e)[:50]}")
        
        print("\n" + "="*60)
        print("✓ CSV processing complete!")
        print("Check 'output/' folder for generated labels")
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")


def load_from_json(json_file):
    """Load recipes from JSON file
    
    JSON Format:
    {
      "recipes": [
        {
          "name": "Recipe Name",
          "description": "Description",
          "servings": 4,
          "ingredients": [
            "200g Whole Wheat Flour",
            "100ml Water",
            "2g Salt"
          ]
        }
      ]
    }
    """
    
    app = NutritionLabelApp()
    
    print(f"\nLoading recipes from {json_file}...")
    print("="*60)
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        recipes = data.get('recipes', [])
        
        if not recipes:
            print("Error: No recipes found in JSON file!")
            return
        
        for recipe in recipes:
            recipe_name = recipe.get('name', 'Unnamed Recipe')
            description = recipe.get('description', '')
            servings = recipe.get('servings', 1)
            ingredients = recipe.get('ingredients', [])
            
            if not ingredients:
                print(f"⚠️  Skipping '{recipe_name}': No ingredients found")
                continue
            
            recipe_text = "\n".join(ingredients)
            
            print(f"\n📝 Processing: {recipe_name}")
            
            try:
                result = app.process_recipe(
                    recipe_name=recipe_name,
                    recipe_text=recipe_text,
                    description=description,
                    servings=servings
                )
                print(f"   ✓ Generated: {result['html_file']}")
                
            except Exception as e:
                print(f"   ❌ Error: {str(e)[:50]}")
        
        print("\n" + "="*60)
        print("✓ JSON processing complete!")
        print("Check 'output/' folder for generated labels")
        
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON file format!")
    except Exception as e:
        print(f"Error reading JSON: {str(e)}")


def create_sample_csv():
    """Create a sample CSV file for users"""
    
    csv_content = """Recipe Name,Description,Servings,Ingredient 1,Ingredient 2,Ingredient 3,Ingredient 4,Ingredient 5
Oatmeal Bowl,Healthy breakfast,2,100g Oats,200ml Whole Milk,50g Almonds,30g Honey,100g Carrot
Paneer Curry,Indian main course,4,250g Paneer,100g Tomato,50g Onion,20g Butter,10ml Sunflower Oil
Chickpea Salad,High protein salad,3,200g Chickpeas,100g Tomato,50g Onion,50g Carrot,10ml Olive Oil
Cheese Toast,Quick breakfast,2,100g White Bread,50g Cheddar Cheese,20g Butter,50g Tomato
Trail Mix,Energy snack,10,100g Almonds,100g Cashews,50g Peanuts,50g Honey,10g Jaggery"""
    
    file_path = Path(__file__).parent.parent / "sample_recipes.csv"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(csv_content)
    
    print(f"✓ Created: {file_path}")
    print("\nYou can now:")
    print("  1. Edit this CSV file with Excel or any text editor")
    print("  2. Run: python tools/recipe_input.py csv sample_recipes.csv")


def create_sample_json():
    """Create a sample JSON file for users"""
    
    json_data = {
        "recipes": [
            {
                "name": "Vegetable Biryani",
                "description": "Fragrant rice dish with vegetables",
                "servings": 4,
                "ingredients": [
                    "300g Rice Flour",
                    "200g Chickpeas",
                    "100g Tomato",
                    "50g Onion",
                    "3g Turmeric Powder",
                    "5g Red Chili Powder",
                    "10ml Sunflower Oil"
                ]
            },
            {
                "name": "Smoothie Bowl",
                "description": "Nutritious breakfast bowl",
                "servings": 2,
                "ingredients": [
                    "200ml Whole Milk",
                    "100g Yogurt (Plain)",
                    "50g Almonds",
                    "30g Honey",
                    "50g Spinach"
                ]
            }
        ]
    }
    
    file_path = Path(__file__).parent.parent / "sample_recipes.json"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Created: {file_path}")
    print("\nYou can now:")
    print("  1. Edit this JSON file with any text editor")
    print("  2. Run: python tools/recipe_input.py json sample_recipes.json")


def main():
    """Main menu"""
    
    print("\n" + "="*60)
    print("RECIPE INPUT TOOL - USER-FRIENDLY INTERFACE")
    print("="*60)
    print("\nChoose an option:")
    print("  1. Interactive input (step-by-step)")
    print("  2. Load from CSV file")
    print("  3. Load from JSON file")
    print("  4. Create sample CSV template")
    print("  5. Create sample JSON template")
    print("  6. Exit")
    
    choice = input("\nYour choice (1-6): ").strip()
    
    if choice == '1':
        interface = RecipeInputInterface()
        interface.interactive_recipe_input()
    
    elif choice == '2':
        csv_file = input("CSV file path (e.g., recipes.csv): ").strip()
        load_from_csv(csv_file)
    
    elif choice == '3':
        json_file = input("JSON file path (e.g., recipes.json): ").strip()
        load_from_json(json_file)
    
    elif choice == '4':
        create_sample_csv()
        print("\n✓ Template created! You can now edit it and use option 2 to load recipes.")
    
    elif choice == '5':
        create_sample_json()
        print("\n✓ Template created! You can now edit it and use option 3 to load recipes.")
    
    elif choice == '6':
        print("Goodbye!")
    
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command-line usage: python recipe_input.py csv file.csv
        command = sys.argv[1].lower()
        
        if command == 'csv' and len(sys.argv) > 2:
            load_from_csv(sys.argv[2])
        elif command == 'json' and len(sys.argv) > 2:
            load_from_json(sys.argv[2])
        elif command == 'interactive':
            interface = RecipeInputInterface()
            interface.interactive_recipe_input()
        else:
            print("Usage:")
            print("  Interactive: python recipe_input.py interactive")
            print("  CSV file:    python recipe_input.py csv recipes.csv")
            print("  JSON file:   python recipe_input.py json recipes.json")
    else:
        # Show menu
        main()
