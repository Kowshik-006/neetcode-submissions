class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # Sort in descending order based on the position
        cars.sort(reverse = True)

        for position, speed in cars:
            # the time taken to reach the target
            stack.append((target-position)/speed)
            # two cars in the stack and the one behind reaches the target earlier
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                # the car behind forms a fleet with the one ahead
            
            # if a fleet can be formed the new element is popped 
            # the car at the foremost of the fleet is kept
            # the number of elements remaining at the end denotes the number of fleets possible

        return len(stack)
        
