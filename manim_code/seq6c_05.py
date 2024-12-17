from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_05(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
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
        self.wait()
        