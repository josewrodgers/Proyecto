import requests
import json
import pandas as pd
import datetime
from datetime import datetime


def acceso(usuario="USUARIO",contraseña="CONTRASEÑA"):
    return json.loads(requests.post("https://api.invertironline.com/token",data={
        "username":usuario,
        "password":contraseña,
        "grant_type":"password"
    }).text)["access_token"]cm


def intradia(simbolo):

    url_idTitulo = 'https://www.invertironline.com/api/cotizaciones/idtitulo?simbolo='+simbolo+'&mercado=BCBA'
    idTitulo = requests.get( url = url_idTitulo , headers = {
        'simbolo':simbolo,
        'mercado':'BCBA'
        } )
    _id = str(idTitulo.text)
    url = "https://www.invertironline.com/Titulo/GraficoIntradiario?idTitulo="+_id+"&idTipo=4&idMercado=1"
    dato = requests.get( url , headers = {
        'idTitulo': _id,
        'idTipo': '4',
        'idMercado': '1'
        } )
    #print(dato.text)
    tabla = json.loads(dato.text)
    hora = []
    precio = []
    volumen = []
    for data in tabla:
        fechahora = data["FechaHora"]
        fh = datetime.utcfromtimestamp(fechahora).strftime('%d-%m-%Y %H:%M:%S')
        hora.append(fh)
        precio.append(data["Ultima"])
        volumen.append(data["CantidadNominal"])
    dataset = {"Hora":hora,"Precio":precio,"Volumen":volumen}
    dataset = pd.DataFrame(dataset , columns=["Hora","Precio","Volumen"])
    return dataset


print(json.loads(requests.post("https://api.invertironline.com/token", data={
    "username": matiassolana1,
    "password": mat0015040,
    "grant_type": "password"
}).text)["access_token"])