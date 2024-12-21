from manim import *
BRAT_GREEN = ManimColor("#8ACE00")

class seq6e_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        self.play(Create(hist_left_line))
        ub_txt = Tex('$\\boxed{d_{n} \\leq \\frac{1}{2} + \\frac{1}{2}\\ln(4n)}$').scale(0.8).next_to(hist_left_line.get_start(), direction = RIGHT, aligned_edge = UP, buff = MED_SMALL_BUFF)
        self.play(Write(ub_txt))
        step_01_txt = ub_txt.copy()
        self.play(
            Transform(
                step_01_txt,
                Tex('$2\\times d_{n} \\leq 1 + \\ln(4n)$').scale(0.8).next_to(ub_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        step_02_txt = step_01_txt.copy()
        self.play(
            Transform(
                step_02_txt,
                Tex('$\\ln(4n) \\geq 2d_{n}-1$').scale(0.8).next_to(step_01_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        step_03_txt = step_02_txt.copy()
        self.play(
            Transform(
                step_03_txt,
                Tex('$n \\geq \\frac{1}{4}\\exp\\left(2d_{n}-1\\right)$').scale(0.8).next_to(step_02_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        self.remove(step_01_txt, step_02_txt, ub_txt)
        self.play(
            Transform(
                step_03_txt,
                Tex('$\\boxed{n \\geq \\frac{1}{4}\\exp\\left(2\\mathbf{d}-1\\right)}$').set_color(BRAT_GREEN).to_corner(UR)
            )
        )
        self.wait()
        step_04_txt = Tex('$n_{1} = \\frac{1}{4}\\exp\\left(2\\mathbf{d_{1}}-1\\right)$').next_to(hist_left_line.get_start(), direction = RIGHT, aligned_edge = UP, buff = MED_SMALL_BUFF)
        self.play(
            Write(step_04_txt)
        )
        step_05_txt = step_04_txt.copy()
        self.play(
            Transform(
                step_05_txt,
                Tex('$n_{2} = \\frac{1}{4}\\exp\\left(2\\mathbf{(d_{1} + 1)}-1\\right)$').next_to(step_04_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        step_06_txt = step_05_txt.copy()
        self.play(
            Transform(
                step_06_txt,
                Tex('$n_{2} = \\frac{1}{4}\\exp\\left(\\mathbf{(2d_{1} - 1)} + 2\\right)$').next_to(step_05_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        step_07_txt = step_06_txt.copy()
        self.play(
            Transform(
                step_07_txt,
                Tex('$n_{2} = \\frac{1}{4}\\exp\\left(2\\mathbf{d_{1}} - 1\\right)\\times\\mathbf{\\exp(2)}$').next_to(step_06_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        step_08_txt = step_07_txt.copy()
        self.play(
            Transform(
                step_08_txt,
                Tex('$n_{2} = \\mathbf{n_{1}}\\times\\exp(2)$').next_to(step_07_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
            )
        )
        final_result_txt = Tex('$\\boxed{d_{2} = d_{1} + 1 \\implies n_{2} \\simeq n_{1}\\times 7.39}$').set_color(BRAT_GREEN).to_edge(DOWN)
        self.play(Write(final_result_txt))
        self.wait()
        