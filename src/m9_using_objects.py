"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Emily Wilcox.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------

    window = rg.RoseWindow()
    circle1 = rg.Circle(rg.Point(100, 100), 20)
    circle1.fill_color = 'pink'
    circle2 = rg.Circle(rg.Point(200, 200), 55)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------

    windows = rg.RoseWindow()
    circle = rg.Circle(rg.Point(100, 100), 50)
    circle.fill_color = 'blue'
    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(200, 175))
    circle.attach_to(windows)
    rectangle.attach_to(windows)
    windows.render()
    windows.close_on_mouse_click()
    print('The thickness of the circle is:', circle.outline_thickness)
    print('The fill color is:', circle.fill_color)
    print('Point is:', circle.center)
    print('X Coordinate is:', circle.center.x)
    print('Y Coordinate is:', circle.center.y)
    print('The thickness of the square is:', rectangle.outline_thickness)
    print('The fill color is:', rectangle.fill_color)
    print('Point is:', rectangle.corner_1)
    print('X Coordinate:', rectangle.corner_1.x)
    print('Y Coordinate:', rectangle.corner_1.y)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.

    window2 = rg.RoseWindow(400, 400)
    line1 = rg.Line(rg.Point(100, 200), rg.Point(200, 200))
    line2 = rg.Line(rg.Point(200, 300), rg.Point(300, 300))
    line2.thickness = 10
    line1.attach_to(window2)
    line2.attach_to(window2)
    window2.render()
    window2.close_on_mouse_click()
    print(rg.Line.get_midpoint(line2))
    print('X coordinate:', rg.Line.get_midpoint(line2).x)
    print('Y Coordinate:', rg.Line.get_midpoint(line2).y)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
