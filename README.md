# Spent_Time_Adder_for_redmine
Redmineの作業時間が固定の場合にまとめて挿入します。

実行した年月と土日祝日を元にRedmineのAPIを元に反映します。

# Dependency

## 使用言語 

* Python3

## 使用ライブラリ

* datetime
* redminelib
* calendar


# Setup

内閣府が公表している祝祭日のcsvデータをダンロードする

http://www8.cao.go.jp/chosei/shukujitsu/syukujitsu_kyujitsu.csv

syukujitsu_kyujitsu.csvは、japan_holiday.pyと同じ階層に保存しておく


# Usage
実行した年月を元に作業時間を記録します。

2019年4月10日に実行した場合は、2019年4月1日～4月30日までの範囲で実行されます。

Spent_time_Adder.py内で必要な項目は次となる。

* project_id
* hours
* activity_id
* custom_fields

うち「custom_fields」は必要に応じて使用する。
※必要ない場合は、コメントアウト

# Licence
This software is released under the MIT License, see LICENSE.

# Authors
jpsejoe

# References

https://kazusa-pg.com/python-script-holiday/

