from manim import *
class seq5c_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(4 * LEFT)
        x_point = Dot(color = TEAL).scale(0.6).move_to(4 * RIGHT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).move_to(saloon.get_center() + 0.25 * LEFT)
        x_txt = Tex('$x_{n}$').set_color(TEAL).scale(0.65).move_to(x_point.get_center() + 0.25 * RIGHT)
        line = Line(saloon.get_center(), x_point.get_center())
        self.add(background_image)
        self.add(line)
        self.play(Create(saloon), Create(s_txt))
        self.play(Create(x_point), Create(x_txt))

        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 8 * RIGHT))

        cargo_amounts = ['0'] + ['1000', '1000-x_{n}', 'x_{n}', '0'] * 4 +  ['1000', '1000-x_{n}', '0']
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        saloon_amounts = ['n\\times1000', '(n-1)\\times1000', '(n-2)\\times1000', '(n-\\dots)\\times1000', '1000', '0']
        saloon_amt_idx = ValueTracker(0)
        saloon_amt_txt = Tex(f'${saloon_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)

        depot_amounts = ['1000', '1000-2x_{n}', '2\\times(1000-2x_{n})', '\\dots\\times(1000-2x_{n})', '(n-1)\\times(1000-2x_{n})', '(n-1)\\times(1000-2x_{n}) + (1000-x_{n})']
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

        for idx_ in range(5):
            saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
            cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
            self.play(
                Transform(saloon_amt_txt, update_saloon_amount()),
                Transform(cargo_amt_txt, update_cargo_amount()),
            )
            if idx_ == 4:
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

            if idx_ < 4:
                cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
                self.play(
                    camel_position.animate.set_value(0),
                    Transform(cargo_amt_txt, update_cargo_amount().shift(8 * LEFT)),
                )
            else:
                self.remove(cargo_amt_txt)

            if idx_ >= 3:
                self.wait()
        return