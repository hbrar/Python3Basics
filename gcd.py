x = 24
y = 60
def gcd(dvr, dvd):
    r = dvd % dvr
    if r == 0:
        return dvr
    else:
      return  gcd(r, dvr)
    
print(gcd(min(x,y),max(x,y)))