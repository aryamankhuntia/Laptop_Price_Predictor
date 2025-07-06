from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_brands', methods=['GET'])
def get_brands():
    response = jsonify({
        'brands': util.get_brands()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_cpus', methods=['GET'])
def get_cpus():
    response = jsonify({
        'cpus': util.get_cpus()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_laptop_price', methods=['GET','POST'])
def predict_laptop_price():
    brand = request.form['brand']
    cpu = request.form['cpu']
    screen_size = float(request.form['screen_size'])
    disk_size = float(request.form['disk_size'])
    ram = int(request.form['ram'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(brand,cpu,screen_size,disk_size,ram)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    print("Starting server for Laptop Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=False)