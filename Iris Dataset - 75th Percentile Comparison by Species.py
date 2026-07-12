import numpy as np

# ============================================================
# Iris Dataset - 75th Percentile Comparison by Species
# Dataset:
#   Iris_setosa
#   Iris_versicolor
#   Iris_virginica
#
# Features:
# PL = Petal Length
# PW = Petal Width
# SL = Sepal Length
# SW = Sepal Width
#
# Goal:
# Compare the 75th percentile (Q3) of each feature for all
# three Iris species.
# ============================================================


# -------------------------------
# 1. Petal Length (PL)
# -------------------------------
print("75th Percentile - Petal Length")
print("Setosa      :", np.percentile(Iris_setosa["PL"], 75))
print("Versicolor  :", np.percentile(Iris_versicolor["PL"], 75))
print("Virginica   :", np.percentile(Iris_virginica["PL"], 75))


# -------------------------------
# 2. Petal Width (PW)
# -------------------------------
print("\n75th Percentile - Petal Width")
print("Setosa      :", np.percentile(Iris_setosa["PW"], 75))
print("Versicolor  :", np.percentile(Iris_versicolor["PW"], 75))
print("Virginica   :", np.percentile(Iris_virginica["PW"], 75))


# -------------------------------
# 3. Sepal Length (SL)
# -------------------------------
print("\n75th Percentile - Sepal Length")
print("Setosa      :", np.percentile(Iris_setosa["SL"], 75))
print("Versicolor  :", np.percentile(Iris_versicolor["SL"], 75))
print("Virginica   :", np.percentile(Iris_virginica["SL"], 75))


# -------------------------------
# 4. Sepal Width (SW)
# -------------------------------
print("\n75th Percentile - Sepal Width")
print("Setosa      :", np.percentile(Iris_setosa["SW"], 75))
print("Versicolor  :", np.percentile(Iris_versicolor["SW"], 75))
print("Virginica   :", np.percentile(Iris_virginica["SW"], 75))