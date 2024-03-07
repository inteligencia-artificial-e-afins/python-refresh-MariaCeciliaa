# -*- coding: utf-8 -*-

# Exercicio 01
def max_consecutive_sum(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Testes 01
def test_max_consecutive_sum():
    print("Teste 1 - max_consecutive_sum")
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print(max_consecutive_sum([1]) == 1)
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)



# Exercício 02
def is_palindrome(word):
    word = word.replace(" ", "").lower()

    return word == word[::-1]

# Testes 02
def text_is_palindrome():
    print("Teste 2 - is_palindrome")
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)



# Exercício 03
def count_increasing_subsets(nums):
    def backtrack(start, subset):
        nonlocal count
        if len(subset) > 0:
            count += 1
        for i in range(start, len(nums)):
            if not subset or nums[i] > subset[-1]:
                backtrack(i + 1, subset + [nums[i]])

    count = 0
    backtrack(0, [])
    return count

# Testes 03
def test_count_increasing_subsets():
    print("Teste 3 - count_increasing_subsets")
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
