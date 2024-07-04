# vitural enviroment => sanal ortamdır. 
# pip install pipenv
# Sanal bir ortam oluşturun. Bunu yapmak için terminalde aşağıdaki komutu yazın:
# pipenv shell
# python -m pipenv shell
# Her şey başarılı olursa, proje klasöründe bir Pip dosyası görünecektir. Bu proje için gereken tüm gereksinimleri ve kitaplıkları listeleyecektir.
# Flask => pip install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="style.css">
                    <title>Anasayfa</title>
                </head>
                <body>
                    <ol>
                        <a href="/sosyal-medya-bagimliligi"><li> Sosyal Medya Bağımlılığı </li></a>
                        <a href="/internet-bagimliligi"><li> İnternet Bağımlılığı </li></a>
                        <a href="/akilli-telefon-bagimliligi"><li> Akıllı Telefon Bağımlılığı </li></a>
                        <a href="/oyun-bagimliligi"><li> Oyun Bağımlılığı </li></a>
                    </ol>
                </body>
                </html>  
            '''

# Akıllı Telefon, İnternet için ve Oyun Bağımlılığı
 
@app.route("/sosyal-medya-bagimliligi")
def sosyal_medya():
    return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Sosyal Medya Bağımlılığı</title>
            </head>
            <body>
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h1>Sosyal Medya Bağımlılığı</h1>
                
                <!-- [TUR]Paragraf => [ENG]Paragraph => [HTML] p -->
                <p>Sosyal medya, gerçek dünyada geçirdiğimiz zamanı azaltır. Ayrıca sürekli güncellemeler ve gönderilerle zihinlerimizi koşullandırır, bu da uzun vadede stresli hale gelebilir.</p>
                <!-- [TUR]Gorsel => [ENG]Image => [HTML] img -->
                <!-- [TUR]Kaynak => [ENG]Source => [HTML] src -->
                <!-- [TUR]Genişlik => [ENG]Width=> [HTML] width -->
                <img width="450px" src="https://1.bp.blogspot.com/-aLBGw_ocK6Y/X1GIyVTzZzI/AAAAAAAABic/Ypm0hDSh09IKC7r5NG8gJ6ZN3kZj9sXlgCLcBGAsYHQ/s1280/sosyal-medya-ba%25C4%259F%25C4%25B1ml%25C4%25B1l%25C4%25B1%25C4%259F%25C4%25B1.jpg" >
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h2>Bu durumla nasıl başa çıkabiliriz?</h2>
                <!--[TUR]Sıralı Liste => [ENG]Order List => [HTML] ol  -->
                <!--[TUR]Sırasız Liste => [ENG]Unorder List => [HTML] ul  -->
                <ul>
                    <!--[TUR]Liste Elemanı => [ENG]List Element => [HTML] li   -->
                    <li>Çevrimiçi/cevrimdışı harcanan zaman için sınırlar belirleyebiliriz </li>
                    <li>Rahatlamak ve dinlenmek için teknolojiden uzak bazı aktivitelerde bulunabilirsiniz.</li>
                </ul>
                <iframe width="560" height="315" src="https://www.youtube.com/embed/C8eIxrkcXfs?si=AKTZ2lej8vfO2JJ1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </body>
            </html>
        '''
