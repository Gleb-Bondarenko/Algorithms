# 547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Массив для отслеживания посещенных городов
        visited = [False] * n
        provinces_count = 0

        def DFS(city_index):
            # Помечаем текущий город как посещенный
            visited[city_index] = True
            
            # Проверяем наличие соседних городов
            for neighbor_index in range(n):
                # Если есть прямое соединение и соседа мы еще не посещали
                if isConnected[city_index][neighbor_index] == 1 and not visited[neighbor_index]:
                    DFS(neighbor_index)

        # Перебор всех городов
        for i in range(n):
            # Если город еще не был посещен, значит найдена новая провинция
            if not visited[i]:
                provinces_count += 1
                # Запускаем DFS, чтобы найти все города в этой провинции
                DFS(i)
        
        return provinces_count
        