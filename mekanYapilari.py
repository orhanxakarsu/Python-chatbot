

from kullanilacakFonksiyonlar import ChatBot
import random
    
    
    

class Cevapla():
        
        
    def __init__(self):
        self.cb = ChatBot()


        self.mekanlar = ButunYapilar().yapilar
        
    def cevapDondur(self,soru):
        soru = soru.lower()
        
        
        
        elemanIntMi = False
        for i,eleman in enumerate(list(self.mekanlar.values())):
            if eleman[0].tur in soru:
                
                soru=soru.replace(eleman[0].tur,'')
                
                for j,elemanIsim in enumerate(eleman):
                    if elemanIsim.isim.lower() in soru:
                        
                        soru=soru.replace(elemanIsim.isim,'')
                        cevap = self.cb.cevapDondur(soru)
        
                        if cevap==0:
                            elemanIntMi=True
                            return self.mekanlar[list(self.mekanlar.keys())[i]][j].adres.adresGetir()
                        elif cevap ==3:
                            elemanIntMi=True
                            return self.mekanlar[list(self.mekanlar.keys())[i]][j].aciklama
                        elif cevap ==1:
                            elemanIntMi=True
                            return elemanIsim.isim+' '+ elemanIsim.tur+ " "+str(self.mekanlar[list(self.mekanlar.keys())[i]][j].yil)+ ' '+'yılında kurulmuştur dost '

        if elemanIntMi ==False:       
            cevap = self.cb.cevapDondur(soru)
            return cevap
                
                
                

    




class Adres:
    
    
    def __init__(self,mahalle=None,cadde=None,sokak=None,no=None):

        self.mahalle = mahalle
        self.cadde = cadde
        self.sokak = sokak
        self.no =no
        
        
    
    def adresGetir(self):
        if self.sokak == None:
            return f'İstanbul ili, Fatih ilçesi, {self.mahalle} mahallesi, {self.cadde} caddesi,{self.no} numaralı yerdedir.'
        elif self.sokak != None:
            return f'İstanbul ili, Fatih ilçesi, {self.mahalle} mahallesi, {self.cadde} caddesi, {self.sokak} sokağı,{self.no} numaralı yerdedir.'
            
    
        
    


class Mekan:
    yil = random.randint(1300, 1800)
    def __init__(self,isim):
        self.isim = isim
        
    
    def aciklamaEkle(self,aciklama):
        self.aciklama = aciklama

    def adresEkle(self,adres):
        self.adres = adres
    
    def tarihEkle(self,yil):
        self.yil = yil
        



class Carsi(Mekan):
    tur = 'çarşı'
    def __init__(self,isim):
        super().__init__(isim)


class Hamam(Mekan):
    tur = 'hamam'
    def __init__(self,isim,cinsiyet):
        super().__init__(isim)
        self.cinsiyet = cinsiyet


class Kapi(Mekan):
    tur = 'kapı'
    def __init__(self,isim):
        
        super().__init__(isim)
    

class Kosk(Mekan):
    tur = 'köşk'
    def __init__(self,isim):
        super().__init__(isim)


class Medrese(Mekan):
    tur = 'mekan'
    
    def __init__(self,isim):
        super().__init__(isim)



class Muze(Mekan):
    tur ='müze'
    
    def __init__(self,isim):
        super().__init__(isim)
        

class Saray(Mekan):
    tur = 'saray'
    
    def __init__(self,isim):
        super().__init__(isim)


class Sarnic(Mekan):
    tur = 'sarnıç'
    
    def __init__(self,isim):
        super().__init__(isim)

class Anit(Mekan):
    tur = 'anıt'
    
    def __init__(self,isim):
        super().__init__(isim)



class Cesme(Mekan):
    tur = 'çeşme'
    
    def __init__(self,isim):
        super().__init__(isim)
