import unittest
from InventoryAllocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
	def setUp(self):
		self.allocator = InventoryAllocator()
		self.warehouses = [
			{"name": "la","inventory": {"apple": 5, "banana": 5, "plum": 1}},
			{"name": "nyc","inventory": {}},
			{"name": "sea","inventory": {"apple": 3, "grape": 3,"honeydew": 3, "plum": 1}},
			{"name": "sf","inventory": {"apple": 0, "grape": 2, "plum": 1}},
			{"name": "dvr","inventory": {"grape": 5, "plum": 1}},
			{"name": "owd","inventory": { "apple": 5, "orange": 10 }},
			{"name": "dm","inventory": { "banana": 5, "orange": 10 } }
		]

	def get_selected_warehouses(self, names):
		selected_warehouse = []
		for warehouse in self.warehouses:
			if warehouse['name'] in names:
				selected_warehouse.append(warehouse)

		return selected_warehouse

	def test_zero_order_zero_stock(self):
		order = {}
		warehouses = self.get_selected_warehouses(["nyc"])

		result = self.allocator.get_shipments(order, warehouses)
		expected = []

		self.assertEqual(result, expected)

	def test_zero_order_non_zero_stock(self):
		order = {}
		warehouses = self.get_selected_warehouses(["dvr"])

		result = self.allocator.get_shipments(order, warehouses)
		expected = []

		self.assertEqual(result, expected)

	def test_zero_order_all_warehouses(self):
		order = {}
		warehouses = self.get_selected_warehouses(["la"])

		result = self.allocator.get_shipments(order, self.warehouses)
		expected = []
		self.assertEqual(result, expected)

	def test_orders_fulfilled_in_two_warehouses(self):
		order = { "apple": 5, "banana": 5, "orange": 5 }
		warehouses = self.get_selected_warehouses(["owd", "dm"])
		result = self.allocator.get_shipments(order, warehouses)
		expected = [{"owd": {"apple": 5, "orange": 5}}, {"dm": {"banana": 5}}]
		self.assertEqual(result, expected)

	def test_warehouses_has_one_stock(self):
		order = { "plum": 4 }
		warehouses = self.get_selected_warehouses(["la", "sea", "sf", "dvr"])
		result = self.allocator.get_shipments(order, warehouses)
		expected = [{"la": {"plum": 1}}, {"sea": {"plum": 1}}, {"sf": {"plum": 1}}, {"dvr": {"plum": 1}} ]
		self.assertEqual(result, expected)

	def test_warehouse_cannot_fulfill_order(self):
		order = { "plum": 4 }
		warehouses = self.get_selected_warehouses(["nyc", "la"])
		result = self.allocator.get_shipments(order, warehouses)
		expected = []
		self.assertEqual(result, expected)

	def test_all_warehouses(self):
		order = { "plum": 4, "apple": 7, "banana": 5, "orange": 15, "grape": 5, "honeydew": 2, "grape": 10 }
		result = self.allocator.get_shipments(order, self.warehouses)
		expected = [
			{"la": {"apple": 5, "banana": 5, "plum": 1}},
			{"sea": {"apple": 2, "grape": 3, "honeydew": 2, "plum": 1}},
			{"sf": {"grape": 2, "plum": 1}},
			{"dvr": {"grape": 5, "plum": 1}},
			{"owd": {"orange": 10}},
			{"dm": {"orange": 5}},
		]
		self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main()
