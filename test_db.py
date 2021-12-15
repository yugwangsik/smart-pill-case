import pymysql
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(2, gp.IN)
gp.setup(27, gp.IN)
gp.setup(22, gp.IN)
gp.setup(23, gp.OUT)
gp.setup(24, gp.OUT)
gp.setup(25, gp.OUT)


yu_db = pymysql.connect(
        host='211.117.3.146',
        user='yu',
        passwd='1234',
        db='SmartPillCase',
        port=10002,
        charset='utf8'
)
i = 0
m = 0
l = 0
e = 0

cursor = yu_db.cursor()
try:
    while(1):
        val_M = gp.input(2)
        val_L = gp.input(27)
        val_E = gp.input(22)

        if(val_M == 0):
            #print(val)
            query = "UPDATE Pill set val = 0 where id = 1"
            cursor.execute(query)
            yu_db.commit()
            m = 0
        else:
            #print(val)
            if(m > 20):
                query = "UPDATE Pill set val = 1 where id = 1"
                cursor.execute(query)
                yu_db.commit()
                m = 0
            m += 1
            print(m)

        if(val_L == 0):
            query = "UPDATE Pill set val = 0 where id = 2"
            cursor.execute(query)
            yu_db.commit()
            l = 0
        else:
            if(l > 20):
                query = "UPDATE Pill set val = 1 where id = 2"
                cursor.execute(query)
                yu_db.commit()
                l = 0
            l += 1
            print(l)

        if(val_E == 0):
            query = "UPDATE Pill set val = 0 where id = 3"
            cursor.execute(query)
            yu_db.commit() 
            e = 0
        else:
            if(e > 20):
                query = "UPDATE Pill set val = 1 where id = 3"
                cursor.execute(query)
                yu_db.commit()
                e = 0
            e += 1
            print(e)
            

        query = "select L_val from LED"
        cursor.execute(query)
        LED = cursor.fetchone()
        #LED = int(LED[0])
        if(LED[0] == 1):
            gp.output(23, gp.HIGH)
            gp.output(24, gp.HIGH)
            gp.output(25, gp.HIGH)
            i += 1
        else:
            gp.output(23, gp.LOW)
            gp.output(24, gp.LOW)
            gp.output(25, gp.LOW)

        if(i == 5):
            query = "UPDATE LED set L_val = 0 where id = 1"
            cursor.execute(query)
            i = 0
            yu_db.commit()
        
        yu_db.commit()
        #print(LED[0])

        time.sleep(1)

finally:
    gp.output(23, gp.LOW)
    gp.output(24, gp.LOW)
    gp.output(25, gp.LOW)
    gp.cleanup()
    yu_db.close()
