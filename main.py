import os

SCENE = "Dad tried to fix the wobbly chair before dinner and now it leans the other way, so Mom just slid the good plate over to his side and said, \"At least the chair finally agrees with you.\""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SCENE)

if __name__ == "__main__":
    main()
