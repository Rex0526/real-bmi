import datetime
import streamlit as st
import pandas as pd
class User_info:
    def __init__(self, name, gender, birth):
        self.name=name
        self.gender=gender
        self.birth=birth
        self.record=[]
    def calculate_bmi(self, height, weight):
        bmi = round(weight / ((height / 100) ** 2), 2)
        if bmi < 18.5: result = "體重過輕"
        elif bmi < 24: result = "體重剛好"
        elif bmi < 27: result = "過重"
        else: result = "肥胖"
        return bmi, result

    def add_record(self, height, weight, date, save_db=True):
        bmi, result = self.calculate_bmi(height, weight)
        new_entry = {"date": date, "height": height, "weight": weight, "bmi": bmi, "result": result}
        if save_db:
                self.record.append(new_entry)
                st.write(f"BMI: {bmi}")
                st.write(f"{result}")
if 'users' not in st.session_state:
    st.session_state.users = {}
title=st.title("BMI計算器")
choose=st.selectbox("歡迎使用，請選擇功能",["1","2","3","4","5"],format_func=lambda x:{"1":"新增使用者","2":"輸入身高、體重","3":"查詢歷史紀錄","4":"更新、刪除BMI紀錄","5":"退出"}.get(x), key="choose")
if choose=="1":
    name=st.text_input("請輸入姓名：", key="name_1")
    if name in st.session_state.users:
        st.write(" 該使用者已存在！")
    else:
        gender=st.text_input("請輸入性別(男/女)：", key="add_gender")
        birth = st.text_input("請輸入生日 (YYYY-MM-DD): ", key="add_birth")
        if st.button("新增使用者"):
            try:
                datetime.datetime.strptime(birth, '%Y-%m-%d')
                st.session_state.users[name] = User_info(name, gender, birth)
                st.write("建立成功")
            except ValueError:
                st.error("格式有誤！請確保格式為 xxxx-xx-xx")
elif choose=="2":
    name=st.text_input("使用者姓名：", key="name_2")
    if name in st.session_state.users:
        a_user=st.session_state.users[name]
        h=st.number_input("請輸入身高(公分)：", key="height")
        w=st.number_input("請輸入體重(公斤)：", key="weight")
        d=st.text_input("請輸入今天日期(xxxx-xx-xx)：", key="date")
        if st.button("計算 BMI"):
            if h <= 0:
                st.write("身高必須大於 0")
            if datetime.datetime.strptime(d, '%Y-%m-%d'):
                a_user.add_record(h, w, d)
            else:
                st.write("ValueError")
                st.write("請確保格式為 xxxx-xx-xx")
    else:
        st.write("無該使用者，請先建立身分")
elif choose=="3":
    name=st.text_input("請輸入姓名：", key="name_3")
    if st.button("查看歷史紀錄"):
        if name in st.session_state.users:
            b_user=st.session_state.users[name]
            st.write(f"{b_user.name}的紀錄")
            c=sorted(b_user.record, key=lambda x: x['date'])
            for r in c:
                st.write(f"日期：{r['date']}\n| BMI值：{r['bmi']}\n| 狀態：{r['result']}")
        else:
            st.write("無該使用者")
elif choose=="4":
    name=st.text_input("請輸入使用者姓名：", key="name_4")
    if name in st.session_state.users:
        c_user=st.session_state.users[name]
        choose2=st.selectbox("選擇功能",["1","2"],format_func=lambda x:{"1":"修改","2":"刪除"}.get(x), key="choose_2")
        t_date=st.text_input("輸入要修改的日期", key="t_date")
        found=False
        for i, r in enumerate(c_user.record):
            if str(r['date']) == t_date:
                found = True
                if choose2 == "1":
                    n_height = float(st.number_input(f"原身高為 {r['height']}, 請輸入新身高：", key="n_height"))
                    n_weight = float(st.number_input(f"原體重為 {r['weight']}, 請輸入新體重：", key="n_weight"))
                    n_date = st.text_input(f"原日期為 {r['date']}, 請輸入新日期或留空已不修改)：", key="n_date") or t_date
                    if st.button("修改"):
                        try: 
                            datetime.datetime.strptime(n_date, '%Y-%m-%d')
                            n_bmi, n_result=c_user.calculate_bmi(n_height, n_weight)
                            c_user.record[i] = {
                                "date": n_date, "height": n_height, "weight": n_weight, 
                                "bmi": n_bmi, "result": n_result
                            }
                            st.write("已修改")
                            st.write(f"新BMI為:{n_bmi}，{n_result}")
                        except ValueError: 
                            st.write("輸入格式錯誤，修改失敗")
                else:
                    c_user.record.remove(r)
                break
        if not found: st.write("找不到該日期的紀錄")   
    else:
        st.write("尚未建立資料")
elif choose=="5":
    if st.button("退出"):
        st.write("謝謝使用")
        st.write("請關閉視窗")
        st.stop()
else:
    st.write("輸入有誤，請重新輸入")