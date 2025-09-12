class Head:
    def __init__(self):
        self.description = "Head"

class Hand:
    def __init__(self):
        self.description = "Hand"

class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand
        self.description = "Arm with a " + hand.description

class Feet:
    def __init__(self):
        self.description = "Feet"

class Leg:
    def __init__(self, feet: Feet):
        self.feet = feet
        self.description = "Leg with a " + feet.description

class Torso:
    def __init__(self, head: Head, right_arm: Arm, left_arm: Arm, right_leg: Leg, left_leg: Leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.description = "Torso with head, arms, and legs"

class Human:
    def __init__(self):
        # Create parts
        head = Head()

        right_hand = Hand()
        left_hand = Hand()

        right_arm = Arm(right_hand)
        left_arm = Arm(left_hand)

        right_feet = Feet()
        left_feet = Feet()

        right_leg = Leg(right_feet)
        left_leg = Leg(left_feet)

        # Assemble torso
        self.torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

    def describe(self):
        print("This human has:")
        print(f"- A {self.torso.head.description}")
        print(f"- A right arm with a {self.torso.right_arm.hand.description}")
        print(f"- A left arm with a {self.torso.left_arm.hand.description}")
        print(f"- A right leg with a {self.torso.right_leg.feet.description}")
        print(f"- A left leg with a {self.torso.left_leg.feet.description}")

person = Human()
person.describe()