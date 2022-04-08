# Hasta ahora todos los elementos primitivos que hemos manejado
# Listas, Diccionarios, Strings, Numbers, etc tienen un cierto tipo
# que vemos con el método especial type()
# 
print(type(1))
print(type(['a','b','c']))
print(type(True)) 
print(type("Hello World"))

class Point:
    def reset(self):
        self.x = 0
        self.y = 0
    def move(self,x,y):
        self.x = x
        self.y = y    

point1 = Point() 
point2 = Point()


point1.move(5,4) 

point2.move(3,6) 

print(type(point1))

print(point1.x, point1.y)

point1.reset()
print(point1.x, point1.y)