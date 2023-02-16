#end corona

def end_corona(recovers, new_cases, active_cases):
    import math
    delta = recovers - new_cases
    days_to_reach_zero = active_cases / delta
    return (math.ceil(days_to_reach_zero))

print(end_corona(4000, 2000, 77000))
