weights=[]
for i in range(0,10):
  weight=float(input(f"enter weight of user {i+1},"))
  weights.append(weight)
avg_weight=sum(weights)/len(weights)
min_weight=min(weights)
max_weight=max(weights)
print(f"average_weight{avg_weight}")
print(f"max_weight{max_weight}")
print(f"min_weight{min_weight}")