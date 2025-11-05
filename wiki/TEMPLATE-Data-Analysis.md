# 📊 Data Analysis Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_data_analysis.ipynb)

> **Professional data analysis framework with pandas, visualization, and statistical tools**

---

## 📋 Overview

The **Data Analysis Template** provides a comprehensive framework for analyzing botanical datasets. Built on pandas, matplotlib, seaborn, and scipy, it includes ready-to-use functions for data cleaning, exploratory analysis, statistical testing, and professional visualizations.

### Perfect For
- 📈 **Exploratory Data Analysis (EDA)** — Understand your datasets
- 📊 **Statistical Analysis** — Hypothesis testing and correlations
- 🎨 **Data Visualization** — Publication-quality charts
- 🧹 **Data Cleaning** — Handle missing values and outliers
- 📉 **Trend Analysis** — Time series and patterns
- 📑 **Report Generation** — Automated insights

---

## 🎯 Use Cases

### Research & Academia
- ✅ **Analyze field data** — Process survey results
- ✅ **Statistical validation** — Test hypotheses
- ✅ **Comparative studies** — Compare groups/treatments
- ✅ **Publication figures** — Create journal-ready charts
- ✅ **Meta-analysis** — Combine multiple datasets

### Educational
- ✅ **Teaching statistics** — Demonstrate concepts
- ✅ **Student assignments** — Structured analysis framework
- ✅ **Lab reports** — Professional data presentation
- ✅ **Interactive tutorials** — Learn data analysis
- ✅ **Exam preparation** — Practice with real data

### Professional
- ✅ **Greenhouse monitoring** — Analyze environmental data
- ✅ **Crop yield analysis** — Optimize production
- ✅ **Quality control** — Monitor plant health
- ✅ **Market research** — Sales and trends
- ✅ **Performance reports** — Business intelligence

### Personal Projects
- ✅ **Garden tracking** — Monitor plant growth
- ✅ **Weather analysis** — Local climate patterns
- ✅ **Citizen science** — Analyze observations
- ✅ **Hobby projects** — Learn data science
- ✅ **Competition entries** — Kaggle-style analysis

---

## ⭐ Key Features

### Data Loading & Preparation

**Multiple format support:**
```python
# CSV files
df = pd.read_csv('data.csv')

# Excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# JSON files
df = pd.read_json('data.json')

# URL/API
df = pd.read_csv('https://example.com/data.csv')

# Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/...'
df = pd.read_csv(sheet_url)
```

**Data cleaning functions:**
```python
def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Comprehensive data cleaning pipeline.
    
    Steps:
        1. Remove duplicate rows
        2. Handle missing values
        3. Fix data types
        4. Remove outliers
        5. Standardize column names
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fix data types
    df = convert_data_types(df)
    
    # Remove outliers (IQR method)
    df = remove_outliers(df, method='iqr')
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    return df
```

### Exploratory Data Analysis

**Automatic EDA:**
```python
def perform_eda(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate comprehensive EDA report.
    
    Returns:
        - Dataset shape and info
        - Descriptive statistics
        - Missing value analysis
        - Correlation matrix
        - Distribution plots
        - Outlier detection
    """
    eda_results = {
        'shape': df.shape,
        'dtypes': df.dtypes,
        'missing': df.isnull().sum(),
        'statistics': df.describe(),
        'correlations': df.corr(),
        'outliers': detect_outliers(df)
    }
    
    # Generate visualizations
    plot_distributions(df)
    plot_correlation_heatmap(df)
    plot_missing_values(df)
    
    return eda_results
```

**Visual summaries:**
```python
def plot_distributions(df: pd.DataFrame) -> None:
    """Plot distribution of all numeric columns."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    fig, axes = plt.subplots(
        nrows=(len(numeric_cols) + 2) // 3,
        ncols=3,
        figsize=(15, 5 * len(numeric_cols) // 3)
    )
    
    for idx, col in enumerate(numeric_cols):
        ax = axes.flatten()[idx]
        df[col].hist(bins=30, ax=ax, edgecolor='black')
        ax.set_title(f'Distribution of {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
```

### Statistical Analysis

