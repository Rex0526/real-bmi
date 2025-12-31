import streamlit as st
def BMI計算():
    try:
        high=float(st.number_input("身高為(公分)："))
        weight=float(st.number_input("體重為(公斤)："))
        high2=float((high/100)**2)
        BMI=float(weight/high2)
        st.write(f"你的BMI是：{BMI:.2f}")
        if BMI<18.5:
            st.write("體重過輕")
        elif 24>BMI>=18.5:
           st.write("體重剛好")
        elif 27>BMI>=24:
            st.write("過重")
        else :
            st.write("肥胖")
    except ValueError:
        print("輸入格式有誤")
while True:
    BMI計算()
    A=st.text_input("是否再次測試?Y/N").upper()
    if A=="N":
        st.write("謝謝你的使用")
        break