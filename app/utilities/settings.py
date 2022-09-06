import re
import sys

# Create a `the` variables
the={}

help="""[[
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = , ]]"""

def __init__(self):
  self.help = parseInput(self.help)
  
def parseInput(self, input):
  pattern = re.compile(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
  for k, x in re.findall(pattern, input):
    self.the[k] = self.coerce(x)
  return input

def coerce(s):
  """
  Parse `the` config settings from `help`.
  """
  if isinstance(s, int):
    return int(s)
  return False if re.match(s, "^\s*(.-)\s*$") is None else True

def cli(t):
  """
  Update settings from values on command-line flags. Booleans need no values
  (we just flip the defaults).
  """
  for slot, v in t.items():
    v = str(v)
    for n, x in enumerate(sys.argv): 
      if x == "-" + slot[0:1] or x == "--" + slot:
        if v == "false":
          v = "true"
        elif v == "true":
          v = "false"
        else:
          v = sys.argv[n + 1] 
    t[slot] = coerce(v)
  if t.help:
    print("\n", t.help, "\n")
    return
  return t