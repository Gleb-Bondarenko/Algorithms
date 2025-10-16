# 695. Max Area of Island # 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Проверяем, пуста ли сетка. Если да, островов нет.
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        # Представим поле, как граф. Тогда можем применить DFS (обход в глубину). 
        def DFS(r, c):
            # Проверка выхода за границы поля или если это вода
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                return 0

            # Зануляем клетку, чтобы не посещать ее снова
            grid[r][c] = 0

            # Считаем текущую клетку и поэтапно прибавляем соседние клетки
            current_area = 1
            current_area += DFS(r + 1, c)
            current_area += DFS(r - 1, c)
            current_area += DFS(r, c + 1)
            current_area += DFS(r, c - 1)
            
            return current_area

        # Цикл для прохода по всему полю
        for r in range(rows):
            for c in range(cols):
                # Если находим часть острова, запускаем DFS
                if grid[r][c] == 1:
                    # Обновляем максимальную площадь
                    current_island_area = DFS(r, c)
                    max_area = max(max_area, current_island_area)
        
        return max_area
        