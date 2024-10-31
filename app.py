from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        tamano = int(request.form['tamano'])
        
        # Generar el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=tamano,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)

        # Crear y guardar la imagen
        imagen_qr = qr.make_image(fill_color="black", back_color="white")
        ruta_archivo = "codigo_qr.png"
        imagen_qr.save(ruta_archivo)

        return send_file(ruta_archivo, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
