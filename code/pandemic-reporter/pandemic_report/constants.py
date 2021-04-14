AGES = { "kid": (0, 15), "young": (15, 60), "adult": (60, 125) }

DATA_COLLECTORS = ["DataCollectorCsv", "DataCollectorAPI"]
# DATA_COLLECTORS = []

POSIBLE_VALUES_SICK = {"positive": True, "negative": False, "yes": True, " no": False, "+": True, "-": False, "wee": True}

LOG_FILE = "logs/pandemic.log"
LOG_FORMATTER = "%(levelname)s:%(name)s:%(message)s"

POSIBLE_STATUS_CODES = {200: {"message": "OK", "is_good": True}, 404: {"message": "Not Found", "is_good": False}, 408: {"message": "Request timeout", "is_good": False}}

# range(0, 10) => [0, 1, 2,3, ..., 10]