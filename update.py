import datetime

dt_now = datetime.datetime.now()
last_update = dt_now.strftime('%Y-%m-%d %H:%M:%S')

f = open("./www/scripts/update_datetime.js", mode="w")
f.write('last_update = "' + last_update +'";')
f.close()