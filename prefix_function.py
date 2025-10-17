def prefix_function(s: str) -> list[int]:
    """
    Вычисляет префикс функцию для строки s
    """
    n = len(s)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i - 1]
        # Отступаем назад по уже вычисленным значениям, пока не найдем совпадающий символ или не дойдем до начала шаблона
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        
        # Если символы совпали, увеличиваем длину текущего префикса
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
    

def main_function(s: str) -> str:
    """
    Находит самый длинный собственный префикс строки, который также является её суффиксом
    """
    if not s:
        return ""

    pi = prefix_function(s)
    
    # Длина искомого префикса — это последнее значение в массиве
    longest_prefix_length = pi[-1] if pi else 0
    
    # Возвращаем срез строки нужной длины
    return s[:longest_prefix_length]

# Примеры

s1 = "motomoto"
result1 = main_function(s1)
print(f"Строка: '{s1}' \n'{result1}'")

s2 = "jojo" # Is that a JoJo reference?!
result2 = main_function(s2)
print(f"Строка: '{s2}' \n'{result2}'")

s3 = "gibbsgibbon"
result3 = main_function(s3)
print(f"Строка: '{s3}' \n'{result3}'")