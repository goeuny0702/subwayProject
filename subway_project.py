import tkinter
import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import heapq
import pyttsx3 
from PIL import ImageTk, Image
from renamed_subway_connections import renamed_connections
from tkinter import font
from PIL import ImageFont 

win = tkinter.Tk()
bm_font = font.Font(family="배달의민족 을지로체 TTF", size=13)

#해상도
win.geometry("1460x1067+450-0")
win.title("노선도창")
win.resizable(False, False)

#원 그리기
def circle(can, cx, cy, r, text, color, po='u'):
   can.create_oval(cx-r, cy-r, cx+r, cy+r, outline=color, fill="white", width=3)
   
   if(po == "u"):
        can.create_text(cx, cy-22, text=text, fill="#4e4e4e", font=bm_font, anchor="center")
   elif(po == "d"):
       can.create_text(cx, cy+22, text=text, fill="#4e4e4e", font=bm_font, anchor="center")
   elif(po == 'l'):
       can.create_text(cx-22, cy, text=text, fill="#4e4e4e", font=bm_font, anchor="e")
   elif(po == 'r'):
       can.create_text(cx+22, cy, text=text, fill="#4e4e4e", font=bm_font, anchor="w")

#선 그리기
def line(can, x1, y1, x2, y2, color, width=10):
    can.create_line(x1, y1, x2, y2, fill=color, width=width)


#환승역 이미지 지정
#환승역 이미지는 선언한 뒤에 맨 마지막에 입력하여 사진들 최상단에 위치하게 지정
img = Image.open("interchange.png")
img = img.resize((20, 20))
image = ImageTk.PhotoImage(img)

#배경 이미지 지정
img1 = Image.open("bg4.png")
img1 = img1.resize((1460, 1067))
image1 = ImageTk.PhotoImage(img1)

#Tikinter 캔버스
can = tk.Canvas(win, width=1460, height=1067)
#배경을 가장 먼저 입력하여 이미지들 최하단에 위치
can.create_image(0, 0, image=image1, anchor="nw")

can.pack()


#부산 김해

부원_봉황 = line(can, 235, 105, 280, 105, "purple")
봉황_수로왕릉 = line(can, 280, 105, 330, 105, "purple")
수로왕릉_박물관 = line(can, 330, 105, 380, 115, "purple")
박물관_연지공원 = line(can, 380, 115, 410, 153, "purple")
연지공원_장신대 = line(can, 410, 153, 410, 192, "purple")
장신대_가야대 = line(can, 410, 192, 410, 232, "purple")

부원_김해시청 = line(can, 235, 105, 185, 130, "purple")
김해시청_인재대 = line(can, 185, 130, 175, 169, "purple")
인재대_김해대학 = line(can, 175, 169, 175, 209, "purple")
김해대학_지내 = line(can, 175, 209, 175, 249, "purple")
지내_불암 = line(can, 175, 249, 175, 289, "purple")
불암_대사 = line(can, 175, 289, 175, 329, "purple")
대사_평강 = line(can, 175, 329, 175, 369, "purple")
평강_대저 = line(can, 175, 369, 175, 404, "purple")
대저_등구 = line(can, 175, 404, 175, 469, "purple")
덕두_공항 = line(can, 175, 469, 175, 524, "purple")
공항_서부산유통지구 = line(can, 175, 524, 175, 592, "purple")
서부산유통지구_괘법르네시티 = line(can, 175, 592, 235, 637, "purple")
괘법르네시티_사상 = line(can, 235, 637, 410, 637, "purple")

부원 = circle(can, 235, 105, 10, "부원", "purple")
봉황 = circle(can, 280, 105, 10, "봉황", "purple", 'd')
수로왕릉 = circle(can, 330, 105, 10, "수로왕릉", "purple")
박물관 = circle(can, 380, 115, 10, "박물관", "purple", 'r')
연지공원 = circle(can, 410, 153, 10, "연지공원", "purple", 'r')
장신대 = circle(can, 410, 192, 10, "장신대", "purple", 'r')
가야대 = circle(can, 410, 232, 10, "가야대", "purple", 'r')

김해시청 = circle(can, 185, 130, 10, "김해시청", "purple", 'l')
인재대 = circle(can, 175, 169, 10, "인재대", "purple", 'l')
김해대학 = circle(can, 175, 209, 10, "김해대학", "purple", 'l')
지내 = circle(can, 175, 249, 10, "지내", "purple", 'l')
불암 = circle(can, 175, 289, 10, "불암", "purple", 'l')
대사 = circle(can, 175, 329, 10, "대사", "purple", 'l')
평강 = circle(can, 175, 369, 10, "평강", "purple", 'l')
대저부 = circle(can, 175, 404, 10, "대저", "purple", 'l')
등구 = circle(can, 175, 469, 10, "등구", "purple", 'r')
덕두 = circle(can, 175, 524, 10, "덕두", "purple", 'r')
공항 = circle(can, 175, 592, 10, "공항", "purple", 'r')
서부산유통지구 = circle(can, 235, 637, 10, "서부산유통지구", "purple", 'd')
괘법르네시티 = circle(can, 320, 637, 10, "괘법르네시티", "purple", 'u')

#1호선

노포_범어사 = line(can, 960, 105, 905, 105, "orange")
범어사_남산 = line(can, 905, 105, 845, 110, "orange")
남산_두실 = line(can, 845, 110, 807, 143, "orange")
두실_구서 = line(can, 807, 143, 807, 183, "orange")
구서_장전 = line(can, 807, 183, 807, 227, "orange")
장전_부산대 = line(can, 807, 227, 807, 267, "orange")
부산대_오천장 = line(can, 807, 267, 807, 310, "orange")
온천장_명륜 = line(can, 807, 310, 807, 357, "orange")
명륜_동래 = line(can, 807, 357, 807, 403, "orange")
동래_교대 = line(can, 807, 403, 807, 520, "orange")
교대_연산 = line(can, 807, 520, 807, 580, "orange")
연산_시청 = line(can, 807, 580, 807, 633, "orange")
시청_양정 = line(can, 807, 633, 807, 667, "orange")
양정_부전 = line(can, 807, 667, 807, 700, "orange")
부전_서면 = line(can, 807, 700, 805, 754, "orange")
서면_범내골 = line(can, 805, 754, 787, 805, "orange")
범내골_범일 = line(can, 787, 805, 733, 816, "orange")
범일_좌천 = line(can, 733, 816, 670, 816, "orange")
좌천_부산진 = line(can, 670, 816, 610, 816, "orange")
부산진_초량 = line(can, 610, 816, 555, 816, "orange")
초량_부산역 = line(can, 555, 816, 490, 816, "orange")
부산역_중앙 = line(can, 490, 816, 434, 816, "orange")
중앙_남포 = line(can, 434, 816, 373, 816, "orange")
남포_자갈치 = line(can, 373, 816, 320, 816, "orange")
자갈치_토성 = line(can, 320, 816, 264, 816, "orange")
토성_동대신 = line(can, 264, 816, 200, 830, "orange")
동대신_서대신 = line(can, 200, 830, 177, 858, "orange")
서대신_대티 = line(can, 177, 858, 180, 900, "orange")
대티_괴정 = line(can, 180, 900, 220, 930, "orange")
괴정_사하 = line(can, 220, 930, 235, 937, "orange")
사하_당리 = line(can, 235, 937, 280, 937, "orange")
당리_하단 = line(can, 280, 937, 400, 937, "orange")
하단_신평 = line(can, 400, 937, 460, 937, "orange")
신평_동매 = line(can, 460, 937, 520, 937, "orange")
동매_장림 = line(can, 520, 937, 570, 937, "orange")
장림_신장림 = line(can, 570, 937, 630, 937, "orange")
신장림_낫개 = line(can, 630, 937, 690, 937, "orange")
낫개_다대포항 = line(can, 690, 937, 750, 937, "orange")
다대포항_다대포해수욕장 = line(can, 750, 937, 800, 937, "orange")

