from manim import *

class seq4e_01(Scene):
    def construct(self):
        stretch_factor = 8

        saloon = Dot(color = LIGHT_BROWN).scale(0.8).move_to(6 * LEFT + 3 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.4).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        line = Line(6 * LEFT, 7 * RIGHT).shift(3 * UP)

        self.add(line, saloon, s_txt)

        x1_val = 0.2
        x2_val = 1/3
        x1_dot = Dot(color = TEAL_D).move_to(6 * LEFT + 3 * UP + x1_val * stretch_factor * RIGHT)
        x2_dot = Dot(color = RED_D).move_to(6 * LEFT + 3 * UP + (x1_val + x2_val) * stretch_factor * RIGHT)
        
        s_x1_line = Line(6 * LEFT + 3 * UP, x1_dot.get_center()).set_color(TEAL_D)
        x1_x2_line = Line(x1_dot.get_center(), x2_dot.get_center()).set_color(RED_D)

        x1_txt = Tex('$x_{1}^{\\star} = 200 \\textrm{m}$').set_color(TEAL_D).scale(0.5).move_to(s_x1_line.get_center() + 0.15 * UP)
        x2_txt = Tex('$x_{2}^{\\star} = 333.33 \\textrm{m}$').set_color(RED_D).scale(0.5).move_to(x1_x2_line.get_center() + 0.15 * UP)

        d1_txt = Tex('$(D1)$').set_color(TEAL_D).scale(0.4).move_to(x1_dot.get_center() + 0.6 * UP)
        d2_txt = Tex('$(D2)$').set_color(RED_D).scale(0.4).move_to(x2_dot.get_center() + 0.6 * UP)

        self.add(s_x1_line, x1_dot, x1_txt, d1_txt)
        self.add(x1_x2_line, x2_dot, x2_txt, d2_txt)
        
        camel = Dot(color = ORANGE).move_to(6 * LEFT + 3 * UP)
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(6 * LEFT + 3 * UP + camel_position.get_value() * stretch_factor * RIGHT))
        self.add(camel)
    
        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)

        cargo_value = ValueTracker(0)
        cargo_txt = always_redraw(lambda: DecimalNumber(cargo_value.get_value(), num_decimal_places = 2)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                        ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))

        depots = {0 : ValueTracker(3000)}
        depots_pos = {0 : 0.0}
        depots_txt = {0 : always_redraw(lambda: DecimalNumber(depots[0].get_value(), num_decimal_places = 2)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                                    .move_to(saloon.get_center() + stretch_factor * depots_pos[0] * RIGHT + 0.35 * UP)
                                       )}
        self.add(cargo_txt, depots_txt[0])
        self.wait()

        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            depots[0].animate.set_value(2000),
            cargo_value.animate.set_value(1000)
        )
        
        depots[1] = ValueTracker(0)
        depots_pos[1] = x1_val
        depots_txt[1] = always_redraw(lambda: DecimalNumber(depots[1].get_value(), num_decimal_places = 2)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                                    .move_to(saloon.get_center() + stretch_factor * depots_pos[1] * RIGHT + 0.35 * UP)
                                       )
        step02_txt = Tex("\\textbf{Déplacement} du Chameau de 200 mètres").scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        self.play(
            camel_position.animate.set_value(depots_pos[1]),
            cargo_value.animate.set_value(800)
        )
        self.add(depots_txt[1])

        step03_txt = Tex("\\textbf{Transfert} de 600 bananes du Chameau vers $(D1)$").scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        self.play(
            cargo_value.animate.set_value(200),
            depots[1].animate.set_value(600)
        )

        step04_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        self.play(
            camel_position.animate.set_value(0.0),
            cargo_value.animate.set_value(0.0)
        )
        
        step05_txt = Tex("\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau").scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        self.play(
            depots[0].animate.set_value(1000),
            cargo_value.animate.set_value(1000)
        )

        step06_txt = Tex("\\textbf{Déplacement} du Chameau en $(D1)$").scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        self.play(
            camel_position.animate.set_value(x1_val),
            cargo_value.animate.set_value(800)
        )

        step07_txt = Tex("\\textbf{Transfert} de 600 bananes du Chameau vers $(D1)$").scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        self.play(
            cargo_value.animate.set_value(200),
            depots[1].animate.set_value(depots[1].get_value() + 600)
        )

        step08_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step07_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        self.play(
            camel_position.animate.set_value(0.0),
            cargo_value.animate.set_value(0.0)
        )
        
        step09_txt = Tex("\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau").scale(0.4).next_to(step08_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step09_txt)
        history_moves.append(step09_txt)
        self.play(
            depots[0].animate.set_value(0),
            cargo_value.animate.set_value(1000)
        )

        step10_txt = Tex("\\textbf{Déplacement} du Chameau en $(D1)$").scale(0.4).next_to(step09_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step10_txt)
        history_moves.append(step10_txt)
        self.play(
            camel_position.animate.set_value(x1_val),
            cargo_value.animate.set_value(800)
        )
        self.remove(depots_txt[0])
        del depots[0]
        del depots_txt[0]
        del depots_pos[0]

        step11_txt = Tex("\\textbf{Transfert} de 800 bananes du Chameau vers $(D1)$").scale(0.4).next_to(step10_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step11_txt)
        history_moves.append(step11_txt)
        self.play(
            cargo_value.animate.set_value(0),
            depots[1].animate.set_value(depots[1].get_value() + 800)
        )

        self.wait()

        dummy12txt = Text('Actions :').scale(0.4).next_to(hist_cen_line.get_start(), RIGHT, aligned_edge=UP)
        step12_txt = Tex("\\textbf{Chargement} de 1000 bananes de (D1) vers le Chameau").scale(0.4).next_to(dummy12txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step12_txt)
        history_moves.append(step12_txt)
        self.play(
            cargo_value.animate.set_value(1000),
            depots[1].animate.set_value(1000)
        )

        step13_txt = Tex("\\textbf{Déplacement} du Chameau de $333.33$ mètres").scale(0.4).next_to(step12_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step13_txt)
        history_moves.append(step13_txt)
        self.play(
            camel_position.animate.set_value(x1_val + x2_val),
            cargo_value.animate.set_value(2000/3)
        )

        depots[2] = ValueTracker(0)
        depots_pos[2] = x1_val + x2_val
        depots_txt[2] = always_redraw(lambda: DecimalNumber(depots[2].get_value(), num_decimal_places = 2)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                                    .move_to(saloon.get_center() + stretch_factor * depots_pos[2] * RIGHT + 0.35 * UP)
                                       )
        
        self.play(Write(depots_txt[2]))
        
        step14_txt = Tex("\\textbf{Transfert} de $333.33$ bananes du Chameau vers $(D1)$").scale(0.4).next_to(step13_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step14_txt)
        history_moves.append(step14_txt)
        self.play(
            cargo_value.animate.set_value(1000 / 3),
            depots[2].animate.set_value(1000 / 3)
        )

        step15_txt = Tex("\\textbf{Retour} du Chameau en $(D1)$").scale(0.4).next_to(step14_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step15_txt)
        history_moves.append(step15_txt)
        self.play(
            camel_position.animate.set_value(x1_val),
            cargo_value.animate.set_value(0.0)
        )

        step16_txt = Tex("\\textbf{Transfert} de $1000$ bananes de $(D1)$ vers le Chameau").scale(0.4).next_to(step15_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step16_txt)
        history_moves.append(step16_txt)
        self.play(
            depots[1].animate.set_value(0.0),
            cargo_value.animate.set_value(1000)
        )
        self.remove(depots_txt[1])
        del depots[1]
        del depots_pos[1]
        del depots_txt[1]

        step17_txt = Tex("\\textbf{Déplacement} du Chameau en $(D2)$").scale(0.4).next_to(step16_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step17_txt)
        history_moves.append(step17_txt)
        self.play(
            camel_position.animate.set_value(x1_val + x2_val),
            cargo_value.animate.set_value(2000 / 3)
        )
 
        step18_txt = Tex("\\textbf{Transfert} de $333.33$ bananes de $(D2)$ vers le Chameau").scale(0.4).next_to(step17_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step18_txt)
        history_moves.append(step18_txt)
        self.play(
            depots[2].animate.set_value(0),
            cargo_value.animate.set_value(1000)
        )
        self.remove(depots_txt[2])
        del depots[2]
        del depots_pos[2]
        del depots_txt[2]
        self.wait()

        step19_txt = Tex("\\textbf{Déplacement} du Chameau de $1000$ mètres").scale(0.4).next_to(step18_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step19_txt)
        history_moves.append(step19_txt)

        self.play(
            camel_position.animate.set_value(1 + x1_val + x2_val),
            cargo_value.animate.set_value(0)
        )
        self.remove(cargo_txt)
        self.wait()

        f_dot = Dot(color = GREEN_D)
        f_dot.add_updater(lambda d_ : d_.move_to(6 * LEFT + 3 * UP + stretch_factor * (3 - 4 * x1_val - 2 * x2_val) * RIGHT))
        self.play(Create(f_dot))
        x2_f_line = Line(x2_dot.get_center(), f_dot.get_center()).set_color(GREEN_D)
        self.play(Create(x2_f_line))
        f_txt = Tex('$(F)$').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.6 * UP)
        f_pos_txt = Tex('$1.533$ \\textrm{km}').set_color(GREEN_D).scale(0.4).move_to(f_dot.get_center() + 0.3 * UP)
        self.play(Write(f_txt), Write(f_pos_txt))
        self.wait()
