from manim import *

class seq4d_01(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 12 * RIGHT)

        x1_val = ValueTracker(0.5)
        x2_val = ValueTracker(0.5)
        x1_dot = Dot(color = TEAL_D)
        x2_dot = Dot(color = RED_D)
        
        stretch_factor = 8
        x1_dot.add_updater(lambda m : m.move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT))
        x2_dot.add_updater(lambda m : m.move_to(saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT))
        
        s_x1_line = Line(saloon.get_center(), x1_dot.get_center()).set_color(TEAL_D)
        s_x1_line.add_updater(lambda l_ : l_.put_start_and_end_on(saloon.get_center(), x1_dot.get_center()))

        x1_x2_line = Line(x1_dot.get_center(), x2_dot.get_center()).set_color(RED_D)
        x1_x2_line.add_updater(lambda l_ : l_.put_start_and_end_on(x1_dot.get_center(), x2_dot.get_center()))

        x1_txt = Tex('$x_{1}$').set_color(TEAL_D).scale(0.5).add_updater(lambda t_ : t_.move_to(s_x1_line.get_center() + 0.25 * UP))
        x2_txt = Tex('$x_{2}$').set_color(RED_D).scale(0.5).add_updater(lambda t_ : t_.move_to(x1_x2_line.get_center() + 0.25 * UP))

        d1_txt = Tex('$(D1)$').set_color(TEAL_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x1_dot.get_center() + 0.6 * UP))
        d2_txt = Tex('$(D2)$').set_color(RED_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x2_dot.get_center() + 0.6 * UP))
        

        self.play(Create(line), Create(saloon), Write(s_txt))
        self.wait()
        self.play(Create(s_x1_line), Create(x1_dot), Write(x1_txt), Write(d1_txt))
        self.play(Create(x1_x2_line), Create(x2_dot), Write(x2_txt), Write(d2_txt))
        self.wait()
        self.play(
            x1_val.animate.set_value(1/5),
            x2_val.animate.set_value(1/3)
        )
        self.play(
            elt_.animate.shift(3 * UP) for elt_ in [saloon, s_txt, line, x1_dot, x2_dot, s_x1_line, x1_x2_line, x1_txt, x2_txt, d1_txt, d2_txt]
        )
        self.wait()

        qs_txt = Tex('$Q(S)$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)
        qx1_txt = Tex('$Q(D1)$').set_color(YELLOW_C).scale(0.4).move_to(x1_dot.get_center() + 0.25 * UP)
        x1x2_txt = Tex('$Q(D2)$').set_color(YELLOW_C).scale(0.4).move_to(x2_dot.get_center() + 0.25 * UP)
        self.play(Write(qs_txt),Write(qx1_txt),Write(x1x2_txt))
        self.wait()
        f_dot = Dot(color = GREEN_D)
        f_dot.add_updater(lambda d_ : d_.move_to(saloon.get_center() + stretch_factor * (3 - 2 * x1_val.get_value() - 4 * x2_val.get_value()) * RIGHT))
        self.play(Create(f_dot))
        x2_f_line = Line(x2_dot.get_center(), f_dot.get_center()).set_color(GREEN_D)
        self.play(Create(x2_f_line))
        f_txt = Tex('$(F)$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.6 * UP)
        self.play(Write(f_txt))
        self.wait()