노포 = circle(can, 960, 105, 10, "노포", "orange", 'u')
범어사 = circle(can, 905, 105, 10, "범어사", "orange", 'u')
남산 = circle(can, 845, 110, 10, "남산", "orange", 'u')
두실 = circle(can, 807, 143, 10, "두실", "orange", 'r')
구서 = circle(can, 807, 183, 10, "구서", "orange", 'r')
장전 = circle(can, 807, 227, 10, "장전", "orange", 'r')
부산대 = circle(can, 807, 267, 10, "부산대", "orange", 'r')
온천장 = circle(can, 807, 310, 10, "온천장", "orange", 'r')
명륜 = circle(can, 807, 357, 10, "명륜", "orange", 'r')
교대1 = circle(can, 807, 520, 10, "교대", "orange", 'u')
시청 = circle(can, 807, 633, 10, "시청", "orange", 'r')
양정 = circle(can, 807, 667, 10, "양정", "orange", 'r')
부전 = circle(can, 807, 700, 10, "부전", "orange", 'r')
범내골 = circle(can, 787, 805, 10, "범내골", "orange", 'r')
범일 = circle(can, 733, 816, 10, "범일", "orange", 'd')
좌천1 = circle(can, 670, 816, 10, "좌천", "orange", 'u')
부산진 = circle(can, 610, 816, 10, "부산진", "orange", 'd')
초량 = circle(can, 555, 816, 10, "초량", "orange", 'u')
부산역 = circle(can, 490, 816, 10, "부산역", "orange", 'd')
중앙 = circle(can, 434, 816, 10, "중앙", "orange", 'u')
남포 = circle(can, 373, 816, 10, "남포", "orange", 'd')
자갈치 = circle(can, 320, 816, 10, "자갈치", "orange", 'u')
토성 = circle(can, 264, 816, 10, "토성", "orange", 'd')
동대신 = circle(can, 200, 830, 10, "동대신", "orange", 'u')
서대신 = circle(can, 177, 858, 10, "서대신", "orange", 'l')
대티 = circle(can, 180, 900, 10, "대티", "orange", 'l')
괴정 = circle(can, 220, 930, 10, "괴정", "orange", 'u')
사하 = circle(can, 280, 937, 10, "사하", "orange", 'd')
당리 = circle(can, 340, 937, 10, "당리", "orange", 'u')
하단 = circle(can, 400, 937, 10, "하단", "orange", 'd')
신평 = circle(can, 460, 937, 10, "신평", "orange", 'u')
동매 = circle(can, 520, 937, 10, "동매", "orange", 'd')
장림 = circle(can, 570, 937, 10, "장림", "orange", 'u')
신장림 = circle(can, 630, 937, 10, "신장림", "orange", 'd')
낫개 = circle(can, 690, 937, 10, "낫개", "orange", 'u')
다대포항 = circle(can, 750, 937, 10, "다대포항", "orange", 'd')
다대포해수욕장 = circle(can, 800, 937, 10, "다대포해수욕장", "orange", 'u')


#2호선
양산_남양산 = line(can, 647, 105, 647, 145, "green")
남양산_부산대양산캠퍼스 = line(can, 647, 145, 647, 185, "green")
부산대양산캠퍼스_증산 = line(can, 647, 105, 647, 235, "green")
증산_호포 = line(can, 647, 235, 620, 275, "green")
호포_금곡 = line(can, 620, 275, 565, 282, "green")
금곡_동원 = line(can, 565, 282, 508, 282, "green")
동원_율리 = line(can, 508, 282, 452, 284, "green")
율리_화영 = line(can, 452, 284, 413, 324, "green")
화영_수정 = line(can, 413, 324, 413, 364, "green")
수정_덕천 = line(can, 413, 364, 413, 404, "green")
덕천_구명 = line(can, 413, 404, 413, 444, "green")
구명_구낭 = line(can, 413, 444, 413, 484, "green")
구낭_모라 = line(can, 413, 484, 413, 524, "green")
모라_모덕 = line(can, 413, 524, 413, 564, "green")
모덕_덕포 = line(can, 413, 564, 413, 604, "green")
덕포_사상 = line(can, 413, 604, 413, 637, "green")
사상_강전 = line(can, 413, 637, 413, 694, "green")
강전_주례 = line(can, 413, 694, 428, 736, "green")
주례_냉정 = line(can, 428, 736, 477, 756, "green")
냉정_개금 = line(can, 477, 756, 540, 756, "green")
개금_동의대 = line(can, 540, 756, 605, 754, "green")
동의대_가야 = line(can, 605, 754, 645, 754, "green")
가야_부암 = line(can, 645, 754, 740, 754, "green")
부암_서면 = line(can, 740, 754, 805, 754, "green")
서면_전포 = line(can, 805, 754, 890, 754, "green")
전포_국제금융센터부산은행 = line(can, 890, 754, 960, 790, "green")
국제금융센터부산은행_문현 = line(can, 960, 790, 964, 855, "green")
문현_지게골 = line(can, 964, 855, 975, 913, "green")
지게골_못골 = line(can, 975, 913, 1050, 935, "green")
못골_대연 = line(can, 1050, 935, 1118, 948, "green")
대연_경성대부경대 = line(can, 1118, 948, 1118, 900, "green")
경성대부경대_남천 = line(can, 1118, 900, 1118, 850, "green")
남천_금련산 = line(can, 1118, 850, 1118, 800, "green")
금련산_광안 = line(can, 1118, 800, 1118, 700, "green")
광안_수영 = line(can, 1118, 700, 1118, 650, "green")
수영_민락 = line(can, 1118, 650, 1130, 598, "green")
민락_센텀시티 = line(can, 1130, 598, 1148, 558, "green")
센텀시티_벡스코 = line(can, 1148, 558, 1200, 518, "green")
벡스코_동백 = line(can, 1200, 518, 1277, 570, "green")
동백_해운대 = line(can, 1277, 570, 1277, 660, "green")
해운대_중동 = line(can, 1277, 660, 1277, 730, "green")
중동_장산 = line(can, 1277, 730, 1277, 810, "green")

