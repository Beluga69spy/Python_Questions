# Merge two tuples and remove duplicates.
def tup(tuple1, tuple2):

  combined = set(tuple1) | set(tuple2)
  return tuple(combined)
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

merged = tup(tuple1, tuple2)

print(f"Merged tuple without duplicates: {merged}")
