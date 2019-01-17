import string

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.dialog import DialogLoader
from mycroft.util.log import getLogger

__author__ = 'Jan Newmarch jan@newmarch.name'

'''
This is a test skill for "Mycroft with failing intents

and accepts the command

  * test fail intent

It should return a null value signalling success
'''


LOGGER = getLogger(__name__)

class TestFail_2_Skill(MycroftSkill):
    def __init__(self):
        super(TestFail_2_Skill, self).__init__(name="TestFail_2_Skill")

    def initialize(self):
        pass
    
    @intent_handler(IntentBuilder("SucceedIntent").\
                    require("TestKeywords").build())
    def fail_intent(self, message):
        """Fail this intent
        """
        self.speak_dialog("succeed")
        return None
     
    def stop(self):
        pass

    
def create_skill():
    return TestFail_2_Skill()


