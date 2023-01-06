#Luke, I'm your...

#Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

def relation_to_luke(relative_name):
    
    values = {
        "luke" : "Luke",
        "relations" : ["Father", "Sister", "Brother in law", "Droid"],
        "message" : "I'm your"
    }

    if relative_name == "Darth Vader":
        return f"{values['luke']}, {values['message']} {values['relations'][0]}."
    elif relative_name == "Leia":
        return f"{values['luke']}, {values['message']} {values['relations'][1]}."
    elif relative_name == "Han":
        return f"{values['luke']}, {values['message']} {values['relations'][2]}."
    elif relative_name == "R2D2":
        return f"{values['luke']}, {values['message']} {values['relations'][3]}!"
    
    return relative_name

print(f"{relation_to_luke('Darth Vader')}")
print(f"{relation_to_luke('Han')}")
print(f"{relation_to_luke('R2D2')}")
print(f"{relation_to_luke('Leia')}")
