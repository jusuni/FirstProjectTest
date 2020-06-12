# ASSIGNMENT JULIO SUNI

# IMPORTING DATETIME TO BE USED AFTER WHEN CREATING THE REPORT:
import datetime
today = datetime.date.today()

# IMPORTING CSV TO BE ABLE TO READ THE CSV FILE
import csv as cs

# USING "try" AND "except" IN CASE THERE IS AN ERROR READING THE FILE:
try:
    #CREATING THE CONNECTION WITH THE FILE TO READ AND ANALYZE:

    with open("500000 Sales Records.csv") as opened_file:
        read_file = cs.reader(opened_file)
        data = list(read_file)

except:
    print("Sorry an error has occured")



#1) INITIALIZING AN EMPTY LIST OF REGIONS.
regions_list = []


#2.A) INITIALIZING A DICTIONARY FOR THE UNITS SOLD PER REGION.
units_sold_per_region = {}

#2.B) INITIALIZING A DICTIONARY FOR THE AVERAGE REVENUE FOR ALL THE UNITS (per order) SOLD PER REGION.
revenue_per_region = {}  #THIS ONE COULD HAVE BEEN USED FOR EXERCISE 2.C, BUT TO MAINTAIN THE ORDER OF THE QUESTIONS I WILL CREATE A DIFFERENT VARIABLE. THIS WILL EASE THE CODE LEGIBILITY ACCORDING TO THE ASSIGNMENT QUESTIONS.
counter_for_average = {} #THIS VARIALBE WILL COUNT HOW MANY ORDERS THERE ARE
final_avg_revenue_per_order = {} #WILL STORE THE AVERAGE REVENUE PER ORDER SEGREAGATED BY REGION
final_avg_revenue_per_unit = {} #WILL STORE THE AVERAGE REVENUE PER UNIT(PRODUCT) SEGREAGATED BY REGION AND WON'T BE USED IN THE REPORT SINCR THE ASSIGNMENT ASKS FOR THE REVENUE PER ORDER (VARIABLE RIGHT ABOVE THIS ONE)

#2.C) INITIALIZING A DICTIONARY WITH THE TOTAL REVENUE PER REGION.
sales_per_region = {} #HERE I AM CREATING A NEW VARIABLE BUT I COULD HAVE USED "revenue_per_region" FROM EXERCISE 2.B SINCE THEY WILL STORE THE SAME INFORMATION. I AM CREATING A NEW VARIABLE JUST FOR ORDER PURPOSES AND CODE LEGIBILITY.


#3.A) VARIABLE FOR BIG TOTAL OF UNITS SOLD.
total_units_sold = 0

#3.B) VARIABLE FOR THE AVERAGE REVENUE OF ALL THE UNIS SOLD.
total_revenue = 0
avg_revenue_per_unit = 0 #AS REQUIRED OF THE GRAND TOTAL, THE AVERAGE REVENUE POR UNIT(PRODUCT) WILL BE CALCULATED.


#LOOPS TO ANALYZE DATA.
for row in data[1:]:
    #GRABING DATA ACCORDING THE COLUMNS REQUIRED.
    region = row[0]
    unitssold = int(row[8])
    order_revenue = float(row[-3]) # YOU WILL NOTICE THIS VARIABLE HAS THE SAME INFORMTION OF THE VARIABLE BELOW "total_sale". I AM DOING THIS FOR ORGANIZATION AND ORDER PURPOSES TO FOLLOW THE QUESTION ORDER IN THE ASSIGNMENT.
    total_sale_of_the_order = float(row[-3]) # AS EXPLAINED IN THE COMMENT OF 2.B, 2C AND THE ONE ABOVE. I COULD HAVE USED "order_revenue" BUT FOR ORGANIZATION PURPOSES OF THE QUESTIONS I WILL USE A DIFFERENT VARIABLE ALSO TO KEEP THE LEGIBILITY OF THE CODE AND ORDER OF THE QUESTIONS IN THE ASSIGNMENT.



    #1) APPENDING THE LIST OF REGIONS.
    if region not in regions_list:
        regions_list.append(region)
    else:
        pass



    #2.A) ADDING INFORMATION TO THE DICTIONARY OF TOTAL UNITS SOLD PER REGION.
    if region not in units_sold_per_region:
        units_sold_per_region[region] = unitssold
    else:
        units_sold_per_region[region] += unitssold



    #2.B) ADDING INFORMATION TO THE DICTIONARY OF AVERAGE REVENUE PER ORDER PER REGION.
    if region in revenue_per_region:
        counter_for_average[region] += 1
        revenue_per_region[region] += order_revenue
    else:
        counter_for_average[region] = 1
        revenue_per_region[region] = order_revenue
    #THE STATEMENT BELOW IS THE AVG REVENUE PER ORDER SEGREGATED BY REGION. THIS IS THE INFORMATION THAT WILL BE USED TO ANSWER QUESTION 2.B AND WILL BE SHOWN IN THE REPORT.
    final_avg_revenue_per_order[region] = revenue_per_region[region]/counter_for_average[region]

    #THE STATEMENT BELOW IS CREATE IN ORDER TO CALCULATE THE AVG REVENUE PER UNIT(PRODUCT) SOLD. I CODED THIS JUST TO EXPERIMENT AND THIS WON'T BE SHOWN IN THE REPORT.
    final_avg_revenue_per_unit[region] = revenue_per_region[region]/units_sold_per_region[region]



    #2.C) ADDING INFORMATION TO THE DICTIONARY OF TOTAL REVENUE PER REGION.
    if region not in sales_per_region:
        sales_per_region[region] = total_sale_of_the_order
    else:
        sales_per_region[region] += total_sale_of_the_order



    #3.A) BIG TOTAL OF UNITS SOLD.
    total_units_sold += unitssold

    #3.B) THE AVERAGE REVENUE OF ALL THE UNITS SOLD.
    total_revenue += order_revenue
    avg_revenue_per_unit = total_revenue/total_units_sold

    #3.C THE TOTAL REVENUE.
    final_total_revenue = total_revenue



#4) CREATING THE SALES REPORT:

print("\n")
print("\n")
print("                                                                             SALES REPORT")
print("                                                                             ¯¯¯¯¯¯¯¯¯¯¯¯")
print("                                                                       Produced on:", today)
print("\n")
print("Regions analysed: ", regions_list)
print("\n")

counter = 0

for i in regions_list:
    counter += 1
print("Total, for %d regions." %counter)

print("\n")

for region in regions_list:
    print(region, "\n")
    print("Total units sold: ", round(units_sold_per_region[region], 2))
    print("Average revenue per order:  $", round(final_avg_revenue_per_order[region], 2)) #IN CASE WE WOULD LIKE TO SEE THE AVERAGE REVENUE PER UNIT(PRODUCT) SOLD WE ONLY NEED TO REPLACE THE VARIABLE "final_avg_revenue_per_order" FOR "final_avg_revenue_per_unit".
    print("Total revenue of sales:  $", round(sales_per_region[region], 2))
    print("\n")


print("Grand Totals")
print("Total units sold: ", round(total_units_sold, 2))
print("Average revenue per unit:  $", round(avg_revenue_per_unit,2)) #AVERAGE REVENUE PER UNIT(PRODUCT) OF ALL REGIONS.
print("Total revenue of sales:  $", round(final_total_revenue, 2))
