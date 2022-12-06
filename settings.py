class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.bullet_width = 4
        self.bullet_height = 18
        self.bullet_color = (28,28,28)
        self.bullets_allowed = 4
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 14
        self.speedup_scale = 1
        self.score_scale = 1.4
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 0.7
        self.alien_points = 48
    def increase_speed(self):
        self.ship_speed_factor = self.speedup_scale
        self.bullet_speed_factor = self.speedup_scale
        self.alien_speed_factor = self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)