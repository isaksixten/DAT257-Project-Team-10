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
            
    def add_location(self, id, name, description, latitude, longitude):
        try:
            with self.conn.cursor() as cur:
                sql = """INSERT INTO Farms VALUES (%s, %s, %s, %s, %s)"""
                cur.execute(sql, (id, name, description, latitude, longitude))

        except psycopg2.Error as e:
            message = repr(e)
            return "failed: " + message