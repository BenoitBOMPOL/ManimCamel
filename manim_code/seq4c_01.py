from manim import *

class seq4c_01(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).move_to(6 * LEFT + 3.0 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        x_point = Dot(color = TEAL).move_to(3 * LEFT + 3.0 * UP)
        x_txt = Tex('$x^{\\star}=333.33\\dots$').set_color(TEAL).scale(0.4).next_to(x_point, direction=UP, buff=MED_LARGE_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 12 * RIGHT)

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(line)
        self.add(saloon, s_txt)
        self.add(x_point, x_txt)
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)
        
        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 9 * RIGHT))

        cargo_value = ValueTracker(0)
        cargo_txt = always_redraw(
            lambda: DecimalNumber(
                cargo_value.get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))
        
        saloon_value = ValueTracker(2000)
        saloon_txt = always_redraw(
            lambda: DecimalNumber(
                saloon_value.get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(saloon.get_center() + 0.3 * UP))
        
        depot_value = ValueTracker(0)
        depot_txt = always_redraw(
            lambda: DecimalNumber(
                depot_value.get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(x_point.get_center() + 0.3 * UP))

        self.play(Create(camel))
        self.play(Write(saloon_txt), Write(cargo_txt))

        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            saloon_value.animate.set_value(1000),
            cargo_value.animate.set_value(1000),
        )

        step02_txt = Tex('\\textbf{Déplacement} du Chameau de 333.33$\\dots$ m').scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        self.play(
            cargo_value.animate.set_value(2000/3),
            camel_position.animate.set_value(1/3),
        )

        self.play(
            Write(depot_txt)
        )

        step03_txt = Tex('\\textbf{Chargement} de 333.33$\\dots$ bananes au dépôt').scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        self.play(
            cargo_value.animate.set_value(1000/3),
            depot_value.animate.set_value(1000/3),
        )

        step04_txt = Tex('\\textbf{Retour} du Chameau au Saloon').scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        self.play(
            camel_position.animate.set_value(0),
            cargo_value.animate.set_value(0),
        )

        step05_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        self.play(
            saloon_value.animate.set_value(0),
            cargo_value.animate.set_value(1000),
        )

        self.play(
            Unwrite(saloon_txt)
        )

        step06_txt = Tex('\\textbf{Déplacement} du Chameau au dépôt').scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        self.play(
            cargo_value.animate.set_value(2000/3),
            camel_position.animate.set_value(1/3),
        )

        step07_txt = Tex('\\textbf{Transfert} de 666.66$\\dots$ bananes vers le chameau').scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depot_value.animate.set_value(0),
        )

        self.play(
            Unwrite(depot_txt)
        )
        
        step08_txt = Tex('\\textbf{Déplacement} du Chameau de 1000 m').scale(0.4).next_to(step07_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        final_camel_pos = Star().set_color(ORANGE).set_fill(ORANGE, 1).scale(0.05).move_to(6 * RIGHT + 3 * UP)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            cargo_value.animate.set_value(0),
            Transform(camel, final_camel_pos),
        )

        f_txt = Tex('Arrivée : $1333.33\\dots$ m').set_color(ORANGE).scale(0.6).to_corner(UR)
        self.play(
            Unwrite(cargo_txt), Write(f_txt)
        )
        self.remove(hist_cen_line, hist_left_line, hist_upp_txt, *history_moves)
        self.wait()