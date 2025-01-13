#Tim
#12/14/24
#Testing Latex text within the manim libarary
from manim import *

class TransferFunction(Scene):
    def construct(self):
        #Title
        title_text = Text("Evaluting a Transfer Function in the Frequency Domain.", font_size=34)
        self.play(Write(title_text))
        self.play(Circumscribe(title_text, time_width=2, color=BLUE))
        self.play(Wait(1))
        self.play(FadeOut(title_text))

        #Initial Deriving Magntiude of Transfer Function
        a=MathTex(r"V_{out} = V_{in}\frac{R_{1}}{R_{1}+R_{2}+R_{3}}")
        voltage_divider_text = Text("Voltage divider equation for three resistors in series.", font_size=24).next_to(a,DOWN)
        b=MathTex(r"\frac{V_{out}}{V_{in}} = \frac{R_{1}}{R_{1}+R_{2}+R_{3}}")
        c=MathTex(r"\frac{V_{out}}{V_{in}} = \frac{z_{1}}{z_{1}+z_{2}+z_{3}}")
        impedence_text=Text("Plugging in impedence to find ratio of\nvoltage out over voltage in; in a band pass circuit.", font_size=24).next_to(c,DOWN)
        d=MathTex(r"H(j\omega)=\frac{z_{1}}{z_{1}+z_{2}+z_{3}} ")
        e=MathTex(r"H(j\omega) = \frac{R}{j\omega L+R+\frac{1}{j\omega C}}")
        magnitude_text=Text("Evaluating the magnitude of the transfer function.",font_size=24).next_to(e,DOWN)
        f=MathTex(r"\left\|H(j\omega)  \right\| = \sqrt{\frac{R}{j\omega L+R+\frac{1}{j\omega C}}\cdot \frac{R}{-j\omega L+R+\frac{1}{-j\omega C}}}")
        g=MathTex(r"\left\|H(j\omega)  \right\| = \frac{R^{2}}{\sqrt{-j^{2}\omega^2L^{2}+j\omega LR+\frac{j\omega L}{-j\omega C}-j\omega LR+R^{2}+\frac{R}{-j\omega C}+\frac{-j\omega L}{j\omega C}+\frac{R}{j\omega C}+\frac{1}{-j^{2}{\omega^{2}C^{2}}}}}",
                  font_size=24)
        h=MathTex(r"\left\|H(s)\right\|=\frac{R^{2}}{\sqrt{\omega^2L^{2}+\frac{-2L}{C}+R^{2}+\frac{1}{\omega^{2}C^{2}}}}")
        self.play(Write(a), Write(voltage_divider_text))
        self.wait(1)
        self.play(FadeOut(voltage_divider_text))
        self.play(ReplacementTransform(a,b))
        self.wait(1)
        self.play(ReplacementTransform(b,c))
        self.play(Write(impedence_text))
        self.wait(1)
        self.play(ReplacementTransform(c,d))
        self.wait(1)
        self.play(ReplacementTransform(d,e))
        self.wait(1)
        self.play(FadeOut(impedence_text))
        self.play(ReplacementTransform(e,f))
        self.play(Write(magnitude_text))
        self.wait(1)
        self.play(ReplacementTransform(f,g))
        self.wait(1)
        self.play(ReplacementTransform(g,h))
        self.play(FadeOut(magnitude_text))
        self.wait(1)
        self.play(Circumscribe(h, time_width=2, color=BLUE))

     

        