"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Jacob Bowman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math as m

def main():
    print_sequence1()
    print_sequence1f(20)
    draw_circles1()
    draw_circles_r(20)
    print_sequence2()
    print_sequence2f(17)
    draw_circles2()
    draw_circle_coor(17)
    print_sequence3()
    print_sequence3f(100)
    draw_circles3()
    draw_circles_r3(100)
    print_cosines()
    cosf(100)
    draw_cosines_and_sines()
    draw_cos_sin_circles(100)
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def print_sequence1():
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')


def print_sequence1f(n):
    for k in range(n + 1):
        print(k * 10)


def draw_circles1():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')


def draw_circles_r(n):
    window = rg.RoseWindow(400, 400)
    for k in range(n + 1):
        circle = rg.Circle(rg.Point(200, 200), 10 * k)
        circle.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def print_sequence2():
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')


def print_sequence2f(n):
    for k in range(n+1):
        print(50 + (k * 20))


def draw_circles2():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')


def draw_circle_coor(n):
    window2 = rg.RoseWindow(400, 400)
    for k in range(n + 1):
        point_coor = rg.Point(50 + (k * 20), 100)
        circle2 = rg.Circle(point_coor, 10)
        circle2.fill_color = 'blue'
        circle2.attach_to(window2)
    window2.render()
    window2.close_on_mouse_click()


def print_sequence3():
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # ------------------------------------------------------------------
    # DONE: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')


def print_sequence3f(n):
    for k in range(n):
        print(k + 1)


def draw_circles3():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')


def draw_circles_r3(n):
    window3 = rg.RoseWindow(300, 300)
    for k in range(n):
        circle3r = (k + 1)
        circle3 = rg.Circle(rg.Point(200, 150), circle3r)
        circle3.attach_to(window3)
    window3.render()
    window3.close_on_mouse_click()


def print_cosines():
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # ------------------------------------------------------------------
    # DONE: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')


def cosf(n):
    for k in range(n + 1):
        print(80 * m.cos(k))


def draw_cosines_and_sines():
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')

def draw_cos_sin_circles(n):
    window4 = rg.RoseWindow(400, 400)
    for k in range(n + 1):
        point_2 = rg.Point(200 + (80 * m.cos(k)), 200 + (80 * m.sin(k)))
        circle_4 = rg.Circle(point_2, 10)
        circle_4.attach_to(window4)
    window4.render()
    window4.close_on_mouse_click()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
