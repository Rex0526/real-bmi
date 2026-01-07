import pandas as pd
import streamlit as st

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["type", "money", "way", "note"])

st.title("記帳")
st.title("請選擇功能")
choose=st.selectbox("歡迎使用，請選擇功能",["1","2","3","4","5","6"],format_func=lambda x:{"1":"收入","2":"支出","3":"查看餘額","4":"歷史紀錄","5":"查看支出","6":"結束"}.get(x), key="choose")
if choose=="1" :
    money=int(st.number_input("請輸入金額：", key="money"))
    way=st.text_input("請輸入類別：", key="way")
    note=st.text_input("請簡短說明：", key="note")
    new_data = pd.DataFrame([{"type": "收入", "money": money, "way": way, "note": note}])
    if st.button("新增"):
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.text("建立成功")
if choose=="2":
    money=int(st.number_input("請輸入金額：", key="money_2"))
    way=st.text_input("請輸入類別：", key="way_2")
    note=st.text_input("請簡短說明：", key="note_2")
    new_data = pd.DataFrame([{"type": "支出", "money": money, "way": way, "note": note}])
    if st.button("新增"):
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
        st.text("建立成功")
if choose=="3":
    summary = st.session_state.data.groupby("type")["money"].sum()
    total_income = summary.get("收入", 0)
    total_expense = summary.get("支出", 0)
    balance = total_income - total_expense
    if st.button("查看餘額"):
        st.write(f"總收入: {total_income}, 總支出: {total_expense}, 當前餘額: {balance}")
    if balance<0:
        st.write("餘額不足")
if choose=="5":
    choice=st.selectbox("A.查看最大支出/B.查看支出總類",["A","B"],format_func=lambda x:{"A":"最大支出","B":"支出種類"}.get(x), key="choice")
    expenses_a = st.session_state.data[st.session_state.data["type"] == "支出"]
    if not expenses_a.empty:
        if choice=="A":
            max_row = expenses_a.loc[expenses_a["money"].idxmax()]
            if st.button("查看最大支出"):
                st.write(f"最大支出金額: {max_row['money']} (類別: {max_row['way']}, 備註: {max_row['note']})")
        elif choice=="B":
            all_type=expenses_a.groupby("way")["money"].sum().reset_index()
            if st.button("查看支出種類"):
                st.write("支出總類:")
                st.write(all_type)
    else:
        st.write("無支出資料")
if choose=="4":
    if not st.session_state.data.empty:
        if st.button("查看歷史紀錄"):
            st.write(st.session_state.data)
    else:
        st.write("無歷史紀錄") 
elif choose=="6":
    st.write("記帳結束")
    st.stop()