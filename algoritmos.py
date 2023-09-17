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


ALGORITMOS = {"ayudante": greedy_scaloni_por_ayudante,
              "diferencia": greedy_scaloni_por_diferencia,
              "scaloni": greedy_scaloni_por_scaloni}
