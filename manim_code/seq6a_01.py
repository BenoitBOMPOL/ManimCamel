from manim import *
BRAT_GREEN = ManimColor("#8ACE00")

def compute_dn(n_ : int) -> float:
    return np.sum(1/(2*np.arange(1, n_ + 1) - 1))

class seq6a_01(Scene):
    def construct(self):
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        self.add(hist_left_line)
        axes = Axes(
            x_range = (0, 1000, 100),
            y_range = (0, 5, 1),
            tips = False
        ).scale(0.8).to_edge(RIGHT)
        axes.add_coordinates()
        self.play(Write(axes))

        last_txt : None | Tex = None
        for idx_, nval_ in enumerate([1] + list(range(50, 1050, 50))):
            dn_ = compute_dn(nval_)
            new_txt = Tex(f'$d_{{{nval_}}} = {dn_:.3f}$').scale(0.4).next_to(
                        hist_left_line.get_start() if idx_ == 0 else last_txt,
                        direction = DR if idx_ == 0 else DOWN,
                        aligned_edge = LEFT,
                        buff = SMALL_BUFF
                    )
            self.play(
                Write(
                    new_txt
                ),
                Create(Dot().scale(0.75).move_to(axes.c2p(nval_, dn_))),
                run_time = 0.2
            )
            last_txt = new_txt
        self.wait()