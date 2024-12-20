from manim import *
BRAT_GREEN = ManimColor("#8ACE00")

class seq6d_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(4 * LEFT)
        x_point = Dot(color = TEAL).scale(0.6).move_to(4 * RIGHT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).move_to(saloon.get_center() + 0.25 * LEFT)
        x_txt = Tex('$x_{n,\\alpha}$').set_color(TEAL).scale(0.65).move_to(x_point.get_center() + 0.5 * RIGHT)
        line = Line(saloon.get_center(), x_point.get_center())
        self.add(background_image)
        self.add(line)
        self.play(Create(saloon), Create(s_txt))
        self.play(Create(x_point), Create(x_txt))
        alpha_txt = Tex('$\\boxed{0 < \\alpha < 1}$').to_edge(UP)
        self.play(Write(alpha_txt))

        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 8 * RIGHT))

        cargo_amounts = ['0'] + ['1000', '1000-x_{n,\\alpha}', 'x_{n,\\alpha}', '0'] * 5 +  ['\\alpha\\times1000', '\\alpha\\times1000-x_{n,\\alpha}', '0']
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        saloon_amounts = ['(n+\\alpha)\\times1000', '((n-1)+\\alpha)\\times1000', '((n-2)+\\alpha)\\times1000', '((n-\\dots)+\\alpha)\\times1000', '(1 + \\alpha)\\times1000', '\\alpha\\times1000', '0']
        saloon_amt_idx = ValueTracker(0)
        saloon_amt_txt = Tex(f'${saloon_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)

        depot_amounts = ['0', '1000-2x_{n,\\alpha}', '2\\times(1000-2x_{n,\\alpha})', '\\dots\\times(1000-2x_{n,\\alpha})', '(n-1)\\times(1000-2x_{n,\\alpha})', 'n\\times(1000-2x_{n,\\alpha})', 'n\\times(1000-2x_{n,\\alpha}) + (\\alpha\\times1000-x_{n,\\alpha})']
        depot_amt_idx = ValueTracker(0)
        depot_amt_txt = Tex(f'${depot_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 8 * RIGHT + 0.25 * UP)

        def update_saloon_amount():
            new_idx = int(saloon_amt_idx.get_value())
            new_text = Tex(f'${saloon_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)
            return new_text
        
        def update_cargo_amount():
            new_idx = int(cargo_amt_idx.get_value())
            new_text = Tex(f'${cargo_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)
            return new_text
        
        def update_depot_amount(scale = False):
            new_idx = int(depot_amt_idx.get_value())
            new_text = Tex(f'${depot_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4 + 0.4 * int(scale)).move_to(saloon.get_center() + 8 * RIGHT + 0.25 * UP)
            return new_text

        self.play(
            Create(camel),
            Write(saloon_amt_txt), Write(cargo_amt_txt)
        )

        for idx_ in range(6):
            saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
            self.play(
                Transform(saloon_amt_txt, update_saloon_amount()),
                Transform(cargo_amt_txt, update_cargo_amount()),
            )
            if idx_ == 5:
                self.play(alpha_txt.animate.set_color(BRAT_GREEN))
                self.remove(saloon_amt_txt)


            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
            self.play(
                camel_position.animate.set_value(1),
                Transform(cargo_amt_txt, update_cargo_amount().shift(8 * RIGHT)),
            )
            if idx_ == 0:
                self.add(depot_amt_txt)
            
            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1),
            depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
            self.play(
                Transform(cargo_amt_txt, update_cargo_amount()),
                Transform(depot_amt_txt, update_depot_amount()),
            )

            if idx_ < 5:
                cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
                self.play(
                    camel_position.animate.set_value(0),
                    Transform(cargo_amt_txt, update_cargo_amount().shift(8 * LEFT)),
                )
            else:
                self.remove(cargo_amt_txt)

            if idx_ >= 3:
                self.wait()
        
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        qte_txt = Tex('Quantité de bananes au dépôt :').scale(0.8).next_to(hist_left_line.get_start(), direction = RIGHT, buff = SMALL_BUFF)
        self.remove(saloon, s_txt, x_point, x_txt, line, camel, alpha_txt)
        self.add(hist_left_line, qte_txt)
        self.play(depot_amt_txt.animate.set_color(WHITE).scale(1.5).next_to(qte_txt, direction = RIGHT, buff = SMALL_BUFF))
        self.wait(DEFAULT_WAIT_TIME / 6)
        souhait_txt = Tex('Nombre de bananes souhaitées : $n\\times1000$').scale(0.8).next_to(qte_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        equation_txt = Tex('Équation à résoudre : ').scale(0.8).next_to(souhait_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        self.add(souhait_txt)
        self.play(Write(equation_txt))
        equation_tex = Tex('$n\\times1000 = n\\times(1000 - 2\\mathbf{x}) + (1000\\alpha - \\mathbf{x})$').scale(0.8).next_to(equation_txt, direction = RIGHT, aligned_edge = DOWN, buff = SMALL_BUFF)
        self.play(Write(equation_tex))
        eq_step_01 = Tex('$1000n = 1000n -2n\\mathbf{x} + (1000\\alpha - \\mathbf{x})$').scale(0.8).next_to(equation_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        self.play(Write(eq_step_01))
        eq_step_02 = Tex('$0 = -2n\\mathbf{x} + (1000\\alpha - \\mathbf{x})$').scale(0.8).next_to(eq_step_01, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        neq_step_01 = eq_step_01.copy()
        self.add(neq_step_01)
        self.play(Transform(neq_step_01,eq_step_02))
        eq_step_03 = Tex('$0 = 1000\\alpha - (2n + 1)\\mathbf{x}$').scale(0.8).next_to(eq_step_02, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        neq_step_02 = eq_step_02.copy()
        self.add(neq_step_02)
        self.play(Transform(neq_step_02,eq_step_03))
        eq_step_04 = Tex('$\\boxed{\\mathbf{x_{n,\\alpha}} = \\frac{1000\\alpha}{2n + 1}}$').set_color(BRAT_GREEN).next_to(eq_step_03, direction = DOWN, aligned_edge = LEFT, buff = MED_LARGE_BUFF)
        neq_step_03 = eq_step_03.copy()
        self.add(neq_step_03)
        self.play(Transform(neq_step_03,eq_step_04))
        self.wait()
        self.remove(hist_left_line, qte_txt, depot_amt_txt, souhait_txt, equation_txt, equation_tex, eq_step_01, eq_step_02, eq_step_03, neq_step_01, neq_step_02)
        dn_eq = Tex('$\\boxed{d_{n} = \\sum_{k = 1}^{n}\\frac{1}{2k-1}}$').scale(0.75).set_color(BRAT_GREEN).to_corner(UL)
        self.play(
            Write(dn_eq),
            neq_step_03.animate.next_to(dn_eq, direction = RIGHT, aligned_edge = UP, buff = MED_SMALL_BUFF)
        )
        self.wait()
        axes = Axes(x_range = (0, 12, 1), y_range = (0, 2, 1), x_length=12,y_length=4, tips = False).to_edge(DOWN)
        axes.add_coordinates()
        def compute_dn(nval_ : float):
            if nval_.is_integer():
                return sum([1/(2*k_ - 1) for k_ in range(1, int(nval_) + 1)])
            float_val = (nval_ - int(nval_)) / (2 * int(nval_) + 1)
            return float_val + compute_dn(int(nval_))
        
        dn_plot = axes.plot(lambda x_ : compute_dn(x_), x_range=(0, 12, 0.001)).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        self.play(Create(axes))
        self.play(Create(dn_plot))
        self.wait()