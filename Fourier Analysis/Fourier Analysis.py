# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:50:06 2024

@author: Tim
"""
from manim import * 
class FourierAnalysis(Scene):
    def construct(self):
        title = Text("Fourier Analysis in a Band-Pass Circuit", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        
        circuit_image=SVGMobject("Band_pass_filter.svg")
        circuit_image.scale(0.7).to_edge(LEFT)
        circuit_label = Text("Band Pass Filter", font_size=24).next_to(circuit_image,UP)
        
        input_signal = Axes(
            x_range = [0,10,1],
            y_range = [-2, 2, 1],
            axis_config={"include_numbers":True}
            ).add_coordinates()
        input_graph = input_signal.plot(lambda x : 2*np.sin(2*PI*x)+np.sin(6*PI*X), color=BLUE)
        input_label = Text("Input Signal",font_size=24).next_to(input_signal,UP)
        
        self.play(Create(input_signal), Write(input_label))
        self.play(Create(input_graph))
        self.wait(2)
        
        freq_axes = Axes(
            x_range = [0,10,1],
            y_range = [0, 3, 1],
            axis_config={"include_numbers":True}
            ).add_coordinates()
        freq_bars=VGroup(
            freq_axes.plot(lambda x:2 if x==2 else 0, color=GREEN),
            freq_axes.plot(lambda x:1 if x==6 else 0, color=GREEN),
            )
        freq_label= Text("Frequency Domain", font_size=24).next_to(freq_axes,UP)
        
        self.play(Fade(input_signal, input_graph))
        self.play(Create(freq_axes),Write(freq_label))
        self.play(Create(freq_axes))
        self.wait(2)
        
        filtered_signal = input_signal.plot(lambda x:2*np.sin(2*PI*X), color=RED)
        filtered_label = Text("Filtered Signal",font_size=24).next_to(input_signal, UP)
        
        self.play(FadeOut(freq_axes, freq_bars, freq_label))
        self.play(Create(input_signal),Write(filtered_label))
        self.play(Create(filtered_signal))
        self.wait(2)
        
        circuit_output_label = Text("Output from Band-Pass Circuit", font_size=24).next_to(circuit_image, DOWN)
        self.play(FadeOut(input_signal, filtered_signal, filtered_label))
        self.play(Write(circuit_output_label))
        self.play(FadeIn(filtered_signal))
        self.wait(2)
        
        conclusion=Text(
            "A band-pass circuit filters specfic frequencies\n"
            "by allowing components within a certain range to pass.",
            font_size=24).next_to(circuit_output_label, DOWN)
        self.play(Write(conclusion))
        self.wait(3)
    
            