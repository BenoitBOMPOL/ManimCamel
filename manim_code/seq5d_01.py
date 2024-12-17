from manim import *

BRAT_GREEN = ManimColor("#8ACE00")

class seq5d_01(Scene):
    def construct(self):
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        self.add(hist_left_line)
        xn_eq = Tex("$\\boxed{x_{\\mathbf{n}} = \\frac{1}{2\\mathbf{n}-1}}$").scale(0.6).next_to(hist_left_line.get_start(), direction = RIGHT, aligned_edge = UP, buff = MED_LARGE_BUFF).set_color(BRAT_GREEN).scale(1.2)
        dn_eq = Tex("$\\boxed{d_{\\mathbf{n}} = d_{\\mathbf{n-1}} + x_{\\mathbf{n}}}$").scale(0.6).next_to(xn_eq, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF).set_color(BRAT_GREEN).scale(1.2)
        self.play(Create(xn_eq), Create(dn_eq))

        nb_int = 8
        x_values = {1 : 1.0}
        d_values = {1 : 1.0}
        d_lhs_items = {1 : Tex(f'$n = 1, d_{{{1}}} = {d_values[1]:.3f}' + '$ \\textrm{km}').scale(0.6).next_to(dn_eq, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)}
        d_rhs_items = {}
        self.add(d_lhs_items[1])
        last_item = d_lhs_items[1]
        for idx_ in range(2, nb_int + 1):
            d_lhs_items[idx_] = Tex(f'$n = {idx_}, ' + 'd_{\\mathbf{' + str(idx_) + '}} = $').scale(0.6).next_to(last_item, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
            d_rhs_items[idx_] = Tex('$d_{\\mathbf{' + str(idx_ - 1) + '}} + x_{\\mathbf{' + str(idx_ - 1) + '}}$').scale(0.6).next_to(d_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            self.add(d_lhs_items[idx_], d_rhs_items[idx_])
            x_values[idx_] = 1/(2 * idx_ - 1)
            d_values[idx_] = d_values[idx_ - 1] + x_values[idx_]
            # tex_drhs = Tex(f'${d_values[idx_ - 1]:.3f} + ' + '\\frac{1}{2\\times' + str(idx_) + '- 1}$').scale(0.6).next_to(d_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            # self.play(Transform(d_rhs_items[idx_], tex_drhs))
            new_drhs = Tex(f'${d_values[idx_ - 1]:.3f} + {x_values[idx_]:.3f}$').scale(0.6).next_to(d_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            self.play(Transform(d_rhs_items[idx_], new_drhs))
            nnew_drhs = Tex(f'${d_values[idx_]:.3f}' + '$ \\textrm{km}').scale(0.6).next_to(d_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            self.play(Transform(d_rhs_items[idx_], nnew_drhs))
            self.wait()
            last_item = d_lhs_items[idx_]
        dn_formula = Tex('$d_{n} = 1 + \\frac{1}{3} + \\frac{1}{5} + \\dots + \\frac{1}{2{n}-1}$').set_color(BRAT_GREEN).to_edge(DOWN)
        self.play(Write(dn_formula))
        return