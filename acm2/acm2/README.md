# Automated Nutrition Label Generator

A Python-based system that generates **FSSAI-compliant nutrition labels** for food products. This tool automates the creation of nutrition facts labels by mapping recipe ingredients to a nutritional database and calculating complete nutritional information.

## 🎯 Features

- **Automated Nutrition Calculation**: Calculates nutritional values from recipe ingredients and weights
- **FSSAI Compliance**: Validates labels against FSSAI 2020 regulations
- **Ingredient Mapping**: Intelligent ingredient matching using fuzzy search or LLM
- **Multiple Export Formats**: Generate labels in HTML, JSON formats
- **Comprehensive Database**: Pre-populated with 30+ common ingredients
- **Validation & Warnings**: Automatic compliance checks and health warnings
- **Batch Processing**: Process multiple recipes efficiently

## 🏗️ Tech Stack

- **Python 3.8+**: Core programming language
- **SQLite**: Nutritional database
- **LLM APIs** (Optional): OpenAI/Anthropic for intelligent ingredient mapping
- **HTML/CSS**: Label generation and visualization

## 📋 Requirements

```
Python 3.8 or higher
```

Optional dependencies for LLM features:
```
openai>=1.0.0
anthropic>=0.18.0
```

## 🚀 Quick Start

### Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up LLM API keys for intelligent ingredient mapping:
```bash
# For OpenAI
set OPENAI_API_KEY=your_api_key_here

# For Anthropic
set ANTHROPIC_API_KEY=your_api_key_here
```

### Basic Usage

Run the main demo:
```bash
python main.py
```

This will:
- Initialize the nutritional database
- Process a sample recipe (Whole Wheat Chapati)
- Generate FSSAI-compliant nutrition labels
- Create HTML and JSON output files

## 📖 Usage Examples

### Process Multiple Recipes

Run the comprehensive demo with all sample recipes:

```bash
python demo/run_demo.py
```

### Process a Specific Recipe

```bash
python demo/run_demo.py --recipe "Protein Chickpea Salad"
```

### Enable LLM-based Ingredient Mapping

```bash
python demo/run_demo.py --llm
```

### Programmatic Usage

```python
from main import NutritionLabelApp

# Initialize the application
app = NutritionLabelApp()

# Define your recipe
recipe_text = """
300g Whole Wheat Flour
150ml Water
2g Salt
10ml Sunflower Oil
"""

# Process the recipe
result = app.process_recipe(
    recipe_name="My Recipe",
    recipe_text=recipe_text,
    description="My delicious recipe",
    servings=4
)

# Access results
print(f"Energy per 100g: {result['nutrition_per_100g']['energy_kcal']} kcal")
print(f"FSSAI Compliant: {result['is_fssai_compliant']}")
```

## 📁 Project Structure

```
acm2/
├── database/
│   ├── schema.sql              # Database schema
│   └── seed_data.sql           # Sample nutritional data
├── src/
│   ├── database_manager.py     # Database operations
│   ├── recipe_parser.py        # Recipe parsing & nutrition calculation
│   ├── fssai_compliance.py     # FSSAI validation logic
│   ├── label_generator.py      # Label generation (HTML/JSON)
│   └── llm_mapper.py           # LLM-based ingredient mapping
├── demo/
│   └── run_demo.py             # Demo script with sample recipes
├── output/                     # Generated labels (created on first run)
├── main.py                     # Main application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── nutrition.db               # SQLite database (created on first run)
```

## 🗃️ Database Structure

The system uses SQLite with the following tables:

- **ingredients**: Nutritional data per 100g (30+ ingredients)
- **recipes**: Recipe metadata
- **recipe_ingredients**: Recipe-ingredient relationships
- **nutrition_labels**: Generated labels history

See [DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) for detailed schema information.

## ✅ FSSAI Compliance Features

The system ensures compliance with FSSAI 2020 regulations:

### Mandatory Nutrients on Labels
- Energy (kcal)
- Protein (g)
- Total Fat (g)
- Saturated Fat (g)
- Trans Fat (g)
- Carbohydrates (g)
- Total Sugars (g)
- Added Sugars (g)
- Sodium (mg)

