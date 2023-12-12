from config import CONN, CURSOR

class Song:
    def __init__(self,name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
             CREATE TABLE IF NOT EXISTS songs(
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 album TEXT
             )
        """
        CURSOR.execute(sql)
        CONN.commit()

        table_info = CURSOR.execute("PRAGMA table_info(songs)").fetchall()
        if table_info:
            print("Table 'songs' created successfully.")
            print("Table Information:")
            for column in table_info:
                print(column)
        else:
                print("Error occurred")

    def save(self):
         sql = """
              INSERT INTO songs(name,album)
              VALUES(?,?)
         """
         CURSOR.execute(sql,(self.name, self.album))
         self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
         CONN.commit()

    @classmethod
    def create(cls,name, album):
         song = Song(name,album)
         song.save()
         return song
Song.create_table()
