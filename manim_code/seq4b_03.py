from manim import *

class seq4b_03(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        context_txt = Tex('Position finale du chameau : $2000 - 2x$').scale(0.6).to_corner(UL)

        line = Line(6 * LEFT, 6 * RIGHT).shift(3 * UP)
        s_dot = Dot(color = LIGHT_BROWN).move_to(6 * LEFT + 3 * UP)
        s_txt = Tex('$S$').scale(0.6).set_color(LIGHT_BROWN).next_to(s_dot, direction=DL, buff = SMALL_BUFF)
        f_dot = Dot().move_to(6 * RIGHT + 3 * UP)
        f_txt = Tex('$F$').scale(0.6).next_to(f_dot, direction=RIGHT, buff = SMALL_BUFF)
        x_dot = Dot(color = TEAL).move_to(3 * LEFT + 3 * UP)
        x_txt = Tex('$x$').scale(0.6).set_color(TEAL).next_to(x_dot, direction=DOWN, buff=SMALL_BUFF)

        constraint_txt = Tex('\\underline{Contraintes} :').scale(0.6).next_to(context_txt, direction=DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)

        a_txt = Tex('(\\textrm{a})').scale(0.6).next_to(constraint_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        a_formula_csttxt = Tex('$x\\geq 0$').scale(0.6).next_to(a_txt, direction=RIGHT, aligned_edge=UP, buff = SMALL_BUFF)
        
        b_txt = Tex('(\\textrm{b})').scale(0.6).next_to(a_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        b_formula_csttxt = Tex('$x\\leq500$').scale(0.6).next_to(b_txt, direction=RIGHT, aligned_edge=UP, buff = SMALL_BUFF)

        c_txt = Tex('(\\textrm{c})').scale(0.6).next_to(b_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        c_formula_csttxt = Tex('$x\\geq 333.33$').scale(0.6).next_to(c_txt, direction=RIGHT, aligned_edge=UP, buff = SMALL_BUFF)

        self.add(background_image)
        self.add(context_txt)
        self.add(line)
        self.add(s_dot, s_txt, x_dot, x_txt, f_dot, f_txt)
        self.add(constraint_txt)
        self.add(a_txt, a_formula_csttxt)
        self.add(b_txt, b_formula_csttxt)
        self.add(c_txt, c_formula_csttxt)

        self.remove(s_dot, s_txt, x_dot, x_txt, f_dot, f_txt, line)
        self.play(Transform(context_txt, Tex('$\\max 2000 - 2x$').scale(0.6).move_to(s_dot.get_center())))

        axes = Axes(x_range = (0, 1000, 250), y_range = (0, 2000, 500), tips = False).scale(0.6).shift(RIGHT)
        axes.add_coordinates()
        x_lab = axes.get_x_axis_label('x').scale(0.6).next_to(axes.get_x_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        y_lab = axes.get_y_axis_label('\\text{Position finale}').scale(0.6).next_to(axes.get_y_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        self.play(Write(axes), Write(x_lab), Write(y_lab))
        
        indic_dot = Dot(color = ORANGE).move_to(axes.c2p(500, 1000))

        x_domain = Line(axes.c2p(1000/3, 0), axes.c2p(500, 0)).set_color(GREEN_C)
        obj_func = axes.plot(lambda x_ : 2000 - 2 * x_, x_range=[0, 1000]).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)

        self.play(
            b_formula_csttxt.animate.set_color(GREEN_C),
            c_formula_csttxt.animate.set_color(GREEN_C),
        )
        self.play(
            Create(x_domain),
            Transform(obj_func, axes.plot(lambda x_ : 2000 - 2 * x_, x_range=[1000/3, 500]).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75))
        )
        opt_indic_dot = Star().set_color(ORANGE).set_fill(ORANGE, 1).scale(0.05).move_to(axes.c2p(1000/3, 4000/3))
        self.play(Create(indic_dot))
        self.play(Transform(context_txt, Tex('\\textbf{max} $2000 - 2x$').set_color(ORANGE).scale(0.6).move_to(s_dot.get_center())))
        self.play(indic_dot.animate.move_to(axes.c2p(1000/3, 4000/3)),
                  Transform(indic_dot, opt_indic_dot))

        opt_vlookout_line = Arrow(axes.c2p(1000/3, 4000/3), axes.c2p(1000/3, 0), buff = SMALL_BUFF, max_tip_length_to_length_ratio = 0.05).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        x_opt_txt = Tex('$x^{\\star}$').scale(0.4).move_to(axes.c2p(1000/3, -75))
        self.play(Create(opt_vlookout_line),Write(x_opt_txt))
        self.play(Write(Tex('$x^{\\star} = 333.33\\dots$').to_edge(DOWN)))
        self.wait()