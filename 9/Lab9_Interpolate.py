# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab9_Interpolate
# Date:       	22 OCTOBER 2019
print('Hello! This program uses interpolation to estimate data values, given temperature.')
p = int(input('Enter the pressure value in MPa: ')) #taking pressure input
flag = True
#checking for valid input and opening the corresponding file
if p==5:
     data = open('Lab9_ThermoProperties_5MPa.csv','r', encoding='UTF-8')
     flag = True
elif p==10:
     data = open('ThermoProperties_10MPa.csv','r')
     flag = True
     print(data)
else:
     print("Invalid input.")
     flag = False
lists = []
tol = []
#for correct input
if flag:
     temp = float(input("Enter a temperature: ")) #taking temperature input
     if p==5:
          for i in data:
               lists.append(i.split('\t')) #extracting rows into list elements
          for i in range(len(lists)):
               for j in range(5):
                    lists[i][j] = float(lists[i][j]) #converting from string to float
          for i in range(len(lists)):
               tol.append(abs(temp - lists[i][0])) #storing differences between entered temperature and the ith temperature
          min1 = min(tol) #first bracketing temperature value
          min1_i = tol.index(min1)
          x1 = lists[min1_i][0]
          tol.pop(min1_i)
          min2 = min(tol) #second bracketing temperature value
          tol.insert(min1_i,min1)
          min2_i = tol.index(min2)
          x2 = lists[min2_i][0]
          #x1 and x2 are the temperature bracketing values

          # for volume
          y1 = lists[min1_i][1]
          y2 = lists[min2_i][1]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated volume for temperature", temp, 'degrees is:', y, 'm^3/kg')

          # for internal energy
          y1 = lists[min1_i][2]
          y2 = lists[min2_i][2]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated internal energy for temperature", temp, 'degrees is:', y, 'kJ/kg')

          # for enthalpy
          y1 = lists[min1_i][3]
          y2 = lists[min2_i][3]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated enthalpy for temperature", temp, 'degrees is:', y, 'kJ/kg')

          # for entropy
          y1 = lists[min1_i][4]
          y2 = lists[min2_i][4]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated entropy for temperature", temp, 'degrees is:', y, 'kJ/(kg K)')
     elif p==10:
          for i in data:
               lists.append(i.split(','))
          print(lists)
          for i in range(len(lists)):
               for j in range(5):
                    lists[i][j] = float(lists[i][j])
          for i in range(len(lists)):
               tol.append(abs(temp - lists[i][0]))
          min1 = min(tol)
          min1_i = tol.index(min1)
          x1 = lists[min1_i][0]
          tol.pop(min1_i)
          min2 = min(tol)
          tol.insert(min1_i, min1)
          min2_i = tol.index(min2)
          x2 = lists[min2_i][0]
          # x1 and x2 are the temperature bracketing values

          # for volume
          y1 = lists[min1_i][1]
          y2 = lists[min2_i][1]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated volume for temperature", temp, 'degrees is:', y, 'm^3/kg')

          # for internal energy
          y1 = lists[min1_i][2]
          y2 = lists[min2_i][2]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated internal energy for temperature", temp, 'degrees is:', y, 'kJ/kg')

          # for enthalpy
          y1 = lists[min1_i][3]
          y2 = lists[min2_i][3]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated enthalpy for temperature", temp, 'degrees is:', y, 'kJ/kg')

          # for entropy
          y1 = lists[min1_i][4]
          y2 = lists[min2_i][4]
          m = (y2 - y1) / (x2 - x1)
          y = m * (temp - x1) + y1
          print("The estimated entropy for temperature", temp, 'degrees is:', y, 'kJ/(kg K)')




