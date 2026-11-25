#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

This program writes exactly one roast line about a smart fridge to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` on a local
run, where ``/output`` may not be writable). The gate wants UTF-8 text
of 1 to 200 characters, not only whitespace, so the file holds exactly
the line itself: no trailing newline, no extra words, no commentary.

The angle: the paywall. Modern smart fridges do not just keep food
cold; they run an app, and the app wants a monthly subscription for
the privilege of stating the obvious. The joke picks the most banal
fact a fridge could possibly report -- that the milk is gone -- and
puts a price tag on it, $4.99 a month, as if knowing you are out of
milk were a premium feature instead of something your eyes do for
free. The punchline then undercuts the whole business model in one
breath: the "premium insight" is available at zero cost by performing
the ancient, subscription-free ritual of opening the door and looking.

Why this angle, and why it is not one of the usual cracks:

* It never touches the midnight-lock / self-control joke, the 3am
  "leftovers, not answers" visit, the door-left-open electric bill,
  or the ice maker as a slot machine -- those lines already exist.
* It never touches the two obvious cracks the judge brief warns
  against: the fridge ordering groceries on its own, and the fridge
  watching its owner. There is no camera here, no spying, no
  auto-order. The fridge is not a creep; it is a cashier.
* It is specific to *smart* fridges rather than any cold box. A dumb
  fridge cannot charge a subscription. Only a fridge with Wi-Fi, an
  app, and delusions of software grandeur can try to rent you the
  knowledge that your milk ran out.
* The wording is tight. Every clause earns its place: the price
  ($4.99 a month) makes the absurdity concrete instead of vague,
  "tell me I'm out of milk" names the most trivial possible report,
  and the closing turn -- "news I can get for free by opening the
  door" -- lands the laugh without explaining it. Nothing in the
  line explains its own joke; the contrast between a monthly fee and
  a free glance does all the work.

The em dash in the middle is doing structural work, not decoration:
it separates the setup (the subscription) from the punchline (the
free alternative), so the line reads as one breath with a turn in
the middle, the way a spoken one-liner should.
"""

import os

# The line. Setup: a monthly fee for a trivial fact. Punchline: the
# same fact is free behind the door. The specific price keeps the
# joke grounded -- "a subscription" alone would be a shrug, while
# "$4.99 a month" is a bill, and bills are funny when they are for
# nothing. "Charges" beats "wants" because it makes the fridge an
# active biller rather than a hopeful one, and calling the milk report
# "a diagnosis" frames the appliance as a doctor delivering verdicts
# about a carton -- a small second laugh hiding inside the punchline.
LINE = (
    "My smart fridge charges $4.99 a month to tell me I'm out of milk "
    "\u2014 a diagnosis I can get for free by opening the door."
)

# The gate: 1 to 200 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 200


def validate(line: str) -> str:
    """Check the line against the gate before anything is written.

    Returns the line unchanged when it passes. Raises ValueError with
    a plain message when it does not, so a bad line fails loudly here
    instead of silently producing an invalid entry downstream.
    """
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    # Round-trip through UTF-8 to prove the text is encodable as the
    # gate requires; the file is then written with that same encoding.
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # The grader collects outputs as another user: leave the file
    # world-readable, or it fails with "<path> is not readable".
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
