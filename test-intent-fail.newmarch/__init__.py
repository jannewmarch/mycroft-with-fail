import string

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.dialog import DialogLoader
from mycroft.util.log import getLogger

__author__ = 'Jan Newmarch jan@newmarch.name'

'''
This is a test skill for "Mycroft with failing and succeeding intents.
Each intent accepts the command

  * test fail intent

fail should return a non-null value signalling failure
succeed returns None signalling success
not_reached should never run
'''


LOGGER = getLogger(__name__)

class TestFailSkill(MycroftSkill):
    def __init__(self):
        super(TestFailSkill, self).__init__(name="TestFailSkill")

    def initialize(self):
        pass

    # NOTE: intent names must be in this alphabetic order:
    # Fail, Good, Not
    # because intents currently loaded that way
    @intent_handler(IntentBuilder("FailIntent").\
                    require("TestKeywords").build())
    def fail_intent(self, message):
        """Fail this intent
        """
        self.speak_dialog("fail")
        return False

    @intent_handler(IntentBuilder("GoodIntent").\
                    require("TestKeywords").build())
    def good_intent(self, message):
        """Succeed this intent
        """
        self.speak_dialog("succeed")
        return None

    @intent_handler(IntentBuilder("NotReachedIntent").\
                    require("TestKeywords").build())
    def not_reached_intent(self, message):
        """Don't reach this intent
        """
        self.speak_dialog("notreached")
        return False

    def stop(self):
        pass

    
def create_skill():
    return TestFailSkill()


