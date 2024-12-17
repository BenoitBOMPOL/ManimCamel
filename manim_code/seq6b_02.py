from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq6b_02(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        hist_left_line = Line(2.5 * UP, 2.5 * DOWN).to_edge(LEFT)
        dn_final_eq = Tex('$\\boxed{d_{n} = H_{2n} - \\frac{1}{2}H_{n}}$').set_color(BRAT_GREEN).to_edge(UP)
        self.play(Write(dn_final_eq))
        self.add(hist_left_line)
        dn_alt_eq_00 = Tex('$d_{n} = H_{2n} - \\frac{1}{2}H_{n}$').scale(0.8).next_to(hist_left_line.get_start(), direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.add(dn_alt_eq_00)
        dn_alt_eq_01 = Tex('$d_{n} = \\frac{1}{2}H_{2n} + \\frac{1}{2}H_{2n} - \\frac{1}{2}H_{n}$').scale(0.8).next_to(dn_alt_eq_00, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(dn_alt_eq_01)
        dn_alt_eq_02 = Tex('$d_{n} = \\frac{1}{2}H_{2n} + \\frac{1}{2}(H_{2n} - H_{n})$').scale(0.8).next_to(dn_alt_eq_01, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(dn_alt_eq_02)
        dn_alt_eq_03 = Tex('$d_{n} = \\frac{1}{2}H_{2n} + \\frac{1}{2}(\\frac{1}{n+1} + \\frac{1}{n+2} + \\dots + \\frac{1}{2n})$').scale(0.8).next_to(dn_alt_eq_02, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(dn_alt_eq_03)
        dn_alt_eq_04 = Tex('$d_{n} = \\frac{1}{2}H_{2n} + \\underbrace{\\frac{1}{2}(\\frac{1}{n+1} + \\frac{1}{n+2} + \\dots + \\frac{1}{2n})}_{\\geq 0}$').scale(0.6).next_to(dn_alt_eq_03, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.play(Write(dn_alt_eq_04))
        dn_alt_eq_05 = Tex('$d_{n} \\geq \\frac{1}{2}H_{2n}$').scale(0.8).next_to(dn_alt_eq_04, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        self.add(dn_alt_eq_05)
        self.wait()
        limit_eq_elts = []
        limit_hn_eq = Tex('$\\boxed{\\lim_{n\\mapsto+\\infty}H_{n} = +\\infty}$').set_color(LOGO_RED).to_edge(DOWN)
        limit_eq_elts.append(limit_hn_eq)
        imp_eq = Tex("$\\implies$").next_to(limit_hn_eq, direction = RIGHT, aligned_edge = ORIGIN, buff = SMALL_BUFF)
        limit_eq_elts.append(imp_eq)
        limit_dn_eq = Tex('$\\boxed{\\lim_{n\\mapsto+\\infty}d_{n} = +\\infty}$').set_color(BRAT_GREEN).next_to(imp_eq, direction = RIGHT, aligned_edge = ORIGIN, buff = SMALL_BUFF)
        limit_eq_elts.append(limit_dn_eq)
        self.play(*[Write(elt_) for elt_ in limit_eq_elts])
        self.wait()