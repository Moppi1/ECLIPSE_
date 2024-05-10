#=== loads the Setings ===

class settings():
    def __init__(self) -> None:
        #load default settings
        self.screen_resolution      = (2560,720)

        self.show_square            = True
        self.show_square_normals    = True
        self.square_can_move        = False

        self.show_polygon           = True
        self.show_poly_normals      = True
        self.polygon_can_move       = True

        self.player_show_normals    = True
        self.player_double_influence= False
        self.player_speed           = 100

        self.do_collision_resolve   = True

        self.show_boundingspheres   = True
        self.show_projections       = False
        self.show_mtv               = True

    def load_settings(self,path:str):
        #loads the settings
        file = open(path,"r")
        content = file.readlines()
        file.close()

        def get_bool(line)  -> bool :
            c = content[line-1].split(":")
            return c[1].replace("\n","") == " True"
        def get_res(line)   -> tuple:
            c = content[line-1].split(":")
            c = c[1].split("x")
            return (int(c[0]),int(c[1]))
        def get_int(line)   -> int  :
            c = content[line-1].split(":")
            return int(c[1])
        
        try:
            self.screen_resolution      = get_res(8)

            self.show_square            = get_bool(12)
            self.show_square_normals    = get_bool(13)
            self.square_can_move        = get_bool(14)

            self.show_polygon           = get_bool(16)
            self.show_poly_normals      = get_bool(17)
            self.polygon_can_move       = get_bool(18)

            self.player_show_normals    = get_bool(20)
            self.player_double_influence= get_bool(21)
            self.player_speed           = get_int(22)

            self.do_collision_resolve   = get_bool(26)

            self.show_boundingspheres   = get_bool(28)
            self.show_projections       = get_bool(29)
            self.show_mtv               = get_bool(30)

        except:
            print("============== warning =============")
            print("========= an error occurred ========")
            print("= not all Settings could be loaded =")