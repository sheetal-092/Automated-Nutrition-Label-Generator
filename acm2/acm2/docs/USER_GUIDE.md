# User Guide - Nutrition Label Generator

## Getting Started

### Installation

1. **Verify Python Installation**
   ```bash
   python --version
   # Should show Python 3.8 or higher
   ```

2. **Install Dependencies** (Optional)
   ```bash
   pip install -r requirements.txt
   ```
   Note: Core functionality works without external dependencies!

3. **Test Installation**
   ```bash
   python main.py
   ```

---

## Basic Usage

### Method 1: Quick Start (Single Recipe)

```bash
python main.py
```

This runs the default example (Whole Wheat Chapati) and generates:
- `output/Whole_Wheat_Chapati_label.html` - Viewable nutrition label
- `output/Whole_Wheat_Chapati_data.json` - Machine-readable data

### Method 2: Run All Demos

```bash
python demo/run_demo.py
```

Processes 5 sample recipes and generates labels for all.

### Method 3: Process Specific Recipe

```bash
python demo/run_demo.py --recipe "Paneer Butter Masala"
```

Available recipes:
- Healthy Oatmeal Bowl
- Paneer Butter Masala
- Protein Chickpea Salad
- Energy Trail Mix
- Classic Cheese Sandwich

---

## Creating Your Own Recipe

### Step 1: Write Your Recipe

Create a text file or string with ingredients (one per line):

```
Ingredient Format: <quantity> <unit> <ingredient_name>
```

**Example:**
```text
300g Whole Wheat Flour
150ml Water
2g Salt
10ml Sunflower Oil
```

**Supported Units:**
- Weight: `g`, `kg`, `grams`, `kilograms`
- Volume: `ml`, `l`, `liters` (converted to weight for liquids)
- Volume (US): `cup`, `tbsp`, `tsp`, `tablespoon`, `teaspoon`

### Step 2: Use the API

```python
from main import NutritionLabelApp

# Initialize
app = NutritionLabelApp()

# Your recipe
recipe_text = """
300g Whole Wheat Flour
150ml Water
2g Salt
10ml Sunflower Oil
"""

# Process
result = app.process_recipe(
    recipe_name="My Custom Recipe",
    recipe_text=recipe_text,
    description="Description of my recipe",
    servings=4  # Number of servings
)

# Results
print(f"Label file: {result['html_file']}")
print(f"FSSAI Compliant: {result['is_fssai_compliant']}")
```

---

## Understanding the Output

### HTML Label

Open `output/YourRecipe_label.html` in any web browser to see:

1. **Nutrition Facts Header** - Standard FSSAI format
2. **Per 100g Values** - All mandatory nutrients
3. **Serving Information** - Per serving breakdown
4. **Ingredients List** - Ordered by weight
5. **Manufacturer Info** - Customizable section
6. **FSSAI License** - Placeholder for your license number

### JSON Data

```json
{
  "product_name": "Recipe Name",
  "generated_at": "2026-02-27T10:30:00",
  "nutrition_per_100g": {
    "energy_kcal": 224,
    "protein_g": 8.6,
    "total_fat_g": 2.6,
    ...
  },
  "fssai_compliant": true,
  "compliance_warnings": []
}
```

### Compliance Report

Printed to console:

```
============================================================
FSSAI COMPLIANCE REPORT
============================================================
Compliance Status: ✓ COMPLIANT

WARNINGS (Recommended):
  ⚠ High sodium content (863.6mg per 100g). Consider adding...

REQUIRED DECLARATIONS:
  • Required: 'High in Salt/Sodium' declaration
============================================================
```

---

## Advanced Features

### 1. Adding Custom Ingredients

If an ingredient is not in the database:

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

### 2. Using LLM for Ingredient Mapping

**Setup:**
```bash
# Set API key
set OPENAI_API_KEY=sk-your-key-here
```

**Usage:**
```python
app = NutritionLabelApp(use_llm=True)
```

Benefits:
- Handles regional names (e.g., "atta" → "Whole Wheat Flour")
- Understands synonyms (e.g., "dahi" → "Yogurt")
- Better ingredient matching

### 3. Customizing Labels

Edit `src/label_generator.py` to modify:

**Change Manufacturer Info:**
```python
manufacturer_info={
    "name": "Your Company Pvt Ltd",
    "address": "123 Food Street, City, State - 123456",
    "contact": "+91-XXXXXXXXXX | email@company.com"
}
```

**Add FSSAI License:**
```python
fssai_license="12345678901234"
```

**Modify Styling:**
Edit the `<style>` section in `generate_html_label()` method.

### 4. Batch Processing

Process multiple recipes:

```python
recipes = [
    {"name": "Recipe 1", "text": "...", "servings": 4},
    {"name": "Recipe 2", "text": "...", "servings": 6},
]

for recipe in recipes:
    result = app.process_recipe(
        recipe_name=recipe["name"],
        recipe_text=recipe["text"],
        servings=recipe["servings"]
    )
```

---

## FSSAI Compliance Guide

### Mandatory Requirements

✅ **Must Include on Label:**
1. Energy (kcal)
2. Protein (g)
3. Total Fat (g)
4. Saturated Fat (g)
5. Trans Fat (g)
6. Carbohydrates (g)
7. Total Sugars (g)
8. Sodium (mg)

✅ **Additional (Recommended):**
9. Added Sugars (g)
10. Dietary Fiber (g)
11. Cholesterol (mg)

### Health Warnings

The system automatically checks:

| Threshold | Declaration Required |
|-----------|---------------------|
| Fat > 17.5g/100g | "High in Fat" |
| Saturated Fat > 5g/100g | "High in Saturated Fat" |
| Sugar > 22.5g/100g | "High in Sugar" |
| Sodium > 600mg/100g | "High in Salt/Sodium" |
| Trans Fat > 2% of total fat | Non-compliant |