**Hypothesis testing:**
```python
from scipy import stats

def compare_groups(
    df: pd.DataFrame,
    column: str,
    group_column: str
) -> Dict[str, float]:
    """
    Compare two groups using t-test.
    
    Returns:
        - t-statistic
        - p-value
        - effect size (Cohen's d)
        - confidence interval
    """
    groups = df.groupby(group_column)[column]
    group1 = groups.get_group(df[group_column].unique()[0])
    group2 = groups.get_group(df[group_column].unique()[1])
    
    # T-test
    t_stat, p_value = stats.ttest_ind(group1, group2)
    
    # Effect size
    cohens_d = (group1.mean() - group2.mean()) / \
               np.sqrt((group1.std()**2 + group2.std()**2) / 2)
    
    # Confidence interval
    ci = stats.t.interval(
        0.95,
        len(group1) + len(group2) - 2,
        loc=group1.mean() - group2.mean(),
        scale=stats.sem(np.concatenate([group1, group2]))
    )
    
    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'confidence_interval': ci
    }
```

**Correlation analysis:**
```python
def analyze_correlations(
    df: pd.DataFrame,
    threshold: float = 0.7
) -> pd.DataFrame:
    """
    Find strong correlations in dataset.
    
    Args:
        threshold: Minimum correlation coefficient
    
    Returns:
        DataFrame with correlated pairs
    """
    corr_matrix = df.corr()
    
    # Get upper triangle
    mask = np.triu(np.ones_like(corr_matrix), k=1).astype(bool)
    upper = corr_matrix.where(mask)
    
    # Find strong correlations
    strong_corr = []
    for col in upper.columns:
        for row in upper.index:
            if abs(upper.loc[row, col]) > threshold:
                strong_corr.append({
                    'var1': row,
                    'var2': col,
                    'correlation': upper.loc[row, col]
                })
    
    return pd.DataFrame(strong_corr)
```

### Professional Visualizations

**Publication-quality charts:**
```python
import seaborn as sns

# Set publication style
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.5)

def create_publication_plot(
    df: pd.DataFrame,
    x: str,
    y: str,
    hue: str = None
) -> None:
    """Create publication-ready scatter plot."""
    plt.figure(figsize=(10, 6), dpi=300)
    
    sns.scatterplot(
        data=df,
        x=x,
        y=y,
        hue=hue,
        s=100,
        alpha=0.7,
        edgecolor='black',
        linewidth=0.5
    )
    
    plt.xlabel(x.replace('_', ' ').title(), fontsize=14)
    plt.ylabel(y.replace('_', ' ').title(), fontsize=14)
    plt.title(f'{y} vs {x}', fontsize=16, fontweight='bold')
    
    if hue:
        plt.legend(title=hue.replace('_', ' ').title())
    
    plt.tight_layout()
    plt.savefig(f'{y}_vs_{x}.png', dpi=300, bbox_inches='tight')
    plt.show()
```

**Interactive dashboards:**
```python
def create_interactive_dashboard(df: pd.DataFrame) -> None:
    """Create interactive visualization dashboard."""
    from ipywidgets import interact, Dropdown
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    @interact(
        x=Dropdown(options=numeric_cols, description='X-axis:'),
        y=Dropdown(options=numeric_cols, description='Y-axis:'),
        plot_type=Dropdown(
            options=['scatter', 'line', 'bar', 'box'],
            description='Plot type:'
        )
    )
    def update_plot(x, y, plot_type):
        plt.figure(figsize=(10, 6))
        
        if plot_type == 'scatter':
            plt.scatter(df[x], df[y], alpha=0.6)
        elif plot_type == 'line':
            plt.plot(df[x], df[y])
        elif plot_type == 'bar':
            df.groupby(x)[y].mean().plot(kind='bar')
        elif plot_type == 'box':
            df.boxplot(column=y, by=x)
        
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{y} vs {x}')
        plt.tight_layout()
        plt.show()
```

### Time Series Analysis

