from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave123'

@app.route('/')
def inicio():
    return redirect('/tmb')

@app.route('/tmb', methods=['GET','POST'])
def tmb():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            edad = int(request.form['edad'])
            genero = request.form['genero']
            act = request.form['actividad fisica']

            if genero == 'hombre':
                tmb = (10*peso)+(6.25*altura)-(5*edad)+5
            else:
                tmb = (10*peso)+(6.25*altura)-(5*edad)-161

            if act == 'nulo':
                get = tmb*1.2
            elif act == 'poco':
                get = tmb*1.375
            elif act == 'moderado':
                get = tmb*1.55
            else:
                get = tmb*1.725

            return render_template('resultado.html', tmb=round(tmb,2), get=round(get,2), genero=genero)
        
        except:
            flash("A ocurrido un errorsote con los datos, intenta otra vez", "error")
            return redirect(url_for('tmb'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)