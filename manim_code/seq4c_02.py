from manim import *

class seq4c_02(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT + 3.0 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 12 * RIGHT)

        intermedots = [Dot().scale(0.8).move_to((-2 + 4 * idx_) * RIGHT + 3 * UP) for idx_ in range(3)]
        km_txts = [Text(f'{idx_ + 1} km').scale(0.25).move_to((-2 + 4 * idx_) * RIGHT + 3.25 * UP) for idx_ in range(3)]
        
        self.play(
            Create(line),
            *[Write(kmtxt_) for kmtxt_ in [s_txt] + km_txts],
            *[Create(dot_) for dot_ in [saloon] + intermedots],)
        
        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)
        
        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 4 * RIGHT))

        cargo_value = ValueTracker(0)
        cargo_txt = always_redraw(
            lambda: DecimalNumber(
                cargo_value.get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))
        
        depots_pos = {0 : 0.0}
        depots = {0 : ValueTracker(3000)}
        depots_name = {0 : Tex('Saloon').set_color(LIGHT_BROWN).scale(0.4).move_to(saloon.get_center() + depots_pos[0] * 4 * RIGHT + 0.6 * UP)}
        depots_txt = {
            0 : always_redraw(
            lambda: DecimalNumber(
                depots[0].get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(saloon.get_center() + depots_pos[0] * 4 * RIGHT + 0.3 * UP))
        }
        self.play(Write(depots_txt[0]), Write(depots_name[0]))
        self.play(Create(camel), Write(cargo_txt))
        
        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[0].animate.set_value(depots[0].get_value() - 1000),
        )

        depots_pos[1] = 0.2
        depots[1] = ValueTracker(0)
        depots_txt[1] = always_redraw(
            lambda: DecimalNumber(
                depots[1].get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(saloon.get_center() + depots_pos[1] * 4 * RIGHT + 0.3 * UP))
        depots_name[1] = Tex('(D1)').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[1] * 4 * RIGHT + 0.6 * UP)

        step02_txt = Tex('\\textbf{Déplacement} du Chameau de 200 m').scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        self.play(
            cargo_value.animate.set_value(800),
            camel_position.animate.set_value(depots_pos[1]),
        )

        step03_txt = Tex('\\textbf{Dépôt} de 600 bananes en (D1)').scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        self.play(Write(depots_txt[1]), Write(depots_name[1]))
        self.play(
            cargo_value.animate.set_value(200),
            depots[1].animate.set_value(depots[1].get_value() + 600),
        )

        step04_txt = Tex('\\textbf{Retour} du Chameau au Saloon').scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        self.play(
            cargo_value.animate.set_value(0),
            camel_position.animate.set_value(depots_pos[0]),
        )

        step05_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon au Chameau').scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[0].animate.set_value(depots[0].get_value() - 1000),
        )

        step06_txt = Tex('\\textbf{Déplacement} du Chameau en (D1)').scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        self.play(
            cargo_value.animate.set_value(800),
            camel_position.animate.set_value(depots_pos[1]),
        )

        step07_txt = Tex('\\textbf{Dépôt} de 600 bananes en (D1)').scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        self.play(
            cargo_value.animate.set_value(200),
            depots[1].animate.set_value(depots[1].get_value() + 600),
        )

        step08_txt = Tex('\\textbf{Retour} du Chameau au Saloon').scale(0.4).next_to(step07_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        self.play(
            cargo_value.animate.set_value(0),
            camel_position.animate.set_value(depots_pos[0]),
        )

        step09_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon au Chameau').scale(0.4).next_to(step08_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step09_txt)
        history_moves.append(step09_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[0].animate.set_value(depots[0].get_value() - 1000),
        )
        self.play(Unwrite(depots_txt[0]), Unwrite(depots_name[0]))
        
        step10_txt = Tex('\\textbf{Déplacement} du Chameau en (D1)').scale(0.4).next_to(step09_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step10_txt)
        history_moves.append(step10_txt)
        self.play(
            cargo_value.animate.set_value(800),
            camel_position.animate.set_value(depots_pos[1]),
        )

        step11_txt = Tex('\\textbf{Dépôt} de 800 bananes en (D1)').scale(0.4).next_to(step10_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step11_txt)
        history_moves.append(step11_txt)
        self.play(
            cargo_value.animate.set_value(0),
            depots[1].animate.set_value(depots[1].get_value() + 800),
        )

        depots_pos[2] = depots_pos[1] + 1/3
        depots[2] = ValueTracker(0)
        depots_txt[2] = always_redraw(
            lambda: DecimalNumber(
                depots[2].get_value(),
                num_decimal_places = 2
                ).set_color(YELLOW_C)
                 .scale(0.4)
            ).add_updater(lambda m : m.move_to(saloon.get_center() + depots_pos[2] * 4 * RIGHT + 0.3 * UP))
        depots_name[2] = Tex('(D2)').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[2] * 4 * RIGHT + 0.6 * UP)
        
        self.wait()
        dummy12txt = Text('Actions :').scale(0.4).next_to(hist_cen_line.get_start(), RIGHT, aligned_edge=UP)
        step12_txt = Tex('\\textbf{Chargement} de 1000 bananes de (D1) sur le Chameau').scale(0.4).next_to(dummy12txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step12_txt)
        history_moves.append(step12_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[1].animate.set_value(depots[1].get_value() - 1000),
        )

        step13_txt = Tex('\\textbf{Déplacement} du Chameau de 333.33 m').scale(0.4).next_to(step12_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step13_txt)
        history_moves.append(step13_txt)
        self.play(
            cargo_value.animate.set_value(2000/3),
            camel_position.animate.set_value(depots_pos[2]),
        )

        self.play(Write(depots_txt[2]), Write(depots_name[2]))

        step14_txt = Tex('\\textbf{Dépôt} de 333.333 bananes en (D2)').scale(0.4).next_to(step13_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step14_txt)
        history_moves.append(step14_txt)
        self.play(
            cargo_value.animate.set_value(1000/3),
            depots[2].animate.set_value(depots[2].get_value() + 1000/3),
        )

        step15_txt = Tex('\\textbf{Retour} du Chameau en (D1)').scale(0.4).next_to(step14_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step15_txt)
        history_moves.append(step15_txt)
        self.play(
            cargo_value.animate.set_value(0),
            camel_position.animate.set_value(depots_pos[1]),
        )

        step16_txt = Tex('\\textbf{Chargement} de 1000 bananes de (D1) sur le Chameau').scale(0.4).next_to(step15_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step16_txt)
        history_moves.append(step16_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[1].animate.set_value(depots[1].get_value() - 1000),
        )

        self.play(Unwrite(depots_txt[1]), Unwrite(depots_name[1]))
        step17_txt = Tex('\\textbf{Déplacement} du Chameau en (D2)').scale(0.4).next_to(step16_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step17_txt)
        history_moves.append(step17_txt)
        self.play(
            cargo_value.animate.set_value(2000/3),
            camel_position.animate.set_value(depots_pos[2]),
        )

        step18_txt = Tex('\\textbf{Chargement} de 666.66 bananes de (D2) vers le Chameau').scale(0.4).next_to(step17_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step18_txt)
        history_moves.append(step18_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[2].animate.set_value(0),
        )
        self.play(Unwrite(depots_txt[2]), Unwrite(depots_name[2]))

        self.wait()
        
        step19_txt = Tex('\\textbf{Déplacement} du Chameau de 1000 m').scale(0.4).next_to(step18_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step19_txt)
        history_moves.append(step19_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[2].animate.set_value(0),
        )

        final_camel_pos = Star().set_color(ORANGE).set_fill(ORANGE, 1).scale(0.05).move_to(saloon.get_center() + (1 + 1/5 + 1/3) * 4 * RIGHT)
        self.play(
            cargo_value.animate.set_value(0),
            camel_position.animate.set_value(camel_position.get_value() + 1),
            Transform(camel, final_camel_pos)
        )
        final_pos_txt = Tex('$1.533\\dots$ \\textrm{km}').set_color(ORANGE).scale(0.45).next_to(final_camel_pos, direction=UR, aligned_edge=UP, buff=SMALL_BUFF)
        self.play(Unwrite(cargo_txt), Write(final_pos_txt))
        self.wait()
        self.remove(*history_moves, hist_left_line, hist_upp_txt, hist_cen_line)
        self.wait()