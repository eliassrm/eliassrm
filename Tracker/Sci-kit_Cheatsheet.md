# 🤖 Scikit-learn Cheat Sheet (with Examples)

A compact reference for **Scikit-learn** (sklearn) — the most popular Python library for machine learning. Includes key functions, modules, and examples in table format.

---

## 🧱 Importing & Basics

| Function / Module                                      | Description                      | Example                                                                    |
| ------------------------------------------------------ | -------------------------------- | -------------------------------------------------------------------------- |
| `import sklearn`                                       | Imports Scikit-learn             | `import sklearn`                                                           |
| `from sklearn import datasets`                         | Access built-in datasets         | `iris = datasets.load_iris()`                                              |
| `from sklearn.model_selection import train_test_split` | Splits data into train/test sets | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)` |
| `from sklearn.preprocessing import StandardScaler`     | Normalizes or standardizes data  | `scaler = StandardScaler(); X_scaled = scaler.fit_transform(X)`            |

---

## 📦 Data Preprocessing

| Function / Class       | Description                                 | Example                                                        |
| ---------------------- | ------------------------------------------- | -------------------------------------------------------------- |
| `StandardScaler()`     | Standardize features (mean=0, var=1)        | `scaler.fit(X_train)`                                          |
| `MinMaxScaler()`       | Scales data to a given range                | `scaler = MinMaxScaler(); X_scaled = scaler.fit_transform(X)`  |
| `LabelEncoder()`       | Encodes categorical labels                  | `encoder.fit_transform(['yes','no','yes']) → [1,0,1]`          |
| `OneHotEncoder()`      | Converts categorical features to binary     | `encoder.fit_transform([[0,1],[1,0]])`                         |
| `SimpleImputer()`      | Fills missing values                        | `imp = SimpleImputer(strategy='mean'); imp.fit_transform(X)`   |
| `PolynomialFeatures()` | Generates polynomial & interaction features | `poly = PolynomialFeatures(2); X_poly = poly.fit_transform(X)` |

---

## 🔍 Model Selection

| Function / Class                          | Description                                    | Example                                                     |
| ----------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| `train_test_split()`                      | Split data into train/test sets                | `X_train, X_test, y_train, y_test = train_test_split(X, y)` |
| `cross_val_score(model, X, y, cv)`        | K-fold cross-validation                        | `cross_val_score(model, X, y, cv=5)`                        |
| `GridSearchCV(estimator, param_grid, cv)` | Performs grid search for hyperparameter tuning | `GridSearchCV(SVC(), {'C':[0.1,1,10]}, cv=5)`               |
| `RandomizedSearchCV()`                    | Randomized hyperparameter search               | `RandomizedSearchCV(model, param_dist, n_iter=10)`          |

---

## ⚙️ Common Algorithms

### 🔢 Linear Models

| Model                  | Description                      | Example                                  |
| ---------------------- | -------------------------------- | ---------------------------------------- |
| `LinearRegression()`   | Fits a linear model              | `model = LinearRegression().fit(X, y)`   |
| `LogisticRegression()` | Binary/multiclass classification | `model = LogisticRegression().fit(X, y)` |
| `Ridge()` / `Lasso()`  | Regularized regression models    | `Ridge(alpha=1.0)`                       |

### 🌳 Tree-Based Models

| Model                          | Description                | Example                                          |
| ------------------------------ | -------------------------- | ------------------------------------------------ |
| `DecisionTreeClassifier()`     | Classification tree        | `model = DecisionTreeClassifier().fit(X, y)`     |
| `RandomForestClassifier()`     | Ensemble of decision trees | `model = RandomForestClassifier().fit(X, y)`     |
| `GradientBoostingClassifier()` | Boosted decision trees     | `model = GradientBoostingClassifier().fit(X, y)` |
| `DecisionTreeRegressor()`      | Regression tree            | `DecisionTreeRegressor().fit(X, y)`              |
| `RandomForestRegressor()`      | Regression using forest    | `RandomForestRegressor().fit(X, y)`              |

### 📈 Support Vector Machines

| Model   | Description               | Example                          |
| ------- | ------------------------- | -------------------------------- |
| `SVC()` | Support Vector Classifier | `SVC(kernel='linear').fit(X, y)` |
| `SVR()` | Support Vector Regression | `SVR(kernel='rbf').fit(X, y)`    |

### 🧠 Neural Networks

| Model             | Description                               | Example                                                           |
| ----------------- | ----------------------------------------- | ----------------------------------------------------------------- |
| `MLPClassifier()` | Multi-layer perceptron for classification | `MLPClassifier(hidden_layer_sizes=(50,), max_iter=500).fit(X, y)` |
| `MLPRegressor()`  | Neural network for regression             | `MLPRegressor().fit(X, y)`                                        |

### 📊 Clustering

| Model                       | Description              | Example                                        |
| --------------------------- | ------------------------ | ---------------------------------------------- |
| `KMeans(n_clusters)`        | K-means clustering       | `KMeans(n_clusters=3).fit(X)`                  |
| `DBSCAN()`                  | Density-based clustering | `DBSCAN(eps=0.5, min_samples=5).fit(X)`        |
| `AgglomerativeClustering()` | Hierarchical clustering  | `AgglomerativeClustering(n_clusters=2).fit(X)` |

---

## 📏 Metrics & Evaluation

| Function                                | Description             | Example                                        |
| --------------------------------------- | ----------------------- | ---------------------------------------------- |
| `accuracy_score(y_true, y_pred)`        | Classification accuracy | `accuracy_score(y_test, y_pred)`               |
| `confusion_matrix(y_true, y_pred)`      | Confusion matrix        | `confusion_matrix(y_test, y_pred)`             |
| `classification_report(y_true, y_pred)` | Precision, recall, f1   | `print(classification_report(y_test, y_pred))` |
| `r2_score(y_true, y_pred)`              | R² for regression       | `r2_score(y_test, y_pred)`                     |
| `mean_squared_error(y_true, y_pred)`    | MSE                     | `mean_squared_error(y_test, y_pred)`           |

---

## 🔄 Model Persistence

| Function                          | Description                     | Example                            |
| --------------------------------- | ------------------------------- | ---------------------------------- |
| `import joblib`                   | Import model persistence module | `import joblib`                    |
| `joblib.dump(model, 'model.pkl')` | Save model                      | `joblib.dump(model, 'model.pkl')`  |
| `joblib.load('model.pkl')`        | Load model                      | `model = joblib.load('model.pkl')` |

---

## 🧩 Pipeline Workflow

| Function / Class             | Description                          | Example                                                           |
| ---------------------------- | ------------------------------------ | ----------------------------------------------------------------- |
| `Pipeline(steps)`            | Chains preprocessing and model steps | `pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])` |
| `pipe.fit(X_train, y_train)` | Fits pipeline                        | `pipe.fit(X_train, y_train)`                                      |
| `pipe.predict(X_test)`       | Makes predictions                    | `pipe.predict(X_test)`                                            |

---

✅ **Tip:** Use `sklearn.show_versions()` to see your Scikit-learn environment setup.
