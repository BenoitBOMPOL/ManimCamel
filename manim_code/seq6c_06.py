from manim import *
BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_06(Scene):
    def construct(self):
        axes = Axes(x_range = (0, 200, 25), y_range = (0, 5, 1), x_length=10, y_length=5, tips = False)
        axes.add_coordinates()
        lb_func = axes.plot(lambda n_ : 0.5 * np.log(4 * n_), x_range = (1, 200, 1)).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        ub_func = axes.plot(lambda n_ : 0.5 + 0.5 * np.log(4 * n_), x_range = (1, 200, 1)).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        self.add(axes)
        self.play(Create(lb_func))
        self.wait()
        dn_func = [Dot(color = BRAT_GREEN).scale(0.35).move_to(axes.c2p(n_, sum([1/(2*k_ - 1) for k_ in range(1, n_ + 1)]))) for n_ in range(1, 201)]
        self.play(
            AnimationGroup(
                *[Create(dot) for dot in dn_func],
                lag_ratio=0.02
            )
        )
        self.play(Create(ub_func))
        self.wait()
        