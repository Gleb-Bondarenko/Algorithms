from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class Graph(ABC):

    def __init__(self, vertices: int, directed: bool = False, weighted: bool = False):
        """
        Инициализатор графа

        Args:
            vertices: количество вершин (должно быть >= 0)
            directed: является ли граф направленным
            weighted: является ли граф взвешенным
        """
        if vertices < 0:
            raise ValueError("vertices must be non-negative")
        
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        # Внутреннее хранилище списка смежности: ключ — номер вершины, значение — список кортежей (сосед, вес)
        self._adjacency_list: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(vertices)}

    # Проверка корректности индекса вершины
    def _check_vertex(self, v: int) -> None:
        # Проверка корректности индекса вершины
        if not (0 <= v < self.vertices):
            raise IndexError(f"vertex {v} is out of range [0, {self.vertices - 1}]")

    @abstractmethod
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """
        Абстрактный метод добавления ребра в граф
        Реализуется в потомках (например, Directed Graph или Undirected Graph)
        """
        pass

    def get_adjacency_list(self) -> Dict[int, List[Tuple[int, float]]]:
        """
        Возвращает копию списка смежности, где соседи каждой вершины отсортированы по индексу
        """
        adj_list_copy = {}
        for vertex, neighbors in self._adjacency_list.items():
            # Сортируем список соседей по индексу вершины
            sorted_neighbors = sorted(neighbors, key=lambda item: item[0])
            adj_list_copy[vertex] = sorted_neighbors
        return adj_list_copy
        # Возвращает матрицу смежности графа

    def get_adjacency_matrix(self) -> List[List[float]]:
        """
        Строит и возвращает матрицу смежности (nxn)
        Для неориентированного графа матрица симметрична
        """
        matrix = [[0.0] * self.vertices for _ in range(self.vertices)]
        for u, neighbors in self._adjacency_list.items():
            for v, weight in neighbors:
                matrix[u][v] = weight
        return matrix

    def get_incidence_matrix(self) -> List[List[int]]:
        # Возвращает матрицу инцидентности графа
        edges = set()
        # Собираем все уникальные рёбра
        for u, neighbors in self._adjacency_list.items():
            for v, _ in neighbors:
                if self.directed:
                    # В ориентированном графе направление имеет значение
                    edges.add((u, v))
                else:
                    # В неориентированном храним (min, max), чтобы не дублировать (u,v) и (v,u)
                    edges.add(tuple(sorted((u, v))))
        
        # Сортируем рёбра, чтобы порядок был фиксированным
        sorted_edges = sorted(list(edges))
        num_edges = len(sorted_edges)

        # Если рёбер нет, возвращаем пустую матрицу (nx0)
        if num_edges == 0:
            return [[] for _ in range(self.vertices)]
            
        # Создаём матрицу nxm, заполненную нулями
        matrix = [[0] * num_edges for _ in range(self.vertices)]

        # Заполняем матрицу значениями
        for j, edge in enumerate(sorted_edges):
            u, v = edge
            if self.directed:
                matrix[u][j] = -1
                matrix[v][j] = 1
            else:  
                matrix[u][j] = 1
                matrix[v][j] = 1
        
        return matrix

    def is_directed(self) -> bool:
        # Возвращает True, если граф направленный, иначе False.
        return self.directed