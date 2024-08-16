import tkinter as tk 
from tkinter import * 
import sqlite3

jendela = tk.Tk()  
jendela.title("Aplikasi Prodi Pilihan")
jendela.geometry("300x400")

# Menghubungkan ke database SQLite dan membuat tabel jika belum ada
conn = sqlite3.connect('prediksi_prodi.db')
c = conn.cursor()

# Membuat tabel jika belum ada
c.execute('''
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matematika REAL,
    geografi REAL,
    inggris REAL,
    hasil_prediksi TEXT
)
''')

conn.commit()

def simpan_database(matematika, geografi, inggris, prediksi):
    c.execute("INSERT INTO nilai_siswa (matematika, geografi, inggris, hasil_prediksi) VALUES (?, ?, ?, ?)",(matematika, geografi, inggris, prediksi))
    conn.commit()

jendela.configure(bg='#eeb3ef')

matematika = tk.DoubleVar() 
inggris = tk.DoubleVar()
geografi = tk.DoubleVar()


def prediksi() :
    
    if int(geografi.get()) < 75 or int(inggris.get()) < 75 or int(matematika.get()) < 75 :
        prediksi_prodi = "tidak lulus"
    elif int(matematika.get()) > int(geografi.get()) and int(matematika.get()) > int(inggris.get()) :
       prediksi_prodi  = "kedokteran"
    elif int(geografi.get()) > int(matematika.get()) and int(geografi.get()) > int(inggris.get()) :
        prediksi_prodi ="Teknik"
    elif int(inggris.get()) > int(geografi.get()) and int(inggris.get()) > int(matematika.get()) :
        prediksi_prodi ="Bahasa"

    hasil_label.config(text=f" {prediksi_prodi} ")
    simpan_database(int(matematika.get()), int(geografi.get()), int(inggris.get()), prediksi_prodi )
    

geografi_label = tk.Label(master=jendela, text=f'Nilai Geografi',
font=('Inter', 12), fg='#4d565d', bg='#cde2f5') 
geografi_label.place (relx=0.5, rely=0.15, anchor='center') 

geografi = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
bg='#f1bfdb', highlightcolor='#FFF0CE', highlightthickness=2,textvariable=geografi) 
geografi.place (relx=0.5, rely=0.22, anchor='center') 

matematika_label = tk.Label(master=jendela, text=f'Nilai Matematika',
font=('Inter', 12), fg='#4d565d', bg='#cde2f5') 
matematika_label.place (relx=0.5, rely=0.28, anchor='center') 

matematika = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
bg='#f1bfdb', highlightcolor="#FFF0CE", highlightthickness=2,textvariable=matematika)
matematika.place (relx=0.5, rely=0.32, anchor='center') 

bahasa_inggris_label = tk.Label(master=jendela, text=f'Nilai bahasa inggris',
font=('Inter', 12), fg='#4d565d', bg='#cde2f5')
bahasa_inggris_label.place (relx=0.5, rely=0.38, anchor='center')

bahasa_inggris = tk.Entry(master=jendela, font=('Inter', 12), width=30, fg='#FFFFFF',
bg='#f1bfdb', highlightcolor="#FFF0CE", highlightthickness=2, textvariable=inggris)
bahasa_inggris.place (relx=0.5, rely=0.42, anchor='center')

prediksi_button = tk.Button(jendela, text='prediksi', command=prediksi) 
prediksi_button.pack() 

hasil_label = tk.Label(jendela, text="")
hasil_label.pack(pady=20)

jendela.mainloop()

conn.close()