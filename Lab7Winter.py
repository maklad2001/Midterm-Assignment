import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
df = pd.read_csv('Data.csv')



# Step 2 and 4: Total Sale
df = df.rename(columns=({'Month':'Year'}))
year_x_axis=[]
sales_y_axis=[]



# this is used to calculate the estimated sales for 2022
sales_last_six_months_2021=[]

# these are used to calculate the SGR (sales growth rate)
a=0
b=0

with open('stats.txt', 'w') as f:
    for i in range(0, len(df)):
        # gets the year and sales of that year
        year=df.iloc[i][0]
        sales=df.iloc[i][1:].sum()
        # puts it in array so we can plot
        year_x_axis.append(year)
        sales_y_axis.append(sales)

        # step 4: get total sales of first 6 months in 2021
        if year==2021:
            total_sales_first_six_months_2021=df.iloc[i][1:7].sum()
            a = total_sales_first_six_months_2021
            print('Sales for first 6 months of 2021: ', total_sales_first_six_months_2021)

            # put the last six months of sales in 2021 in list so we can loop thru it later
            for sale in df.iloc[i][7:13]:
                sales_last_six_months_2021.append(sale)



        # step 4: get total sales of first 6 months in 2022
        if year==2022:
            total_sales_first_six_months_2022=df.iloc[i][1:7].sum()
            b = total_sales_first_six_months_2022
            print('Sales for first 6 months of 2022: ', total_sales_first_six_months_2022)



        f.write(f"{year}: {sales}\n")

    # Step 3: Bar Plot
    plt.figure(1)
    plt.bar(year_x_axis, sales_y_axis)
    plt.title('Total Sales per Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.savefig('total_sales.png')

    # to write the SGR to the stats.txt
    SGR = ((a - b) / a)
    SGR_string = str(round(SGR*100, 2)) + "%"
    f.write(f"\nSales Growth Rate (SGR): {SGR_string}\n")
    print(SGR)

    # Estimated sale in month M of 2022 = Sale in month M of 2021 + Sale in month M of 2021 ∗ SGR
    y_axis_last_six_months_estimated_sales_2022=[]

    f.write(f"\nEstimated sales for July-December:\n")
    for j in sales_last_six_months_2021:
        estimated_month_sales_2022 = round(j + (j*SGR))
        y_axis_last_six_months_estimated_sales_2022.append(estimated_month_sales_2022)

        f.write(f"\n{estimated_month_sales_2022}")

    # Step 5: Horizontal Bar Plot

    x_axis_last_six_months_2022=['Jul','Aug','Sep','Oct','Nov','Dec']
    plt.figure(2)
    plt.barh(x_axis_last_six_months_2022, y_axis_last_six_months_estimated_sales_2022)
    plt.title('Estimated Sales for Jul-Dec 2022')
    plt.xlabel('Sales')
    plt.ylabel('Month')
    plt.savefig('estimated_sales.png')



