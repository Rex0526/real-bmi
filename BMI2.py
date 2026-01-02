import datetime
users = {} 
class User_info:
    def __init__(self, name, gender, birth):
        self.name=name
        self.gender=gender
        self.birth=birth
        self.record=[]
    def add_record(self, height, weight, date):
        
        high2=(height/100)**2
        BMI=round(weight/high2)

        if BMI<18.5:
            result=("體重過輕")
        elif 24>BMI>=18.5:
            result=("體重剛好")
        elif 27>BMI>=24:
            result=("過重")
        else :
            result=("肥胖")
        record={
            "date":date,
            "height":height,
            "weight":weight,
            "BMI":BMI,
            "result":result
        }
        self.record.append(record)
        print(f"紀錄成功, BMI: {BMI} ({result})")
while True:
    choose=input("歡迎使用，請選擇功能\n""1.新增使用者\n""2.輸入身高、體重\n""3.查詢歷史紀錄\n""4.更新、刪除BMI紀錄\n""5.退出\n")
    if choose=="1":
        name=input("請輸入姓名：")
        if name in users:
            print(" 該使用者已存在！")
            continue
        gender=input("請輸入性別(男/女)：")
        while True:
            birth = input("請輸入生日 (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(birth, '%Y-%m-%d')
                break
            except ValueError:
                print("格式有誤！請確保格式為 xxxx-xx-xx")
        users[name]=User_info(name, gender, birth)
        print("建立成功")
    elif choose=="2":
        name=input("使用者姓名：")
        if name in users:
            a_user=users[name]
            while True:
                h=input("請輸入身高(公分)：")
                try:
                    height=float(h)
                    break
                except ValueError:
                    print("身高輸入格式有誤, 請確保皆為數字")
            while True:
                w=input("請輸入體重(公斤)：")
                try:
                    weight=float(w)
                    break
                except ValueError:
                    print("體重輸入格式有誤, 請確保皆為數字")
            while True:
                d=input("請輸入今天日期(xxxx-xx-xx)：")
                try:
                    datetime.datetime.strptime(d, '%Y-%m-%d')
                    break
                except ValueError:
                    print("格式有誤！請確保格式為 xxxx-xx-xx")
            a_user.add_record(height, weight, d)
        else:
            print("請先建立身分")
    elif choose=="3":
        name=input("請輸入姓名：")
        if name in users:
            b_user=users[name]
            print(f"{b_user.name}的紀錄")
            c=sorted(b_user.record, key=lambda x: x['date'])
            for r in c:
                print(f"日期：{r['date']}\n| BMI值：{r['BMI']}\n| 狀態：{r['result']}")
        else:
            print("無該使用者")
    elif choose=="4":
        name=input("請輸入使用者姓名：")
        if name in users:
            c_user=users[name]
            choose2=input("要1.修改或2.刪除紀錄")
            t_date=input("輸入要修改的日期")
            found=False
            for r in c_user.record[:]: 
                if r['date'] == t_date:
                    found = True
                    if choose2=="1":
                        try:
                            n_weight=float(input(f"原體重為：{r['weight']}, 請輸入新體重："))
                            n_height=float(input(f"原身高為：{r['height']}, 請輸入新身高："))
                            n_date=input((f"原日期為：{r['date']},請輸入新日期："))
                            c_user.record.remove(r)
                            print("已修改")
                            c_user.add_record(n_height, n_weight, n_date)
                        except ValueError: 
                            print("輸入格式錯誤，修改失敗")
                    else:
                        c_user.record.remove(r)
                        print("已刪除")
                        break
            if not found: print("找不到該日期的紀錄")   
        else:
            print("尚未建立資料")
    elif choose=="5":
        print("謝謝使用")
        break
    else:
        print("輸入有誤，請重新輸入")