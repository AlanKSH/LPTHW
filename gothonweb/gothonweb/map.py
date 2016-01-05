class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
                        """
                        The Gothons of Planet Percel #25 have invaded your ship and destroyed
                        your entire crew. You are the last surviving menber and your last 
                        mission is to get the neutron destruct bomb from the Weapons Armory,
                        put it in the bridge, and blow the ship up after getting into an
                        escape pod.

                        You're running down the central corridor to the Weapons Armory when a 
                        Gothon jumps out, red scaly skin, dark frimy teeth, and evil clown costume
                        flowing around his hate filled body. He's blocking the door to the Armory and
                        about to pull a weapon to blast you.
                        """)

laser_weapon_armory = Room("Laser Weapon Armory",
                           """
                           Lucky for you they made you learn Gothon insults in academy,
                           ...
                           You need a code to get the bomb out.
                           Wrong 10 times then the lock closes forever.
                           The code is 3 digits.
                           """
                           )

the_bridge = Room("The Bridge",
                  """
                  The container clicks open and ...you can to the bridge where you must place it in the right spot.
                  """
                  )

escape_pod = Room("Escape Pod",
                  """
                  You point your blaster at the bomb under your arm
                  ...
                  There's 5 pods, which one do you take?
                  """
                  )

the_end_winner = Room("The End",
                      """
                      You jump into pod 2 adn hit the eject button.
                      ...
                      You won
                      """
                      )

the_end_loser = Room("The End",
                     """
                     You jump into a ...
                     you lose.
                     """)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
    })

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb':escape_pod
    })

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*':generic_death
    })

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke!': laser_weapon_armory
    })

START = central_corridor




                           