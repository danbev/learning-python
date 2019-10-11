class Results(object):
     def __init__(self, contenders):
         self._places = [None]*contenders
     def __setitem__(self, place, data):
          self._places[place] = data
     def __getitem__(self, place):
          return self._places[place]

r = Results(3)
r[0] = 'Gold'
r[1] = 'Silver'
r[2] = 'Bronce'
print(r[2])
