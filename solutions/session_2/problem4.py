# Parameter for the problems
n = 7  # Number of persons
k = 3  # Step to which people are eliminated

# List of persons. NOTE: We start from 1
persons = list(range(1, n + 1, 1))

# The 1st people eliminated is the k-th person.
# NOTE: k must be less than n, otherwise the
#       problem does not really make sense.
i = k

# Here I am using a flag. Otherwise you could
# put the condition directly into the while loop.
# In my opinion this makes the code more readable,
# but that is a matter of personal taste.
finished = False
while not finished:
    # NOTE: Since finished = False
    #       we now that we enter the loop
    # At each iteration we need to remove person "k + 1",
    # this is managed by the index i, in which persons are
    # popped from the list. Note that Python starts
    # counting from 0, so that i actually corresponds to the
    # person k + 1 (since i = k). In our case, k = 3,
    # so that when we pop the index 3, it is actually the
    # 4th element (0, 1, 2, _3_).
    eliminated_person = persons.pop(i)
    # Print who's eliminated (useful for debugging)
    print(f"Eliminated person {eliminated_person}")
    # Dirty trick to make a loop over the list
    i = (i + k) % len(persons)

    # Break the loop if we only have 1 person left.
    # you could actually put len(persons) == 1.
    # NOTE: you could also use the break command.
    if len(persons) <= 1:
        finished = True
# To finish, we print the selected person.
print(f"Selected person: {persons[0]}")
