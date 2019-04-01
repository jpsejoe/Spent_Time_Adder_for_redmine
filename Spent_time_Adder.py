# -*- coding: utf-8 -*-
import datetime
from redminelib import Redmine
import calendar
from japan_holiday import JapanHoliday

now = datetime.datetime.now()
holiday = JapanHoliday()

redmine = Redmine('[redimeのurl]', key='[redimeのAPIキー]')

now = datetime.datetime.now()
_, lastday = calendar.monthrange(now.year,now.month)

for i in range(1,lastday+1):
    days =  holiday.is_holiday(str(now.year) + '/' + str(now.month) + '/' + str(i))
    if days :  
        time_entry = redmine.time_entry.new()
        time_entry.project_id = [プロジェクトID]
        time_entry.spent_on = datetime.date(now.year, now.month, i)
        time_entry.hours = [作業時間]
        time_entry.activity_id = [アクティビティID]
        time_entry.comments = '休日'
        time_entry.custom_fields = [{'id': 2, 'value': '[カスタムフィールドの値]'}]
        time_entry.save()
        print(str(time_entry.spent_on) + '完了')
    else:
        time_entry = redmine.time_entry.new()
        time_entry.project_id = [プロジェクトID]
        time_entry.spent_on = datetime.date(now.year, now.month, i)
        time_entry.hours = [作業時間]
        time_entry.activity_id = [アクティビティID]
        time_entry.comments = '[作業コメント]'
        time_entry.custom_fields = [{'id': 1, 'value': '[カスタムフィールドの値]'}]
        time_entry.save()
        print(str(time_entry.spent_on)+ '完了')

