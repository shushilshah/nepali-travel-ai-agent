
import mlflow


from travel_agent.crew import TravelAgent
from datetime import datetime
import warnings
import sys
mlflow.crewai.autolog()

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("TravelAgent")
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    try:
        starting_place = input("Starting place: ")
        destination_place = input("Destination place: ")

        inputs = {
            'starting_place': starting_place,
            'destination_place': destination_place
        }

        TravelAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'starting_place': 'pokhara',
        'destination_place': 'kathmandu'
    }
    try:
        TravelAgent().crew().train(n_iterations=int(
            sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'starting_place': 'pokhara',
        'destination_place': 'kathmandu'
    }

    try:
        TravelAgent().crew().test(n_iterations=int(
            sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
