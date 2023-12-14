import random

class player_brawler:

    def __init__(self, max_health, max_stamina, multiplier, dmg_1, dmg_2, dmg_3, dmg_4):

        self.max_health = max_health
        self.current_health = self.max_health
        self.max_stamina = max_stamina
        self.current_stamina = self.max_stamina
        self.dmg_1 = dmg_1
        self.dmg_2 = dmg_2
        self.dmg_3 = dmg_3
        self.dmg_4 = dmg_4
        self.flexed = False
        self.my_turn = True

    def set_my_turn(self, is_turn, stamin_up):

        self.my_turn = is_turn 

        self.current_stamina += stamin_up

        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    def heal(self):

        self.current_health = self.max_health

    def damage_taken(self, damage):

        self.current_health -= damage

        if self.current_health < 0:
            self.current_health = 0

    def ability_punch(self):
        
        self.current_stamina -= 5

        if self.current_stamina < 0:
            self.current_stamina = 0

        if self.flexed:
            self.flexed = False
            return self.dmg_1 * 3
        
        else: 
            return self.dmg_1
    
    def ability_cont(self):
        
        self.flexed = False
        self.current_stamina += 20

        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    def ability_hevpunch(self):

        self.current_stamina -= 40

        if self.current_stamina < 0:
            self.current_stamina = 0 

        if self.flexed:
            self.flexed = False
            return self.dmg_2 * 3
        
        else: 
            return self.dmg_2

    def ability_flex(self):

        self.current_stamina -= 25

        if self.current_stamina < 0:
            self.current_stamina = 0

        self.flexed = True

    def is_alive(self):

        if self.current_health <= 0:
            return False
        
        else:
            return True

class Enemy:

    def __init__(self, max_health, d1, d2):
        
        self.max_health = max_health
        self.current_health = self.max_health
        self.d1 = d1
        self.d2 = d2
        self.enemy_turn = False
    
    def damage_taken(self, damage):

        self.current_health -= damage

        if self.current_health < 0:
            self.current_health = 0
    
    def damage_done(self):

        return random.randint(self.d1, self.d2)
    
    def is_alive(self):

        if self.current_health <= 0:
            return False
        
        else:
            return True

#player = player_brawler(500, 100, 10, 12, 14, 15)
#print(player.current_health) 
#player.max_health += 600 
#print(player.max_health)

        





     




