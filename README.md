# KMDB

## Clone do repósitorio + execução local:

prossiga com os passos: 
### você deve ter o python e o gerenciador de pacotes PIP instalados na sua máquina.

1. Crone o repósitorio:
```bash
git clone <link-do-repositorio>
```
2. Acessa a pasta que você clonou e execute os seguintes comandos:
```bash
cd <nome-da-pasta>
```

- Crie seu ambiente virtual:
```bash
python -m venv venv
```

- Ative seu venv:
```bash
# linux:
source venv/bin/activate
# windows:
.\venv\Scripts\activate
```

- Instale as dependencias:
```bash
# linux:
pip install -r requirements.txt
```

3. Executando a aplicação localmente:

- Gerando as tabelas do banco de dados:
```shell
python manage.py migrate
```
- Criando usuário admin para acessar o painel administrativo:
```bash
python manage.py create_admin
# username e password padrão são:
# username: admin
# password: admin1234
# você pode definir o username, password e email opcionais passando da seguinte forma:
python manage.py create_admin --username <seu-username> --password <seu-password> --email <seu-email>
# você pode encurtar os parâmetros da seguinte forma:
# --username = -u
# --password = -p
# --email = -e
```

- Executando o servidor:
```shell
python manage.py runserver
```

## Pronto agora você pode acessar todos os endpoints a partir da rota: http://127.0.0.1:8000/

### Ao acessar http://127.0.0.1:8000/admin/ você terá acesso ao painel administrativo, basta acessar com seu usuário criado no passo 3.2
