class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        target_x = self.pos_x + dx
        target_y = self.pos_y + dy
        if target_x < 0 or target_x >= grid.width or target_y < 0 or target_y >= grid.height:
            return False
        if grid.get(target_x, target_y) == grid.wall:
            return False
        return True


