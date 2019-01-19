# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/robot.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/>
Mycroft core with intent succeed/fail tests

## About 
In standard Mycroft all intents succeed. This is an extension that allows an intent to fail, in which case another intent matching the utterance can be tried. 

## Status
Beta v0.5


## Files
* skills/core.py
* skills/intent_service.py
* engine.py - replaces .venv/lib/python3.5/site-packages/adapt/engine.py
* test-intent-fail-1.newmarch - see Testing
* test-intent-fail-2.newmarch - see Testing
* test-intent-fail-3.newmarch - see Testing

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
Three intents are supplied for testing:

* test-intent-fail-1.newmarch
* test-intent-fail-2.newmarch
* test-intent-fail-3.newmarch

They must be installed into the directory /opt/mycroft/skills.

They must be loaded into Mycroft in the correct order. To do this, edit mycroft/configuration/mycroft.conf and change the priority list to

    "priority_skills": ["mycroft-pairing", "mycroft-volume",
                        "test-intent-fail-1.newmarch", "test-intent-fail-2.newmarch", "test-intent-fail-3.newmarch"
                       ],

Then the query "test fail intent" should produce two responses:

    Expected to fail to try next intent
    Expected to succeed  

The first should fail allowing the second to try. This should succeed, or a third will be invoked.




## Credits 
Jan Newmarch (jan@newmarch.name)


## Tags

#Mycroft

#Digital assistants


