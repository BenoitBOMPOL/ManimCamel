from manim import *

class seq4b_02(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        context_txt = Tex('Position finale du chameau :').scale(0.6).to_corner(UL)
        objective_txt = Tex('$2000 - 2x$').scale(0.6).next_to(context_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        self.play(Write(context_txt))
        self.play(Write(objective_txt))

        line = Line(6 * LEFT, 6 * RIGHT).shift(3 * UP)
        s_dot = Dot(color = LIGHT_BROWN).move_to(6 * LEFT + 3 * UP)
        s_txt = Tex('$S$').scale(0.6).set_color(LIGHT_BROWN).next_to(s_dot, direction=DL, buff = SMALL_BUFF)
        f_dot = Dot().move_to(6 * RIGHT + 3 * UP)
        f_txt = Tex('$F$').scale(0.6).next_to(f_dot, direction=RIGHT, buff = SMALL_BUFF)
        x_dot = Dot(color = TEAL).move_to(3 * LEFT + 3 * UP)
        x_txt = Tex('$x$').scale(0.6).set_color(TEAL).next_to(x_dot, direction=DOWN, buff=SMALL_BUFF)
        self.add(line)
        self.add(s_dot, s_txt, x_dot, x_txt, f_dot, f_txt)

        constraint_txt = Tex('\\underline{Contraintes} :').scale(0.6).next_to(context_txt, direction=DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        self.play(Write(constraint_txt))

        a_txt = Tex('(\\textrm{a})').scale(0.6).next_to(constraint_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        desc_a_txt = Tex(' La distance parcourue est \\textbf{positive}.').scale(0.6).next_to(a_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        a_formula_csttxt = Tex('$x\\geq 0$').scale(0.6).next_to(desc_a_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)
        self.add(a_txt, desc_a_txt, a_formula_csttxt)
        self.wait()

        b_txt = Tex('(\\textrm{b})').scale(0.6).next_to(a_txt, direction = DOWN, aligned_edge = LEFT, buff = LARGE_BUFF)
        desc_b_txt = Tex(" L'aller-retour \\textbf{Saloon}-\\textbf{Dépôt} doit être possible sans recharge.").scale(0.6).next_to(b_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        b_formula_csttxt = Tex('$2x\\leq 1000$').scale(0.6).next_to(desc_b_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)
        self.add(b_txt, desc_b_txt, b_formula_csttxt)
        self.play(Transform(b_formula_csttxt, Tex('$x\\leq 500$').scale(0.6).next_to(desc_b_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)))
        self.wait()

        c_txt = Tex('(\\textrm{c})').scale(0.6).next_to(b_txt, direction = DOWN, aligned_edge = LEFT, buff = LARGE_BUFF)
        rapl_c_txt = Tex("\\underline{Rappel} : Avant l'ultime trajet, le chameau possède $2000 - 3x$ bananes.").scale(0.6).next_to(c_txt, direction = RIGHT, aligned_edge = UP, buff = SMALL_BUFF)
        desc_c_txt = Tex(" Le chameau doit pouvoir prendre $2000-3x$ bananes dans son réservoir.").scale(0.6).next_to(rapl_c_txt, direction = DOWN, aligned_edge = LEFT, buff = SMALL_BUFF)
        c_txt.next_to(desc_c_txt, direction = LEFT, aligned_edge = UP, buff = SMALL_BUFF)
        c_formula_csttxt = Tex('$2000-3x\\leq1000$').scale(0.6).next_to(desc_c_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)
        self.add(rapl_c_txt)
        self.add(c_txt, desc_c_txt, c_formula_csttxt)
        self.play(Transform(c_formula_csttxt, Tex('$1000-3x\\leq0$').scale(0.6).next_to(desc_c_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)))
        self.play(Transform(c_formula_csttxt, Tex('$x\\geq\\frac{1000}{3}\\simeq 333.33$').scale(0.6).next_to(desc_c_txt, direction=DOWN, aligned_edge=LEFT, buff = SMALL_BUFF)))
        self.wait()