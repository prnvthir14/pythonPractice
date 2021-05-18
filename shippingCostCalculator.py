package_weight = input("Enter your package weight in lbs:")
print(package_weight)
package_weight_float = float(package_weight)
print("package_weight_float", package_weight_float)

# 3 options, :
# 
# ground Shipping
# 
# 
# Ground shipping premium 
# 
# 
# Drone shipping 
#
# Calculate each cost based on weight provided and return the smallest value
# 
#  

groundCost = 0
groundPremiumCost = 125
droneCost = 0

# all optinons have same weight cutoffs

if (package_weight_float <= 2.0):
  #calc indiviudal costs
  groundCost = 1.50*package_weight_float + 20.0
  droneCost  = 4.50*package_weight_float

elif (package_weight_float > 2.0 and package_weight_float <= 6.0):
  #calc indiviudal costs
  groundCost = 3.0*package_weight_float + 20.0
  droneCost  = 9.0*package_weight_float

elif (package_weight_float > 6.0 and package_weight_float <= 10.0):
  #calc indiviudal costs
  groundCost = 4.0*package_weight_float + 20.0
  droneCost  = 12.0*package_weight_float

elif (package_weight_float > 10.0):
  #calc indiviudal costs
  groundCost = 4.75*package_weight_float + 20.0
  droneCost  = 14.25*package_weight_float  

else:
  print("invalid weight")

print(groundCost,
groundPremiumCost,
droneCost)  

#
# Test each class

#  lbs expected_cost_ground expected_cost_drone 
#  1   21.50                4.50 ---PASS
#  4   32                   36 ---PASS
#  7   48                   84 --Pass -- 41.0 125 63.0
#  11  72.25                156.75 --pass

