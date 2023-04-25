input = [3, 3]

min_val = min(input)
max_val = max(input)

def gcd(max_val,min_val):
    if(min_val==0):
        return max_val
    else:
        return gcd(min_val, max_val%min_val)


print(gcd(min_val,max_val))