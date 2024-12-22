from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_04(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        reseq_1 = Tex('$\\boxed{\\frac{1}{2n} + \\ln(2n) \\leq H_{2n} \\leq 1 + \\ln(2n)}$').scale(0.6).to_corner(UL)
        reseq_2 = Tex('$\\boxed{\\ln(2) - \\frac{1}{2n} \\leq H_{2n} - H_{n} \\leq \\ln(2)}$').scale(0.6).to_corner(UR)
        reseq_3 = Tex('$\\boxed{d_{n} = H_{2n} - \\frac{1}{2}H_{n}}$').scale(0.6).to_edge(UP)
        self.add(reseq_1, reseq_2, reseq_3)
        self.play(
            Transform(
                reseq_3,
                Tex('$\\boxed{d_{n} = \\frac{1}{2}H_{2n} + \\frac{1}{2}\\left(H_{2n} - H_{n}\\right)}$').scale(0.6).to_edge(UP)
            )
        )
        lhs_1 = Tex('$\\frac{1}{4n} + \\frac{1}{2}\\ln(2n) \\leq \\frac{1}{2}H_{2n} \\leq \\frac{1}{2} + \\frac{1}{2}\\ln(2n)$').scale(0.6).next_to(reseq_3, direction = DOWN, buff = MED_LARGE_BUFF)
        self.play(
            Transform(
                reseq_3,
                Tex('$\\boxed{d_{n} = \\mathbf{\\frac{1}{2}H_{2n}} + \\frac{1}{2}\\left(H_{2n} - H_{n}\\right)}$').scale(0.6).to_edge(UP)
            ),
            Write(lhs_1)
        )
        lhs_2 = Tex('$\\frac{1}{2}\\ln(2) - \\frac{1}{4n} \\leq \\frac{1}{2}(H_{2n} - H_{n}) \\leq \\frac{1}{2}\\ln(2)$').scale(0.6).next_to(lhs_1, direction = DOWN, buff = MED_LARGE_BUFF)
        self.play(
            Transform(
                reseq_3,
                Tex('$\\boxed{d_{n} = \\frac{1}{2}H_{2n} + \\mathbf{\\frac{1}{2}\\left(H_{2n} - H_{n}\\right)}}$').scale(0.6).to_edge(UP)
            ),
            Write(lhs_2)
        )

        self.remove(reseq_3)
        self.add(Tex('$\\boxed{d_{n} = \\frac{1}{2}H_{2n} + \\frac{1}{2}\\left(H_{2n} - H_{n}\\right)}$').scale(0.6).to_edge(UP))

        final_res_eq = Tex('$\\boxed{\\frac{1}{4n} + \\frac{1}{2}\\ln(2n) + \\frac{1}{2} \\ln(2) - \\frac{1}{4n} \\leq d_{n} \\leq \\frac{1}{2} + \\frac{1}{2}\\ln(2n) + \\frac{1}{2}\\ln(2)}$')
        self.play(
            Write(final_res_eq)
        )
        self.play(
            Transform(
                final_res_eq,
                Tex('$\\boxed{\\frac{1}{2}\\ln(2n) + \\frac{1}{2} \\ln(2) \\leq d_{n} \\leq \\frac{1}{2} + \\frac{1}{2}\\ln(4n)}$')
            )
        )
        self.play(
            Transform(
                final_res_eq,
                Tex('$\\boxed{\\frac{1}{2}\\ln(4n) \\leq d_{n} \\leq \\frac{1}{2} + \\frac{1}{2}\\ln(4n)}$').set_color(BRAT_GREEN)
            )
        )

        axes = Axes(x_range = (0, 20, 1), y_range = (0, 4, 1), x_length=10, y_length=2, tips = False).to_edge(DOWN)
        axes.add_coordinates()
        self.play(Write(axes))

        lb_func = axes.plot(lambda n_ : 0.5 * np.log(4 * n_), x_range = (1, 20, 1)).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        self.add(lb_func)

        ub_func = axes.plot(lambda n_ : 0.5 + 0.5 * np.log(4 * n_), x_range = (1, 20, 1)).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        self.add(ub_func)

        self.wait()
        dn_func = [Dot(color = BRAT_GREEN).scale(0.5).move_to(axes.c2p(n_, sum([1/(2*k_ - 1) for k_ in range(1, n_ + 1)]))) for n_ in range(1, 21)]
        self.play(
            AnimationGroup(
                *[Create(dot) for dot in dn_func],
                lag_ratio=0.1
            )
        )
        self.wait()
        