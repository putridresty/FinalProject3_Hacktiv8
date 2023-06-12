import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('heartfailure_predict.sav', 'rb'))

st.title("Prediksi Kematian Akibat Gagal Jantung")

# Membagi visualisasi menjadi 2 kolom
col1, col2= st.columns(2)

with col1:
    Umur = st.number_input('Berapa usia pasien?') 
with col2:
    Anemia = st.selectbox('Apakah pasien memiliki anemia: (0=YA, 1=TIDAK)', (0,1)) 
with col1:
    KadarKeratin = st.number_input('Berapakah kadar keratin pasien: (mL)') 
with col2:
    Diabetes = st.selectbox('Apakah pasien memiliki riwayat diabetes: (0=YA, 1=TIDAK)', (0,1)) 
with col1:
    KadarFraksiEnjeksi = st.number_input('Berapakah kadar fraksi enjeksi pasien: (%)') 
with col2:
    TekananDarahTinggi = st.selectbox('Apakah pasien menderita tekanan darah tinggi: (0=YA, 1=TIDAK)', (0,1)) 
with col1:
    Trombosit = st.number_input('Berapakah besaran trombosit pasien: (mcL)')
with col2:
    KadarSerumKeratin = st.number_input('Berapakah kadar serum keratin pasien: (mg/dL)')    
with col1:
    KadarSodiumSerum = st.number_input('Berapakah kadar sodium keratin pasien: (mEq/L)')
with col2:
    JenisKelamin = st.selectbox('Jenis kelamin pasien (0=Wanita, 1=Pria)', (0,1))
with col1:
    Perokok = st.selectbox('Apakah pasien merokok: (0=YA, 1=TIDAK)', (0,1)) 
with col2:
    Hari = st.number_input('Berapa hari pasien membutuhkan waktu untuk tindak lanjut?')

data_predict = [Umur, Anemia, KadarKeratin, Diabetes, KadarFraksiEnjeksi, TekananDarahTinggi,
         Trombosit, KadarSerumKeratin, KadarSodiumSerum, JenisKelamin, Perokok, Hari]

predict = ''

if st.button("Prediksi"):
    predict = model.predict([data_predict])
    if(predict[0]==1):
        heartfailure_predict = 'Dipredikasi Pasien Meninggal sebelum jadwal Follow-up'
    else:
        heartfailure_predict = 'Diprediksi Pasien bertahan ketika jadwal Follow-up'
    
    st.success(heartfailure_predict)
