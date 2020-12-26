from flask import Flask,render_template,redirect,request
import joblib


#__name__==__main__
app = Flask(__name__)

model1 = joblib.load("knn_cv1.pkl")
model2 = joblib.load("knn_cv.pkl")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def fun():
    if request.method=='POST':
        flag,fraud,paymentmode,diff = False,0,0,0
        try:
            bill=float(request.form['Total Bill Amount'])
            reimbursement=float(request.form['Total Reimbursement Amount'])
            inclaimnum=float(request.form['Inpatient Claim Number'])
            outclaimnum=float(request.form['Outpatient Claim Number'])
            inclaimamt=float(request.form['Inpatient Claim Amount'])
            outclaimamt=float(request.form['Outpatient Claim Amount'])

            temp=[inclaimnum,outclaimnum,inclaimamt,outclaimamt]

            diff=str(bill-reimbursement)
            fraud = str(model1.predict([temp])[0][0])
            paymentmode = str(model2.predict([temp])[0][0])
        except:
            flag = True
    
    return render_template("index.html", fraud=fraud, paymentmode=paymentmode, flag=flag, diff=diff)

if __name__ == "__main__":
    #app.debug = True
    app.run(debug = True)