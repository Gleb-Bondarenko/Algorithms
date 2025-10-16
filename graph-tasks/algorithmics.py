import collections
from typing import List, Dict
from graph_abc import Graph

class GraphAlgorithms:
    """
    Класс c алгоритмами для работы с графами
    Все методы реализованы как staticmethod, чтобы вызывать их напрямую,
    передавая Graph без необходимости создавать экземпляр класса
    """

    @staticmethod
    def bfs(graph: Graph, start: int) -> List[int]:
        """
        BFS алгоритм - возвращает порядок обхода вершин
        """
        # Проверяем, что стартовая вершина находится в допустимом диапазоне
        if not (0 <= start < graph.vertices):
            raise IndexError("Start vertex is out of range.")
        # Получаем список смежности
        adj = graph.get_adjacency_list()
        
        queue = collections.deque([start])
        visited = {start}
        visit_order = []
        
        # Пока есть вершины в очереди
        while queue:
            u = queue.popleft()
            visit_order.append(u)
            
            # Перебираем всех соседей (v) вершины u
            for v, _ in adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        
        return visit_order

    @staticmethod
    def dfs(graph: Graph, start: int) -> List[int]:
        """
        DFS - возвращает порядок обхода вершин
        """
        if not (0 <= start < graph.vertices):
            raise IndexError("Start vertex is out of range.")

        adj = graph.get_adjacency_list()
        
        visited = set()
        visit_order = []

        def _dfs_recursive(u: int):
            visited.add(u)
            visit_order.append(u)
            
            for v, _ in adj.get(u, []):
                if v not in visited:
                    _dfs_recursive(v)

        _dfs_recursive(start)
        
        return visit_order

    @staticmethod
    def connected_components(graph: Graph) -> List[List[int]]:
        """
        Находит все связные компоненты графа
        Для направленного графа возвращает слабо связные компоненты
        """
        adj = graph.get_adjacency_list()
        
        # Создаем список поиска смежности для обхода
        # Для направленного графа делаем его неориентированным (чтобы найти слабые компоненты)
        search_adj = {i: [] for i in range(graph.vertices)}

        if graph.is_directed():
            # Добавляем обратные рёбра, превращая направленный граф в неориентированный
            for u, neighbors in adj.items():
                for v, _ in neighbors:
                    search_adj[u].append(v)
                    search_adj[v].append(u)
            # Убираем дубликаты и сортируем для детерминированного вывода       
            for u in search_adj:
                search_adj[u] = sorted(list(set(search_adj[u])))
        else:
            for u, neighbors in adj.items():
                search_adj[u] = [v for v, _ in neighbors]

        visited = set()
        components = []

        # Обходим все вершины
        for i in range(graph.vertices):
            if i not in visited:
                current_component = []
                q = collections.deque([i])
                visited.add(i)
                
                while q:
                    u = q.popleft()
                    current_component.append(u)
                    # Добавляем непосещенных соседей
                    for v in search_adj.get(u, []):
                        if v not in visited:
                            visited.add(v)
                            q.append(v)
                
                current_component.sort()
                components.append(current_component)
        
        components.sort(key=lambda comp: comp[0])
        return components

    @staticmethod
    def components_with_stats(graph: Graph) -> List[Dict[str, object]]:
        """
        Возвращает статистику для каждой связной компоненты:
        1) список вершин
        2) количество вершин
        3) количество рёбер внутри компоненты
        4) наименьшую вершину
        """
        comps = GraphAlgorithms.connected_components(graph)
        adj = graph.get_adjacency_list()
        stats_list = []

        # Считаем параметры для каждой компоненты   
        for component in comps:
            component_set = set(component)
            node_count = len(component)
            smallest_vertex = component[0] 
            edge_count = 0
            
            for u in component:
                for v, _ in adj.get(u, []):
                    if v in component_set:
                        if graph.is_directed():
                            # В направленном графе каждое ребро учитывается отдельно
                            edge_count += 1
                        else:
                            if u < v:
                                # В неориентированном графе считаем ребро (u,v) только один раз
                                edge_count += 1
            
            # Формируем словарь со статистикой
            stats_list.append({
                "vertices": component,
                "node_count": node_count,
                "edge_count": edge_count,
                "smallest_vertex": smallest_vertex
            })
            
        stats_list.sort(key=lambda s: (-s["node_count"], -s["edge_count"], s["smallest_vertex"]))
        
        return stats_list