**Trend detection:**
```python
def analyze_time_series(
    df: pd.DataFrame,
    date_column: str,
    value_column: str
) -> Dict[str, Any]:
    """
    Analyze time series data.
    
    Returns:
        - Trend analysis
        - Seasonality detection
        - Forecasting
        - Change points
    """
    # Convert to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(date_column)
    
    # Calculate rolling statistics
    df['rolling_mean'] = df[value_column].rolling(window=7).mean()
    df['rolling_std'] = df[value_column].rolling(window=7).std()
    
    # Trend analysis
    from scipy.stats import linregress
    x = np.arange(len(df))
    slope, intercept, r_value, p_value, std_err = linregress(x, df[value_column])
    
    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df[date_column], df[value_column], label='Actual', alpha=0.7)
    plt.plot(df[date_column], df['rolling_mean'], label='7-day MA', linewidth=2)
    plt.fill_between(
        df[date_column],
        df['rolling_mean'] - df['rolling_std'],
        df['rolling_mean'] + df['rolling_std'],
        alpha=0.2
    )
    plt.legend()
    plt.title(f'Time Series Analysis: {value_column}')
    plt.xlabel('Date')
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return {
        'trend_slope': slope,
        'trend_pvalue': p_value,
        'r_squared': r_value**2
    }
```

---

## 📦 What's Included

### Notebook Structure (15 Cells)

1. **Introduction & Setup**
   - Template overview
   - Installation instructions
   - Quick start guide

2. **Library Imports**
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   from scipy import stats
   import ipywidgets as widgets
   ```

3. **Configuration**
   - Plot settings
   - Display options
   - Random seed

4. **Data Loading**
   - File upload widget
   - Multiple format support
   - Sample dataset

5. **Data Cleaning**
   - Handle missing values
   - Remove duplicates
   - Fix data types

6. **Exploratory Analysis**
   - Dataset overview
   - Descriptive statistics
   - Missing value analysis

7. **Distribution Analysis**
   - Histograms
   - KDE plots
   - Q-Q plots

8. **Correlation Analysis**
   - Correlation matrix
   - Heatmap visualization
   - Strong correlation finder

9. **Statistical Testing**
   - T-tests
   - ANOVA
   - Chi-square tests

10. **Group Comparisons**
    - Box plots
    - Violin plots
    - Statistical significance

11. **Time Series (if applicable)**
    - Trend analysis
    - Seasonality
    - Forecasting

12. **Advanced Visualizations**
    - Pair plots
    - Joint plots
    - Facet grids

13. **Interactive Dashboards**
    - Widget-based controls
    - Dynamic plotting
    - Parameter tuning

14. **Report Generation**
    - Summary statistics
    - Key findings
    - Recommendations

15. **Export Results**
    - Save processed data
    - Export charts
    - Generate PDF report

---

## 🚀 Getting Started

### Quick Start

1. **Open in Colab** — Click badge above

2. **Upload Your Data:**
   ```python
   # Use file upload widget
   from google.colab import files
   uploaded = files.upload()
   
   # Load data
   df = pd.read_csv(list(uploaded.keys())[0])
   ```

3. **Run Analysis:**
   ```python
   # Quick EDA
   eda_results = perform_eda(df)
   
   # View summary
   print(eda_results['statistics'])
   ```

4. **Create Visualizations:**
   ```python
   # Correlation heatmap
   plot_correlation_heatmap(df)
   
   # Distribution plots
   plot_distributions(df)
   ```

5. **Export Results:**
   ```python
   # Save cleaned data
   df.to_csv('cleaned_data.csv', index=False)
   
   # Download from Colab
   files.download('cleaned_data.csv')
   ```

---

## 💡 Usage Examples

### Example 1: Basic Analysis

```python
# Load data
df = pd.read_csv('plant_measurements.csv')

# Clean data
df = clean_dataset(df)

# Analyze
summary = df.describe()
correlations = df.corr()

# Visualize
plot_correlation_heatmap(df)
```

### Example 2: Group Comparison

```python
# Compare treatment groups
results = compare_groups(
    df=df,
    column='height',
    group_column='treatment'
)

print(f"P-value: {results['p_value']:.4f}")
print(f"Effect size: {results['cohens_d']:.4f}")
```

### Example 3: Time Series

```python
# Analyze growth over time
time_results = analyze_time_series(
    df=df,
    date_column='measurement_date',
    value_column='height'
)

print(f"Growth rate: {time_results['trend_slope']:.2f} cm/day")
```

---

## 📚 Related Resources

- [Botanical Notebook](TEMPLATE-Botanical-Notebook) — Data collection
- [Machine Learning Template](TEMPLATE-Machine-Learning) — Predictive models
- [MyST Scientific Template](TEMPLATE-MyST-Scientific) — Documentation

---

## 📄 License

MIT License — Free to use, modify, and distribute

[← Back to Templates](Home#-templates) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_data_analysis.ipynb)
