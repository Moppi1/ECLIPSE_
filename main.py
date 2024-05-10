# === Main ===
# imports
import object as o
import draw as d
import vec_2d as v
import collision_detection as c
import set_inter as s

# === MAIN ===
def main():
    while True: #main  loop
        d.clear()

        deltatime = d.delta_time()/1000
        inputs(deltatime,player)

        
        player.render(True,True)
        if settings.show_polygon:   #starts rendering cube if it is visible
            polygon.render(settings.show_poly_normals
            ,settings.show_boundingspheres)
        if settings.show_square:    #starts rendering square if it is visible
            cube.render(settings.show_square_normals
            ,settings.show_boundingspheres)

        col_world.update(settings.do_collision_resolve,
        settings.show_projections,settings.show_mtv)

        d.update()

def inputs(t,ob):
    if d.key("q"): ob.scale(20*t)
    if d.key("e"): ob.scale(-20*t)
    speed = settings.player_speed #pixels per second
    if d.key("w"): ob.move(v.vec(0,speed*t))
    if d.key("s"): ob.move(v.vec(0,-speed*t))
    if d.key("d"): ob.move(v.vec(speed*t,0))
    if d.key("a"): ob.move(v.vec(-speed*t,0))


if __name__ == "__main__":
    #create settings
    settings = s.settings()
    settings.load_settings("settings.txt")

    d.window(settings.screen_resolution,"Eclipse")
    d.window_seticon("icon_eclipse.png")

    col_world = c.collision_world()

    def init_player():
        player = o.object()
        player.create_shape_polygon("polygon1.txt")
        player.set_scale(100)
        player.set_color((15,15,40))
        player.activate_collision(col_world,True,settings.player_double_influence)
        return player

    def init_cube():
        cube    = o.object(v.vec(400,100))
        cube.create_shape_polygon("cube.txt")
        cube.set_scale(50)
        cube.set_color((40, 15, 39))
        cube.activate_collision(col_world,settings.square_can_move)
        return cube

    def inti_poylgon():
        polygon = o.object(v.vec(-200,-100))
        polygon.create_shape_polygon("polygon2.txt")
        polygon.set_scale(100)
        polygon.set_color((15, 38, 40))
        polygon.activate_collision(col_world,settings.polygon_can_move)
        return polygon

    player = init_player()
    if settings.show_square:    polygon = init_cube()
    if settings.show_polygon:   cube = inti_poylgon()

    main()