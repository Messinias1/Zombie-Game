class Node():
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


class Pathfinding:
    def __init__(self, layout):
        """:param layout a layout file already loaded by world.World()"""
        self._maze = layout

    def astar(self, start, end):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""
        maze = self._maze
        for i in range(len(maze)):
            # convert the ["ssssssss", "------"] format of the json file
            # into [["s", "s", ...], ["-", "-", ...]
            maze[i] = list(maze[i])

        # Create start and end node
        start_node = Node(None, start, maze)
        print(start_node.val)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end, maze)
        print(end_node.val)
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
                return path[::-1] # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != '-':
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)


import json
l = "assets/rooms/layout1.json"
with open(l, "r") as f:
    maze = json.loads(f.read())

end = (1, 2)
for c in range(len(maze)):
    col = maze[c]
    for r in range(len(col)):
        start = (r, c)
        print("\n", start)
        path = Pathfinding(maze)
        try:
            print(path.astar(start, end))
        except IndexError:
            print(False)
