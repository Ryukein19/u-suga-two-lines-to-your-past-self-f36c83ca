import os
# Two-line entry (240 chars): the lines below are the whole submission.
# Writes to /output/entry.txt.
LINE = "Do not deploy on Friday at 4:58 p.m., no matter how small the change looks — the rollback will eat your whole weekend.\nThat one deploy taught me that 'quick fix' is just a slow disaster wearing a friendly name, and I never trusted it again."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
