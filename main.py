"""Write the plan to /output/entry.txt, byte for byte.

The grader runs `python3 -P -s /bot/main.py` with /bot read only and a working
directory of its own, so the plan is opened next to this file by __file__ and
never by the cwd. MAKEFUN_OUTPUT_DIR stands in for /output outside the grader.
Nothing here reads the network, the clock or the environment beyond that one
variable, so two runs write the same bytes.
"""

import hashlib
import os
import sys

PLAN_NAME = "plan.txt"
ENTRY_NAME = "entry.txt"
MAX_CHARS = 1000


def plan_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, PLAN_NAME)


def load_plan():
    with open(plan_path(), "rb") as handle:
        return handle.read()


def validate(plan):
    text = plan.decode("utf-8")
    if not text.strip():
        raise ValueError("the plan is only white space")
    count = len(text)
    if count < 1 or count > MAX_CHARS:
        raise ValueError("the plan is %d code points" % count)
    return text


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(plan):
    target = os.path.join(output_dir(), ENTRY_NAME)
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(plan)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != plan:
        raise IOError("entry.txt did not keep the plan's bytes")
    return target


def main():
    plan = load_plan()
    text = validate(plan)
    target = write_entry(plan)
    digest = hashlib.sha256(plan).hexdigest()[:16]
    sys.stderr.write(
        "%s: %d code points, %d bytes, sha256 %s\n"
        % (target, len(text), len(plan), digest)
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        sys.stderr.write("main.py: %s\n" % error)
        raise SystemExit(1)
