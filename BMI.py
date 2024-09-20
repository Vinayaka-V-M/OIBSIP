# Body Mass Index Calculator :-

try:
    weight=float(input("Enter the weight:"))                   #taking input
    height=float(input("Enter the height in feet:"))           #taking input
    height_2 = height*0.3048                                   #coversion
    
    if weight<=0 or height<=0:
        print("!INVALID INPUT , Height and Weight should be above 0.")
    
    else :
        bmi=weight/(height_2**2)                               #formula for bmi.
        if bmi <= 18.5:
            category = "You are a underweight"
        elif 18.5 <= bmi < 24.9:
            category = "you are normal weight."
        elif 24.9 <= bmi < 29.9:
            category = "you are overweight "
        else :
            category = "Obesity!"
        
        print(f"Your BMI is:{bmi:.2f}")                         #bmi output
        print(f"Category is :{category}")                       
    

except ValueError:
    print("INVALID INPUT ! please enter a numerical value.")     #Error Handeling
