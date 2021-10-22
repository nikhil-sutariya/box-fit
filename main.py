from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

class conceptserve_exception_APIException(Exception):
    def itemerror(self):
        return "There are more than 15 items!!"

class conceptserve_box_packfit(conceptserve_exception_APIException):
    def __init__(self):
        self.max_weight = []
        self.values = []
        self.answer = []

    def read_file(self,filename):
        f = open(filename)
        for line in f:
            values = line.split(":")
            self.max_weight.append(values[0])
            self.values.append(values[1])
        
        for i in range(len(self.values)):
            self.box(self.values[i], self.max_weight[i])

    def box(self, boxdata, capacity):
        current = 0
        output = []
        items = 0
        df = pd.DataFrame(eval(boxdata), columns= ['index', 'weight', 'cost'])
        df.eval('cwr = (cost/weight) + cost', inplace=True)
        df.sort_values(by='cwr', ascending=False, inplace=True, ignore_index=True)
        global result
        result = df
        for index, weight in zip(df['index'], df['weight']):
            items += 1
            if (weight + current) <= int(capacity):
                current = weight + current
                output.append(index)

        if items <= 15:
            if(len(output)>0):
                anslist = ','.join([str(item) for item in output])
                self.answer.append(anslist)
            else:
                self.answer.append("-")
        else:
            anslist = ",".join([str(item) for item in output])
            self.answer.append(self.itemerror())

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        filename = request.form.get('file')
        obj = conceptserve_box_packfit()
        obj.read_file(filename)
        return render_template('index.html',result = obj.answer)
    return render_template("index.html")
