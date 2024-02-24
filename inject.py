import sqlite3

if __name__ == "__main__":
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        while (True):
            try:
                cur_id = input("> ")
                cur.execute(
                    f"SELECT * FROM TEST WHERE ID = '{cur_id}'"
                )
                for i in cur:
                    print(f"{i[0]} | {i[1]:20d}")
                new_val = input("New Value:\n> ")
                if (len(new_val) == 0):
                    continue
                cur.executescript(
                    f"UPDATE TEST SET VAL = {new_val} WHERE ID = '{cur_id}'"
                )
                conn.commit()
            except:
                break
