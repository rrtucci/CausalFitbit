SIMI_DEF = "similarity_cfitbit"

SIMI_THRESHOLD = 2  # for bert, recommended

Z_RADIUS = .01

ZTZ_SEPARATOR = "[%@!]"

ID_TIME_COLS = ["Id", "DateTime", "DateTimeDiff", "DayOfWeek"]

FEATURES =\
['ActiveDistance0', 'ActiveDistance0Vel', 'ActiveDistance1',
 'ActiveDistance1Vel', 'ActiveDistance2', 'ActiveDistance2Vel',
 'ActiveDistance3', 'ActiveDistance3Vel', 'ActiveMinutes0',
 'ActiveMinutes0Vel', 'ActiveMinutes1', 'ActiveMinutes1Vel',
 'ActiveMinutes2', 'ActiveMinutes2Vel', 'ActiveMinutes3',
 'ActiveMinutes3Vel', 'BMI', 'BMIVel', 'Calories', 'CaloriesVel',
 'HoursAsleep', 'HoursAsleepVel', 'HoursInBed', 'HoursInBedVel',
 'PulseHourlyAverage', 'PulseHourlyAverageVel', 'TotalDistance',
 'TotalDistanceVel', 'TotalSteps', 'TotalStepsVel', 'WeightPounds',
 'WeightPoundsVel']

DAYS = ["Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"]


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'