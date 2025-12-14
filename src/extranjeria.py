import csv
from typing import NamedTuple



RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)



def lee_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    res = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais_nacimiento, hombres, mujeres in lector:
            distrito = str(distrito)
            seccion = str(seccion)
            barrio = str(barrio)
            pais_nacimiento = str(pais_nacimiento)
            hombres = int(hombres)
            mujeres = int(mujeres)
            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais_nacimiento, hombres, mujeres))
    return res


ruta = "data\extranjeriaSevilla.csv"
registros = lee_datos_extranjeria(ruta)
# print(registros[0])



def numero_nacionalidades_distintas(registros):
    res = set()
    for registro in registros:
        res.add(registro.pais)
    return len(res)

# print(numero_nacionalidades_distintas(registros))
    


def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    res = set() #cuidado con los duplicados
    for r in registros:
        if r.pais in paises:
            res.add((r.distrito, r.seccion))

    res = list(res)
    # print(res)
    return sorted(res, key = lambda x: x[0])

# print(f"{len(secciones_distritos_con_extranjeros_nacionalidades(registros, {'ITALIA', 'ALEMANIA'}))}")



def total_extranjeros_por_pais(registros):
    res = dict()
    for r in registros:
        if r.pais not in res:
            res[r.pais] = 0
        else:
            res[r.pais] += r.hombres + r.mujeres

    # res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return res


# print(total_extranjeros_por_pais(registros))




def top_n_extranjeria(registros: list[RegistroExtranjeria], n: int = 3) -> list[tuple[str, int]]:
    res = {}
    for r in registros:
        if r.pais not in res:
            res[r.pais] = 0
        else:
            res[r.pais] += r.hombres + r.mujeres

    ordenados = sorted(res.items(), key=lambda x: x[1], reverse=True)
    
    return ordenados[:n]


# print(top_n_extranjeria(registros, 3))


def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str:
    # Diccionario: barrio = conjunto de países
    paises_por_barrio = {}
    for r in registros:
        if r.barrio not in paises_por_barrio: #si no está, lo añadimos sin ningun valor
            paises_por_barrio[r.barrio] = set()
        else:
            paises_por_barrio[r.barrio].add(r.pais) # si ya estaba registrado el barrio le añadimos el pais
    
    barrio_max = max(paises_por_barrio.items(), key=lambda x: len(x[1]))
    
    return barrio_max[0]


# print(barrio_mas_multicultural(registros))



def barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo: str | None = None) -> str:
    # Diccionario: barrio = total de extranjeros
    totales = {}
    for r in registros:
        if tipo is None:
            cantidad = r.hombres + r.mujeres
        elif tipo == 'Hombres':
            cantidad = r.hombres
        elif tipo == 'Mujeres':
            cantidad = r.mujeres
        
        totales[r.barrio] = totales.get(r.barrio, 0) + cantidad
    
    barrio_max = max(totales.items(), key=lambda x: x[1])
    return barrio_max[0]

# print(barrio_con_mas_extranjeros(registros, "Mujeres"))






def pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]) -> dict[str:str]:
    # Diccionario: distrito -> {pais = total_extranjeros}
    conteo = {}
    for r in registros:
        if r.distrito not in conteo:
            conteo[r.distrito] = {}
        conteo[r.distrito][r.pais] = conteo[r.distrito].get(r.pais, 0) + r.hombres + r.mujeres
    
    # Diccionario resultado: distrito -> país con más extranjeros
    resultado = {}
    for distrito, paises in conteo.items():
        pais_max = max(paises.items(), key=lambda x: x[1])[0]
        resultado[distrito] = pais_max
    
    return resultado


print(pais_mas_representado_por_distrito(registros))




