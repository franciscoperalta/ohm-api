from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
	return "Para acceder al servicio se debe acceder a las rutas es: url + /potencial o /corriente o /resistencia + dato1 + & + dato2"

@app.route('/potencial/<string:corriente>&<string:resistencia>')
def getPotencial(corriente, resistencia):
	potencial = float(corriente) * float(resistencia)
	return jsonify({"potencial":potencial})

@app.route('/corriente/<string:potencial>&<string:resistencia>')
def getCorriente(potencial, resistencia):
	corriente = float(potencial) / float(resistencia)
	return jsonify({"corriente":corriente})

@app.route('/resistencia/<string:potencial>&<string:corriente>')
def getResistencia(potencial, corriente):
	resistencia = float(potencial) / float(corriente)
	return jsonify({"resistencia":resistencia})

if __name__ == '__main__':
	app.run(debug=True)