@app.route("/internet-bagimliligi")
def internet():
    return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title> İnternet Bağımlılığı </title>
            </head>
            <body>
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h1> İnternet Bağımlılığı </h1>
                
                <!-- [TUR]Paragraf => [ENG]Paragraph => [HTML] p -->
                <p>Sürekli bilgisayar veya mobil cihaz kullanımı uzun süreli oturma pozisyonuna ve hareketsizliğe yol açabilir. Bu durum obezite, kas-iskelet sistemi problemleri, göz yorgunluğu gibi sağlık sorunlarına neden olabilir.</p>
                <!-- [TUR]Gorsel => [ENG]Image => [HTML] img -->
                <!-- [TUR]Kaynak => [ENG]Source => [HTML] src -->
                <!-- [TUR]Genişlik => [ENG]Width=> [HTML] width -->
                <img width="450px" src="https://www.acibadem.com.tr/hayat/Images/YayinTestler/internet-bagimlisi-misiniz-test-edin_1691_1.jpg" >
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h2>Bu durumla nasıl başa çıkabiliriz?</h2>
                <!--[TUR]Sıralı Liste => [ENG]Order List => [HTML] ol  -->
                <!--[TUR]Sırasız Liste => [ENG]Unorder List => [HTML] ul  -->
                <ul>
                    <!--[TUR]Liste Elemanı => [ENG]List Element => [HTML] li   -->
                    <li>İnterneti kullanırken harcanan zaman için sınırlar belirleyebiliriz </li>
                    <li>Birisinden yardım alarak bize sınırlar koymasını isteyebiliriz</li>
                </ul>
                <iframe width="560" height="315" src="https://www.youtube.com/watch?v=Z0KJgHKNcB0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </body>
            </html>
        '''
@app.route("/oyun-bagimliligi")
def oyun():
       return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Oyun Bağımlılığı</title>
            </head>
            <body>
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h1>Oyun Bağımlılığı</h1>
                
                <!-- [TUR]Paragraf => [ENG]Paragraph => [HTML] p -->
                <p>Gereğinden fazla oyun oynamak, gerçek dünyada geçirdiğimiz zamanı azaltır. Ayrıca oyunlara gelen güncellemeler ile zihinlerimizi koşullandırır.</p>
                <!-- [TUR]Gorsel => [ENG]Image => [HTML] img -->
                <!-- [TUR]Kaynak => [ENG]Source => [HTML] src -->
                <!-- [TUR]Genişlik => [ENG]Width=> [HTML] width -->
                <img width="450px" src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.medicalpark.com.tr%2Foyun-bagimliligi%2Fhg-2079&psig=AOvVaw2rgkkFt2PyjXuQfQpTgvvU&ust=1720167510392000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKC_hcD5jIcDFQAAAAAdAAAAABAE" >
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h2>Bu durumla nasıl başa çıkabiliriz?</h2>
                <!--[TUR]Sıralı Liste => [ENG]Order List => [HTML] ol  -->
                <!--[TUR]Sırasız Liste => [ENG]Unorder List => [HTML] ul  -->
                <ul>
                    <!--[TUR]Liste Elemanı => [ENG]List Element => [HTML] li   -->
                    <li>Oyundayken yanımıza kronometre alırız ve oyunda geçirdiğimiz süreyi sayar sonrasında bunu yavaş yavaş azaltabiliriz.</li>
                    <li>Rahatlamak ve dinlenmek için oyundan çıkıp bazı aktivitelerde bulunabilirsiniz.</li>
                </ul>
                <iframe width="560" height="315" src="https://www.youtube.com/watch?v=IahOQPQxSlw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </body>
            </html>
        '''
app.route("/akilli-telefon-bagimliligi")
def akilli_telefon():
       return '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="style.css">
                <title>Akıllı Telefon Bağımlılığı</title>
            </head>
            <body>
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h1>Akıllı Telefon Bağımlılığı</h1>
                
                <!-- [TUR]Paragraf => [ENG]Paragraph => [HTML] p -->
                <p>Akıllı telefon, gerçek dünyada geçirdiğimiz zamanı azaltır. Ayrıca sürekli yeni gelen telefon güncellemeleri ile zihinlerimizi koşullandırır.</p>
                <!-- [TUR]Gorsel => [ENG]Image => [HTML] img -->
                <!-- [TUR]Kaynak => [ENG]Source => [HTML] src -->
                <!-- [TUR]Genişlik => [ENG]Width=> [HTML] width -->
                <img width="450px" src="https://www.google.com/imgres?q=ak%C4%B1ll%C4%B1%20telefon%20ba%C4%9F%C4%B1ml%C4%B1l%C4%B1%C4%9F%C4%B1&imgurl=https%3A%2F%2Fwww.insancaakademi.com%2Fwp-content%2Fuploads%2F2022%2F03%2FAkilli-Telefon-Bagimliligi.jpg&imgrefurl=https%3A%2F%2Fwww.insancaakademi.com%2Fakilli-telefon-bagimliligi%2F&docid=ZgqfUUUfOBGFVM&tbnid=dZHIJy8dsBIjuM&vet=12ahUKEwj_5-zd-oyHAxW5BdsEHZFDAC0QM3oECB4QAA..i&w=1024&h=683&hcb=2&ved=2ahUKEwj_5-zd-oyHAxW5BdsEHZFDAC0QM3oECB4QAA" >
                <!--[TUR]Başlık => [ENG]Headline => [HTML] h1-h6  -->
                <h2>Bu durumla nasıl başa çıkabiliriz?</h2>
                <!--[TUR]Sıralı Liste => [ENG]Order List => [HTML] ol  -->
                <!--[TUR]Sırasız Liste => [ENG]Unorder List => [HTML] ul  -->
                <ul>
                    <!--[TUR]Liste Elemanı => [ENG]List Element => [HTML] li   -->
                    <li>Çevrimiçi/cevrimdışı harcanan zaman için sınırlar belirleyebiliriz </li>
                    <li>Rahatlamak ve dinlenmek için telefondan uzak bazı aktivitelerde bulunabilirsiniz.</li>
                </ul>
                <iframe width="560" height="315" src="https://www.youtube.com/watch?v=Txey7yBuibU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </body>
            </html>
        '''

app.run(debug=True)
