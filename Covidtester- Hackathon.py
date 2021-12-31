import time
run = True 

name = input("Hello, welcome to the Covid tester. (Please enter your name):")
print()

tester = ""
while tester != "Yes" and tester != "No":
    tester = input("Hello " + name + ". Our world is dealing with a hard time during the Covid pandemic. All of us have seen alot and it is"
    " time to take care of ourselves. Do you want to take this Covid test? Yes or No: ") 
    print() 
      
if tester == "Yes":
    print("Thank you for agreeing, we are here to insure everyones safety, please select accurate answers and stay safe!")
    time.sleep(3)
    print()
elif tester == "No": 
    print("Hope you have a great day, Please ignore the next question")  

vaccine = ""

while True: 
    vaccine = input("Have you recieved your covid vaccine yet? Yes or No:")
    print()
    break

while True: 
    if vaccine == "Yes": 
        vaccinated = input("Are you fully vaccinated? Yes or No?: ")
    break

if vaccine == "Yes":
        print() 
        symptoms = input("Are you facing any of the following symptoms,:"
        " Fever or chills, Lost of taste or smell, Difficulty breathing, Extreme tiredness (Yes or No): ")
elif vaccine == "No": 
        print()

        symptoms = input("Are you facing any of the following symptoms:"
        " Fever or chills, Lost of taste or smell, Difficulty breathing, Extreme tiredness (Yes or No):")
if symptoms == "Yes":
        print("Please isolate and get tested. Thank you!")  
elif symptoms == "No": 
        contact = input("Have you been in close contact with someone who currently has Covid-19? Yes or No: ")
        if contact == "Yes":
            print("Please isolate and get tested. Thank you!")
            print()
        elif contact == "No":
            print("Thank you for taking the test, continue to follow Covid health and safety protocols to stay safe and the people around you!")
            print()
              
