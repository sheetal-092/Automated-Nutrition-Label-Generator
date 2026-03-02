-- Nutritional Database Schema for FSSAI-compliant Label Generator

-- Table for storing nutritional information of ingredients (per 100g)
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    energy_kcal REAL NOT NULL,
    protein_g REAL NOT NULL,
    total_fat_g REAL NOT NULL,
    saturated_fat_g REAL,
    trans_fat_g REAL,
    carbohydrates_g REAL NOT NULL,
    total_sugars_g REAL,
    added_sugars_g REAL,
    dietary_fiber_g REAL,
    sodium_mg REAL,
    cholesterol_mg REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing recipes
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    total_weight_g REAL NOT NULL,
    servings INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for recipe ingredients (many-to-many relationship)
CREATE TABLE IF NOT EXISTS recipe_ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    weight_g REAL NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (id) ON DELETE CASCADE
);

-- Table for storing generated labels
CREATE TABLE IF NOT EXISTS nutrition_labels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    label_data TEXT NOT NULL, -- JSON format
    fssai_compliant BOOLEAN DEFAULT 1,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id) ON DELETE CASCADE
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_ingredients_name ON ingredients(name);
CREATE INDEX IF NOT EXISTS idx_ingredients_category ON ingredients(category);
CREATE INDEX IF NOT EXISTS idx_recipe_ingredients_recipe ON recipe_ingredients(recipe_id);
CREATE INDEX IF NOT EXISTS idx_recipe_ingredients_ingredient ON recipe_ingredients(ingredient_id);
