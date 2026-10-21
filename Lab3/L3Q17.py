def can_jump(speed, power, name, injured):
    distance = speed * power
    if injured:
        distance = distance * 0.8
    if distance >= 1:
        return f"{name} can jump {distance:.2f} m!"
    else:
        return name + ' made a false attempt!'

print(can_jump(9.0, 0.6, "Morrison", True))