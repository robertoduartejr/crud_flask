from sqlalchemy_utils import EmailType
from app import db


class Torcedor(db.Model):

    #defini o controle de usuários repetidos a partir do CPF.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    data_nascimento = db.Column(db.DateTime)
    time = db.Column(db.String(20))
    email = db.Column(EmailType)
    cpf = db.Column(db.String(14), unique=True)

    def __init__(self,nome,data_nascimento,time,email,cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.time = time
        self.email = email
        self.cpf = cpf