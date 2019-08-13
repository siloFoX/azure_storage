import tkinter as tk
import json
import os

from upload import start

PATH = 'Json_data'

date_y = 50
patient_y = 70
doctor_y = 90
site_y = 110
room_y = 130
time_y = 150

data = {
    "_id" : "default",
    "수술날짜" : "default",
    "환자이름" : "default",
    "담당의사" : "default",
    "수술부위" : "default",
    "수술실" : "default",
    "수술시간" : "default"
}

window = tk.Tk()

window.title("DB works")
window.geometry("450x250")
window.resizable(False, False)

entry_width = 20
entry_x = 70
result_x = 250
result_width = 20

def date_save(event) :
    data["수술날짜"] = entry_date.get()
    label = tk.Label(window, text = data["수술날짜"], width = result_width)
    label.place(x = result_x, y = date_y)
    
def patient_save(event) :
    data["환자이름"] = entry_patient.get()
    label = tk.Label(window, text = data["환자이름"], width = result_width)
    label.place(x = result_x, y = patient_y)
    
def doctor_save(event) :
    data["담당의사"] = entry_doctor.get()
    label = tk.Label(window, text = data["담당의사"], width = result_width)
    label.place(x = result_x, y = doctor_y)
    
def site_save(event) :
    data["수술부위"] = entry_site.get()
    label = tk.Label(window, text = data["수술부위"], width = result_width)
    label.place(x = result_x, y = site_y)
    
def room_save(event) :
    data["수술실"] = entry_room.get()
    label = tk.Label(window, text = data["수술실"], width = result_width)
    label.place(x = result_x, y = room_y)

def time_save(event) :
    data["수술시간"] = entry_time.get()
    label = tk.Label(window, text = data["수술시간"], width = result_width)
    label.place(x = result_x, y = time_y)
    
def transport() :
    data["_id"] = data["수술날짜"] + data["환자이름"] + data["수술부위"]
    
    with open(os.path.join(PATH, data["_id"] + '.json'), mode = "w", encoding = "UTF-8") as f :
        f.write(json.dumps(data, ensure_ascii = False, indent = '\t'))
    
    label = tk.Label(window, text = "저장 중입니다. 프로그램을 끄지 마세요.", width = 40)
    label.place(x = 180, y = 200)

    try :
        start()

        label = tk.Label(window, text = "저장 완료했습니다.", width = 40)
        label.place(x = 180, y = 200) 

    except Exception as e:
        
        print(e)

        label = tk.Label(window, text = "저장에 실패했습니다.", width = 40)
        label.place(x = 180, y = 200) 



label_main = tk.Label(window, text = "각 줄마다 정보를 입력하고 enter를 꼭 눌러주세요.", fg = "red")
label_sub = tk.Label(window, text = "정보를 전부 다 입력하신 후에 전송 버튼을 눌러주세요. | result |")
label_date = tk.Label(window, text = "   날짜 ")
label_patient = tk.Label(window, text = "환자이름")
label_docter = tk.Label(window, text = "담당의사")
label_site = tk.Label(window, text = "수술부위")
label_room = tk.Label(window, text = " 수술실 ")
label_time = tk.Label(window, text = "수술시간")

label_main.place(x = 0, y = 0)
label_sub.place(x = 0, y = 20)
label_date.place(x = 0, y = date_y)
label_patient.place(x = 0, y = patient_y)
label_docter.place(x = 0, y = doctor_y)
label_site.place(x = 0, y = site_y)
label_room.place(x = 0, y = room_y)
label_time.place(x = 0, y = time_y)

entry_date = tk.Entry(window, width = entry_width)
entry_patient = tk.Entry(window, width = entry_width)
entry_doctor = tk.Entry(window, width = entry_width)
entry_site = tk.Entry(window, width = entry_width)
entry_room = tk.Entry(window, width = entry_width)
entry_time = tk.Entry(window, width = entry_width)

entry_date.bind('<Return>', date_save)
entry_patient.bind('<Return>', patient_save)
entry_doctor.bind('<Return>', doctor_save)
entry_site.bind('<Return>', site_save) 
entry_room.bind('<Return>', room_save)
entry_time.bind('<Return>', time_save)

entry_date.place(x = entry_x, y = date_y)
entry_patient.place(x = entry_x, y = patient_y)
entry_doctor.place(x = entry_x, y = doctor_y)
entry_site.place(x = entry_x, y = site_y)
entry_room.place(x = entry_x, y = room_y)
entry_time.place(x = entry_x, y = time_y)

button = tk.Button(window, text = "전송", overrelief = "raised", command = transport, width = 10, repeatdelay = 1000, repeatinterval = 100)
button.place(x = 100, y = 200)

window.mainloop()