class ButunYapilar:

    def __init__(self):
        self.yapilar = {
            'çarşılar':[Carsi('At Pazarı'),
                        Carsi('Bab-ı Ali'),
                        Carsi('Beyazıt Meydanı'),
                        Carsi('Mısır')
                        ],
            'hamamlar':[Hamam('2. Beyazıt','Erkek-Kadın'),
                        Hamam('Ağa','Erkek'),
                        Hamam('Balat Çavuş','Erkek'),
                        Hamam('Nişanca','Kadın')
                        ],
            
            'kapılar': [Kapi('Ahır'),
                        Kapi('Altın'),
                        Kapi('Belgrad'),
                        Kapi('Cibali'),
                        Kapi('Dördüncü Askeri'),
                        Kapi('Eğri'),
                        Kapi('Eski Aya'),
                        Kapi('Konstantin')
                        ],
            
            'köşkler': [Kosk('Çinili')],
            
            'medreseler':[Medrese('Ankaravi Mehmet Efend i'),
                          Medrese('Davut Paşa'),
                          Medrese('Ekmekçizade Ahmet Paşa'),
                          Medrese('Gevher Sultan'),
                          Medrese('Hacı Beşir Ağa'),
                          Medrese('Halil Efendi')
                          ],
            
            'müzeler':[Muze('Basın'),
                       Muze('Büyüksaray Mozaikleri'),
                       Muze('Fethiye'),
                       Muze('İslam Bilim ve Teknoloji Tarihi'),
                       Muze('İtfaiye'),
                       Muze('Karikatür ve Mizah')
                       ],
            'saraylar':[Saray('Antiyokus'),
                        Saray('Boğdan'),
                        Saray('Bukaleon'),
                        Saray('Magnavra'),
                        Saray('Topkapı')
                        ],
            'sarnıçlar':[Sarnic('Altımermer'),
                         Sarnic('Binbirdirek'),
                         Sarnic('Bizans'),
                         Sarnic('Çukurbostan Aspar'),
                         Sarnic('Myrelaion'),
                         Sarnic('Sultan'),
                         Sarnic('Yerebatan')
                         
                         ],
            'anıtlar': [Anit('Fatih'),
                        Anit('İmrahor İlyas Bey'),
                        Anit('Millon')
                        ],
            'çeşmeler': [Cesme('abbas ağa'),
                         Cesme('ABDİ ÇELEBİ'),
                         Cesme('AKAĞASI HAYDAR PAŞA'),
                         Cesme('AKBIYIK'),
                         Cesme('ALİ AĞA'),
                         Cesme('ALİ EFENDİ'),
                         Cesme('ALİŞAH EFENDİ'),
                         Cesme('alman')
                         ]
            
            }
        
        self.aciklamaEkle(0,0,"Fatih'in Cihangir'i olarak bilinen At Pazarı İstanbul'un eski meydanlarından. Osmanlı döneminde at satılan bir yer olan bu meydan günümüzde çeşitli kafelerin yer aldığı gençlerin popüler mekanları arasında.")
        self.aciklamaEkle(0,1,"Bâb-ı Âli ya da basitleştirilmiş şekli ile Babıali, Osmanlı Devleti döneminde sadrazam sarayına verilen isimdir. 18. yüzyıl sonlarına yakın bir zamana kadar Paşa sarayı, Paşa kapısı, Bab-ı Asafi gibi adlarda denilen sadrazam sarayına I. Abdülhamid zamanından itibaren Bab-ı Ali denilmeye başlanmıştır.")
        self.aciklamaEkle(0,2,"Beyazıt Meydanı, İstanbul’da tarihî yarımadada merkezî bir konuma sahip meydandır. Konumu Bizans döneminde şehrin en önemli meydanlarından olan Theodosius Forumu’yla büyük ölçüde örtüşmektedir.")
        self.aciklamaEkle(0,3,"Mısır Çarşısı, Eminönü'nde Yeni Camii'nin arkasında ve Çiçek Pazarı'nın yanındadır. İstanbul'un en eski kapalı çarşılarından biridir. Aktarlarıyla meşhur bu çarşıda hâlen tabii ilaçlar, baharat, çiçek tohumları, nadir bitki kök ve kabukları gibi eski geleneğine uygun ürünlerin yanı sıra; kuruyemiş, şarküteri ürünleri, değişik gıda maddeleri satılmaktadır.")
        self.aciklamaEkle(1,0,"Hamamın Beyazıt Külliyesi’nin bir parçası olduğunu söyleyen Yazgülü Turan, “II. Bayezid Hamamı, Yavuz Sultan Selim’in annesi II. Bayezıd’ın eşi Gülbahar Hatun tarafından vakıf yapısı olarak inşa edilmiş.")
        self.aciklamaEkle(1,1,"Ağa Hamamı 1454 yılında Osmanlı Padişahı Fatih Sultan Mehmet tarafından inşaa ettilmiştir. Fatih Sultan Mehmet'in ve şehzadelerinin özel hamamı olarak kullanılmıştır.")
        self.aciklamaEkle(1,2,"Haliç kıyısında aynı addaki mahallede, Mimar Sinan’ın eseri olan Ferruh Kethüdâ veya Balat Camii’nin yanında bulunmaktadır.")
        self.aciklamaEkle(2,0,"Ahırkapı, İstanbul’un tarihsel semtlerinden biridir ve Sarayburnu gibi tarihi bir saray bölgesidir.")
        self.aciklamaEkle(2,1,"Altın Kapı, Bizans imparatorlarının özellikle Avrupa’ya yapılacak seferlere gidişlerde ve sefer dönüşlerinde ve ihtişamlı törenlerle kullanılmıştır.")
        self.aciklamaEkle(2,2,"İki yuvarlak kule arasında bulunan kapı içte Despot'un Kapısına dışta Leopol'un Kapısına birer köprüyle bağlanır.")
        self.aciklamaEkle(2,3,"Haliç’in kıyısında yer alan bu tarihi semtin girişinde yine aynı isim ile anılan Cibali kapısı yer alır. Günümüze kadar çok azı ulaşan bu kapılardan biri olan Cibali Kapı ve ismini verdiği semt oldukça ilginç hikayelerle doludur. Çok eski medeniyetlerden itibaren beri şehrin etrafı güvenlik amacıyla inşa edilmiş surlarla çevriliydi. Ve girişler bu kapılardan yapılmaktaydı.")
        self.aciklamaEkle(3,0,"Çinili Köşk, Topkapı Sarayı'nın dış surlarının içinde yer alan, 1472 yılından kalma bir köşktür.[1] Osmanlı sultanı II. Mehmed tarafından yazlık saray ya da köşk olarak yaptırılmıştır.")
        self.aciklamaEkle(4,0,"Herhangi bir külliyeye bağlı olmadan tek yapı olarak inşa edildi. Ancak, giriş tarafı hariç 3 tarafı çevredeki yapılarla çevriliydi. Günümüzde ise İstanbul Belediye Sarayı'nın güney tarafında tek başına bir yapıdır.")
        self.aciklamaEkle(4,1,"Davud Paşa Medresesi, II. Bayezid dönemi vezirlerinden Koca Davud Paşa tarafından yaptırılmış, içerisinde cami, medrese, mektep, mahkeme, aşevi gibi yapı ve kurumlar barındıran, 1485 yılında yapımı tamamlanan bir külliyedir.")
        self.aciklamaEkle(4,2,"Ekmekçizade Ahmet Paşa Medresesi; İstanbul Suriçi Vefa'da Cemal Yener Tosyalı Caddesi ile Taş Mektepler Sokağı'nın birleştiği köşede Molla Hüsrev Camisi karşısında 1618 tarihinde inşa edilmiştir. Ekmekçizade Ahmet Paşa, Sultan I.Ahmet döneminde görev yapmış bir maliyeci ve vezir idi. Burası ufak bir külliyedir.")
        self.aciklamaEkle(5,0,"Türkiye Gazeteciler Cemiyeti'ne kiralanan yapı 1984-1988 yılları arasında restore edildi ve 9 Mayıs 1988 tarihinde Basın Müzesi olarak hizmete açıldı.")
        self.aciklamaEkle(5,1,"ammakaristos Kilisesi 1261 Latin egemenliğinin son bulmasından sonra eski kilisenin kalıntıları üzerine yeniden yaptırılmıştır.")
        self.aciklamaEkle(5,2,"İstanbul’da Gülhane Parkı’nın içindeki Saray Sur Duvarına bitişik Has Ahırlar Binası’nda yer alır. Osmanlı Dönemi’nde, padişahın ve yakın hizmetindekilerin atlarının bulunduğu ahırlara Has Ahır (İstabl-ı amire) denilmiştir")
        self.aciklamaEkle(6,0,"Sarayın yapısı 1940 ve 1950'li yıllarda Hipodrom'a yakın yapılan kazılarda ortaya çıkarılmıştır, kalanların bazıları hala görülebilir durumdadır.")
        self.aciklamaEkle(7,0,"Yerebatan ve Binbirdirek sarnıçlarından sonra İstanbul’un en büyük üçüncü su havuzudur")
        self.aciklamaEkle(8,0,"1985 yılında yapılması için girişimlerde bulunulan Fatih Sultan Mehmet Anıtı 1987 yılında Hüseyin Gezer tarafından yapılmış ve Fatih’teki İtfaiye Parkı’na konulmuştur.")
        self.aciklamaEkle(9,0,"Üsküdar’da Hayrettin mahallesinde Dutlu kahve mevkiinde ( Toptaşı cad- Ferah sokak köşe) köşe başında bulunan bu çeşmeyi yaptıran Darüssaade Ağası Abbas Ağadır. Bu çeşmeye “ Ağalar başı çeşmesi” de denilmektedir.")
        
        
        
        self.adresEkle(0, 0, 'Zeyrek', ' Eski Mutaflar',None, '34083')
        self.adresEkle(0,1,"Hoca Paşa","Alayköşkü",None,"29")
        self.adresEkle(0, 2, "Beyazıt", "Ordu ", None, "34134")
        self.adresEkle(1,0,"Balabanağa"," Kimyager Derviş Paşa",None,"2")
        self.adresEkle(1, 1, "Kuloglu ", "Turnacibasi ", "Aga Hamami", "48 ")
        self.adresEkle(1, 2, 'Sümbül Efendi', '34107', '?', '34107')
        self.adresEkle(2,0,"Cankurtaran","Ahırkapı ",None,"56")
        self.adresEkle(3,0,'Cankurtaran',"Osman Hamdibey Yokuşu",None,'34122')
        self.adresEkle(4,0,"Kemal Paşa","Ahmet Selahattin",None,"23")
        self.adresEkle(4, 1, 'Cerrahpaşa', 'Hekimoğlu Ali Paşa','Davutpaşa Medresesi ', '1')
        self.adresEkle(4,2,"Mollahüsrev","Taş Tekneler",None,'35')
        
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        self.tarihEkle(0, 1, 1456)
        
    def yapiEkle(self,yapiNo,yapi):
        self.yapilar[str(list(self.yapilar.keys())[yapiNo])].append(yapi)
    
    def aciklamaEkle(self,yapiNo,mekanNo,yapiAciklamasi):
        self.yapilar[str(list(self.yapilar.keys())[yapiNo])][mekanNo].aciklamaEkle(yapiAciklamasi)
    
    def adresEkle(self,yapiNo,mekanNo,mahalle,cadde,sokak,no):
        adres = Adres(mahalle, cadde, sokak, no)
        self.yapilar[str(list(self.yapilar.keys())[yapiNo])][mekanNo].adresEkle(adres)
    
    def tarihEkle(self,yapiNo,mekanNo,yil):
        self.yapilar[str(list(self.yapilar.keys())[yapiNo])][mekanNo].tarihEkle(yil)
        
    

    

#a =ButunYapilar()
#a.yapiEkle(0, Carsi('At Pazarı'))


    


    
    
    







        
        
        

