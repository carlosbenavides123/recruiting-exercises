### How to run this application

Have python3 installed

Clone this repo/fork

cd .\recruiting-exercises\inventory-allocator\src\

python3 .\TestInventoryAllocator.py

### How this application works

1) check if any wrong inputs, empty orders or warehouses

2) check if we can fulfill the order... aggregate all the fruits from all the warehouses then compare them to the order requirements
   if a fruit does not exist in the aggregated warehouse fruits, or if a order exceeds stock in aggregated warehouse... return [] because cannot fulfill

3) make a map of the fruit to the warehouse location and quantity

for example given:

            warehouses = [{"name": "owd","inventory": { "apple": 5, "orange": 10 }}, {"name": "dm","inventory": { "banana": 5, "orange": 10 } }
            order = { "apple": 5, "banana": 5, "orange": 5 }

we want to make a map that looks like:

    warehouse_supplies = {'apple': [{'owd': 5}], 'orange': [{'owd': 10}, {'dm': 10}], 'banana': [{'dm': 5}]})

    the map warehouse_supplies is... fruit -> list of dicts ({location: quantity of fruit})

after fulfilling the requirements, the warehouse_supplies should look like:

    {'apple': [{'owd': 0}], 'orange': [{'owd': 5}, {'dm': 10}], 'banana': [{'dm': 0}]})

we uses 5 apples and 5 oranges from owd
and 5 banandas from dm

the warehouse_supplies_used collects this ^ data

    warehouse_supplies_used = {'owd': {'apple': 5, 'orange': 5}, 'dm': {'banana': 5}})

then iterate over warehouse_supplies_used and return the result...

solution time: O(N*M), N = the amount of warehouses, M = the amount of unique fruit

solution space: O(N*M), worst case warehouses has 1 of every fruit and each fruit order has amount of N




