# I used the paper resource (included in project root) to help design my calculations

import math

round_to_n = lambda x, n: round(x, -int(math.floor(math.log(x,10))) + (n - 1))

def perpendicularRectangles(h,w,l):
  #Rectangular plate to unequal rectangular plate
  #From a horizontal rectangle of W·L to adjacent vertical rectangle of H·L, with h=H/L and w=W/L.
  H = h/l
  W = w/l
  x = (1 + (H**2) + (W**2))
  y = (H**2) + (W**2)
  a = (1+(H**2))*(1+(W**2)) / x
  b = ((W**2) * x) / ((1 + (W**2)) * y)
  c = ((H**2) * x) / ((1 + (H**2)) * y)
  F = 1/(math.pi * W)
  F = F * ((H * math.atan(1/H)) + (W * math.atan(1/W)) - (math.sqrt(y) * math.atan(1/(math.sqrt(y)))) + (0.25*math.log(a*b**W**2 * c**H**2)))
  return(F)

def parallelDisks(r1,r2,H):
  #From a disc of radius R 1 to a coaxial parallel disc of radius R 2 at separation H, with r 1 =R 1 /H and r 2 =R 2 /H.
  r1 = r1 / H
  r2 = r2 / H
  x = 1 + (1 / r1**2) + (r2**2 / r1 **2)
  y = math.sqrt(x**2 - 4*(r2**2 / r1**2))
  F = (x - y) / 2
  return(F)

def parallelRectangle(w1,w2,H):
  x, y = w1/H, w2/H
  x1, y1 = math.sqrt(1 + (x**2)), math.sqrt(1 + (y**2))
  a = math.log( ((x1**2) * (y1**2)) / ((x1**2) + (y1**2) - 1) )
  b = (2*x*((y1*math.atan(x/y1))-math.atan(x)))
  c = (2*y*((x1*math.atan(y/x1))-math.atan(y)))
  F = (a+b+c) / (math.pi * x * y)
  return(F)

h = 2 # height of A2
w = 2 # length of A1
l = 2 # depth of A1
F = perpendicularRectangles(h,w,l)
print(round_to_n(F,5))

R1 = 1 # radius of disc one
R2 = 1 # radius of disc two
H = 1  # distance between the disks
F = parallelDisks(R1,R2, H)
print(round_to_n(F,4))

w1 = 1 # width of rectangle 
w2 = 1 # height of rectangle 
H = 1  # distance between rectangles
F=(parallelRectangle(w1,w2,H))
print(round_to_n(F,4))
