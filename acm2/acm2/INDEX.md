# 📑 Project Index - Automated Nutrition Label Generator

## 🎯 Quick Navigation

### 🚀 Getting Started
- [README.md](README.md) - **START HERE** - Complete project overview
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick commands and API reference
- [requirements.txt](requirements.txt) - Python dependencies

### 📚 Documentation
- [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - Detailed usage instructions
- [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) - Database schema and API
- [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) - Complete ingredient list
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Project completion summary

### 💻 Source Code
- [main.py](main.py) - Main application entry point
- [src/database_manager.py](src/database_manager.py) - Database operations
- [src/recipe_parser.py](src/recipe_parser.py) - Recipe parsing & nutrition calculation
- [src/fssai_compliance.py](src/fssai_compliance.py) - FSSAI validation logic
- [src/label_generator.py](src/label_generator.py) - Label generation (HTML/JSON)
- [src/llm_mapper.py](src/llm_mapper.py) - LLM ingredient mapping

### 🎮 Demos & Examples
- [demo/run_demo.py](demo/run_demo.py) - Comprehensive demo with 5 recipes
- [examples/code_examples.py](examples/code_examples.py) - Code usage examples

### 🗄️ Database
- [database/schema.sql](database/schema.sql) - Database schema
- [database/seed_data.sql](database/seed_data.sql) - Sample nutritional data (30+ ingredients)
- `nutrition.db` - SQLite database (auto-created on first run)

### 📤 Output
- [output/](output/) - Generated nutrition labels (HTML & JSON files)

---

## 📖 Documentation Guide

### For First-Time Users
1. Read [README.md](README.md) for project overview
2. Review [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for commands
3. Run `python demo/run_demo.py` to see it in action
4. Check [docs/USER_GUIDE.md](docs/USER_GUIDE.md) for detailed usage

### For Developers
1. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for architecture
2. Study [src/](src/) folder for code structure
3. Check [examples/code_examples.py](examples/code_examples.py) for API usage
4. Read [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) for database

### For Food Professionals
1. Start with [README.md](README.md) - Features section
2. Check [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) for available ingredients
3. Review [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - FSSAI Compliance section
4. Run `python main.py` to generate your first label

---

## 🎯 Common Tasks - Quick Links

### Run the Application
```bash
python main.py
```
See: [main.py](main.py)

### Run All Demos
```bash
python demo/run_demo.py
```
See: [demo/run_demo.py](demo/run_demo.py)

### View Available Ingredients
See: [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md)

### Add Custom Ingredient
See: [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - Advanced Features section

### Understand FSSAI Compliance
See: [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - FSSAI Compliance Guide section

### Database Operations
See: [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md)

---

## 📋 File Descriptions

### Root Level Files

| File | Description | When to Use |
|------|-------------|-------------|
| [README.md](README.md) | Project overview and setup | First-time setup |
| [main.py](main.py) | Main application | Running single recipe |
| [requirements.txt](requirements.txt) | Dependencies | Installation |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Command cheat sheet | Quick lookups |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Completion summary | Understanding deliverables |
| [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) | Ingredient list | Finding ingredients |

### Documentation Folder

| File | Description | When to Use |
|------|-------------|-------------|
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Complete user manual | Learning how to use |
| [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) | Database reference | Database operations |

### Source Code Folder

| File | Purpose | Key Features |
|------|---------|--------------|
| [src/database_manager.py](src/database_manager.py) | Database ops | CRUD operations, connections |
| [src/recipe_parser.py](src/recipe_parser.py) | Recipe parsing | Ingredient parsing, nutrition calc |
| [src/fssai_compliance.py](src/fssai_compliance.py) | FSSAI validation | Compliance checking, warnings |
| [src/label_generator.py](src/label_generator.py) | Label creation | HTML/JSON generation |
| [src/llm_mapper.py](src/llm_mapper.py) | AI mapping | Intelligent ingredient matching |

### Database Folder

| File | Purpose | When to Modify |
|------|---------|----------------|
| [database/schema.sql](database/schema.sql) | Table definitions | Adding new tables |
| [database/seed_data.sql](database/seed_data.sql) | Sample data | Adding ingredients |

### Demo & Examples

| File | Purpose | When to Use |
|------|---------|-------------|
| [demo/run_demo.py](demo/run_demo.py) | Full demo | Testing, learning |
| [examples/code_examples.py](examples/code_examples.py) | Code samples | API learning |

---

## 🔍 Finding What You Need

### "How do I...?"

| Task | See This File | Section |
|------|---------------|---------|
| Get started | [README.md](README.md) | Quick Start |
| Process a recipe | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Python API |
| Add an ingredient | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Advanced Features |
| Understand FSSAI rules | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | FSSAI Compliance |
| Find ingredient data | [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) | All tables |
| Customize labels | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Customizing Labels |
| Query database | [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) | Database Operations |
| Use LLM features | [README.md](README.md) | LLM Integration |

---

## 📊 Project Statistics

### Files Created
- **Documentation**: 6 files
- **Source Code**: 6 Python modules
- **Database**: 2 SQL files
- **Demos**: 2 Python scripts
- **Total**: 16+ core files

### Lines of Code
- **Python**: ~2,500+ lines
- **SQL**: ~200+ lines
- **Documentation**: ~3,000+ lines

### Features
- **30+ Ingredients** across 9 categories
- **5 Demo Recipes** included
- **11 Nutrients** tracked per ingredient
- **4 Database Tables** in schema
- **2 Output Formats** (HTML, JSON)

---

## 🎓 Learning Path

### Beginner Path
1. ✅ [README.md](README.md) - Understand what it does
2. ✅ [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Learn basic commands
3. ✅ Run `python demo/run_demo.py` - See it work
4. ✅ [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) - Know what's available
5. ✅ [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - Master the features

### Advanced Path
1. ✅ [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - System architecture
2. ✅ [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) - Database deep dive
3. ✅ [examples/code_examples.py](examples/code_examples.py) - Code patterns
4. ✅ Review [src/](src/) modules - Implementation details
5. ✅ Extend and customize

---

## 🔗 External Resources

- **FSSAI Official**: https://www.fssai.gov.in/
- **USDA FoodData**: https://fdc.nal.usda.gov/
- **Python Documentation**: https://docs.python.org/3/
- **SQLite Documentation**: https://www.sqlite.org/docs.html

---

## ✅ Checklist for New Users

- [ ] Read [README.md](README.md)
- [ ] Run `python main.py`
- [ ] Check output in `output/` folder
- [ ] Review [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- [ ] Try `python demo/run_demo.py`
- [ ] Read [docs/USER_GUIDE.md](docs/USER_GUIDE.md)
- [ ] Explore [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md)
- [ ] Try creating your own recipe

---

## 📞 Support

For help with specific topics:

| Topic | Resource |
|-------|----------|
| Installation issues | [README.md](README.md) - Installation section |
| Usage questions | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) |
| Database queries | [docs/DATABASE_DOCUMENTATION.md](docs/DATABASE_DOCUMENTATION.md) |
| FSSAI compliance | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - FSSAI section |
| Code examples | [examples/code_examples.py](examples/code_examples.py) |
| Ingredient list | [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md) |

---

## 🚀 Next Steps

1. **Run the Demo**: `python demo/run_demo.py`
2. **Process Your Recipe**: Modify [main.py](main.py) with your recipe
3. **Explore the Database**: Review [INGREDIENT_DATABASE.md](INGREDIENT_DATABASE.md)
4. **Read Full Guide**: Check [docs/USER_GUIDE.md](docs/USER_GUIDE.md)
5. **Customize**: Extend with your own ingredients and features

---

**Version**: 1.0  
**Last Updated**: February 27, 2026  
**Status**: ✅ Complete & Ready to Use  

---

*Happy Label Generating!* 🏷️
