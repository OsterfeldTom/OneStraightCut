import tkinter as tk
from app import StraightSkeletonApp


SOFTWARE_NAME: str = "Straight-Skeleton Tool"
SOFTWARE_VERSION: str = "0.2.5"
MAX_POLYGONS: int = 2


def main():
    root = tk.Tk()
    root.title(f"{SOFTWARE_NAME} v{SOFTWARE_VERSION}")
    root.minsize(800, 800)
    app = StraightSkeletonApp(root, MAX_POLYGONS)
    root.mainloop()


if __name__ == "__main__":
    main()