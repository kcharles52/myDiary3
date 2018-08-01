from db import DatabaseConnection
conn = DatabaseConnection()
class DiaryEntry:
    def __init__(self, diaryTitle, date, diaryEntryBody, user_id):
        self.diaryTitle = diaryTitle
        self.diaryEntryBody = diaryEntryBody
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return repr(self.__dict__)

    def create_entry(self):
        conn.cursor.execute("""INSERT INTO entries(diaryTitle,diaryBody,diaryDate,user_id) VALUES (%s,%s,%s,%s) """,
                            (self.diaryTitle, self.diaryEntryBody, self.date, self.user_id))
        conn.connection.close()
