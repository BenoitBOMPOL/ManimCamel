from manim import *

class seq3a_02(Scene):
    def construct(self):
        origin = Dot().move_to(6 * LEFT + 2 * UP)
        dots = [Dot().scale(0.8).move_to((-2 + 4 * idx_) * RIGHT + 2 * UP) for idx_ in range(3)]
        line = Line(6 * LEFT + 2 * UP, 6 * RIGHT + 2 * UP)
        m_txts = [Text(f'{idx_} m').scale(0.25).move_to((-6 + 4 * idx_) * RIGHT + 2.2 * UP) for idx_ in range(4)]
        self.play(Create(origin), *[Create(dot_) for dot_ in dots], Create(line))
        self.play(*[Create(mtxt_) for mtxt_ in m_txts])
        self.wait()
    
        nb_bananas = 4

        cargo_value = ValueTracker(0)
        cargo_txt = always_redraw(lambda: DecimalNumber(cargo_value.get_value(), num_decimal_places = 0)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                        ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))

        camel = Dot(color = ORANGE).move_to(origin.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(origin.get_center() + camel_position.get_value() * 4 * RIGHT))
        
        camel_position = ValueTracker(0)
        depots : dict[int, ValueTracker] = {0 : ValueTracker(nb_bananas)}
        depots_pos : dict[int, float] = {0 : 0.0}
        depots_txt : dict[int, Mobject] = {
            0 : always_redraw(lambda: DecimalNumber(depots[0].get_value(), num_decimal_places = 0)
                              .set_color(YELLOW_C)
                              .scale(0.4)
                              .move_to(origin.get_center() + depots_pos[0] * 4 * RIGHT + 0.35 * UP)
                              )
                            }
        depots_shp = {
            0 : VGroup(
                Tex('Saloon').set_color(YELLOW_C).scale(0.5).move_to(camel.get_center() + 0.6 * UP)
                )}
        self.play(Create(camel), Write(cargo_txt))
        self.play(Write(depots_txt[0]), Create(depots_shp[0]))

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)

        # Dépôt vers Cargo
        step00_txt = Tex('\\textbf{Chargement} de 3 bananes du Saloon vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step00_txt)
        history_moves.append(step00_txt)
        self.play(
            depots[0].animate.set_value(depots[0].get_value() - 3),
            cargo_value.animate.set_value(cargo_value.get_value() + 3)
        )

        # Déplacement du Chameau
        step01_txt = Tex('\\textbf{Déplacement} du Chameau de 1 mètre').scale(0.4).next_to(step00_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step01_txt)
        history_moves.append(step01_txt)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            cargo_value.animate.set_value(cargo_value.get_value() - 1)
        )

        depots[1] = ValueTracker(0)
        depots_pos[1] = 1.0
        depots_txt[1] = always_redraw(lambda: DecimalNumber(depots[1].get_value(), num_decimal_places = 0)
                              .set_color(YELLOW_C)
                              .scale(0.4)
                              .move_to(origin.get_center() + depots_pos[1] * 4 * RIGHT + 0.35 * UP)
                              )
        depots_shp[1] = VGroup(
                Tex('(D1)').set_color(YELLOW_C).scale(0.5).move_to(origin.get_center() + 4 * depots_pos[1] * RIGHT + 0.6 * UP)
                )
        self.play(Write(depots_txt[1]), Create(depots_shp[1]))

        step02_txt = Tex("\\textbf{Dépôt} d'1 banane au dépôt").scale(0.4).next_to(step01_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step02_txt)
        history_moves.append(step02_txt)
        self.play(
            cargo_value.animate.set_value(cargo_value.get_value() - 1),
            depots[1].animate.set_value(depots[1].get_value() + 1)
        )

        step03_txt = Tex("\\textbf{Retour} du Chameau au Saloon").scale(0.4).next_to(step02_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step03_txt)
        history_moves.append(step03_txt)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() - 1),
            cargo_value.animate.set_value(cargo_value.get_value() - 1)
        )

        step04_txt = Tex("\\textbf{Chargement} d'1 banane du Saloon vers le Chameau").scale(0.4).next_to(step03_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step04_txt)
        history_moves.append(step04_txt)
        self.play(
            depots[0].animate.set_value(depots[0].get_value() - 1),
            cargo_value.animate.set_value(cargo_value.get_value() + 1)
        )
        self.play(Unwrite(depots_txt[0]), Uncreate(depots_shp[0]))

        step05_txt = Tex('\\textbf{Déplacement} du Chameau de 1 mètre').scale(0.4).next_to(step04_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step05_txt)
        history_moves.append(step05_txt)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            cargo_value.animate.set_value(cargo_value.get_value() - 1)
        )

        step06_txt = Tex("\\textbf{Chargement} d'1 banane du dépôt vers le Chameau").scale(0.4).next_to(step05_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step06_txt)
        history_moves.append(step06_txt)
        self.play(
            depots[1].animate.set_value(depots[1].get_value() - 1),
            cargo_value.animate.set_value(cargo_value.get_value() + 1)
        )
        self.play(Unwrite(depots_txt[1]), Uncreate(depots_shp[1]))

        step07_txt = Tex('\\textbf{Déplacement} du Chameau de 1 mètre').scale(0.4).next_to(step06_txt, DOWN, aligned_edge=LEFT, buff = MED_SMALL_BUFF)
        self.add(step07_txt)
        history_moves.append(step07_txt)
        self.play(
            camel_position.animate.set_value(camel_position.get_value() + 1),
            cargo_value.animate.set_value(cargo_value.get_value() - 1)
        )
        self.play(Uncreate(cargo_txt))
        self.remove(*history_moves, hist_left_line, hist_upp_txt, hist_cen_line)
        self.wait()
