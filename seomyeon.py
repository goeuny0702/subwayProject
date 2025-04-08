import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
from tkinter import font
from tkinter import PhotoImage
from PIL import Image, ImageTk

info_window = tk.Tk()
info_window.title("서면역")
info_window.geometry("1000x800+450+100") 

bm_font = font.Font(family="배달의민족 을지로체 TTF", size=13)

# 배경 이미지 지정
img1 = Image.open("image/breadBoard2.png")
img1 = img1.resize((1000, 800), Image.LANCZOS)  # 최신 Pillow에 맞게 수정
img1 = ImageTk.PhotoImage(img1)

# 캔버스 생성
can = Canvas(info_window, width=1000, height=800)
can.pack(fill="both", expand=True)

# 배경 이미지 추가
can.create_image(0, 0, image=img1, anchor="nw")

# 캔버스 위에 텍스트 추가
can.create_text(500, 280, text="🍞 희와제과", font=bm_font, fill="black")
can.create_text(500, 300, text="운영시간: 07:00 - 19:00", font=bm_font, fill="black")
can.create_text(500, 320, text="주소: 부산 부산진구 전포대로246번길 6 1층 상가", font=bm_font, fill="black")

can.create_text(500, 370, text="🍞 라푀유크로와상", font=bm_font, fill="black")
can.create_text(500, 390, text="운영시간: 10:30 - 24:00", font=bm_font, fill="black")
can.create_text(500, 410, text="주소: 부산 부산진구 중앙대로680번가길 38 1층 111호 라푀유크로와상", font=bm_font, fill="black")

can.create_text(500, 460, text="🍞 뭉구점 비건베이커리", font=bm_font, fill="black")
can.create_text(500, 480, text="운영시간: 12:00 - 19:00", font=bm_font, fill="black")
can.create_text(500, 500, text="주소: 부산 부산진구 서전로37번길 26 B동 1층 156호", font=bm_font, fill="black")


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
