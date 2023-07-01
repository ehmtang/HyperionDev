swimming_time = float(input("Enter swimming time in minutes: "))
cycling_time = float(input("Enter cycling time in minutes: "))
running_time = float(input("Enter running time in minutes: "))

qualifying_time = 100

participant_time = swimming_time + cycling_time + running_time
print(participant_time)

if participant_time < qualifying_time:
    print("Provincial Colours")

elif (participant_time - qualifying_time) < 5:
    print("Provincial Half Colours")

elif (participant_time - qualifying_time) < 10:
    print("Provincial Scroll")

else:
    print("No award")
    