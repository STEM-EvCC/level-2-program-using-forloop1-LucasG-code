#Data Sample
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#functions
#Mission success rate function
def SuccessRate(x, y):
    Rate = (x / y) * 100
    return Rate

#function to call repeatedly for adding data to our lists
def DataAdd():
    AddedName = input("What is the Name of the Mission?: ")
    mission_names.append(AddedName)
    AddedYear = int(input("What year did the mission occur or was planned for?: "))
    mission_years.append(AddedYear)
    AddedSuccess = bool(input("Was this mission a success? True or False: "))
    mission_success.append(AddedSuccess)

#Start here, info gathering
print("_________________________")
print("Space Missions Stats and Year report!")
InputYear = int(input("\nPlease input a year to continue: ")) #Year Assigned here
BoA = input("Would you like these displayed missions to be before or after " + str(InputYear) + "? Type Before or After: ") #Before or After Assigned here in BoA
print("\nOur Dataset is currently limited to a small selection")
Choice = input("Would you like to add onto the mission list? Yes or No: ")
while Choice == "yes" or Choice == "Yes":
    DataAdd() #function call
    Choice = input("Would you like to add another entry? Yes or No: ")
print("_________________________")


#Total number of missions accounted for here, any list if all up to date should work if plugged in here
SpaceMissions = len(mission_years)

#Counts the number of successful missions
successlist = []
index = 0
for success in mission_success:
    if mission_success[index] is True:
        successlist.append(True)
        index += 1
    else: index += 1
SuccessfulMissions = len(successlist)

#percentage of successful missions, calls SuccessRate function from above
SuccessPercentage = SuccessRate(SuccessfulMissions, SpaceMissions)

#Missions before or after or during a certain year
BeforeYear = []
AfterYear = []
CurrentYear = []
index = 0 
for Year in mission_years:
    if mission_years[index] < InputYear: #If Year is Before
        BeforeYear.append(mission_names[index])
        index += 1
    elif mission_years[index] > InputYear: #If Year is After
        AfterYear.append(mission_names[index])
        index += 1
    else:  #Else it's during the Current Input year
        CurrentYear.append(mission_names[index])
        index += 1

#Final print out and program end point
print("Final Stats")
print("_________________________")
print("Total number of missions: " + str(SpaceMissions))
print("Number of successful missions: " + str(SuccessfulMissions))
print(f"Success Rate: {SuccessPercentage:.2f}%")
print("Missions during " + str(InputYear) + ": " + str(CurrentYear))
if BoA == "Before" or BoA == "before": #Choice if Before is choosen, assigned at the into
    print("Missions launched before the year: " + str(InputYear))
    for BF in BeforeYear:
        print(BF)
elif BoA == "After" or BoA == "after":  #Choice if After is choosen, assigned at the into
    print("Missions launched after the year: " + str(InputYear))
    for AY in AfterYear:
        print(AY)
print("_________________________")



#    .--.
#   /( @ >    ,-.
#  / ' .'--._/  /
#  :   ,    , .'
#  '. (___.'_/
#    ((-((-''