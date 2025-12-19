# Sistema de Mensagens - Teste Técnico Full Stack

## 🚀 Descrição do Projeto
Este projeto é um sistema de mensagens desenvolvido em **Django 6.x**, com uma **landpage pública** para envio de mensagens e uma **área administrativa protegida** para gestão das mensagens.  
O projeto utiliza **TailwindCSS** para estilização, **HTMX** para interações assíncronas e **Alpine.js** para microinterações e modais.

O sistema atende aos requisitos do teste técnico, incluindo autenticação, CRUD de mensagens, indicadores de mensagens lidas/não lidas e responsividade para diferentes dispositivos.

---

## 📋 Funcionalidades

### Landpage (Pública)
- Formulário funcional de envio de mensagem com validação.
- Feedback visual de sucesso ao enviar a mensagem.
- Design responsivo com TailwindCSS.

### Área Administrativa (Protegida)
- **Login personalizado** para superusuários.
- **Listagem de mensagens** com:
  - Nome, email, mensagem resumida, data de envio.
  - Indicador visual de mensagens lidas/não lidas.
  - Botões de ação para **ver**, **editar** e **excluir**.
- **Visualização individual** de mensagens.
- **Edição de mensagens** com formulário.
- **Exclusão com confirmação**.
- **Logout com confirmação via modal**.
- Interatividade com **HTMX** e **Alpine.js**:
  - Modais dinâmicos para edição e exclusão.
  - Marcar mensagens como lidas sem recarregar a página.
  - Edição inline de mensagens.

---

## 🛠️ Tecnologias Utilizadas
- **Backend:** Django 6.x
- **Frontend:** HTML5, TailwindCSS, HTMX, Alpine.js
- **Banco de dados:** SQLite (default Django, fácil de configurar)
- **Controle de versão:** Git / GitHub

---

## 💻 Estrutura do Projeto

```
seu-projeto/
├── README.md**
├── requirements.txt**
├── manage.py
├── core/
│ ├── settings.py
│ └── urls.py
├── app_principal/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
│ ├── base.html
│ ├── landpage.html
│ ├── login.html
│ ├── logout_confirm.html
│ ├── messages_list.html
│ ├── message_detail.html
│ ├── message_edit.html
│ └── message_delete_confirm.html
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── media/
└── examples/
```

---

## ⚡ Funcionalidades Avançadas

- **Modais com Alpine.js e HTMX** para:
  - Confirmação de logout
  - Confirmação de exclusão
  - Edição de mensagens
- **Edição inline** de mensagens usando HTMX
- **Marcar como lida** sem reload da página
- **Filtros de busca e status** com HTMX (opcional)
- **Responsividade total** em todas as telas administrativas

---

## 📦 Como Rodar o Projeto

```bash
1️⃣ Clone o repositório:
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```
```bash
2️⃣ Crie e ative um ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```
```bash
3️⃣ Instale as dependências:

pip install -r requirements.txt
```
```bash
4️⃣ Configure o banco de dados:

python manage.py migrate
```
```bash
5️⃣ Crie um superusuário:

python manage.py createsuperuser
```
```bash
6️⃣ Execute o servidor:

python manage.py runserver
```
```bash
7️⃣ Acesse a aplicação:

Landpage pública: http://localhost:8000

Área administrativa: http://localhost:8000/admin
```
```bash
📝 Decisões Técnicas

Django: Framework robusto para backend e autenticação nativa.

TailwindCSS: Facilita estilização responsiva e consistente.

HTMX: Permite interações assíncronas sem recarregar páginas.

Alpine.js: Implementação de modais e microinterações de forma simples.

Estrutura de templates: base.html para layout comum, reaproveitamento de código.

Segurança: Rotas administrativas protegidas com @login_required.

UX: Feedbacks visuais claros, cores para status de mensagens, design clean.
```
```bash
✅ Observações

Todos os requisitos obrigatórios do teste foram implementados.

O projeto é responsivo e funcional.

HTMX e Alpine.js foram usados para interatividade avançada.

Funcionalidades extras como filtros e edição inline são implementadas.
```
