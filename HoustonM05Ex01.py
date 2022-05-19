#Defining variables in main function

def main():

    monthlySales = inputSales()

    countyTaxes = calcCounty(monthlySales)

    stateTaxes = calcState(monthlySales)

    totalTaxes = calctotalTaxes(monthlySales)

    printInfo(countyTaxes, stateTaxes, totalTaxes)

def inputSales():

    monthlySales = float(input('Enter sales for the month: $')) #Must be a float input for the multiplication of decimals

    return monthlySales

def calcCounty(monthlySales):

    countyTaxes = monthlySales * .025

    return countyTaxes

def calcState(monthlySales):

    stateTaxes = monthlySales * .05

    return stateTaxes

def calctotalTaxes(monthlySales):

    totalTaxes = monthlySales * .075  #Taxes combined for the multiplication of total sales tax

    return totalTaxes

def printInfo(countyTaxes, stateTaxes, totalTaxes):
    print('The county taxes are $', countyTaxes)
    print('The state taxes are $', stateTaxes)
    print('The total taxes are $', totalTaxes)

main()