#define fall class

class Fall:
    def __init__(self, f_rope, f_height, c_mass, b_mass, stat_elong = 0.09):
        self.f_rope = f_rope
        self.f_height = f_height
        self.c_mass = c_mass
        self.b_mass = b_mass
        self.stat_elong = stat_elong

#define methods
    def fall_factor(self):
        return self.f_height/self.f_rope

    def force_c_calc(self):
        force_constant = (self.c_mass * 9.81)/self.stat_elong
        force_experienced = ((self.c_mass * 9.81) + ((self.c_mass * 9.81)**2 + 2 * (self.f_height/self.f_rope) * self.c_mass * 9.81 * force_constant)**0.5)/1000
        return force_experienced

    
  
    

#welcome string
welcome = """Climbing Force Calculator

------
DISCLAIMER: While this programme does its best to approximate the forces experienced by the climber, the belayer and the gear in the event of a fall, these are only approximations.

Real world events include a range of factors which are not included in the scope of these calculations and the results from these calculations should not be taken as accurate.

Climbing is a dangerous sport with genuine risk to life. Please climb safely.
------
"""
print(welcome)
rope_length = float(input("How high off the deck where you when you fell in metres? "))
fall_height = float(input("How far did you fall in metres? "))
climber_mass = float(input("What is your mass in kg? "))
belayer_mass = float(input("What is the mass of your belayer? "))
static_elong = input("If you know it, what is the static elongation of the rope used in the fall as a decimal value? If you aren't sure, leave this blank. ")

if static_elong != "":
    static_elong = float(static_elong)
    fall = Fall(rope_length, fall_height, climber_mass, belayer_mass, static_elong)
else:
    fall = Fall(rope_length, fall_height, climber_mass, belayer_mass)

force_b = fall.force_c_calc() * 0.66
    
force_g = fall.force_c_calc() + force_b

results = """
Approximate fall force values:
-----
Fall factor: {ff}
Force on climber: {fc} KN
Force on belayer: {fb} KN
Force on gear: {fg} KN
-----
""".format(ff = round(fall.fall_factor(), 2), fc = round(fall.force_c_calc(), 2), fb = round(force_b, 2), fg = round(force_g, 2))

print(results)