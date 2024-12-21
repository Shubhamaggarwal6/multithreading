import tkinter as tk
import threading
import time
import random

data = [
    {'range': (10, 20), 'color': 'peachpuff', 'refresh_time': 10},
    {'range': (-10, 10), 'color': 'lightblue', 'refresh_time': 20},
    {'range': (-100, 0), 'color': 'lightgreen', 'refresh_time': 8},
    {'range': (0, 20), 'color': 'khaki', 'refresh_time': 12},
    {'range': (-40, 40), 'color': 'lightsteelblue', 'refresh_time': 16},
    {'range': (100, 200), 'color': 'lightgray', 'refresh_time': 14}
]

stop_flag = threading.Event()


def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1,
              x2, y1, x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius,
              x2, y2, x2 - radius, y2, x2 - radius, y2, x1 + radius, y2, x1 + radius, y2,
              x1, y2, x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)


def task(label, canvas, rect_id, lb, ub, refresh_time, base_color):
    while not stop_flag.is_set():
        new_value = random.randint(lb, ub)

        try:
            label.config(text=str(new_value))
            # Flash color
            canvas.itemconfig(rect_id, fill="yellow")
            time.sleep(0.2)
            canvas.itemconfig(rect_id, fill=base_color)
        except tk.TclError:
            break

        time.sleep(refresh_time - 0.2)


def stop_app(root):
    stop_flag.set()
    root.quit()
    root.destroy()


def create_window():
    root = tk.Tk()
    root.title("Multithreading Label Refresh")

    for i, item in enumerate(data):
        frame = tk.Frame(root)
        frame.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        canvas = tk.Canvas(frame, width=200, height=100, highlightthickness=0)
        canvas.pack()

        rect_id = create_rounded_rect(canvas, 10, 10, 190, 90, radius=25, fill=item['color'], outline='black', width=2)

        label = tk.Label(canvas, text='-', font=('Arial', 20), bg=item['color'])
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        info_label = tk.Label(frame, text=f"{item['range']} refresh time = {item['refresh_time']}", font=('Arial', 12))
        info_label.pack(pady=5)

        threading.Thread(target=task,
                         args=(label, canvas, rect_id, item['range'][0], item['range'][1], item['refresh_time'],
                               item['color'])).start()

    exit_button = tk.Button(root, text="Exit", command=lambda: stop_app(root), font=('Arial', 12), bg='red', fg='white')
    exit_button.grid(row=(len(data) // 2) + 1, column=0, columnspan=2, pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_window()
