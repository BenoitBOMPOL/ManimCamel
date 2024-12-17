from manim import *

class seq3a_04(Scene):
    def construct(self):
        origin = Dot().move_to(6 * LEFT + 2 * UP)
        dots = [Dot().scale(0.8).move_to((-2 + 4 * idx_) * RIGHT + 2 * UP) for idx_ in range(3)]
        line = Line(6 * LEFT + 2 * UP, 6 * RIGHT + 2 * UP)
        m_txts = [Text(f'{idx_} m').scale(0.25).move_to((-6 + 4 * idx_) * RIGHT + 2.2 * UP) for idx_ in range(4)]
        self.play(Create(origin), *[Create(dot_) for dot_ in dots], Create(line))
        self.play(*[Create(mtxt_) for mtxt_ in m_txts])
        self.wait()

        camel = Dot(color = ORANGE).move_to(origin.get_center())
        cargo_value = ValueTracker(0)

        init_nb_bananas : int = 3000
        camel_cargo_size : int = 1000
    
        depots : dict[int, ValueTracker] = {0 : ValueTracker(init_nb_bananas)}
        depots_pos : dict[int, float] = {0 : 0}
        depots_txt : dict[int, Mobject] = {0 : always_redraw(lambda: DecimalNumber(depots[0].get_value(), num_decimal_places = 0)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                                    .move_to(origin.get_center() + depots_pos[0] * 4 * RIGHT + 0.35 * UP)
                                                )
                                        }
        depots_shp = {
            0 : VGroup(
                Tex('Saloon').set_color(YELLOW_C).scale(0.5).move_to(camel.get_center() + 0.6 * UP)
                )}
        # Créer les textes avec toujours la valeur des ValueTrackers
        camel_cargo_txt = always_redraw(lambda: DecimalNumber(cargo_value.get_value(), num_decimal_places = 0)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                        ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))

        # Créer le camel et ajouter les valeurs dynamiques à la scène
        camel_pos_track = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(origin.get_center() + camel_pos_track.get_value() * 4 * RIGHT))
        self.play(Create(camel),
                  Write(depots_txt[0]), Create(depots_shp[0]),
                  Write(camel_cargo_txt))
        self.wait()

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt, hist_cen_line)

        step01_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            depots[0].animate.set_value(init_nb_bananas - camel_cargo_size),
            cargo_value.animate.set_value(camel_cargo_size)
        )

        step02_txt = Tex('\\textbf{Déplacement} du Chameau de 2 mètres').scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)  
        self.add(step02_txt)
        history_moves.append(step02_txt)          
        self.play(
            camel_pos_track.animate.set_value(camel_pos_track.get_value() + 2),
            cargo_value.animate.set_value(cargo_value.get_value() - 2)
        )

        depots[1] = ValueTracker(0)
        depots_pos[1] = 2
        depots_txt[1] = always_redraw(lambda: DecimalNumber(depots[1].get_value(), num_decimal_places = 0)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                                    .move_to(origin.get_center() + 4 * depots_pos[1] * RIGHT + 0.35 * UP)
                                       )
        depots_shp[1] = VGroup(
            Tex('(D1)').set_color(YELLOW_C).scale(0.5).move_to(origin.get_center() + 4 * depots_pos[1] * RIGHT + 0.6 * UP)
        )
        self.play(Write(depots_txt[1]), Create(depots_shp[1]))

        step03_txt = Tex("\\textbf{Dépôt} de 996 bananes en (D1)").scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        self.play(
            depots[1].animate.set_value(996),
            cargo_value.animate.set_value(2)
        )

        step04_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        self.play(
            camel_pos_track.animate.set_value(camel_pos_track.get_value() - 2),
            cargo_value.animate.set_value(cargo_value.get_value() - 2)
        )

        step05_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        self.play(
            depots[0].animate.set_value(depots[0].get_value() - camel_cargo_size),
            cargo_value.animate.set_value(camel_cargo_size)
        )

        step06_txt = Tex('\\textbf{Déplacement} du Chameau en (D1)').scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)            
        self.add(step06_txt)
        history_moves.append(step06_txt)
        self.play(
            camel_pos_track.animate.set_value(camel_pos_track.get_value() + 2),
            cargo_value.animate.set_value(cargo_value.get_value() - 2)
        )

        step07_txt = Tex("\\textbf{Dépôt} de 996 bananes en (D1)").scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        self.play(
            depots[1].animate.set_value(depots[1].get_value() + 996),
            cargo_value.animate.set_value(2)
        )

        step08_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step07_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)            
        self.add(step08_txt)
        history_moves.append(step08_txt)
        self.play(
            camel_pos_track.animate.set_value(camel_pos_track.get_value() - 2),
            cargo_value.animate.set_value(cargo_value.get_value() - 2)
        )
        
        step09_txt = Tex('\\textbf{Chargement} de 1000 bananes du Saloon vers le Chameau').scale(0.4).next_to(step08_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step09_txt)
        history_moves.append(step09_txt)
        self.play(
            depots[0].animate.set_value(depots[0].get_value() - camel_cargo_size),
            cargo_value.animate.set_value(camel_cargo_size)
        )

        self.play(Unwrite(depots_txt[0]), Uncreate(depots_shp[0]))

        step10_txt = Tex('\\textbf{Déplacement} du Chameau en (D1)').scale(0.4).next_to(step09_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)            
        self.add(step10_txt)
        history_moves.append(step10_txt)
        self.play(
            camel_pos_track.animate.set_value(camel_pos_track.get_value() + 2),
            cargo_value.animate.set_value(cargo_value.get_value() - 2),
        )
        
        step11_txt = Tex("\\textbf{Dépôt} de 998 bananes en (D1)").scale(0.4).next_to(step10_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step11_txt)
        history_moves.append(step11_txt)
        self.play(
            depots[1].animate.set_value(depots[1].get_value() + 998),
            cargo_value.animate.set_value(0),
        )
        history_moves.append(step11_txt)
        self.wait()
        self.remove(*history_moves, hist_left_line, hist_upp_txt, hist_cen_line)
        self.wait()
