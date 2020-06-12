# ASSIGNMENT-2 JULIO SUNI

#IMPORTING THE REQUIRED LIBRARIES FOR THE CODE.
import pandas as pd
import matplotlib.pyplot as plt


#STEP 2: READING THE FILE AND HANDLING ERROR IN CASE THE FILE IS NOT FOUND.
try:
    #GIVING FORMAT TO THE DATA:
    pd.options.display.float_format = "{:.2f}".format

    #FINALLY READING THE FILE:
    df = pd.read_csv("50000 Sales Records.csv")

except FileNotFoundError:
    print("Sorry and error has occured. File not found!")
    exit()

#ADJUSTING THE NAME FO THE COLUMS. LOWER CASE, STRIPPIN SPACES AND REPLACING SYMBOLS THAT WOULD CASE ERRORS.
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")


#STEP 3: CREATING FUNCTIONS THE USER WILL CALL WHEN USING THE MENU.

def country_profit(country):
    country_profit_result = df.groupby("country")["total_profit"].sum()[country]
    print("The profit of country \"" + country + "\" is $", round(country_profit_result, 2))

def region_profit(region):
    region_profit_result = df.groupby("region")["total_profit"].sum()[region]
    print("The proftit of region '" + region + "' is $", round(region_profit_result, 2))

def barchart_totalprofit_percountry():
    total_profit_per_country = df.groupby("country")["total_profit"].sum()
    total_profit_per_country.plot(kind="bar", x="country", y="total_profit")
    plt.title("TOTAL PROFIT PER COUNTRY", fontsize=20, c="brown")
    plt.xlabel("Countries", c="blue")
    plt.ylabel("Total Profit", c="blue")
    plt.show()

def piechart_totalprofit_perregion():
    total_profit_per_region = df.groupby("region")["total_profit"].sum()
    total_profit_per_region.plot(kind="pie", x="country", y="total_profit")
    plt.title("TOTAL PROFIT PER REGION", fontsize=20, c="brown")
    plt.xlabel("Countries", c="blue")
    plt.ylabel("Total Profit", c="blue")
    plt.legend(sorted(df.region.unique()))
    plt.show()


#STEP 4: CREATING A MENU FOR THE USER TO INTERACT WITH THE PROGRAM

while True:

    #MENU SELECTION:
    function = input("""\nWelcome to Data Analysis tools.\n
    Select from one of the following options:
    1) Total profit based on a country
    2) Total profit based on a region
    3) Bar chart for total profit per country
    4) Pie chart for total profit in each region
    5) Exit\n\n""")


    #DEPENDING ON THE NUMBER THE USER SELECTS, THE CODE WILL RUN A DIFFERENT QUESTION AND/OR FUNCTION:

    if function == "1":
        countryselected = input("Please provide the name of the country:\n")
        try:
            country_profit(countryselected)
        except:
            print("Invalid country. Please consider using uppercase for the first letter. Restarting program. Please select again:")
        #PLEASE NOTE THAT I COULD HAVE USER ANOTHER "while True" STATEMENT IN ORDER NOT TO RESTART THE PROGRAM FROM THE BEGINNING BUT FROM THE COUNTRY SELECTION.
        #BUT I PREFERED TO RESTART THE PROGRAM FROM THE TOP


    elif function == "2":
        regionselected = input("Please provide the name of the region:\n")
        try:
            region_profit(regionselected)
        except:
            print("Invalid region. Please consider using uppercase for the first letter. Restarting program. Please select again:")
        # PLEASE NOTE THAT I COULD HAVE USER ANOTHER "while True" STATEMENT IN ORDER NOT TO RESTART THE PROGRAM FROM THE BEGINNING BUT FROM THE REGION SELECTION.
        # BUT I PREFERED TO RESTART THE PROGRAM FROM THE TOP


    elif function == "3":
        barchart_totalprofit_percountry()

    elif function == "4":
        piechart_totalprofit_perregion()

    elif function == "5":
        exit()

    else:
        print("Invalid selection. Restarting program . Please select again:")



