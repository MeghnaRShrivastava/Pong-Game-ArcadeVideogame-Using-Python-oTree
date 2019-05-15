from otree.api import (
     BaseConstants, BaseSubsession, BaseGroup, BasePlayer,WaitPage

)
import random


doc = """
Ping Pong Game Setup
"""

class Constants(BaseConstants):
    name_in_url = 'pingpong'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'pingpong/game_setup.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.do_my_shuffle()

class Group(BaseGroup):
 pass

class Player(BasePlayer):
   pass #player_name = models.StringField()
