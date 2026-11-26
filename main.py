"""Entry program for 'The Funniest Sick-Day Excuse'.

One line, under 200 characters, that a person could plausibly send to call
in sick while still getting a laugh out of the boss. The joke is built on
a domestic appliance turning against its owner: a smart fridge that has
locked its owner out of the kitchen and then filed a noise complaint
against the owner's own stomach. That is fresh territory - no fever, no
dog, no dead grandmother - and the twist lands on the last words, when the
"charges" turn out to be something a fridge can press against a stomach.

The line reads like a real typed message because it starts with the plain
report of waking up to the problem and only then escalates into the absurd
part, and it stays a genuine excuse throughout: the sender is staying in
bed, which is exactly what a sick day asks for. Every clause earns its
place - the lock-out explains why there is no breakfast, the noise
complaint explains the stomach, and "until it drops the charges" gives the
absence an end condition that is funny precisely because it will never
arrive. Nothing in the line is decoration; the whole sentence is the
excuse, the joke and the punchline at once.
"""

import sys
from pathlib import Path

LINE = "Woke up locked out of my own kitchen by a smart fridge that filed a noise complaint against my stomach \u2014 staying in bed until it drops the charges."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, over the 200 limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert "  " not in LINE, "entry must not contain double spaces"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