양산 = circle(can, 647, 105, 10, "양산", "green", 'r')
남양산 = circle(can, 647, 145, 10, "남양산", "green", 'r')
부산대양산캠퍼스 = circle(can, 647, 185, 10, "부산대양산캠퍼스", "green", 'r')
증산 = circle(can, 647, 235, 10, "증산", "green", 'r')
호포 = circle(can, 620, 275, 10, "호포", "green", 'd')
금곡 = circle(can, 565, 282, 10, "금곡", "green", 'u')
동원 = circle(can, 508, 282, 10, "동원", "green", 'd')
율리 = circle(can, 452, 284, 10, "율리", "green", 'u')
화영 = circle(can, 413, 324, 10, "화영", "green", 'l')
수정 = circle(can, 413, 364, 10, "수정", "green", 'r')
구명 = circle(can, 413, 444, 10, "구명", "green", 'l')
구낭 = circle(can, 413, 484, 10, "구낭", "green", 'r')
모라 = circle(can, 413, 524, 10, "모라", "green", 'r')
모덕 = circle(can, 413, 564, 10, "모덕", "green", 'r')
덕포 = circle(can, 413, 604, 10, "덕포", "green", 'r')
사상2 = circle(can, 413, 637, 10, "사상", "green", 'r')
강전 = circle(can, 413, 694, 10, "강전", "green", 'r')
주례 = circle(can, 428, 736, 10, "주례", "green", 'r')
냉정 = circle(can, 477, 756, 10, "냉정", "green", 'd')
개금 = circle(can, 540, 756, 10, "개금", "green", 'u')
동의대 = circle(can, 605, 754, 10, "동의대", "green", 'd')
가야 = circle(can, 670, 754, 10, "가야", "green", 'u')
부암 = circle(can, 740, 754, 10, "부암", "green", 'd')
서면2 = circle(can, 805, 754, 10, "서면", "green", 'u')
전포 = circle(can, 890, 754, 10, "전포", "green", 'd')
국제금융센터부산은행 = circle(can, 960, 790, 10, "국제금융센터부산은행", "green", 'd')
문현 = circle(can, 964, 855, 10, "문현", "green", 'd')
지게골 = circle(can, 975, 913, 10, "지게골", "green", 'd')
못골 = circle(can, 1050, 935, 10, "못골", "green", 'd')
대연 = circle(can, 1118, 948, 10, "대연", "green", 'd')
경성대부경대 = circle(can, 1118, 900, 10, "경성대부경대", "green", 'r')
남천 = circle(can, 1118, 850, 10, "남천", "green", 'r')
금련산 = circle(can, 1118, 800, 10, "금련산", "green", 'r')
광안 = circle(can, 1118, 700, 10, "광안", "green", 'r')
수영2 = circle(can, 1118, 650, 10, "수영", "green", 'r')
민락 = circle(can, 1130, 598, 10, "민락", "green", 'l')
센텀시티 = circle(can, 1148, 558, 10, "센텀시티", "green", 'l')
동백 = circle(can, 1277, 570, 10, "동백", "green", 'l')
해운대 = circle(can, 1277, 660, 10, "해운대", "green", 'l')
중동 = circle(can, 1277, 730, 10, "중동", "green", 'l')
장산 = circle(can, 1277, 810, 10, "장산", "green", 'l')

#3호선

대저_체육공원 = line(can, 175, 404, 240, 404, "pink")
체육공원_강서구청 = line(can, 240, 404, 300, 404, "pink")
강서구청_구포 = line(can, 300, 404, 350, 404, "pink")
구포_덕천 = line(can, 350, 404, 400, 404, "pink")
덕천_숙등 = line(can, 400, 404, 460, 404, "pink")
숙등_남산정 = line(can, 460, 404, 510, 404, "pink")
남산정_만덕 = line(can, 510, 404, 565, 404, "pink")
만덕_미남 = line(can, 565, 404, 650, 404, "pink")
미남_사직 = line(can, 650, 404, 650, 460, "pink")
사직_종합운동장 = line(can, 650, 460, 650, 520, "pink")
종합운동장_거제 = line(can, 650, 520, 650, 580, "pink")
거제_연산 = line(can, 650, 580, 800, 580, "pink")
연산_물만골 = line(can, 800, 580, 880, 580, "pink")
물만골_배산 = line(can, 880, 580, 950, 580, "pink")
배산_망미 = line(can, 950, 580, 950, 650, "pink")
망미_수영 = line(can, 950, 650, 1118, 650, "pink")


체육공원 = circle(can, 240, 404, 10, "체육공원", "pink", 'u')
강서구청 = circle(can, 300, 404, 10, "강서구청", "pink", 'd')
구포 = circle(can, 350, 404, 10, "구포", "pink", 'u')
덕천3 = circle(can, 412, 404, 10, "덕천", "pink", 'd')
숙등 = circle(can, 460, 404, 10, "숙등", "pink", 'd')
남산정 = circle(can, 510, 404, 10, "남산정", "pink", 'd')
만덕 = circle(can, 565, 404, 10, "만덕", "pink", 'u')
미남3 = circle(can, 650, 404, 10, "미남", "pink", 'u')
사직 = circle(can, 650, 460, 10, "사직", "pink", 'l')
종합운동장 = circle(can, 650, 520, 10, "종합운동장", "pink", 'l')
거제3 = circle(can, 650, 580, 10, "거제", "pink", 'u')
연산3 = circle(can, 807, 580, 10, "연산", "pink", 'd')
물만골 = circle(can, 880, 580, 10, "물만골", "pink", 'u')
배산 = circle(can, 950, 580, 10, "배산", "pink", 'r')
망미 = circle(can, 950, 650, 10, "망미", "pink", 'l')
수영3 = circle(can, 1118, 650, 10, "", "pink", 'd')

#4호선

안평_고촌 = line(can, 1120, 105, 1120, 145, "#2cafff")
고촌_윗반송 = line(can, 1120, 145, 1120, 185, "#2cafff")
윗반송_영산대 = line(can, 1120, 185, 1120, 230, "#2cafff")
영산대_석대 = line(can, 1120, 230, 1120, 280, "#2cafff")
석대_반여농산물시장 = line(can, 1120, 280, 1120, 315, "#2cafff")
반여농산물시장_금사 = line(can, 1120, 315, 1120, 365, "#2cafff")
금사_서동 = line(can, 1120, 365, 1085, 397, "#2cafff")
서동_명장 = line(can, 1085, 397, 1030, 403, "#2cafff")
명장_충렬사 = line(can, 1030, 403, 970, 403, "#2cafff")
충렬사_낙민 = line(can, 970, 403, 920, 403, "#2cafff")
낙민_수안 = line(can, 920, 403, 870, 403, "#2cafff")
수안_동래 = line(can, 870, 403, 795, 403, "#2cafff")
동래_미남 = line(can, 795, 403, 650, 403, "#2cafff")

