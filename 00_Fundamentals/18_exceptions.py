try:
    int("hello")
except ValueError as e:
    print("Exception!", e)

print("Done")