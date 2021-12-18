#!/usr/bin/env python
from adventinput import get_data

def simulate_fish_naive(ages, days):
    for _ in range(days):
        spawn_count = ages.count(0)
        ages = list(map(lambda x: x - 1 if x > 0 else 6, ages))
        ages.extend([8] * spawn_count)
    return ages

def simulate_fish(ages, days):
    # Simulate all the cycles when spawning will be guaranteed to occur
    base_spawning_cycles = days // 7
    # When a lanternfish is born, it has a timer of 8 (9 days).
    # That is (almost) equivalent to saying the child's timer = (parents' spawning timer + 2) mod 7
    # Parent Child
    # 5      -
    # 4      -
    # 3      -
    # 2      -
    # 1      -
    # 0      -
    # 6      8
    # 5      7
    # 4      6 --> At this point this will be the relationship

    # So if the base_spawning_cycles is 10, all the initial lanternfish with a timer of 0 will
    # produce 10 children with a timer 2 greater than it, etc

    # Now onto figuring out the children of the children. But first, working through an example:

    # If days = 14, days % 7 == 0. All initial fish spawn twice.
    # However, initial fish with timers 6 and 5 will have 1st generation children that don't spawn
    # once, but all the others (timer < 5) will have 1st gen children that spawn once.
    # This is because 7 + 9 = 16, and 6 + 9 = 15, both of which are greater than 14 days.
    # Another way to think about it is that we're essentially breaking up time into 7 day cycles,
    # irrespective of the timers of the fish.
    # The 1st gen fish that spawn with 6/5 parents come in to the next cycle with a timer at 8 or 7,
    # which precludes them from spawning at all during that cycle, for obvious reasons.

    # So from what I can tell, what we want to do is:
    # For initial fish timer < 5: (base_spawning_cycles - 1) + (base_spawning_cycles - 2) + ...
    # For initial fish timer in [5,6]: (base_spawning_cycles - 2) + (base_spawning_cycles - 3) + ...
    # Use the triangular sum formula for this: n(n+1)/2 etc

    # I guess each time we do this we get a crop of children with timers + 2 mod 7, so we repeat the
    # above process until we can't get any more? Something like that probably
    timers = [
              ages.count(0),
              ages.count(1),
              ages.count(2),
              ages.count(3),
              ages.count(4),
              ages.count(5),
              ages.count(6),
              0,
              0
             ]
    initial_kids = [0, 0, 
                    timers[0] * base_spawning_cycles,
                    timers[1] * base_spawning_cycles,
                    timers[2] * base_spawning_cycles,
                    timers[3] * base_spawning_cycles,
                    timers[4] * base_spawning_cycles,
                    timers[5] * base_spawning_cycles,
                    timers[6] * base_spawning_cycles,
                   ]
    for d in range(days, 0, -1):
        # brain has stopped working at this point
    

    # We haven't dealt with the remainder of days
    left_over = days % 7
    additonal_fish = sum([x < left_over for x in ages]) # This should be the final list of all the
                                                        # fish. 

if __name__ == "__main__":
    ages = [int(s) for s in get_data(6)[0].split(",")]

    # Part 1
    fish_after_80_days = simulate_fish_naive(ages, 80)
    print(f"The number of fish after 80 days is {len(fish_after_80_days)}")

    # Part 2
    # Yeah, this doesn't work with the naive implementation. On my as of writing 9 year old Samsung
    # NP355 I got nowhere after several minutes and Python's memory usage creeping over 2 GB out of
    # the 8 I had.
    # fish_after_256_days = simulate_fish_naive(fish_after_80_days, 256-80)
    # print(f"The number of fish after 256 days is {len(fish_after_256_days)}")
