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
                return res
            else:
                return "Location does not exist"
            
    def fetch_all_locations(self):
        with self.conn.cursor() as cur:
            sql = """ SELECT * FROM Farms WHERE Farms.id"""
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                for location in res:
                    dict = {
                        "id" : location[0],
                        "name" : location[1],
                        "description" : location[2],
                        "latitude" : location[3],
                        "longitude" : location[4]
                    }
                return dict
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