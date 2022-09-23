#define fall class

class Fall:
    def __init__(self, f_rope, f_height, c_weight, b_weight, stat_elong = 0.09):
        self.f_rope = f_rope
        self.f_height = f_height
        self.c_weight = c_weight
        self.b_weight = b_weight
        self.stat_elong = stat_elong