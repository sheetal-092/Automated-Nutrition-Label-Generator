"""
Nutrition Label Generator
Generates FSSAI-compliant nutrition labels in various formats (PDF, PNG, HTML)
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
import json


class LabelGenerator:
    """Generates nutrition labels in various formats"""
    
    def __init__(self):
        self.label_template = None
        
    def generate_html_label(self, 
                           product_name: str,
                           nutrition_per_100g: Dict[str, float],
                           nutrition_per_serving: Optional[Dict[str, float]] = None,
                           serving_size: Optional[str] = None,
                           servings_per_package: Optional[int] = None,
                           ingredients_list: Optional[str] = None,
                           manufacturer_info: Optional[Dict[str, str]] = None,
                           fssai_license: Optional[str] = None) -> str:
        """
        Generate HTML nutrition label following FSSAI format
        """
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nutrition Facts - {product_name}</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .nutrition-label {{
            width: 350px;
            border: 2px solid black;
            background-color: white;
            padding: 10px;
            margin: 0 auto;
        }}
        .label-header {{
            text-align: center;
            border-bottom: 8px solid black;
            padding-bottom: 5px;
        }}
        .label-title {{
            font-size: 28px;
            font-weight: bold;
            margin: 0;
        }}
        .product-name {{
            font-size: 18px;
            font-weight: bold;
            margin: 10px 0;
            text-align: center;
        }}
        .serving-info {{
            border-bottom: 2px solid black;
            padding: 5px 0;
            font-size: 13px;
        }}
        .amount-per-serving {{
            font-size: 11px;
            font-weight: bold;
            margin: 5px 0;
            border-bottom: 4px solid black;
            padding-bottom: 2px;
        }}
        .nutrient-row {{
            display: flex;
            justify-content: space-between;
            padding: 3px 0;
            border-bottom: 1px solid #ddd;
            font-size: 13px;
        }}
        .nutrient-row.thick-border {{
            border-bottom: 4px solid black;
            padding-bottom: 5px;
        }}
        .nutrient-row.medium-border {{
            border-bottom: 2px solid black;
        }}
        .nutrient-name {{
            font-weight: normal;
        }}
        .nutrient-name.bold {{
            font-weight: bold;
        }}
        .nutrient-name.indent {{
            padding-left: 20px;
            font-size: 12px;
        }}
        .nutrient-value {{
            font-weight: bold;
        }}
        .ingredients-section {{
            margin-top: 15px;
            padding-top: 10px;
            border-top: 2px solid black;
            font-size: 11px;
        }}
        .ingredients-title {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .manufacturer-info {{
            margin-top: 15px;
            padding-top: 10px;
            border-top: 2px solid black;
            font-size: 10px;
        }}
        .fssai-logo {{
            text-align: center;
            margin-top: 10px;
            font-weight: bold;
            font-size: 11px;
        }}
        .note {{
            font-size: 9px;
            margin-top: 10px;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="nutrition-label">
        <div class="label-header">
            <div class="label-title">Nutrition Facts</div>
        </div>
        
        <div class="product-name">{product_name}</div>
        
        {self._generate_serving_info_html(serving_size, servings_per_package)}
        
        <div class="amount-per-serving">Nutritional Information (per 100g)</div>
        
        <div class="nutrient-row thick-border">
            <span class="nutrient-name bold">Energy</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['energy_kcal'], 'energy_kcal')} kcal</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name bold">Protein</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['protein_g'], 'protein_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name bold">Total Fat</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['total_fat_g'], 'total_fat_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name indent">Saturated Fat</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['saturated_fat_g'], 'saturated_fat_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name indent">Trans Fat</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['trans_fat_g'], 'trans_fat_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name bold">Carbohydrates</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['carbohydrates_g'], 'carbohydrates_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name indent">Total Sugars</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['total_sugars_g'], 'total_sugars_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name indent">Added Sugars</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g.get('added_sugars_g', 0), 'added_sugars_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name indent">Dietary Fiber</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g.get('dietary_fiber_g', 0), 'dietary_fiber_g')} g</span>
        </div>
        
        <div class="nutrient-row">
            <span class="nutrient-name bold">Sodium</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g['sodium_mg'], 'sodium_mg')} mg</span>
        </div>
        
        <div class="nutrient-row medium-border">
            <span class="nutrient-name bold">Cholesterol</span>
            <span class="nutrient-value">{self._format_value(nutrition_per_100g.get('cholesterol_mg', 0), 'cholesterol_mg')} mg</span>
        </div>
        
        {self._generate_ingredients_html(ingredients_list)}
        
        {self._generate_manufacturer_html(manufacturer_info, fssai_license)}
        
        <div class="note">
            * Nutritional values are approximate and based on standard ingredient data.
        </div>
    </div>
</body>
</html>
"""
        return html
    
    def _generate_serving_info_html(self, serving_size: Optional[str], 
                                   servings_per_package: Optional[int]) -> str:
        """Generate serving information HTML"""
        if not serving_size:
            return ""
        
        html = '<div class="serving-info">'
        html += f'<div>Serving Size: {serving_size}</div>'
        if servings_per_package:
            html += f'<div>Servings per package: {servings_per_package}</div>'
        html += '</div>'
        return html
    
    def _generate_ingredients_html(self, ingredients_list: Optional[str]) -> str:
        """Generate ingredients section HTML"""
        if not ingredients_list:
            return ""
        
        return f"""
        <div class="ingredients-section">
            <div class="ingredients-title">Ingredients:</div>
            <div>{ingredients_list}</div>
        </div>
        """
    
    def _generate_manufacturer_html(self, manufacturer_info: Optional[Dict[str, str]], 
                                   fssai_license: Optional[str]) -> str:
        """Generate manufacturer information HTML"""
        if not manufacturer_info and not fssai_license:
            return ""
        
        html = '<div class="manufacturer-info">'
        
        if manufacturer_info:
            if 'name' in manufacturer_info:
                html += f"<div><strong>Manufactured by:</strong> {manufacturer_info['name']}</div>"
            if 'address' in manufacturer_info:
                html += f"<div>{manufacturer_info['address']}</div>"
            if 'contact' in manufacturer_info:
                html += f"<div>Contact: {manufacturer_info['contact']}</div>"
        
        html += '</div>'
        
        if fssai_license:
            html += f"""
            <div class="fssai-logo">
                <div>FSSAI License No.: {fssai_license}</div>
            </div>
            """
        
        return html
    
    def _format_value(self, value: float, nutrient: str) -> str:
        """Format nutritional value according to FSSAI standards"""
        if nutrient == 'energy_kcal':
            return f"{round(value)}"
        elif nutrient.endswith('_mg'):
            if value < 1:
                return f"{value:.2f}"
            else:
                return f"{round(value, 1)}"
        else:
            if value < 0.5:
                return f"{value:.2f}"
            elif value < 10:
                return f"{round(value, 1)}"
            else:
                return f"{round(value, 1)}"
    
    def save_html_label(self, html_content: str, filename: str):
        """Save HTML label to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Label saved to {filename}")
    
    def generate_json_label(self,
                           product_name: str,
                           nutrition_per_100g: Dict[str, float],
                           nutrition_per_serving: Optional[Dict[str, float]] = None,
                           serving_size: Optional[str] = None,
                           servings_per_package: Optional[int] = None,
                           ingredients_list: Optional[str] = None,
                           fssai_compliant: bool = True,
                           compliance_warnings: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate label data in JSON format"""
        
        label_data = {
            "product_name": product_name,
            "generated_at": datetime.now().isoformat(),
            "nutrition_per_100g": nutrition_per_100g,
            "fssai_compliant": fssai_compliant,
            "compliance_version": "FSSAI 2020"
        }
        
        if nutrition_per_serving:
            label_data["nutrition_per_serving"] = nutrition_per_serving
        
        if serving_size:
            label_data["serving_size"] = serving_size
        
        if servings_per_package:
            label_data["servings_per_package"] = servings_per_package
        
        if ingredients_list:
            label_data["ingredients"] = ingredients_list
        
        if compliance_warnings:
            label_data["compliance_warnings"] = compliance_warnings
        
        return label_data
    
    def save_json_label(self, label_data: Dict[str, Any], filename: str):
        """Save label data as JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(label_data, f, indent=2)
        print(f"Label data saved to {filename}")
