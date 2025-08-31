import subprocess
url="https://ntfy.sh/"
default="atencion"
def collect():
    prompt=input("""'Si sabes usar ntfy (solo descargalo de la playstore es bastante facil) podes introducir el nombre de tu topico.
    Si lo dejas en blanco me va a llegar al mio:'""")
    if prompt=="" or prompt==" " or prompt=="  ":
        prompt=default
    data=input("Mensaje a enviar al topico: "+prompt+" (añadi algo, si usas el programa, para que pueda saber quien sos):")
    if data=="" or data==None or data==" " or data=="   ":
        print("No puede ser vacio el mensaje ------")
        collect()
    else:
        subprocess.run("curl -d "+ data+" https://ntfy.sh/"+ prompt)
        print("°Mensaje Enviado!°")
while True:
    collect()