from manim import *

class seq4d_05(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 14 * RIGHT)

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

        dd1_txt = Tex('$(D1)$').set_color(TEAL_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x1_dot.get_center() + 0.6 * UP))
        dd2_txt = Tex('$(D2)$').set_color(RED_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x2_dot.get_center() + 0.6 * UP))
        
        self.play(Create(line), Create(saloon), Write(s_txt))
        self.wait()
        self.play(Create(s_x1_line), Create(x1_dot), Write(x1_txt), Write(dd1_txt))
        self.play(Create(x1_x2_line), Create(x2_dot), Write(x2_txt), Write(dd2_txt))
        self.wait()
        self.play(
            x1_val.animate.set_value(0.2),
            x2_val.animate.set_value(1/3)
        )
        self.play(
            elt_.animate.shift(3 * UP) for elt_ in [saloon, s_txt, line, x1_dot, x2_dot, s_x1_line, x1_x2_line, x1_txt, x2_txt, dd1_txt, dd2_txt]
        )

        f_dot = Dot(color = GREEN_D)
        f_dot.add_updater(lambda d_ : d_.move_to(saloon.get_center() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT))
        self.play(Create(f_dot))
        x2_f_line = Line(x2_dot.get_center(), f_dot.get_center()).set_color(GREEN_D)
        self.play(Create(x2_f_line))
        epsilon = 1e-6
        x2_f_line.add_updater(lambda l_:
            l_.put_start_and_end_on(
                saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT,
                saloon.get_center() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT + epsilon * RIGHT
            )
        )
        f_txt = Tex('$(F)$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.6 * UP)
        f_txt.add_updater(lambda t_ : t_.move_to(f_dot.get_center() + 0.6 * UP))

        f_pos_txt = Tex('$3000 - 4x_{1} - 2x_{2}$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.3 * UP)
        f_pos_txt.add_updater(lambda t_ : t_.move_to(f_dot.get_center() + 0.3 * UP))

        self.play(Write(f_txt), Write(f_pos_txt))
        self.wait()

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

        region1 = Polygon(
            axes.c2p(0, -100),
            axes.c2p(600, -100),
            axes.c2p(600, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.25
            ).set_color(PURPLE_E)     

        region2 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(600, 0),
            axes.c2p(600, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.3
            ).set_color(PURPLE_E)        
        
        region3 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(500, 0),
            axes.c2p(500, 600),
            axes.c2p(0, 600),
            fill_color = PURPLE,
            fill_opacity = 0.35
            ).set_color(PURPLE_E)        
        
        region4 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(500, 0),
            axes.c2p(500, 500),
            axes.c2p(0, 500),
            fill_color = PURPLE,
            fill_opacity = 0.4
            ).set_color(PURPLE_E)

        region5 = Polygon(
            axes.c2p(0, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 500),
            axes.c2p(0, 500),
            fill_color = PURPLE,
            fill_opacity = 0.45
        ).set_color(PURPLE_E)

        region6 = Polygon(
            axes.c2p(200, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.5
        ).set_color(PURPLE_E)

        region7 = Polygon(
            axes.c2p(200, 0),
            axes.c2p(400, 0),
            axes.c2p(400, 1000/3),
            axes.c2p(300, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.55
        ).set_color(PURPLE_E)

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
        self.play(Transform(region0, region1))
        self.play(Transform(region0, region2))
        self.play(Transform(region0, region3))
        self.play(Transform(region0, region4))

        self.play(Transform(c1_formula_txt, Tex('$3000 - 5x_{1} \\geq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(c1_formula_txt, Tex('$x_{1} \\leq 400$').set_color(YELLOW_C).scale(0.4).next_to(c1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))

        self.play(Transform(region0, region5))

        self.play(Transform(c2_formula_txt, Tex('$3000 - 5x_{1} \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(c2_formula_txt, Tex('$x_{1} \\geq 200$').set_color(YELLOW_C).scale(0.4).next_to(c2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))

        self.play(Transform(region0, region6))

        self.play(Transform(d1_formula_txt, Tex('$3000 - 5x_{1} - 3x_{2} \\geq 0$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(d1_formula_txt, Tex('$5x_{1} + 3x_{2} \\leq 3000$').set_color(YELLOW_C).scale(0.4).next_to(d1_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(region0, region7))
        
        self.play(Transform(d2_formula_txt, Tex('$3000 - 5x_{1} - 3x_{2} \\leq 1000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))
        self.play(Transform(d2_formula_txt, Tex('$5x_{1} + 3x_{2} \\geq 2000$').set_color(YELLOW_C).scale(0.4).next_to(d2_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)))

        self.play(Transform(region0, region8))
        self.wait()

        objectif_txt = Tex('\\underline{Objectif} : $\\max 3000 - 4x_{1} - 2x_{2}$').scale(0.6).next_to(constraint_txt, direction = UP, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(objectif_txt)

        intermedots = [Dot().scale(0.8).move_to(saloon.get_center() + (idx_ + 1) * stretch_factor * RIGHT + 3 * UP) for idx_ in range(2)]
        km_txts = [Text(f'{idx_ + 1} km').scale(0.25).move_to(saloon.get_center() + (idx_ + 1) * stretch_factor * RIGHT + 3.25 * UP) for idx_ in range(2)]
        self.play(
            *[Write(kmtxt_) for kmtxt_ in km_txts],
            *[Create(dot_) for dot_ in intermedots],
            Unwrite(dd1_txt), Unwrite(dd2_txt), Unwrite(s_txt), Unwrite(f_txt)
        )

        self.remove(x1_txt, x2_txt, f_pos_txt)
        x1_txt = always_redraw(lambda : Tex('$x_{1} = ' + f'{round(1000 * x1_val.get_value(), 2)}$').set_color(TEAL_D).scale(0.5)).add_updater(lambda t_ : t_.move_to(s_x1_line.get_center() + 0.25 * UP))
        x2_txt = always_redraw(lambda : Tex('$x_{2} = ' + f'{round(1000 * x2_val.get_value(), 2)}$').set_color(RED_D).scale(0.5)).add_updater(lambda t_ : t_.move_to(x1_x2_line.get_center() + 0.25 * UP))
        self.play(Write(x1_txt), Write(x2_txt))

        k_value = ValueTracker(700 + (100/3))
        obj_func = always_redraw(lambda: 
            axes.plot(
                lambda x_: (1500 - (k_value.get_value() / 2)) - 2 * x_,
                x_range=[max(0, 500 - 0.25 * k_value.get_value()), min(500, 750 - 0.25 * k_value.get_value())],
                color=GREEN_D
            ).set_stroke(width=DEFAULT_STROKE_WIDTH)
        )
        self.add(obj_func)

        points = [(400, 1000/3), (300, 500), (200, 500), (400, 0), (200, 1000/3)]

        f_pos_txt = always_redraw(lambda : Tex(f'${k_value.get_value() / 1000:.3f}$' + '\\textrm{km}').set_color(GREEN_D).scale(0.45)).add_updater(lambda t_ : t_.move_to(f_dot.get_center() + 0.3 * DOWN))
        for idxp_, (xp_, yp_) in enumerate(points):
            kp_ = 3000 - 4 * xp_ - 2 * yp_
            self.play(
                x1_val.animate.set_value(xp_ / 1000),
                x2_val.animate.set_value(yp_ / 1000),
                k_value.animate.set_value(kp_)
            )
            point_p = Dot().scale(0.6).set_color(GREEN_D).move_to(axes.c2p(xp_, yp_))
            self.add(point_p)
            if idxp_ == 0:
                self.add(f_pos_txt.move_to(f_dot.get_center() + 0.3 * DOWN))
            self.wait()

        x_opt_line = DashedLine(axes.c2p(200, 1000 / 3), axes.c2p(200, 0)).set_color(TEAL_D).set_stroke(TEAL_D, DEFAULT_STROKE_WIDTH * 0.8)
        x_opt_dot = Dot(color = TEAL_D).scale(0.8).move_to(axes.c2p(200, 0))
        x_opt_txt = Tex('$x_{1}^{\\star} = 200 \\textrm{m}$').set_color(TEAL_D).scale(0.4).next_to(x_opt_dot, UL, buff = SMALL_BUFF)
        y_opt_line = DashedLine(axes.c2p(200, 1000 / 3), axes.c2p(0, 1000 / 3)).set_color(RED_D).set_stroke(RED_D, DEFAULT_STROKE_WIDTH * 0.8)
        y_opt_dot = Dot(color = RED_D).scale(0.8).move_to(axes.c2p(0, 1000 / 3))
        y_opt_txt = Tex('$x_{2}^{\\star} = 333.33 \\textrm{m}$').set_color(RED_D).scale(0.4).next_to(y_opt_dot, LEFT, buff = SMALL_BUFF)
        self.play(Create(x_opt_line), Create(x_opt_dot), Write(x_opt_txt))
        self.play(Create(y_opt_line), Create(y_opt_dot), Write(y_opt_txt))
        self.wait()