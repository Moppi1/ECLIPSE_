import vec_2d as v
import draw as d



class object:
    def __init__(self,p:v.vec=v.vec(0,0),s:float=1,r:float=0):
        self.pos    = p
        self.size   = s
        self.rot    = r

        self.color      = (0,0,0)
        self.shape_type = None # could be : polygon , cirlce
        # self.normals
        # self.points
        # self.radius
        # self.bounding_rad
        # self.transformed_points
        # self.is_moveable
        # self.is_player

    #=== create shape colliders ===

    def calculate_collider(self,):
        self.normals = []

        # =  calculate a center point (inside Polygon) =
        surface_center = v.vec(0,0)     # init center
        for i in self.points:           
            surface_center.add(i)
        surface_center.skaldiv(len(self.points))

        # = calculate normals (Triple cross product with center) =

        highest_length = 0
        counter = 0
        for i in self.points:
            if i.length() > highest_length:
                highest_length = i.length()

            next_point = self.points[counter+1] if counter < len(self.points)-1 else self.points[0]

            towards_center  = surface_center.ret_sub(i)
            towards_next    = i.ret_sub(next_point)
            normal          = towards_next.ret_triple_cross(towards_center)

            self.normals.append(normal.ret_nor())
            counter += 1

        self.bounding_rad = highest_length # rad of bounding sphere

    def create_shape_polygon(self,path:str,res:int = 3 ):
        """point list decoder for 2d | example : 0.892 9.456"""

        self.shape_type = "polygon"
        
        # load the point list file
        file = open(path,"r")
        content = file.readlines()
        file.close()

        # initialize the reader
        self.points = []
        for i in content:
            i.replace("\n","")
            x = float(i.split(" ")[0])
            y = float(i.split(" ")[1])
            self.points.append(v.vec(round(x,res),round(y,res)))
        self.calculate_collider()
        #print("loaded point list from",path)

    def create_shape_circle(self,rad : float = 30):
        self.shape_type = "circle"
        self.radius     = rad

    def set_color(self,rgb:tuple): #sets color of the shape
        self.color = rgb

    def activate_collision(self,c_world,moveable:bool=False,player:bool=False):
        """add this object to collision world.\n the object can be moveable and """
        c_world.add_collider(self)
        self.is_player = False if c_world.get_player_exists() else player
        self.is_moveable = moveable if not self.is_player else True

    #=== render ===

    def render(self,show_n:bool=False,show_b:bool=False):
        if self.shape_type == "polygon":

            transformed_points = []
            counter = 0
            for i in self.points:
                current = i.copy()
                current.skalmul(self.size)  # Applies the Scale to the shape
                current.rot(self.rot)       # Applies the rotation
                current.add(self.pos)       # Applies the translation (order is important)
                transformed_points.append(current)

                if show_n:  #shows normals
                    d.line(current,current.ret_add(self.normals[counter].ret_skalmul(20)),3,(255,0,0))

                counter += 1

            self.transformed_points = transformed_points

            d.fill_polygon(self.transformed_points,self.color,anti=True)
            if show_b:      #show bounding sphere
                d.circle(self.pos,int(self.bounding_rad*self.size),(115, 115, 115),4,True)


        if self.shape_type == "circle": #not needed
            d.fill_circle(self.pos,self.radius,self.color,True)

    #=== Transformations ===

    # Translation
    def move(self,value : v.vec):
        self.pos = self.pos.ret_add(value)
    def set_pos(self,value : v.vec):
        self.pos = value

    # Rotation (not supported)
    def _rotate(self, rot , set=False):
        """changes rotation of object or sets it if set = True"""
        self.rot += rot
    def _set_rotation(self,rot):
        self.rot = rot

    #Scale
    def scale(self,s:float):
        self.size += s
    def set_scale(self,s:float):
        self.size = s
