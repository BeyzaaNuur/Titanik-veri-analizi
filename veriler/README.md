# Titanic Veri Seti - Keşifsel Veri Analizi (EDA)

Bu proje, klasik Titanic yolcu veri seti üzerinde yapılan bir keşifsel veri
analizi (Exploratory Data Analysis) çalışmasıdır. Python, pandas ve matplotlib
kullanılarak veri setinin yapısı incelenmiş, kategorik ve sayısal değişkenlerin
dağılımları görselleştirilmiş, ve hayatta kalma (Survived) değişkeni ile diğer
değişkenler arasındaki ilişkiler analiz edilmiştir.

## Proje Kapsamı

- Veri setinin yüklenmesi ve genel yapısının incelenmesi (`head()`, `shape`, `describe()`)
- Kategorik değişkenlerin (Survived, Sex, Pclass, Embarked, SibSp, Parch) frekans
  dağılımlarının bar grafikleriyle görselleştirilmesi
- Sayısal değişkenlerin (Fare, Age) histogramlarla incelenmesi
- Pclass, Sex, SibSp ve Parch değişkenlerinin Survived ile ilişkisinin
  gruplama (`groupby`) yöntemiyle analizi
- Train ve test setlerinin birleştirilerek eksik veri analizinin yapılması
- Fare değişkeninin Embarked limanına göre boxplot ile karşılaştırılması

## Kullanılan Veri Seti

`veri setleri/train.csv` ve `veri setleri/test.csv` dosyaları, Titanic yolcu
bilgilerini (isim, yaş, cinsiyet, bilet sınıfı, ücret, liman vb.) içerir.

## Kurulum ve Çalıştırma

```bash
pip install -r requirements.txt
python main
```

## Kullanılan Kütüphaneler

- pandas
- numpy
- matplotlib

## Sonraki Adımlar

Bu proje şu an EDA aşamasında tamamlanmıştır. Planlanan sonraki adımlar:

- Eksik değerlerin (Age, Embarked, Fare) doldurulması
- Name sütunundan unvan (Title) çıkarımı ve aile büyüklüğü gibi yeni
  değişkenlerin türetilmesi
- Basit bir sınıflandırma modeliyle (Logistic Regression vb.) hayatta kalma
  tahmini yapılması
