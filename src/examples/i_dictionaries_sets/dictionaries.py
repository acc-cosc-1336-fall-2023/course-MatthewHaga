def test_config():
    return True
def remove_inventory(widget_name, inventory):
    if widget_name in inventory:
        del inventory[widget_name]
        del inventory[widget_name]

def play_both_sports(set1,set2):
    set = set1.intersection(set2)
    return set

def plays_one_sport(set1,set2):
    set = set1.symmetric_difference(set2)
    return set

def play_sports_union(set1,set2):
    set = set1.union(set2)
    return set

def plays_1st_sport(set1,set2):
    first_sport = set1.difference(set2)
    return first_sport

def plays_2nd_sport(set1,set2):
    second_sport = set2.difference(set1)
    return second_sport

def difference_and_add(set1,set2):
    first_sport = set1.difference(set2)
    second_sport = set2.difference(set1)
    return first_sport, second_sport
    single_sport = first_sport.union(second_sport)

    return single_sport