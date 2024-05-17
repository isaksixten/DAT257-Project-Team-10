from backend.query_machine import QueryMachine
import unittest


class TestQueryMachine(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestQueryMachine, self).__init__(*args, **kwargs)
        self.query = QueryMachine()

    def setUp(self):
        self.query.createDatabaseFromScratch()

    def testFetchAllLocationType(self):
        self.query.add_location('abc', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        res = self.query.fetch_all_locations()
        self.assertIsInstance(res, list)

    def testFetchAllLocationValuesType(self):
        self.query.add_location('acd', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_location('bac', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        res = self.query.fetch_all_locations()
        for elem in res:
            self.assertIsInstance(elem, dict)

    def testErrorForWrongInsert(self):
        self.assertRaises(TypeError, self.query.add_location("cab", "Location", "cool location", "5", "302", "401", 2, "www.com.com", 104))

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

    def testAddTagToFarm(self):
        self.query.add_location('a', 'b', 'c', 5, 10, 11, 'd', 'e', 0)
        a = self.query.fetch_farms_tag('a')
        self.query.add_tag('Open now')
        self.query.add_farmtag('a', 'Open now')
        b = self.query.fetch_farms_tag('a')
        self.assertNotEqual(a, b)
        self.query.delete_farm_tag('a', 'Open now')

    def testUpdateOpenNowDelete(self):
        self.query.add_location('bdc', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_opening_hours('bdc', 1, '0200', '0400')
        self.query.add_opening_hours('bdc', 2, '0200', '0400')
        self.query.add_opening_hours('bdc', 3, '0200', '0400')
        self.query.add_opening_hours('bdc', 4, '0200', '0400')
        self.query.add_opening_hours('bdc', 5, '0200', '0400')
        self.query.add_opening_hours('bdc', 6, '0200', '0400')
        self.query.add_opening_hours('bdc', 7, '0200', '0400')
        self.query.add_farmtag('bdc', 'Open now')
        a = self.query.fetch_farms_tag('bdc')
        self.query.update_open_now('bdc')
        b = self.query.fetch_farms_tag('bdc')
        self.assertNotEqual(a, b)
        

    def testUpdateOpenNowInsert(self):
        self.query.add_location('bcd', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_opening_hours('bcd', 1, '0000', '2400')
        self.query.add_opening_hours('bcd', 2, '0000', '2400')
        self.query.add_opening_hours('bcd', 3, '0000', '2400')
        self.query.add_opening_hours('bcd', 4, '0000', '2400')
        self.query.add_opening_hours('bcd', 5, '0000', '2400')
        self.query.add_opening_hours('bcd', 6, '0000', '2400')
        self.query.add_opening_hours('bcd', 7, '0000', '2400')
        a = self.query.fetch_farms_tag('bcd')
        self.query.update_open_now('bcd') 
        b = self.query.fetch_farms_tag('bcd')
        self.assertNotEqual(a, b)

    def testFetchBySearch(self):
        self.query.add_location('abc', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_location('acb', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_location('adc', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        res = self.query.fetch_by_search('Be')
        self.assertEqual(3, len(res))

    def testFetchOpeningHours(self):
        self.query.add_location('abc', 'Bertils slakt och grönt', 'Bästa slaktaren i staden',5, -37.33056, 48.64247,'FakeStreet 1','fake1.se','+123')
        self.query.add_opening_hours('abc', 1, "1000", "1500")
        a = self.query.fetch_opening_hours('abc')
        self.assertEqual('10:00', a['abc'][1][0])

if __name__ == "__main__":
    unittest.main()