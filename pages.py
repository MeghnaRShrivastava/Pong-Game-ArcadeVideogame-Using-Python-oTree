from ._builtin import Page, WaitPage
import time

class game_setup(Page):
    pass

page_sequence = [
    game_setup
 ]



class Start(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 5*60


class Page1(Page):
    form_model = 'player'
    form_fields = ['accept']

    timeout_seconds = 60
    timeout_submission = {'accept': True}


class MyPage(Page):

    def get_timeout_seconds(self):
        return self.session.config['my_page_timeout_seconds']