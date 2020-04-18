import matplotlib
from matplotlib import pyplot as plt
plt.title("Random plot", fontsize=16)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.bar([2,5,7,9,11,12],[2,5,7,9,11,12])
plt.show()

list1 = [1,2,3,4,5]

list2 = list(filter(lambda x: True if x > 3 else False, list1))
print(list2)