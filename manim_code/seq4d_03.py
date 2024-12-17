from manim import *

class seq4d_03(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT + 3 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 12 * RIGHT)

        stretch_factor = 8

        x1_val = ValueTracker(0.2)
        x1_dot = Dot(color = TEAL_D)
        x1_dot.add_updater(lambda m : m.move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT))
        s_x1_line = Line(saloon.get_center(), x1_dot.get_center()).set_color(TEAL_D)
        s_x1_line.add_updater(lambda l_ : l_.put_start_and_end_on(saloon.get_center(), saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT))
        x1_txt = Tex('$x_{1}$').set_color(TEAL_D).scale(0.5).add_updater(lambda t_ : t_.move_to(s_x1_line.get_center() + 0.25 * UP))
        d1_txt = Tex('$(D1)$').set_color(TEAL_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x1_dot.get_center() + 0.6 * UP))

        self.add(line, saloon, s_txt)
        self.play(Create(s_x1_line), Create(x1_dot), Write(x1_txt), Write(d1_txt))
    
        x2_val = ValueTracker(1/3)
        x2_dot = Dot(color = RED_D)
        x2_dot.add_updater(lambda m : m.move_to(saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT))
        x2_txt = Tex('$x_{2}$').set_color(RED_D).scale(0.5).add_updater(lambda t_ : t_.move_to(x1_x2_line.get_center() + 0.25 * UP))
        x1_x2_line = Line(x1_dot.get_center(), x2_dot.get_center()).set_color(RED_D)
        x1_x2_line.add_updater(lambda l_ : l_.put_start_and_end_on(x1_dot.get_center(), x2_dot.get_center()))
        d2_txt = Tex('$(D2)$').set_color(RED_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x2_dot.get_center() + 0.6 * UP))

        self.play(Create(x1_x2_line), Create(x2_dot), Write(x2_txt), Write(d2_txt))
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

        constraint_txt = Tex('\\underline{Contraintes} :').scale(0.6).next_to(saloon, direction=DOWN, aligned_edge=ORIGIN, buff=LARGE_BUFF).to_edge(LEFT)
        self.play(Write(constraint_txt))

        a_txt = Tex("$(A)$ : Les distances $x_{1}$ et $x_{2}$ sont positives.").scale(0.4).next_to(constraint_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        a1_txt = Tex('$(a1)$').scale(0.4).next_to(a_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        a2_txt = Tex('$(a2)$').scale(0.4).next_to(a1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(a_txt, a1_txt, a2_txt)
        a1_formula_txt = Tex('$x_{1} \\geq 0$').set_color(TEAL_D).scale(0.4).next_to(a1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        a2_formula_txt = Tex('$x_{2} \\geq 0$').set_color(RED_D).scale(0.4).next_to(a2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.play(Write(a1_formula_txt), Write(a2_formula_txt))
        self.wait()
        
        b_txt = Tex("$(B)$ : Les distances $x_{1}$ et $x_{2}$ permettent de faire des allers-retours.").scale(0.4).next_to(a2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        b1_txt = Tex('$(b1)$').scale(0.4).next_to(b_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        b2_txt = Tex('$(b2)$').scale(0.4).next_to(b1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(b_txt, b1_txt, b2_txt)
        b1_formula_txt = Tex('$2x_{1} \\leq 1000$').scale(0.4).next_to(b1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        b2_formula_txt = Tex('$2x_{2} \\leq 1000$').scale(0.4).next_to(b2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.play(Write(b1_formula_txt), Write(b2_formula_txt))
        self.play(
            Transform(b1_formula_txt, Tex('$x_{1} \\leq 500$').set_color(TEAL_D).scale(0.4).next_to(b1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)),
            Transform(b2_formula_txt, Tex('$x_{2} \\leq 500$').set_color(RED_D).scale(0.4).next_to(b2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)),
        )
        self.wait()

        c_txt = Tex('$(C)$ : Un aller-retour et un aller simple entre $(D1)$ et $(D2)$').scale(0.4).next_to(b2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        c1_txt = Tex('$(c1)$').scale(0.4).next_to(c_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        c2_txt = Tex('$(c2)$').scale(0.4).next_to(c1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(c_txt, c1_txt, c2_txt)
        c1_formula_txt = Tex('$Q(D1) \\geq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        c2_formula_txt = Tex('$Q(D1) \\leq 2000$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.play(Write(c1_formula_txt), Write(c2_formula_txt))
        self.wait()

        d_txt = Tex('$(D)$ : Un seul trajet partant de $(D2)$ vers la position finale').scale(0.4).next_to(c2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        d1_txt = Tex('$(d1)$').scale(0.4).next_to(d_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        d2_txt = Tex('$(d2)$').scale(0.4).next_to(d1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(d_txt, d1_txt, d2_txt)
        d1_formula_txt = Tex('$Q(D2) \\geq 0$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        d2_formula_txt = Tex('$Q(D2) \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.play(Write(d1_formula_txt), Write(d2_formula_txt))
        self.wait()