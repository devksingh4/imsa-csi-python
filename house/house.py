# Dev Singh, House, 4/9/2020
from graphics import GraphWin, Rectangle, Point, Polygon, Text
import time # allows me to sleep the program


def main():
    win = GraphWin("House", 600, 600)
    win.setCoords(0,0,600,600)
    Text(Point(300,10),"5 Click House").draw(win)
    # Draw the main house
    p1 = win.getMouse()
    p2 = win.getMouse()
    Rectangle(p1, p2).draw(win)

    # Draw the door
    con = (abs(p1.x) - (p2.x)) / 5
    p3 = win.getMouse()
    d1 = Point(p3.x + con / 2, p3.y)
    d2 = Point(p3.x - con / 2, p1.y)
    Rectangle(d1, d2).draw(win)

    # Draw the window
    p4 = win.getMouse()
    w1 = Point(p4.x - con / 4, p4.y + con / 4)
    w2 = Point(p4.x + con / 4, p4.y - con / 4)
    Rectangle(w1, w2).draw(win)

    p5 = win.getMouse()
    Polygon(p2, Point(p1.x, p2.y), p5).draw(win)

    Text(Point(300,590),"I hoped you liked my house!!").draw(win)
    time.sleep(10) # sleep the thread for 10 seconds

main()