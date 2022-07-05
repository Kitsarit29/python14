#การแสดงค่าในlist
fruits = ["apple","banana","cherry","watermelon","blueberry"]
print(fruits[1])
#เปลี่ยนคำในlist
fruits[1] ="blackcurrant"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:3] = ["kiwi","mango","pineapple"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#กิตติ์สฤษฏิ์ แสนคำ 29 ม.6/14