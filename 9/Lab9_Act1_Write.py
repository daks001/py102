# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Names:      	DAKSHIKA SRIVASTAVA
# 	        	MAHIRAH SAMAH
# 	        	MIKE MARTIN
# Section:    	532
# Assignment: 	Lab9_Act0
# Date:       	22 OCTOBER 2019

# temperature in degrees C
tempC = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]

# specific volume in m^3/kg
v = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.001041,
     0.0010576, 0.0010769, 0.0010988, 0.001124, 0.0011531, 0.0011868,
     0.0012268, 0.0012755]

# internal energy in kJ/kg
u = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65, 501.91, 586.8, 672.55,
     759.47, 847.92, 938.39, 1031.6, 1128.5]

# enthalpy in kJ/kg
h = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85, 507.19, 592.18,
     678.04, 765.09, 853.68, 944.32, 1037.7, 1134.9]

# entropy in kJ/(kg K)
s = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344,
     1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]

data = open('Lab9_ThermoProperties_5MPa.csv', 'w')

for i in range(len(tempC)):
    data.write(str(tempC[i])+'\t'+str(v[i])+'\t'+str(u[i])+'\t'+str(h[i])+'\t'+str(s[i])+'\n') #writing data