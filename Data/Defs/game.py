from discord import player


class Character:

    def __init__(self, title, contemplation=0, damage=0, flashbacks=0):
        self.title = title  # The character's title or name
        self.contemplation = contemplation  # The amount of contemplation
        self.damage = damage  # The amount of damage the character has
        self.flashbacks = flashbacks  # The number of flashbacks experienced
        self.keepsakes = []  # List that holds the character's keepsakes
        self.role = "Passenger"  # Used to track their second-leg role
        self.touchstones = []  # List that holds the character's touchstones

        self.touchstone_cap = 3  # The maximum number of touchstones allowed

    def add_flashback(self, touchstone):
        self.flashbacks += 1
        # This needs more functionality!

    def add_keepsake(self, keepsake):
        self.keepsakes.append(keepsake)

    def add_touchstone(self, touchstone):
        if len(self.touchstones) < self.touchstone_cap:
            self.touchstones.append(touchstone)
        else:
            print("You can't have any more touchstones!")

    def change_contemplation(self, amount):
        self.contemplation += amount

    def change_damage(self, amount):
        self.damage += amount


class Event:

    def __init__(self, category, text, short, danger, keepsake, is_stop):
        self.category = category  # The event's category
        self.text = text  # The main text of the event
        self.short = short  # A short descriptor of the event
        self.danger = danger  # The event's danger level
        self.keepsake = keepsake  # The event's keepsake text
        self.is_stop = is_stop  # Check for if the event is a stop

    def change_danger(self, amount):
        self.danger += amount


class Game:

    def __init__(self, turn_order, has_gm=True, min_size=3, max_size=4):
        self.has_gm = has_gm  # Bool for whether there is a GM running the game
        self.turn_order = turn_order  # A list showing turn order, or None
        self.min_size = min_size  # Minimum number of players required
        self.max_size = max_size  # Maximum number of players allowed
        self.players = {}  # Dict matching players to characters
        self.events = []  # List that contains all active events

    def join(self, user):
        if len(self.players) < self.max_size:
            self.players[user] = None  # Player does not yet have character
            # Replace this with ctx message send
            print("You've joined the game!")
        else:
            # Replace this with ctx message send
            print("This game is already full!")
