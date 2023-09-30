print("*****Welcome to Body Mass Index (BMI) Calculator*****")
print("Made By Vaskar Chakma, CS Student of Nantong University.")


print("In which type you want to enter your Height? (Write 'CM' for 'Centimeter'/ 'M' for 'Meter'/ 'I' for 'Inch'):  ")
height = input()
print("In which type you want to enter your Mass/Weight? (Write 'G' for Gram/ 'KG' for 'Kilogram'/ 'P' for 'Pound'): ")
mass = input()

if height == 'CM' and mass == 'G':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass * 0.001) / ((height * 0.01) * (height * 0.01))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*0.01)*(height*0.01)
        print(f"You're {int(age)} years old. You need to decrease {(mass*0.001) - newMass} KG ")
        
elif height == 'CM' and mass == 'KG':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = mass / ((height * 0.01) * (height * 0.01))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*0.01)*(height*0.01)
        print(f"You're {int(age)} years old. You need to decrease {(mass) - newMass} KG ")

elif height == 'CM' and mass == 'P':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass* 0.454) / ((height * 0.01) * (height * 0.01))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*0.01)*(height*0.01)
        print(f"You're {age} years old. You need to decrease {(mass*0.454) - newMass} KG ")

elif height == 'M' and mass == 'G':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass* 0.001) / (height * height)
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*height)
        print(f"You're {int(age)} years old. You need to decrease {(mass*0.001) - newMass} KG ")

elif height == 'M' and mass == 'KG':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = mass / (height * height)
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*height)
        print(f"You're {int(age)} years old. You need to decrease {(mass) - newMass} KG ")

elif height == 'M' and mass == 'P':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass* 0.454) / (height * height)
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * (height*height)
        print(f"You're {int(age)} years old. You need to decrease {(mass*0.454) - newMass} KG ")

elif height == 'I' and mass == 'G':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass* 0.001) / ((height*0.0254) * (height*0.0254))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * ((height*0.0254) * (height*0.0254))
        print(f"You're {int(age)} years old. You need to decrease {(mass*0.001) - newMass} KG ")

elif height == 'I' and mass == 'KG':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = mass / ((height*0.0254) * (height*0.0254))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * ((height*0.0254) * (height*0.0254))
        print(f"You're {int(age)} years old. You need to decrease {(mass) - newMass} KG ")

elif height == 'I' and mass == 'P':
    age, height, mass = map(float, input("Please Input Your Age, Height and Weight According to Your Selection: ").split())
    BMI = (mass* 0.454) / ((height*0.0254) * (height*0.0254))
    print(format(BMI,".2f"))
    if BMI < 18.5:
        print("Underweight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("""Normal Weight. "Congratulations!! You are perfect one.""")
    else:
        print("Obese")
        newMass = 21.7 * ((height*0.0254) * (height*0.0254))
        print(f"You're {int(age)} years old. You need to decrease {(mass*0.454) - newMass} KG ")