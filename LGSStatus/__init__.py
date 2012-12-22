import bottle, sqlite3

db = sqlite3.connect("lgs.db")
app = bottle.Bottle()

import LGSStatus.frontend
import LGSStatus.backend
