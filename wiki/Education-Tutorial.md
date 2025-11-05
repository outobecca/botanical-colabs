# 🎓 Tutorial Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/education/tutorial.ipynb)

> **Step-by-step introduction to botanical data science — perfect for beginners!**

---

## 📋 Overview

The **Tutorial Notebook** provides a gentle, hands-on introduction to using the Botanical Colabs library. Perfect for students, educators, and anyone new to botanical data science. No prior programming experience required!

### What You'll Learn
- 🌱 **Botanical data basics** — Understanding plant data sources
- 🐍 **Python fundamentals** — Learn as you go
- 📊 **Data visualization** — Create beautiful charts
- 🤖 **API integration** — Fetch real botanical data
- 📝 **Best practices** — Professional workflows

---

## 🎯 Who Is This For?

### Students
- ✅ **Beginner programmers** — Learn Python with botany
- ✅ **Biology students** — Apply data science to plants
- ✅ **High school projects** — Science fair projects
- ✅ **University assignments** — Research projects
- ✅ **Self-learners** — Teach yourself data science

### Educators
- ✅ **Course material** — Ready-to-use lessons
- ✅ **Interactive teaching** — Engage students
- ✅ **Assignment templates** — Customize for your class
- ✅ **Demonstration tool** — Show concepts live
- ✅ **Assessment resource** — Test understanding

### Hobbyists
- ✅ **Curious gardeners** — Learn about your plants
- ✅ **Citizen scientists** — Contribute to research
- ✅ **Nature enthusiasts** — Explore plant data
- ✅ **Career changers** — Explore data science
- ✅ **Lifelong learners** — New skills

---

## 📚 Tutorial Sections

### 1. Welcome & Setup (5 minutes)
```python
# Print welcome message
print("🌿 Welcome to Botanical Data Science!")

# What you'll learn
topics = [
    "Fetching plant data from APIs",
    "Creating visualizations",
    "Analyzing botanical information",
    "Building your first plant card"
]

for i, topic in enumerate(topics, 1):
    print(f"{i}. {topic}")
```

### 2. Python Basics (10 minutes)
```python
# Variables - storing information
species_name = "Rosa canina"
common_name = "Dog Rose"
height_cm = 150

# Lists - multiple items
characteristics = ["deciduous", "thorny", "fragrant"]

# Dictionaries - key-value pairs
plant_info = {
    "species": "Rosa canina",
    "family": "Rosaceae",
    "height": 150
}

# Print and format
print(f"The {common_name} ({species_name}) grows to {height_cm} cm")
```

### 3. Your First API Call (15 minutes)
```python
import requests

# Fetch plant data from GBIF
def get_plant_info(species_name):
    """
    Get plant information from GBIF.
    Don't worry about the details yet!
    """
    url = f"https://api.gbif.org/v1/species/match?name={species_name}"
    response = requests.get(url)
    return response.json()

# Try it!
plant_data = get_plant_info("Rosa canina")

# Print what we found
print(f"Scientific Name: {plant_data['scientificName']}")
print(f"Family: {plant_data['family']}")
print(f"Kingdom: {plant_data['kingdom']}")
```

**Explanation:**
- We ask GBIF (a plant database) for information
- It sends back data about the plant
- We print the interesting parts

### 4. Data Visualization (20 minutes)
```python
import matplotlib.pyplot as plt

# Create your first chart
heights = [50, 150, 200, 180, 120]
species = ['Viola', 'Rose', 'Sunflower', 'Lily', 'Lavender']

plt.figure(figsize=(10, 6))
plt.bar(species, heights, color='green')
plt.xlabel('Species')
plt.ylabel('Height (cm)')
plt.title('Plant Heights Comparison')
plt.show()
```

**Try it yourself:**
- Change the heights
- Add more species
- Try different colors

### 5. Working with Pandas (20 minutes)
```python
import pandas as pd

# Create a plant database
plants_df = pd.DataFrame({
    'species': ['Rosa canina', 'Quercus robur', 'Betula pendula'],
    'common_name': ['Dog Rose', 'English Oak', 'Silver Birch'],
    'height_m': [2, 30, 25],
    'native': [True, True, True]
})

# View the data
print(plants_df)

# Filter tall plants
tall_plants = plants_df[plants_df['height_m'] > 10]
print("\nTall plants:")
print(tall_plants)

# Calculate average height
avg_height = plants_df['height_m'].mean()
print(f"\nAverage height: {avg_height:.1f} meters")
```

### 6. Build Your First Plant Card (30 minutes)

**The complete workflow:**
```python
# Step 1: Choose a plant
my_plant = "Rosa canina"

# Step 2: Fetch taxonomy data
gbif_data = get_plant_info(my_plant)

# Step 3: Get Wikipedia description
def get_wikipedia_summary(species):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{species}"
    response = requests.get(url)
    return response.json()['extract']

wiki_summary = get_wikipedia_summary(my_plant)

# Step 4: Create a beautiful card
print("=" * 50)
print(f"🌹 {gbif_data['scientificName']}")
print("=" * 50)
print(f"\n📚 Family: {gbif_data['family']}")
print(f"🌍 Kingdom: {gbif_data['kingdom']}")
print(f"\n📖 Description:")
print(wiki_summary)
print("\n" + "=" * 50)
```

