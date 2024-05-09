# === Main ===
# imports
import object as o
import draw as d
import vec_2d as v
import collision_detection as c

def inputs(t,ob):
    if d.key("q"): ob.scale(20*t)
    if d.key("e"): ob.scale(-20*t)
    speed = 120 #pixels per second
    if d.key("w"): ob.move(v.vec(0,speed*t))
    if d.key("s"): ob.move(v.vec(0,-speed*t))
    if d.key("d"): ob.move(v.vec(speed*t,0))
    if d.key("a"): ob.move(v.vec(-speed*t,0))

# === MAIN ===
def main():
    while True:
        d.clear()
        deltatime = d.delta_time()/1000
        inputs(deltatime,polygon)

        polygon.render(True,True)
        polygon2.render(True,True)
        cube.render(True,True)
        col_world.update(True,False,True)

        d.update()


if __name__ == "__main__":
    d.window(2560,720,"Eclipse")

    col_world = c.collision_world()

    polygon = o.object()
    polygon.create_shape_polygon("polygon1.txt")
    polygon.set_scale(100)
    polygon.set_color((15,15,40))
    polygon.activate_collision(col_world)

    cube    = o.object(v.vec(200,100))
    cube.create_shape_polygon("cube.txt")
    cube.set_scale(50)
    cube.set_color((40, 15, 39))
    cube.activate_collision(col_world)

    polygon2 = o.object(v.vec(-200,-100))
    polygon2.create_shape_polygon("polygon2.txt")
    polygon2.set_scale(100)
    polygon2.set_color((15, 38, 40))
    polygon2.activate_collision(col_world,True)

    main()