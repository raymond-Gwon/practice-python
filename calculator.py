def plus(a=0,b=0):
  return (a + b)

def minus(a=0,b=0):
  return (a - b)

def times(a=0,b=0):
  return (a * b)

def division(a=0,b=0):
  return (a / b)

def negative(a=0):
  return (-a)

def remind(a=0,b=0):
  return (a % b)
  
def ppower(a=0,b=0):
  return (a ** b)            

a=2
b=5

int(a)
int(b)

print(
  plus(a,b),
  minus(a,b),
  times(a,b),
  division(a,b),
  negative(a),
  remind(a,b),
  ppower(a,b)
)