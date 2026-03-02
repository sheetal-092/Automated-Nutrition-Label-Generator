"""
FSSAI Compliance Module
Validates and ensures nutrition labels comply with FSSAI regulations
"""

from typing import Dict, List, Tuple, Any
from enum import Enum


class FSSAICategory(Enum):
    """FSSAI food product categories"""
    GENERAL = "General Food Products"
    PACKAGED_DRINKING_WATER = "Packaged Drinking Water"
    INFANT_FOOD = "Infant Food"
    HEALTH_SUPPLEMENT = "Health Supplement"
    SNACKS = "Snacks"
    BEVERAGES = "Beverages"
    DAIRY = "Dairy Products"


class FSSAIValidator:
    """Validates nutrition labels against FSSAI regulations"""
    
    # FSSAI 2020 regulations - Nutrient thresholds
    LOW_FAT_THRESHOLD = 3.0  # g per 100g for solids
    LOW_SUGAR_THRESHOLD = 5.0  # g per 100g for solids
    LOW_SODIUM_THRESHOLD = 120  # mg per 100g
    
    HIGH_FAT_THRESHOLD = 17.5  # g per 100g
    HIGH_SATURATED_FAT_THRESHOLD = 5.0  # g per 100g
    HIGH_SUGAR_THRESHOLD = 22.5  # g per 100g
    HIGH_SODIUM_THRESHOLD = 600  # mg per 100g
    
    # Required nutrients on label (as per FSSAI)
    MANDATORY_NUTRIENTS = [
        'energy_kcal',
        'protein_g',
        'total_fat_g',
        'saturated_fat_g',
        'trans_fat_g',
        'carbohydrates_g',
        'total_sugars_g',
        'sodium_mg'
    ]
    
    # Optional but recommended
    OPTIONAL_NUTRIENTS = [
        'added_sugars_g',
        'dietary_fiber_g',
        'cholesterol_mg'
    ]
    
    def __init__(self):
        self.warnings = []
        self.errors = []
        
    def validate_label(self, nutrition: Dict[str, float], 
                      category: FSSAICategory = FSSAICategory.GENERAL) -> Tuple[bool, List[str], List[str]]:
        """
        Validate nutrition label against FSSAI requirements
        Returns: (is_compliant, warnings, errors)
        """
        self.warnings = []
        self.errors = []
        
        # Check mandatory nutrients are present
        self._check_mandatory_nutrients(nutrition)
        
        # Validate trans fat compliance
        self._check_trans_fat(nutrition)
        
        # Check for health warnings
        self._check_health_warnings(nutrition)
        
        # Validate added sugars declaration
        self._check_added_sugars(nutrition)
        
        # Check rounding rules
        self._check_rounding_compliance(nutrition)
        
        is_compliant = len(self.errors) == 0
        
        return is_compliant, self.warnings, self.errors
    
    def _check_mandatory_nutrients(self, nutrition: Dict[str, float]):
        """Ensure all mandatory nutrients are present"""
        for nutrient in self.MANDATORY_NUTRIENTS:
            if nutrient not in nutrition:
                self.errors.append(f"Missing mandatory nutrient: {nutrient}")
    
    def _check_trans_fat(self, nutrition: Dict[str, float]):
        """
        FSSAI regulation: Trans fat must be less than 2% of total fat
        Products with < 0.2g trans fat per serving can be labeled as "0"
        """
        trans_fat = nutrition.get('trans_fat_g', 0)
        total_fat = nutrition.get('total_fat_g', 0)
        
        if total_fat > 0:
            trans_fat_percentage = (trans_fat / total_fat) * 100
            
            if trans_fat_percentage > 2.0:
                self.errors.append(
                    f"Trans fat exceeds 2% of total fat ({trans_fat_percentage:.2f}%). "
                    "FSSAI requires trans fat to be < 2% of total fat."
                )
        
        # Trans fat should be declared if >= 0.2g per serving
        if trans_fat >= 0.2:
            self.warnings.append(
                f"Trans fat is {trans_fat:.2f}g. Consider reformulation to reduce trans fat."
            )
    
    def _check_health_warnings(self, nutrition: Dict[str, float]):
        """Check if product requires health warnings based on nutrient levels"""
        
        # High fat warning
        if nutrition.get('total_fat_g', 0) > self.HIGH_FAT_THRESHOLD:
            self.warnings.append(
                f"High fat content ({nutrition['total_fat_g']:.1f}g per 100g). "
                "Consider adding 'High in Fat' declaration."
            )
        
        # High saturated fat warning
        if nutrition.get('saturated_fat_g', 0) > self.HIGH_SATURATED_FAT_THRESHOLD:
            self.warnings.append(
                f"High saturated fat content ({nutrition['saturated_fat_g']:.1f}g per 100g). "
                "Consider adding 'High in Saturated Fat' declaration."
            )
        
        # High sugar warning
        if nutrition.get('total_sugars_g', 0) > self.HIGH_SUGAR_THRESHOLD:
            self.warnings.append(
                f"High sugar content ({nutrition['total_sugars_g']:.1f}g per 100g). "
                "Consider adding 'High in Sugar' declaration."
            )
        
        # High sodium warning
        if nutrition.get('sodium_mg', 0) > self.HIGH_SODIUM_THRESHOLD:
            self.warnings.append(
                f"High sodium content ({nutrition['sodium_mg']:.0f}mg per 100g). "
                "Consider adding 'High in Salt/Sodium' declaration."
            )
    
    def _check_added_sugars(self, nutrition: Dict[str, float]):
        """
        FSSAI regulation: Added sugars must be declared separately from total sugars
        """
        added_sugars = nutrition.get('added_sugars_g', 0)
        total_sugars = nutrition.get('total_sugars_g', 0)
        
        if added_sugars > total_sugars:
            self.errors.append(
                f"Added sugars ({added_sugars:.1f}g) cannot exceed total sugars ({total_sugars:.1f}g)"
            )
        
        # Warning if added sugars are significant
        if added_sugars > 0 and added_sugars not in nutrition:
            self.warnings.append(
                "Added sugars should be declared separately from total sugars as per FSSAI 2020 regulations."
            )
    
    def _check_rounding_compliance(self, nutrition: Dict[str, float]):
        """
        FSSAI rounding rules:
        - Energy: round to nearest 1 kcal
        - Protein, Carbs, Fat: round to 0.1g if < 10g, else 1g
        - Sodium: round to nearest mg
        """
        # These checks are informational
        energy = nutrition.get('energy_kcal', 0)
        if energy < 5:
            self.warnings.append(
                "Energy is very low. Ensure accurate calculation and rounding."
            )
    
    def get_fssai_declarations(self, nutrition: Dict[str, float]) -> List[str]:
        """
        Generate required FSSAI declarations based on nutrient content
        """
        declarations = []
        
        # Trans fat declaration
        trans_fat = nutrition.get('trans_fat_g', 0)
        if trans_fat < 0.2:
            declarations.append("Trans Fat: 0g (per serving)")
        
        # Health claims eligibility
        if nutrition.get('total_fat_g', 0) <= self.LOW_FAT_THRESHOLD:
            declarations.append("Eligible for 'Low Fat' claim")
        
        if nutrition.get('total_sugars_g', 0) <= self.LOW_SUGAR_THRESHOLD:
            declarations.append("Eligible for 'Low Sugar' claim")
        
        if nutrition.get('sodium_mg', 0) <= self.LOW_SODIUM_THRESHOLD:
            declarations.append("Eligible for 'Low Sodium' claim")
        
        # Warning declarations
        if nutrition.get('total_fat_g', 0) > self.HIGH_FAT_THRESHOLD:
            declarations.append("Required: 'High in Fat' declaration")
        
        if nutrition.get('saturated_fat_g', 0) > self.HIGH_SATURATED_FAT_THRESHOLD:
            declarations.append("Required: 'High in Saturated Fat' declaration")
        
        if nutrition.get('total_sugars_g', 0) > self.HIGH_SUGAR_THRESHOLD:
            declarations.append("Required: 'High in Sugar' declaration")
        
        if nutrition.get('sodium_mg', 0) > self.HIGH_SODIUM_THRESHOLD:
            declarations.append("Required: 'High in Salt/Sodium' declaration")
        
        return declarations
    
    def generate_compliance_report(self, nutrition: Dict[str, float]) -> str:
        """Generate detailed FSSAI compliance report"""
        is_compliant, warnings, errors = self.validate_label(nutrition)
        declarations = self.get_fssai_declarations(nutrition)
        
        report_lines = [
            "=" * 60,
            "FSSAI COMPLIANCE REPORT",
            "=" * 60,
            f"Compliance Status: {'✓ COMPLIANT' if is_compliant else '✗ NON-COMPLIANT'}",
            ""
        ]
        
        if errors:
            report_lines.append("ERRORS (Must Fix):")
            for error in errors:
                report_lines.append(f"  ✗ {error}")
            report_lines.append("")
        
        if warnings:
            report_lines.append("WARNINGS (Recommended):")
            for warning in warnings:
                report_lines.append(f"  ⚠ {warning}")
            report_lines.append("")
        
        if declarations:
            report_lines.append("REQUIRED DECLARATIONS:")
            for declaration in declarations:
                report_lines.append(f"  • {declaration}")
            report_lines.append("")
        
        if is_compliant and not warnings:
            report_lines.append("✓ Label meets all FSSAI requirements")
        
        report_lines.append("=" * 60)
        
        return '\n'.join(report_lines)
