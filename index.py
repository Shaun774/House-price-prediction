import numpy as np
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,request

app = Flask(__name__)

x = np.array([
    [800,1],
    [1000,2],
    [1200,2],
    [1500,2],
    [1800,3]
])

y  = np.array([30,40,45,60,72])

model = LinearRegression()

model.fit(x,y)

# The 'root' route
@app.route('/',methods = ['GET','POST'])
def index():
    
    pred = None
    if request.method == "POST":
        area = int(request.form.get('area'))
        rooms = int(request.form.get('rooms'))
        pre = model.predict([[area,rooms]])
        pred = round(pre[0],2)
        return render_template('index.html', prediction=pred)
    return render_template('index.html', prediction=pred)


if __name__ == '__main__':
    app.run(debug=True)


