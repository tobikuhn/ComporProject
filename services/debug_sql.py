from datetime import datetime

def debug_sql(sql):
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    with open('/var/www/drupal/log.txt','a') as f:
        f.write(date_time)
        f.write(" ")
        f.write(sql)
        f.write("\n")
