if __name__ == "__main__":
  n, x = input().split()
  n = int(n)
  x = int(x)

  coupons = input().split()
  coupons = [int(i) for i in coupons]

  diff = abs(coupons[0] - x)
  winner_coupon = coupons[0]
  for i in range(1, len(coupons)):
    _diff = abs(coupons[i] - x)
    if _diff < diff:
      diff = _diff
      winner_coupon = coupons[i]
    elif _diff == diff:
      if coupons[i] < winner_coupon:
        winner_coupon = coupons[i]
  
  print(winner_coupon)
