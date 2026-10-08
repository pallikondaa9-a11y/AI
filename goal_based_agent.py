# Goal-Based Agent
# AI Practical: Simple Goal-Based Agent in a Toy Environment

class GoalBasedAgent:
    def __init__(self, start, goal):
        self.position = start
        self.goal = goal

    def act(self):
        if self.position < self.goal:
            print("Agent moves RIGHT")
            self.position += 1

        elif self.position > self.goal:
            print("Agent moves LEFT")
            self.position -= 1

        else:
            print("Agent has reached the GOAL!")


# Create the agent
agent = GoalBasedAgent(start=0, goal=5)

print("Starting Position:", agent.position)
print("Goal Position:", agent.goal)
print()

# Agent works until it reaches the goal
while agent.position != agent.goal:
    agent.act()
    print("Current Position:", agent.position)

print("\nTask completed successfully!")
