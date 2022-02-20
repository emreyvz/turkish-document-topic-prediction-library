![](https://i.ibb.co/gSPSqrB/banner.png)

# Türkçe Doküman Konusu Tespit Sınıfı | 🇹🇷

Bu Python sınıfını kullanarak dahili dataset ile Türkçe dokümanların konularını birkaç satır kod ile tahmin edebilirsiniz. İçerisinde dahili olarak yer alan ve 4000 içerik, 1060500 kelimeden oluşan verisetinden yararlanır. Multinomial Naive Bayes Sınıflandırıcısı kullanılmıştır.

</br>

> Emre Yavuz tarafından Python ile yazılmıştır  | github.com/emreyvz

</br>

**Kullanılabilecek Methotlar**

- İçeriğin tahmini konusunu bulma | getPrediction(@param)
- Veriseti başarı skorunu getirme | getAccuracyScore()
- Verisetinde yer alan konu adları | getTopics()

</br>

**Verisetinde Yer Alan Konular**

- Politika
- Spor
- Sağlık
- Teknoloji
- Ekonomi
- Magazin
- Askeri

# Turkish Document Topic Prediction Library | 🇬🇧

You can get topic of given Turkish text content with couple lines of code by using this library. The library use an internal dataset that include 4000 different contents and around 1060500 words. Multinomial Naive Bayes Classifer were used in this library.

</br>

> Written by Emre Yavuz  | github.com/emreyvz

</br>

**Available Methods**

- Get topic prediction of given text | getPrediction(@param)
- Get Accuracy score of dataset | getAccuracyScore()
- Get unique topic list from dataset file | getTopics()

</br>

**Avaible Topics**

- Politics
- Sports
- Health
- Technology
- Economics
- Magazine
- Military

# Sample Codes / Örnek Kodlar
---
## Get prediction of given text content | Verilen dokümanın konusunu bulma

```python
from TurkishTopicPredictLibrary import *

TopicPredict = TurkishTopicPredict()
detectedTopic = TopicPredict.getPrediction("İklim değişikliğinin en önemli nedenlerinden biri, sera gazlarına yol açan fosil yakıtlar. Bu nedenle fosil yakıtlara yeni alternatifler aranıyor. Bu alternatiflerden biri de biyoyakıt üretiminde kullanılabilen yosunlar. Yosunlar, verimli tarım arazilerine ihtiyaç duymadıkları için tarımsal faaliyetler ile rekabet etmiyorlar. Güneş ışığı ve karbondioksit kullanarak fotosentez yaptıklarından sürdürülebilir koşullar altında üretiliyorlar. Biyorafineriler, konvansiyonel rafinerilerde işlenen fosil yakıtlara alternatif biyoyakıt üretimi yanında katma değerli ek ürünlerin de elde edildiği, sıfır atık temelli ve sürdürülebilir kalkınma odaklı bir model sunuyor.")
print(detectedTopic)
```

</br>

## Get unique topic list from dataset | Verisetinde yer alan konu adlarını göstermek

```python
from TurkishTopicPredictLibrary import *

TopicPredict = TurkishTopicPredict()
print(TopicPredict.getTopics())
```

</br>

## Check Dataset Accuracy Score | Veriseti Doğruluk Skorunu Kontrol Etme

```python
from TurkishTopicPredictLibrary import *

TopicPredict = TurkishTopicPredict()
if TopicPredict.getAccuracyScore() < 50:
    print('Accuracy Score must be greater than 50')
```

</br>

## License / Lisans

<img src="https://opensource.org/files/osi_keyhole_300X300_90ppi_0.png" height="24" width="24">

- **[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)**
- 2022 © Emre Yavuz
