import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
#import numpy as np
#import cv2
#import pandas as pd
#from st_aggrid import AgGrid
#import plotly.express as px
#import io 

st.set_page_config(layout="wide")
image = Image.open('infographicnotebook.png')
st.image(image)
st.markdown("<h1 style='text-align: center; color: orange; font-size:55px ; font-family: 'Cooper Black'>TEAM PROJECT: CYBERSECURITY</h1>", unsafe_allow_html=True)

choose = option_menu(None, ["Intro", "News", "Risk", "Protect", "Member", "Contact"], 
                    icons=['house', 'newspaper', 'asterisk', 'shield-check','person', "upc-scan"], 
                    menu_icon="cast", default_index=0, orientation="horizontal",
                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "green"},
    }
)

police = Image.open('polisi.png')
pencuri = Image.open('pencuri.png')
antivirus = Image.open('antivirus.png')
protek = Image.open('protek.png')
if choose == "Intro":
    st.markdown("""Cybersecurity Fundamentals: 
    A Real-World Perspective explains detailed concepts within computer networks and computer security 
    in an easy-to-understand way, making it the perfect introduction to the topic.""")
    st.write("""The short definition of cybersecurity is, 
    “The protection of software, hardware, and data resources connected and stored 
    on the Internet is known as the cybersecurity”. From an individual to a large corporation, 
    everybody is concerned about the security of their online data, software, and information. 
    The protection of the personal, financial data, commercial data, business-critical information, 
    operational continuity, data integrity, and availability of online software services fall in the cybersecurity domain. 
    Regulating the physical access and control- ling the malicious intrusion, allowing the authorized access, 
    encrypting the valuable information, and safeguarding the privacy are the components of cybersecurity.
    Cybersecurity is one of the most important domains in the field of information technology.
    There are two spellings for it, “Cybersecurity” and “Cyber Security”. 
    Cybersecurity is basically the name of standard practices that involve the people,
    technology, and processes in an organiza- tion, in a team, or even in a stand-alone environment 
    in which the computers with the valuable data are connected to the Internet or the Intranet. 
    Cybersecurity deals with the different procedures that create an environment of full security.""")
        
   
elif choose == "News":
#Add the cover image for the cover page. Used a little trick to center the image
    col1, col2 = st.columns( [1, 1])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Lindungi Akun Media Sosialmu</p>', unsafe_allow_html=True)
        st.write("""Sosial media sudah menjadi bagian aktifitas keseharian kita. Jumlahnya pun terus mengalami peningkatan.
        Tapi ada hal yang perlu penggunanya waspadai yakni KEAMANAN. Berhati-hatilah dalam menginstall aplikasi
        di smartphone maupun aplikasi komputer/laptop/tablet mu. Kenapa??? Mari kita baca artikel dari CNBC di bawah ini. """)
        st.image(antivirus, width=700)    
        
    with col2:
        st.image(police, width=700) 
        st.write("""Jakarta, CNBC Indonesia - Sebanyak 214 juta data pribadi dari akun Facebook, Instagram, dan LinkedIn dikabarkan
        bocor di internet. Pelanggaran data besar ini diungkap oleh peneliti Safety Detectives.
        Data yang dicuri termasuk alamat email, nomor telepon serta nama lengkap pengguna, dan dalam beberapa
        kasus, data lokasi tertentu.
        Dalam laporan Safety Detectives disebutkan lebih dari 400 GB data pribadi yang bocor berasal dari Socialarks
        yang dicuri. Ini adalah perusahaan manajemen media sosial asal China.
        Database ElesticSearch menjadi sasaran pelaku kejahatan online, di mana lebih dari 318 juta catatan telah disita.
        Safety Detectives menyebut database ini dibuat setelah data pengguna 'dihapus' dari Facebook, Instagram, dan
        Linkedin.
        sumber :https://www.cnbcindonesia.com/tech/20210114181641-37-216058/data-pribadi-214-juta-pengguna-facebook-instagram-dicuri """)
       
elif choose == "Risk":
    col1, col2 = st.columns( [1, 1])
    with col1:               # To display brand logo
        st.image(pencuri,  width=700)
    with col2:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Apa saja risiko kejahatan siber akun media sosial?</p>', unsafe_allow_html=True)
        st.write("""Data Pribadi. \n\nDari data pribadi meliputi nama, tanggal lahir, alamat, email, NIK,  nomor telepon, dll.
        \n\n1.  Disalahgunakan untuk  membobol rekening(keuangan kita)
        \n\n2. Disalahgunakan untuk penipuan pinjaman online
        \n\n3. Disalahgunakan untuk kepentingan politik
        \n\n4. Disalahgunakan untuk kejahatan siber di dunia maya
        \n\nFoto dan Video
        \n\nDari data foto dan video pribadi milikmu
        \n\n1.  Disalahgunakan untuk  membobol rekening(keuangan kita)
        \n\n2. Disalahgunakan untuk penipuan pinjaman online
        \n\n3. Disalahgunakan untuk kepentingan politik
        \n\n4. Disalahgunakan untuk kejahatan siber di dunia maya termasuk manipulasi visual""") 
    
elif choose == "Protect":
    col1, col2 = st.columns( [1, 1])
    with col1:               # To display brand logo
        st.image(protek, width=700)
    with col2:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Tips Mencegah Kejahatan Siber Pada Media Sosial</p>', unsafe_allow_html=True)
        st.write("""Kadang kita lengah atau mungkin tak menyadari bahaya yang mengancam sosial media
        dimulai saat : 
        \n\n1.  Install aplikasi, pastikan aplikasi yang kamu install resmi dan aman
        \n\n2. Baca baik-baik ketentuan privacy and police
        \n\n3. Jangan sembarang klik “Allow ” di ketentuan permission
        \n\n4. Jangan akses link-link yang mencurigakan dan modus penipuan
        \n\n5. Berhati-hati saat menggunakan layanan wifi di tempat umum
        \n\n6. Ubah password mu secara berkala dan jangan pernah menggunakan nama dan tanggal lahir
        \n\n7. Bijaksanalah menggunakan media sosial
        \n\n8. Bisa pakai fitur private jika tersedia pada aplikas1.  Disalahgunakan untuk  membobol rekening(keuangan kita)
        """) 
     

elif choose == "Member":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Team Project Cybersecutiry: JUMANJI (Jeddah, Umroini, Alfhiyana)</p>', unsafe_allow_html=True)

    st.subheader('Jeddah Yanti')
    st.markdown('Jobdesk : Coding web berbasis streamlit')

    code = '''import streamlit as st \nfrom streamlit_option_menu import option_menu \nimport streamlit.components.v1 as html \nfrom  PIL import Image'''
    st.code(code, language='python')

    st.subheader('Umroini')
    st.markdown('Jobdesk : Pembuatan konten tema cybersecurity')

    st.subheader('Alfhiyana')
    st.markdown('Jobdesk :  ')

    #Display the first code snippet
    


elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Hubungi lebih lajut:</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): 
        Name=st.text_input(label='Nama Lengkap') 
        Email=st.text_input(label='Email') 
        Pesan=st.text_input(label='Pesan') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Terima kasih kepada Ibu Prima, Bapak Hef, Mbak Dio, serta seluruh Tim Kominfo yang telah berkontribusi. ')