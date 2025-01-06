# Desenvolvimento web com Django, React e deploy AWS e Linux

Curso: [Desenvolvimento web com Django, React e deploy AWS e Linux](https://www.udemy.com/course/desenvolvimento-web-com-django-react-e-deploy-aws-e-linux/)

## React

### Criando um novo app React 19

```bash
npm config set legacy-peer-deps true #To solve the error with React 19
npx create-react-app <nome_para_o_projeto>
cd <nome_para_o_projeto>
npm install --save-dev ajv@^7 #To install the missing dependency
npm start
```

## Django

### Criando um novo app Django 4.2

Dei preferencia por criar uma nova venv Python e instalar o Django 4.2 nela:

```bash
#Com a venv já ativada
pip install django==4.2
django-admin startproject <nome_para_o_projeto> .
python manage.py runserver
```

### Django Rest Framework

[Django Rest Framework](https://www.django-rest-framework.org/)

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

[Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

```bash
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```

#### Serializers

São como os arquivos POCO em .Net. Definem as entidades que serão utilizadas no projeto.

#### Views

Definem como as entidades serão retornadas, endpoints.

#### Testando os endpoints

Sendo necessário autenticação, usa-se a url: http://127.0.0.1:8000/admin/