안평 = circle(can, 1120, 105, 10, "안평", "#2cafff", 'l')
고촌 = circle(can, 1120, 145, 10, "고촌", "#2cafff", 'l')
윗반송 = circle(can, 1120, 185, 10, "윗반송", "#2cafff", 'l')
영산대 = circle(can, 1120, 230, 10, "영산대", "#2cafff", 'l')
석대 = circle(can, 1120, 280, 10, "석대", "#2cafff", 'l')
반여농산물시장 = circle(can, 1120, 315, 10, "반여농산물시장", "#2cafff", 'l')
금사 = circle(can, 1120, 365, 10, "금사", "#2cafff", 'r')
서동 = circle(can, 1085, 397, 10, "서동", "#2cafff", 'd')
명장 = circle(can, 1030, 403, 10, "명장", "#2cafff", 'u')
충렬사 = circle(can, 970, 403, 10, "충렬사", "#2cafff", 'd')
낙민 = circle(can, 920, 403, 10, "낙민", "#2cafff", 'u')
수안 = circle(can, 870, 403, 10, "수안", "#2cafff", 'd')
동래4 = circle(can, 807, 403, 10, "동래", "#2cafff", 'd')
미남4 = circle(can, 650, 403, 10, "", "#2cafff", 'l')

#동해

태화강_개운포 = line(can, 1277, 105, 1277, 140, "blue")
개운포_덕하 = line(can, 1277, 140, 1277, 175, "blue")
덕하_망양 = line(can, 1277, 175, 1277, 210, "blue")
망양_남창 = line(can, 1277, 210, 1277, 245, "blue")
남창_서생 = line(can, 1277, 245, 1277, 280, "blue")
서생_월내 = line(can, 1277, 280, 1277, 315, "blue")
월내_좌천 = line(can, 1277, 315, 1277, 345, "blue")
좌천_일광 = line(can, 1277, 345, 1277, 383, "blue")
일광_기장 = line(can, 1277, 383, 1277, 415, "blue")
기장_오시리아 = line(can, 1277, 415, 1277, 450, "blue")
오시리아_송정 = line(can, 1277, 450, 1273, 489, "blue")
송정_신해운대 = line(can, 1273, 489, 1240, 515, "blue")
신해운대_벡스코 = line(can, 1240, 515, 1200, 518, "blue")
벡스코_센텀 = line(can, 1200, 518, 1147, 518, "blue")
센텀_재송 = line(can, 1147, 518, 1085, 518, "blue")
재송_부산원 = line(can, 1085, 518, 1030, 518, "blue")
부산원_안락 = line(can, 1030, 518, 972, 518, "blue")
안락_동래 = line(can, 972, 518, 920, 518, "blue")
동래_교대동 = line(can, 920, 518, 807, 520, "blue")
교대_거제 = line(can, 807, 520, 650, 580, "blue")
거제_거제해맞이 = line(can, 650, 580, 650, 650, "blue")
거제해맞이_부전 = line(can, 650, 650, 650, 700, "blue")

태화강 = circle(can, 1277, 105, 10, "태화강", "blue", 'l')
개운포 = circle(can, 1277, 140, 10, "개운포", "blue", 'l')
덕하 = circle(can, 1277, 175, 10, "덕하", "blue", 'l')
망양 = circle(can, 1277, 210, 10, "망양", "blue", 'l')
남창 = circle(can, 1277, 245, 10, "남창", "blue", 'l')
서생 = circle(can, 1277, 280, 10, "서생", "blue", 'l')
월내 = circle(can, 1277, 315, 10, "월내", "blue", 'l')
좌천동 = circle(can, 1277, 345, 10, "좌천", "blue", 'l')
일광 = circle(can, 1277, 383, 10, "일광", "blue", 'l')
기장 = circle(can, 1277, 415, 10, "기장", "blue", 'l')
오시리아 = circle(can, 1277, 450, 10, "오시리아", "blue", 'l')
송정 = circle(can, 1273, 489, 10, "송정", "blue", 'r')
신해운대 = circle(can, 1240, 515, 10, "신해운대", "blue", 'r')
벡스코동 = circle(can, 1200, 518, 10, "벡스코", "blue", 'u')
센텀 = circle(can, 1147, 518, 10, "센텀", "blue", 'u')
재송 = circle(can, 1085, 518, 10, "재송", "blue", 'u')
부산원동 = circle(can, 1030, 518, 10, "부산원", "blue", 'd')
안락 = circle(can, 972, 518, 10, "안락", "blue", 'u')
동래동 = circle(can, 920, 518, 10, "동래", "blue", 'd')
거제동 = circle(can, 650, 580, 10, "", "blue", 'l')
거제해맞이 = circle(can, 650, 650, 10, "거제해맞이", "blue", 'l')
부전동 = circle(can, 650, 700, 10, "부전", "blue", 'l')


#환승역 이미지

inter대저 = can.create_image(175, 404, image=image, anchor="center")
inter덕천 = can.create_image(413, 404, image=image, anchor="center")
inter동래 = can.create_image(807, 403, image=image, anchor="center")
inter사상 = can.create_image(413, 637, image=image, anchor="center")
inter서면 = can.create_image(805, 754, image=image, anchor="center")
inter연산 = can.create_image(807, 580, image=image, anchor="center")
inter교대 = can.create_image(807, 520, image=image, anchor="center")
inter수영 = can.create_image(1118, 650, image=image, anchor="center")
inter벡스코 = can.create_image(1200, 518, image=image, anchor="center")
inter거제 = can.create_image(650, 580, image=image, anchor="center")
inter미남 = can.create_image(650, 403, image=image, anchor="center")
#---------------------------------노선도---------------------------------------------------

# 음성 엔진 초기화
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 말하는 속도 설정

# 환승 시 추가 시간
TRANSFER_TIME = 3 * 60


