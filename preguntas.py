"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    import csv

    total = 0
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            total += int(row[1])

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return total


def pregunta_02():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            if row[0] not in data:
                data[row[0]] = 1
            else:
                data[row[0]] += 1

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return sorted(data.items())


def pregunta_03():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            if row[0] not in data:
                data[row[0]] = int(row[1])
            else:
                data[row[0]] += int(row[1])
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return sorted(data.items())


def pregunta_04():
    import csv

    data = {str(x).zfill(2): 0 for x in range(1, 13)}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            mes = row[2].split("-")[1]
            data[mes] += 1

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return sorted(data.items())


def pregunta_05():
    import csv

    data = {}
    lista = []
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            if row[0] not in data:
                data[row[0]] = []
            data[row[0]].append(int(row[1]))
    for key in data:
        lista.append((key, max(data[key]), min(data[key])))
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return sorted(lista)


def pregunta_06():
    import csv

    data = {}
    lista = []
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            diccionarios = row[4].split(",")
            for diccionario in diccionarios:
                diccionarioReal = diccionario.split(":")
                if diccionarioReal[0] not in data:
                    data[diccionarioReal[0]] = []
                data[diccionarioReal[0]].append(int(diccionarioReal[1]))
    for key in data:
        lista.append((key, min(data[key]), max(data[key])))
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return sorted(lista)


def pregunta_07():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            numero = int(row[1])
            if numero not in data:
                data[numero] = []
            data[numero].append(row[0])
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return sorted(data.items())


def pregunta_08():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            numero = int(row[1])
            if numero not in data:
                data[numero] = set()
            data[numero].add(row[0])
    for key in data:
        data[key] = sorted(list(data[key]))

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return sorted(data.items())


def pregunta_09():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            diccionarios = row[4].split(",")
            for diccionario in diccionarios:
                diccionarioReal = diccionario.split(":")
                if diccionarioReal[0] not in data:
                    data[diccionarioReal[0]] = 1
                else:
                    data[diccionarioReal[0]] += 1
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return dict(sorted(data.items()))


def pregunta_10():
    import csv

    lista = []
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            lista.append((row[0], len(row[3].split(",")), len(row[4].split(","))))
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return lista


def pregunta_11():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            letras = row[3].split(",")
            for letra in letras:
                if letra not in data:
                    data[letra] = 0
                data[letra] += int(row[1])
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return dict(sorted(data.items()))


def pregunta_12():
    import csv

    data = {}
    with open("data.csv") as file:
        fileCsv = csv.reader(file, delimiter="\t")
        for row in fileCsv:
            if row[0] not in data:
                data[row[0]] = 0
            diccionarios = row[4].split(",")
            for diccionario in diccionarios:
                dic = diccionario.split(":")
                data[row[0]] += int(dic[1])
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return dict(sorted(data.items()))
