import datetime
import time
from utility import any_common, TTS, text_edit, ofline_TTS
from command import node

global Three

Three = [
    node(["ahoj","nazdar", "cus", "te pic"],
     lambda inp: "nazdar",
     [
         node(["se mas", "ti je"],
          lambda inp: "mam se celkem fajn"
         )
     ]
    ),
    node(["se mas","ti je"],
     lambda inp: "na prd"
                
    ),
    node(["datum"],
     lambda inp: datetime.datetime.now().strftime("Dnes je %d %m %Y")
    ),
    node(["cas","hodin", "kolik je"],
     lambda inp: "právě je "+datetime.datetime.now().strftime("%H hodin a %M minut")
    ),
    node(["neopic"],
     lambda inp: inp,
     [
         node(["prosim"],
            lambda inp: "ok, sorry"
         )
     ]
    ),
    node(["s{3}"],
     lambda inp: "nope"
    ),
    node(["pomoc","co?"],
     lambda inp: "\n".join([str(tupl[0]) for tupl in Three])
    )
    ]