from manim import *
BRAT_GREEN = ManimColor("#8ACE00")

class seq7_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)

        stretch_factor : float = 5.0

        axes = Axes(x_range = (-50, 550, 100), y_range = (-50, 550, 100), x_length=5,y_length=5, tips = False).to_edge(LEFT)
        axes.add_coordinates()
        axes.get_x_axis().set_color(TEAL_D)
        axes.get_y_axis().set_color(RED_D)
        x_lab = MathTex(r"x_{1}").set_color(TEAL_D).scale(0.6).next_to(axes.get_x_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        y_lab = MathTex(r"x_{2}").set_color(RED_D).scale(0.6).next_to(axes.get_y_axis().get_end(), aligned_edge=UL, buff=SMALL_BUFF)
        self.play(Create(axes), Write(x_lab), Write(y_lab))

        polyhedra = Polygon(
            axes.c2p(200, 1000/3),
            axes.c2p(400, 0),
            axes.c2p(400, 1000/3),
            axes.c2p(300, 500),
            axes.c2p(200, 500),
            fill_color = PURPLE,
            fill_opacity = 0.6
        ).set_color(PURPLE_E)
        self.play(Create(polyhedra))
        self.wait()

        x1_val = ValueTracker(0.3)
        x2_val = ValueTracker(0.3)

        line = Line(ORIGIN, ORIGIN).next_to(axes, direction = RIGHT, aligned_edge = UP, buff = MED_LARGE_BUFF)
        line.add_updater(lambda l_ : l_.put_start_and_end_on(l_.get_start(), line.get_start() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT))
        or_dot = Dot().move_to(line.get_start())
        or_x1_line = Line(line.get_center(), line.get_center()).set_color(TEAL_D).add_updater(lambda l_ : l_.put_start_and_end_on(line.get_start(), line.get_start() + stretch_factor * x1_val.get_value() * RIGHT))
        x1_dot = Dot(color = TEAL_D).add_updater(lambda d_ : d_.move_to(line.get_start() + stretch_factor * x1_val.get_value() * RIGHT))
        x1_x2_line = Line(line.get_center(), line.get_center()).set_color(RED_D).add_updater(lambda l_ : l_.put_start_and_end_on(line.get_start() + stretch_factor * x1_val.get_value() * RIGHT, line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT))
        x2_dot = Dot(color = RED_D).add_updater(lambda d_ : d_.move_to(line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT))
        x1_txt = Tex('$x_{1}$').scale(0.6).set_color(TEAL_D).add_updater(lambda t_ : t_.move_to(or_x1_line.get_center() + 0.25 * UP))
        x2_txt = Tex('$x_{2}$').scale(0.6).set_color(RED_D).add_updater(lambda t_ : t_.move_to(x1_x2_line.get_center() + 0.25 * UP))
        f_dot = Dot(color = GREEN_D).add_updater(lambda d_ : d_.move_to(line.get_start() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT))
        axes_p12 = Dot(color = PURPLE).add_updater(lambda d_ : d_.move_to(axes.c2p(1000 * x1_val.get_value(), 1000 * x2_val.get_value())))
        self.add(line, or_dot)
        self.play(Create(or_x1_line), Create(x1_x2_line))
        self.play(Create(x1_dot), Create(x2_dot), Write(x1_txt), Write(x2_txt))
        self.play(Create(f_dot))
        self.play(Create(axes_p12))

        step9 = Line(
            line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 2.25 * DOWN,
            line.get_start() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT + 2.25 * DOWN
        )

        step9.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 2.25 * DOWN,
                line.get_start() + stretch_factor * (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * RIGHT + 2.25 * DOWN
            )
        )

        e1_dot = Dot(color = LIGHT_GRAY).scale(0.6).add_updater(lambda d_ : d_.move_to(line.get_start() + (2/3) * (1 - x1_val.get_value()) * stretch_factor * RIGHT))
        e2_dot = Dot(color = LIGHT_GRAY).scale(0.6).move_to(line.get_start() + 0.2 * stretch_factor * RIGHT)
        e0_tex = MathTex(r"E_{0}").scale(0.6).add_updater(lambda d_ : d_.move_to(line.get_start() + (3 - 4 * x1_val.get_value() - 2 * x2_val.get_value()) * stretch_factor * RIGHT + 0.5 * UP))
        e1_tex = MathTex(r"E_{1}").scale(0.6).add_updater(lambda d_ : d_.move_to(line.get_start() + (2/3) * (1 - x1_val.get_value()) * stretch_factor * RIGHT + 0.5 * UP))
        e2_tex = MathTex(r"E_{2}").scale(0.6).move_to(line.get_start() + 0.2 * stretch_factor * RIGHT + 0.5 * UP)
        e3_tex = MathTex(r"E_{3}").scale(0.6).move_to(line.get_start() + 0.5 * UP)
        self.add(e1_dot, e2_dot)
        self.play(Write(e0_tex), Write(e1_tex), Write(e2_tex), Write(e3_tex))

        step1_lhs = Line(
            line.get_start() + 0.25 * DOWN,
            line.get_start() + 0.25 * DOWN + 0.2 * stretch_factor * RIGHT
        )

        step1_rhs = Line(
            line.get_start() + 0.25 * DOWN + 0.2 * stretch_factor * RIGHT,
            line.get_start() + 0.25 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
        ).set_color(BRAT_GREEN)

        step1_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + 0.25 * DOWN + 0.2 * stretch_factor * RIGHT,
                line.get_start() + 0.25 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
            )
        ) 

        step2_lhs = Line(
            line.get_start() + 0.5 * DOWN,
            line.get_start() + 0.5 * DOWN + 0.2 * stretch_factor * RIGHT
        )
        step2_rhs = Line(
            line.get_start() + 0.5 * DOWN + 0.2 * stretch_factor * RIGHT,
            line.get_start() + 0.5 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
        ).set_color(BRAT_GREEN)
        step2_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + 0.5 * DOWN + 0.2 * stretch_factor * RIGHT,
                line.get_start() + 0.5 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
            )
        ) 

        step3_lhs = Line(
            line.get_start() + 0.75 * DOWN,
            line.get_start() + 0.75 * DOWN + 0.2 * stretch_factor * RIGHT
        )
        step3_rhs = Line(
            line.get_start() + 0.75 * DOWN + 0.2 * stretch_factor * RIGHT,
            line.get_start() + 0.75 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
        ).set_color(BRAT_GREEN)
        step3_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + 0.75 * DOWN + 0.2 * stretch_factor * RIGHT,
                line.get_start() + 0.75 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
            )
        )
        step4_lhs = Line(
            line.get_start() + 1.0 * DOWN,
            line.get_start() + 1.0 * DOWN + 0.2 * stretch_factor * RIGHT
        )
        step4_rhs = Line(
            line.get_start() + 1.0 * DOWN + 0.2 * stretch_factor * RIGHT,
            line.get_start() + 1.0 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
        ).set_color(BRAT_GREEN)
        step4_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + 1.0 * DOWN + 0.2 * stretch_factor * RIGHT,
                line.get_start() + 1.0 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
            )
        ) 

        step5_lhs = Line(
            line.get_start() + 1.25 * DOWN,
            line.get_start() + 1.25 * DOWN + 0.2 * stretch_factor * RIGHT
        )
        step5_rhs = Line(
            line.get_start() + 1.25 * DOWN + 0.2 * stretch_factor * RIGHT,
            line.get_start() + 1.25 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
        ).set_color(BRAT_GREEN)
        step5_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + 1.25 * DOWN + 0.2 * stretch_factor * RIGHT,
                line.get_start() + 1.25 * DOWN + 0.2 * stretch_factor * RIGHT + (x1_val.get_value() - 0.2) * stretch_factor * RIGHT
            )
        )

        step6_lhs = Line(
            line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 1.5 * DOWN,
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.5 * DOWN
        ).set_color(BRAT_GREEN)
        step6_lhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 1.5 * DOWN,
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.5 * DOWN
            )
        )
        step6_rhs = Line(
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.5 * DOWN,
            line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 1.5 * DOWN
        ).set_color(LOGO_BLUE)
        step6_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.5 * DOWN,
                line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 1.5 * DOWN
            )
        )

        step7_lhs = Line(
            line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 1.75 * DOWN,
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.75 * DOWN
        ).set_color(BRAT_GREEN)
        step7_lhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 1.75 * DOWN,
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.75 * DOWN
            )
        )
        step7_rhs = Line(
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.75 * DOWN,
            line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 1.75 * DOWN
        ).set_color(LOGO_BLUE)
        step7_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 1.75 * DOWN,
                line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 1.75 * DOWN
            )
        )

        step8_lhs = Line(
            line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 2.0 * DOWN,
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 2.0 * DOWN
        ).set_color(BRAT_GREEN)
        step8_lhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * x1_val.get_value() * RIGHT + 2.0 * DOWN,
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 2.0 * DOWN
            )
        )
        step8_rhs = Line(
            line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 2.0 * DOWN,
            line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 2.0 * DOWN
        ).set_color(LOGO_BLUE)
        step8_rhs.add_updater(
            lambda l_ : l_.put_start_and_end_on(
                line.get_start() + stretch_factor * (2/3) * (1 - x1_val.get_value()) * RIGHT + 2.0 * DOWN,
                line.get_start() + stretch_factor * (x1_val.get_value() + x2_val.get_value()) * RIGHT + 2.0 * DOWN
            )
        )

        step9.set_color(LOGO_BLUE)
        self.play(
            Create(step1_lhs), Create(step1_rhs),
            Create(step2_lhs), Create(step2_rhs),
            Create(step3_lhs), Create(step3_rhs),
            Create(step4_lhs), Create(step4_rhs),
            Create(step5_lhs), Create(step5_rhs),
            Create(step6_lhs), Create(step6_rhs),
            Create(step7_lhs), Create(step7_rhs),
            Create(step8_lhs), Create(step8_rhs),
            Create(step9)
        )
        self.wait()

        c_s1_lhs = step1_lhs.copy()
        c_s1_lhs.clear_updaters()
        c_s2_lhs = step2_lhs.copy()
        c_s2_lhs.clear_updaters()
        c_s3_lhs = step3_lhs.copy()
        c_s3_lhs.clear_updaters()
        c_s4_lhs = step4_lhs.copy()
        c_s4_lhs.clear_updaters()
        c_s5_lhs = step5_lhs.copy()
        c_s5_lhs.clear_updaters()
        c_s6_lhs = step6_lhs.copy()
        c_s6_lhs.clear_updaters()
        c_s7_lhs = step7_lhs.copy()
        c_s7_lhs.clear_updaters()
        c_s8_lhs = step8_lhs.copy()
        c_s8_lhs.clear_updaters()

        c_s1_rhs = step1_rhs.copy()
        c_s1_rhs.clear_updaters()
        c_s2_rhs = step2_rhs.copy()
        c_s2_rhs.clear_updaters()
        c_s3_rhs = step3_rhs.copy()
        c_s3_rhs.clear_updaters()
        c_s4_rhs = step4_rhs.copy()
        c_s4_rhs.clear_updaters()
        c_s5_rhs = step5_rhs.copy()
        c_s5_rhs.clear_updaters()
        c_s6_rhs = step6_rhs.copy()
        c_s6_rhs.clear_updaters()
        c_s7_rhs = step7_rhs.copy()
        c_s7_rhs.clear_updaters()
        c_s8_rhs = step8_rhs.copy()
        c_s8_rhs.clear_updaters()

        c_s9 = step9.copy()
        c_s9.clear_updaters()

        self.play(c_s1_lhs.animate.shift((2.5 + c_s1_lhs.get_start()[1]) * DOWN), run_time = 2/5)
        dot_1l = Dot().scale(0.6).move_to(c_s1_lhs.get_start() + 1 * stretch_factor * 0.2 * RIGHT)
        self.add(dot_1l)
        self.play(c_s2_lhs.animate.next_to(c_s1_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 2/5)
        dot_2l = Dot().scale(0.6).move_to(c_s1_lhs.get_start() + 2 * stretch_factor * 0.2 * RIGHT)
        self.add(dot_2l)
        self.play(c_s3_lhs.animate.next_to(c_s2_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 2/5)
        dot_3l = Dot().scale(0.6).move_to(c_s1_lhs.get_start() + 3 * stretch_factor * 0.2 * RIGHT)
        self.add(dot_3l)
        self.play(c_s4_lhs.animate.next_to(c_s3_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 2/5)
        dot_4l = Dot().scale(0.6).move_to(c_s1_lhs.get_start() + 4 * stretch_factor * 0.2 * RIGHT)
        self.add(dot_4l)
        self.play(c_s5_lhs.animate.next_to(c_s4_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 2/5)

        dot_1r = Dot(color = BRAT_GREEN).scale(0.6)
        dot_1r.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + 1 * stretch_factor * (x1_val.get_value() - 0.2) * RIGHT))
        dot_2r = Dot(color = BRAT_GREEN).scale(0.6)
        dot_2r.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + 2 * stretch_factor * (x1_val.get_value() - 0.2) * RIGHT))
        dot_3r = Dot(color = BRAT_GREEN).scale(0.6)
        dot_3r.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + 3 * stretch_factor * (x1_val.get_value() - 0.2) * RIGHT))
        dot_4r = Dot(color = BRAT_GREEN).scale(0.6)
        dot_4r.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + 4 * stretch_factor * (x1_val.get_value() - 0.2) * RIGHT))
        dot_5r = Dot(color = BRAT_GREEN).scale(0.6)
        dot_5r.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + 5 * stretch_factor * (x1_val.get_value() - 0.2) * RIGHT))
        dot_6l = Dot(color = BRAT_GREEN).scale(0.6)
        dot_6l.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + stretch_factor * (5 * (x1_val.get_value() - 0.2) + 1 * ((2/3) * (1 - x1_val.get_value()) - x1_val.get_value())) * RIGHT))
        dot_7l = Dot(color = BRAT_GREEN).scale(0.6)
        dot_7l.add_updater(lambda d_ : d_.move_to(c_s1_rhs.get_start() + stretch_factor * (5 * (x1_val.get_value() - 0.2) + 2 * ((2/3) * (1 - x1_val.get_value()) - x1_val.get_value())) * RIGHT))

        self.play(c_s1_rhs.animate.next_to(c_s1_lhs, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF), run_time = 1/4)
        self.add(dot_1r)
        self.play(c_s2_rhs.animate.next_to(c_s1_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_2r)
        self.play(c_s3_rhs.animate.next_to(c_s2_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_3r)
        self.play(c_s4_rhs.animate.next_to(c_s3_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_4r)
        self.play(c_s5_rhs.animate.next_to(c_s4_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_5r)
        self.play(c_s6_lhs.animate.next_to(c_s5_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_6l)
        self.play(c_s7_lhs.animate.next_to(c_s6_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.add(dot_7l)
        self.play(c_s8_lhs.animate.next_to(c_s7_lhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/4)
        self.wait()
        
        self.play(c_s6_rhs.animate.next_to(c_s1_rhs, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF), run_time = 1/2)
        dot_6r = Dot(color = LOGO_BLUE).scale(0.6)
        dot_6r.add_updater(lambda d_ : d_.move_to(c_s6_rhs.get_start() + stretch_factor * 1 * (x1_val.get_value() + x2_val.get_value() - (2/3) * (1 - x1_val.get_value())) * RIGHT))
        self.add(dot_6r)
        self.play(c_s7_rhs.animate.next_to(c_s6_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/2)
        dot_7r = Dot(color = LOGO_BLUE).scale(0.6)
        dot_7r.add_updater(lambda d_ : d_.move_to(c_s6_rhs.get_start() + stretch_factor * 2 * (x1_val.get_value() + x2_val.get_value() - (2/3) * (1 - x1_val.get_value())) * RIGHT))
        self.add(dot_7r)
        self.play(c_s8_rhs.animate.next_to(c_s7_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/2)
        dot_8r = Dot(color = LOGO_BLUE).scale(0.6)
        dot_8r.add_updater(lambda d_ : d_.move_to(c_s6_rhs.get_start() + stretch_factor * 3 * (x1_val.get_value() + x2_val.get_value() - (2/3) * (1 - x1_val.get_value())) * RIGHT))
        self.add(dot_8r)
        self.play(c_s9.animate.next_to(c_s8_rhs, direction = RIGHT, aligned_edge = ORIGIN, buff = 0.0), run_time = 1/2)
        self.wait()

        for (x1_, x2_) in [(1/5, 1/3), (2/5, 0), (2/5, 1/3), (0.3, 1/2), (1/5, 1/2), (1/5, 1/3), (1/4, 5/12)]:
            self.play(
                x1_val.animate.set_value(x1_ + 1e-6),
                x2_val.animate.set_value(x2_ + 1e-6)
            )
        self.wait()

        step1_rhs.clear_updaters()
        step1_lhs.clear_updaters()
        step2_rhs.clear_updaters()
        step2_lhs.clear_updaters()
        step3_rhs.clear_updaters()
        step3_lhs.clear_updaters()
        step4_rhs.clear_updaters()
        step4_lhs.clear_updaters()
        step5_rhs.clear_updaters()
        step5_lhs.clear_updaters()
        step6_rhs.clear_updaters()
        step6_lhs.clear_updaters()
        step7_rhs.clear_updaters()
        step7_lhs.clear_updaters()
        step8_rhs.clear_updaters()
        step8_lhs.clear_updaters()
        step9.clear_updaters()
        
        self.play(
            step6_lhs.animate.next_to(step1_rhs.get_end(), direction = RIGHT, buff = 0.0),
            step7_lhs.animate.next_to(step2_rhs.get_end(), direction = RIGHT, buff = 0.0),
            step8_lhs.animate.next_to(step3_rhs.get_end(), direction = RIGHT, buff = 0.0),
        )
        self.play(
            step6_rhs.animate.next_to(step6_lhs.get_end(), direction = RIGHT, buff = 0.0),
            step7_rhs.animate.next_to(step7_lhs.get_end(), direction = RIGHT, buff = 0.0),
            step8_rhs.animate.next_to(step8_lhs.get_end(), direction = RIGHT, buff = 0.0),
        )

        self.play(
            step9.animate.next_to(step6_rhs.get_end(), direction = RIGHT, buff = 0.0)
        )

        self.play(Uncreate(axes), Unwrite(x_lab), Unwrite(y_lab), Uncreate(polyhedra), Uncreate(axes_p12))
        self.remove(
            c_s1_lhs, c_s1_rhs,
            c_s2_lhs, c_s2_rhs,
            c_s3_lhs, c_s3_rhs,
            c_s4_lhs, c_s4_rhs,
            c_s5_lhs, c_s5_rhs,
            c_s6_lhs, c_s6_rhs,
            c_s7_lhs, c_s7_rhs,
            c_s8_lhs, c_s8_rhs,
            c_s9 
        )
        self.remove(
            dot_1l, dot_1r,
            dot_2l, dot_2r,
            dot_3l, dot_3r,
            dot_4l, dot_4r,
            dot_5r,
            dot_6l, dot_6r,
            dot_7l, dot_7r,
            dot_8r,
        )
        self.wait()

        line.clear_updaters()
        or_dot.clear_updaters()
        or_x1_line.clear_updaters()
        x1_dot.clear_updaters()
        x1_x2_line.clear_updaters()
        x2_dot.clear_updaters()
        x1_txt.clear_updaters()
        x2_txt.clear_updaters()
        f_dot.clear_updaters()
        e1_dot.clear_updaters()
        e2_dot.clear_updaters()
        e0_tex.clear_updaters()
        e1_tex.clear_updaters()
        e2_tex.clear_updaters()
        e3_tex.clear_updaters()

        self.play(
            line.animate.shift(5 * LEFT),
            or_dot.animate.shift(5 * LEFT),
            or_x1_line.animate.shift(5 * LEFT),
            x1_dot.animate.shift(5 * LEFT),
            x1_x2_line.animate.shift(5 * LEFT),
            x2_dot.animate.shift(5 * LEFT),
            x1_txt.animate.shift(5 * LEFT),
            x2_txt.animate.shift(5 * LEFT),
            f_dot.animate.shift(5 * LEFT),
            e1_dot.animate.shift(5 * LEFT),
            e2_dot.animate.shift(5 * LEFT),
            e0_tex.animate.shift(5 * LEFT),
            e1_tex.animate.shift(5 * LEFT),
            e2_tex.animate.shift(5 * LEFT),
            e3_tex.animate.shift(5 * LEFT),
        )
        
        self.play(
            AnimationGroup(
                step1_lhs.animate.shift(5 * LEFT),
                step2_lhs.animate.shift(5 * LEFT),
                step3_lhs.animate.shift(5 * LEFT),
                step4_lhs.animate.shift(5 * LEFT),
                step5_lhs.animate.shift(5 * LEFT),
                step1_rhs.animate.shift(5 * LEFT),
                step2_rhs.animate.shift(5 * LEFT),
                step3_rhs.animate.shift(5 * LEFT),
                step4_rhs.animate.shift(5 * LEFT),
                step5_rhs.animate.shift(5 * LEFT),
                step6_lhs.animate.shift(5 * LEFT),
                step7_lhs.animate.shift(5 * LEFT),
                step8_lhs.animate.shift(5 * LEFT),
                step6_rhs.animate.shift(5 * LEFT),
                step7_rhs.animate.shift(5 * LEFT),
                step8_rhs.animate.shift(5 * LEFT),
                step9.animate.shift(5 * LEFT),
                lag_ratio = 0.1
            )
        )
        hist_left_line = Line(UP, 3 * DOWN).to_edge(LEFT)
        self.add(hist_left_line)
        eq_dist_32 = Tex("$5 \\times \\mathrm{dist}(E_{3}, E_{2}) \\leq 1$").next_to(hist_left_line.get_start(), direction = DR, buff = MED_LARGE_BUFF)
        self.play(Write(eq_dist_32))
        eq_dist_21 = Tex("$3 \\times \\mathrm{dist}(E_{2}, E_{1}) \\leq 1$").next_to(eq_dist_32, direction = DOWN, buff = MED_LARGE_BUFF).set_color(BRAT_GREEN)
        self.play(Write(eq_dist_21))
        eq_dist_10 = Tex("$1 \\times \\mathrm{dist}(E_{1}, E_{0}) \\leq 1$").next_to(eq_dist_21, direction = DOWN, buff = MED_LARGE_BUFF).set_color(LOGO_BLUE)
        self.play(Write(eq_dist_10))
        self.play(
            Transform(
                eq_dist_32,
                Tex("$\\mathrm{dist}(E_{3}, E_{2}) \\leq \\frac{1}{5}$").next_to(hist_left_line.get_start(), direction = DR, buff = MED_LARGE_BUFF)
            )
        )
        self.play(
            Transform(
                eq_dist_21,
                Tex("$\\mathrm{dist}(E_{2}, E_{1}) \\leq \\frac{1}{3}$").next_to(eq_dist_32, direction = DOWN, buff = MED_LARGE_BUFF).set_color(BRAT_GREEN)
            )
        )
        self.play(
            Transform(
                eq_dist_10,
                Tex("$\\mathrm{dist}(E_{1}, E_{0}) \\leq \\frac{1}{1}$").next_to(eq_dist_21, direction = DOWN, buff = MED_LARGE_BUFF).set_color(LOGO_BLUE)
            )
        )
        eq_dn_d123 = Tex("$\\mathrm{dist}(E_{3}, E_{0}) = \\mathrm{dist}(E_{3}, E_{2}) + \\mathrm{dist}(E_{2}, E_{1}) + \\mathrm{dist}(E_{1}, E_{0})$").to_edge(DOWN)
        self.play(
            Write(eq_dn_d123)
        )
        self.play(
            Transform(
                eq_dn_d123,
                Tex('$\\boxed{\\mathrm{dist}(E_{3}, E_{0}) \\leq 1 + \\frac{1}{3} + \\frac{1}{5} = d_{3}}$').scale(0.8).to_edge(DOWN)
            )
        )
        self.wait()
