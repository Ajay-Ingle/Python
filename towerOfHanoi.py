def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem.
    
    Parameters:
    n: int - Number of disks
    source: str - Name of the source rod
    target: str - Name of the target rod
    auxiliary: str - Name of the auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')