### Automatic Validations
- Trans fat < 2% of total fat
- Proper rounding according to FSSAI guidelines
- Health warning thresholds
- Nutrient declaration requirements

### Health Warnings

The system automatically flags products that exceed FSSAI thresholds:
- High in Fat (>17.5g per 100g)
- High in Saturated Fat (>5.0g per 100g)
- High in Sugar (>22.5g per 100g)
- High in Salt/Sodium (>600mg per 100g)

## 📊 Sample Recipes Included

1. **Healthy Oatmeal Bowl** - Nutritious breakfast
2. **Paneer Butter Masala** - Indian curry
3. **Protein Chickpea Salad** - High-protein vegetarian
4. **Energy Trail Mix** - Nutrient-dense snack
5. **Classic Cheese Sandwich** - Quick meal

## 🎨 Output Formats

### HTML Label
- Professional nutrition facts table
- FSSAI-compliant formatting
- Print-ready design
- Includes ingredients list and manufacturer info

### JSON Data
- Complete nutritional breakdown
- Compliance status
- Warnings and recommendations
- Machine-readable format

## 🔧 Configuration

### Adding Custom Ingredients

Add ingredients directly to the database:

```python
app.db.connect()
app.db.add_ingredient({
    'name': 'Your Ingredient',
    'category': 'Category',
    'energy_kcal': 100,
    'protein_g': 5.0,
    'total_fat_g': 2.0,
    # ... other nutrients
})
app.db.disconnect()
```

### Customizing Labels

Modify `src/label_generator.py` to customize:
- Label design and styling
- Manufacturer information
- Additional declarations
- Export formats

## 🤖 LLM Integration

The system supports LLM-based ingredient mapping for better accuracy:

**Supported Providers:**
- OpenAI (GPT-3.5/4)
- Anthropic (Claude)

**Benefits:**
- Handles regional ingredient names
- Understands cooking terminology
- Better synonym matching
- Generates estimates for missing ingredients

## 📈 Use Cases

- **Food Startups**: Generate labels for new products
- **Home Bakers**: Create professional labels for home-made products
- **Restaurants**: Nutritional information for menu items
- **Food Manufacturers**: Rapid prototyping of product labels
- **Nutritionists**: Calculate nutritional content of recipes
- **Compliance Teams**: Validate FSSAI compliance

## 🔍 Validation Process

1. **Ingredient Parsing**: Extract ingredients and quantities
2. **Database Mapping**: Match to nutritional database
3. **Calculation**: Compute total nutrition per 100g and per serving
4. **FSSAI Validation**: Check compliance against regulations
5. **Label Generation**: Create formatted labels
6. **Export**: Save as HTML and JSON

## ⚠️ Limitations

- Nutritional data is based on standard databases (USDA, IFCT)
- Actual values may vary based on specific brands/varieties
- Cooking methods may alter nutritional content
- Labels should be verified by certified nutritionists for commercial use

## 🤝 Contributing

To add more ingredients to the database:
1. Edit `database/seed_data.sql`
2. Re-run the database initialization
3. Follow FSSAI nutritional data standards

## 📄 License

This project is provided as-is for educational and commercial use.

## 🆘 Support

For issues or questions:
1. Check the documentation in `docs/`
2. Review sample recipes in `demo/run_demo.py`
3. Examine the database schema in `database/schema.sql`

## 🎓 FSSAI Resources

- [FSSAI Official Website](https://www.fssai.gov.in/)
- [Food Safety and Standards (Packaging and Labelling) Regulations, 2011](https://www.fssai.gov.in/cms/food-safety-and-standards-regulations.php)
- [FSSAI Nutritional Labeling Guidelines](https://www.fssai.gov.in/)

## 🏆 Credits

Built with:
- Nutritional data from USDA and IFCT databases
- FSSAI 2020 regulations compliance
- Modern Python best practices

---

**Made for food startups, manufacturers, and entrepreneurs to simplify nutrition labeling** 🥗
