from mekanYapilari import Cevapla
import streamlit as st


def main():
    st.markdown('<style>body{background-color: White;}</style>',unsafe_allow_html=True)
    if 'deger' not in st.session_state:
        cb =Cevapla()
        st.session_state['deger']=None
        st.session_state['model']=cb

    


    st.title('Uygulama ChatBot\'u')
    soruForm = st.form(key='form_alani')
    cumle = soruForm.text_input("Bana Soru Sor :",key='soru')
    buton = soruForm.form_submit_button('Gönder')
    if buton:
        st.text(st.session_state['model'].cevapDondur(cumle))
        cumleButonu=False
        
    
    #sesliAsistan = konusmaBotu()
    
    #cumle = 'Merhaba dünya'
    #print(cb.ozetCumlelerDondur([cumle,'Nasılsın dünya','Bu ne böyle'],3))
    """
    cb =Cevapla()
    soru = input("Bana Soru Sor :")
    print(cb.cevapDondur(soru))"""
    #print(cb.word_vectors['nerede'])
    
    #print(cb.cevapDondur(soru))
    
if __name__=='__main__':
    main()

