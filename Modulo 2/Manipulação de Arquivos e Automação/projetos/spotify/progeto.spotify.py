import streamlit as st 

musicas = { 
     "Luis Fonsi":{
         "Despacito":"https://www.youtube.com/watch?v=kJQP7kiw5Fk"
     },
     "Nacho":{
         "Materialista":"https://www.youtube.com/watch?v=RxhgLTS5eAg"
         }
}
st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("selecione o artista" , musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)
for musicas in musicas_artista.items():
    titulo,link = musicas 
    st.subheader(titulo)
    st.video(link)
