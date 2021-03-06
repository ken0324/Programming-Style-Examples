# Print out all the state names from the csv
# Showing an "event-driven" style
from electiondata import ElectionResults
import sys

filename = '2012_US_election_state.csv'
results = ElectionResults(filename)

while True:
    command = raw_input('Enter your input (1 to load, 2 to print result, 3 to quit):')

    if command=="1":
        results.load();
        print "Loaded ("+str(results.state_count())+" lines)"
    elif command=="2":
        val = 0
        state_names = results.states()
        for state in state_names:
            val = val + int(state)
        print val
    elif command=="3":
        print "bye!"
        sys.exit()
    else:
        print "Uknown command :-("
