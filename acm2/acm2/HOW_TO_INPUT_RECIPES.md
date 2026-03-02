# 👥 USER-FRIENDLY INPUT GUIDE

For non-technical users, use these **3 simple methods** to input recipes:

---

## **Method 1: Interactive Input (Easiest)**

### Step 1: Run the tool
```bash
python tools/recipe_input.py interactive
```

### Step 2: Follow the prompts
```
📝 Recipe Name: My Chocolate Cookies
📝 Description: Homemade delicious cookies
🍽️  Number of servings: 12
```

### Step 3: Add ingredients one by one
```
Ingredient 1: 300g Whole Wheat Flour
Ingredient 2: 200g Butter
Ingredient 3: 150g White Sugar
Ingredient 4: 2g Salt
Type 'done' when finished
```

✅ Labels generated automatically!

---

## **Method 2: CSV File (Spreadsheet)**

### Step 1: Open sample file
Open `sample_recipes.csv` with **Excel, Google Sheets, or any spreadsheet**:

| Recipe Name | Description | Servings | Ingredient 1 | Ingredient 2 | Ingredient 3 |
|-------------|-------------|----------|--------------|--------------|--------------|
| My Snack | Healthy snack | 6 | 100g Almonds | 50g Honey | 30g Jaggery |

### Step 2: Add your recipes
Simply add rows to the spreadsheet with your recipes.

### Step 3: Run the tool
```bash
python tools/recipe_input.py csv sample_recipes.csv
```

✅ All recipes processed and labels generated!

---

## **Method 3: JSON File (Text)**

### Step 1: Open sample file
Open `sample_recipes.json` with **Notepad or any text editor**:

```json
{
  "recipes": [
    {
      "name": "My Recipe",
      "description": "Description here",
      "servings": 4,
      "ingredients": [
        "200g Whole Wheat Flour",
        "100ml Water",
        "2g Salt"
      ]
    }
  ]
}
```

### Step 2: Add your recipes
Copy and paste recipe blocks, filling in your details.

### Step 3: Run the tool
```bash
python tools/recipe_input.py json sample_recipes.json
```

✅ All recipes processed!

---

## **Quick Start Commands**

### Interactive (No file needed)
```bash
python tools/recipe_input.py interactive
```

### Load from CSV
```bash
python tools/recipe_input.py csv recipes.csv
```

### Load from JSON
```bash
python tools/recipe_input.py json recipes.json
```

### Show menu
```bash
python tools/recipe_input.py
```

---

## **📊 Sample Files Provided**

We've included **ready-to-use** sample files:

### **sample_recipes.csv**
10 ready-made recipes in spreadsheet format
- Healthy Breakfast Bowl
- Indian Paneer Curry
- Chickpea Salad
- Homemade Trail Mix
- And more...

**How to use:**
1. Open with Excel or Google Sheets
2. Edit the recipes as needed
3. Run: `python tools/recipe_input.py csv sample_recipes.csv`

### **sample_recipes.json**
6 recipes in JSON format
- Whole Grain Breakfast
- Protein Power Salad
- Creamy Curry Delight
- Energy Snack Mix
- Simple Vegetable Rice
- Quick Cheese Toast

**How to use:**
1. Open with Notepad
2. Edit the recipes as needed
3. Run: `python tools/recipe_input.py json sample_recipes.json`

---

## **Available Ingredients**

You can use any of these **30+ ingredients**:

### Grains
- Whole Wheat Flour
- Rice Flour
- Oats
- White Bread

### Dairy
- Whole Milk
- Cheddar Cheese
- Yogurt (Plain)
- Butter

### Vegetables
- Tomato
- Onion
- Potato
- Spinach
- Carrot

### Proteins
- Chicken Breast
- Eggs
- Chickpeas
- Paneer

### Oils
- Olive Oil
- Sunflower Oil
- Coconut Oil

### Sweeteners
- White Sugar
- Honey
- Jaggery

### Nuts
- Almonds
- Cashews
- Peanuts

### Spices
- Salt
- Turmeric Powder
- Red Chili Powder

---

## **Format Examples**

### ✅ CORRECT INGREDIENT FORMAT
```
200g Whole Wheat Flour
100ml Whole Milk
2 cups Rice Flour
1 tbsp Salt
50g Almonds
30ml Olive Oil
```

### ❌ INCORRECT FORMAT (Don't use)
```
wheat flour 200g
milk 100ml
some salt
handful of almonds
```

---

## **What You Get**

After processing recipes, you'll find in `output/` folder:

### HTML Label Files
- Professional nutrition facts tables
- Print-ready design
- FSSAI-compliant format
- Open in any browser to view

### JSON Data Files
- Machine-readable nutritional data
- Per 100g values
- Per serving values
- FSSAI compliance status

---

## **Example Workflow**

### Using CSV (Easiest for Most People)

1. **Open Excel/Google Sheets**
   - Open `sample_recipes.csv`

2. **Add your recipes**
   - Add rows with your recipe names and ingredients

3. **Save the file**
   - File → Save

4. **Run the tool**
   ```bash
   python tools/recipe_input.py csv sample_recipes.csv
   ```

5. **View your labels**
   - Open `output/` folder
   - Open `.html` files in browser

---

## **Troubleshooting**

### "File not found" error
Make sure the file is in the same folder as `recipe_input.py`:
```
c:\Users\justa\Downloads\acm2\
  ├── tools\
  │   └── recipe_input.py
  ├── sample_recipes.csv     ← Here
  └── sample_recipes.json    ← Or here
```

### Ingredient not found
Use the exact ingredient names from the list above. Common issues:
```
❌ "wheat flour" 
✅ "Whole Wheat Flour"

❌ "dahi"
✅ "Yogurt (Plain)"

❌ "chana"
✅ "Chickpeas"
```

### Still stuck?
1. Try the interactive method: `python tools/recipe_input.py interactive`
2. Check the sample recipes for format examples
3. Review the ingredient list for correct names

---

## **Features**

✅ **No coding required** - Simple menus and files  
✅ **Batch processing** - Process multiple recipes at once  
✅ **FSSAI validation** - Automatic compliance checking  
✅ **Professional output** - Print-ready HTML labels  
✅ **Sample files** - Copy and edit provided templates  
✅ **Instant labels** - Get results in seconds  

---

**Ready to start? Choose your method above and begin creating labels!** 🏷️
