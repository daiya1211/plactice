class DateTimeDisplay:
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def show_date(self):
        print(f"今日の日付は{self.year}年{self.month}月{self.day}日です。")

    def show_time(self):
        print(f"現在の時刻は{self.hour}時{self.minute}分{self.second}秒です。")
dt = DateTimeDisplay(2021, 1, 1, 14, 10, 14)
dt.show_date()
dt.show_time()
