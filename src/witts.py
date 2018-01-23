import dslink
import socket
import re

import dslink
import random

my_num = random.randint(0, 50)


class ExampleDSLink(dslink.DSLink):
    def start(self):
        print("Starting DSLink")

    def get_default_nodes(self, super_root):
        # Create MyNum Node
        # Name the node, specify the parent
        my_node = dslink.Node("MyNum", super_root)
        my_node.set_display_name("My Number")
        my_node.set_type("int")
        my_node.set_value(my_num)

        # Add my_node to the super root
        super_root.add_child(my_node)

        # Return the super root
        return super_root

    def start(self):
        # Kick off initial loop.
        self.call_later(1, self.update)

    def update(self):
        num = random.randint(0, 50)
        self.responder.get_super_root().get("/MyNum").set_value(num)

        # Call again 1 second later.
        self.call_later(1, self.update)

if __name__ == "__main__":
    ExampleDSLink(dslink.Configuration("example", responder=True))