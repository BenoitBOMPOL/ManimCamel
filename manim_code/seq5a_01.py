from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq5a_01(Scene):
    def construct(self):
        axes = Axes(x_range = (-250, 10250, 1000), y_range = (-0.25, 2.5, 0.5), x_length=12,y_length=6, tips = False).to_edge(DOWN)
        axes.get_x_axis().add_tip(tip_length=0.15)
        axes.get_y_axis().add_tip(tip_length=0.15)
        axes.add_coordinates()
        axes.get_x_axis().set_color(TEAL_D)
        axes.get_y_axis().set_color(RED_D)
        x_lab = MathTex(r"x_{1}").set_color(TEAL_D).scale(0.6).next_to(axes.get_x_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        y_lab = MathTex(r"x_{2}").set_color(RED_D).scale(0.6).next_to(axes.get_y_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        self.add(axes, x_lab, y_lab)

        dots = {0 : Dot().move_to(axes.c2p(0, 0)).set_color(BRAT_GREEN)}
        self.play(Create(dots[0]))
        yi_ = 0
        for i_ in range(1, 11):
            xi_ = i_ * 1000
            yi_ += 1/(2*i_ - 1)
            dots[i_] = Dot().move_to(axes.c2p(xi_, yi_))
            if i_ < 2:
                dots[i_].set_color(BRAT_GREEN)
            self.add(dots[i_])
            self.wait(DEFAULT_WAIT_TIME / 5)
        self.wait()
