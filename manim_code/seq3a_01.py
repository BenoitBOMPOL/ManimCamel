from manim import *

class seq3a_01(Scene):
    def construct(self):
        origin = Dot().move_to(6 * LEFT + 2 * UP)
        dots = [Dot().scale(0.8).move_to((-2 + 4 * idx_) * RIGHT + 2 * UP) for idx_ in range(3)]
        line = Line(6 * LEFT + 2 * UP, 6 * RIGHT + 2 * UP)
        m_txts = [Text(f'{idx_} m').scale(0.25).move_to((-6 + 4 * idx_) * RIGHT + 2.2 * UP) for idx_ in range(4)]
        self.play(Create(origin), *[Create(dot_) for dot_ in dots], Create(line))
        self.play(*[Create(mtxt_) for mtxt_ in m_txts])
        self.wait()

        cargo_value = ValueTracker(0)
        cargo_txt = always_redraw(lambda: DecimalNumber(cargo_value.get_value(), num_decimal_places = 0)
                                                    .set_color(YELLOW_C)
                                                    .scale(0.4)
                                        ).add_updater(lambda m : m.move_to(camel.get_center() + 0.3 * DOWN))

        camel = Dot(color = ORANGE).move_to(origin.get_center())
        camel_position = ValueTracker(0)
        camel.add_updater(lambda m : m.move_to(origin.get_center() + camel_position.get_value() * 4 * RIGHT))

        hist_left_line = Line(1.5 * UP, 3.5 * DOWN).to_edge(LEFT)
        hist_cen_line = Line(1.5 * UP, 3.5 * DOWN)
        hist_upp_txt = Text('Actions :').scale(0.4).next_to(hist_left_line.get_start(), RIGHT, aligned_edge=UP)
        history_moves = []
        self.add(hist_left_line, hist_cen_line, hist_upp_txt)

        ### Une banane au début ###
        for nb_bananas in range(1, 4):
            history_moves = []
            camel_position.set_value(0)
            depots : dict[int, ValueTracker] = {0 : ValueTracker(nb_bananas)}
            depots_pos : dict[int, float] = {0 : 0.0}
            depots_txt : dict[int, Mobject] = {0 : always_redraw(lambda: DecimalNumber(depots[0].get_value(), num_decimal_places = 0)
                                                        .set_color(YELLOW_C)
                                                        .scale(0.4)
                                                        .move_to(origin.get_center() + depots_pos[0] * 4 * RIGHT + 0.5 * UP)
                                                    )
                                                }
            
            self.play(Create(camel), Write(cargo_txt))
            self.play(Write(depots_txt[0]))
            
            # Dépôt vers Cargo
            act_depot_txt = Tex('\\textbf{Transfert} de ' + f'{nb_bananas} banane' + (' ' if nb_bananas < 2 else 's ') + 'du dépôt vers le Chameau').scale(0.4).next_to(hist_upp_txt, DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
            self.play(
                depots[0].animate.set_value(0),
                cargo_value.animate.set_value(depots[0].get_value()),
                Write(act_depot_txt)
            )
            history_moves.append(act_depot_txt)
            self.play(Unwrite(depots_txt[0]))
            
            # Déplacement du Chameau
            move_cargo_txt = Tex('\\textbf{Déplacement} du Chameau de ' + f'{nb_bananas} mètre' + ('.' if nb_bananas < 2 else 's.')).scale(0.4).next_to(act_depot_txt, DOWN, aligned_edge = LEFT, buff=MED_SMALL_BUFF)
            self.play(
                camel_position.animate.set_value(camel_position.get_value() + nb_bananas),
                cargo_value.animate.set_value(0),
                Write(move_cargo_txt)
            )
            history_moves.append(move_cargo_txt)
            self.play(Unwrite(cargo_txt))
            self.remove(camel)
            self.remove(*history_moves)
            if nb_bananas == 3:
                self.remove(hist_upp_txt, hist_left_line, hist_cen_line)
            self.wait()
