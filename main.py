import arcade

pumpkin_window = arcade.open_window(1000, 900, "Jack-O-Lantern")
arcade.set_background_color(arcade.color.PURPLE)
arcade.start_render()

arcade.draw_circle_filled(500, 450, 300, arcade.color.PUMPKIN)
arcade.draw_triangle_filled(425, 375, 500, 475, 575, 375,
                            arcade.color.BLACK)
arcade.draw_arc_outline(500, 374, 400, 100, arcade.color.BLACK, -180, 0, 7)
arcade.draw_xywh_rectangle_filled(220, 740, 560, 20, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(330, 760, 330, 100, arcade.color.BLACK)
arcade.draw_arc_filled(330, 495, 100, 200, arcade.color.BLACK, 0, 180,)
arcade.draw_arc_filled(630, 495, 100, 200, arcade.color.BLACK, 0, 180)


arcade.finish_render()

arcade.run()