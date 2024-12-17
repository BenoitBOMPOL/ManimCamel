from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_03(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        comp_tex = Tex('$\\boxed{\\frac{1}{k + 1} \\leq \\ln(k + 1) - \\ln(k) \\leq \\frac{1}{k}}$').to_edge(UP)
        self.play(Write(comp_tex))
        hist_left_line = Line(1.5 * UP, 1.5 * DOWN).to_edge(LEFT)
        eq_k1 = Tex('$\\frac{1}{\\mathbf{1} + 1} \\leq \\ln(\\mathbf{1} + 1) - \\ln(\\mathbf{1}) \\leq \\frac{1}{\\mathbf{1}}$').scale(0.6).next_to(hist_left_line.get_start(), direction = DR, buff = SMALL_BUFF)
        eq_k2 = Tex('$\\frac{1}{\\mathbf{2} + 1} \\leq \\ln(\\mathbf{2} + 1) - \\ln(\\mathbf{2}) \\leq \\frac{1}{\\mathbf{2}}$').scale(0.6).next_to(eq_k1, direction = DOWN, buff = SMALL_BUFF)
        eq_k3 = Tex('$\\frac{1}{\\mathbf{3} + 1} \\leq \\ln(\\mathbf{3} + 1) - \\ln(\\mathbf{3}) \\leq \\frac{1}{\\mathbf{3}}$').scale(0.6).next_to(eq_k2, direction = DOWN, buff = SMALL_BUFF)
        self.add(hist_left_line)
        self.play(Write(eq_k1))
        self.play(
            Transform(
                eq_k1,
                Tex('$\\frac{1}{2} \\leq \\ln(2) - \\ln(1) \\leq \\frac{1}{1}$').scale(0.6).next_to(hist_left_line.get_start(), direction = DR, buff = SMALL_BUFF)
            ),
            Write(eq_k2)
        )
        self.play(
            Transform(
                eq_k2,
                Tex('$\\frac{1}{3} \\leq \\ln(3) - \\ln(2) \\leq \\frac{1}{2}$').scale(0.6).next_to(eq_k1, direction = DOWN, buff = SMALL_BUFF)
            ),
            Write(eq_k3)
        )
        self.play(
            Transform(
                eq_k3,
                Tex('$\\frac{1}{4} \\leq \\ln(4) - \\ln(3) \\leq \\frac{1}{3}$').scale(0.6).next_to(eq_k2, direction = DOWN, buff = SMALL_BUFF)
            )
        )
        eq_kdots = Tex('$\\vdots$').scale(0.6).next_to(eq_k3, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(Write(eq_kdots))
        eq_kn = Tex('$\\frac{1}{\\mathbf{2n-1} + 1} \\leq \\ln(\\mathbf{2n-1} + 1) - \\ln(\\mathbf{2n-1}) \\leq \\frac{1}{\\mathbf{2n-1}}$').scale(0.6).next_to(eq_kdots, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(Write(eq_kn))
        self.play(
            Transform(
                eq_kn,
                Tex('$\\frac{1}{2n} \\leq \\ln(2n) - \\ln(2n-1) \\leq \\frac{1}{2n-1}$').scale(0.6).next_to(eq_kdots, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
            )
        )
        sum_eq = Tex('$\\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2n} \\leq \\ln(2n) - \\ln(1) \\leq 1 + \\frac{1}{2} + \\dots + \\frac{1}{2n-1}$').scale(0.6).next_to(eq_kn, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(Write(sum_eq))
        self.play(
            Transform(
                sum_eq,
                Tex('$\\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2n} \\leq \\ln(2n) \\leq 1 + \\frac{1}{2} + \\dots + \\frac{1}{2n-1}$').scale(0.6).next_to(eq_kn, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
            )
        )

        res_eq = Tex('$H_{2n} - 1 \\leq \\ln(2n) \\leq H_{2n} - \\frac{1}{2n}$').scale(0.6).next_to(sum_eq, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(
            Write(res_eq)
        )

        final_res_eq = Tex('$\\boxed{\\frac{1}{2n} + \\ln(2n) \\leq H_{2n} \\leq 1 + \\ln(2n)}$').set_color(BRAT_GREEN).to_edge(DOWN)
        self.play(Transform(res_eq, final_res_eq))
        
        self.wait()