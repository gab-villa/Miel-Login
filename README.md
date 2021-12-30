# Miel-Login
script en python para logearse a miel. Automatizable con programadores de tareas como crontab.
Primero que nada debe contar con las librerias requests y json.
Para comenzar a usar debe completar los espacios indicados en el programa (usuario y clave)
Si el programa no funciona, podria ser que la pagina cambio, los datos los debera sacar de los logs generados al ingresar por la pagina web.
En chrome, para sacar los logs debe usar la herramienta de "inspeccionar elemento" y buscar "red". Active la opcion de "preservar log".Debe comenzar a grabar con el boton rojo, y luego logearse a la pagina. Busque un log con el nombre "login-ajax" o algun nombre similar. Sabra que es el correcto si posee sus credenciales.
