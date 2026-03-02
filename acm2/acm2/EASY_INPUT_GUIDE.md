# NON-TECHNICAL USER SOLUTION

## ✅ Now You Can Input Recipes 3 Easy Ways!

---

## **🎯 Quick Overview**

```
┌─────────────────────────────────────┐
│   USER PROVIDES RECIPES             │
│  (No coding knowledge needed)        │
├─────────────────────────────────────┤
│                                     │
│  Option 1: Interactive Menu         │
│  Option 2: Spreadsheet (CSV)        │
│  Option 3: Text File (JSON)         │
│                                     │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  NUTRITION LABEL GENERATOR          │
│                                     │
│  • Parse ingredients                │
│  • Calculate nutrition              │
│  • Validate FSSAI compliance        │
│  • Generate professional labels     │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  PROFESSIONAL LABELS GENERATED      │
│                                     │
│  ✓ HTML files (print-ready)        │
│  ✓ JSON files (data files)         │
│  ✓ FSSAI-compliant format          │
└─────────────────────────────────────┘
```

---

## **📝 OPTION 1: INTERACTIVE (Simplest)**

### For beginners with no files needed

```bash
python tools/recipe_input.py interactive
```

**How it works:**
1. System asks for recipe name
2. System asks for description
3. System asks for servings
4. You type each ingredient
5. Type "done" when finished
6. Labels generated automatically

**No files. No spreadsheets. Just answer questions!**

---

## **📊 OPTION 2: SPREADSHEET (Fastest for Many Recipes)**

### For people who know Excel/Google Sheets

**Files provided:**
- `sample_recipes.csv` - Ready to use

**Steps:**
1. Open `sample_recipes.csv` with Excel
2. Edit or add your recipes
3. Save the file
4. Run: `python tools/recipe_input.py csv sample_recipes.csv`
5. Done! Labels generated

**Example:**
```
Recipe Name          | Servings | Ingredient 1        | Ingredient 2      | Ingredient 3
My Chocolate Snack   | 12       | 200g Almonds        | 100g Honey        | 50g Jaggery
Paneer Curry         | 4        | 300g Paneer         | 150g Tomato       | 100g Onion
```

---

## **📄 OPTION 3: TEXT FILE (For developers)**

### For people comfortable with text files

**Files provided:**
- `sample_recipes.json` - Ready to use

**Steps:**
1. Open `sample_recipes.json` with Notepad
2. Edit or add your recipes
3. Save the file
4. Run: `python tools/recipe_input.py json sample_recipes.json`
5. Done! Labels generated

**Format:**
```json
{
  "recipes": [
    {
      "name": "My Recipe",
      "description": "Description",
      "servings": 4,
      "ingredients": [
        "200g Ingredient1",
        "100g Ingredient2"
      ]
    }
  ]
}
```

---

## **🎬 TRY IT NOW**

### Quickest test (2 minutes):

```bash
# Use provided sample recipes
python tools/recipe_input.py csv sample_recipes.csv
```

This will:
- Process 10 recipes from the sample file
- Generate 10 professional labels
- Save them in `output/` folder

### Check the results:
Open any `.html` file in the `output/` folder to see the labels!

---

## **📁 What You Get**

After running the tool, check `output/` folder:

```
output/
├── Healthy_Breakfast_Bowl_label.html     ← Open in browser
├── Healthy_Breakfast_Bowl_data.json      ← Raw data
├── Indian_Paneer_Curry_label.html        ← Open in browser
├── Indian_Paneer_Curry_data.json         ← Raw data
└── ... (more recipes)
```

**HTML files** = Professional nutrition labels (print-ready)  
**JSON files** = Data in machine-readable format

---

## **🌟 Sample Recipes Included**

Both files come with ready-to-use recipes:

### In sample_recipes.csv:
✓ Healthy Breakfast Bowl  
✓ Indian Paneer Curry  
✓ Chickpea Salad  
✓ Homemade Trail Mix  
✓ Cheese and Vegetable Toast  
✓ Lentil Soup  
✓ Sweet Honey Almonds  
✓ Vegetable Fried Rice  
✓ Paneer Tikka  
✓ Mixed Nut Butter  

### In sample_recipes.json:
✓ Whole Grain Breakfast  
✓ Protein Power Salad  
✓ Creamy Curry Delight  
✓ Energy Snack Mix  
✓ Simple Vegetable Rice  
✓ Quick Cheese Toast  

---

## **❓ FAQ**

**Q: Do I need to know how to code?**  
A: No! Use interactive mode or edit the provided CSV/JSON files.

**Q: Can I use my own recipe?**  
A: Yes! Edit the sample files or use interactive mode.

**Q: Which method is easiest?**  
A: Interactive mode - just answer questions!

**Q: Can I process multiple recipes at once?**  
A: Yes! CSV and JSON methods process all recipes in the file.

**Q: What output do I get?**  
A: Professional HTML labels (print-ready) and JSON data.

**Q: Are the labels FSSAI-compliant?**  
A: Yes! Automatically validated for FSSAI 2020 regulations.

---

## **🚀 Get Started in 3 Steps**

### Step 1: Open terminal
```
Press Windows key + R
Type: cmd
Press Enter
```

### Step 2: Navigate to folder
```bash
cd c:\Users\justa\Downloads\acm2
```

### Step 3: Run one of these commands

**For interactive input:**
```bash
python tools/recipe_input.py interactive
```

**For sample recipes (fastest):**
```bash
python tools/recipe_input.py csv sample_recipes.csv
```

**View your labels:**
- Open `output/` folder
- Double-click any `.html` file

---

## **📞 Need Help?**

See detailed guide: [HOW_TO_INPUT_RECIPES.md](HOW_TO_INPUT_RECIPES.md)

Available ingredients: [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md)

---

## **💡 Perfect For:**

✅ Food Startups - No developer needed  
✅ Home Bakers - Simple input interface  
✅ Restaurants - Batch process menus  
✅ Food Manufacturers - Rapid prototyping  
✅ Anyone - Even non-technical users  

---

**Now anyone can create professional nutrition labels - no coding required!** 🏷️✨
