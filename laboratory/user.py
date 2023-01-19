import functools
from flask import (Blueprint, request,jsonify)
from mysql import connector
import re



mydb = connector.connect(user='root', password= '', database='lab', host='localhost')
    
userBlueprint = Blueprint('user',__name__,url_prefix='/api/v1') 

@userBlueprint.route('/registerPatient',methods = ['POST'])
def registerPatient():
    data=request.get_json()
    
    d = {}
    
    if type(data.get('designation'))!= str:
        d['designation'] = "Invalid designation"
    if type(data.get('full_name'))!= str:
        d['full_name'] = "Invalid Name"    
    if type(data.get('gender'))!= str:
        d['gender'] = "Invalid Gender"
    if type(data.get('mobile'))!= int:
        d['mobile'] = "Invalid Mobile Number"
    pattern_mobile = re.compile("^[0-9]{10}$")
    if pattern_mobile.match(str(data.get('mobile'))):
        print("")
    else:
        d['mobile'] = "Invalid Mobile Number"
    if type(data.get('gmail'))!= str:
        d['gmail'] = "Invalid Email Id"
    pattern_gmail = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    if pattern_gmail.match(data.get('gmail')):
        print("")
    else:
        d['gmail'] = "Invalid Email Id"
    if type(data.get('state'))!= str:
        d['state'] = "Invalid State"
    if type(data.get('district'))!= str:
        d['district'] = "Invalid District"
    if type(data.get('taluka'))!= str:
        d['taluka'] = "Invalid Taluka"
    if type(data.get('city'))!= str: 
        d['city'] = "Invalid City"
    if type(data.get('pincode'))!= int: 
        d['pincode'] = "Invalid Pincode"
    pattern_pincode = re.compile("^[0-9]{6}$")
    if pattern_pincode.match(str(data.get('pincode'))):
        print("")
    else:
        d['pincode'] = "Invalid Pincode"
            
    if data.get('designation') == None:
        d['designation'] = "Invalid designation"
    if data.get('full_name') == None:
        d['full_name'] = "Invalid Name"
    if data.get('gender') == None:
        d['gender'] = "Invalid Gender"
    if data.get('mobile') == None:
        d['mobile'] = "Invalid Mobile"
    if data.get('gmail') == None:
        d['gmail'] = "Invalid Gmail"
    if data.get('state') == None:
        d['state'] = "Invalid State"
    if data.get('district') == None:
        d['district'] = "Invalid District"
    if data.get('taluka') == None:
        d['taluka'] = "Invalid Taluka"
    if data.get('city') == None:
        d['city'] = "Invalid City"
    if data.get('pincode') == None:
        d['pincode'] = "Invalid Pincode"
    if d == {}:
        return jsonify(data ="Patient Registration Successful", status = 200)
    return(d)
    

    

@userBlueprint.route('/show',methods=['GET','POST'])
def user():
    con = mydb.cursor(dictionary=True)
    con.execute("select * from patient, patient_geos, patient_address")
    r = con.fetchall()
    print("json: {json.dumps(r)}")
    return jsonify(data =r)

@userBlueprint.route('/insert', methods = ['POST'])
def addUser():
    data = request.get_json()
    con = mydb.cursor()
    sql1 = "INSERT INTO patient (designation,full_name,gender,mobile,gmail) VALUES (%s, %s,%s, %s,%s)"
    val1 =  (data.get('designation'),data.get('full_name'),data.get('gender'),data.get('mobile'),data.get('gmail'))
    sql2 = "INSERT INTO patient_geos (state,district,taluka,city,pincode) VALUES (%s, %s,%s, %s,%s)"
    val2 =  (data.get('state'),data.get('district'),data.get('taluka'),data.get('city'),data.get('pincode'))
    # sql3 = "INSERT INTO patient_address(id_pat,id_geos) VALUES (%s,%s)"
    # val3 = (data.get('id_pat'),data.get('id_geos'))
    con.execute(sql1,val1)
    con.execute(sql2,val2)

    # con.execute(sql3,val3)
    mydb.commit()
    return jsonify(data = "Registration is Completed")

@userBlueprint.route('/update', methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        data = request.get_json()
        cur = mydb.cursor()
        sql1 = ("""
        UPDATE patient
        SET designation = %s,full_name = %s,gender = %s,mobile = %s, gmail = %s
        where id_pat = %s
        """)
        val1 = (data.get('designation'),data.get('full_name'),data.get('gender'),data.get('mobile'),data.get('gmail'),data.get('id_pat'))
        
        sql2 = ("""
        UPDATE patient_geos
        SET state = %s,district = %s,taluka = %s,city = %s, pincode = %s
        where id_geos = %s
        """)
        val2 = (data.get('state'),data.get('district'),data.get('taluka'),data.get('city'),data.get('pincode'),data.get('id_geos'))
        cur.execute(sql1,val1)
        cur.execute(sql2,val2)
        mydb.commit()
        print(data)
        return jsonify(data = "Update success")

@userBlueprint.route('/delete', methods = ['POST','GET'])
def delete():
    curr = mydb.cursor()
    if request.method == 'POST':
        data = request.get_json()
        sql1 = curr.execute("delete from patient where id_pat={}".format(data.get('id_pat')))
        sql2 = curr.execute("delete from patient_geos where id_geos={}".format(data.get('id_geos')))
        sql1
        sql2
        mydb.commit()
        return jsonify(data = "Success")
