
class InventoryAllocator:
	# assume print is LOG in production...
	def get_shipments(self, orders, warehouses):
		import collections
		if not orders or not warehouses:
			print("orders or warehouses is null")
			return []

		# remove any possible human/front errors...
		# negative or 0 quantity orders should not exist
		orders = {fruit:quantity for fruit, quantity in orders.items() if int(quantity) > 0}

		if not self.enough_supplies_to_fufill(orders, warehouses):
			return []
		warehouse_supplies = collections.defaultdict(list)

		for warehouse in warehouses:
			warehouse_name = warehouse["name"]
			for warehouse_fruit in warehouse["inventory"]:
				warehouse_supplies[warehouse_fruit].append({warehouse_name:warehouse["inventory"][warehouse_fruit]})

		warehouse_supplies_used = collections.defaultdict(dict)
		shipment = []

		for fruit in orders:
			order_fruit_quantity = orders[fruit]
			for warehouse_map in warehouse_supplies[fruit]:
				if order_fruit_quantity == 0: break
				for warehouse_location, warehouse_fruit_quantity in warehouse_map.items():
					if warehouse_fruit_quantity == 0: continue

					if order_fruit_quantity > warehouse_fruit_quantity:
						warehouse_map[warehouse_location] -= warehouse_fruit_quantity
						warehouse_supplies_used[warehouse_location].update({fruit: warehouse_fruit_quantity})
					else:
						warehouse_map[warehouse_location] -= order_fruit_quantity
						warehouse_supplies_used[warehouse_location].update({fruit: order_fruit_quantity})
					order_fruit_quantity -= min(warehouse_fruit_quantity, order_fruit_quantity)

		for warehouse_location in warehouse_supplies_used:
			shipment.append({warehouse_location: warehouse_supplies_used[warehouse_location]})
		return shipment

	def enough_supplies_to_fufill(self, orders, warehouses):
		import collections

		all_warehouse_supplies = collections.defaultdict(int)
		for warehouse in warehouses:
			for fruit in warehouse["inventory"]:
				all_warehouse_supplies[fruit] += warehouse["inventory"][fruit]

		for fruit in orders:
			if fruit not in all_warehouse_supplies:
				print("Warehouses do not contain the fruit: %s"% fruit)
				return False
			elif orders[fruit] > all_warehouse_supplies[fruit]:
				print("Not enough fruit of type %s to fufill the order."% fruit)
				return False
		return True
