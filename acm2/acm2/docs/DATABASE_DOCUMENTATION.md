# Database Documentation

## Automated Nutrition Label Generator - Database Schema

### Overview

The nutrition label generator uses SQLite database to store:
- Nutritional information for ingredients
- Recipe definitions
- Generated nutrition labels
- Ingredient-recipe relationships

### Database File

- **Location**: `nutrition.db` (root directory)
- **Type**: SQLite 3
- **Auto-created**: Yes, on first run
- **Character Set**: UTF-8

---

## Table Schemas

### 1. ingredients

Stores nutritional information for food ingredients (per 100g serving).

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique ingredient ID |
| name | TEXT | NOT NULL, UNIQUE | Ingredient name |
| category | TEXT | NOT NULL | Food category (Grains, Dairy, Protein, etc.) |
| energy_kcal | REAL | NOT NULL | Energy in kilocalories |
| protein_g | REAL | NOT NULL | Protein in grams |
| total_fat_g | REAL | NOT NULL | Total fat in grams |
| saturated_fat_g | REAL | NULL | Saturated fat in grams |
| trans_fat_g | REAL | NULL | Trans fat in grams |
| carbohydrates_g | REAL | NOT NULL | Total carbohydrates in grams |
| total_sugars_g | REAL | NULL | Total sugars in grams |
| added_sugars_g | REAL | NULL | Added sugars in grams |
| dietary_fiber_g | REAL | NULL | Dietary fiber in grams |
| sodium_mg | REAL | NULL | Sodium in milligrams |
| cholesterol_mg | REAL | NULL | Cholesterol in milligrams |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Last update time |

**Indexes:**
- `idx_ingredients_name` on `name`
- `idx_ingredients_category` on `category`

**Sample Data:**

```sql
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, 
                         saturated_fat_g, trans_fat_g, carbohydrates_g, 
                         total_sugars_g, added_sugars_g, dietary_fiber_g, 
                         sodium_mg, cholesterol_mg)
VALUES ('Whole Wheat Flour', 'Grains', 340, 13.2, 1.7, 0.3, 0.0, 72.0, 
        0.4, 0.0, 12.2, 2, 0);
```

**Categories:**
- Grains
- Dairy
- Vegetables
- Protein
- Oils
- Sweeteners
- Condiments
- Spices
- Nuts

---

### 2. recipes

Stores recipe metadata and information.

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique recipe ID |
| name | TEXT | NOT NULL | Recipe name |
| description | TEXT | NULL | Recipe description |
| total_weight_g | REAL | NOT NULL | Total weight in grams |
| servings | INTEGER | DEFAULT 1 | Number of servings |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Creation time |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Last update time |

**Sample Data:**

```sql
INSERT INTO recipes (name, description, total_weight_g, servings)
VALUES ('Whole Wheat Chapati', 'Traditional Indian flatbread', 462, 6);
```

---

### 3. recipe_ingredients

Junction table linking recipes to ingredients with quantities.

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique record ID |
| recipe_id | INTEGER | NOT NULL, FOREIGN KEY | References recipes(id) |
| ingredient_id | INTEGER | NOT NULL, FOREIGN KEY | References ingredients(id) |
| weight_g | REAL | NOT NULL | Ingredient weight in grams |

**Foreign Keys:**
- `recipe_id` → `recipes(id)` ON DELETE CASCADE
- `ingredient_id` → `ingredients(id)` ON DELETE CASCADE

**Indexes:**
- `idx_recipe_ingredients_recipe` on `recipe_id`
- `idx_recipe_ingredients_ingredient` on `ingredient_id`

**Sample Data:**

```sql
INSERT INTO recipe_ingredients (recipe_id, ingredient_id, weight_g)
VALUES (1, 1, 300.0);  -- 300g of Whole Wheat Flour for recipe 1
```

---

### 4. nutrition_labels

Stores generated nutrition labels with compliance information.

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique label ID |
| recipe_id | INTEGER | NOT NULL, FOREIGN KEY | References recipes(id) |
| label_data | TEXT | NOT NULL | JSON-formatted label data |
| fssai_compliant | BOOLEAN | DEFAULT 1 | FSSAI compliance status |
| generated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Generation time |

**Foreign Keys:**
- `recipe_id` → `recipes(id)` ON DELETE CASCADE

**Sample label_data JSON:**

```json
{
  "product_name": "Whole Wheat Chapati",
  "generated_at": "2026-02-27T10:30:00",
  "nutrition_per_100g": {
    "energy_kcal": 224,
    "protein_g": 8.6,
    "total_fat_g": 2.6,
    "saturated_fat_g": 0.3,
    "trans_fat_g": 0.0,
    "carbohydrates_g": 46.8,
    "total_sugars_g": 0.3,
    "added_sugars_g": 0.0,
    "dietary_fiber_g": 7.9,
    "sodium_mg": 863.6,
    "cholesterol_mg": 0.0
  },
  "fssai_compliant": true,
  "compliance_version": "FSSAI 2020"
}
```

---

## Nutritional Data Standards

### Units of Measurement

All nutritional values in the `ingredients` table are **per 100g**:

- **Energy**: kilocalories (kcal)
- **Macronutrients**: grams (g)
  - Protein
  - Total Fat
  - Saturated Fat
  - Trans Fat
  - Carbohydrates
  - Sugars
  - Fiber
- **Micronutrients**: milligrams (mg)
  - Sodium
  - Cholesterol

