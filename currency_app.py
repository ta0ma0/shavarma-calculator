import subprocess
from flask import Flask, render_template, request
from mir_calc.get_mir_page import get_page
from mir_calc.dram_calculator import shavarmator, amd_to_rur, rur_to_amd

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_data_rur', methods=['POST'])
def submit_data_rur():
    rur = request.form['RUR']  
    # Do something with the form data, e.g. store it in a database
    if rur == '':
        rur =0
    data = call_calculator(rur, 'RUR')
    return render_template('result_page.html', answer=data)

@app.route('/submit_data_amd', methods=['POST'])
def submit_data_amd():
    amd = request.form['AMD']
    if amd == '':
        amd =0
    data = call_calculator(amd, 'AMD')
# Do something with the form data, e.g. store it in a database
#   data = 'test'
#   print(data)
    return render_template('result_page.html', answer=data)

def call_calculator(data, flag):
    rate = get_page()
    dram_rate = rate
    answer = []
    if flag == 'AMD':
        # amd_value = rur_to_amd(args.amd, dram_rate[1])
        rur_value = amd_to_rur(int(data), dram_rate)
        rur_value = round(rur_value, 3)
        answer.append(f'AMD to RUR: {data} AMD =  {rur_value} RUR')
        shaverma = shavarmator(rur_value, 'RUR')
        shavarma = shavarmator(data, 'AMD')
        answer.append(f'В СПб, вы бы купили: {shaverma} x 🌯 по 200 рублей')
        answer.append(f'В Армении, вы можете купить: {shavarma} x 🌯 по 950 драм')
        return answer
    elif flag == 'RUR':
        # amd_value = rur_to_amd(args.rur, dram_rate[1])
        amd_value = rur_to_amd(int(data), dram_rate)
        amd_value = round(amd_value, 3)
        answer.append(f'RUR to AMD: {data} RUR =  {amd_value} AMD')
        shaverma = shavarmator(data, 'RUR')
        shavarma = shavarmator(amd_value, 'AMD')
        answer.append(f'В СПб, вы бы купили: {shaverma} x 🌯 по 200 рублей')
        answer.append(f'В Армении, вы можете купить: {shavarma} x 🌯 по 950 драм')
        return answer



if __name__ == '__main__':
    app.run(debug=True)
