#arquivo pra chamar todos os arquivos em sequencia e evitar erro do flask de referência circular

import app
from models import Torcedor
import views

#criar tudo no banco, caso não tenha sido criado..

#rodar aplicação
if __name__ == '__main__':
    app.db.create_all()
    app.app.run(debug=True)

