import psycopg2
import datetime
import pickle

con = psycopg2.connect(user="datamaskuser",
                                  password="datamaskuser123",
                                  host="35.245.71.89",
                                  port="5432",
                                  dbname="datamask")



cur = con.cursor()


servicedetails = []


cur.execute("SELECT * FROM services WHERE status = %s",('active',))
services = cur.fetchall()

for service in services:
    sid = service[0]

    cur.execute("SELECT * FROM servicedetails WHERE sid = %s",(sid,))
    s = cur.fetchall()
    urls = []
    for i in s:
        urls.append(i[2])
        #print(urls)

    cur.execute("SELECT * FROM fsets WHERE fsetid = %s",(sid,))
    fsets = cur.fetchall()
    fids = [j for i,j,_ in fsets]
    print(fids)

    fdetails = []

    for fid in fids:
            cur.execute("SELECT * FROM filters WHERE fid = %s",(fid,))
            f = cur.fetchall()[0]
            #print(f)
            #fdetails.append([f[4].replace("\\",""),f[5],f[6]])
            fdetails.append([f[4],f[5],f[6],f[7]])
            print(fdetails)
            print(f[7],type(f[7]))