subway_map = {
    '다대포해수욕장': {'다대포항': ('1호선', 2, 15)},
    '다대포항': {'다대포해수욕장': ('1호선', 2, 15), '낫개': ('1호선', 1, 45)},
    '낫개': {'다대포항': ('1호선', 1, 45), '신장림': ('1호선', 1, 55)},
    '신장림': {'낫개': ('1호선', 1, 55), '장림': ('1호선', 1, 15)},
    '장림': {'신장림': ('1호선', 1, 15), '동매': ('1호선', 2, 5)},
    '동매': {'장림': ('1호선', 2, 5), '신평': ('1호선', 2, 45)},
    '신평': {'동매': ('1호선', 2, 45), '하단': ('1호선', 2, 25)},
    '하단': {'신평': ('1호선', 2, 25), '당리': ('1호선', 1, 15)},
    '당리': {'하단': ('1호선', 1, 15), '사하': ('1호선', 1, 30)},
    '사하': {'당리': ('1호선', 1, 30), '괴정': ('1호선', 1, 20)},
    '괴정': {'사하': ('1호선', 1, 20), '대티': ('1호선', 1, 10)},
    '대티': {'괴정': ('1호선', 1, 10), '서대신': ('1호선', 1, 50)},
    '서대신': {'대티': ('1호선', 1, 50), '동대신': ('1호선', 2, 5)},
    '동대신': {'서대신': ('1호선', 2, 5), '토성': ('1호선', 2, 0)},
    '토성': {'동대신': ('1호선', 2, 0), '자갈치': ('1호선', 1, 50)},
    '자갈치': {'토성': ('1호선', 1, 50), '남포': ('1호선', 1, 10)},
    '남포': {'자갈치': ('1호선', 1, 10), '중앙': ('1호선', 1, 25)},
    '중앙': {'남포': ('1호선', 1, 25), '부산역': ('1호선', 1, 25)},
    '부산역': {'중앙': ('1호선', 1, 25), '초량': ('1호선', 1, 10)},
    '초량': {'부산역': ('1호선', 1, 10), '부산진': ('1호선', 1, 10)},
    '부산진': {'초량': ('1호선', 1, 10), '좌천(1호선)': ('1호선', 1, 15)},
    '좌천(1호선)': {'부산진': ('1호선', 1, 15), '범일': ('1호선', 1, 25)},
    '범일': {'좌천(1호선)': ('1호선', 1, 25), '범내골': ('1호선', 1, 5)},
    '범내골': {'범일': ('1호선', 1, 5), '서면': ('1호선', 1, 35)},
    '서면': {'범내골': ('1호선', 1, 35), '부전': ('1호선', 1, 5), '전포': ('2호선', 1, 55), '부암': ('2호선', 1, 25)},
    '부전': {'서면': ('1호선', 1, 5), '양정': ('1호선', 1, 40)},
    '양정': {'부전': ('1호선', 1, 40), '시청': ('1호선', 1, 10)},
    '시청': {'양정': ('1호선', 1, 10), '연산': ('1호선', 1, 20)},
    '연산': {'시청': ('1호선', 1, 20), '교대': ('1호선', 1, 30), '물만골': ('3호선', 1, 55), '거제': ('3호선', 1, 15)},
    '교대': {'연산': ('1호선', 1, 30), '동래': ('1호선', 1, 30), '동래(동해선)': ('동해선', 2, 0), '거제': ('동해선', 1, 0)},
    '동래': {'교대': ('1호선', 1, 30), '명륜': ('1호선', 1, 10), '수안': ('4호선', 1, 10), '미남': ('4호선', 1, 30)},
    '명륜': {'동래': ('1호선', 1, 10), '온천장': ('1호선', 1, 25)},
    '온천장': {'명륜': ('1호선', 1, 25), '부산대': ('1호선', 1, 30)},
    '부산대': {'온천장': ('1호선', 1, 30), '장전': ('1호선', 1, 20)},
    '장전': {'부산대': ('1호선', 1, 20), '구서': ('1호선', 1, 30)},
    '구서': {'장전': ('1호선', 1, 30), '두실': ('1호선', 1, 30)},
    '두실': {'구서': ('1호선', 1, 30), '남산': ('1호선', 1, 20)},
    '남산': {'두실': ('1호선', 1, 20), '범어사': ('1호선', 1, 25)},
    '범어사': {'남산': ('1호선', 1, 25), '노포': ('1호선', 2, 10)},
    '노포': {'범어사': ('1호선', 2, 10)},
    
    #2호선
    '장산': {'중동': ('2호선', 1, 30)},
    '중동': {'장산': ('2호선', 1, 30), '해운대': ('2호선', 1, 20)},
    '해운대': {'중동': ('2호선', 1, 20), '동백': ('2호선', 1, 40)},
    '동백': {'해운대': ('2호선', 1, 40), '벡스코': ('2호선', 1, 35)},
    '벡스코': {'동백': ('2호선', 1, 35), '센텀시티': ('2호선', 1, 20), '신해운대': ('동해선', 4, 0), '센텀': ('동해선', 2, 0)},
    '센텀시티': {'벡스코': ('2호선', 1, 20), '민락': ('2호선', 1, 40)},
    '민락': {'센텀시티': ('2호선', 1, 40), '수영': ('2호선', 2, 15)},
    '수영': {'민락': ('2호선', 2, 15), '광안': ('2호선', 1, 15), '망미': ('3호선', 2, 0)},
    '광안': {'수영': ('2호선', 1, 15), '금련산': ('2호선', 1, 15)},
    '금련산': {'광안': ('2호선', 1, 15), '남천': ('2호선', 1, 30)},
    '남천': {'금련산': ('2호선', 1, 30), '경성대부경대': ('2호선', 1, 15)},
    '경성대부경대': {'남천': ('2호선', 1, 15), '대연': ('2호선', 1, 15)},
    '대연': {'경성대부경대': ('2호선', 1, 15), '못골': ('2호선', 1, 10)},
    '못골': {'대연': ('2호선', 1, 10), '지게골': ('2호선', 1, 25)},
    '지게골': {'못골': ('2호선', 1, 25), '문현': ('2호선', 1, 30)},
    '문현': {'지게골': ('2호선', 1, 30), '국제금융센터부산은행': ('2호선', 1, 20)},
    '국제금융센터부산은행': {'문현': ('2호선', 1, 20), '전포': ('2호선', 1, 20)},
    '전포': {'국제금융센터부산은행': ('2호선', 1, 20), '서면': ('2호선', 1, 55)},
    '서면': {'전포': ('2호선', 1, 55), '부암': ('2호선', 1, 25), '범내골': ('1호선', 1, 35), '부전': ('1호선', 1, 5)},
    '부암': {'서면': ('2호선', 1, 25), '가야': ('2호선', 1, 15)},
    '가야': {'부암': ('2호선', 1, 15), '동의대': ('2호선', 1, 20)},
    '동의대': {'가야': ('2호선', 1, 20), '개금': ('2호선', 1, 35)},
    '개금': {'동의대': ('2호선', 1, 35), '냉정': ('2호선', 1, 25)},
    '냉정': {'개금': ('2호선', 1, 25), '주례': ('2호선', 1, 20)},
    '주례': {'냉정': ('2호선', 1, 20), '감전': ('2호선', 1, 45)},
    '감전': {'주례': ('2호선', 1, 45), '사상': ('2호선', 1, 45)},
    '사상': {'감전': ('2호선', 1, 45), '덕포': ('2호선', 1, 50), '괘법르네시떼': ('부산김해선', 1, 25)},
    '덕포': {'사상': ('2호선', 1, 50), '모덕': ('2호선', 1, 15)},
    '모덕': {'덕포': ('2호선', 1, 15), '모라': ('2호선', 1, 30)},
    '모라': {'모덕': ('2호선', 1, 30), '구남': ('2호선', 1, 35)},
    '구남': {'모라': ('2호선', 1, 35), '구명': ('2호선', 1, 15)},
    '구명': {'구남': ('2호선', 1, 15), '덕천': ('2호선', 2, 5)},
    '덕천': {'구명': ('2호선', 2, 5), '수정': ('2호선', 2, 5), '숙등': ('3호선', 1, 10), '구포': ('3호선', 1, 45)},
    '수정': {'덕천': ('2호선', 2, 5), '화명': ('2호선', 2, 10)},
    '화명': {'수정': ('2호선', 2, 10), '율리': ('2호선', 1, 35)},
    '율리': {'화명': ('2호선', 1, 35), '동원': ('2호선', 1, 15)},
    '동원': {'율리': ('2호선', 1, 25), '금곡': ('2호선', 1, 45)},
    '금곡': {'동원': ('2호선', 1, 45), '호포': ('2호선', 2, 25)},
    '호포': {'금곡': ('2호선', 2, 25), '증산': ('2호선', 4, 10)},
    '증산': {'호포': ('2호선', 4, 10), '부산대양산캠퍼스': ('2호선', 1, 35)},
    '부산대양산캠퍼스': {'증산': ('2호선', 1, 35), '남양산': ('2호선', 1, 40)},
    '남양산': {'부산대양산캠퍼스': ('2호선', 1, 40), '양산': ('2호선', 2, 15)},
    '양산': {'남양산': ('2호선', 2, 15)},
    
    #3호선
    '수영': {'망미': ('3호선', 2, 0), '민락': ('2호선', 2, 15), '광안': ('2호선', 1, 15)},
    '망미': {'수영': ('3호선', 2, 0), '배산': ('3호선', 1, 35)},
    '배산': {'망미': ('3호선', 1, 35), '물만골': ('3호선', 1, 55)},
    '물만골': {'배산': ('3호선', 1, 55), '연산': ('3호선', 1, 35)},
    '연산': {'물만골': ('3호선', 1, 55), '거제': ('3호선', 1, 15), '시청': ('1호선', 1, 20), '교대': ('1호선', 1, 30)},
    '거제': {'연산': ('3호선', 1, 15), '종합운동장': ('3호선', 1, 15), '교대': ('동해선', 1, 0), '거제해맞이': ('동해선', 1, 30)},
    '종합운동장': {'거제': ('3호선', 1, 15), '사직': ('3호선', 1, 25)},
    '사직': {'종합운동장': ('3호선', 1, 25), '미남': ('3호선', 1, 35)},
    '미남': {'사직': ('3호선', 1, 35), '만덕': ('3호선', 4, 0), '동래': ('4호선', 1, 45)},
    '만덕': {'미남': ('3호선', 4, 0), '남산정': ('3호선', 1, 40)},
    '남산정': {'만덕': ('3호선', 1, 40), '숙등': ('3호선', 1, 25)},
    '숙등': {'남산정': ('3호선', 1, 25), '덕천': ('3호선', 1, 10)},
    '덕천': {'숙등': ('3호선', 1, 10), '구포': ('3호선', 1, 45), '구명': ('2호선', 2, 5), '수정': ('2호선', 2, 5)},
    '구포': {'덕천': ('3호선', 1, 45), '강서구청': ('3호선', 2, 25)},
    '강서구청': {'구포': ('3호선', 2, 25), '체육공원': ('3호선', 1, 35)},
    '체육공원': {'강서구청': ('3호선', 1, 35), '대저': ('3호선', 1, 25)},
    '대저': {'체육공원': ('3호선', 1, 25), '등구': ('부산김해선', 2, 49), '평강': ('부산김해선', 1, 45)},
    
    #4호선
    '미남': {'동래': ('4호선', 1, 45), '만덕': ('3호선', 4, 0), '사직': ('3호선', 1, 35)},
    '동래': {'미남': ('4호선', 1, 45), '수안': ('4호선', 1, 10), '교대': ('1호선', 1, 30), '명륜': ('1호선', 1, 10)},
    '수안': {'동래': ('4호선', 1, 10), '낙민': ('4호선', 1, 10)},
    '낙민': {'수안': ('4호선', 1, 10), '충렬사': ('4호선', 1, 20)},
    '충렬사': {'낙민': ('4호선', 1, 20), '명장': ('4호선', 1, 15)},
    '명장': {'충렬사': ('4호선', 1, 15), '서동': ('4호선', 1, 55)},
    '서동': {'명장': ('4호선', 1, 55), '금사': ('4호선', 1, 20)},
    '금사': {'서동': ('4호선', 1, 20), '반여농산물시장': ('4호선', 1, 20)},
    '반여농산물시장': {'금사': ('4호선', 1, 20), '석대': ('4호선', 1, 45)},
    '석대': {'반여농산물시장': ('4호선', 1, 45), '영산대': ('4호선', 2, 5)},
    '영산대': {'석대': ('4호선', 2, 5), '윗반송': ('4호선', 1, 45)},
    '윗반송': {'영산대': ('4호선', 1, 45), '고촌': ('4호선', 1, 25)},
    '고촌': {'윗반송': ('4호선', 1, 25), '안평': ('4호선', 1, 45)},
    '안평': {'고촌': ('4호선', 1, 45)},
    
    #동해선
    '태화강': {'개운포': ('동해선', 4, 30)},
    '개운포': {'태화강': ('동해선', 4, 30), '덕하': ('동해선', 2, 30)},
    '덕하': {'개운포': ('동해선', 2, 30), '망양': ('동해선', 4, 0)},
    '망양': {'덕하': ('동해선', 4, 0), '남창': ('동해선', 4, 0)},
    '남창': {'망양': ('동해선', 4, 0), '서생': ('동해선', 7, 0)},
    '서생': {'남창': ('동해선', 7, 0), '월내': ('동해선', 3, 0)},
    '월내': {'서생': ('동해선', 3, 0), '좌천(동해선)': ('동해선', 3, 30)},
    '좌천(동해선)': {'월내': ('동해선', 3, 30), '일광': ('동해선', 4, 30)},
    '일광': {'좌천(동해선)': ('동해선', 4, 30), '기장': ('동해선', 3, 0)},
    '기장': {'일광': ('동해선', 3, 0), '오시리': ('동해선', 5, 0)},
    '오시리': {'기장': ('동해선', 5, 0), '송정': ('동해선', 1, 30)},
    '송정': {'오시리': ('동해선', 1, 30), '신해운대': ('동해선', 3, 0)},
    '신해운대': {'송정': ('동해선', 3, 0), '벡스코': ('동해선', 4, 0)},
    '벡스코': {'신해운대': ('동해선', 4, 0), '센텀': ('동해선', 2, 0),'동백': ('2호선', 1, 35), '센텀시티': ('2호선', 1, 20)},
    '센텀': {'벡스코': ('동해선', 2, 0), '재송': ('동해선', 1, 30)},
    '재송': {'센텀': ('동해선', 1, 30), '부산원': ('동해선', 1, 30)},
    '부산원': {'재송': ('동해선', 1, 30), '안락': ('동해선', 2, 0)},
    '안락': {'부산원': ('동해선', 2, 0), '동래(동해선)': ('동해선', 1, 30)},
    '동래(동해선)': {'안락': ('동해선', 1, 30), '교대': ('동해선', 2, 0)},
    '교대': {'동래(동해선)': ('동해선', 2, 0), '거제': ('동해선', 1, 0),'연산': ('1호선', 1, 30), '동래': ('1호선', 1, 30)},
    '거제': {'교대': ('동해선', 1, 0), '거제해맞이': ('동해선', 1, 30),'연산': ('3호선', 1, 15), '종합운동장': ('3호선', 1, 15)},
    '거제해맞이': {'거제': ('동해선', 1, 30), '부전(동해선)': ('동해선', 3, 0)},
    '부전(동해선)': {'거제해맞이': ('동해선', 3, 0)},

    #부산김해선
    '사상': {'괘법르네시떼': ('부산김해선', 1, 25),'감전': ('2호선', 1, 45),'덕포': ('2호선', 1, 50)},
    '괘법르네시떼': {'사상': ('부산김해선', 1, 25),'서부산유통지구': ('부산김해선', 3, 0)},
    '서부산유통지구': {'괘법르네시떼': ('부산김해선', 3, 0),'공항': ('부산김해선', 1, 55)},
    '공항': {'서부산유통지구': ('부산김해선', 1, 55),'덕두': ('부산김해선', 2, 22)},
    '덕두': {'공항': ('부산김해선', 2, 22),'등구': ('부산김해선', 2, 36)},
    '등구': {'덕두': ('부산김해선', 2, 36),'대저': ('부산김해선', 2, 49)},
    '대저': {'등구': ('부산김해선', 2, 49),'평강': ('부산김해선', 1, 45),'체육공원': ('3호선', 1, 25)},
    '평강': {'대저': ('부산김해선', 1, 45),'대사': ('부산김해선', 1, 45)},
    '대사': {'평강': ('부산김해선', 1, 45),'불암': ('부산김해선', 1, 42)},
    '불암': {'대사': ('부산김해선', 1, 42),'지내': ('부산김해선', 1, 23)},
    '지내': {'불암': ('부산김해선', 1, 23),'김해대학': ('부산김해선', 1, 38)},
    '김해대학': {'지내': ('부산김해선', 1, 38),'인제대': ('부산김해선', 1, 58)},
    '인제대': {'김해대학': ('부산김해선', 1, 58),'김해시청': ('부산김해선', 1, 51)},
    '김해시청': {'인제대': ('부산김해선', 1, 51),'부원': ('부산김해선', 1, 26)},
    '부원': {'김해시청': ('부산김해선', 1, 26),'봉황': ('부산김해선', 2, 2)},
    '봉황': {'부원': ('부산김해선', 2, 2),'수로왕릉': ('부산김해선', 1, 24)},
    '수로왕릉': {'봉황': ('부산김해선', 1, 24),'박물관': ('부산김해선', 1, 38)},
    '박물관': {'수로왕릉': ('부산김해선', 1, 38),'연지공원': ('부산김해선', 1, 59)},
    '연지공원': {'박물관': ('부산김해선', 1, 59),'장신대': ('부산김해선', 3, 12)},
    '장신대': {'연지공원': ('부산김해선', 3, 12),'가야대': ('부산김해선', 2, 37)},
    '가야대': {'장신대': ('부산김해선', 2, 37)}
}

