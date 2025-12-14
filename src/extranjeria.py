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

    res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return res


print(total_extranjeros_por_pais(registros))
