from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6d_02(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        x_na = Tex('$\\boxed{\\mathbf{x_{n,\\alpha}} = \\frac{\\alpha}{2n + 1}}$').to_corner(UL)
        dn_eq = Tex('$\\boxed{d_{n} = \\sum_{k = 1}^{n}\\frac{1}{2k-1}}$').scale(0.75).next_to(x_na, direction = RIGHT, aligned_edge = UP, buff = MED_SMALL_BUFF)
        self.play(Write(x_na), Write(dn_eq))
        dx_eq = Tex('$\\boxed{d(x) = \\left(\\sum_{k = 1}^{\\lfloor{x}\\rfloor}\\frac{1}{2k-1}\\right) + \\frac{x - \\lfloor{x}\\rfloor}{2\\lfloor{x}\\rfloor + 1}}$')
        self.play(Write(dx_eq))

        return