class Rhombus:

    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a


    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("Must be greater then 0")

            super().__setattr__(name, value)
            
        elif name == "corner_a":
            super().__setattr__(name, value)
            super().__setattr__("corner_b", 180-value)
            
        else:
            super().__setattr__(name, value)


r = Rhombus(20,70)
print(r.side_a)
print(r.corner_a)
print(r.corner_b)




