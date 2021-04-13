AGES = { "kid": (0, 15), "young": (15, 60), "adult": (60, 125) }

DATA_COLLECTORS = ["DataCollectorCsv", "DataCollectorAPI"]
# DATA_COLLECTORS = []

POSIBLE_VALUES_SICK = {"positive": True, "negative": False, "yes": True, " no": False, "+": True, "-": False, "wee": True}

LOG_FILE = "logs/pandemic.log"
LOG_FORMATTER = "%(levelname)s:%(name)s:%(message)s"

# range(0, 10) => [0, 1, 2,3, ..., 10]