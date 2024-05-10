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

    def testAddLocation(self):
        self.query.add_location('a', 'b', 'c', 5, 10, 11, 'd', 'e', 0)
        res = self.query.fetch_location('a')
        dict = {
            "id" : 'a',
            "name" : 'b',
            "description" : 'c',
            "rating" : 5,
            "latitude" : 10.0,
            "longitude" : 11.0,
            "address" : 'd',
            "website" : 'e',
            "phonenumber" : '0',
        }
        self.assertEqual(res, dict)

    def testDeleteTag(self):
        a = self.query.fetch_tags()
        self.query.add_tag('ö')
        self.query.delete_tag('ö')
        b = self.query.fetch_tags()
        self.assertEqual(a, b)

    def testAddTag(self):
        a = self.query.fetch_tags()
        self.query.add_tag('ö')
        b = self.query.fetch_tags()
        self.assertNotEqual(a, b)
        self.query.delete_tag('ö')

    def testAddTagToFarm(self):
        a = self.query.fetch_farms_tag('a')
        self.query.add_farmtag('a', 'open_now')
        b = self.query.fetch_farms_tag('a')
        self.assertNotEqual(a, b)
        self.query.delete_farm_tag('a', 'open_now')


if __name__ == "__main__":
    unittest.main()