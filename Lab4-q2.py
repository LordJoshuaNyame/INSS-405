#Hot
#Warm
#Cold
#Extremely_cold

temperature = 5

for i in range (temperature):
    temperature = int(input('enter temperature'))
    if (int(temperature)) >= 50:
        print('Hot')
    elif(int(temperature) >= 30 and int(temperature) <50):
        print('Warm')
    elif(int(temperature) >= 0 and int(temperature) <30):
        print('Cold')
    elif(int(temperature) <0):
        print('Extreme cold')