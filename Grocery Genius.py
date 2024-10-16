#================================================
#
#  Title:       <Grocery Genius.py>
#  Author:      <Lizbeth Alatorre>
#  Date:        <9/29/2023>
#  Description:
#       <This program prompts the clerk to input a single-character code, and then
#       calculates milk type’s cost multiplied by the number of gallons purchased in   #	order output total cost of milk purchase.>
#  Special Concerns: <if any>
#
#================================================

# Declaration of Variables
milkTypes = ["Whole", "2Percent", "Skim"]
selectedMilkType = ""
costPerGal = [4.00,3.50,3.00]
milkCost = 0.0
milkCode = ""
numbOfGal = 0
total = 0.0

# Input Section
print("Grocery Genius")
print("==========================")
milkCode = input("Enter milk type (w=whole; t=2Percent; s=skim): ")
numbOfGal = int(input("Enter the gallons: "))
print()

# Processing/Calculations Section
if (milkCode == "w"):
    selectedMilkType = milkTypes[0]
    milkCost = costPerGal[0]
elif (milkCode == "W"):
    selectedMilkType = milkTypes[0]
    milkCost = costPerGal[0]
if (milkCode == "t"):
    selectedMilkType = milkTypes[1]
    milkCost = costPerGal[1]
elif (milkCode == "T"):
    selectedMilkType = milkTypes[1]
    milkCost = costPerGal[1]
if (milkCode == "s"):
    selectedMilkType = milkTypes[2]
    milkCost = costPerGal[2]
elif (milkCode == "S"):
    selectedMilkType = milkTypes[2]
    milkCost = costPerGal[2]

total = milkCost*numbOfGal
    
# Output Section
print("Milk Type purchased:       {0:>10s}".format(selectedMilkType))
print("Gallons purchased:         {0:>10d}".format(numbOfGal))
print("Cost per gallon:        ${0:12.2f}".format(milkCost))
print("Total:                  ${0:12.2f}".format(total))
print()
print("End of Milk Lovers Grocery Store")
