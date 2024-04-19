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
                    "latitude" : res[3],
                    "longitude" : res[4],
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
                        "latitude" : location[3],
                        "longitude" : location[4]
                    }
                    list.append(dict)
                return list
            else:
                return "No locations in database"
            
            
    def add_location(self, id, name, description, latitude, longitude):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farms VALUES (%s, %s, %s, %s, %s)"""
                cur.execute(sql, (id, name, description, latitude, longitude))

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
    
    def add_farm_info(self, id, adress, phone_nr, rating, website):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farm_Information VALUES (%s, %s, %s, %s, %s)"""
                cur.execute(sql, (id, adress, phone_nr, rating, website))

        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message
