# Exercise 2:
K=100000 #simulation rounds
n=100 #number of persons
same=0
for k in range(K):
  birthdays = np.random.randint(1,366,n) # Assign random birthdays (1 to 365 with the size of n)
  unique, counts = np.unique(birthdays,return_counts=True) # Count occurrences
  if np.any(counts >= 3):
    same += 1
result = same/K
print("Simulation result: ",result)