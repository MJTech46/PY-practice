import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} deleted")


def create_cyclic_reference():
    print("\nCreating cyclic references...")
    node1 = Node("Node 1")
    node2 = Node("Node 2")
    node1.ref = node2  # Node 1 references Node 2
    node2.ref = node1  # Node 2 references Node 1 (cycle)
    return node1, node2  # Return nodes to simulate external references


if __name__ == "__main__":
    print("Garbage Collection Example")

    # Part 1: Normal reference count-based garbage collection
    print("\n** Part 1: Reference Counting **")
    temp_node = Node("Temp Node")
    del temp_node  # Reference count drops to zero; memory is reclaimed

    # Part 2: Cyclic garbage collection
    print("\n** Part 2: Cyclic Garbage Collection **")
    node1, node2 = create_cyclic_reference()

    # Break the external references to trigger garbage collection
    print("Breaking external references...")
    del node1
    del node2

    print("\nTriggering garbage collection manually...")
    collected = gc.collect()  # Force garbage collection
    print(f"Garbage Collector: Collected {collected} unreachable objects.")

    # Display remaining garbage (if any)
    print("\nRemaining garbage objects:", gc.garbage)

    # Enable/disable garbage collection
    print("\nDisabling garbage collection...")
    gc.disable()
    print("Garbage collection disabled.")

    print("\nEnabling garbage collection...")
    gc.enable()
    print("Garbage collection enabled.")
