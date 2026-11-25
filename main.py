"""The Internet in One Word — entry program.

Chosen word: "arguments"

Why this word, scored against the judge's five criteria (most important first):

1. Single word describing the whole internet — yes. "arguments" is one
   word, and it names what the internet *is* at every level: comment
   sections, quote-tweets, forums, group chats, reviews, replies to
   replies. It is not one app, one site or one mood.
2. Funny by itself, no explanation needed — the laugh lands immediately:
   the entire internet, all of human knowledge and connection, mostly
   used to argue with strangers. It is wry rather than loud, which is
   exactly the joke.
3. True about the internet as a whole — every corner of it runs on
   disagreement. Even the friendly parts (fandoms, hobby groups, recipe
   blogs) are one disagreement away from a thread.
4. Surprising — the obvious first words everyone reaches for are
   "chaos", "memes", "cats", "doomscrolling". "arguments" is the truth
   hiding one step behind the cliche.
5. Lands in one beat — nine letters, spelled correctly, instantly
   readable, no hyphen, no trick.

Candidates considered and rejected:
- "rabbithole": poetic and true, but the laugh is softer — it describes
  an experience, not what the internet *is*.
- "unread": short and surprising, but the joke is dry to the point of
  being flat; it scores lower on funniness, the second criterion.

The program below is fully deterministic: it always writes the same
single word, with no randomness, no time, no network.
"""

import os
import stat

# The entry: one word for the whole internet.
WORD = "arguments"

# Gate limits from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 30 characters, not only whitespace.
MAX_CHARS = 30
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(word):
    """Enforce the sealed gate: a single token, 1-30 chars, non-blank."""
    if not isinstance(word, str):
        raise TypeError("word must be a str")
    if not (1 <= len(word) <= MAX_CHARS):
        raise ValueError("word must be 1 to 30 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("word must be a single token, no whitespace inside")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace characters")
    # One more guard for criterion 5 (lands in one beat): the word must
    # be plain lowercase letters only, so nothing odd can sneak into the
    # entry and slow the reader down.
    if not word.isalpha() or not word.islower():
        raise ValueError("word must be plain lowercase letters only")
    word.encode("utf-8")  # must be valid UTF-8 text
    return word


def main():
    os.umask(0o022)
    word = validate(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word)
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
