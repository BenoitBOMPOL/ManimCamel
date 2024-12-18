from manim import *

class seq5c_02(Scene):
    def construct(self):
        background_image = ImageMobject('manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        hist_left_line = Line(3 * UP, 3 * DOWN).to_edge(LEFT)
        self.add(hist_left_line)

        qte_txt = Tex("Quantité de bananes au dépôt :").scale(0.6).next_to(
            hist_left_line.get_start(), direction=RIGHT, buff=SMALL_BUFF
        )
        eqn_tex = Tex(
            "$(n-1)\\times(1000-2x_{n}) + (1000-x_{n})$"
        ).scale(0.6).next_to(qte_txt, direction=RIGHT, aligned_edge=DOWN, buff=SMALL_BUFF)

        self.play(Write(qte_txt))
        self.play(Write(eqn_tex))
        self.wait()

        qte2_txt = Tex("Quantité souhaitée de bananes au dépôt :").scale(0.6).next_to(
            qte_txt, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        )
        rhs_tex = Tex("$(n-1)\\times1000$"
        ).scale(0.6).next_to(qte2_txt, direction=RIGHT, aligned_edge=DOWN, buff=SMALL_BUFF)

        self.play(Write(qte2_txt))
        self.play(Write(rhs_tex))
        self.wait()

        eqn_txt = Tex(
            "Équation à résoudre : $(n-1)\\times1000 = (n-1)\\times(1000-2x_{n}) + (1000-x_{n})$"
        ).scale(0.6).next_to(qte2_txt, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        
        self.play(Write(eqn_txt))
        self.wait()

        eqn_step_1 = Tex(
            "$(n-1)\\times1000 = (n-1)\\times1000 -2(n-1)x_{n} + (1000-x_{n})$"
        ).scale(0.6).next_to(eqn_txt, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        self.play(Transform(eqn_txt, eqn_step_1))

        eqn_step_2 = Tex("$0 = -2(n-1)x_{n} + 1000-x_{n}$").scale(0.6).next_to(
            eqn_step_1, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF
        )
        self.play(Transform(eqn_txt, eqn_step_2))

        eqn_step_3 = Tex("$2(n-1)x_{n} + x_{n} = 1000$"
        ).scale(0.6).next_to(eqn_step_2, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        self.play(Transform(eqn_txt, eqn_step_3))

        eqn_step_4 = Tex("$(2n - 2 + 1)x_{n} = 1000$"
        ).scale(0.6).next_to(eqn_step_3, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        self.play(Transform(eqn_txt, eqn_step_4))

        eqn_step_5 = Tex("$(2n - 1)x_{n} = 1000$"
        ).scale(0.6).next_to(eqn_step_4, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        
        self.play(Transform(eqn_txt, eqn_step_5))

        eqn_result = Tex("$x_{n} = \\frac{1000}{2n-1}$"
        ).scale(0.6).next_to(eqn_step_5, direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        self.play(Transform(eqn_txt, eqn_result))
        
        self.wait()
        new_eqn_res = Tex("$\\boxed{x_{n} = \\frac{1000}{2n-1}}$").scale(0.6).next_to(hist_left_line.get_start(), direction = RIGHT, aligned_edge = UP, buff = MED_LARGE_BUFF).set_color(ManimColor("#8ACE00")).scale(1.2)
        self.remove(qte_txt, eqn_tex, qte2_txt, rhs_tex)
        self.play(
            Transform(
                eqn_txt,
                new_eqn_res
            )
        )

        nb_int = 10
        x_lhs_items = {}
        x_rhs_items = {}
        x_values = {}
        last_item = eqn_txt
        for idx_ in range(1, nb_int + 1):
            x_lhs_items[idx_] = Tex(f'$n = {idx_}, ' + 'x_{' + str(idx_) + '} = $').scale(0.6).next_to(last_item, direction = DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
            x_rhs_items[idx_] = Tex('$\\frac{1}{2\\times' + str(idx_) + '-1}$').scale(0.6).next_to(x_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            x_values[idx_] = 1/(2*idx_ - 1)
            self.add(x_lhs_items[idx_], x_rhs_items[idx_])
            last_item = x_lhs_items[idx_]
            new_item_rhs = Tex(f'${x_values[idx_]:.3f}$' + ' \\textrm{km}').scale(0.6).next_to(x_lhs_items[idx_], direction = RIGHT, buff = SMALL_BUFF)
            self.play(Transform(x_rhs_items[idx_], new_item_rhs))
        self.wait()
        self.remove(*list(x_lhs_items.values()))
        self.remove(*list(x_rhs_items.values()))
        self.remove(eqn_txt)
        self.wait()