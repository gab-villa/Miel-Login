import json
import requests
headers = {
    #fijarse en el log al ingresar por la pagina
    #puede probar con: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
    'user-agent': 'Escribe-tu-user-agent'
}
login_data = {
    'usuario': 'Escribe-tu-usuario',
    'clave': 'Escribe-tu-clave'
}
with requests.Session() as s:
    #Esto puede cambiar en el tiempo. 30/12/2021
    url = "https://miel.unlam.edu.ar/principal/event/loginAjax/"

    r = s.get(url, headers=headers)
    r = s.post(url, data=login_data, headers=headers)

    jsonRes = json.loads(r.content)
    
    if jsonRes["estado"] == 0:
	print("El usuario se ha logueado correctamente.")
    else:
	print("No se ha podido logear.")
