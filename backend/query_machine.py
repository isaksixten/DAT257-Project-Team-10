import datetime

import psycopg2
from datetime import datetime



class QueryMachine:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            password = "postgres")
        self.conn.autocommit = True

    def createDatabase(self):
        try:
            with self.conn.cursor() as cur:
                tables = open(r"./database/tables.sql")
                inserts = open(r"./database/exampleinserts.sql")
                views = open(r"./database/views.sql")
                cur.execute(tables.read())
                cur.execute(inserts.read())
                cur.execute(views.read())
                tables.close()
                inserts.close()
                views.close()
        except psycopg2.Error as e:
            print("Database is already created")

    def createDatabaseFromScratch(self): #For testing purposes
        with self.conn.cursor() as cur:
            dropschema = open(r"./database/createdb.sql")
            tables = open(r"./database/tables.sql")
            inserts = open(r"./database/exampleinserts.sql")
            views = open(r"./database/views.sql")
            cur.execute(dropschema.read())
            cur.execute(tables.read())
            cur.execute(inserts.read())
            cur.execute(views.read())
            dropschema.close()
            tables.close()
            inserts.close()
            views.close()

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
                      
    def add_location(self, id: str, name: str, description: str, rating: float, latitude: float, longitude: float, address: str, website: str, phonenumber: str):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farms VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"""
                cur.execute(sql, (id, name, description,rating, latitude, longitude, address, website, phonenumber))
        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message
    
    def add_tag(self, tag):
        try:
            with self.conn.cursor() as cur:
                sql = """ INSERT INTO Tags VALUES (%s)"""
                cur.execute(sql, (tag,))
        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message

    def delete_tag(self, tag):
        try:
            with self.conn.cursor() as cur:
                sql = """ DElETE FROM Tags WHERE tag = (%s)"""
                cur.execute(sql, (tag,))
        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message

    def delete_farm_tag(self, farm, tag):
        try:
            with self.conn.cursor() as cur:
                sql = """ DElETE FROM Farm_Tags WHERE (farm = (%s) AND tag = (%s)) """
                cur.execute(sql, (farm, tag))
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

    def fetch_farms_tag(self, id):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Farm_Tags WHERE farm = %s"""
            cur.execute(sql, (id,))
            res = cur.fetchall()
            a_list = []
            if res:
                for i in res:
                    a_list.append((i[0], i[1]))
                return a_list
            else:
                return []
            # its a nice function
    
    def fetch_continous_farmtags(self, tags):
        params = (tuple(tags), len(tags))
        with self.conn.cursor() as cur:
            sql = """ SELECT Farms.id
                        FROM Farms
                        JOIN Farm_Tags ON Farms.id = Farm_Tags.farm
                        WHERE Farm_Tags.tag IN %s
                        GROUP BY Farms.id, Farms.name, Farms.address
                        HAVING COUNT(DISTINCT Farm_Tags.tag) = %s;"""
            cur.execute(sql, params)
            res = cur.fetchall()
            list = []
            if res:
                for farm in res:
                    list.append(self.fetch_location(farm))
                return list
            else:
                return []

    def update_open_now(self, farmid):
        # fix with weekday
        current_time = datetime.now().strftime("%H:%M")
        weekday = datetime.today().weekday() + 1
        with self.conn.cursor() as cur:
            sql = """ SELECT farm_id, open_time, close_time FROM Opening_Hours WHERE Opening_hours.farm_id = %s AND weekday = %s"""
            cur.execute(sql, (farmid, weekday))
            res = cur.fetchall()
            for i in res:
                if i[1] > current_time or current_time > i[2]:
                    #with self.conn.cursor() as cur2:
                        sql = """ DELETE FROM Farm_tags WHERE farm_tags.farm = %s AND tag = 'Open now' """
                        cur.execute(sql, (i[0],))
                else:
                    #with self.conn.cursor() as cur2:
                        sql = """ INSERT INTO Farm_tags VALUES (%s,  'Open now') """
                        cur.execute(sql, (i[0],))

            
    def fetch_by_search(self, term): # Can search for both name and address. Only returns name and adress to search bar as of now....
        with self.conn.cursor() as cur:
            sql = """SELECT id,name, address FROM Farms WHERE Farms.name ILIKE %s OR Farms.address ILIKE %s"""
            cur.execute(sql, (term + '%', term + '%'))
            res = cur.fetchall()
            list = []
            if res:
                for location in res:
                    list.append(location)
                return list
            else:
                return []

    def fetch_opening_hours(self, id): # Fetches location opening hours based on id and returns them in the form of a dictionary.
        with self.conn.cursor() as cur:
            sql = """SELECT * FROM Opening_Hours WHERE Opening_Hours.farm_id = %s"""
            cur.execute(sql, (id,))
            res = cur.fetchall()
            dict = {}
            innerdict = {}
            if res:
                for location in res:
                    innerdict[location[1]] = [location[2], location[3]]
                    dict[location[0]] = innerdict
        return dict # Bör returnera en dict med key som är farm ID och value som är en lista av [Weekday, opening_time, closing_time].
    
    def fetch_all_opening_hours(self): # Fetches all opening_hours for all locations in the database.
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Opening_Hours """
            cur.execute(sql)
            res = cur.fetchall()
            dict = {}
            innerdict = {}
            if res:
                for location in res:
                    innerdict[location[1]] = [location[2], location[3]]
                    dict[location[0]] = innerdict
        return dict
