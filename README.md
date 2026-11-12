<div align="center">

# 🚢 Titanic – Keşifsel Veri Analizi ve Karar Ağaçları

**Veriyi tanımaktan modele: Titanic yolcularının hayatta kalma analizi**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-11557c?style=for-the-badge)

</div>

---

## 📂 Proje Yapısı

| Aşama | Dosya | İçerik |
|---|---|---|
| **1. EDA** | `veriler/analiz.py` | Veri yapısı, dağılımlar, Survived ile ilişkiler |
| **2. Modelleme** | `titanic_karar_agaci.ipynb` | Veri temizleme, karar ağacı, Random Forest |

---

## 1️⃣ Keşifsel Veri Analizi (EDA)

- Veri setinin genel yapısının incelenmesi (`head()`, `shape`, `describe()`)
- Kategorik değişkenlerin (Survived, Sex, Pclass, Embarked, SibSp, Parch) bar grafikleriyle görselleştirilmesi
- Sayısal değişkenlerin (Fare, Age) histogramlarla incelenmesi
- Pclass, Sex, SibSp ve Parch değişkenlerinin Survived ile ilişkisinin `groupby` ile analizi
- Train ve test setleri birleştirilerek eksik veri analizi
- Fare değişkeninin Embarked limanına göre boxplot ile karşılaştırılması

---

## 2️⃣ Modelleme: Karar Ağaçları 🌳

### 🧹 Veri Hazırlığı
| Sorun | Çözüm | Neden |
|---|---|---|
| `Cabin` %77 boş | Sütun silindi | Doldurulursa sütunun çoğu uydurma değer olur |
| `Age` %20 boş | **Medyan** ile dolduruldu | Uç değerlerden etkilenmez |
| `Embarked` 2 boş | **Mod** ile dolduruldu | Kategorik verinin ortalaması alınamaz |
| `PassengerId`, `Name`, `Ticket` | Silindi | Kimlik niteliğinde, kalıp taşımaz |
| `Sex` / `Embarked` | `map` / one-hot encoding | Model sadece sayı anlar |

Veri %70 train · %15 validation · %15 test olarak bölündü (`stratify` ile).

### 🔍 Ağaç Ne Öğrendi?
`max_depth=3` ile çizilen ağaç, ilk soru olarak **cinsiyeti** seçti:
- Erkeklerin **%19**'u, kadınların **%75**'i hayatta kalmış
- 3,5 yaş altındaki erkek çocukların 12'sinden 11'i yaşamış
- 1. ve 2. sınıftaki kadınlarda hayatta kalma oranı **%94**

Ağaç, EDA'da gözlemlenen *"önce kadınlar ve çocuklar"* örüntüsünü veriden kendisi buldu.
k-NN'den farklı olarak her tahminin **nedeni adım adım okunabiliyor**.

### 📈 Derinlik ve Overfitting
| max_depth | Train | Validation | Fark |
|:---:|:---:|:---:|:---:|
| 1 | 0.791 | 0.813 | −0.02 |
| 3 | 0.830 | 0.836 | −0.01 |
| 6 | 0.880 | 0.843 | 0.04 |
| 9 | 0.929 | 0.791 | **0.14** 🔴 |

Derinlik arttıkça validation başarısı düşüyor → **overfitting**.
Benzer başarı veren seçenekler arasından daha basit olan `max_depth=3` tercih edildi.

### 🌲 Tek Ağaç vs Random Forest
| Model | Train | Validation | Fark |
|---|:---:|:---:|:---:|
| Tek Ağaç (max_depth=5) | 0.864 | 0.821 | 0.043 |
| **Random Forest** (200 ağaç) | 0.865 | **0.851** | **0.014** |

### 🧪 Deney: Ağaçlarda Ölçekleme Gerekli mi?
Aynı ağaç ölçeksiz ve MinMaxScaler ile ölçeklenmiş veriyle eğitildi → **134 / 134 tahmin aynı.**
Ağaçlar eşik sorusu sorduğu için ölçekleme sonucu değiştirmez; k-NN gibi mesafe tabanlı modellerde ise zorunludur.

### 🏁 Test Sonucu (Random Forest)
| Accuracy | Precision (Yaşadı) | Recall (Yaşadı) | F1 macro | F1 weighted |
|:---:|:---:|:---:|:---:|:---:|
| 0.784 | 0.775 | 0.608 | 0.76 | 0.78 |

---

## 🚀 Çalıştırma

```bash
pip install -r veriler/requirements.txt
python veriler/analiz.py
```
Modelleme notebook'u Google Colab'da doğrudan açılabilir.

## 🔜 Sonraki Adımlar
- [x] ~~Eksik değerlerin doldurulması~~
- [x] ~~Sınıflandırma modeliyle hayatta kalma tahmini~~
- [ ] `Name` sütunundan unvan (Mr, Mrs, Miss, Master) çıkarımı
- [ ] Aile büyüklüğü (`SibSp + Parch + 1`) değişkeninin
- [ ] 
