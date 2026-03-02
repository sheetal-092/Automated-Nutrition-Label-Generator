# Ingredient Database Reference

## Quick Ingredient Lookup

### All Available Ingredients (30+ items)

---

## 🌾 GRAINS (4 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Whole Wheat Flour | 340 | 13.2 | 1.7 | 72.0 |
| Rice Flour | 366 | 6.0 | 1.4 | 80.0 |
| Oats | 389 | 16.9 | 6.9 | 66.3 |
| White Bread | 265 | 9.0 | 3.2 | 49.0 |

---

## 🥛 DAIRY (4 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Whole Milk | 61 | 3.2 | 3.3 | 4.8 |
| Cheddar Cheese | 403 | 24.9 | 33.1 | 1.3 |
| Yogurt (Plain) | 59 | 3.5 | 0.4 | 4.7 |
| Butter | 717 | 0.9 | 81.1 | 0.1 |

---

## 🥕 VEGETABLES (5 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Tomato | 18 | 0.9 | 0.2 | 3.9 |
| Onion | 40 | 1.1 | 0.1 | 9.3 |
| Potato | 77 | 2.0 | 0.1 | 17.5 |
| Spinach | 23 | 2.9 | 0.4 | 3.6 |
| Carrot | 41 | 0.9 | 0.2 | 9.6 |

---

## 🍗 PROTEINS (4 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Chicken Breast | 165 | 31.0 | 3.6 | 0.0 |
| Eggs | 155 | 12.6 | 10.6 | 1.1 |
| Chickpeas | 364 | 19.3 | 6.0 | 60.7 |
| Paneer | 265 | 18.3 | 20.8 | 1.2 |

---

## 🛢️ OILS (3 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Olive Oil | 884 | 0.0 | 100.0 | 0.0 |
| Sunflower Oil | 884 | 0.0 | 100.0 | 0.0 |
| Coconut Oil | 862 | 0.0 | 100.0 | 0.0 |

---

## 🍯 SWEETENERS (3 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| White Sugar | 387 | 0.0 | 0.0 | 100.0 |
| Honey | 304 | 0.3 | 0.0 | 82.4 |
| Jaggery | 383 | 0.4 | 0.1 | 98.0 |

---

## 🧂 CONDIMENTS (1 item)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Sodium (mg) |
|------------|-------------------|-------------|---------|-------------|
| Salt | 0 | 0.0 | 0.0 | 38758 |

---

## 🌶️ SPICES (2 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Turmeric Powder | 312 | 9.7 | 3.3 | 67.1 |
| Red Chili Powder | 282 | 13.5 | 14.3 | 54.7 |

---

## 🥜 NUTS (3 items)

| Ingredient | Energy (kcal/100g) | Protein (g) | Fat (g) | Carbs (g) |
|------------|-------------------|-------------|---------|-----------|
| Almonds | 579 | 21.2 | 49.9 | 21.6 |
| Cashews | 553 | 18.2 | 43.8 | 30.2 |
| Peanuts | 567 | 25.8 | 49.2 | 16.1 |

---

## 📊 Complete Nutrient Profiles

### High Protein Sources (>15g/100g)
1. Chicken Breast - 31.0g
2. Peanuts - 25.8g
3. Cheddar Cheese - 24.9g
4. Almonds - 21.2g
5. Chickpeas - 19.3g
6. Paneer - 18.3g
7. Cashews - 18.2g
8. Oats - 16.9g

### High Fiber Sources (>10g/100g)
1. Turmeric Powder - 22.7g
2. Red Chili Powder - 34.8g
3. Chickpeas - 17.4g
4. Almonds - 12.5g
5. Whole Wheat Flour - 12.2g

### Low Calorie Options (<100 kcal/100g)
1. Tomato - 18 kcal
2. Spinach - 23 kcal
3. Onion - 40 kcal
4. Carrot - 41 kcal
5. Yogurt (Plain) - 59 kcal
6. Whole Milk - 61 kcal
7. Potato - 77 kcal

### High Energy Dense (>500 kcal/100g)
1. Olive Oil - 884 kcal
2. Sunflower Oil - 884 kcal
3. Coconut Oil - 862 kcal
4. Butter - 717 kcal
5. Almonds - 579 kcal
6. Peanuts - 567 kcal
7. Cashews - 553 kcal

---

## 🔍 Usage in Recipes

### Exact Names Required

When writing recipes, use these **exact names** for automatic matching:

```
✅ CORRECT:
300g Whole Wheat Flour
100ml Whole Milk
50g Cheddar Cheese
200g Chickpeas

❌ INCORRECT:
300g wheat flour
100ml milk
50g cheese
200g chana
```

### Alternative: Use LLM Mapping

For flexible ingredient names, enable LLM:

```bash
python demo/run_demo.py --llm
```

This allows:
- "atta" → Whole Wheat Flour
- "dahi" → Yogurt (Plain)
- "aloo" → Potato
- "pyaaz" → Onion

---

## ➕ Adding Custom Ingredients

### Method 1: Via Code

```python
from main import NutritionLabelApp

app = NutritionLabelApp()
app.db.connect()

app.db.add_ingredient({
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

app.db.disconnect()
```

### Method 2: Via SQL

Edit `database/seed_data.sql` and add:

```sql
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, 
                         saturated_fat_g, trans_fat_g, carbohydrates_g, 
                         total_sugars_g, added_sugars_g, dietary_fiber_g, 
                         sodium_mg, cholesterol_mg)
VALUES ('Your Ingredient', 'Category', 100, 5.0, 2.0, 0.5, 0.0, 15.0, 
        1.0, 0.0, 3.0, 10, 0);
```

Then reinitialize the database.

---

## 🔎 Searching Ingredients

### By Name
```python
app.db.connect()
ingredient = app.db.get_ingredient_by_name("Oats")
print(f"{ingredient['name']}: {ingredient['energy_kcal']} kcal")
app.db.disconnect()
```

### By Category
```python
app.db.connect()
dairy = app.db.get_ingredients_by_category("Dairy")
for ing in dairy:
    print(f"{ing['name']}: {ing['protein_g']}g protein")
app.db.disconnect()
```

### Search Term
```python
app.db.connect()
results = app.db.search_ingredients("wheat")
for ing in results:
    print(ing['name'])
app.db.disconnect()
```

---

## 📚 Data Sources

All nutritional data is based on:

1. **USDA FoodData Central** - United States Department of Agriculture
2. **IFCT** - Indian Food Composition Tables
3. **FSSAI Guidelines** - Food Safety Standards Authority of India

Values are per 100g and represent typical/average values.

---

## ⚠️ Important Notes

1. **All values are per 100g** - The system automatically adjusts for recipe quantities
2. **Cooking methods affect nutrition** - Data represents raw/uncooked ingredients unless specified
3. **Brand variations exist** - Actual values may differ by brand/variety
4. **Commercial use** - Verify with certified nutritionist before using labels commercially

---

## 🆕 Requesting New Ingredients

To request addition of new ingredients to the database:

1. Provide ingredient name
2. Specify category
3. Include nutritional data source
4. Submit via issue or pull request

---

**Last Updated**: February 27, 2026  
**Total Ingredients**: 30+  
**Categories**: 9  
**Database Version**: 1.0
