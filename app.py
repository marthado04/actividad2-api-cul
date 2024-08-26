from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
   
    nombres = ['Yiniva', 'Alex', 'Silvio', 'Marta']
    
    return jsonify(nombres)

if __name__ == '__main__':
    app.run(debug=True)
