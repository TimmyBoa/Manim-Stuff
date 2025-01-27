import numpy as np
from manim import *

class Visualization(Scene):
    def construct(self):
        # Define control points
        P0 = np.array([-3, -1, 0])
        P1 = np.array([-1, 2, 0])
        P2 = np.array([1, -2, 0])
        P3 = np.array([3, 1, 0])
        points = [P0, P1, P2, P3]
        dots = VGroup(*[Dot(point) for point in points])
        labels = VGroup(*[MathTex(rf"P_{{{i}}}", font_size=).next_to(point, DOWN) for i, point in enumerate(points)])
        
        # Add control points and labels to the scene
        self.play(Create(dots), Write(labels))
        self.wait(1)
        
        # Animate the progression along the curve
        t_tracker = ValueTracker(0)
        
        def get_interpolated_point(t):
            return (P3 * ((-t + 1) ** 3) + 
                    P2 * (-3 * ((-t + 1) ** 3) + 3 * ((-t + 1) ** 2)) + 
                    P1 * (-3 * t ** 3 + 3 * t ** 2) + 
                    P0 * (t ** 3))
        
        def get_lines(t):
            A = (1-t) * P0 + t * P1
            B = (1-t) * P1 + t * P2
            C = (1-t) * P2 + t * P3
            D = (1-t) * A + t * B
            E = (1-t) * B + t * C
            F = (1-t) * D + t * E
            lines = VGroup(
                Line(P0, P1, color=BLUE),
                Line(P1, P2, color=BLUE),
                Line(P2, P3, color=BLUE),
                Line(A, B, color=GREEN),
                Line(B, C, color=GREEN),
                Line(D, E, color=RED),
                Dot(F, color=YELLOW)
            )
            return lines
        
        lines = always_redraw(lambda: get_lines(t_tracker.get_value()))
        
        # Progression indicator
        progression_text = always_redraw(lambda: Text(f"t = {t_tracker.get_value():.2f}", font_size=36).to_edge(UP))
        
        # Plot the actual Bézier curve function
        bezier_curve = ParametricFunction(
            lambda t: P3 * ((-t + 1) ** 3) + 
                      P2 * (-3 * ((-t + 1) ** 3) + 3 * ((-t + 1) ** 2)) + 
                      P1 * (-3 * t ** 3 + 3 * t ** 2) + 
                      P0 * (t ** 3),
            t_range=[0, 1],
            color=WHITE
        )
        
        self.play(Create(bezier_curves), run_time=1.5)
        self.play(Create(lines), Write(progression_text), run_time=1.5)
        self.play(t_tracker.animate.set_value(1), run_time=5, rate_func=linear)
        self.wait(2)
        self.play(FadeOut(dots), FadeOut(labels), FadeOut(lines), FadeOut(progression_text), FadeOut(bezier_curve))

# Run the scene
if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    config.verbosity = "WARNING"
    scene = Visualization()
    scene.render()