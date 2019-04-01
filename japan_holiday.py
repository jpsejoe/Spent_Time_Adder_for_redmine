import csv
from datetime import datetime
 
 
class JapanHoliday:
    def __init__(self, path='syukujitsu_kyujitsu.csv', encoding='cp932'):
        self._holidays = self._read_holiday(path, encoding)
 
    def _read_holiday(self, path, encoding):
        holidays = {}
        with open(path, encoding=encoding, newline='') as f:
            reader = csv.reader(f)
            next(reader)  # CSVのヘッダーを飛ばす
            for row in reader:
                day, name = row[0], row[1]
                holidays[day] = {'day': day, 'name': name}
        return holidays
 
    def is_holiday(self, day_str):
        try:
            day = datetime.strptime(day_str, '%Y/%m/%d')
            if day.weekday() >= 5:
                return True
        except ValueError:
            print('日付は2018/03/01 %Y/%m/%dの形式で入力してください')
            raise ValueError
        if day_str in self._holidays:
            return True
        return False
    
    def get_holiday_dict(self):
        return self._holidays
