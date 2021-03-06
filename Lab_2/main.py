import pandas as pd

f = open('data.txt', 'r')
arr = f.readline().split(',')
f.close()
m1 = float(arr[0])
d1 = float(arr[1])
p1 = float(arr[2])
d2 = float(arr[3])
p2 = float(arr[4])
m2 = float(arr[5])
d21 = float(arr[6])
p21 = float(arr[7])
d22 = float(arr[8])
p22 = float(arr[9])
p33 = float(arr[10])
p34 = float(arr[11])
p31 = float(arr[12])
p32 = float(arr[13])
A = -m1 + 5 * (p1 * d1 + p2 * d2)
B = -m2 + 5 * (p21 * d21 + p22 * d22)
Ca = p33 * (-m1 + 4 * (p31 * d1 + p32 * d2)) + p34 * 0
Cb = p33 * (-m2 + 4 * (p31 * d21 + p32 * d22)) + p34 * 0
results = pd.DataFrame(list(zip(['Варіант А', 'Варіант Б', 'Варіант Ва', 'Варіант Вб', ], [A, B, Ca, Cb])))
results.columns = ['Стратегія', 'Очікуваний дохід']
print(results)
results.to_csv(r'Results.txt')
print('Найкращим є:', results['Очікуваний дохід'].max())
