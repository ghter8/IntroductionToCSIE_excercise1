tasks = []

def add_task(name):
    if name in tasks:
        print(f"'{name}' already exitsts, skipping.")
        return
    tasks.append(name)

def show_tasks():
    print(f"=== Todo List ({len(tasks)} to do) ===")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def main():
    add_task("Learn Git")
    add_task("Learn Git")
    show_tasks()

if __name__ == "__main__":
    main()
