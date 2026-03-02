import contextlib
import sys
import traceback
import os
import csv
from io import StringIO
from pathlib import Path

from flask import Flask, request, send_from_directory, render_template_string, Response

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from main import NutritionLabelApp

app = Flask(__name__)

OUTPUT_DIR = ROOT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load .env file if it exists (simple implementation)
env_file = ROOT_DIR / ".env"
if env_file.exists():
    try:
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    except Exception as e:
        print(f"Warning: Could not load .env file: {e}")

# LLM Configuration (optional)
LLM_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
USE_LLM = bool(LLM_API_KEY)

nutrition_app = NutritionLabelApp(use_llm=USE_LLM)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Nutrition Label Generator</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="preconnect" href="https://images.unsplash.com">
  <style>
    :root {
      --bg: #0f172a;
      --card: #ffffff;
      --muted: #6b7280;
      --accent: #10b981;
      --accent-dark: #059669;
      --ink: #0f172a;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Inter", "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
      background-size: 400% 400%;
      animation: gradient 15s ease infinite;
      color: #e5e7eb;
      padding: 36px 18px 48px;
    }
    @keyframes gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .container {
      max-width: 1080px;
      margin: 0 auto;
    }
    .hero {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 20px;
      align-items: center;
      margin-bottom: 22px;
    }
    .hero-card {
      background: linear-gradient(135deg, rgba(16,185,129,0.16), rgba(14,165,233,0.10));
      border: 1px solid rgba(148,163,184,0.18);
      border-radius: 18px;
      padding: 22px 26px;
      backdrop-filter: blur(10px);
    }
    .hero-title {
      font-size: 32px;
      margin: 0 0 10px;
    }
    .hero-sub { color: #cbd5f5; margin: 0; line-height: 1.5; }
    .hero-image {
      border-radius: 18px;
      overflow: hidden;
      height: 220px;
      box-shadow: 0 16px 30px rgba(0,0,0,0.35);
      border: 1px solid rgba(148,163,184,0.2);
    }
    .hero-image img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .card {
      background: var(--card);
      color: var(--ink);
      border-radius: 18px;
      padding: 24px;
      box-shadow: 0 18px 40px rgba(15,23,42,0.18);
    }
    label { display: block; margin: 12px 0 6px; font-weight: 600; }
    input, textarea, select {
      width: 100%;
      padding: 12px;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      font-size: 14px;
      background: #fff;
      color: #0f172a;
    }
    textarea { min-height: 150px; font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; }
    button {
      margin-top: 16px;
      padding: 12px 18px;
      background: var(--accent);
      color: #fff;
      border: 0;
      border-radius: 10px;
      cursor: pointer;
      font-size: 15px;
      font-weight: 600;
      box-shadow: 0 12px 24px rgba(16,185,129,0.35);
    }
    button:hover { background: var(--accent-dark); }
    .row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .alert { padding: 12px; border-radius: 10px; margin-top: 16px; }
    .error { background: #fee2e2; color: #991b1b; }
    .success { background: #dcfce7; color: #14532d; }
    .outputs { margin-top: 16px; }
    .outputs a {
      display: inline-block;
      margin-right: 12px;
      color: #0f172a;
      background: #e2e8f0;
      padding: 8px 12px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
    }
    .outputs a:hover { background: #cbd5f5; }
    pre { background: #0b1020; color: #e5e7eb; padding: 12px; border-radius: 10px; overflow-x: auto; }
    .hint { color: var(--muted); font-size: 13px; margin-top: 6px; }
    .footer { margin-top: 22px; color: #94a3b8; font-size: 13px; text-align: center; }
    .llm-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin: 8px 0; }
    .llm-enabled { background: #dcfce7; color: #14532d; }
    .llm-disabled { background: #fee2e2; color: #991b1b; }
    .llm-info { background: #eff6ff; border-left: 4px solid #0ea5e9; color: #0c4a6e; padding: 12px; border-radius: 6px; margin: 12px 0; font-size: 13px; }
    @media (max-width: 900px) {
      .hero { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="hero">
      <div class="hero-card">
        <h1 class="hero-title">Nutrition Label Generator</h1>
        <p class="hero-sub">Create professional, FSSAI-friendly nutrition labels in seconds. Add ingredients, generate outputs, and download the label files instantly.</p>
      </div>
      <div class="hero-image">
        <img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1200&q=80" alt="Fresh ingredients">
      </div>
    </div>

    <div class="card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
        <p style="margin: 0;">Enter recipe details and ingredients below. Each ingredient must follow: <strong>quantity unit ingredient</strong>.</p>
        {% if llm_enabled %}
          <span class="llm-badge llm-enabled">🤖 AI Agent Active</span>
        {% else %}
          <span class="llm-badge llm-disabled">AI Agent Off</span>
        {% endif %}
      </div>

      {% if llm_enabled %}
        <div class="llm-info">
          ✨ <strong>AI Agent is Active:</strong> Your ingredients will be intelligently matched using LLM, improving accuracy for similar ingredient names (e.g., "rice" → "white rice").
        </div>
      {% else %}
        <div class="llm-info">
          💡 <strong>Tip:</strong> Set OPENAI_API_KEY or ANTHROPIC_API_KEY environment variable to enable AI Agent for smarter ingredient matching!
        </div>
      {% endif %}

    <form method="post">
      <div class="row">
        <div>
          <label for="recipe_name">Recipe Name</label>
          <input id="recipe_name" name="recipe_name" placeholder="Paneer Butter Masala" value="{{ recipe_name|default('') }}" required>
        </div>
        <div>
          <label for="servings">Servings</label>
          <input id="servings" name="servings" type="number" min="1" value="{{ servings|default(1) }}" required>
        </div>
      </div>

      <label for="description">Description</label>
      <input id="description" name="description" placeholder="Creamy tomato-based curry with paneer" value="{{ description|default('') }}">

      <label for="ingredients">Ingredients (one per line)</label>
      <textarea id="ingredients" name="ingredients" placeholder="200g Paneer\n150g Tomato\n100g Onion\n50g Cashew\n30g Butter\n10ml Sunflower Oil\n2g Red Chili Powder" required>{{ ingredients|default('') }}</textarea>
      <div class="hint">Examples: 200g Paneer, 150ml Milk, 2 tbsp Butter</div>

      <button type="submit">Generate Labels</button>
    </form>

    <hr style="margin: 24px 0; border: none; border-top: 1px solid #e2e8f0;">

    <h3 style="margin-top: 0;">📤 Or Upload CSV (Batch Processing)</h3>
    <p>Process multiple recipes at once. Download the template to see the format.</p>

    <form method="post" enctype="multipart/form-data" id="csv-form">
      <label for="csv_file">Select CSV File</label>
      <input type="file" id="csv_file" name="csv_file" accept=".csv" required>
      <div class="hint">Format: Recipe Name, Description, Servings, Ingredient 1, Ingredient 2, ...</div>
      <button type="submit" name="upload_csv" value="true">Process CSV</button>
      
      <a href="/download-template" style="display: inline-block; margin-left: 12px; padding: 12px 18px; background: #8b5cf6; color: #fff; text-decoration: none; border-radius: 10px; font-weight: 600;">📥 Download Template</a>
    </form>

    {% if error %}
      <div class="alert error">{{ error }}</div>
    {% endif %}

    {% if success %}
      <div class="alert success">
        {% if recipes_processed > 1 %}
          ✓ Successfully processed <strong>{{ recipes_processed }} recipes</strong>! All labels are ready to download.
        {% else %}
          ✓ Labels generated successfully.
        {% endif %}
      </div>
    {% endif %}

    {% if outputs %}
      <div class="outputs">
        <strong>Downloads:</strong>
        {% for o in outputs %}
          <a href="{{ o.url }}" target="_blank">{{ o.label }}</a>
        {% endfor %}
      </div>
    {% endif %}

    {% if log_output %}
      <h3>Processing Output</h3>
      <pre>{{ log_output }}</pre>
    {% endif %}
    </div>

    <div class="footer">Built for fast nutrition labeling • Download HTML/JSON instantly</div>
  </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    success = False
    outputs = []
    log_output = ""
    recipes_processed = 0

    recipe_name = request.form.get("recipe_name", "")
    description = request.form.get("description", "")
    servings = request.form.get("servings", "1")
    ingredients = request.form.get("ingredients", "")

    if request.method == "POST":
        try:
            # Check if it's a CSV upload
            if request.form.get("upload_csv") == "true" and "csv_file" in request.files:
                csv_file = request.files["csv_file"]
                if not csv_file or csv_file.filename == "":
                    raise ValueError("No CSV file selected")
                
                if not csv_file.filename.endswith(".csv"):
                    raise ValueError("File must be a CSV file")
                
                # Read CSV and process recipes
                stream = csv_file.stream.read().decode("utf-8")
                csv_reader = csv.reader(StringIO(stream))
                headers = next(csv_reader)  # Skip header
                
                stdout = StringIO()
                successful_labels = []
                
                for row_num, row in enumerate(csv_reader, 2):
                    if not row or not row[0].strip():
                        continue
                    
                    recipe_name_csv = row[0].strip()
                    description_csv = row[1].strip() if len(row) > 1 else ""
                    
                    try:
                        servings_csv = int(row[2].strip()) if len(row) > 2 and row[2].strip() else 1
                    except ValueError:
                        servings_csv = 1
                    
                    # Extract ingredients
                    ingredients_list = [ing.strip() for ing in row[3:] if ing.strip()]
                    ingredients_csv = "\n".join(ingredients_list)
                    
                    if not ingredients_list:
                        continue
                    
                    with contextlib.redirect_stdout(stdout):
                        result = nutrition_app.process_recipe(
                            recipe_name=recipe_name_csv,
                            recipe_text=ingredients_csv,
                            description=description_csv,
                            servings=servings_csv
                        )
                    
                    recipes_processed += 1
                    html_file = Path(result["html_file"]).name
                    json_file = Path(result["json_file"]).name
                    successful_labels.append({
                        "name": recipe_name_csv,
                        "html": html_file,
                        "json": json_file
                    })
                
                log_output = stdout.getvalue().strip()
                success = True
                
                # Format outputs
                for label in successful_labels:
                    outputs.append({"label": f"{label['name']} (HTML)", "url": f"/download/{label['html']}"})
                    outputs.append({"label": f"{label['name']} (JSON)", "url": f"/download/{label['json']}"})
                
            else:
                # Manual form submission
                servings_value = int(servings)
                if servings_value < 1:
                    raise ValueError("Servings must be at least 1")

                if not recipe_name.strip():
                    raise ValueError("Recipe name is required")

                if not ingredients.strip():
                    raise ValueError("Please enter at least one ingredient")

                stdout = StringIO()
                with contextlib.redirect_stdout(stdout):
                    result = nutrition_app.process_recipe(
                        recipe_name=recipe_name.strip(),
                        recipe_text=ingredients.strip(),
                        description=description.strip(),
                        servings=servings_value
                    )

                log_output = stdout.getvalue().strip()
                success = True
                recipes_processed = 1

                html_file = Path(result["html_file"]).name
                json_file = Path(result["json_file"]).name

                outputs = [
                    {"label": "HTML Label", "url": f"/download/{html_file}"},
                    {"label": "JSON Data", "url": f"/download/{json_file}"}
                ]
        except Exception as exc:
            trace = traceback.format_exc()
            log_output = f"{log_output}\n{trace}".strip()
            error = str(exc)

    return render_template_string(
        TEMPLATE,
        error=error,
        success=success,
        outputs=outputs,
        log_output=log_output,
        recipe_name=recipe_name,
        description=description,
        servings=servings,
        ingredients=ingredients,
        llm_enabled=USE_LLM,
        recipes_processed=recipes_processed
    )


@app.route("/download-template")
def download_template():
    """Generate and download CSV template"""
    csv_content = """Recipe Name,Description,Servings,Ingredient 1,Ingredient 2,Ingredient 3,Ingredient 4,Ingredient 5,Ingredient 6,Ingredient 7
Paneer Butter Masala,Creamy tomato curry with paneer,4,200g Paneer,150g Tomato,100g Onion,50g Cashew,30g Butter,10ml Sunflower Oil,2g Red Chili Powder
Healthy Oatmeal Bowl,Nutritious breakfast,2,100g Oats,200ml Whole Milk,50g Almonds,30g Honey,100g Carrot,,
Chickpea Salad,High protein vegetarian,3,200g Chickpeas,100g Tomato,50g Onion,50g Carrot,30g Spinach,10ml Olive Oil,
Vegetable Fried Rice,Quick dinner,4,300g Cooked Rice,100g Carrot,100g Peas,50g Onion,10ml Sunflower Oil,2g Salt,"""
    
    return Response(
        csv_content,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=recipe_template.csv"}
    )


@app.route("/download/<path:filename>")
def download(filename: str):
    safe_path = (OUTPUT_DIR / filename).resolve()
    if OUTPUT_DIR not in safe_path.parents and safe_path != OUTPUT_DIR:
        return "Invalid file", 400
    if not safe_path.exists():
        return "File not found", 404
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