### Rounding Rules (Auto-applied)

- **Energy**: Nearest 1 kcal
- **Nutrients < 10g**: 0.1g precision
- **Nutrients ≥ 10g**: 1g precision
- **Trans Fat < 0.2g**: Can be labeled as "0g"

---

## Troubleshooting

### Issue: Ingredient Not Found

**Problem:**
```
Warning: Could not find 'xyz' in database
```

**Solutions:**
1. Check spelling
2. Use common name (e.g., "Tomato" not "Tamatar")
3. Enable LLM mapping for better matching
4. Add custom ingredient to database

### Issue: Parser Error

**Problem:**
```
ValueError: Could not parse ingredient line: ...
```

**Solution:**
Ensure correct format:
```
❌ wheat flour 300g
✅ 300g Whole Wheat Flour

❌ 2 cups rice
✅ 2 cups Rice Flour
```

### Issue: Non-Compliant Label

**Problem:**
```
Compliance Status: ✗ NON-COMPLIANT
ERRORS: Trans fat exceeds 2% of total fat
```

**Solution:**
- Review recipe formulation
- Check ingredient nutritional data
- Consider reformulation to reduce trans fat

### Issue: Database Locked

**Problem:**
```
sqlite3.OperationalError: database is locked
```

**Solution:**
Ensure only one instance is accessing the database. Close other connections:
```python
app.db.disconnect()
```

---

## Best Practices

### 1. Recipe Writing

✅ **DO:**
- Use consistent units
- List ingredients in descending order by weight
- Use specific names ("Whole Wheat Flour" not "Flour")

❌ **DON'T:**
- Mix units without context
- Use vague terms ("some salt")
- Omit quantities

### 2. Nutrition Accuracy

✅ **DO:**
- Use standardized ingredient names from database
- Verify total weight matches sum of ingredients
- Review compliance warnings

❌ **DON'T:**
- Ignore FSSAI warnings
- Use estimated weights for commercial products
- Skip ingredient verification

### 3. Label Usage

✅ **DO:**
- Get labels certified by nutritionist for commercial use
- Update labels if recipe changes
- Include all required FSSAI declarations

❌ **DON'T:**
- Use for final product labels without verification
- Ignore health warning thresholds
- Forget to add manufacturer information

---

## Examples Gallery

### Example 1: Simple Snack

```python
recipe = """
100g Almonds
50g Honey
"""

result = app.process_recipe(
    recipe_name="Honey Roasted Almonds",
    recipe_text=recipe,
    servings=5
)
```

**Output:**
- Energy: 516 kcal/100g
- High in Fat (warning)
- High in Sugar (warning)

### Example 2: Balanced Meal

```python
recipe = """
200g Chickpeas
100g Tomato
50g Onion
10ml Olive Oil
3g Salt
5g Turmeric Powder
"""

result = app.process_recipe(
    recipe_name="Chickpea Curry",
    recipe_text=recipe,
    servings=3
)
```

**Output:**
- Energy: 206 kcal/100g
- Good protein source
- FSSAI Compliant

### Example 3: Breakfast Bowl

```python
recipe = """
100g Oats
200ml Whole Milk
30g Honey
50g Almonds
"""

result = app.process_recipe(
    recipe_name="Power Breakfast",
    recipe_text=recipe,
    servings=2
)
```

**Output:**
- Energy: 266 kcal/100g
- Balanced macros
- Minor warnings on fat content

---

## API Reference

### NutritionLabelApp

**Constructor:**
```python
app = NutritionLabelApp(
    db_path="nutrition.db",  # Database file path
    use_llm=False            # Enable LLM mapping
)
```

**Main Method:**
```python
result = app.process_recipe(
    recipe_name: str,         # Recipe name
    recipe_text: str,         # Ingredients (one per line)
    description: str = "",    # Recipe description
    servings: int = 1         # Number of servings
)
```

**Returns:**
```python
{
    'recipe_id': int,                      # Database ID
    'label_id': int,                       # Label ID
    'total_weight_g': float,               # Total recipe weight
    'nutrition_per_100g': dict,            # Nutrients per 100g
    'nutrition_per_serving': dict,         # Nutrients per serving
    'is_fssai_compliant': bool,           # Compliance status
    'warnings': list,                      # Compliance warnings
    'errors': list,                        # Compliance errors
    'html_file': str,                      # Path to HTML label
    'json_file': str                       # Path to JSON data
}
```

---

## FAQ

**Q: Can I use this for commercial products?**
A: The system generates FSSAI-compliant labels, but you should have them verified by a certified nutritionist before using on commercial products.

**Q: How accurate are the nutritional values?**
A: Based on standard USDA and IFCT databases. Actual values may vary based on specific ingredients and cooking methods.

**Q: Can I add my own ingredient database?**
A: Yes! Add ingredients via the database API or edit `database/seed_data.sql`.

**Q: Does this work for packaged foods?**
A: Yes, any food product with a defined recipe can use this system.

**Q: What if my ingredient has regional names?**
A: Use LLM mapping (--llm flag) or add custom mappings to the database.

**Q: Can I export to PDF?**
A: HTML labels can be printed to PDF using any browser's print function.

---

## Support & Resources

- **Documentation**: See `docs/` folder
- **Sample Code**: Check `demo/run_demo.py`
- **Database Reference**: Read `docs/DATABASE_DOCUMENTATION.md`
- **FSSAI Guidelines**: Visit https://www.fssai.gov.in/

---

**Happy Label Generating! 🏷️**
