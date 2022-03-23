import string
import requests
import numpy as np
from bs4 import BeautifulSoup,NavigableString, Tag
from fake_useragent import UserAgent
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import speech_recognition as sr
from gtts import gTTS
import os
import time
import streamlit as st
import json
#from mekanYapilari import Cevapla,ButunYapilar




class ChatBot:
    
    def __init__(self):
        self.word_vectors = KeyedVectors.load_word2vec_format('trmodel', binary=True)
        self.dataSetVektorizeDurumu=False
        
        #Burata soruları yazıyoruz. int olan value'leri diğer dosyada işleyeceğiz.
        self.dataSet= [{'soru': 'nerede','cevap':0},
                       {'soru': 'ne zaman yapıldı','cevap':1},
                       {'soru':'adres','cevap':2},
                       {'soru':'nedir','cevap':3},
                       {'soru':'Merhaba','cevap':"Merhaba dost. Sana nasıl yardımcı olabilirim ?"},
                       {'soru':'Uygulama bilgi','cevap':'Bu uygulama sayesinde Fatih\'te olan ; \n Turistik yerleri keşfedebilir,\n Bilmediğin yeni yerleri öğrenebilir,\n Bu bilmediğin yerlerde güzel vakit geçireceğini düşündüğümüz aktiviteleri öğrenebilir,\n bu bilmediğin yerlerin yakınındaki seveceğini düşündüğümüz restorantları öğrenebilir,\n bütün bunların yanında senin kişisel özelliklerini baz alarak sana özel mekanları öğrenebilirsin. '},
                       {'soru':'kimsin','cevap':'Ben sana yardımcı olmak için görevli bir asistanım dost :)'}
                       
                       
                       ]
        

        
        
        with open('veriler.json') as json_file:
            self.stopWords = json.load(json_file)
    
    
    # Cümledeki stopwordsleri kaldırır.
    def etkisizKelimeOlmayanCumle(self,cumle):
        
        
        cumle = cumle.lower()
        cumle = cumle.translate(str.maketrans('','', string.punctuation))
        kelimeler = cumle.split()
        for i,kelime in enumerate(kelimeler):
            if kelime in self.stopWords:
                
                kelimeler.pop(i)
      
        return kelimeler
        
                
    # dot, norm ve cos fonksiyonları cos benzerliği için kullanılır. Bu algoritmayla birbirine en benzeyen cümleleri çıkaracağız.
    
    def dot(self,dizi1,dizi2):
        
        return sum([dizi1[i]*dizi2[i] for i in range(len(list(dizi1)))])
    
    
    def norm(self,dizi):
        
        return np.sqrt(self.dot(dizi,dizi))
    
    
    def cos(self,dizi1,dizi2):
        
        return self.dot(dizi1,dizi2)/(self.norm(dizi1)*self.norm(dizi2))
    
    
    
    # Bunun sayesinde elimizdeki word_vectors word2vec modeliyle kelimeleri vektör haline getiriyoruz.
    def vektorize(self,cumle):
        duzeltilmisCumle = self.etkisizKelimeOlmayanCumle(cumle)

        #bosDizi = [word_vectors[kelime] for kelime in duzeltilmisCumle]
        bosDizi =[]
        toplam=0
        #print(duzeltilmisCumle)
        for kelime in duzeltilmisCumle:
            try:
                
                bosDizi.append(self.word_vectors[kelime])
                toplam+=1
            except:
                continue
        
        if len(bosDizi)!=0:
            sonDizi=[0 for a in range(len(bosDizi[0]))]
        #print(bosDizi)
        for i in range(len(bosDizi[0])):
            for j in range(toplam):
                sonDizi[i]+=bosDizi[j][i]
        ortalamaDizi = list(np.array(sonDizi)/toplam)
        

        return ortalamaDizi
    
    # Burada da  gelen soruya cevap döndüren bir fonksiyon var. 
    def cevapDondur(self,cumle):
        #İlk yapacağımız şey eğer elimizdeki dataset vektörize edilmemişse bütün cümlelerini vektörize etmektir.
        if not self.dataSetVektorizeDurumu :
            for i in range(len(self.dataSet)):
                self.dataSet[i]['vektorizeEdilmisSoru']=self.vektorize(self.dataSet[i]['soru'])
            self.dataSetVektorizeDurumu=True
        
        
        vektorizeEdilmisCumle = self.vektorize(cumle)
        benzerlikDizisi = [self.cos(vektorizeEdilmisCumle,self.dataSet[i]['vektorizeEdilmisSoru']) for i in range(len(self.dataSet)) ]
        
        
        toplanmisDizi =[]
        for i in range(len(benzerlikDizisi)):
            toplanmisDizi.append(benzerlikDizisi[i].sum())
        
        
        toplanmisDizi=np.array(toplanmisDizi)
        
        
        
        siralanmisBenzerlikDizisi = toplanmisDizi.argsort()
        

        
        
        
        return self.dataSet[siralanmisBenzerlikDizisi[-1]]['cevap']

    

    
# İsteğe bağlı veriyi sesle de çekebiliriz.
class konusmaBotu:
    def speak(self,audioString):
        tts = gTTS(text=audioString, lang='tr')
        tts.save("audio.mp3")
        os.system("audio.mp3")
    
    def recordAudio(self):#Mikrofonu dinlemeden önce Recognizer(tanıyıcı)mızı tanımlıyoruz.
        r = sr.Recognizer()
        #Burada mikrofondan veri almaya başlıyoruz
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
     
        # Burada google'ın ses tanıma sistemini kullandık bu sistem internet gerektiriyor.
        data = ""
        
        try:
            #burda türkçe olmasını istediğimiz için tanıyıcımızın türkçe sesleri tanımasını ayarlıyoruz.
            data = r.recognize_google(audio, language='tr-tr')
            #burada sesinizin tonuna göre büyük küçük harf geldiği için text verisini lower hale getiriyoruz. 
            data=data.lower()
        #Bu ise gereksiz gürültü sesleri geldiğinde döndüreceği komut
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        return data
    
    


    
        
        
    
    