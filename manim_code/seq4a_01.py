from manim import *

class seq4a_01(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(6 * LEFT + 3.0 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).next_to(saloon, direction=LEFT,buff=SMALL_BUFF)
        x_point = Dot(color = TEAL).scale(0.6).move_to(3 * LEFT + 3.0 * UP)
        x_txt = Tex('$x$').set_color(TEAL).scale(0.65).next_to(x_point, direction=UR, buff=MED_SMALL_BUFF)
        f_point = Dot(color = ORANGE).scale(0.6).move_to(6 * RIGHT + 3.0 * UP)
        f_txt = Tex('Arrivée : $x+(2000-3x)=2000-2x$').set_color(ORANGE).scale(0.6).next_to(f_point, direction=UL, buff=SMALL_BUFF)
        line = Line(saloon.get_center(), f_point.get_center())
        self.add(background_image)
        self.add(line)
        self.add(saloon, s_txt)
        self.add(x_point, x_txt)
        
        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 9 * RIGHT))

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)

        cargo_amounts = ['0', '1000', '1000-x', 'x', '0', '1000', '1000 - x', '2000 - 3x', '0']
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        saloon_amounts = ['2000', '1000', '0']
        saloon_amt_idx = ValueTracker(0)
        saloon_amt_txt = Tex(f'${saloon_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)

        depot_amounts = ['1000-2x', '0']
        depot_amt_idx = ValueTracker(0)
        depot_amt_txt = Tex(f'${depot_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 3 * RIGHT + 0.25 * UP)

        self.play(
            Create(camel),
            Write(saloon_amt_txt), Write(cargo_amt_txt)
        )

        # Fonction pour animer le changement basé sur le ValueTracker
        def update_saloon_amount():
            new_idx = int(saloon_amt_idx.get_value())
            new_text = Tex(f'${saloon_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)
            return new_text
        
        def update_cargo_amount():
            new_idx = int(cargo_amt_idx.get_value())
            new_text = Tex(f'${cargo_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)
            return new_text
        
        def update_depot_amount():
            new_idx = int(depot_amt_idx.get_value())
            new_text = Tex(f'${depot_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 3 * RIGHT + 0.25 * UP)
            return new_text
    
        # Exemple d'utilisation avec ValueTracker
        saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            Transform(saloon_amt_txt, update_saloon_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        
        step02_txt = Tex('\\textbf{Déplacement} du Chameau en position $x$').scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1/3),
            Transform(cargo_amt_txt, update_cargo_amount().shift(3 * RIGHT)),
        )
        
        step03_txt = Tex('\\textbf{Transfert} de $1000-2x$ bananes au dépôt').scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1),
        self.play(
            Transform(cargo_amt_txt, update_cargo_amount()),
            Write(depot_amt_txt),
        )
        
        step04_txt = Tex('\\textbf{Retour} du Chameau au Saloon').scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(0),
            Transform(cargo_amt_txt, update_cargo_amount().move_to(saloon.get_center() + 0.25 * DOWN)),
        )
        
        step05_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon au Chameau').scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(saloon_amt_txt, update_saloon_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        self.play(Unwrite(saloon_amt_txt))
        
        step06_txt = Tex('\\textbf{Déplacement} du Chameau en position $x$').scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1/3),
            Transform(cargo_amt_txt, update_cargo_amount().shift(3 * RIGHT)),
        )

        step07_txt = Tex('\\textbf{Chargement} des $1000-2x$ bananes du dépôt sur le Chameau').scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(depot_amt_txt, update_depot_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        self.play(Unwrite(depot_amt_txt))
        
        step08_txt = Tex('\\textbf{Déplacement} du Chameau de $2000-3x$ mètres').scale(0.4).next_to(step07_txt, DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            Transform(cargo_amt_txt, update_cargo_amount().shift(9 * RIGHT)),
        )
        self.play(Unwrite(cargo_amt_txt))
        self.play(Create(VGroup(f_point, f_txt)))
        self.wait()
        self.remove(hist_cen_line, hist_left_line, hist_upp_txt, *history_moves)
        self.wait()