# app.py
from flask import Flask, request, render_template
from controllers.courtController import insertarCourt
app = Flask(__name__)


@app.route('/courts', methods=['GET'])
def formulario():
    return render_template('formularioCourt.html')  

@app.route('/courts', methods=['POST'])
def agregar_court():
    if request.method == 'POST':
        price = request.form['price']
        status = request.form['status']
        
        respuesta = insertarCourt(price, status)
        
        if respuesta:
            return render_template('formularioCourt.html')
        else:
            return 'Error al crear court'
        
if __name__ == '__main__':
    app.run(debug=True)