# 기존 subway_map에 병합
for station, links in renamed_connections.items():
    if station not in subway_map:
        subway_map[station] = links
    else:
        subway_map[station].update(links)


# 경로 탐색 함수 (소요 시간 + 환승)
def find_shortest_path_with_transfers(start, end):
    queue = []
    heapq.heappush(queue, (0, start, [start], None, 0))
    distances = {station: float("inf") for station in subway_map}
    transfers = {station: float("inf") for station in subway_map}
    distances[start] = 0
    transfers[start] = 0

    while queue:
        current_time, current_station, path, prev_line, transfer_count = heapq.heappop(queue)

        if current_station == end:
            minutes = current_time // 60
            return f"{minutes}분", transfer_count, path

        for neighbor, (line, min_, sec_) in subway_map[current_station].items():
            transfer_time = TRANSFER_TIME if prev_line and line != prev_line else 0
            new_transfer_count = transfer_count + 1 if prev_line and line != prev_line else transfer_count
            additional_time = (min_ * 60 + sec_) + transfer_time
            new_time = current_time + additional_time

            if new_time < distances[neighbor] or new_transfer_count < transfers[neighbor]:
                distances[neighbor] = new_time
                transfers[neighbor] = new_transfer_count
                heapq.heappush(queue, (new_time, neighbor, path + [neighbor], line, new_transfer_count))

    return None, None, []

