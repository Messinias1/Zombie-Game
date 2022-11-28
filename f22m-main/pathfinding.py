from world import World
from tile import Tile


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


class PathfindingWorld(World):
    """This is a child of the World class
    when you want to create a world object that uses pathfinding
    you'll need to create it thru PathfindingWorld() instead of World()"""
    def __init__(self, layout):
        super().__init__(layout)

    def rowcol_to_mazeval(self, rowcol: (int, int)) -> str:
        """:param rowcol the requested (row, column)
        :return the string value stored in the layout file at rowcol"""
        return self.maze[rowcol[1]][rowcol[0]]

    def get_node_val(self, node: Node) -> str:
        return self.rowcol_to_mazeval(node.position)

    def find_next_moves(self, start_xy, end_xy) -> [(int, int)]:
        """Finds the best path between two points that avoids all walls in the room
        :param start_xy the (x, y) to start at
        :param end_xy the (x, y) to end at
        :returns a list of tuple of pixels to move in (move_x, move_y)"""
        start_pos = Tile.xy_to_rowcol(start_xy)
        end_pos = Tile.xy_to_rowcol(end_xy)
        try:
            path = self.astar(start_pos, end_pos)
            path.pop(0)
        except IndexError:  # if the end or start tile is a wall
            path = [start_pos]  # stay at the starting pos
        return path

    def find_next_move(self, start_xy: (int, int), end_xy: (int, int)) -> (int, int):
        return self.find_next_moves((start_xy[0], start_xy[1]), (end_xy[0], end_xy[1]))[0]

    def find_next_move_towards(self, source: 'Character', target: 'Character') -> (int, int):
        """Same as 'find_next_moves' but you can input two characters instead of x y positions
        :param source the character that will move
        :param target the character to move towards"""
        return self.find_next_move((source.xpos, source.ypos), (target.xpos, target.ypos))

    def astar(self, start, end):
        """Returns a list of tuples as a path from the given start to the given end in the given self.maze"""
        for i in range(len(self.maze)):
            # convert the ["ssssssss", "------"] format of the json file
            # into [["s", "s", ...], ["-", "-", ...]
            self.maze[i] = list(self.maze[i])

        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        if self.get_node_val(end_node) != "-" or self.get_node_val(start_node) != "-":
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
            cur_tile = self.find_tile_by_row_col(current_node.position)
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


