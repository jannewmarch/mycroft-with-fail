from unittest.mock import MagicMock
from test.integrationtests.skills.skill_tester import SkillTest

def test_runner(skill, example, emitter, loader):

    # Get the skill object from the skill path
    s = [s for s in loader.skills if s and s.root_dir == skill]

    # replace the light_wrapper service with a mock
    s[0].light_wrapper = MagicMock()
    
    # Set a valid return value for discover_bulbs()
    s[0].light_wrapper.discover_bulbs.return_value = [
        {'ip': '192.168.1.25',
         'port': 55443,
         'capabilities': {'name': 'bedroom'
                        }
        },
        {'ip': '192.168.1.26',
         'port': 55443,
         'capabilities': {'name': 'lounge'
                         }
        }
    ]
 
    # Set a valid return value for new_light()
    s[0].light_wrapper.new_light.return_value = TestBulb()

    return SkillTest(skill, example, emitter).run(loader)

class TestBulb:
    def turn_on(self):
        pass

    def turn_off(self):
        pass
