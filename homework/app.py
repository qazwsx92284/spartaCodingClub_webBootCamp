from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    addr_receive = request.form['addr_give']
    phone_receive = request.form['phone_give']


    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'addr': addr_receive,
        'phone': phone_receive
    }

    db.shoping.insert_one(doc)

    return jsonify({'msg': '!!저장완료!!'})


@app.route('/order', methods=['GET'])
def read_order():
    orders = list(db.shoping.find({}, {'_id': False}))
    return jsonify({'all_orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
