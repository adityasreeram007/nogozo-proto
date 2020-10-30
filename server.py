from flask import Flask
from flask import render_template,request,redirect,url_for,make_response
import sqlite3 as sql
app=Flask(__name__)
app.secret_key="wearelegends"

@app.route('/')
def mainpage():
    if (request.cookies.get('username')!='None'):
        conn=sql.connect('Database.db')
        q='select area from locinfo where email=?'
        param=(request.cookies.get('username'),)
        c=conn.execute(q,param)
        print(c)
        res=c.fetchall()
        area=res[0][0]
        return render_template('landingpage.html',email=request.cookies.get('username').split('@')[0],area=area)
    else:

        return render_template('mainpage.html')

@app.route('/login',methods=["POST"])
def login():
    if request.method=="POST":
        conn=sql.connect('Database.db')
        email=request.form['email']
        password=request.form['password']
        q='select password from userdata where email=?'
        param=(email,)
        c=conn.execute(q,param)
        print(c)
        res=c.fetchall()
        passer=res[0][0]
        if passer==password:
            resp = make_response(redirect(url_for('mainpage')))
            resp.set_cookie('username',email )
            return resp
        else:
            return render_template('mainpage.html',msg='Username or Password Wrong!')
@app.route('/signup')
def singup():
    return render_template('signup.html')
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=="POST":
        conn=sql.connect('Database.db')
        email=request.form['email']
        password=request.form['pass']
        phone=request.form['phone']
        q='insert into userdata (email,password,Phone) values(?,?,?)'
        param=(str(email),str(password),str(phone),)
        try:
            cur=conn.execute(q,param)
            print(cur)
            conn.commit()
        except:
            return render_template('mainpage.html',msg='Cannot SignUp! Wrong iNputs Or User aLready Exist')
        return render_template('locinfo.html')
@app.route('/saveloc',methods=['POST','GET'])
def saveloc():
    if request.method=="POST":
        conn=sql.connect('Database.db')
        email=request.form['email']
        line1=request.form['line1']
        line2=request.form['line2']
        dis=request.form['dis']
        area=request.form['area']
        pin=request.form['pin']
        
        
        q='insert into locinfo (email,line1,line2,district,pincode,area) values(?,?,?,?,?,?)'
        param=(str(email),str(line1),str(line2),str(dis),str(pin),str(area),)
        try:
            cur=conn.execute(q,param)
            print(cur)
            conn.commit()
            
        except:
            
            return redirect(url_for('mainpage'))

        resp = make_response(redirect(url_for('mainpage')))
        resp.set_cookie('username',email )
        return resp
@app.route('/locinfo')
def locinfo():
    return render_template('locinfo.html')

@app.route('/landing')
def landing():
    return render_template('landingpage.html')

@app.route('/logout',methods=['POST'])
def logout():
    resp = make_response(redirect(url_for('mainpage')))
    resp.set_cookie('username','None' )
    return resp
if __name__=='__main__':
    app.run(debug=True)