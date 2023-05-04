class AnalogClock:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours % 12  # converts 24-hour to 12-hour format
        self.minutes = minutes

    def calculateLesserAngle(self) -> float:
        hoursAngle = (self.hours + self.minutes / 60) * 30  # each hour is 30 degrees
        minutesAngle = self.minutes * 6  # each minute is 6 degrees
        differenceAngle = abs(hoursAngle - minutesAngle)
        lesserAngle = min(differenceAngle, 360 - differenceAngle)
        return lesserAngle


def promptUserInput() -> tuple:
    hours = int(input("Enter hours (0-23): "))
    minutes = int(input("Enter minutes (0-59): "))
    return (hours, minutes)


def outputResult(angle: float):
    print(f"Lesser angle between hour and minute hand: {round(angle, 3)} degrees")


def main():
    hours, minutes = promptUserInput()
    clock = AnalogClock(hours, minutes)
    angle = clock.calculateLesserAngle()
    outputResult(angle)


if __name__ == "__main__":
    main()
