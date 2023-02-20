
# Cheapest Electric Cars - API

Bu projenin amacı, [Kaggle](https://www.kaggle.com)'dan almış olduğum ["En Ucuz Elektrikli Arabalar"](https://www.kaggle.com/datasets/kkhandekar/cheapest-electric-cars) datasetini çeşitli metodlarla parse ederek [FastAPI](https://fastapi.tiangolo.com) araclılığıyla sunmak ve kullanıcılara kolay erişim sağlamaktır.

Bu API ile kullanıcılara, elektrikli arabaların marka, model, batarya kapasitesi, menzil, enerji verimliliği, şarj süresi, gibi teknik özelliklerini, ayrıca ülke bazlı fiyatlarını ve diğer detaylarını sunar. 

Böylece, bu verileri kullanarak uygulamalar veya web siteleri oluşturabilir, bu bilgilere dayalı araç karşılaştırması yapabilir veya müşteriler için bir fiyat teklifi hazırlanabilir.


## API Kullanımı

#### Tüm öğeleri getir

```
  GET /cars
```

#### Öğeyi getir

```http
  GET /cars/{car_name}
```

#### Marka-model ile filtreleme

```http
  GET /cars/name/{car_name}
```

#### Öğe ekle

```http
  POST /cars
```

#### Öğe verisi değiştir

```http
  PUT /cars
```

#### Öğe sil

```http
  DELETE /cars
```

