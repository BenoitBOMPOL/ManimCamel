from manim import *

class seq4d_02(Scene):
    def construct(self):
        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(saloon.get_center(), saloon.get_center() + 12 * RIGHT)

        x1_val = ValueTracker(0.5)
        x2_val = ValueTracker(0.5)
        x1_dot = Dot(color = TEAL_D)
        x2_dot = Dot(color = RED_D)
        
        stretch_factor = 8
        x1_dot.add_updater(lambda m : m.move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT))
        x2_dot.add_updater(lambda m : m.move_to(saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT))
        
        s_x1_line = Line(saloon.get_center(), x1_dot.get_center()).set_color(TEAL_D)
        s_x1_line.add_updater(lambda l_ : l_.put_start_and_end_on(saloon.get_center(), x1_dot.get_center()))

        x1_x2_line = Line(x1_dot.get_center(), x2_dot.get_center()).set_color(RED_D)
        x1_x2_line.add_updater(lambda l_ : l_.put_start_and_end_on(x1_dot.get_center(), x2_dot.get_center()))

        x1_txt = Tex('$x_{1}$').set_color(TEAL_D).scale(0.5).add_updater(lambda t_ : t_.move_to(s_x1_line.get_center() + 0.25 * UP))
        x2_txt = Tex('$x_{2}$').set_color(RED_D).scale(0.5).add_updater(lambda t_ : t_.move_to(x1_x2_line.get_center() + 0.25 * UP))

        d1_txt = Tex('$(D1)$').set_color(TEAL_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x1_dot.get_center() + 0.6 * UP))
        d2_txt = Tex('$(D2)$').set_color(RED_D).scale(0.4).add_updater(lambda t_ : t_.move_to(x2_dot.get_center() + 0.6 * UP))

        self.play(Create(line), Create(saloon), Write(s_txt))
        self.wait()
        self.play(Create(s_x1_line), Create(x1_dot), Write(x1_txt), Write(d1_txt))
        self.play(Create(x1_x2_line), Create(x2_dot), Write(x2_txt), Write(d2_txt))
        self.wait()
        self.play(
            x1_val.animate.set_value(1/5),
            x2_val.animate.set_value(1/3)
        )
        self.play(
            elt_.animate.shift(3 * UP) for elt_ in [saloon, s_txt, line, x1_dot, x2_dot, s_x1_line, x1_x2_line, x1_txt, x2_txt, d1_txt, d2_txt]
        )
        self.wait()

        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * stretch_factor * RIGHT))
        self.play(Create(camel))
        
        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)
        
        cargo_amounts = '0,1000,1000-x_{1},x_{1},0,1000,1000-x_{1},x_{1},0,1000,1000-x_{1},0,1000,1000-x_{2},x_{2},0,2000-5x_{1},2000-5x_{1}-x_{2},3000-5x_{1}-3x_{2},0'.rsplit(',')
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        depots = {
            0 : '3000,2000,1000,0'.rsplit(','),
            1 : '0,1000-2x_{1},2000-4x_{1},3000-5x_{1},2000-5x_{1},0'.rsplit(','),
            2 : '0,1000-2x_{2},0'.rsplit(',')
        }
        
        depots_pos = {
            0 : 0.0,
            1 : x1_val.get_value(),
            2 : x1_val.get_value() + x2_val.get_value()
        }

        depots_idx = {
            0 : ValueTracker(0),
            1 : ValueTracker(0),
            2 : ValueTracker(0),
        }

        depots_txt = {
            0 : Tex(f'${depots[0][0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[0] * stretch_factor * RIGHT + 0.25 * UP),
            1 : Tex(f'${depots[1][0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[1] * stretch_factor * RIGHT + 0.25 * UP),
            2 : Tex(f'${depots[2][0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[2] * stretch_factor * RIGHT + 0.25 * UP),
        }

        def update_cargo_amount():
            new_idx = int(cargo_amt_idx.get_value())
            new_text = Tex(f'${cargo_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)
            return new_text

        self.play(Write(depots_txt[0]), Write(cargo_amt_txt))
        def update_depot_amount(idx):
            new_idx = int(depots_idx[idx].get_value())
            new_text = Tex(f'${depots[idx][new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + depots_pos[idx] * stretch_factor * RIGHT + 0.25 * UP)
            return new_text
        
        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[0].set_value(depots_idx[0].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[0], update_depot_amount(0)),
        )

        step02_txt = Tex("\\textbf{Déplacement} du Chameau de $x_{1}$ mètres").scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT + 0.25 * DOWN)),
        )
        self.play(Write(depots_txt[1]))

        step03_txt = Tex("\\textbf{Transfert} de $1000 - 2x_{1}$ bananes du Chameau vers $(D1)$").scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[1].set_value(depots_idx[1].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[1], update_depot_amount(1)),
        )

        step04_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(0.0),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + 0.25 * DOWN)),
        )
        
        step05_txt = Tex("\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau").scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[0].set_value(depots_idx[0].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[0], update_depot_amount(0)),
        )

        step06_txt = Tex("\\textbf{Déplacement} du Chameau en $(D1)$").scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT + 0.25 * DOWN)),
        )

        step07_txt = Tex("\\textbf{Transfert} de $1000 - 2x_{1}$ bananes du Chameau vers $(D1)$").scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[1].set_value(depots_idx[1].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[1], update_depot_amount(1)),
        )

        step08_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step07_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(0.0),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + 0.25 * DOWN)),
        )

        step09_txt = Tex("\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau").scale(0.4).next_to(step08_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step09_txt)
        history_moves.append(step09_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[0].set_value(depots_idx[0].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[0], update_depot_amount(0)),
        )
        self.play(Unwrite(depots_txt[0]))
        history_moves.append(step09_txt)

        step10_txt = Tex("\\textbf{Déplacement} du Chameau en $(D1)$").scale(0.4).next_to(step09_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step10_txt)
        history_moves.append(step10_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT + 0.25 * DOWN)),
        )
        
        step11_txt = Tex("\\textbf{Transfert} de $1000 - x_{1}$ bananes du Chameau vers $(D1)$").scale(0.4).next_to(step10_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step11_txt)
        history_moves.append(step11_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[1].set_value(depots_idx[1].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[1], update_depot_amount(1)),
        )
        self.wait()

        dummy12txt = Text('Actions :').scale(0.4).next_to(hist_cen_line.get_start(), RIGHT, aligned_edge=UP)
        step12_txt = Tex("\\textbf{Chargement} de 1000 bananes de (D1) vers le Chameau").scale(0.4).next_to(dummy12txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step12_txt)
        history_moves.append(step12_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[1].set_value(depots_idx[1].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[1], update_depot_amount(1)),
        )

        step13_txt = Tex("\\textbf{Déplacement} du Chameau de $x_{2}$ mètres").scale(0.4).next_to(step12_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step13_txt)
        history_moves.append(step13_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value() + x2_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT + 0.25 * DOWN)),
        )

        step14_txt = Tex("\\textbf{Transfert} de $1000 - 2x_{2}$ bananes du Chameau vers $(D1)$").scale(0.4).next_to(step13_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.play(Write(depots_txt[2]))
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[2].set_value(depots_idx[2].get_value() + 1)
        self.add(step14_txt)
        history_moves.append(step14_txt)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[2], update_depot_amount(2)),
        )

        step15_txt = Tex("\\textbf{Retour} du Chameau en $(D1)$").scale(0.4).next_to(step14_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step15_txt)
        history_moves.append(step15_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + x1_val.get_value() * stretch_factor * RIGHT + 0.25 * DOWN)),
        )

        step16_txt = Tex("\\textbf{Transfert} de $Q(D1) - 1000$ bananes de $(D1)$ vers le Chameau").scale(0.4).next_to(step15_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step16_txt)
        history_moves.append(step16_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[1].set_value(depots_idx[1].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[1], update_depot_amount(1)),
        )

        step17_txt = Tex("\\textbf{Déplacement} du Chameau en $(D2)$").scale(0.4).next_to(step16_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.play(Unwrite(depots_txt[1]))
        self.add(step17_txt)
        history_moves.append(step17_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(x1_val.get_value() + x2_val.get_value()),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + (x1_val.get_value() + x2_val.get_value()) * stretch_factor * RIGHT + 0.25 * DOWN)),
        )

        step18_txt = Tex("\\textbf{Transfert} de $1000-2x_{2}$ bananes de $(D2)$ vers le Chameau").scale(0.4).next_to(step17_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step18_txt)
        history_moves.append(step18_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        depots_idx[2].set_value(depots_idx[2].get_value() + 1)
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Transform(depots_txt[2], update_depot_amount(2)),
        )
        self.play(
            Unwrite(depots_txt[2])
        )

        step19_txt = Tex("\\textbf{Déplacement} du Chameau de $Q(D2)$").scale(0.4).next_to(step18_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step19_txt)
        history_moves.append(step19_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value((3 - 2 * x1_val.get_value() - 4 * x2_val.get_value())),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + (3 - 2 * x1_val.get_value() - 4 * x2_val.get_value()) * stretch_factor * RIGHT + 0.25 * DOWN)),
        )
        self.play(Unwrite(cargo_amt_txt))
        
        f_dot = Dot(color = GREEN_D)
        f_dot.add_updater(lambda d_ : d_.move_to(saloon.get_center() + stretch_factor * (3 - 2 * x1_val.get_value() - 4 * x2_val.get_value()) * RIGHT))
        self.play(Create(f_dot))
        x2_f_line = Line(x2_dot.get_center(), f_dot.get_center()).set_color(GREEN_D)
        self.play(Create(x2_f_line))
        f_txt = Tex('$(F)$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.6 * UP)
        f_pos_txt = Tex('$x_{1} + x_{2} + (3000-5x_{1}-3x_{2})$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.3 * UP)
        self.play(Write(f_txt), Write(f_pos_txt))
        self.play(Transform(f_pos_txt, Tex('$3000 - 4x_{1} - 2x_{2}$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.3 * UP)))
        self.wait()
