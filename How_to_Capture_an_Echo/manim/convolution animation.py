import manim as mn 
from manim.utils import rate_functions
import numpy as np
from pathops.operations import _draw

class Integral(mn.Scene):
    def construct(self):
        plane1 = (
                mn.NumberPlane(x_range=[-5,5,1],
                               x_length=10,
                               y_range=[-0.5, 3,1],
                               y_length=3,
                               background_line_style={
                                   "stroke_opacity":0.0
                                   }
                               ).shift(mn.UP * 2)
                )

        plane2 = (
                mn.NumberPlane(x_range=[-5,5,1],
                               x_length=10,
                               y_range=[-0.5, 3,1],
                               y_length=3,
                               background_line_style={
                                   "stroke_opacity":0.0
                                   }
                               ).shift(mn.DOWN * 2)
                )
        
        k = mn.ValueTracker(-8)

        rect1 = mn.always_redraw(
                lambda: plane1.plot(
                    lambda x: 1,
                    x_range=[-1 + k.get_value(), 1 + k.get_value() ]
                    )
                )
        rect2 = mn.always_redraw(
                lambda: plane1.plot(
                    lambda x: 0,
                    x_range=[-5,-1 + k.get_value() ]
                    )
                )

        rect3 = mn.always_redraw(
                lambda: plane1.plot(
                    lambda x: 0,
                    x_range=[1 + k.get_value(), 5 ]
                    )
                )

        rect4 = mn.Line(
                start = plane1.c2p(-1 + k.get_value(), 0),
                end = plane1.c2p(-1 + k.get_value(), 1)
                )

        rect5 = mn.Line(
                start = plane1.c2p(1 + k.get_value(), 0),
                end = plane1.c2p(1 + k.get_value(), 1)
                )

        rect4.add_updater(lambda z: z.become(mn.Line(
            plane1.c2p(-1 + k.get_value(), 0),
            plane1.c2p(-1 + k.get_value(), 1)
            ))) 

        rect5.add_updater(lambda z: z.become(mn.Line(
            plane1.c2p(1 + k.get_value(), 0),
            plane1.c2p(1 + k.get_value(), 1)
            ))) 
        
        
        rect = mn.VGroup(rect1, rect2, rect3, rect4, rect5).set_color(mn.BLUE)
        
        # sq1 = mn.Square(color=mn.WHITE, le) ############

        self.add(plane1, plane2, rect)
        self.play(k.animate.set_value(8), run_time = 6, rate_func = mn.linear)
        self.wait()
        

class Brian(mn.Scene):
    def construct(self):

        k = mn.ValueTracker(-3)

        plane1 = (
                mn.NumberPlane(x_range=[-3,4,1],
                               x_length=5,
                               y_range=[-8, 9,2],
                               y_length=5,
                               ).add_coordinates()
                                .shift(mn.LEFT * 3.5)
                )

        func1 = plane1.plot(
                lambda x: (1/3) * x**3, 
                x_range=[-3,3],
                color = mn.RED_C
                )

        moving = mn.always_redraw(
                lambda: plane1.get_secant_slope_group(
                    x = k.get_value(),
                    graph=func1,
                    dx=0.05
                    )
                )

        dot = mn.always_redraw(
                lambda: mn.Dot().move_to(
                    plane1.c2p(k.get_value(), func1.underlying_function(k.get_value()))
                    )
                )

        plane2 = (
                mn.NumberPlane(x_range=[-3,4,1],
                               x_length=5,
                               y_range=[0,11,2],
                               y_length=5,
                               ).add_coordinates()
                                .shift(mn.RIGHT * 3.5)
                )

        func2 = mn.always_redraw(
                lambda: plane2.plot(
                    lambda x: x**2,
                    x_range=[-3, k.get_value()]
                    )
                )

        self.play(
                mn.LaggedStart(
                    mn.DrawBorderThenFill(plane1),
                    mn.Create(func1),
                    run_time = 5, 
                    lag_ratio= 0.5
                    )
                )

        self.add(moving, dot, func1,func2)
        self.play(k.animate.set_value(3), run_time = 15)
        self.wait()
