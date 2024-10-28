"""Faqat bitta elementli ro'yxat yaratish. Ro'yxatdan barcha elementlarni o'chirib faqat bitta elementni
qoldiring.
fruits=["apple", "banana", "cherry", "date", "elderberry"]
Natija: ["banana"]"""

fruits=["apple", "banana", "cherry", "date", "elderberry"]

del fruits[2:]
del fruits[0:1]

print(fruits)