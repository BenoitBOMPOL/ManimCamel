from manim import *

class seq4b_01(Scene):
    def construct(self):
        background_image = ImageMobject('/home/benoit/Desktop/VoyageurDesert/manim_code/blackboard.jpg').scale(2.0).set_opacity(0.6)
        self.add(background_image)
        context_txt = Tex('Position finale du chameau :').scale(0.6).to_corner(UL)
        self.play(Write(context_txt))
        dist_txt = Tex('$x+(2000-3x) = 2000 - 2x$').scale(0.6).next_to(context_txt, direction=RIGHT, buff=SMALL_BUFF)
        self.play(Write(dist_txt))
        self.play(Transform(dist_txt, Tex('$2000 - 2x$').set_color(ORANGE).scale(0.6).next_to(context_txt, direction=RIGHT, buff=SMALL_BUFF)))
        
        axes = Axes(x_range = (0, 1000, 250), y_range = (0, 2000, 500), tips = False).scale(0.8)
        axes.add_coordinates()
        x_lab = axes.get_x_axis_label('x').scale(0.6).next_to(axes.get_x_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        y_lab = axes.get_y_axis_label('\\text{Position finale}').scale(0.6).next_to(axes.get_y_axis().get_end(), aligned_edge=DL, buff=SMALL_BUFF)
        self.play(Write(axes), Write(x_lab), Write(y_lab))
        
        obj_func = axes.plot(lambda x_ : 2000 - 2 * x_).set_stroke(width = DEFAULT_STROKE_WIDTH * 0.75)
        indic_dot = Dot(color = ORANGE).move_to(axes.c2p(0, 2000))

        x_dot = Dot().scale(0.8).move_to(axes.c2p(0, 0))
        x_line = Line(axes.c2p(0, 0), axes.c2p(0, 2000)).set_stroke(width = DEFAULT_STROKE_WIDTH / 3).set_color(TEAL)
        y_dot = Dot().scale(0.8).move_to(axes.c2p(0, 2000))
        y_line = Line(axes.c2p(0, 2000), axes.c2p(0, 2000)).set_stroke(width = DEFAULT_STROKE_WIDTH / 3).set_color(ORANGE)

        self.add(x_line, y_line)
        self.add(indic_dot, obj_func)
        self.add(x_dot, y_dot)

        # Mise à jour des lignes pendant le déplacement du point
        self.play(
            Create(obj_func),
            indic_dot.animate.move_to(axes.c2p(1000, 0)),
            x_dot.animate.move_to(axes.c2p(1000, 0)),
            x_line.animate.put_start_and_end_on(axes.c2p(1000, 0), axes.c2p(1000, 0)),
            y_dot.animate.move_to(axes.c2p(0,0)),
            y_line.animate.put_start_and_end_on(axes.c2p(0, 0), axes.c2p(1000, 0)),
        )