from world import World


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, maze=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        try:
            self.val = maze[self.position[0]][self.position[1]]
        except:
            self.val = None

    def __eq__(self, other):
        return self.position == other.position


class PathfindingWorld(World):
    """This is a child of the World class
    when you want to create a world object that uses pathfinding
    you'll need to create it thru PathfindingWorld() instead of World()"""
    def __init__(self, layout):
        super().__init__(layout)

    def find_next_moves(self, start_x, start_y, end_x, end_y) -> [(int, int)]:
        """Finds the best path between two points that avoids all walls in the room
        :param start_x the x position to start at
        :param start_y the y position to start at
        :param end_x the desired x pos to end at
        :param end_y the y pos to end at
        :returns a list of tuple of pixels to move in (move_x, move_y)"""
        start_row, start_col = int(start_x // 32) + 1, int(start_y // 32)
        end_row, end_col = int(end_x // 32) + 1, int(end_y // 32)
        # all tiles have dimensions 32x32
        # so using integer division will convert (x, y) to (row, col)
        try:
            path = self.astar((start_row, start_col), (end_row, end_col))
        except IndexError:  # if the end or start tile is a wall
            path = [(start_row, start_col)]  # stay at the starting pos
        return path

    def find_next_move(self, start_x, start_y, end_x, end_y) -> (int, int):
        return self.find_next_moves(start_x, start_y, end_x, end_y)[0]

    def find_moves_towards(self, source: 'Character', target: 'Character') -> [(int, int)]:
        """Same as 'find_next_moves' but you can input two characters instead of x y positions
        :param source the character that will move
        :param target the character to move towards"""
        return self.find_next_moves(source.xpos, source.ypos, target.xpos, target.ypos)

    def astar(self, start, end):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""
        maze = self._layout_json
        for i in range(len(maze)):
            # convert the ["ssssssss", "------"] format of the json file
            # into [["s", "s", ...], ["-", "-", ...]
            maze[i] = list(maze[i])

        # Create start and end node
        start_node = Node(None, start, maze)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end, maze)
        if end_node.val != "-" or start_node.val != "-":
            raise IndexError  # the end or start node is a wall
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            #print(current_node.position)
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path

            # Generate children
            children = []
            cur_tile = self.find_tile_by_row_col(current_node.position[0], current_node.position[1])
            neighbors = cur_tile.get_neighbors()
            for cur_neigh in neighbors:  # Adjacent squares
                # Get node position
                node_position = (cur_neigh.row, cur_neigh.col)
                # Make sure within range
                new_node = Node(current_node, node_position)
                if cur_neigh.collideable:
                    # it's a wall
                    continue
                if Node(current_node, node_position) in closed_list:
                    continue
                # Append
                children.append(new_node)
            # Loop through children
            for child in children:
                # Child is on the closed list
                cont = False
                for closed_child in closed_list:
                    if child == closed_child:
                        cont = True
                        break
                        # we need to continue on the for loop at line 93, not the one at line 96
                if cont:
                    continue
                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g >= open_node.g:
                        cont = True
                        break
                        # we need to continue on the for loop at line 93, not the one at line 108
                if cont:
                    continue

                # Add the child to the open list
                open_list.append(child)


if __name__ == "__main__":
    finder = PathfindingWorld("assets/rooms/layout1.json").init_room()
    end = (1, 2)
    maze = finder._layout_json
    for c in range(len(maze)):
        col = maze[c]
        for r in range(len(col)):
            start = (r, c)
            print("\n", start)
            try:
                print(finder.astar(start, end))
            except IndexError:
                print(False)
