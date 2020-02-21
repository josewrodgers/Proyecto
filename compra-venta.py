def vender(simbolo,precio,cantidad):
    return requests.post("https://api.invertironline.com/api/v2/operar/Vender",headers={"Authorization":"Bearer "+acceso()}, data={
        "mercado":"bCBA",
        "simbolo":simbolo,
        "cantidad":cantidad,
        "precio":precio,
        "validez":"2019-04-30",
        "plazo":"t1"
    }).text

def comprar(simbolo,precio,cantidad):
    return requests.post("https://api.invertironline.com/api/v2/operar/Comprar",headers={"Authorization":"Bearer "+acceso()}, data={
        "mercado":"bCBA",
        "simbolo":simbolo,
        "cantidad":cantidad,
        "precio":precio,
        "validez":"2019-04-30",
        "plazo":"t1"

    }).text
