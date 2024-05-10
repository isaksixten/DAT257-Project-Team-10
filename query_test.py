from backend.query_machine import QueryMachine
import unittest

class TestQueryMachine(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestQueryMachine, self).__init__(*args, **kwargs)
        self.query = QueryMachine()

    def testFetchAllLocationType(self):
        res = self.query.fetch_all_locations()
        self.assertIsInstance(res, list)

    def testFetchAllLocationValuesType(self):
        res = self.query.fetch_all_locations()
        for elem in res:
            self.assertIsInstance(elem, dict)

    def testErrorForWrongInsert(self):
        self.assertIn("failed", self.query.add_location("abc", "Location", "cool location", "5", "302", "401", 2, "www.com.com", 104))

if __name__ == "__main__":
    unittest.main()