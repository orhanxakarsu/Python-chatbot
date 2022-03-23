# Python-chatbot
Word2vec yöntemiyle chatbot oluşturma.

word2vec modeli linki : https://drive.google.com/drive/folders/1IBMTAGtZ4DakSCyAoA4j7Ch0Ft1aFoww
!!!! Modelle py uzantılı dosyalar aynı klasörde olsun.

* Burada ilk olarak elimizdeki liste halinde tutulan soru- cevap senaryolarındaki soru kısmından stopwords kelimeleri çıkartıyoruz. 
* Daha sonra noktalama işaretlerini kaldırıp word2vec modeliyle vektörize hale getiriyoruz. 
* Daha sonra aynı cümledeki kelime vektörlerini birbiriyle toplayıp bu sözlük yapısına her bir senaryo için yeni eleman olarak ekliyoruz.
* Dikkat ederseniz sözlükteki bazı value'ler string tipinde değil int tipindedir. Bunun nedeni int tipindeki value'yi sonradan işleyecek olmamızdır.


Bu chatbot'un amacı Fatih'teki kültürel ve tarihi mekanlar hakkında kullanıcıların sorularını cevaplamaktır. Chatbot'un mimarisi neredeyse tamamdır. Sadece veri ekleme işlemi kaldı. O da çok zamanımı aldığından şu anlık yapmadım. Fakat eldeki verilerle gayet iyi çalışmakta.

Burada sorguyu direkt vektörize etmeye çalışmıyoruz. İlk olarak sorgu içerisinde, veri setimizdeki tür isimlerini arıyoruz. Eğer eşleşen olursa daha sonra, eşleşen türdeki tarihi eserlerin içindeki mekan isimlerini arıyoruz. Bunda da eşleşen olursa bu iki bilgiyi cümleden çıkarıp sorguyu anlamak için ;
* İlk olarak gelen sorgudaki noktalama işaretlerini, stopwords kelimeleri çıkarıyoruz. Daha sonra elimizdeki cümledeki kelimeleri teker teker vektörize edip bunları topluyoruz. 
* Daha sonra bu toplanmış vektörlerle elde ettiğimiz yeni vektörü, dizi halinde tuttuğumuz sorgu-cevap senaryolarının sorgu vektörleriyle cos benzerliği kullanarak arasındaki açının cos değerini alıyoruz. Birbirine en yakın olan cümlelerin sözlükteki value değerini döndürüyoruz.
* Gelen değer string ise direkt olarak yazdırılıyor. Eğer string değilse gelen int değere göre gerekli olan bilgi döndürülüyor.


Ses tanıma- sesle yazma işlemlerini de opsiyonel class olarak ekledim. Kolay bir şekilde entegre edebilirsiniz.

Son olarak chatbot'u test etmek için ufak bir streamlit kodu yazdım. O da sorunsuz çalışmakta.