# UI 시작
root = ttkb.Window(themename="morph")
root.title("부산 지하철 길찾기")
root.geometry("450x1067+0-0")

# 메인 프레임
main_frame = ttkb.Frame(root, bootstyle="light", padding=20)
main_frame.pack(pady=30, padx=30, fill="both", expand=False)


# 자동완성 목록 업데이트
def update_autocomplete(event, entry, listbox, top):
    value = entry.get()  # 입력값 가져오기
    listbox.delete(0, ttkb.END)  # 기존 목록 삭제

    if value == '':  # 입력값이 비었을 때 목록 숨기기
        top.withdraw()
        return

    # 필터링된 목록 생성
    filtered = [item for item in subway_map.keys() if item.startswith(value)]

    if filtered:  # 필터링 결과가 있을 때만 표시
        for item in filtered:
            listbox.insert(ttkb.END, item)

        # 입력란의 위치와 창의 높이를 고려하여 목록 표시 방향 결정
        x = entry.winfo_rootx()
        y = entry.winfo_rooty() + entry.winfo_height()

        # 아래 공간 부족 시 위로 표시
        if y + listbox.winfo_reqheight() > root.winfo_height() + root.winfo_y():
            y = entry.winfo_rooty() - listbox.winfo_reqheight()

        top.geometry(f"{entry.winfo_width()}x{listbox.winfo_reqheight()}+{x}+{y}")
        top.deiconify()
    else:
        top.withdraw()  # 목록 숨기기

# 리스트박스 선택 시 입력란에 반영
def on_select(event, entry, listbox, top):
    selected = listbox.get(listbox.curselection())
    entry.delete(0, ttkb.END)
    entry.insert(0, selected)
    top.withdraw()  # 선택 후 자동완성 목록 숨기기

