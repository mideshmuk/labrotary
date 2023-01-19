def where(dicts):
    if dicts!=None:
        cond = "WHERE "
        And = " AND "
        count = 0
        for i in dicts:
            if count>0:
                cond = cond + And
                cond = cond + str(i)+"="+ str(dicts[i]) 
            else:
                count = count + str(i)+"="+ str(dicts[i])
            count = count + 1
        return cond
    return ""

def rawQuery(mysql,query,type,fetch="all"):
    if type=="SELECT":
        mycursor = mysql.cursor()
        try:
            mycursor.execute(query)
            if fetch!="all":
                data = dict(zip(mycursor.column_names, mycursor.fetchone()))
            else:
                fields = [field_md[0] for field_md in mycursor.description]
                data = [dict(zip(fields,row)) for row in mycursor.fetchall()]
            mycursor.close()    
            return data
        except Exception as e:
            return e
    if type=="INSERT":
        mycursor = mysql.cursor()
        mycursor.execute(query)
        id = mycursor.lastrowid
        mysql.commit()
        return id
    if type=="UPDATE":
        return mysql.update(query)
    if type=="DELETE":
        pass
    return ""
def q_create(dicts,table):
    column = ""
    value = ""
    for i in dicts:
        column =column+i+","
        value = value+"'"+dicts[i]+"',"
    value = value[:len(value)-1]
    column = column[:len(column)-1]
    return "INSERT INTO "+table+" ("+column+")"+"VALUES ("+value+")"


def create(conn,table,dictionary):
    try:
        column = ""
        value = ""
        for i in dictionary:
            column =column+i+","
            value = value+"'"+str(dictionary[i])+"',"
        value = value[:len(value)-1]
        column = column[:len(column)-1]
        query = "INSERT INTO "+table+"("+column+")"+"VALUES ("+value+")"
        mycursor = conn.cursor()
        mycursor.execute(query)
        id = mycursor.lastrowid
        conn.commit()  
        return True,id
    except Exception as e:
        print(e)
        return False,None

def get(conn,table,array=None,condition=None,fetch="all"):
    try:
        column = ""
        for i in array:
            column = column + str(i)+","
        column = column[:len(column)-1]
        if(condition is None):
            query = "select "+column+" "+"FROM "+table
        else:
            query = "select "+column+" "+"FROM "+table+" "+condition
        mycursor = conn.cursor()
        mycursor.execute(query)
        if fetch!="all":
            data = dict(zip(mycursor.column_names, mycursor.fetchone()))
        else:
            fields = [field_md[0] for field_md in mycursor.description]
            data = [dict(zip(fields,row)) for row in mycursor.fetchall()]
        return data
    except Exception as e:
        print(e)
        return None 
    
def put(conn,table,dicts,condition):
    try:
        q = ""
        for i in dicts:
            q = q +str(i)+"="+"'"+str(dicts[i])+"',"
        q = q[:len(q)-1]
        query = 'UPDATE '+table+' '+'SET'+' '+q+' '+condition
        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()
        return None,True
    except Exception as e:
        return e,False   

def delete(conn,table,array,condition):
    try:
        column = ""
        for i in array:
            column = column + str(i)+","
        column = column[:len(column)-1]
        query = "DELETE FROM "+table+" "+condition
        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()
        return "",True
    except Exception as e:
        return e,False