states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {"kone": set(["id", "nv", "ut"]),
            "ktwo": set(["wa", "id", "mt"]),
            "kthres": set(["or", "nv", "ca"]),
            "kfour": set(["nv", "ut"]),
            "kfive": set(["ca", "az"])
            }

best_station = None
states_covered = set()
final_states = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():

        covered = states_needed & states

        if len(covered) > len(states_covered):#有交集 len(covered)长度不为零！

            best_station = station
            states_covered = covered

            states_needed -= states_covered
            final_states.add(best_station)

print(final_states)
