from manim import *

class seq3c_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(4 * LEFT + 2 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).move_to(saloon.get_center() + 0.25 * LEFT)
        
        x_point = Dot(color = TEAL).move_to(4 * RIGHT + 2 * UP)
        line = Line(saloon.get_center(), x_point.get_center())
        x_txt = Tex('$x$').set_color(TEAL).scale(0.8).next_to(x_point, direction=RIGHT, buff=SMALL_BUFF)
        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        self.add(saloon, s_txt, line, x_point, x_txt)
        self.add(camel)
        self.wait()

        remaining_bnn_txt = Tex('$(1000-x)+2\\times(1000-2x)$').scale(0.4).set_color(YELLOW_C).to_edge(LEFT)
        self.add(remaining_bnn_txt)

        simplification_step1 = Tex('$= 3000 - 5x \\mathbf{\\geq 0}$', color=YELLOW_C).scale(0.4).next_to(remaining_bnn_txt, RIGHT, buff=SMALL_BUFF)
        self.play(Write(simplification_step1))
        self.wait()

        unfold_rbnn_txt = Tex('$\\implies x \\leq \\frac{3000}{5} = 600 \\textrm{m}$', color=YELLOW_C).scale(0.4).next_to(simplification_step1, DOWN, buff=SMALL_BUFF, aligned_edge=LEFT)
        self.play(Write(unfold_rbnn_txt))
        self.wait()
        self.remove(background_image)
        self.remove(unfold_rbnn_txt, simplification_step1, remaining_bnn_txt)
        self.remove(*[saloon, s_txt, x_point, line, x_txt, camel])
        self.wait()
