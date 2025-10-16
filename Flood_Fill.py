class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # Исходный цвет начального пикселя
        initial_color = image[sr][sc]

        # Если новый цвет совпадает с исходным, то никаких изменений не требуется
        if initial_color == color:
            return image

        # Размеры изображения для проверки границ
        rows, cols = len(image), len(image[0])

        # DFS (поиск в глубину)
        def DFS(r, c):
            # Проверяем условия: ячейка находится в пределах границ и цвет текущего пикселя совпадает с исходным цветом
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == initial_color:
                image[r][c] = color

                # Вызываем функцию для соседей
                DFS(r + 1, c)
                DFS(r - 1, c)
                DFS(r, c + 1)
                DFS(r, c - 1)

        # Запускаем функцию с первого пикселя
        DFS(sr, sc)

        # Новое изображение
        return image
        