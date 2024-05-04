weight = 41.5

#check for ground shipping and drone shipping
if weight <= 2:
  ground_total_cost = 1.50 * weight + 20
  drone_total_cost = 4.50 * weight

elif (weight > 2) and (weight <= 6):
  ground_total_cost = 3.00 * weight + 20
  drone_total_cost = 9.00 * weight

elif (weight > 6) and (weight <= 10):
  ground_total_cost = 4.00 * weight + 20
  drone_total_cost = 12.00 * weight

elif (weight > 10):
  ground_total_cost = 4.75 * weight + 20
  drone_total_cost = 14.25 * weight

else:
  print("Error")

premium_cost_total = 125.00

print("Ground shipping cost: ")
print(ground_total_cost)

print("Premium shipping cost: ")
print(premium_cost_total)

print("Drone shipping cost: ")
print(drone_total_cost)

#Result: checking the weight 4.8 pounds and 41.5 pounds, ground shipping cost is the cheapest under both situations.
