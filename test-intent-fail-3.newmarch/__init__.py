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

It should return a non-null value signalling failure
But if it is runs after test-intent-fail-2, it should never get here
'''


LOGGER = getLogger(__name__)

class TestFail_3_Skill(MycroftSkill):
    def __init__(self):
        super(TestFail_3_Skill, self).__init__(name="TestFail_3_Skill")

    def initialize(self):
        pass
    
    @intent_handler(IntentBuilder("FailIntent").\
                    require("TestKeywords").build())
    def fail_intent(self, message):
        """Fail this intent
        """
        self.speak_dialog("fail")
        return False
     
    def stop(self):
        pass

    
def create_skill():
    return TestFail_3_Skill()


