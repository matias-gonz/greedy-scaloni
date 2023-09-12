from typing import List, Tuple


def greedy_scaloni_por_ayudante(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por A_i en orden descendiente
    """
    return sorted(tiempos, key=lambda t: t[1], reverse=True)


def greedy_scaloni_por_diferencia(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por A_i - S_i en orden descendiente
    """
    return sorted(tiempos, key=lambda t: t[1] - t[0], reverse=True)


def greedy_scaloni_por_scaloni(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por S_i en orden ascendente
    """
    return sorted(tiempos, key=lambda t: t[0])


def cargar_tiempos(path) -> List[Tuple[int, int]]:
    with open(path, "r") as archivo:
        lineas = archivo.readlines()
        tiempos = []
        for linea in lineas[1:]:
            t_i = linea.strip().split(',')
            s_i = int(t_i[0])
            a_i = int(t_i[1])
            tiempos.append((s_i, a_i))

    return tiempos


def main():
    tiempos = cargar_tiempos("casos/10000 elem.csv")
    print(greedy_scaloni_por_ayudante(tiempos))
    print(greedy_scaloni_por_diferencia(tiempos))
    print(greedy_scaloni_por_scaloni(tiempos))


main()
