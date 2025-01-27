import pandas as pd
from manim import *

class BezierCurveFromExcel(Scene):
    def construct(self):
        # Title and Formula
        formula = MathTex(r"B_{t}=\sum_{i=0}^{n}\left(\frac{n!}{i!\left(n-i\right)!}\right)\left(1-t\right)^{n-i}t^{i}P_{i}", font_size=36)
        title = Text("Bézier Curves formula in polynomial form to the nth degree", font_size=24).next_to(formula, DOWN)
        self.play(Write(formula), Write(title))
        self.wait(2)
        self.play(FadeOut(formula), FadeOut(title))

        # Define control points
        points = [LEFT, LEFT * 0.3 + 1.5 * UP, RIGHT + DOWN * 0.7, RIGHT * 3 + UP * 1.5]
        dots = VGroup(*[Dot(point) for point in points])
        labels = VGroup(*[MathTex(rf"P_{{{i}}}", font_size=18).next_to(point, DOWN) for i, point in enumerate(points)])
        
        # Create the Bézier curve
        bezier_curve = CubicBezier(*points)
        
        # Add control points and labels to the scene
        self.play(Create(dots), Write(labels))
        self.wait(1)
        
        # Add the Bézier curve to the scene
        self.play(Create(bezier_curve))
        self.wait(1)

        # Draw lines connecting the control points
        connecting_lines = VGroup()
        for i in range(len(points) - 1):
            line = Line(points[i], points[i + 1], color=BLUE)
            connecting_lines.add(line)
        self.play(Create(connecting_lines))
        self.wait(2)
        self.play(FadeOut(dots), FadeOut(labels), FadeOut(bezier_curve), FadeOut(connecting_lines))

        # Title
        title = Text(f"Example of what can be done using only Bézeir Curves", font_size=24)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Read control points from Excel file
        df = pd.read_excel("control_points.xlsx")

        # Create animation groups
        animations = []
        fade_out_animations = []
        all_elements = VGroup()

        # Iterate over each curve column
        for curve_index in range(1, 184):
            column_name = f'Curve{curve_index}'
            points = []
            for point in df[column_name][:4]:  # Only read up to row 5
                point = str(point).replace('(', '').replace(')', '')
                x, y = map(float, point.split(','))
                if ',' not in point:
                    print(f"Skipping invalid point: {point}")
                    continue
                try:
                    x, y = map(float, point.split(','))
                    points.append(np.array([x, y, 0]))
                except ValueError as e:
                    print(f"Error processing point {point}: {e}")
                    continue

            # Bezier Curve
            bezier_curve = CubicBezier(*points)
            animations.append(Create(bezier_curve))

            # fadeout animations
            fade_out_animations.append(FadeOut(bezier_curve))
            all_elements.add(bezier_curve)


        all_elements.scale(0.20).move_to(ORIGIN)
        # play all the animations
        self.play(AnimationGroup(*animations), lag_ration=0.2)
        self.wait(2)

        # Fade out all the curves
        self.play(AnimationGroup(*fade_out_animations), lag_ration=0.2)

# Run the scene
if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    config.verbosity = "WARNING"
    scene = BezierCurveFromExcel()
    scene.render()