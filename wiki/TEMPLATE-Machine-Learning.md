# 🤖 Machine Learning Template

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_machine_learning.ipynb)

> **Complete ML pipeline with scikit-learn: from data prep to model deployment**

---

## 📋 Overview

The **Machine Learning Template** provides a production-ready framework for building, training, and evaluating machine learning models for botanical applications. Built on scikit-learn, it includes automated feature engineering, model selection, hyperparameter tuning, and model evaluation.

### What You'll Learn
- 🎯 **Problem formulation** — Define ML objectives
- 🔧 **Feature engineering** — Create meaningful features
- 🤖 **Model selection** — Choose the right algorithm
- ⚙️ **Hyperparameter tuning** — Optimize performance
- 📊 **Model evaluation** — Assess accuracy and reliability
- 🚀 **Deployment** — Save and use models

---

## 🎯 Use Cases

### Classification Problems
- ✅ **Species identification** — Classify plants from features
- ✅ **Disease detection** — Identify plant diseases
- ✅ **Quality grading** — Grade produce quality
- ✅ **Pest classification** — Identify pest types
- ✅ **Toxicity prediction** — Classify plant toxicity

### Regression Problems
- ✅ **Yield prediction** — Estimate crop yields
- ✅ **Growth modeling** — Predict plant growth rates
- ✅ **Nutrient estimation** — Predict nutrient needs
- ✅ **Price forecasting** — Estimate market prices
- ✅ **Water demand** — Predict irrigation needs

### Clustering
- ✅ **Plant grouping** — Find similar species
- ✅ **Habitat classification** — Group by environment
- ✅ **Customer segmentation** — Market analysis
- ✅ **Anomaly detection** — Identify outliers
- ✅ **Pattern discovery** — Find hidden patterns

---

## ⭐ Key Features

### Automated Data Preparation

**Feature engineering pipeline:**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

def create_preprocessing_pipeline(
    numeric_features: List[str],
    categorical_features: List[str]
) -> ColumnTransformer:
    """
    Create comprehensive preprocessing pipeline.
    
    Steps:
        - Impute missing values
        - Scale numeric features
        - Encode categorical features
        - Handle outliers
    """
    # Numeric pipeline
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Categorical pipeline
    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combine pipelines
    preprocessor = ColumnTransformer([
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])
    
    return preprocessor
```

### Model Selection

**Automated model comparison:**
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def compare_models(
    X: np.ndarray,
    y: np.ndarray,
    cv: int = 5
) -> pd.DataFrame:
    """
    Compare multiple models using cross-validation.
    
    Returns:
        DataFrame with model performance metrics
    """
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100),
        'Gradient Boosting': GradientBoostingClassifier(),
        'SVM': SVC()
    }
    
    results = []
    for name, model in models.items():
        # Cross-validation scores
        scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
        
        results.append({
            'Model': name,
            'Mean Accuracy': scores.mean(),
            'Std Accuracy': scores.std(),
            'Min Accuracy': scores.min(),
            'Max Accuracy': scores.max()
        })
    
    return pd.DataFrame(results).sort_values('Mean Accuracy', ascending=False)
```

### Hyperparameter Tuning

**Automated grid search:**
```python
from sklearn.model_selection import GridSearchCV

def optimize_hyperparameters(
    model,
    X: np.ndarray,
    y: np.ndarray,
    param_grid: Dict[str, List],
    cv: int = 5
) -> Tuple[Any, Dict]:
    """
    Find optimal hyperparameters using grid search.
    
    Returns:
        - Best model
        - Best parameters
    """
    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=cv,
        scoring='accuracy',
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X, y)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_, grid_search.best_params_

# Example: Random Forest tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

best_model, best_params = optimize_hyperparameters(
    RandomForestClassifier(),
    X_train,
    y_train,
    param_grid
)
```

### Model Evaluation

**Comprehensive evaluation:**
```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)

def evaluate_model(
    model,
    X_test: np.ndarray,
    y_test: np.ndarray
) -> Dict[str, Any]:
    """
    Comprehensive model evaluation.
    
    Returns:
        - Accuracy metrics
        - Confusion matrix
        - Classification report
        - ROC curve data
    """
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    # Metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    # Classification report
    report = classification_report(y_test, y_pred)
    
    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
    
    # ROC curve (for binary classification)
    if y_pred_proba is not None and len(np.unique(y_test)) == 2:
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], 'k--', label='Random')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve')
        plt.legend()
        plt.show()
        
        metrics['roc_auc'] = roc_auc
    
    print("Classification Report:")
    print(report)
    
    return metrics
```

### Feature Importance

**Identify key features:**
```python
def plot_feature_importance(
    model,
    feature_names: List[str],
    top_n: int = 20
) -> pd.DataFrame:
    """
    Plot and return feature importances.
    
    Works with:
        - Tree-based models (Random Forest, Gradient Boosting)
        - Linear models (coefficients)
    """
    # Get importances
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
    elif hasattr(model, 'coef_'):
        importances = np.abs(model.coef_[0])
    else:
        raise ValueError("Model doesn't support feature importance")
    
    # Create DataFrame
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=False).head(top_n)
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.barh(range(len(importance_df)), importance_df['importance'])
    plt.yticks(range(len(importance_df)), importance_df['feature'])
    plt.xlabel('Importance')
    plt.title(f'Top {top_n} Feature Importances')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    
    return importance_df
```