# 입력란 이외를 클릭했을 때 자동완성 숨기기
def hide_listbox(event, top):
    top.withdraw()

# 출발역 입력란
ttkb.Label(main_frame, text="출발역", font=("Helvetica", 13, "bold"), bootstyle="dark").pack(pady=(10, 0), anchor="w")
start_entry = ttkb.Combobox(main_frame, values=list(subway_map.keys()), font=("Helvetica", 12), bootstyle="info")
start_entry.pack(fill="x", pady=(0, 10), ipady=6)

# 출발역 자동완성 목록을 최상위 창으로 생성
start_top = ttkb.Toplevel(root)
start_top.withdraw()
start_top.overrideredirect(True)  # 테두리 없는 창으로 설정
start_listbox = tk.Listbox(start_top, font=("Arial", 12), height=5)
start_listbox.pack()

# 도착역 입력란
ttkb.Label(main_frame, text="도착역", font=("Helvetica", 13, "bold"), bootstyle="dark").pack(pady=(10, 0), anchor="w")
end_entry = ttkb.Combobox(main_frame, values=list(subway_map.keys()), font=("Helvetica", 12), bootstyle="info")
end_entry.pack(fill="x", pady=(0, 10), ipady=6)

# 도착역 자동완성 목록을 최상위 창으로 생성
end_top = ttkb.Toplevel(root)
end_top.withdraw()
end_top.overrideredirect(True)  # 테두리 없는 창으로 설정
end_listbox = tk.Listbox(end_top, font=("Arial", 12), height=5)
end_listbox.pack()

# 출발역 이벤트 바인딩
start_entry.bind('<KeyRelease>', lambda event: update_autocomplete(event, start_entry, start_listbox, start_top))
start_listbox.bind('<ButtonRelease-1>', lambda event: on_select(event, start_entry, start_listbox, start_top))

# 도착역 이벤트 바인딩
end_entry.bind('<KeyRelease>', lambda event: update_autocomplete(event, end_entry, end_listbox, end_top))
end_listbox.bind('<ButtonRelease-1>', lambda event: on_select(event, end_entry, end_listbox, end_top))

# 포커스 잃을 때 자동완성 숨기기
root.bind('<Button-1>', lambda event: hide_listbox(event, start_top))
root.bind('<Button-1>', lambda event: hide_listbox(event, end_top))


# 길찾기 버튼
ttkb.Button(main_frame, text="길찾기", command=lambda: search_route(), bootstyle="primary-outline").pack(pady=15, fill="x")

# 결과 요약
time_label = ttkb.Label(main_frame, text="", font=("Helvetica", 12), bootstyle="dark")
time_label.pack(pady=10, anchor="w")

# 결과 출력용 스크롤 캔버스
canvas = ttkb.Canvas(main_frame, highlightthickness=0)
scroll_y = ttkb.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
result_container = ttkb.Frame(canvas, bootstyle="light")

result_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=result_container, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(fill="both", expand=True, side="left")
scroll_y.pack(fill="y", side="right")

# 경로 검색
def search_route():
    for widget in result_container.winfo_children():
        widget.destroy()

    start = start_entry.get().strip()
    end = end_entry.get().strip()

    if start not in subway_map or end not in subway_map:
        Messagebox.show_error("오류", "유효한 출복지와 도착지를 입력하세요!")
        return

    if start == end:
        Messagebox.show_info("결과", "출복지와 도착지가 같습니다! 😆")
        return

    travel_time, transfer_count, route = find_shortest_path_with_transfers(start, end)

    if not route:
        time_label.config(text="경로를 찾을 수 없습니다.")
        return

    time_label.config(text=f"총 소요시간: {travel_time}분\n환승 횟수: {transfer_count}회")

    pass  
    engine.runAndWait()


    prev_line = None
    segment_count = 0
    segment_time = 0
    segment_start_station = None

    actual_time = 0  # 중복 방지 실제 소요 시간 누적

    for i in range(len(route) - 1):
        station = route[i]
        next_station = route[i + 1]
        line, min_, sec_ = subway_map[station][next_station]
        curr_line = line
        time_to_next = min_ + (1 if sec_ > 0 else 0)

        if i == 0:
            # 시작역 초기화
            prev_line = curr_line
            segment_count = 1
            segment_time = time_to_next
            actual_time += time_to_next
            segment_start_station = station
        elif curr_line != prev_line:
            # 환승 발생 전 세그먼트 출력
            display_segment(prev_line, segment_start_station, segment_count + 1, segment_time, start=True)
            display_segment(prev_line, station, transfer=True)

            prev_line = curr_line
            segment_count = 1
            segment_time = time_to_next
            actual_time += time_to_next
            segment_start_station = station
        else:
            segment_count += 1
            segment_time += time_to_next
            actual_time += time_to_next

    # 마지막 구간 출력
    last_station = route[-1]
    display_segment(prev_line, segment_start_station, segment_count + 1, segment_time, start=True)
    display_segment(prev_line, last_station, end=True)

    # 실제 누적 시간 기준으로 상단 라벨 업데이트
    voice_text = f"{start}에서 출발해서, 총 {transfer_count}번 환승 후 {end}에 도착합니다. 총 소요 시간은 {actual_time}분입니다."
    engine.say(voice_text)
    engine.runAndWait()
    time_label.config(text=f"총 소요시간: {actual_time}분\n환승 횟수: {transfer_count}회")

# 세그먼트 UI 출력

def display_segment(line, station, count=0, time=0, start=False, end=False, transfer=False):
    frame = ttkb.Frame(result_container, padding=4)
    frame.pack(anchor="center", pady=2)

    line_colors = {
        "1호선": "#FF7F00",
        "2호선": "#3ED93B",
        "3호선": "#E8AB56",
        "4호선": "#64C4FF",
        "동해선": "#1239C6",
        "부산김해선": "#8200FF"
    }
    color = line_colors.get(line, "#7f8c8d")

    icon = ttkb.Canvas(frame, width=30, height=30, highlightthickness=0)
    icon.create_oval(2, 2, 28, 28, fill=color, outline="")
    icon.create_text(15, 15, text=(line[0] if start else "하차"), fill="white", font=("Helvetica", 10, "bold" if start else "normal"))
    icon.pack(side="left", padx=(0, 6))

    if start:
        text = f"{station}\n{count}개역 ({time}분)"
    elif transfer:
        text = f"{station} (환승)"
    else:
        text = station

    label = ttkb.Label(frame, text=text, font=("Helvetica", 12))
    label.pack(side="left")

            

    # ttkb.Label(frame, text=text, font=("Helvetica", 12), anchor="w", justify="left").pack(side="left", padx=(5, 0))
    
    
# Tkinter 메인 루프 시작
win.mainloop()    
root.mainloop()