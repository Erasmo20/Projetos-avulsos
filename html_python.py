from flask import Flask , render_template

pagina = open("templates/index.html","w")
pagina.write("""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>html_python</title>
</head>
<body>
    <table>   
        <p></p>
        <h1>Teste02</h1>
        <th>Nome</th>
        <tr>
            <td>Erasmo Alves a </td>
        </tr>
    </table> 
</body>
</html>
             """)

pagina.close()

app = Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")

app.run()
