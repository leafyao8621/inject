import sqlite3
import random

if __name__ == "__main__":
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS TEST")
        cur.execute("CREATE TABLE IF NOT EXISTS TEST (ID CHAR(10) PRIMARY KEY, VAL int)");
        for i in range(100000):
            query =\
                f'''
                INSERT INTO TEST VALUES (
                '{"".join(chr(random.randint(65, 65 + 25)) for i in range(10))}',
                {random.randint(0, 0xffffffff)})
                '''
            cur.execute(query)
        cur.close()
        conn.commit()
