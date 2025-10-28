#!/usr/bin/env python3
# todo.py - very small CLI todo app

import json
import sys
from pathlib import Path

DATA = Path("todo.json")

def load():
    if not DATA.exists():
        return []
    return json.loads(DATA.read_text())

def save(items):
    DATA.write_text(json.dumps(items, ensure_ascii=False, indent=2))

def list_items(items):
    if not items:
        print("No todos.")
        return
    for i, it in enumerate(items, 1):
        status = "✓" if it.get("done") else " "
        print(f"{i}. [{status}] {it['task']}")

def add_item(items, task):
    items.append({"task": task, "done": False})
    save(items)
    print("Added.")

def done_item(items, index):
    try:
        items[index]["done"] = True
        save(items)
        print("Marked done.")
    except Exception:
        print("Invalid index.")

def remove_item(items, index):
    try:
        items.pop(index)
        save(items)
        print("Removed.")
    except Exception:
        print("Invalid index.")

def help_msg():
    print("""Usage:
          python todo.py list
          python todo.py add "task description"
          python todo.py done N
          python todo.py remove N
          python todo.py help""")
             

def main(argv):
    items = load()
    if len(argv) < 2:
        help_msg(); return
    cmd = argv[1]
    if cmd == "list":
        list_items(items)
    elif cmd == "add":
        if len(argv) < 3:
            print("Provide task text."); return
        add_item(items, " ".join(argv[2:]))
    elif cmd == "done":
        if len(argv) < 3:
            print("Provide index."); return
        done_item(items, int(argv[2]) - 1)
    elif cmd == "remove":
        if len(argv) < 3:
            print("Provide index."); return
        remove_item(items, int(argv[2]) - 1)
    else:
        help_msg()

if __name__ == "__main__":
    main(sys.argv)
