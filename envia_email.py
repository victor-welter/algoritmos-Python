import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
# Configurações de e-mail
remetente_email = 'vw0121225@setrem.com.br'
remetente_senha = 'vINI909018'
destinatario_email = 'desenvolvimento.welter@gmail.com'

# Conecte-se ao servidor SMTP do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remetente_email, remetente_senha)

# Crie a mensagem de e-mail
mensagem = MIMEMultipart()
mensagem['From'] = remetente_email
mensagem['To'] = destinatario_email
mensagem['Subject'] = 'Oi, sou o Welter!'
corpo_email = 'Oi, sou o Welter!'
mensagem.attach(MIMEText(corpo_email, 'plain'))
texto_do_email = mensagem.as_string()

server.sendmail(remetente_email, destinatario_email, texto_do_email)
print('E-mail enviado com sucesso!')

# Encerre a conexão com o servidor
server.quit()

