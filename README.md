# Agenda de Contatos - Pratica TDD 4

Projeto desenvolvido como parte da disciplina **Desenvolvimento Web 3**.
O objetivo e implementar uma **agenda de contatos completa**, utilizando **Django + Testes (TDD)**, com **cobertura minima de 90%**.

---

## Funcionalidades

### Sprint 1
- Sistema de Login e Logout
- Autenticacao somente com e-mail institucional `@fatec.sp.gov.br`
- Telas entregues: Login, Index (home) e Logout

### Sprint 2
- CRUD de Contatos (Model **Agenda**)
  - Cadastrar contato
  - Listar contatos
  - Atualizar contato
  - Remover contato
- Protecao de rotas (somente usuarios autenticados)
- Manter cobertura de testes acima de **90%**

---

## Telas do projeto

| Tela Login | Tela Index | Logout |
|------------|------------|--------|
| [Login](https://ik.imagekit.io/vvkjumzbj/Py/login.png?updatedAt=1762212158611) | [Index](https://ik.imagekit.io/vvkjumzbj/Py/index.png?updatedAt=1762212158687) | [Logout](https://ik.imagekit.io/vvkjumzbj/Py/logout.png?updatedAt=1762212158609) |

---

## Como executar o projeto

### Pre-requisitos
- Python 3.10+
- Git
- Virtualenv (Linux) ou venv (Windows)

### Linux

```bash
git clone https://github.com/orlandosaraivajr/Pratica_TDD_4.git
cd Pratica_TDD_4/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

cd agenda/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test
coverage html
python manage.py createsuperuser
python manage.py runserver
```

### Windows

```powershell
git clone https://github.com/orlandosaraivajr/Pratica_TDD_4.git
cd Pratica_TDD_4/

python -m venv venv      # ou: virtualenv venv
venv\Scripts\activate.bat     # CMD
.env\Scripts\Activate.ps1   # PowerShell

pip install -r requirements.txt

cd agenda/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test
coverage html
python manage.py createsuperuser
python manage.py runserver
```

---

## Superusuario (para correcao)

| Campo | Informacao |
|-------|------------|
| Username | `admin12` |
| Email | seu e-mail institucional (`@fatec.sp.gov.br`) |
| Password | `fatec` |

---

## Cobertura de Testes

O relatorio HTML do coverage ficara disponivel na pasta:

```
/agenda/htmlcov/index.html
```

---

## Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Django | Desenvolvimento da aplicacao |
| SQLite | Banco de dados |
| TDD (pytest / unittest / coverage) | Garantia de qualidade e seguranca de codigo |
| Bootstrap | Interface visual |

---

## Autor

Projeto desenvolvido para fins educacionais na disciplina **Desenvolvimento Web 3** - FATEC. Por Rafaela Lemes.
