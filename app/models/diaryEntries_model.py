class DiaryEntry:
    def __init__(self, diaryTitle, date, diaryEntryBody, user_id):
        self.diaryTitle = diaryTitle
        self.diaryEntryBody = diaryEntryBody
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return repr(self.__dict__)
