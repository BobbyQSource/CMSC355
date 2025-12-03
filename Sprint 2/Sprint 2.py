# Workout Logger
# Logging workout information for TC01–TC04

class WorkoutLogger:
    def __init__(self):
        self.history = []  # stores logged workouts

    def save_workout(self, exercise, weight, reps, sets):
        # TC02: Missing required field
        if exercise == "" or weight == "" or reps == "" or sets == "":
            return "Error: All fields must be filled!"

        # Convert numeric values
        try:
            weight = int(weight)
            reps = int(reps)
            sets = int(sets)
        except ValueError:
            return "Error: Weight, reps, and sets must be numbers!"

        # TC03: Invalid weight
        if weight <= 0:
            return "Invalid weight."

        # TC04: Invalid reps
        if reps <= 0:
            return "Invalid number of reps."

        # Optional improvement: Validate sets
        if sets <= 0:
            return "Invalid number of sets."

        # TC01: Valid entry
        entry = {
            "Exercise": exercise,
            "Weight": weight,
            "Reps": reps,
            "Sets": sets
        }

        self.history.append(entry)
        return "Workout saved."

    def view_history(self):
        return self.history


# --------------------------
# Test Cases (TC01–TC04)
# --------------------------
if __name__ == "__main__":
    logger = WorkoutLogger()

    # TC01 – Valid input
    print("TC01:", logger.save_workout("Bench Press", "135", "10", "3")) 

    # TC02 – Missing sets field
    print("TC02:", logger.save_workout("Deadlift", "135", "10", ""))

    # TC03 – Invalid weight (0)
    print("TC03:", logger.save_workout("Squat", "0", "10", "3"))

    # TC04 – Invalid reps (0)
    print("TC04:", logger.save_workout("Overhead Press", "135", "0", "3"))

    # Show saved history
    print("\nWorkout History:", logger.view_history())