### Model Deployment

**Save and load models:**
```python
import joblib

def save_model(
    model,
    filename: str,
    metadata: Dict = None
) -> None:
    """
    Save model with metadata for deployment.
    
    Args:
        model: Trained model
        filename: Path to save
        metadata: Additional info (features, version, etc.)
    """
    model_package = {
        'model': model,
        'metadata': metadata or {},
        'timestamp': pd.Timestamp.now(),
        'scikit_learn_version': sklearn.__version__
    }
    
    joblib.dump(model_package, filename)
    print(f"Model saved to {filename}")

def load_model(filename: str) -> Tuple[Any, Dict]:
    """
    Load saved model.
    
    Returns:
        - Model object
        - Metadata dictionary
    """
    model_package = joblib.load(filename)
    
    print("Model loaded successfully!")
    print(f"Saved on: {model_package['timestamp']}")
    print(f"Metadata: {model_package['metadata']}")
    
    return model_package['model'], model_package['metadata']

# Usage
save_model(
    best_model,
    'plant_classifier.joblib',
    metadata={
        'features': feature_names,
        'accuracy': 0.95,
        'description': 'Random Forest species classifier'
    }
)

# Load for prediction
loaded_model, metadata = load_model('plant_classifier.joblib')
predictions = loaded_model.predict(new_data)
```

---

## 📦 What's Included

### Notebook Structure (16 Cells)

1. **Introduction** — ML workflow overview
2. **Setup** — Install scikit-learn, pandas, matplotlib, seaborn
3. **Data Loading** — Load and preview dataset
4. **Data Exploration** — EDA and visualizations
5. **Feature Engineering** — Create and select features
6. **Train/Test Split** — Split data properly
7. **Preprocessing Pipeline** — Automated data preparation
8. **Model Selection** — Compare multiple algorithms
9. **Hyperparameter Tuning** — Optimize best model
10. **Model Training** — Train final model
11. **Model Evaluation** — Comprehensive metrics
12. **Feature Importance** — Identify key features
13. **Cross-Validation** — Validate robustness
14. **Prediction Examples** — Test with new data
15. **Model Deployment** — Save model
16. **Production Use** — Load and use model

---

## 🚀 Getting Started

### Quick Start: Classification

```python
# 1. Load data
df = pd.read_csv('species_data.csv')
X = df.drop('species', axis=1)
y = df['species']

# 2. Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Create and train pipeline
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('preprocessor', create_preprocessing_pipeline(numeric_cols, categorical_cols)),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)

# 4. Evaluate
metrics = evaluate_model(pipeline, X_test, y_test)
print(f"Accuracy: {metrics['accuracy']:.4f}")

# 5. Save model
save_model(pipeline, 'species_classifier.joblib')
```

### Quick Start: Regression

```python
# 1. Load yield data
df = pd.read_csv('crop_yield.csv')
X = df.drop('yield', axis=1)
y = df['yield']

# 2. Split and train
from sklearn.ensemble import GradientBoostingRegressor

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = GradientBoostingRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 3. Evaluate
from sklearn.metrics import mean_absolute_error, r2_score

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")

# 4. Feature importance
plot_feature_importance(model, X.columns)
```

---

## 💡 Usage Examples

### Example 1: Species Classification

```python
# Classify plant species from measurements
features = ['height', 'leaf_length', 'flower_diameter', 'habitat']
target = 'species'

# Train model
pipeline = Pipeline([
    ('preprocessor', create_preprocessing_pipeline(numeric_cols, categorical_cols)),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)

# Predict new sample
new_plant = pd.DataFrame({
    'height': [150],
    'leaf_length': [8.5],
    'flower_diameter': [3.2],
    'habitat': ['forest']
})

species = pipeline.predict(new_plant)
probability = pipeline.predict_proba(new_plant)

print(f"Predicted species: {species[0]}")
print(f"Confidence: {probability.max():.2%}")
```

### Example 2: Yield Prediction

```python
# Predict crop yield from environmental factors
features = ['temperature', 'rainfall', 'soil_ph', 'fertilizer_amount']
target = 'yield_kg_per_ha'

# Feature engineering
df['temperature_rainfall'] = df['temperature'] * df['rainfall']
df['optimal_ph'] = (df['soil_ph'] - 6.5).abs()  # Distance from optimal

# Train gradient boosting
from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=5
)

model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} kg/ha")
```

### Example 3: Clustering Similar Species

```python
# Group plants by characteristics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Prepare data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Find optimal number of clusters
inertias = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Elbow plot
plt.plot(range(2, 11), inertias, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Final clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Visualize (PCA for 2D)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Species Clusters')
plt.colorbar(label='Cluster')
plt.show()
```

---

## 📚 Related Resources

- [Data Analysis Template](TEMPLATE-Data-Analysis) — Data preparation
- [Greenhouse ML Yield Prediction](Greenhouse-ML-Yield-Prediction) — Real example
- [scikit-learn Documentation](https://scikit-learn.org)

---

## 📄 License

MIT License — Free to use, modify, and distribute

[← Back to Templates](Home#-templates) | [View on GitHub](https://github.com/outobecca/botanical-colabs/blob/main/notebooks/templates/TEMPLATE_machine_learning.ipynb)
