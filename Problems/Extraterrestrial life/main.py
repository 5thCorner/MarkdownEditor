# The parental gene sequences are stored here
one_ancestor = input()
other_ancestor = input()

# Calculate the identity of a new alien here
new_alien = int((id(other_ancestor) + id(one_ancestor)) // 2)
