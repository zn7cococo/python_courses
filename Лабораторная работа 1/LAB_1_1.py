numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

n = list.index(numbers, None)
numbers_new = (sum(numbers[:n])+sum(numbers[n+1:]))/len(numbers)
print("Измененный список:", numbers[:n]+[numbers_new]+numbers[n+1:])
