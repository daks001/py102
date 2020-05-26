# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 		DAKSHIKA SRIVASTAVA
# 	 		    MAHIRAH SAMAH
#               MICHAEL MARTIN
# Section:		532
# Assignment:	Lab6_Activity1
# Date:		    1 OCTOBER 19

#taking inputs for the gender, age, cholesterol level, if they smoke, hdl, systolic bp and if it's treated
gender = input("Enter 'm' for male and 'f' for female: ")
age = int(input("Enter your age: "))
total_chol = int(input("Enter your total cholesterol level: "))
smoker = input("Enter 1 if you smoke and 0 if you don't: ")
hdl = int(input("Enter your HDL value in mg/dL: "))
sys_bp = int(input("Enter your systolic BP in mm Hg: "))
sys_treat = input("Enter 1 if your BP is treated and 0 if untreated: ")

#points maintains total points of the user
#flag keeps track of invalid input
points = 0
flag = 0

if gender=='m':
    #person is male
    if age>=20 and age<=34:
        points -= 9
    elif age>=35 and age<=39:
        points -= 4
    elif age>=40 and age<=44:
        points = 0
    elif age>=45 and age<=49:
        points += 3
    elif age>=50 and age<=54:
        points += 6
    elif age>=55 and age<=59:
        points += 8
    elif age>=60 and age<=64:
        points += 10
    elif age>=65 and age<=69:
        points += 11
    elif age>=70 and age<=74:
        points += 12
    elif age>=75 and age<=79:
        points += 13
    else:
        print("Age out of range")
        flag = 1

    if age>=20 and age<=39:
        if total_chol<160:
            points += 0
        elif total_chol>=160 and total_chol<=199:
            points += 4
        elif total_chol>=200 and total_chol<=239:
            points += 7
        elif total_chol>=240 and total_chol<=279:
            points += 9
        elif total_chol>=280:
            points += 11
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker=='1':
            points += 8
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=40 and age<=49:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 3
        elif total_chol >= 200 and total_chol <= 239:
            points += 5
        elif total_chol >= 240 and total_chol <= 279:
            points += 6
        elif total_chol >= 280:
            points += 8
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 5
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=50 and age<=59:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 2
        elif total_chol >= 200 and total_chol <= 239:
            points += 3
        elif total_chol >= 240 and total_chol <= 279:
            points += 4
        elif total_chol >= 280:
            points += 5
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 3
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=60 and age<=69:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 1
        elif total_chol >= 200 and total_chol <= 239:
            points += 1
        elif total_chol >= 240 and total_chol <= 279:
            points += 2
        elif total_chol >= 280:
            points += 3
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 1
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=70 and age<=79:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 0
        elif total_chol >= 200 and total_chol <= 239:
            points += 0
        elif total_chol >= 240 and total_chol <= 279:
            points += 1
        elif total_chol >= 280:
            points += 1
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 1
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1

    if hdl>=60:
        points -= 1
    elif hdl>=50 and hdl<=59:
        points += 0
    elif hdl>=40 and hdl<=49:
        points += 1
    elif hdl<40:
        points += 2
    else:
        print("Invalid input")
        flag = 1

    if sys_treat=='0':
        if sys_bp<120:
            points += 0
        elif sys_bp>=120 and sys_bp<=129:
            points+= 0
        elif sys_bp >= 130 and sys_bp <= 139:
            points += 1
        elif sys_bp >= 140 and sys_bp <= 159:
            points += 1
        elif sys_bp >= 160:
            points += 2
        else:
            print("Invalid input")
            flag = 1
    elif sys_treat=='1':
        if sys_bp<120:
            points += 0
        elif sys_bp>=120 and sys_bp<=129:
            points+= 1
        elif sys_bp >= 130 and sys_bp <= 139:
            points += 2
        elif sys_bp >= 140 and sys_bp <= 159:
            points += 2
        elif sys_bp >= 160:
            points += 3
        else:
            print("Invalid input")
            flag = 1
    else:
        print("Invalid input")
        flag = 1

    if flag == 0:
        if points<0:
            print("Risk is <1%")
        elif points==0:
            print("Risk is 1%")
        elif points == 1:
            print("Risk is 1%")
        elif points == 2:
            print("Risk is 1%")
        elif points == 3:
            print("Risk is 1%")
        elif points == 4:
            print("Risk is 1%")
        elif points == 5:
            print("Risk is 2%")
        elif points == 6:
            print("Risk is 2%")
        elif points == 7:
            print("Risk is 3%")
        elif points == 8:
            print("Risk is 4%")
        elif points == 9:
            print("Risk is 5%")
        elif points == 10:
            print("Risk is 6%")
        elif points == 11:
            print("Risk is 8%")
        elif points == 12:
            print("Risk is 10%")
        elif points == 13:
            print("Risk is 12%")
        elif points == 14:
            print("Risk is 16%")
        elif points == 15:
            print("Risk is 20%")
        elif points == 16:
            print("Risk is 25%")
        elif points>=17:
            print("Risk is >=30%")
    else:
        print("Invalid input")

