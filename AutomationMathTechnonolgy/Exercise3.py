# Exercise 3:
K = 100000
n = 10
t = [20, 30, 40, 50]
count = 0
for k in range(K):
    # collectedCoupon = set()
    collectedCoupon = []

    for _ in range(t[1]):
        coupon = randint(1, n+1)  # Get a random coupon number between 1 and n
    #     collectedCoupon.add(coupon)  # Add coupon to the set (duplicates will be ignored)
        if coupon not in collectedCoupon:
            collectedCoupon.append(coupon)
        # print(collectedCoupon)
        if len(collectedCoupon) == n:  # If all coupons are collected, break the loop
            break
    
    # Check if we collected all coupons
    if len(collectedCoupon) == n:
        count += 1
result = count/K
print("Simulation result: ",result)