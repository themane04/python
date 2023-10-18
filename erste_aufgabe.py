import datetime

now = datetime.datetime.now()
print("Aktuelles Datum und Uhrzeit:", now)

today = datetime.date.today()
print("Aktuelles Datum:", today)

d = datetime.datetime(2023, 10, 18, 15, 00)
print("Manuell festgelegtes Datum und Uhrezeit:", d)

delta = datetime.timedelta(days=5, hours=3)
new_time = now + delta
print("Neues Datum und Uhrzeit:", new_time)