### Data Sources

Nutritional data is based on:
1. **USDA FoodData Central** - United States Department of Agriculture
2. **IFCT** - Indian Food Composition Tables
3. **FSSAI Guidelines** - Food Safety and Standards Authority of India

### FSSAI Compliance Requirements

#### Mandatory Nutrients (Must be on label)

1. Energy (kcal)
2. Protein (g)
3. Total Fat (g)
4. Saturated Fat (g)
5. Trans Fat (g)
6. Carbohydrates (g)
7. Total Sugars (g)
8. Sodium (mg)

#### Optional but Recommended

1. Added Sugars (g)
2. Dietary Fiber (g)
3. Cholesterol (mg)

#### Health Warning Thresholds

Per 100g of product:

| Nutrient | Low | High | Required Declaration |
|----------|-----|------|---------------------|
| Total Fat | ≤3g | >17.5g | "High in Fat" |
| Saturated Fat | - | >5g | "High in Saturated Fat" |
| Total Sugars | ≤5g | >22.5g | "High in Sugar" |
| Sodium | ≤120mg | >600mg | "High in Salt/Sodium" |
| Trans Fat | - | <2% of fat | Must be <2% total fat |

---

## Database Operations

### Initialization

```python
from src.database_manager import DatabaseManager

db = DatabaseManager("nutrition.db")
db.initialize_database("database/schema.sql", "database/seed_data.sql")
```

### Adding Ingredients

```python
db.connect()
ingredient_id = db.add_ingredient({
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
db.disconnect()
```

### Querying Ingredients

```python
db.connect()

# Get specific ingredient
ingredient = db.get_ingredient_by_name("Whole Wheat Flour")

# Search ingredients
results = db.search_ingredients("wheat")

# Get by category
dairy_products = db.get_ingredients_by_category("Dairy")

db.disconnect()
```

### Creating Recipes

```python
db.connect()

# Create recipe
recipe_id = db.create_recipe(
    name="My Recipe",
    description="Delicious dish",
    total_weight_g=500,
    servings=4
)

# Add ingredients to recipe
db.add_recipe_ingredient(recipe_id, ingredient_id=1, weight_g=200)
db.add_recipe_ingredient(recipe_id, ingredient_id=5, weight_g=100)

# Get recipe with ingredients
recipe_data = db.get_recipe(recipe_id)
ingredients = db.get_recipe_ingredients(recipe_id)

db.disconnect()
```

---

## Pre-loaded Ingredients

The database comes with **30+ ingredients** across 9 categories:

### Grains (4 items)
- Whole Wheat Flour
- Rice Flour
- Oats
- White Bread

### Dairy (4 items)
- Whole Milk
- Cheddar Cheese
- Yogurt (Plain)
- Butter

### Vegetables (5 items)
- Tomato
- Onion
- Potato
- Spinach
- Carrot

### Proteins (4 items)
- Chicken Breast
- Eggs
- Chickpeas
- Paneer

### Oils (3 items)
- Olive Oil
- Sunflower Oil
- Coconut Oil

### Sweeteners (3 items)
- White Sugar
- Honey
- Jaggery

### Condiments (1 item)
- Salt

### Spices (2 items)
- Turmeric Powder
- Red Chili Powder

### Nuts (3 items)
- Almonds
- Cashews
- Peanuts

---

## Database Maintenance

### Backup

```bash
# Windows PowerShell
Copy-Item nutrition.db nutrition_backup.db
```

### Reset Database

Delete `nutrition.db` file and run the application again to recreate.

### Update Ingredient

```python
db.connect()
db.cursor.execute("""
    UPDATE ingredients 
    SET protein_g = 14.0, updated_at = CURRENT_TIMESTAMP
    WHERE name = 'Whole Wheat Flour'
""")
db.conn.commit()
db.disconnect()
```

---

## FSSAI Rounding Rules

Applied automatically by the system:

1. **Energy**: Round to nearest 1 kcal
2. **Protein, Fat, Carbs**:
   - If < 10g: Round to 0.1g
   - If ≥ 10g: Round to 1g
3. **Sodium, Cholesterol**: Round to nearest mg
4. **Trans Fat**: Can be declared as "0" if < 0.2g per serving

---

## API Reference

See `src/database_manager.py` for complete API documentation.

Key methods:
- `initialize_database(schema_file, seed_file)`
- `get_ingredient_by_name(name)`
- `search_ingredients(search_term)`
- `add_ingredient(ingredient_data)`
- `create_recipe(name, description, total_weight_g, servings)`
- `add_recipe_ingredient(recipe_id, ingredient_id, weight_g)`
- `get_recipe_ingredients(recipe_id)`
- `save_nutrition_label(recipe_id, label_data, fssai_compliant)`

---

## Performance

- Database size: ~50 KB with seed data
- Query performance: <1ms for single ingredient lookup
- Supports 1000s of recipes and ingredients
- Indexes optimize common queries

---

## Future Enhancements

Potential additions to the database:

1. **Vitamins & Minerals**: Vitamin A, C, D, Iron, Calcium
2. **Allergen Information**: Common allergens tracking
3. **Product Categories**: Separate table for FSSAI categories
4. **Batch Tracking**: Manufacturing batch information
5. **Shelf Life**: Storage and expiry information
6. **Regional Data**: Multiple regional name mappings

---

**Last Updated**: February 27, 2026
**Database Version**: 1.0
**FSSAI Compliance**: 2020 Regulations
