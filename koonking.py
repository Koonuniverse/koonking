print("1.รับค่า * เข้ามาหนึ่งครั้ง จากนั้นรับตัวเลขจํานวนเต็ม แล้วให้แสดงผลลัพธ์ดังนี้Input = * และ 10 output **********")

char = input()
num = int(input())
print("")
print(char * num)

print("")

print("2.เขียนโปรแกรมรับจํานวนคะแนนสอบกลางภาค และปลายภาค ซึ่งแต่ละครั้งมีคะแนนและค่าเฉลี่ยของคะแนนนสอบทั้งสองครั้งบรรทัดแรก รับจํานวนจริง midterm แทนคะแนนสอบกลางภาค โดย0<= midterm <=60บรรทัดที่ สอง รับจํานวนจริง Final แทนคะแนนสอบปลายภาค โดย0<= final <=60OUTPUTบรรทัดแรกแสดงข้อความ “Total:” ตามด้วยผลรวมของคะแนนนสอบทั้งสองครั้งบรรทัดที่สองแสดงข้อความ “Average:” ตามด้วยค่าเฉลี่ยของคะแนนนสอบทั้งสองครั้ง**กําหนดค่า Input = 50.5 และ 31.5")
midterm = float(input())
final = float(input())
total = midterm + final
average = total / 2
print("")
print(f"รวม: {total}")
print(f"เฉลี่ย: {average}")

print("")

print("3.กําหนดให้สระว่ายน้ํา เป็นรูปสี่เหลี่ยมผืนผ้า โดยเราต้องการเติมน้ําลงไปในสระให้เต็ม จงเขียนโปรแกรมเพื่อรับความกว้าง ความยาว และความลึกของสระในหน่วยเมตร เพื่อคํานวณว่าต้องใช้เวลากี่นาทีในการเติมน้ําลงในสระให้เต็ม เมื่อกําหนดให้ใช้เวลา 15 วินาทีในการเติมน้ํา 1ลูกบาศก์เมตร แสดงคําตอบด้วยทศนิยมสองตําแหน่ง***กําหนด Input กว้าง:18.5ยาว : 38.75ลึก : 1.35ต้องใช้เวลาในการเติมน้ํา 241.95 นาที.")

width = float(input())
length = float(input())
depth = float(input())

volume = width * length * depth
time_seconds = volume * 15
time_minutes = time_seconds / 60
print("")
print(f"{time_minutes:.2f} นาที")
