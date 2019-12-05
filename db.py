import sqlite3
con = sqlite3.connect("hospital.db")
def database():
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS HOSPITAL(HOSPITAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,HOSPITAL_NAME VARCHAR,BED_COUNT INTEGER)")
    cur.execute('''CREATE TABLE IF NOT EXISTS DOCTOR(DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,DOCTOR_NAME TEXT, HOSPITAL_ID INTEGER
                    REFERENCES HOSPITAL(HOSPITAL_ID),
                    JOINING_DATE DATE,SPECIALITY TEXT,SALARY INTEGER,EXPERIENCE INTEGER)''')
    print("database created successfully...")
database()