import unittest
import sum_min_max
import math

class TestSum(unittest.TestCase):
	def test_positives(self):
		test_data = [
			[[1,2,3,4,5,6,7,8,9,10], 11],
			[[1], 2],
			[[1, 1], 2],
			[[0, 0,0,0,0,1], 1],
			[[1000, 100, 50, 20, 0], 1000]
		]
		for t in test_data:
			#print("Check {} and {}".format(t[0], t[1]))
			self.assertEqual(sum_min_max.sum_min_max(t[0]), t[1])

	def test_negatives(self):
		test_data = [
			[[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10], -11],
			[[-1], -2],
			[[-1, -1], -2],
			[[0, 0, 0, 0, 0,-1], -1],
			[[-1000, -100, -50, -20, 0], -1000]
		]
		for t in test_data:
			#print("Check {} and {}".format(t[0], t[1]))
			self.assertEqual(sum_min_max.sum_min_max(t[0]), t[1])

	def test_extreme(self):
		test_data = [
			[[1,-2, 3,-4, 5, -6, 7, -8, 9, -10], -1], # mixed
			[[], math.nan], # empty array
			[["hello", "world"], math.nan],
			[[0, 0, 0, 0, 0, 0], 0],
			[["-1000", -100, -50, 20, 0], -80]
		]
		for t in test_data:
			print("Check {} and {}".format(t[0], t[1]))
			if math.isnan(t[1]):
				self.assertEqual(math.isnan(sum_min_max.sum_min_max(t[0])), math.isnan(t[1]))
			else:
				self.assertEqual(sum_min_max.sum_min_max(t[0]), t[1])

if __name__ == '__main__':
	unittest.main()
