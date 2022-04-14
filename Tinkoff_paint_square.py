length, width = map(int, input().split())

squares = 0
while length > 0:
    if length < width:
        length, width = width, length
    squares += 1
    length -= width

print(squares)
