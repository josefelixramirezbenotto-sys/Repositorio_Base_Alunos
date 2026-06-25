import streamlit as st

st.sidebar.title("locadora de veiculo")
st.sidebar.image("carro imagen marca.png")
carro = st.sidebar.selectbox("Selecione o carro que deseja alugar: ",
                     ["Gol","Uno","Voyage","Civic","BMW X7"])

valores_diarias= {"Gol":250,"Uno":100,"Voyage":350,"Civic":600,"BMW X7":1200}

st.image(f"{carro}.png")
st.subheader(f"Valor da diaria:R${valores_diarias[carro]}")

data_retirada = st.date_input("Selecione a data de retirada: ",datetime.now())
data_retirada = st.date_input("Selecione a data da devoluçao:",data_retirada)

if st.bottom("Alugar"):
    dias = data_devolucao - data_retirada
    total = dias * valores_diarias[carro]