-- Sample Nutritional Data (per 100g) - Based on USDA and IFCT databases

-- Grains and Cereals
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Whole Wheat Flour', 'Grains', 340, 13.2, 1.7, 0.3, 0.0, 72.0, 0.4, 0.0, 12.2, 2, 0),
('Rice Flour', 'Grains', 366, 6.0, 1.4, 0.4, 0.0, 80.0, 0.1, 0.0, 2.4, 0, 0),
('Oats', 'Grains', 389, 16.9, 6.9, 1.2, 0.0, 66.3, 0.0, 0.0, 10.6, 2, 0),
('White Bread', 'Grains', 265, 9.0, 3.2, 0.7, 0.1, 49.0, 5.0, 3.0, 2.7, 491, 0);

-- Dairy Products
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Whole Milk', 'Dairy', 61, 3.2, 3.3, 1.9, 0.1, 4.8, 5.1, 0.0, 0.0, 44, 10),
('Cheddar Cheese', 'Dairy', 403, 24.9, 33.1, 21.1, 0.9, 1.3, 0.5, 0.0, 0.0, 621, 105),
('Yogurt (Plain)', 'Dairy', 59, 3.5, 0.4, 0.3, 0.0, 4.7, 4.7, 0.0, 0.0, 46, 5),
('Butter', 'Dairy', 717, 0.9, 81.1, 51.4, 3.3, 0.1, 0.1, 0.0, 0.0, 11, 215);

-- Vegetables
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Tomato', 'Vegetables', 18, 0.9, 0.2, 0.0, 0.0, 3.9, 2.6, 0.0, 1.2, 5, 0),
('Onion', 'Vegetables', 40, 1.1, 0.1, 0.0, 0.0, 9.3, 4.2, 0.0, 1.7, 4, 0),
('Potato', 'Vegetables', 77, 2.0, 0.1, 0.0, 0.0, 17.5, 0.8, 0.0, 2.2, 6, 0),
('Spinach', 'Vegetables', 23, 2.9, 0.4, 0.1, 0.0, 3.6, 0.4, 0.0, 2.2, 79, 0),
('Carrot', 'Vegetables', 41, 0.9, 0.2, 0.0, 0.0, 9.6, 4.7, 0.0, 2.8, 69, 0);

-- Proteins
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Chicken Breast', 'Protein', 165, 31.0, 3.6, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 74, 85),
('Eggs', 'Protein', 155, 12.6, 10.6, 3.3, 0.0, 1.1, 1.1, 0.0, 0.0, 124, 373),
('Chickpeas', 'Protein', 364, 19.3, 6.0, 0.6, 0.0, 60.7, 10.7, 0.0, 17.4, 24, 0),
('Paneer', 'Protein', 265, 18.3, 20.8, 13.0, 0.5, 1.2, 1.2, 0.0, 0.0, 18, 65);

-- Fats and Oils
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Olive Oil', 'Oils', 884, 0.0, 100.0, 13.8, 0.0, 0.0, 0.0, 0.0, 0.0, 2, 0),
('Sunflower Oil', 'Oils', 884, 0.0, 100.0, 10.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0),
('Coconut Oil', 'Oils', 862, 0.0, 100.0, 86.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0);

-- Sugars and Sweeteners
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('White Sugar', 'Sweeteners', 387, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 100.0, 0.0, 1, 0),
('Honey', 'Sweeteners', 304, 0.3, 0.0, 0.0, 0.0, 82.4, 82.1, 0.0, 0.2, 4, 0),
('Jaggery', 'Sweeteners', 383, 0.4, 0.1, 0.0, 0.0, 98.0, 98.0, 0.0, 0.0, 30, 0);

-- Spices and Condiments
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Salt', 'Condiments', 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 38758, 0),
('Turmeric Powder', 'Spices', 312, 9.7, 3.3, 1.8, 0.0, 67.1, 3.2, 0.0, 22.7, 27, 0),
('Red Chili Powder', 'Spices', 282, 13.5, 14.3, 2.5, 0.0, 54.7, 10.3, 0.0, 34.8, 91, 0);

-- Nuts and Seeds
INSERT INTO ingredients (name, category, energy_kcal, protein_g, total_fat_g, saturated_fat_g, trans_fat_g, carbohydrates_g, total_sugars_g, added_sugars_g, dietary_fiber_g, sodium_mg, cholesterol_mg)
VALUES 
('Almonds', 'Nuts', 579, 21.2, 49.9, 3.8, 0.0, 21.6, 4.4, 0.0, 12.5, 1, 0),
('Cashews', 'Nuts', 553, 18.2, 43.8, 7.8, 0.0, 30.2, 5.9, 0.0, 3.3, 12, 0),
('Peanuts', 'Nuts', 567, 25.8, 49.2, 6.8, 0.0, 16.1, 4.7, 0.0, 8.5, 18, 0);