**What you created:**
- A professional plant information card
- Using real data from scientific databases
- Automatically formatted and ready to share

### 7. Hands-On Exercises

**Exercise 1: Try Different Plants**
```python
# Try these species:
exercise_plants = [
    "Quercus robur",      # English Oak
    "Betula pendula",     # Silver Birch
    "Pinus sylvestris",   # Scots Pine
    "Vaccinium myrtillus" # Bilberry
]

# Create a card for each one
for plant in exercise_plants:
    # Your code here!
    pass
```

**Exercise 2: Add More Data**
```python
# Can you add:
# - Number of occurrences from GBIF
# - Images from Wikimedia
# - Common names in different languages
```

**Exercise 3: Create a Comparison**
```python
# Compare two species
# Which one is taller?
# Which family do they belong to?
# What are the differences?
```

### 8. Next Steps

**What to explore next:**
1. 📊 [Data Analysis Template](TEMPLATE-Data-Analysis) — Analyze datasets
2. 🤖 [Machine Learning Template](TEMPLATE-Machine-Learning) — Build predictive models
3. 🌿 [Botanical Notebook](TEMPLATE-Botanical-Notebook) — Advanced features
4. 🎨 [MyST Scientific Template](TEMPLATE-MyST-Scientific) — Professional documentation

**Resources to continue learning:**
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [GBIF Data Portal](https://www.gbif.org)

---

## 💡 Tips for Success

### For Students
- ✅ Run each code cell one at a time
- ✅ Experiment by changing values
- ✅ Don't worry about errors — they're learning opportunities!
- ✅ Use comments (#) to remember what code does
- ✅ Ask questions in discussions

### For Educators
- ✅ Customize examples for your curriculum
- ✅ Add your own exercises
- ✅ Use local plant species students know
- ✅ Combine with field trips or herbarium visits
- ✅ Encourage collaboration between students

### Common Mistakes to Avoid
- ❌ Skipping the basics — foundation is important!
- ❌ Not reading error messages — they help you learn
- ❌ Copying without understanding — try to explain it
- ❌ Not experimenting — change things and see what happens
- ❌ Giving up too quickly — persistence pays off!

---

## 🎯 Learning Outcomes

After completing this tutorial, you will be able to:

1. ✅ **Fetch botanical data** from online APIs
2. ✅ **Create visualizations** with matplotlib
3. ✅ **Work with DataFrames** using pandas
4. ✅ **Build information cards** for plants
5. ✅ **Understand Python basics** (variables, functions, loops)
6. ✅ **Use Jupyter notebooks** effectively
7. ✅ **Apply concepts** to your own projects

---

## 📊 Difficulty Level

| Aspect | Level | Notes |
|--------|-------|-------|
| **Python** | Beginner | No prior experience needed |
| **Biology** | Beginner | Basic plant knowledge helpful |
| **Data Science** | Beginner | Gentle introduction |
| **Time Required** | 2-3 hours | Take breaks! |
| **Support** | Full | Detailed explanations |

---

## 🔧 Requirements

**No Installation Needed!**
- Just click "Open in Colab" above
- Everything runs in your browser
- No setup, no configuration
- Free to use

**Optional (for offline work):**
- Python 3.8+
- Jupyter Notebook
- Libraries: requests, pandas, matplotlib

---

## 🤝 Get Help

**Stuck? Here's how to get help:**

1. **Read the error message** — It usually tells you what's wrong
2. **Check the tutorial text** — The answer might be there
3. **Try Google** — "Python [your error message]"
4. **Ask in discussions** — Community is friendly!
5. **Reach out** — [GitHub Issues](https://github.com/outobecca/botanical-colabs/issues)

---

## 🌟 Success Stories

*"This tutorial got me into data science! I went from zero Python knowledge to building my own plant database in a week."* — Student

*"Perfect for my biology class. Students love working with real plant data instead of abstract examples."* — Educator

*"As a gardener with no coding experience, I was able to create beautiful visualizations of my garden data!"* — Hobbyist

---

## 📚 Related Resources

### Other Tutorials
- [API Setup Guide](https://github.com/outobecca/botanical-colabs/blob/main/API_SETUP.md)
- [MyST & Marp Guide](https://github.com/outobecca/botanical-colabs/blob/main/MYST_MARP_GUIDE.md)

### More Examples
- [Plant Card Generator](Examples-Plant-Card-Generator)
- [Batch Plant Cards](Examples-Batch-Plant-Cards)

### Advanced Topics
- [Machine Learning](TEMPLATE-Machine-Learning)
- [Data Analysis](TEMPLATE-Data-Analysis)

---

## 📄 License

MIT License — Free for educational use

**Perfect for:**
- Classroom teaching
- Self-study
- Workshops
- Bootcamps
- Online courses

---

## ✨ Make It Your Own

**Customization ideas:**
- Add your local plant species
- Include photos from your region
- Create exercises for specific topics
- Add quizzes or assessments
- Translate to other languages

---

**Created:** 2025-01-10  
**Updated:** 2025-11-05  
**Level:** 🟢 Beginner-Friendly  
**Time:** ⏱️ 2-3 hours  
**Prerequisites:** None!

[← Back to Education](Home#-education) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/education/tutorial.ipynb) | [Start Learning Now!](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/education/tutorial.ipynb)
