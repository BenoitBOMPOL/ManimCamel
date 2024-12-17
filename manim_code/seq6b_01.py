from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6b_01(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        self.add(hist_left_line)
        hn_eq = Tex("$\\boxed{H_{n} = 1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{n}}$").scale(0.8).next_to(hist_left_line.get_start(), direction=RIGHT, aligned_edge=UP, buff=SMALL_BUFF).set_color(LOGO_BLUE)
        dn_eq = Tex("$\\boxed{d_{n} = 1 + \\frac{1}{3} + \\frac{1}{5} + \\dots + \\frac{1}{2n-1}}$").scale(0.8).next_to(hn_eq, direction=RIGHT, aligned_edge=UP, buff=SMALL_BUFF).set_color(BRAT_GREEN)
        self.play(Write(hn_eq), Write(dn_eq))
        self.wait()
        dn_eq_root = Tex('$d_{n} = 1 + \\frac{1}{3} + \\frac{1}{5} + \\dots + \\frac{1}{2n-1}$').next_to(hn_eq, direction=DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.play(Write(dn_eq_root))
        dn_eq_01 = Tex('$d_{n} = \\left(1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2n-1} + \\frac{1}{2n}\\right) - \\left(\\frac{1}{2} + \\frac{1}{4} + \\dots + \\frac{1}{2n}\\right)$').scale(0.6).next_to(dn_eq_root, direction=DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.play(Write(dn_eq_01))
        dn_eq_02 = Tex('$d_{n} = \\left(1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2n-1} + \\frac{1}{2n}\\right) - \\frac{1}{2}\\left(1 + \\frac{1}{2} + \\dots + \\frac{1}{n}\\right)$').scale(0.6).next_to(dn_eq_01, direction=DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.play(Write(dn_eq_02))
        dn_eq_03_01 = Tex('$d_{n} =$').scale(0.7).next_to(dn_eq_02, direction=DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        dn_eq_03_02 = Tex('$\\left(1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{2n}\\right)$').set_color(LOGO_BLUE).scale(0.7).next_to(dn_eq_03_01, direction=RIGHT, aligned_edge=ORIGIN, buff=SMALL_BUFF)
        dn_eq_03_03 = Tex('$-\\frac{1}{2}$').scale(0.7).next_to(dn_eq_03_02, direction = RIGHT, aligned_edge = ORIGIN, buff = SMALL_BUFF)
        dn_eq_03_04 = Tex('$\\left(1 + \\frac{1}{2} + \\frac{1}{3} + \\dots + \\frac{1}{n}\\right)$').set_color(LOGO_BLUE).scale(0.7).next_to(dn_eq_03_03, direction=RIGHT, aligned_edge=ORIGIN, buff=SMALL_BUFF)
        self.play(Write(dn_eq_03_01))
        self.play(Write(dn_eq_03_02))
        self.play(Write(dn_eq_03_03))
        self.play(Write(dn_eq_03_04))
        dn_final_eq = Tex('$\\boxed{d_{n} = H_{2n} - \\frac{1}{2}H_{n}}$').scale(0.95).set_color(BRAT_GREEN).to_edge(DOWN)
        self.play(Write(dn_final_eq))
        self.wait()

