import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train_data = pd.read_csv("C:/Users/dince/OneDrive/veri proje/veri setleri/train.csv")
test_data = pd.read_csv("C:/Users/dince/OneDrive/veri proje/veri setleri/test.csv")



print("-- Veri Başarıyla Yüklendi! --")
print(train_data.head())

print("\nVeri Seti Boyutu:", train_data.shape)
print(" ")
print(" ")
print("-- Veri Başarıyla Yüklendi! --")
print(test_data.head())

print("\nVeri Seti Boyutu:", test_data.shape)
print(" ")
print(" ")
print("-- Train Veri Seti Ortalamaları! --")
print(train_data.describe())


def degiskenler(variable):
    cat = train_data[variable]
    sayi = cat.value_counts() 
    
    plt.figure(figsize=(9, 3))
    plt.bar(sayi.index.astype(str), sayi)  
    plt.title(variable)
    plt.ylabel("Frekans / Sayı")
    plt.show()
    
    print(f"{variable} değişkeni dağılımı:\n{sayi}\n")


category1 = ["Survived", "Sex", "Pclass", "Embarked", "SibSp", "Parch"]


for i in category1:
    degiskenler(i)

category2= ["Cabin","Name","Ticket"]
for i in category2:
    print(train_data[i].value_counts())   

def hist(variable):
    plt.figure(figsize=(9, 3))
    plt.hist(train_data[variable])
    plt.xlabel(variable)
    plt.ylabel("frekans")
    plt.title(variable)
    plt .show()

sayisal= ["Fare","Age","PassengerId"]
for i in sayisal:
    hist(i)  

pclass_survived = train_data[["Pclass", "Survived"]].groupby(["Pclass"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print("- Pclass / Survived -")
print(pclass_survived)

sex_survived = train_data[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print("\n- Sex / Survived -")
print(sex_survived)

sibsp_survived = train_data[["SibSp", "Survived"]].groupby(["SibSp"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print("\n- SibSp / Survived -")
print(sibsp_survived)

parch_survived = train_data[["Parch", "Survived"]].groupby(["Parch"], as_index=False).mean().sort_values(by="Survived", ascending=False)
print("\n- Parch / Survived -")
print(parch_survived)


train_data_len = len(train_data)
train_data1 = pd.concat([train_data, test_data], axis=0).reset_index(drop=True)

print("\n--- Eksik Değer İçeren Sütunlar ---")
print(train_data1.columns[train_data1.isnull().any()])

print("\n--- Sütun Bazlı Eksik Veri Sayıları ---")
print(train_data1.isnull().sum())

print("\n--- Embarked Sütununda Boş Olan Satırlar ---")
print(train_data1[train_data1["Embarked"].isnull()])


train_data1.boxplot(column="Fare", by="Embarked")
plt.show() 