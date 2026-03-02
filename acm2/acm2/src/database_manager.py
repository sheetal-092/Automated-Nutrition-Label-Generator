"""
Database Manager for Nutrition Label Generator
Handles all database operations including initialization, CRUD operations
"""

import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime


class DatabaseManager:
    """Manages SQLite database operations for nutritional data"""
    
    def __init__(self, db_path: str = "nutrition.db"):
        """Initialize database connection"""
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        
    def connect(self):
        """Establish database connection"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Enable column access by name
        self.cursor = self.conn.cursor()
        
    def disconnect(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            
    def initialize_database(self, schema_file: str, seed_file: Optional[str] = None):
        """Initialize database with schema and optional seed data"""
        self.connect()
        
        # Execute schema
        with open(schema_file, 'r') as f:
            schema_sql = f.read()
            self.conn.executescript(schema_sql)
            
        # Execute seed data if provided
        if seed_file and Path(seed_file).exists():
            with open(seed_file, 'r') as f:
                seed_sql = f.read()
                self.conn.executescript(seed_sql)
                
        self.conn.commit()
        print(f"Database initialized successfully at {self.db_path}")
        
    def get_ingredient_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Retrieve ingredient by name"""
        self.cursor.execute(
            "SELECT * FROM ingredients WHERE LOWER(name) = LOWER(?)", 
            (name,)
        )
        row = self.cursor.fetchone()
        return dict(row) if row else None
        
    def search_ingredients(self, search_term: str) -> List[Dict[str, Any]]:
        """Search ingredients by name or category"""
        self.cursor.execute(
            """SELECT * FROM ingredients 
               WHERE LOWER(name) LIKE LOWER(?) OR LOWER(category) LIKE LOWER(?)""",
            (f"%{search_term}%", f"%{search_term}%")
        )
        return [dict(row) for row in self.cursor.fetchall()]
        
    def add_ingredient(self, ingredient_data: Dict[str, Any]) -> int:
        """Add new ingredient to database"""
        columns = ', '.join(ingredient_data.keys())
        placeholders = ', '.join(['?' for _ in ingredient_data])
        
        self.cursor.execute(
            f"INSERT INTO ingredients ({columns}) VALUES ({placeholders})",
            list(ingredient_data.values())
        )
        self.conn.commit()
        return self.cursor.lastrowid
        
    def create_recipe(self, name: str, description: str, 
                     total_weight_g: float, servings: int = 1) -> int:
        """Create a new recipe"""
        self.cursor.execute(
            """INSERT INTO recipes (name, description, total_weight_g, servings)
               VALUES (?, ?, ?, ?)""",
            (name, description, total_weight_g, servings)
        )
        self.conn.commit()
        return self.cursor.lastrowid
        
    def add_recipe_ingredient(self, recipe_id: int, 
                             ingredient_id: int, weight_g: float):
        """Add ingredient to recipe"""
        self.cursor.execute(
            """INSERT INTO recipe_ingredients (recipe_id, ingredient_id, weight_g)
               VALUES (?, ?, ?)""",
            (recipe_id, ingredient_id, weight_g)
        )
        self.conn.commit()
        
    def get_recipe_ingredients(self, recipe_id: int) -> List[Dict[str, Any]]:
        """Get all ingredients for a recipe"""
        self.cursor.execute(
            """SELECT i.*, ri.weight_g 
               FROM ingredients i
               JOIN recipe_ingredients ri ON i.id = ri.ingredient_id
               WHERE ri.recipe_id = ?""",
            (recipe_id,)
        )
        return [dict(row) for row in self.cursor.fetchall()]
        
    def get_recipe(self, recipe_id: int) -> Optional[Dict[str, Any]]:
        """Get recipe by ID"""
        self.cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None
        
    def save_nutrition_label(self, recipe_id: int, label_data: Dict[str, Any], 
                            fssai_compliant: bool = True) -> int:
        """Save generated nutrition label"""
        self.cursor.execute(
            """INSERT INTO nutrition_labels (recipe_id, label_data, fssai_compliant)
               VALUES (?, ?, ?)""",
            (recipe_id, json.dumps(label_data), fssai_compliant)
        )
        self.conn.commit()
        return self.cursor.lastrowid
        
    def get_all_ingredients(self) -> List[Dict[str, Any]]:
        """Get all ingredients from database"""
        self.cursor.execute("SELECT * FROM ingredients ORDER BY category, name")
        return [dict(row) for row in self.cursor.fetchall()]
        
    def get_ingredients_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get ingredients by category"""
        self.cursor.execute(
            "SELECT * FROM ingredients WHERE category = ? ORDER BY name",
            (category,)
        )
        return [dict(row) for row in self.cursor.fetchall()]
