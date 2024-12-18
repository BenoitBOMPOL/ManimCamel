from manim import *
class seq5b_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(4 * LEFT)
        x_point = Dot(color = TEAL).scale(0.6).move_to(4 * RIGHT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).move_to(saloon.get_center() + 0.25 * LEFT)
        x_txt = Tex('$x_{4}$').set_color(TEAL).scale(0.65).move_to(x_point.get_center() + 0.25 * RIGHT)
        line = Line(saloon.get_center(), x_point.get_center())
        self.add(background_image)
        self.add(line)
        self.add(saloon, s_txt)
        self.add(x_point, x_txt)

        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 8 * RIGHT))

        cargo_amounts = '0,1000,1000-x_{4},x_{4},0,1000,1000-x_{4},x_{4},0,1000,1000-x_{4},x_{4},0,1000,1000-x_{4},0'.rsplit(',')
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        saloon_amounts = '4000,3000,2000,1000,0'.rsplit(',')
        saloon_amt_idx = ValueTracker(0)
        saloon_amt_txt = Tex(f'${saloon_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)

        depot_amounts = '0,1000-2x_{4},2\\times(1000-2x_{4}),3\\times(1000-2x_{4}),3\\times(1000-2x_{4})+(1000-x_{4}),4000-7x_{4}'.rsplit(',')
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

        for idx_ in range(3):
            saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
            self.play(
                Transform(saloon_amt_txt, update_saloon_amount()),
                Transform(cargo_amt_txt, update_cargo_amount()),
            )

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

            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
            self.play(
                camel_position.animate.set_value(0),
                Transform(cargo_amt_txt, update_cargo_amount().shift(8 * LEFT)),
            )

        saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(saloon_amt_txt, update_saloon_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        self.remove(saloon_amt_txt)

        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(1),
            Transform(cargo_amt_txt, update_cargo_amount().shift(8 * RIGHT)),
        )
        
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1),
        depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depot_amt_txt, update_depot_amount()),
        )
        self.remove(cargo_amt_txt)
        self.play(depot_amt_txt.animate.scale(1.25))
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        qte_txt = Tex('Quantité de bananes au dépôt :').scale(0.8).next_to(hist_left_line.get_start(), direction = RIGHT, buff = SMALL_BUFF)
        self.remove(saloon, s_txt, x_point, x_txt, line, camel)
        self.add(hist_left_line, qte_txt)
        self.play(depot_amt_txt.animate.next_to(qte_txt, direction = RIGHT, buff = SMALL_BUFF))
        self.wait(DEFAULT_WAIT_TIME / 6)
        depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
        self.play(Transform(depot_amt_txt, update_depot_amount(scale = True).set_color(WHITE).next_to(qte_txt, direction = RIGHT, buff = SMALL_BUFF)))
        souhait_txt = Tex('Nombre de bananes souhaitées : $3000$').scale(0.8).next_to(qte_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        equation_txt = Tex('Équation à résoudre : ').scale(0.8).next_to(souhait_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        self.add(souhait_txt)
        self.play(Write(equation_txt))
        equation_tex = Tex('$3000 = 4000 - 7x_{4}$').scale(0.8).next_to(equation_txt, direction = RIGHT, aligned_edge = DOWN, buff = SMALL_BUFF)
        self.play(Write(equation_tex))
        self.remove(equation_txt)
        self.play(Transform(equation_tex, Tex('$x_{4} = \\frac{1000}{7}$').scale(0.8).next_to(souhait_txt, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)))
        d4_txt = Tex('$\\begin{aligned} d_{\\max}(4) &\\geq \\frac{1000}{7} + 1533.333 \\\\&\\geq 1.676\\dots \\textrm{ km} \\end{aligned}$').scale(0.8)
        self.play(Write(d4_txt))
        self.wait()