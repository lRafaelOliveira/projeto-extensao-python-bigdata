# Site de Comunicação para ONG
Este é um site simples construído com Python (Flask) para ajudar uma ONG a se comunicar de forma mais eficaz com seus beneficiários. O site inclui uma página inicial, uma página de eventos, um formulário de contato e uma integração para o envio de notificações por e-mail.

Funcionalidades
Página inicial com informações básicas sobre a ONG.
Página de eventos com a exibição dos próximos eventos.
Página de contato com um formulário para envio de mensagens para a administração da ONG.
Design responsivo para uso em dispositivos móveis e desktops.
Integração com serviços de e-mail para o envio de notificações.
Tecnologias Utilizadas
Flask: Um framework web leve para Python.
Flask-Mail: Para envio de notificações por e-mail.
HTML/CSS/JavaScript: Para a estrutura e design do front-end.
Bootstrap (opcional): Para tornar o design responsivo (ou pode ser usado TailwindCSS).
Heroku/PythonAnywhere: (Opcional) Para hospedagem.
Instruções de Instalação
1. Clonar o Repositório
``` git clone https://github.com/seuusuario/seu-repositorio.git cd seu-repositorio ```

2. Configurar o Ambiente Virtual
``` python -m venv venv source venv/bin/activate # No Windows use: venv\Scripts\activate ```

3. Instalar as Dependências
``` pip install -r requirements.txt ```

4. Definir Variáveis de Ambiente
Antes de executar o aplicativo, você precisa definir as variáveis de ambiente para o serviço de e-mail (como o Gmail). ``` export EMAIL_USER='seu-email@gmail.com' export EMAIL_PASS='sua-senha-do-email' ```

No Windows, use set em vez de export.

5. Executar a Aplicação
``` python app.py ``` A aplicação será iniciada em http://127.0.0.1:5000/. Você pode abrir essa URL no navegador para visualizar o site.

6. Testes
Você pode testar o formulário de contato preenchendo e enviando-o. A mensagem será enviada para o endereço de e-mail especificado na variável de ambiente EMAIL_USER.

Implantação
Implantar no Heroku
Crie uma conta no Heroku e instale o Heroku CLI.
Faça login no Heroku pelo CLI: &&& heroku login &&&
Crie um aplicativo Heroku: &&& heroku create &&&
Envie o código para o Heroku: &&& git push heroku master &&&
Defina as variáveis de ambiente para e-mail no Heroku: &&& heroku config
EMAIL_USER='seu-email@gmail.com' heroku config
EMAIL_PASS='sua-senha-do-email' &&&
Abra seu app no Heroku no navegador: &&& heroku open &&&
Implantar no PythonAnywhere
Crie uma conta no PythonAnywhere.
Envie seu projeto para o PythonAnywhere usando Git ou via o painel de controle.
Configure um aplicativo web a partir do painel do PythonAnywhere e vincule-o ao app Flask.
Defina as variáveis de ambiente via as configurações de ambiente do PythonAnywhere.
Estrutura do Projeto
``` project/ │ ├── app.py # Aplicação principal do Flask ├── templates/ # Pasta para arquivos HTML │ ├── index.html # Página inicial │ ├── contact.html # Página de contato │ └── base.html # Template base ├── static/ # Arquivos estáticos (CSS, JS, imagens) │ └── style.css # Estilo CSS customizado ├── requirements.txt # Dependências do projeto └── config.py # Configurações para e-mail e outras ```
