"""One Line, Big Laugh — make.fun entry.

Entry text: 118 characters (limit 200).
"""

import os

ENTRY = 'My fitness tracker congratulated me for sleeping eight hours, then reminded me I burned fewer calories than the couch.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
