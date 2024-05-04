hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
# Loop through the prices list and add each price to the variable total_price.
for num in prices:
  total_price += num

#Get average price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#Cut all prices by 5 dollars.
new_prices = [num - 5 for num in prices]
print(new_prices)

# After your loop, print the value of total_revenue, so the output looks like:
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue:",total_revenue)

average_daily_revenue = total_revenue / 7
print("Average daily revenue:",average_daily_revenue)

# Really confused part
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Cut prices under 30:",cuts_under_30)
