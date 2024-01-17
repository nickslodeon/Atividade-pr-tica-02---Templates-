# main.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculos.db'
db = SQLAlchemy(app)

class Curriculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    experiencia = db.Column(db.Text)

class CurriculoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    experiencia = TextAreaField('Experiência Profissional')
    submit = SubmitField('Criar Currículo')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurriculoForm()

    if form.validate_on_submit():
        novo_curriculo = Curriculo(
            nome=form.nome.data,
            email=form.email.data,
            telefone=form.telefone.data,
            endereco=form.endereco.data,
            experiencia=form.experiencia.data
        )
        db.session.add(novo_curriculo)
        db.session.commit()
        return redirect(url_for('listar_curriculos'))

    curriculos = Curriculo.query.all()
    return render_template('index.html', form=form, curriculos=curriculos)

@app.route('/listar_curriculos')
def listar_curriculos():
    curriculos = Curriculo.query.all()
    return render_template('listar_curriculos.html', curriculos=curriculos)

@app.route('/editar/<int:curriculo_id>', methods=['GET', 'POST'])
def editar_curriculo(curriculo_id):
    curriculo = Curriculo.query.get(curriculo_id)
    form = CurriculoForm(obj=curriculo)

    if form.validate_on_submit():
        curriculo.nome = form.nome.data
        curriculo.email = form.email.data
        curriculo.telefone = form.telefone.data
        curriculo.endereco = form.endereco.data
        curriculo.experiencia = form.experiencia.data
        db.session.commit()
        return redirect(url_for('listar_curriculos'))

    return render_template('editar_curriculo.html', form=form)

@app.route('/excluir/<int:curriculo_id>')
def excluir_curriculo(curriculo_id):
    curriculo = Curriculo.query.get(curriculo_id)
    db.session.delete(curriculo)
    db.session.commit()
    return redirect(url_for('listar_curriculos'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
