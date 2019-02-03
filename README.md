# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/robot.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/>
Mycroft core with intent succeed/fail tests

## About 
In standard Mycroft all intents succeed.
If an intent is chosen as the bext syntactic match, it is the only one tried and will be assumed
to have succeeded.
This is an extension that allows an intent to fail, in which case another intent matching the utterance can be tried. 

## Status
Beta v0.6


## Files
* skills/core.py
* skills/intent_service.py
* engine.py - replaces .venv/lib/python3.5/site-packages/adapt/engine.py
* test/integrationtests/skills/skill_tester.py
* test-intent-fail.newmarch - see Testing

## Pseudo-code
The pseudo-code for normal intent selection and execution is
```
best intent = None
for each matching intent
    update best intent
if best intent != None
    execute intent
    return
execute fallback skills
```

This code changes this to
```
matching intent list = []
for each matching intent (> some confidence)
    add to matching intent list
sort matching intent list
for each intent in matching intent list
    execute intent
    if execution failed
        continue with next intent
    else
        exit
execute fallback skills
```

Current intents (except fallbacks) do not return a value. i.e. they return None. An intent under this scheme is considered to have failed if it returns any value (True, False, etc) except None.

## Testing
The skill testing system is modified slightly. Usually one would expect a failing test to produce no
output. For testing, both succeeding and failing skills should produce output so we can check they
have been called correctly. A new type is added to the test types of
`"expected_response_sequence"` which takes a list of responses expected. A test succeeds if all
intents for an utterance are called until one succeeds, and their dialogs match the appropriate
element of the list. The modifications are in `skill_tester.py`.

One skill is added for testing:
* test-intent-fail.newmarch
It contains three intents which all respond to the utterance `test fail skill`. The first, `fail_intent` should
fail with dialog `"Expected to fail to try next intent"`. The second,
`succeed_intent` should succeed with dialog `"Expected to succeed"`. The third,
`not_reached_intent` should not be executed. 


## Credits 
Jan Newmarch (jan@newmarch.name)


## Tags

#Mycroft

#Digital assistants


