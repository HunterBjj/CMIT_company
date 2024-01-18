"""
1) Решить задачу: в строке, состоящей из слов, разделенных пробелом, найти самое длинное слово.
2) Код задачи должен быть выложен на GitHub.
3) Ссылку на результат скинуть в чат.
"""


def find_max(words):
    len_max = 0
    for word in words:
        len_word = len(word)
        if len_word > len_max:
            len_max = len_word

    return len_max


words = input().split()

res = find_max(words)
print(res)

