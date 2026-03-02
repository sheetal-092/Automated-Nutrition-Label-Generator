"""
Enhanced Nutrition Analysis Features
Adds compliance indicators, allergen detection, % daily values, and insights
"""

from typing import Dict, List, Tuple, Any


class NutritionAnalyzer:
    """Advanced nutrition analysis and insights"""
    
    # FSSAI/ICMR Recommended Daily Values (for adults)
    DAILY_VALUES = {
        'energy_kcal': 2000,
        'protein_g': 50,
        'total_fat_g': 65,
        'saturated_fat_g': 20,
        'carbohydrates_g': 300,
        'total_sugars_g': 50,
        'added_sugars_g': 25,
        'dietary_fiber_g': 25,
        'sodium_mg': 2300,
        'cholesterol_mg': 300
    }
    
    # Allergen keywords to detect in ingredients
    ALLERGEN_KEYWORDS = {
        'Milk': ['milk', 'dairy', 'whey', 'casein', 'lactose', 'butter', 'cream', 'yogurt', 'cheese', 'paneer', 'ghee'],
        'Wheat/Gluten': ['wheat', 'flour', 'gluten', 'atta', 'maida', 'bread', 'roti'],
        'Soy': ['soy', 'soya', 'tofu', 'soybean'],
        'Nuts': ['almond', 'cashew', 'walnut', 'pistachio', 'peanut', 'hazelnut', 'pecan', 'nut'],
        'Eggs': ['egg', 'albumin', 'mayonnaise'],
        'Fish': ['fish', 'salmon', 'tuna', 'cod', 'anchovy'],
        'Shellfish': ['shrimp', 'prawn', 'crab', 'lobster', 'shellfish'],
        'Sesame': ['sesame', 'til', 'tahini']
    }
    
    @staticmethod
    def calculate_daily_values(nutrition: Dict[str, float]) -> Dict[str, float]:
        """Calculate % Daily Value for nutrients"""
        daily_values = {}
        
        for nutrient, value in nutrition.items():
            if nutrient in NutritionAnalyzer.DAILY_VALUES:
                dv = NutritionAnalyzer.DAILY_VALUES[nutrient]
                daily_values[nutrient] = round((value / dv) * 100, 1)
            else:
                daily_values[nutrient] = 0
        
        return daily_values
    
    @staticmethod
    def detect_allergens(ingredients_list: str) -> List[str]:
        """Detect potential allergens in ingredients"""
        if not ingredients_list:
            return []
        
        ingredients_lower = ingredients_list.lower()
        detected_allergens = []
        
        for allergen, keywords in NutritionAnalyzer.ALLERGEN_KEYWORDS.items():
            for keyword in keywords:
                if keyword in ingredients_lower:
                    detected_allergens.append(allergen)
                    break  # Found this allergen, move to next
        
        return list(set(detected_allergens))  # Remove duplicates
    
    @staticmethod
    def generate_nutritional_insights(nutrition_per_100g: Dict[str, float]) -> Dict[str, List[str]]:
        """Generate smart nutritional insights"""
        insights = {
            'highlights': [],
            'concerns': [],
            'recommendations': []
        }
        
        protein = nutrition_per_100g.get('protein_g', 0)
        total_fat = nutrition_per_100g.get('total_fat_g', 0)
        saturated_fat = nutrition_per_100g.get('saturated_fat_g', 0)
        total_sugars = nutrition_per_100g.get('total_sugars_g', 0)
        added_sugars = nutrition_per_100g.get('added_sugars_g', 0)
        dietary_fiber = nutrition_per_100g.get('dietary_fiber_g', 0)
        sodium = nutrition_per_100g.get('sodium_mg', 0)
        energy = nutrition_per_100g.get('energy_kcal', 0)
        
        # Protein analysis
        if protein >= 15:
            insights['highlights'].append(f"🥇 Excellent protein source ({protein:.1f}g per 100g)")
        elif protein >= 8:
            insights['highlights'].append(f"✓ Good protein content ({protein:.1f}g per 100g)")
        elif protein < 3:
            insights['concerns'].append(f"⚠️ Low in protein ({protein:.1f}g per 100g)")
        
        # Fat analysis
        if total_fat > 17.5:
            insights['concerns'].append(f"⚠️ High in total fat ({total_fat:.1f}g per 100g)")
        elif total_fat < 3:
            insights['highlights'].append(f"✓ Low fat product ({total_fat:.1f}g per 100g)")
        
        # Saturated fat
        if saturated_fat > 5:
            insights['concerns'].append(f"⚠️ High in saturated fat ({saturated_fat:.1f}g per 100g)")
            insights['recommendations'].append("Consider alternatives with lower saturated fat")
        
        # Sugar analysis
        if total_sugars > 22.5:
            insights['concerns'].append(f"⚠️ High sugar content ({total_sugars:.1f}g per 100g)")
        elif total_sugars < 5:
            insights['highlights'].append(f"✓ Low sugar content ({total_sugars:.1f}g per 100g)")
        
        if added_sugars > 10:
            insights['concerns'].append(f"⚠️ Contains added sugars ({added_sugars:.1f}g per 100g)")
            insights['recommendations'].append("Limit consumption due to added sugars")
        
        # Fiber analysis
        if dietary_fiber >= 6:
            insights['highlights'].append(f"🥇 Excellent source of fiber ({dietary_fiber:.1f}g per 100g)")
        elif dietary_fiber >= 3:
            insights['highlights'].append(f"✓ Good source of fiber ({dietary_fiber:.1f}g per 100g)")
        elif dietary_fiber < 1:
            insights['concerns'].append(f"⚠️ Low in dietary fiber ({dietary_fiber:.1f}g per 100g)")
        
        # Sodium analysis
        if sodium > 600:
            insights['concerns'].append(f"⚠️ High sodium content ({sodium:.0f}mg per 100g)")
            insights['recommendations'].append("Not recommended for individuals on low-sodium diet")
        elif sodium < 120:
            insights['highlights'].append(f"✓ Low sodium ({sodium:.0f}mg per 100g)")
        
        # Energy analysis
        if energy > 400:
            insights['concerns'].append(f"⚠️ High calorie product ({energy:.0f} kcal per 100g)")
            insights['recommendations'].append("Consume in moderation as part of balanced diet")
        elif energy < 100:
            insights['highlights'].append(f"✓ Low calorie option ({energy:.0f} kcal per 100g)")
        
        # Overall healthiness
        if len(insights['concerns']) == 0 and len(insights['highlights']) >= 2:
            insights['highlights'].insert(0, "🌟 Overall: Nutritionally balanced product")
        
        return insights
    
    @staticmethod
    def get_compliance_status(is_compliant: bool, warnings: List[str], errors: List[str]) -> Dict[str, Any]:
        """Generate comprehensive compliance status"""
        if is_compliant and len(warnings) == 0:
            status = {
                'level': 'FULLY COMPLIANT',
                'badge': '✅',
                'color': '#059669',
                'message': 'Product meets all FSSAI 2020 requirements'
            }
        elif is_compliant and len(warnings) > 0:
            status = {
                'level': 'COMPLIANT WITH WARNINGS',
                'badge': '⚠️',
                'color': '#f59e0b',
                'message': f'Product is compliant but has {len(warnings)} warning(s)'
            }
        else:
            status = {
                'level': 'NON-COMPLIANT',
                'badge': '❌',
                'color': '#dc2626',
                'message': f'Product has {len(errors)} compliance error(s) that must be addressed'
            }
        
        status['warnings_count'] = len(warnings)
        status['errors_count'] = len(errors)
        
        return status
    
    @staticmethod
    def format_batch_nutrition(total_nutrition: Dict[str, float], total_weight_g: float) -> str:
        """Format batch nutrition output"""
        return f"""
🔹 TOTAL BATCH NUTRITION (Full Recipe: {total_weight_g:.0f}g)
   Energy: {total_nutrition.get('energy_kcal', 0):.0f} kcal
   Protein: {total_nutrition.get('protein_g', 0):.1f}g
   Fat: {total_nutrition.get('total_fat_g', 0):.1f}g
   Carbs: {total_nutrition.get('carbohydrates_g', 0):.1f}g
   Fiber: {total_nutrition.get('dietary_fiber_g', 0):.1f}g
   Sodium: {total_nutrition.get('sodium_mg', 0):.0f}mg
"""
