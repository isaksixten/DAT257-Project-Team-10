
import psycopg2

class QueryMachine:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "postgres")
        self.conn.autocommit = True

    def fetch_location(self, id):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Farms WHERE Farms.id = %s"""
            cur.execute(sql, (id,))
            res = cur.fetchone()
            if res:
                dict = {
                    "id" : res[0],
                    "name" : res[1],
                    "description" : res[2],
                    "rating" : res[3],
                    "latitude" : res[4],
                    "longitude" : res[5],
                    "address" : res[6],
                    "website" : res[7],
                    "phonenumber" : res[8],
                }
                return dict
            else:
                return "Location does not exist"

    def fetch_all_locations(self):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Farms"""
            cur.execute(sql)
            res = cur.fetchall()
            list = []
            if res:
                for location in res:
                    dict = {
                    "id" : location[0],
                    "name" : location[1],
                    "description" : location[2],
                    "rating" : location[3],
                    "latitude" : location[4],
                    "longitude" : location[5],
                    "address" : location[6],
                    "website" : location[7],
                    "phonenumber" : location[8],
                    }
                    list.append(dict)
                return list
            else:
                return "No locations in database"
                      
    def add_location(self, id, name, description, rating, latitude, longitude,address, website, phonenumber):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farms VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"""
                cur.execute(sql, (id, name, description,rating, latitude, longitude, address,website,phonenumber))
        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message
    
    def add_farmtag(self, id, tag):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farm_Tags VALUES (%s, %s)"""
                cur.execute(sql, (id, tag))

        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message

    def add_opening_hours(self, farm_id: str, weekday: int, open_time: str, close_time: str):
        try:
            with self.conn.cursor() as cur:
                a = list(open_time)
                b = list(close_time)
                open = a[0] + a[1] + ":" + a[2] + a[3]
                close = b[0] + b[1] + ":" + b[2] + b[3]
                sql = """INSERT INTO Opening_hours VALUES (%s, %s, %s, %s)"""
                cur.execute(sql, (farm_id, weekday, open, close))
        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message


    def fetch_tags(self):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Tags"""
            cur.execute(sql)
            res = cur.fetchall()
            list = []
            if res:
                for location in res:
                    list.append(location[0])
                return list
            else:
                return "No locations in database"   

    def fetch_farmtags(self):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Farm_Tags"""
            cur.execute(sql)
            res = cur.fetchall()
            print("res:" + str(res))
            list = []
            if res:
                for farm in res:
                    list.append(farm)
                return list
            else:
                return []     
    
    def fetch_continous_farmtags(self, tags):
        params = (tuple(tags), len(tags))
        with self.conn.cursor() as cur:
            sql = """ SELECT Farms.id, Farms.name, Farms.address
                        FROM Farms
                        JOIN Farm_Tags ON Farms.id = Farm_Tags.farm
                        WHERE Farm_Tags.tag IN %s
                        GROUP BY Farms.id, Farms.name, Farms.address
                        HAVING COUNT(DISTINCT Farm_Tags.tag) = %s;"""
            cur.execute(sql, params)
            res = cur.fetchall()
            print("res:", res)
            list = []
            if res:
                for farm in res:
                    list.append(farm)
                return list
            else:
                return []   
            
    def fetch_by_search(self, term): # Can search for both name and address. Only returns name and adress to search bar as of now....
        with self.conn.cursor() as cur:
            sql = """SELECT id,name, address FROM Farms WHERE Farms.name ILIKE %s OR Farms.address ILIKE %s"""
            cur.execute(sql, (term + '%', term + '%'))
            res = cur.fetchall()
            list = []
            if res:
                for location in res:
                    list.append(location)
                list.sort()
                return list
            else:
                return []
    
    def reset_database(self):
        with self.conn.cursor() as cur:
            sql = """DELETE FROM Farms"""
            cur.execute(sql)
            

    def fetch_opening_hours(self, id): # Fetches location opening hours based on id and returns them in the form of a dictionary.
        with self.conn.cursor() as cur:
            sql = """SELECT * FROM Opening_Hours WHERE Opening_Hours.farm_id = %s"""
            cur.execute(sql, (id))
            res = cur.fetchall()
            dict = {}
            if res:
                for location in res:
                    dict[location[0]] = [location[1], location[2], location[3]]
                return dict # Bör returnera en dict med key som är farm ID och value som är en lista av [Weekday, opening_time, closing_time].
            else:
                return "No location with that ID"
