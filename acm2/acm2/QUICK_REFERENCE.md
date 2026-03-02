# Quick Reference Guide

## 🚀 Quick Start Commands

### Run Demo
```bash
# All recipes
python demo/run_demo.py

# Specific recipe
python demo/run_demo.py --recipe "Paneer Butter Masala"

# With LLM support
python demo/run_demo.py --llm
```

### Basic Usage
```bash
python main.py
```

---

## 📝 Recipe Format

```text
<quantity><unit> <ingredient_name>

Examples:
300g Whole Wheat Flour
2 cups Oats
1 tbsp Salt
150ml Whole Milk
```

### Supported Units
- **Weight**: g, kg, grams, kilograms
- **Volume**: ml, l, liters
- **US Volume**: cup, tbsp, tsp, tablespoon, teaspoon

---

## 🐍 Python API

```python
from main import NutritionLabelApp

# Initialize
app = NutritionLabelApp()

# Process recipe
result = app.process_recipe(
    recipe_name="My Recipe",
    recipe_text="""
    300g Whole Wheat Flour
    150ml Water
    """,
    description="Description",
    servings=4
)

# Access results
print(result['nutrition_per_100g'])
print(result['is_fssai_compliant'])
print(result['html_file'])
```

---

## 📊 FSSAI Thresholds

| Nutrient | Low | High |
|----------|-----|------|
| Fat | ≤3g | >17.5g |
| Saturated Fat | - | >5g |
| Sugar | ≤5g | >22.5g |
| Sodium | ≤120mg | >600mg |

**Trans Fat**: Must be <2% of total fat

---

## 🗂️ File Structure

```
acm2/
├── main.py              # Main application
├── demo/
│   └── run_demo.py      # Demo script
├── src/
│   ├── database_manager.py
│   ├── recipe_parser.py
│   ├── fssai_compliance.py
│   ├── label_generator.py
│   └── llm_mapper.py
├── database/
│   ├── schema.sql
│   └── seed_data.sql
├── docs/                # Documentation
├── output/              # Generated labels
└── nutrition.db         # SQLite database
```

---

## 🔧 Common Tasks

### Add Ingredient
```python
app.db.connect()
app.db.add_ingredient({
    'name': 'Quinoa',
    'category': 'Grains',
    'energy_kcal': 368,
    'protein_g': 14.1,
    'total_fat_g': 6.1,
    'saturated_fat_g': 0.7,
    'trans_fat_g': 0.0,
    'carbohydrates_g': 64.2,
    'total_sugars_g': 0.0,
    'added_sugars_g': 0.0,
    'dietary_fiber_g': 7.0,
    'sodium_mg': 5,
    'cholesterol_mg': 0
})
app.db.disconnect()
```

### Search Ingredients
```python
app.db.connect()
results = app.db.search_ingredients("wheat")
for ing in results:
    print(f"{ing['name']}: {ing['energy_kcal']} kcal")
app.db.disconnect()
```

### View All Ingredients
```python
app.db.connect()
all_ingredients = app.db.get_all_ingredients()
for ing in all_ingredients:
    print(f"{ing['category']}: {ing['name']}")
app.db.disconnect()
```

---

## 🏷️ Output Files

### HTML Label
- Professional nutrition facts table
- FSSAI-compliant format
- Print-ready
- Open in any browser

### JSON Data
```json
{
  "product_name": "Recipe Name",
  "nutrition_per_100g": {
    "energy_kcal": 224,
    "protein_g": 8.6,
    ...
  },
  "fssai_compliant": true
}
```

---

## ⚠️ Troubleshooting

### Ingredient Not Found
- Check spelling
- Use common names
- Enable LLM: `--llm`
- Add custom ingredient

### Parse Error
Use format: `<quantity><unit> <name>`
```
❌ wheat flour 300g
✅ 300g Whole Wheat Flour
```

### Database Locked
Close all connections:
```python
app.db.disconnect()
```

---

## 📚 Resources

- **Full Documentation**: `docs/USER_GUIDE.md`
- **Database Info**: `docs/DATABASE_DOCUMENTATION.md`
- **Sample Code**: `demo/run_demo.py`
- **FSSAI**: https://www.fssai.gov.in/

---

## 🎯 30+ Pre-loaded Ingredients

**Grains**: Whole Wheat Flour, Rice Flour, Oats, White Bread
**Dairy**: Whole Milk, Cheddar Cheese, Yogurt, Butter
**Vegetables**: Tomato, Onion, Potato, Spinach, Carrot
**Proteins**: Chicken Breast, Eggs, Chickpeas, Paneer
**Oils**: Olive Oil, Sunflower Oil, Coconut Oil
**Sweeteners**: Sugar, Honey, Jaggery
**Nuts**: Almonds, Cashews, Peanuts
**Spices**: Turmeric, Red Chili, Salt

---

**Made with ❤️ for Food Entrepreneurs**
