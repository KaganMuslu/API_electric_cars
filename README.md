
# Cheapest Electric Cars - API

Bu projenin amacı, [Kaggle](https://www.kaggle.com)'dan almış olduğum ["En Ucuz Elektrikli Arabalar"](https://www.kaggle.com/datasets/kkhandekar/cheapest-electric-cars) datasetini çeşitli metodlarla parse ederek [FastAPI](https://fastapi.tiangolo.com) araclılığıyla sunmak ve kullanıcılara kolay erişim sağlamaktır.

Bu API kullanıcılara, elektrikli arabaların marka, model, batarya kapasitesi, menzil, enerji verimliliği, şarj süresi, gibi teknik özelliklerini, ayrıca ülke bazlı fiyatlarını ve diğer detaylarını sunar. 

Böylece, bu verileri kullanarak uygulamalar veya web siteleri oluşturabilir, bu bilgilere dayalı araç karşılaştırması yapabilir veya müşteriler için bir fiyat teklifi hazırlanabilir.


## API Kullanımı

#### Tüm öğeleri getir

```
  GET /cars
```

![Ekran görüntüsü 2023-10-17 231353](https://github.com/KaganMuslu/API_electric_cars/assets/71410113/c63e9469-8854-4551-a0e5-883ed8e1f2ae)


#### Öğeyi getir

```
  GET /cars/{car_id}
```

![Ekran görüntüsü 2023-10-17 231550](https://github.com/KaganMuslu/API_electric_cars/assets/71410113/32f5a29e-1534-4ffe-9f20-e64e241632f5)


#### Marka-Model ile filtreleme

```
  GET /cars/name/{car_name}
```

![Ekran görüntüsü 2023-10-17 231142](https://github.com/KaganMuslu/API_electric_cars/assets/71410113/d9635424-1e0c-4dea-aa97-46bd9194f29a)


#### Öğe ekle

```
  POST /cars
```

![Ekran görüntüsü 2023-10-17 232355](https://github.com/KaganMuslu/API_electric_cars/assets/71410113/004dab66-cb7f-4e13-8366-e7959df5e36a)


#### Öğe verisi değiştir

```
  PUT /cars/{car_id}
```

#### Öğe sil

```
  DELETE /cars/{car_id}
```

![Ekran görüntüsü 2023-10-17 232546](https://github.com/KaganMuslu/API_electric_cars/assets/71410113/0bed4992-916f-468a-9862-322cc8a55884)


