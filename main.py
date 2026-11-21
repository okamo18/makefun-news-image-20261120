# main.py: copy the entry image to the output directory (stdlib only).
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
shutil.copyfile(os.path.join(here, "entry.png"),
                os.path.join(out, "entry.png"))
