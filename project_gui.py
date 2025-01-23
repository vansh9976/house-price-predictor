from tkinter import *
import project

#functions
def predict():
    #Land Area Value
    landAreaValue = landAreaInput.get()
    landAreaValue = float(landAreaValue)

    #Floor Area Value
    floorAreaValue = floorAreaInput.get()
    floorAreaValue = float(floorAreaValue)

    #Bedrooms Count
    bedroomsMenuValue = valueInsideBedrooms.get()
    bedroomsMenuValue = int(bedroomsMenuValue)

    #Bathrooms Count
    bathroomsMenuValue = valueInsideBathrooms.get()
    bathroomsMenuValue = int(bathroomsMenuValue)

    #Garage Count
    garageMenuValue = valueInsideGarage.get()
    garageMenuValue = int(garageMenuValue)

    #Build Year
    buildYearMenuValue = valueInsideBuildYear.get()
    buildYearMenuValue = int(buildYearMenuValue)

    predictedValue = project.model(landAreaValue, floorAreaValue, bedroomsMenuValue, bathroomsMenuValue, garageMenuValue, buildYearMenuValue)

    predictedValue = float(predictedValue)

    predictionBoxVar.set(predictedValue)

#Window 
root = Tk()
root.geometry("600x750")
root.title("Price Predictor")
root.config(bg="white")

#Variables, Lists
bedroomsCountList = []
bathroomsCountList = []
garageCountList = []
buildYearCountList = []

for i in range(1,11):
    bedroomsCountList.append(i)
    garageCountList.append(i)
bedroomsCountList.insert(0, "Select")
garageCountList.insert(0, "Select")

for i in range(1,17):
    bathroomsCountList.append(i)
bathroomsCountList.insert(0, "Select")

for i in range(1868, 2021):
    buildYearCountList.append(i)
buildYearCountList.insert(0, "Select")

predictionBoxVar = StringVar()

#Main Heading
mainHeading = Label(root, text="Price Predictor", font=("Arial", 25), pady=20, bg="white", fg="black").pack()

#Land Area
landAreaLabel = Label(root, text="Land Area in Sq ft", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
landAreaInput = Entry(root, font=('calibre',12), bg="pink", fg="black")
landAreaInput.pack()

#Floor Area
floorAreaLabel = Label(root, text="Floor Area in Sq ft", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
floorAreaInput = Entry(root, font=('calibre',12), bg="pink", fg="black")
floorAreaInput.pack()

#Bedrooms Option Menu
bedroomsLabel = Label(root, text="Bedrooms", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
valueInsideBedrooms = StringVar(root)
valueInsideBedrooms.set("Select")
bedroomsMenu = OptionMenu(root, valueInsideBedrooms, *bedroomsCountList)
bedroomsMenu.config(bg="white", fg="black")
bedroomsMenu.pack()

#Bathrooms Option Menu
bathroomsLabel = Label(root, text="Bathrooms", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
valueInsideBathrooms = StringVar(root)
valueInsideBathrooms.set("Select")
bathroomsMenu = OptionMenu(root, valueInsideBathrooms, *bathroomsCountList)
bathroomsMenu.pack()
bathroomsMenu.config(bg="white", fg="black")

#Garage Option Menu
garageLabel = Label(root, text="Garage", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
valueInsideGarage = StringVar(root)
valueInsideGarage.set("Select")
garageMenu = OptionMenu(root, valueInsideGarage, *garageCountList)
garageMenu.config(bg="white", fg="black")
garageMenu.pack()

#Build Year Option Menu
buildYearLabel = Label(root, text="Build Year", font=("Arial", 15), pady=20, bg="white", fg="black").pack()
valueInsideBuildYear = StringVar(root)
valueInsideBuildYear.set("Select")
buildYearMenu = OptionMenu(root, valueInsideBuildYear, *buildYearCountList)
buildYearMenu.config(bg="white", fg="black")
buildYearMenu.pack()

#Prediction UI area

predictButton = Button(root, text='Predict', highlightbackground="white", fg="black", bg="black", activebackground="red", borderwidth=0, command=predict)
predictButton.pack(pady=22)


predictionBox = Entry(root, textvariable=predictionBoxVar, font=('calibre',12), bg="pink", fg="black")
predictionBox.pack(pady=10)
australianDollar = Label(root, text="Price in dollars", bg="white", fg="black").pack()

#Main Loop
root.mainloop()