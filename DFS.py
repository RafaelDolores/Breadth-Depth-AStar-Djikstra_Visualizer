from configurations import *

class DepthFirst():
    def __init__(self, app, start_node_x, start_node_y, end_node_x, end_node_y, wall_pos):
        self.app = app
        self.start_node_x = start_node_x
        self.start_node_y = start_node_y
        self.end_node_x = end_node_x
        self.end_node_y = end_node_y
        self.wall_pos = wall_pos
        self.visited = [(self.start_node_x, self.start_node_y)]
        self.route = None #String containing each direction
        self.route_found = False

    def draw_path(self, i, j):
        ##### Draw each node the computer is visiting as it is searching SIMULTNEOUSLY
        pygame.draw.rect(self.app.DISP, TAN, (i * 24 + 240, j * 24, 24, 24), 0)

        ##### Redraw start/end nodes on top of all routes
        pygame.draw.rect(self.app.DISP, YELLOW,
                         (240 + self.start_node_x * 24, self.start_node_y * 24, 24, 24), 0)
        pygame.draw.rect(self.app.DISP, ROYALBLUE,
                         (240 + self.end_node_x * 24, self.end_node_y * 24, 24, 24), 0)

        # Redraw grid (for aesthetic purposes lol)
        for x in range(52):
            pygame.draw.line(self.app.DISP, ALICE, (GStart_x + x * 24, GStart_y),
                             (GStart_x + x * 24, GEND_y))
        for y in range(30):
            pygame.draw.line(self.app.DISP, ALICE, (GStart_x, GStart_y + y * 24),
                             (GEnd_x, GStart_y + y * 24))

        pygame.display.update()

    def is_valid_step(self, move):
        if move not in self.wall_pos and move not in self.visited:
            self.visited.append(move)
            return True
        return False

    def reached_dest(self, first_in):
        if first_in == (self.end_node_x, self.end_node_y):
            return True
        return False

    def DepthFirst_Search(self):
        stack = []
        first_in = (self.start_node_x, self.start_node_y)
        stack.append(first_in)

        moves_stack = []
        moves_first_in = ''
        moves_stack.append(moves_first_in)

        while len(stack) > 0:
            last_out = stack.pop()
            moves_last_out = moves_stack.pop()

            for m in ['L', 'R', 'U', 'D']:
                i, j = last_out
                if m == 'L':
                    i -= 1
                elif m == 'R':
                    i += 1
                elif m == 'U':
                    j -= 1
                elif m == 'D':
                    j += 1

                move_update = moves_last_out + m

                if self.reached_dest((i, j)):
                    self.route = move_update
                    self.route_found = True
                    break

                if self.is_valid_step((i, j)):
                    stack.append((i, j))
                    moves_stack.append(move_update)
                    self.draw_path(i, j)

            if self.route_found:
                break






