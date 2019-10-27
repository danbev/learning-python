
def doit():
  print("doit...")
  def inner(): 
    print("from inner...")
  inner()

doit()

