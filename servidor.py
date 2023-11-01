import socket 
from flask import Flask ,render_template 

HOST='localhost'
PORT=5000

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("Aguardando conexão de um cliente")
conn, ender =s.accept()
print("conectado em : ",ender)

app = Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")

app.run()

while True:
    data = conn.recv(1024)
    if not data:
        print("Fechando a conexão")
        conn.close
        break
    conn.sendall(data)