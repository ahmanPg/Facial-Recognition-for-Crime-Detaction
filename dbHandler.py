import datetime
from datetime import datetime
import pymysql.cursors
from datetime import date

today = date.today()


def insertData(data):
    rowId = 0
    db = pymysql.connect(host='localhost', port=3306, user='root', database="criminalsDB")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    print("database connected")

    query = "INSERT INTO criminal_data VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"],
             data["Marital Status"], data["Blood Group"], data["Roaming"], data["MarkID"],
             data["Nationality"], data["Religion"], data["Crime Done"], today, today)
    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except pymysql.Error as e:
        db.rollback()
        print(f"why? {e}")

    db.close()
    print("connection closed")
    return rowId


def updateData(id, data):
    rowId = 0
    db = pymysql.connect(host='localhost', port=3306, user='root', database="criminalsDB")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    print("database connected")
    roam = 1 if (data["Roaming"] == "true") else 0
    year = "19"+data["DOB(yyyy-mm-dd)"][:2]+"/12/14 00:00:00"
    try:
        dob = datetime.strptime(year, '%y/%m/%d %H:%M:%S')
    except ValueError:
        dob = datetime.strptime('19/12/14 00:00:00', '%y/%m/%d %H:%M:%S')
    print(dob)
    query = "UPDATE criminal_data SET name='%s', fathersName='%s', mothersName='%s', gender='%s',DOB='%s', " \
            "maritalStatus='%s', bloodType='%s', roaming='%s', idMark='%s', nationality='%s', religion='%s', " \
            "crimeDone='%s' WHERE id=%s;" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             dob, data["Marital Status"], data["Blood Group"], roam, data["MarkID"],
             data["Nationality"], data["Religion"], data["Crime Done"], id)
    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data updated on row %d" % rowId)
    except pymysql.Error as e:
        db.rollback()
        print(e)

    db.close()
    print("connection closed")
    return rowId


def retrieveData(name):
    crim_id = None
    crim_data = None
    db = pymysql.connect(host='localhost', port=3306, user='root', database="criminalsDB")
    cursor = db.cursor(pymysql.cursors.DictCursor)
    print("database connected")

    query = "SELECT * FROM criminal_data WHERE Name='%s'" % name

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        crim_id = result["id"]
        years = str(today.year - result["DOB"].year) + " years"
        last_seen = str(today)
        roam = "true" if (result["roaming"] == 1) else "false"
        crim_data = {
            "Name": result["name"],
            "Father's Name": result["fathersName"],
            "Mother's Name": result["mothersName"],
            "Gender": result["gender"],
            "DOB(yyyy-mm-dd)": years,
            "Marital Status": result["maritalStatus"],
            "Blood Group": result["bloodType"],
            "Roaming": roam,
            "MarkID": result["idMark"],
            "Nationality": result["nationality"],
            "Religion": result["religion"],
            "Crime Done": result["crimeDone"],
            "Last Seen": last_seen
        }

        print("data retrieved")
    except pymysql.Error as e:
        print(f"Failed loading data: {e}")

    db.close()
    print("connection closed")

    return crim_id, crim_data


if __name__ == "__main__":
    pass
