from manim import *

class seq4d_04(Scene):
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


        f_dot = Dot(color = GREEN_D)
        f_dot.add_updater(lambda d_ : d_.move_to(saloon.get_center() + stretch_factor * (3 - 2 * x1_val.get_value() - 4 * x2_val.get_value()) * RIGHT))
        self.play(Create(f_dot))
        x2_f_line = Line(x2_dot.get_center(), f_dot.get_center()).set_color(GREEN_D)
        self.play(Create(x2_f_line))
        f_txt = Tex('$(F)$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.6 * UP)
        f_pos_txt = Tex('$3000 - 4x_{1} - 2x_{2}$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.3 * UP)
        self.play(Write(f_txt), Write(f_pos_txt))
        self.wait()

        qs_txt = Tex('$Q(S)$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)
        qx1_txt = Tex('$Q(D1)$').set_color(YELLOW_C).scale(0.4).move_to(x1_dot.get_center() + 0.25 * UP)
        x1x2_txt = Tex('$Q(D2)$').set_color(YELLOW_C).scale(0.4).move_to(x2_dot.get_center() + 0.25 * UP)
        self.add(qs_txt, qx1_txt, x1x2_txt)

        constraint_txt = Tex('\\underline{Contraintes} :').scale(0.6).next_to(saloon, direction=DOWN, aligned_edge=ORIGIN, buff=LARGE_BUFF).to_edge(LEFT)
        self.add(constraint_txt)

        a_txt = Tex("$(A)$ : Les distances $x_{1}$ et $x_{2}$ sont positives.").scale(0.4).next_to(constraint_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        a1_txt = Tex('$(a1)$').scale(0.4).next_to(a_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        a2_txt = Tex('$(a2)$').scale(0.4).next_to(a1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        a1_formula_txt = Tex('$x_{1} \\geq 0$').set_color(TEAL_D).scale(0.4).next_to(a1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        a2_formula_txt = Tex('$x_{2} \\geq 0$').set_color(RED_D).scale(0.4).next_to(a2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.add(a_txt, a1_txt, a2_txt, a1_formula_txt, a2_formula_txt)
        
        b_txt = Tex("$(B)$ : Les distances $x_{1}$ et $x_{2}$ permettent de faire des allers-retours.").scale(0.4).next_to(a2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        b1_txt = Tex('$(b1)$').scale(0.4).next_to(b_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        b2_txt = Tex('$(b2)$').scale(0.4).next_to(b1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        b1_formula_txt = Tex('$x_{1} \\leq 500$').set_color(TEAL_D).scale(0.4).next_to(b1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        b2_formula_txt = Tex('$x_{2} \\leq 500$').set_color(RED_D).scale(0.4).next_to(b2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.add(b_txt, b1_txt, b2_txt, b1_formula_txt, b2_formula_txt)

        c_txt = Tex('$(C)$ : Un aller-retour et un aller simple entre $(D1)$ et $(D2)$').scale(0.4).next_to(b2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        c1_txt = Tex('$(c1)$').scale(0.4).next_to(c_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        c2_txt = Tex('$(c2)$').scale(0.4).next_to(c1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        c1_formula_txt = Tex('$Q(D1) \\geq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        c2_formula_txt = Tex('$Q(D1) \\leq 2000$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.add(c_txt, c1_txt, c2_txt, c1_formula_txt, c2_formula_txt)

        d_txt = Tex('$(D)$ : Un seul trajet partant de $(D2)$ vers la position finale').scale(0.4).next_to(c2_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        d1_txt = Tex('$(d1)$').scale(0.4).next_to(d_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        d2_txt = Tex('$(d2)$').scale(0.4).next_to(d1_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        d1_formula_txt = Tex('$Q(D2) \\geq 0$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        d2_formula_txt = Tex('$Q(D2) \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.add(d_txt, d1_txt, d2_txt, d1_formula_txt, d2_formula_txt)
        self.wait()

        axes = Axes(x_range = (-50, 550, 100), y_range = (-50, 550, 100), x_length=5,y_length=5, tips = False).shift(3 * RIGHT + 0.75 * DOWN)
        axes.add_coordinates()
        axes.get_x_axis().set_color(TEAL_D)
        axes.get_y_axis().set_color(RED_D)
        x_lab = MathTex(r"x_{1}").set_color(TEAL_D).scale(0.6).next_to(axes.get_x_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        y_lab = MathTex(r"x_{2}").set_color(RED_D).scale(0.6).next_to(axes.get_y_axis().get_end(), aligned_edge=UL, buff=SMALL_BUFF)
        self.add(axes, x_lab, y_lab)

        region0 = Polygon(
            axes.c2p(-100, -100),
            axes.c2p(600, -100),
            axes.c2p(600, 600),
            axes.c2p(-100, 600),
            fill_color = PURPLE,
            fill_opacity = 0.2
            ).set_color(PURPLE_E)
        
        plot_01 = Line(axes.c2p(0, -100), axes.c2p(0, 600)).set_stroke(TEAL_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_01 = Tex("$x_{1} \\geq 0$").set_color(TEAL_D).scale(0.4).next_to(plot_01.get_end(), UR, buff = SMALL_BUFF)

        region1 = Polygon(
            axes.c2p(0, -100),
            axes.c2p(600, -100),
            axes.c2p(600, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.25
            ).set_color(PURPLE_E)     
        
        plot_12 = Line(axes.c2p(-100, 0), axes.c2p(600, 0)).set_stroke(RED_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_12 = Tex("$x_{2} \\geq 0$").set_color(RED_D).scale(0.4).next_to(plot_12.get_end(), UR, buff = SMALL_BUFF)

        region2 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(600, 0),
            axes.c2p(600, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.3
            ).set_color(PURPLE_E)

        plot_23 = Line(axes.c2p(500, -100), axes.c2p(500, 600)).set_stroke(TEAL_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_23 = Tex("$x_{1} \\leq 500$").set_color(TEAL_D).scale(0.4).next_to(plot_23.get_end(), UR, buff = SMALL_BUFF)     
        
        region3 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(500, 0),
            axes.c2p(500, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.35
            ).set_color(PURPLE_E)   

        plot_34 = Line(axes.c2p(-100, 500), axes.c2p(600, 500)).set_stroke(RED_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_34 = Tex("$x_{2} \\leq 500$").set_color(RED_D).scale(0.4).next_to(plot_34.get_end(), UR, buff = SMALL_BUFF)          
        
        region4 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(500, 0),
            axes.c2p(500, 500),
            axes.c2p(0, 500),
            fill_color = PURPLE,
            fill_opacity = 0.4
            ).set_color(PURPLE_E)
        
        plot_45 = Line(axes.c2p(400, -100), axes.c2p(400, 600)).set_stroke(TEAL_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_45 = Tex("$x_{1} \\leq 400$").set_color(TEAL_D).scale(0.4).next_to(plot_45.get_end(), UR, buff = SMALL_BUFF)

        region5 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 500),
            axes.c2p(0, 500),
            fill_color = PURPLE,
            fill_opacity = 0.45
        ).set_color(PURPLE_E)
        
        plot_56 = Line(axes.c2p(200, -100), axes.c2p(200, 600)).set_stroke(TEAL_D, DEFAULT_STROKE_WIDTH * 0.4)
        label_56 = Tex("$x_{1} \\geq 200$").set_color(TEAL_D).scale(0.4).next_to(plot_56.get_end(), UR, buff = SMALL_BUFF)

        region6 = Polygon(
            axes.c2p(200, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.5
        ).set_color(PURPLE_E)

        # 5x + 3y = 3000
        plot_67 = axes.plot(
                lambda x_: 1000 - (5/3) * x_,
                x_range=[300, 400],
                color=PURPLE_D
            ).set_stroke(width=DEFAULT_STROKE_WIDTH * 0.4)
        label_67 = Tex("$5x_{1} + 3x_{2} = 3000$").set_color(PURPLE_D).scale(0.4).next_to(plot_67.get_end(), UR, buff = SMALL_BUFF)

        region7 = Polygon(
            axes.c2p(200, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 1000/3),
            axes.c2p(300, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.55
        ).set_color(PURPLE_E)

        # 5x + 3y = 2000
        plot_78 = axes.plot(
                lambda x_: (2000 - 5 * x_) / 3,
                x_range=[200, 400],
                color=PURPLE_D
            ).set_stroke(width=DEFAULT_STROKE_WIDTH * 0.4)
        label_78 = Tex("$5x_{1} + 3x_{2} = 2000$").set_color(PURPLE_D).scale(0.4).next_to(plot_78.get_end(), UR, buff = SMALL_BUFF)

        region8 = Polygon(
            axes.c2p(200, 1000/3),
            axes.c2p(400, 0),
            axes.c2p(400, 1000/3),
            axes.c2p(300, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.6
        ).set_color(PURPLE_E)

        self.add(region0)
        self.wait()
        self.add(plot_01, label_01)
        self.play(Transform(region0, region1))
        self.remove(plot_01, label_01)

        self.add(plot_12, label_12)
        self.play(Transform(region0, region2))
        self.remove(plot_12, label_12)

        self.add(plot_23, label_23)
        self.play(Transform(region0, region3))
        self.remove(plot_23, label_23)

        self.add(plot_34, label_34)
        self.play(Transform(region0, region4))
        self.remove(plot_34, label_34)

        self.play(Transform(c1_formula_txt, Tex('$3000 - 5x_{1} \\geq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(c1_formula_txt, Tex('$x_{1} \\leq 400$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.add(plot_45, label_45)
        self.play(Transform(region0, region5))
        self.remove(plot_45, label_45)

        self.play(Transform(c2_formula_txt, Tex('$3000 - 5x_{1} \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(c2_formula_txt, Tex('$x_{1} \\geq 200$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.add(plot_56, label_56)
        self.play(Transform(region0, region6))
        self.remove(plot_56, label_56)

        self.play(Transform(d1_formula_txt, Tex('$3000 - 5x_{1} - 3x_{2} \\geq 0$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(d1_formula_txt, Tex('$5x_{1} + 3x_{2} \\leq 3000$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.add(plot_67, label_67)
        self.play(Transform(region0, region7))
        self.remove(plot_67, label_67)

        self.play(Transform(d2_formula_txt, Tex('$3000 - 5x_{1} - 3x_{2} \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(d2_formula_txt, Tex('$5x_{1} + 3x_{2} \\geq 2000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.add(plot_78, label_78)
        self.play(Transform(region0, region8))
        self.remove(plot_78, label_78)
        self.wait()