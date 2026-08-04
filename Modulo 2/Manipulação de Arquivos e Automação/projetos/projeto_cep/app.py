import requests #Biblioteca mais facil de se comunicar com APIs

import streamlit as st

cep = st.sidebar.text_input("Digete o CEP que deseja perquisar" , icon="🗺️")
if st.sidebar.button("Pesquisar"): 
    if len(cep)!=8:
        st.error("CEP invalido,digete sem pontos e traço e verifique os digito ")
        st.stop()

    busca = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    #LIÇAO 
    # Mostrar as informaçoes do endereço(variavel busca)
    #Mostrar em un mapa usando a latitude e logitude (variavel busca[st.map()])
    # Melhorar validaçao de CEP
    # VOCE PRECISA SER CAPAZ DE ENTENDER TUDO O QUE A IA GERA !!!

    busca = busca.json()

    st.write("CEP:",busca["cep"])
    st.write("Rua:", busca["address"])
    st.write("Bairro:", busca["district"])
    st.write("Cidade:", busca["city"])
    st.write("Estado:", busca["state"])
    import pandas as pd
    mapa = pd.DataFrame({
        "lat": [float(busca["lat"])],
        "lon": [float(busca["lng"])]
    })

    st.map(mapa)