from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Grea', idade=12)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Cute Kyouhime').first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Grea").first()
    pessoa.nome = "Cute Kyouhime"
    pessoa.idade = 12
    pessoa.save()

def deleta_pesssoa():
    pessoa = Pessoas.query.filter_by(nome='Grea').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    #insere_pessoas()
    insere_usuario('Grea', '123')
    consulta_todos_usuarios()
    #deleta_pesssoa()
    #consulta()
    #altera_pessoa()

