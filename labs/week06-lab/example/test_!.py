"""
เขียน funtion ชื่อ covert_currency(value, currency)
ที่ทำหน้าในการแปลงสกุล
THB <-> USD กำหนดให้USD = 33 THB

ทั้งนี้ให้funtion ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการเปลี่ยนแปลง และสกุลเงินปลายทาง

ตัวอย่างการเรียกใช้
convert_currency(100,"USD")
convert_currency(100,"THB")

ตัวอย่าง หน้าจอ
100 THB = 3.33 USD
100 USD = 3300.0 THB
"""

def convert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

convert_currency(100,"USD")
convert_currency(100,"THB")
