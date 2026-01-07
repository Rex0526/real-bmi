import streamlit as st

def BMI計算():
    high = st.number_input("身高為(公分)：", min_value=0.0)
    weight = st.number_input("體重為(公斤)：", min_value=0.0)
    if high <= 0:
        st.warning("身高必須大於 0")
        return

    high2 = (high / 100) ** 2
    BMI = weight / high2

    st.write(f"你的 BMI 是：{BMI:.2f}")

    if BMI < 18.5:
        st.write("體重過輕")
    elif BMI < 24:
        st.write("體重剛好")
    elif BMI < 27:
        st.write("過重")
    else:
        st.write("肥胖")

BMI計算()


