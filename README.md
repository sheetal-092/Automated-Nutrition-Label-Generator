🏷️ Automated Nutrition Label Generator

A Python-based system that generates FSSAI-compliant nutrition labels for food products.

This tool automates the creation of nutrition facts labels by mapping recipe ingredients to a nutritional database and calculating complete nutritional information.

🎯 Features

✅ Automated Nutrition Calculation (from recipe ingredients & weights)

✅ FSSAI 2020 Compliance Validation

✅ Intelligent Ingredient Mapping (Fuzzy Search / LLM-based)

✅ Multiple Export Formats (HTML & JSON)

✅ Pre-populated Database (30+ ingredients)

✅ Compliance Warnings & Health Flags

✅ Batch Processing Support

🏗️ Tech Stack

Python 3.8+

SQLite (Nutrition Database)

HTML/CSS (Label Design)

OpenAI / Anthropic APIs (Optional) – Intelligent Mapping

📋 Requirements

Python 3.8 or higher

Optional (for LLM features):

openai>=1.0.0
anthropic>=0.18.0

💻 Programmatic Usage

from main import NutritionLabelApp

# Initialize the app
app = NutritionLabelApp()

recipe_text = """
300g Whole Wheat Flour
150ml Water
2g Salt
10ml Sunflower Oil
"""

result = app.process_recipe(
    recipe_name="My Recipe",
    recipe_text=recipe_text,
    description="My delicious recipe",
    servings=4
)

print(f"Energy per 100g: {result['nutrition_per_100g']['energy_kcal']} kcal")
print(f"FSSAI Compliant: {result['is_fssai_compliant']}")


📁 Project Structure
acm2/
│
├── database/
│   ├── schema.sql
│   └── seed_data.sql
│
├── src/
│   ├── database_manager.py
│   ├── recipe_parser.py
│   ├── fssai_compliance.py
│   ├── label_generator.py
│   └── llm_mapper.py
│
├── demo/
│   └── run_demo.py
│
├── output/
├── main.py
├── requirements.txt
├── README.md
└── nutrition.db

🗃️ Database Structure

The SQLite database contains:

ingredients → Nutritional data per 100g

recipes → Recipe metadata

recipe_ingredients → Recipe-ingredient relationships

nutrition_labels → Generated label history

✅ FSSAI Compliance Features

Ensures compliance with FSSAI 2020 Regulations

Mandatory Nutrients

Energy (kcal)

Protein (g)

Total Fat (g)

Saturated Fat (g)

Trans Fat (g)

Carbohydrates (g)

Total Sugars (g)

Added Sugars (g)

Sodium (mg)

Automatic Validations

Trans fat < 2% of total fat

Proper rounding as per FSSAI norms

Nutrient declaration validation

Threshold-based warnings

📊 Sample Recipes Included

Healthy Oatmeal Bowl

Paneer Butter Masala

Protein Chickpea Salad

Energy Trail Mix

Classic Cheese Sandwich

🎨 Output Formats
🧾 HTML Label

Professional nutrition table

FSSAI-compliant formatting

Print-ready design

Ingredients & manufacturer info included

📦 JSON Output

Complete nutritional breakdown

Compliance status

Warnings and recommendations

Machine-readable format

🤖 LLM Integration

Supported Providers:

OpenAI (GPT-3.5 / GPT-4)

Anthropic (Claude)

Benefits:

Regional ingredient recognition

Cooking terminology understanding

Synonym matching

Nutritional estimation for missing ingredients

📈 Use Cases

Food Startups

Home Bakers

Restaurants

Food Manufacturers

Nutritionists

Compliance Teams

🔍 Validation Workflow

Ingredient Parsing

Database Mapping

Nutrition Calculation

FSSAI Compliance Check

Label Generation

Export (HTML/JSON)

⚠️ Limitations

Based on standard nutrition databases (USDA, IFCT)

Brand-specific variations not included

Cooking method changes not fully modeled

Commercial use should be verified by certified nutritionists

🤝 Contributing

To add more ingredients:

Edit database/seed_data.sql

Re-run database initialization

Follow FSSAI data standards

📄 License

This project is open for educational and commercial use.

🏆 Credits

Nutritional Data: USDA & IFCT Databases

FSSAI 2020 Labeling Guidelines

Built using Modern Python Best Practices

