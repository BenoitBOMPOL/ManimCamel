from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)

        axes = Axes(x_range = (0, 8, 1), y_range = (0.00, 1.25, 0.25), tips = False)
        axes.add_coordinates()
        self.play(Create(axes))
        inv_func = axes.plot(lambda x_ : 1 / x_, x_range = [1, 7]).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.5)
        self.play(Create(inv_func))
        self.wait()

        k_val = ValueTracker(1.0)

        upper_area_poly = always_redraw(
            lambda: Polygon(
                axes.c2p(k_val.get_value(), 0),
                axes.c2p(k_val.get_value() + 1, 0),
                axes.c2p(k_val.get_value() + 1, 1/k_val.get_value()),
                axes.c2p(k_val.get_value(), 1/k_val.get_value()),
                fill_color = LOGO_BLUE,
                fill_opacity = 0.8
            ).set_color(LOGO_BLUE)
        )
        up_sq = Square(side_length = 0.5).set_color(LOGO_BLUE).set_fill(LOGO_BLUE, 0.8).move_to(3.5 * RIGHT + 3 * UP)
        up_area_txt = always_redraw(lambda: DecimalNumber(
            (1 / (k_val.get_value())),
            num_decimal_places=3
        ).set_color(LOGO_BLUE).scale(0.7).next_to(up_sq, RIGHT, buff=SMALL_BUFF))

        area_under_curve = always_redraw(lambda: axes.get_area(
            graph=inv_func,
            x_range=(k_val.get_value(), k_val.get_value() + 1),
            color=WHITE,
            opacity=0.8
        ).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.5))
        auc_sq = Square(side_length = 0.5).set_color(WHITE).set_fill(WHITE, 0.8).move_to(3.5 * RIGHT + 2.5 * UP)
        auc_area_txt = always_redraw(
            lambda: DecimalNumber(
                np.log(1 + (1/k_val.get_value())),
                num_decimal_places = 3
            ).set_color(WHITE).scale(0.7).next_to(auc_sq, RIGHT, buff = SMALL_BUFF)
        )

        lower_area_poly = always_redraw(
            lambda: Polygon(
                axes.c2p(k_val.get_value(), 0),
                axes.c2p(k_val.get_value() + 1, 0),
                axes.c2p(k_val.get_value() + 1, 1/(k_val.get_value() + 1)),
                axes.c2p(k_val.get_value(), 1/(k_val.get_value() + 1)),
                fill_color = LOGO_RED,
                fill_opacity = 0.8
            ).set_color(LOGO_RED)
        )

        lw_sq = Square(side_length = 0.5).set_color(LOGO_RED).set_fill(LOGO_RED, 0.8).move_to(3.5 * RIGHT + 2 * UP)
        lw_area_txt = always_redraw(lambda: DecimalNumber(
            (1 / (1 + k_val.get_value())),
            num_decimal_places=3
        ).set_color(LOGO_RED).scale(0.7).next_to(lw_sq, RIGHT, buff=SMALL_BUFF))

        self.play(Create(upper_area_poly), Create(up_sq), Write(up_area_txt))
        self.play(Create(area_under_curve), Create(auc_sq), Write(auc_area_txt))
        self.play(Create(lower_area_poly), Create(lw_sq), Write(lw_area_txt))
        self.play(k_val.animate.set_value(k_val.get_value() + 5), run_time = DEFAULT_WAIT_TIME * 2.5)
        self.wait()
        self.remove(axes)
        axes = Axes(x_range = (0, 8, 1), y_range = (0.00, 1.25, 0.25))
        self.add(axes)
        self.play(k_val.animate.set_value(2))
        k_txt = Tex('$k$').scale(0.6).next_to(axes.c2p(2, 0), direction = DOWN, buff = MED_SMALL_BUFF)
        kpp_txt = Tex('$k + 1$').scale(0.6).next_to(axes.c2p(3, 0), direction = DOWN, buff = MED_SMALL_BUFF)
        inv_kpp_txt = Tex('$\\frac{1}{k+1}$').set_color(LOGO_RED).scale(0.6).next_to(axes.c2p(0, 1/3), direction = LEFT, buff = MED_SMALL_BUFF)
        inv_txt = Tex('$\\frac{1}{k}$').set_color(LOGO_BLUE).scale(0.6).next_to(axes.c2p(0, 1/2), direction = LEFT, buff = MED_SMALL_BUFF)
        inv_kpp_line = Line(axes.c2p(0, 1/3), axes.c2p(2, 1/3)).set_color(LOGO_RED).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        inv_k_line = Line(axes.c2p(0, 1/2), axes.c2p(2, 1/2)).set_color(LOGO_BLUE).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        self.play(Write(k_txt), Write(kpp_txt))

        self.remove(up_area_txt)
        up_area_txt = Tex('$\\frac{1}{k} \\times ((k + 1) - k)$').set_color(LOGO_BLUE).scale(0.7).next_to(up_sq, RIGHT, buff=SMALL_BUFF)
        self.play(Write(inv_txt), Create(inv_k_line), Write(up_area_txt))

        self.remove(lw_area_txt)
        lw_area_txt = Tex('$\\frac{1}{k + 1} \\times ((k + 1) - k)$').set_color(LOGO_RED).scale(0.7).next_to(lw_sq, RIGHT, buff=SMALL_BUFF)
        self.play(Write(inv_kpp_txt), Create(inv_kpp_line), Write(lw_area_txt))


        self.remove(auc_area_txt)
        auc_area_txt = Tex('?').set_color(WHITE).scale(0.7).next_to(auc_sq, RIGHT, buff=SMALL_BUFF)
        self.play(
            Transform(
                up_area_txt,
                Tex('$\\frac{1}{k}$').set_color(LOGO_BLUE).scale(0.7).next_to(up_sq, RIGHT, buff = SMALL_BUFF)
            ),
            Write(auc_area_txt),
            Transform(
                lw_area_txt,
                Tex('$\\frac{1}{k+1}$').set_color(LOGO_RED).scale(0.7).next_to(lw_sq, RIGHT, buff = SMALL_BUFF)
            )
        )

        self.remove(k_txt, kpp_txt, inv_txt, inv_kpp_txt, inv_k_line, inv_kpp_line)
        lb_group = Group(lw_sq, lw_area_txt)
        auc_group = Group(auc_sq, auc_area_txt)
        ub_group = Group(up_sq, up_area_txt)
        self.wait()
        self.play(auc_group.animate.move_to(ORIGIN))
        self.play(
            Transform(
                auc_area_txt,
                Tex('\\textrm{Aire}($t\\mapsto \\frac{1}{t}, t \\in [k, k+1]$)').scale(0.7).next_to(auc_sq, direction = RIGHT, buff = SMALL_BUFF)
            )
        )
        self.wait()
        self.play(
            Transform(
                auc_area_txt,
                Tex('$\\int_{k}^{k+1}\\frac{\\mathrm{d}t}{t}$').scale(0.7).next_to(auc_sq, direction = RIGHT, buff = SMALL_BUFF)
            )
        )
        self.wait()
        self.play(
            Transform(
                auc_area_txt,
                Tex('$\\ln(k + 1) - \\ln(k)$').scale(0.7).next_to(auc_sq, direction = RIGHT, buff = SMALL_BUFF)
            )
        )
        self.wait()
        self.play(
            lb_group.animate.next_to(auc_group, direction = LEFT, buff = MED_LARGE_BUFF),
            ub_group.animate.next_to(auc_group, direction = RIGHT, buff = MED_LARGE_BUFF)    
        )
        self.wait()
        comp_tex = Tex('$\\boxed{\\frac{1}{k + 1} \\leq \\ln(k + 1) - \\ln(k) \\leq \\frac{1}{k}}$').set_color(BRAT_GREEN).to_edge(UP)
        self.play(Write(comp_tex))
        self.wait()