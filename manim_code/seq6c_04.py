from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6c_04(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        comp_tex = Tex('$\\boxed{\\frac{1}{k + 1} \\leq \\ln(k + 1) - \\ln(k) \\leq \\frac{1}{k}}$').to_edge(UP)
        self.play(Write(comp_tex))
        hist_left_line = Line(1.5 * UP, 1.5 * DOWN).to_edge(LEFT)
        
        eq_kn = Tex('$\\frac{1}{\\mathbf{n} + 1} \\leq \\ln(\\mathbf{n} + 1) - \\ln(\\mathbf{n}) \\leq \\frac{1}{\\mathbf{n}}$').scale(0.6).next_to(hist_left_line.get_start(), direction = DR, buff = SMALL_BUFF)
        eq_knpp = Tex('$\\frac{1}{\\mathbf{n + 1} + 1} \\leq \\ln(\\mathbf{n + 1} + 1) - \\ln(\\mathbf{n + 1}) \\leq \\frac{1}{\\mathbf{n + 1}}$').scale(0.6).next_to(eq_kn, direction = DOWN, buff = SMALL_BUFF)
        self.add(hist_left_line)
        self.play(Write(eq_kn))
        self.play(
            Transform(
                eq_kn,
                Tex('$\\frac{1}{n + 1} \\leq \\ln(n + 1) - \\ln(n) \\leq \\frac{1}{n}$').scale(0.6).next_to(hist_left_line.get_start(), direction = DR, buff = SMALL_BUFF)
            ),
            Write(eq_knpp))
        self.play(
            Transform(
                eq_knpp,
                Tex('$\\frac{1}{n + 2} \\leq \\ln(n + 2) - \\ln(n + 1) \\leq \\frac{1}{n + 1}$').scale(0.6).next_to(eq_kn, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
            )
        )
        eq_kdots = Tex('$\\vdots$').scale(0.6).next_to(eq_knpp, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(
            Write(eq_kdots)
        )
        eq_k2nm = Tex('$\\frac{1}{\\mathbf{2n-1} + 1} \\leq \\ln(\\mathbf{2n-1} + 1) - \\ln(\\mathbf{2n - 1}) \\leq \\frac{1}{\\mathbf{2n - 1}}$').scale(0.6).next_to(eq_kdots, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(
            Write(eq_k2nm)
        )
        self.play(
            Transform(
                eq_k2nm,
                Tex('$\\frac{1}{2n} \\leq \\ln(2n) - \\ln(2n - 1) \\leq \\frac{1}{2n - 1}$').scale(0.6).next_to(eq_kdots, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
            )
        )
        sum_eq = Tex('$\\frac{1}{n+1} + \\frac{1}{n+2} + \\dots + \\frac{1}{2n} \\leq \\ln(2n) - \\ln(n) \\leq \\frac{1}{n} + \\frac{1}{n + 1} + \\dots + \\frac{1}{2n-1}$').scale(0.6).next_to(eq_k2nm, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(
            Write(sum_eq)
        )
        res_eq = Tex('$H_{2n} - H_{n} \\leq \\ln(2n) - \\ln(n) \\leq H_{2n} - H_{n} + \\frac{1}{n} - \\frac{1}{2n}$').scale(0.6).next_to(eq_k2nm, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(
            Write(res_eq)
        )
        self.play(
            Transform(
                res_eq,
                Tex('$H_{2n} - H_{n} \\leq \\mathbf{\\ln(2)} \\leq H_{2n} - H_{n} + \\frac{1}{2n}$').scale(0.6).next_to(eq_k2nm, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
            )
        )
        
        final_res_eq = Tex('$\\boxed{\\mathbf{\\ln(2)} - \\frac{1}{2n} \\leq H_{2n} - H_{n} \\leq \\mathbf{\\ln(2)}}$').set_color(BRAT_GREEN).to_edge(DOWN)
        self.play(Transform(res_eq, final_res_eq))
        
        self.wait()