elif gender=='f':
    #person is female
    if age>=20 and age<=34:
        points -= 7
    elif age>=35 and age<=39:
        points -= 3
    elif age>=40 and age<=44:
        points = 0
    elif age>=45 and age<=49:
        points += 3
    elif age>=50 and age<=54:
        points += 6
    elif age>=55 and age<=59:
        points += 8
    elif age>=60 and age<=64:
        points += 10
    elif age>=65 and age<=69:
        points += 12
    elif age>=70 and age<=74:
        points += 14
    elif age>=75 and age<=79:
        points += 16
    else:
        print("Age out of range")
        flag = 1

    if age>=20 and age<=39:
        if total_chol<160:
            points += 0
        elif total_chol>=160 and total_chol<=199:
            points += 4
        elif total_chol>=200 and total_chol<=239:
            points += 8
        elif total_chol>=240 and total_chol<=279:
            points += 11
        elif total_chol>=280:
            points += 13
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker=='1':
            points += 9
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=40 and age<=49:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 3
        elif total_chol >= 200 and total_chol <= 239:
            points += 6
        elif total_chol >= 240 and total_chol <= 279:
            points += 8
        elif total_chol >= 280:
            points += 10
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 7
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=50 and age<=59:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 2
        elif total_chol >= 200 and total_chol <= 239:
            points += 4
        elif total_chol >= 240 and total_chol <= 279:
            points += 5
        elif total_chol >= 280:
            points += 7
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 4
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=60 and age<=69:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 1
        elif total_chol >= 200 and total_chol <= 239:
            points += 2
        elif total_chol >= 240 and total_chol <= 279:
            points += 3
        elif total_chol >= 280:
            points += 4
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 2
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    elif age>=70 and age<=79:
        if total_chol < 160:
            points += 0
        elif total_chol >= 160 and total_chol <= 199:
            points += 1
        elif total_chol >= 200 and total_chol <= 239:
            points += 1
        elif total_chol >= 240 and total_chol <= 279:
            points += 2
        elif total_chol >= 280:
            points += 2
        else:
            print("Wrong input for cholesterol level.")
            flag = 1

        if smoker == '1':
            points += 1
        elif smoker == '0':
            points += 0
        else:
            print("Invalid input")
            flag = 1
    else:
        print("Age out of range")
        flag = 1

    if hdl>=60:
        points -= 1
    elif hdl>=50 and hdl<=59:
        points += 0
    elif hdl>=40 and hdl<=49:
        points += 1
    elif hdl<40:
        points += 2
    else:
        print("Invalid input")
        flag = 1

    if sys_treat=='0':
        if sys_bp<120:
            points += 0
        elif sys_bp>=120 and sys_bp<=129:
            points+= 1
        elif sys_bp >= 130 and sys_bp <= 139:
            points += 2
        elif sys_bp >= 140 and sys_bp <= 159:
            points += 3
        elif sys_bp >= 160:
            points += 4
        else:
            print("Invalid input")
            flag = 1
    elif sys_treat=='1':
        if sys_bp<120:
            points += 0
        elif sys_bp>=120 and sys_bp<=129:
            points+= 3
        elif sys_bp >= 130 and sys_bp <= 139:
            points += 4
        elif sys_bp >= 140 and sys_bp <= 159:
            points += 5
        elif sys_bp >= 160:
            points += 6
        else:
            flag = 1
            print("Invalid input")
    else:
        print("Invalid input")
        flag = 1

    if flag == 0:
        if points<9:
            print("Risk is <1%")
        elif points==9:
            print("Risk is 1%")
        elif points == 10:
            print("Risk is 1%")
        elif points == 11:
            print("Risk is 1%")
        elif points == 12:
            print("Risk is 1%")
        elif points == 13:
            print("Risk is 2%")
        elif points == 14:
            print("Risk is 2%")
        elif points == 15:
            print("Risk is 3%")
        elif points == 16:
            print("Risk is 4%")
        elif points == 17:
            print("Risk is 5%")
        elif points == 18:
            print("Risk is 6%")
        elif points == 19:
            print("Risk is 8%")
        elif points == 20:
            print("Risk is 11%")
        elif points == 21:
            print("Risk is 14%")
        elif points == 22:
            print("Risk is 17%")
        elif points == 23:
            print("Risk is 22%")
        elif points == 24:
            print("Risk is 27%")
        elif points>=25:
            print("Risk is >=30%")
    else:
        print("Invalid input")

else:
    #wrong input for gender
    print("Rerun the program with correct input.")

