import vec_2d as v
import object as o
import draw as d

#=== Handles all the collisions by using mtv and Sat ===

class collision_world:
    def __init__(self) -> None:
        self.objects = []

    def add_collider(self,object):  #adds a obect to be considered for collisions
        self.objects.append(object)

    def get_player_exists(self) -> bool: #checks if alrady a player object exists
        for i in self.objects: 
            try: 
                if i.is_player: return True
            except: pass
        return False

    def update(self,resolve:bool=False,show_a:bool=False,show_mtv:bool=False):
        # Starts updating the collisions with the given settings
        if len(self.objects) >= 2:
            self.broad_phase(resolve,show_a,show_mtv)
    
    def broad_phase(self,resolve,show_a,show_mtv):
        def sphere_col(ob1,ob2): #check collision of two bounding spheres
            distance = ob1.pos.ret_sub(ob2.pos).length()
            rad1 = ob1.bounding_rad*ob1.size
            rad2 = ob2.bounding_rad*ob2.size
            if distance <=  rad1+rad2:
                return True
            return False

        for i in range(len(self.objects)): #check every sphere against every other
            for j in range(i+1,len(self.objects)):
                if sphere_col(self.objects[i],self.objects[j]):
                    self.narrow_phase(self.objects[i],self.objects[j],resolve,show_a,show_mtv)

    def narrow_phase(self,ob1,ob2,resolve,show_a,show_mtv): #SAT
        test_col = []               	#a list of the results of SAT (True and False)
        mtv , depth = None , None       #initialize mtv and depth

        def Sat(normal,mtv,depth):      #The whole Sat/Mtv algorithm
            projection1 = []
            projection2 = []

            for j in ob1.transformed_points: projection1.append(i.skal(j)) #project all points on normal
            for j in ob2.transformed_points: projection2.append(i.skal(j)) # "

            p1_min, p1_max = min(projection1),max(projection1) # define min and max points on normal axis
            p2_min, p2_max = min(projection2),max(projection2) # define min and max points on normal axis

            if p1_max < p2_min or p2_max < p1_min: #test overlap
                test_col.append(False)  #does not overlap / you could return if not using mtv
            else:
                test_col.append(True)   #does overlap

                #calculate depth
                x = max(p1_min,p2_min)      
                y = min(p1_max,p2_max)     
                overlap = max(x,y)-min(x,y)
                #orienting the MTV
                if p1_min < p2_min: overlap *= -1   

                #check if new overlap ist smaller tha depth
                if depth == None: depth,mtv = overlap,normal
                elif  abs(overlap) < abs(depth): depth,mtv = overlap,normal

            if show_a: # shows the axis to visualize
                d.line(i.ret_skalmul(min(projection1)),i.ret_skalmul(max(projection1)),3,(0,90,0),anti=True)

                d.line(i.ret_skalmul(min(projection2)).ret_add(v.vec(4,4)),
                i.ret_skalmul(max(projection2)).ret_add(v.vec(4,4)),3,(190,0,0),anti=True)

            return mtv , depth #return results of SAT


        #for all normals of both objects
        for i in ob1.normals:  mtv , depth = Sat(i, mtv, depth)
        for i in ob2.normals:  mtv , depth = Sat(i, mtv , depth)

        # Resolve collision with calculated mtv
        if resolve:
            if False not in test_col:       #if both objects really colide
                if ob1.is_moveable and ob2.is_moveable : #if both objects are allowed to move
                    if  ob1.is_player   : 
                        ob2.move(mtv.ret_skalmul(-depth))
                    elif ob2.is_player  : 
                        ob1.move(mtv.ret_skalmul(depth))
                    else:
                        ob1.move(mtv.ret_skalmul(depth/2))
                        ob2.move(mtv.ret_skalmul(-depth/2))
                if ob1.is_moveable:     ob1.move(mtv.ret_skalmul(depth))    # moves object 1 if object 2 is static
                elif ob2.is_moveable:   ob2.move(mtv.ret_skalmul(-depth))   # moves object 2 if object 1 is static
        
        if show_mtv:
                d.circle(v.vec(0,0,),5,(0,0,0),anti=True)
                d.line(v.vec(0,0),mtv.ret_skalmul(depth),color=(13,13,13),anti=True)
        #ob1.set_color((15,15,40)) if False in test_col else ob1.set_color((12,240,12))
        