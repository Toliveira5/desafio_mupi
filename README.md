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

