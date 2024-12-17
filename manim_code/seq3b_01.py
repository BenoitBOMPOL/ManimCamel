from manim import *

class seq3b_01(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        saloon = Dot(color = LIGHT_BROWN).scale(0.6).move_to(4 * LEFT + 3.0 * UP)
        s_txt = Tex('$S$').set_color(LIGHT_BROWN).scale(0.65).move_to(saloon.get_center() + 0.25 * LEFT)
        x_point = Dot(color = TEAL).scale(0.6).move_to(4 * RIGHT + 3.0 * UP)
        x_txt = Tex('$x$').set_color(TEAL).scale(0.65).move_to(x_point.get_center() + 0.25 * RIGHT)
        line = Line(saloon.get_center(), x_point.get_center())
        self.add(background_image)
        self.add(line)
        self.add(saloon, s_txt)
        self.add(x_point, x_txt)

        camel = Dot(color = ORANGE).move_to(saloon.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(saloon.get_center() + camel_position.get_value() * 8 * RIGHT))

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)

        cargo_amounts = '0,1000,1000-x,x,0,1000,1000-x,x,0,1000,1000-x,0'.rsplit(',')
        cargo_amt_idx = ValueTracker(0)
        cargo_amt_txt = Tex(f'${cargo_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(camel.get_center() + 0.25 * DOWN)

        saloon_amounts = '3000,2000,1000,0'.rsplit(',')
        saloon_amt_idx = ValueTracker(0)
        saloon_amt_txt = Tex(f'${saloon_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 0.25 * UP)

        depot_amounts = '1000-2x,2\\times(1000-2x),(1000-x)+2\\times(1000-2x)'.rsplit(',')
        depot_amt_idx = ValueTracker(0)
        depot_amt_txt = Tex(f'${depot_amounts[0]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 8 * RIGHT + 0.25 * UP)

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
            new_text = Tex(f'${depot_amounts[new_idx]}$').set_color(YELLOW_C).scale(0.4).move_to(saloon.get_center() + 8 * RIGHT + 0.25 * UP)
            return new_text
        
        self.wait()
        
        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(saloon_amt_txt, update_saloon_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )

        step02_txt = Tex('\\textbf{Déplacement} du Chameau en position $x$').scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            Transform(cargo_amt_txt, update_cargo_amount().shift(8 * RIGHT)),
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
    
        step06_txt = Tex('\\textbf{Déplacement} du Chameau en position $x$').scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            Transform(cargo_amt_txt, update_cargo_amount().shift(8 * RIGHT)),
        )
    
        step07_txt = Tex('\\textbf{Transfert} des $1000-2x$ bananes du Chameau au dépôt').scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(depot_amt_txt, update_depot_amount()),
            Transform(cargo_amt_txt, update_cargo_amount())
        )

        step08_txt = Tex('\\textbf{Retour} du Chameau au Saloon').scale(0.4).next_to(step07_txt, DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        self.add(step08_txt)
        history_moves.append(step08_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(0),
            Transform(cargo_amt_txt, update_cargo_amount().shift(8 * LEFT)),
        )
        
        step09_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon au Chameau').scale(0.4).next_to(step08_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step09_txt)
        history_moves.append(step09_txt)
        saloon_amt_idx.set_value(saloon_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(saloon_amt_txt, update_saloon_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        self.play(
            Unwrite(saloon_amt_txt)
        )
        
        step10_txt = Tex('\\textbf{Déplacement} du Chameau en position $x$').scale(0.4).next_to(step09_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step10_txt)
        history_moves.append(step10_txt)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            Transform(cargo_amt_txt, update_cargo_amount().shift(8 * RIGHT)),
        )
        
        step11_txt = Tex('\\textbf{Transfert} des $1000-x$ bananes du Chameau au dépôt').scale(0.4).next_to(step10_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step11_txt)
        history_moves.append(step11_txt)
        depot_amt_idx.set_value(depot_amt_idx.get_value() + 1)
        cargo_amt_idx.set_value(cargo_amt_idx.get_value() + 1)
        self.play(
            Transform(depot_amt_txt, update_depot_amount()),
            Transform(cargo_amt_txt, update_cargo_amount()),
        )
        self.play(Unwrite(cargo_amt_txt))
        
        dummy12txt = Tex('Nombre de bananes au dépôt :').scale(0.4).next_to(hist_cen_line.get_start(), RIGHT, aligned_edge=UP)
        self.add(dummy12txt)
        self.play(
            depot_amt_txt.animate.next_to(dummy12txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        )
        self.remove(hist_left_line, hist_upp_txt, *history_moves)
        simplification_text = Tex('$= (1000-x) + (2000-4x)$').set_color(YELLOW_C).scale(0.4).next_to(depot_amt_txt, RIGHT, aligned_edge=RIGHT, buff = 1.25 * LARGE_BUFF)
        result_text = Tex('$= 3000 - 5x$').set_color(YELLOW_C).scale(0.4).next_to(simplification_text, DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
        self.play(Write(simplification_text))
        self.play(Write(result_text))
        conso_bnn_txt = Tex('Nombre de bananes consommées : $\\mathbf{5}x$').scale(0.4).next_to(dummy12txt, DOWN, aligned_edge=LEFT, buff = 1.25 * LARGE_BUFF)
        self.play(Write(conso_bnn_txt))
        self.wait()
