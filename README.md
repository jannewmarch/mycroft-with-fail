# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/robot.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/>
Mycroft core with intent succeed/fail tests

## About 
In standard Mycroft all intents succeed. This is an extension that allows an intent to fail, in which case another intent matching the utterance can be tried. 

## Status
Alpha - still has some bugs.
No tests are currently included

## Files
* skills/core.py
* skills/intent_service.py
* engine.py - replaces .venv/lib/python3.5/site-packages/adapt/engine.py

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


## Credits 
Jan Newmarch (jan@newmarch.name)


## Tags
#Mycroft
#Digital assistants


