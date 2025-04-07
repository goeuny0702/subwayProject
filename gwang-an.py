import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
from tkinter import font

info_window = tk.Tk()
info_window.title("광안역")
info_window.geometry("1000x800")

bm_font = font.Font(family="배달의민족 을지로체 TTF", size=13)

# 배경 이미지 지정
img1 = Image.open("breadBoard2.png")
img1 = img1.resize((1000, 800), Image.LANCZOS)  # 최신 Pillow에 맞게 수정
img1 = ImageTk.PhotoImage(img1)

# 캔버스 생성
can = Canvas(info_window, width=1000, height=800)
can.pack(fill="both", expand=True)

# 배경 이미지 추가
can.create_image(0, 0, image=img1, anchor="nw")

# 캔버스 위에 텍스트 추가
can.create_text(500, 280, text="🍞 하우스멜", font=bm_font, fill="black")
can.create_text(500, 300, text="운영시간: 12:00 - 19:00", font=bm_font, fill="black")
can.create_text(500, 320, text="주소: 부산 수영구 광안로49번길 87 1층", font=bm_font, fill="black")

can.create_text(500, 370, text="🍞 달럽", font=bm_font, fill="black")
can.create_text(500, 390, text="운영시간: 10:00 - 20:00", font=bm_font, fill="black")
can.create_text(500, 410, text="주소: 부산 수영구 수영로 551 103호", font=bm_font, fill="black")

can.create_text(500, 460, text="🍞 올선데이", font=bm_font, fill="black")
can.create_text(500, 480, text="운영시간: 10:00 - 21:30", font=bm_font, fill="black")
can.create_text(500, 500, text="주소: 부산 수영구 광안로61번길 28 1층", font=bm_font, fill="black")

can.create_text(500, 550, text="🍞 비비비", font=bm_font, fill="black")
can.create_text(500, 570, text="운영시간: 09:30 - 20:00", font=bm_font, fill="black")
can.create_text(500, 590, text="주소: 부산 수영구 수영로582번길 21 1층", font=bm_font, fill="black")

# 닫기 버튼을 캔버스에 추가하려면 create_window 사용
close_button = tk.Button(
    info_window,
    text="닫기",
    command=info_window.destroy,
    font=bm_font,
    bg="#A97142",         # 따뜻한 브라운 (Milk chocolate tone)
    fg="white",           # 글자색 흰색으로 깔끔하게
    activebackground="#8B5E3C",  # 클릭 시 진한 브라운
    activeforeground="white",
    relief="flat",        # 테두리 없이
    padx=10,
    pady=5
)
can.create_window(900, 750, window=close_button)

info_window.mainloop()
