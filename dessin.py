from turtle import *

color('red', 'blue')
begin_fill()
while True:

    forward(50)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()