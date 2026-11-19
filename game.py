"""بازی فکر بکر 
درس برنامه سازی پیشرفته
حسین نوری اصل 404131303"""

import random

"""یک تابع تعریف میکنیم تا مشخصات بازی و خودمان را نمایش دهیم"""
def info ():
    print("bazi fekre bekr")
    print("dars barname sazi pishrafte")
    print("hossein noori asl 404131303")
    print("shoma 10 forsat baraye hads zadan darid")
    print("ramz makhfi yek adad 4 raghami ba ragham haye motefavet bein adaad 1 ta 6 ast")

"""یک تابع تعریف میکنیم تا یک رمز 4 رقمی بدون رقم تکراری ایجاد کند و در یک لیست ذخیره کند"""
toole_ramz = 4
def generate ():
    ramz = []
    while len(ramz) < toole_ramz:
        ragham = random.randrange(1,7)
        if ragham not in ramz:
            ramz = ramz + [ragham]
    return ramz

"""یک تابع تعریف میکنیم تا بررسی کند ایا رمز وارد شده معتبر است یا نه"""
valid_num = ['1' , '2' , '3' , '4' , '5' , '6']
def valid_guess (text):
    if len(text) != toole_ramz:
        return False
    for ch in text:
        if ch not in valid_num:
            return False
    for i in range(toole_ramz):
        for j in range(i+1 , toole_ramz):
            if text[i] == text [j]:
                return False
    return True

"""یک تابع تعریف میکنیم تا یک رمز از کاربر بگیرد و با تابع قبل ان را چک کند اگر معتبر بود ان را به صورت عدد در یک لیست ذخیره کند
در غیر این صورت بگوید که ورودی نا معتبر است"""
def get_guess ():
    while True:
        text = input ("4 adad motafavet az adaad 1 ta 6 vared konid:")
        if valid_guess (text):
            guess = []
            for ch in text:
                guess = guess + [int(ch)]
            return guess
        print("voroodi na motabar")

"""یک تابع تعریف میکنیم تا تعداد ارقام درست در مکان درست و تعداد ارقام درست در مکان نادرست را پیدا کند و به کاربر بگوید"""
def compare(ramz , guess):
    right_place = 0
    wrong_place = 0
    for index , ragham in enumerate(guess):
        if ragham == ramz[index]:
            right_place += 1
        elif ragham in ramz:
            wrong_place += 1
    return right_place , wrong_place

"""یک تابع درست میکنیم که یک رمز با استفاده از تابع جنریت تولید کند
و از کاربر با استفاده از تابع گس حدس های او را بگیرد این کار را تا 10 حدس انجام دهد
ارقام درست در مکان درست و اشتباه را به کاربر بگوید و اگر
تمام ارقام در مکان درست بودند کاربر برنده میشود و در غیر این صورت
کاربر میبازد"""
def game ():
    ramz = generate()
    max_tries = 10
    tries = 0
    while tries < max_tries:
        guess = get_guess()
        tries += 1

        right_place , wrong_place = compare(ramz , guess)
        print(f'tedad argham dorost dar makan dorost: {right_place}')
        print(f'tedad argham dorost dar makan eshtebah: {wrong_place}')

        if right_place == toole_ramz:
            print(f'win. your tries: {tries}')
            return
    print("lose")
    print("ramz:" , ramz)

"""یک تابع تعریف میکنیم تا اظلاعات را نمایش دهد و برای بازی مجدد کاربر نیاز باشد یک حرف خاص وارد کند"""
def main ():
    info()
    again = 'y'
    while again == 'y':
        game()
        again = input("bazi mojadad: y")

main()
