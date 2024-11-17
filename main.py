import streamlit as st
import pandas as pd

# Datos de las cotizaciones desde la imagen
data = {
    "Método": ["Payoneer", "Wise", "PayPal", "Stablecoins"],
    "Transferencia Bancaria": [1060.77, 1072.06, 959.21, 1128.48],
    "Efectivo ARS": [1046.67, 1060.77, 936.64, 1072.06],
    "Efectivo USD": ["7%", "6.5%", "17%", "5.25%"],
    "USDT": ["5.25%", "4.5%", "13.5%", "-"]
}

df = pd.DataFrame(data)

# Mostrar tabla de cotizaciones
st.title("Calculadora de Conversión de Divisas 💱")
st.subheader("Cotizaciones más utilizadas")
st.dataframe(df.set_index("Método"), use_container_width=True)

# Paso 1: Ingresar monto
with st.expander("Paso 1: Ingresa el monto en USD", expanded=True):
    monto = st.number_input("Monto en USD:", min_value=1.0, value=100.0, label_visibility="collapsed")
    st.write(f"Monto ingresado: {monto} USD")

# Paso 2: Seleccionar método
with st.expander("Paso 2: Selecciona el método de cambio"):
    metodo = st.selectbox("Método de cambio:", df["Método"], label_visibility="collapsed")

# Paso 3: Seleccionar tipo de conversión
with st.expander("Paso 3: Selecciona el tipo de conversión"):
    tipo_cambio = st.radio("Tipo de conversión:", ["Transferencia Bancaria", "Efectivo ARS", "Efectivo USD", "USDT"], label_visibility="collapsed")

# Calcular el resultado
rate = df.loc[df["Método"] == metodo, tipo_cambio].values[0]

if isinstance(rate, str) and "%" in rate:
    porcentaje = float(rate.strip('%')) / 100
    result = monto - (monto * porcentaje)
elif rate == "-":
    result = "No disponible"
else:
    result = monto * rate

# Paso 4: Mostrar el resultado
with st.expander("Paso 4: Resultado"):
    st.write(f"El monto recibido según la cotización de **{metodo}** es:")
    if isinstance(result, str):
        st.warning(result)
    else:
        st.metric(label=f"Equivalente en {tipo_cambio}", value=f"{result:,.2f} ARS")

with st.expander("Paso 5: WhatsApp"):
    st.write(f"Continuar proceso por WhatsApp")
    telefono = "+5491131638720"
    mensaje = f"Hola, quiero convertir {monto} USD usando {metodo} en la modalidad {tipo_cambio}."
    url_whatsapp = f"https://wa.me/{telefono}?text={mensaje.replace(' ', '%20')}"

    st.markdown(f"""
    <a href="{url_whatsapp}" target="_blank">
        <button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-size: 16px; display: block; margin-bottom:20px">
            WhatsApp
        </button>
    </a>
    """, unsafe_allow_html=True)


# Firma al final
st.markdown("""
<hr>
<p style="text-align: center; font-size: 14px;">
    Desarrollado por <a href="https://www.palanca.xyz" target="_blank" style="text-decoration: none; color: #007bff;">Palanca</a> con ❤️ desde 🇦🇷
</p>
""", unsafe_allow_html=True)
