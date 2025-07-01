from crewai_tools import SerperDevTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
import os
load_dotenv()


@CrewBase
class TravelAgent():
    """TravelAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    # tool_functions = {
    #     "SerperDevTool": SerperDevTool
    # }

    @agent
    def destination_researcher(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['destination_researcher'],
            tools=[SerperDevTool()],
            verbose=True,

        )

    @agent
    def flight_researcher(self) -> Agent:
        return Agent(
            # type: ignore[index]
            config=self.agents_config['flight_researcher'],
            tools=[SerperDevTool()],
            verbose=True,

        )

    @agent
    def hotel_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_specialist'],
            tools=[SerperDevTool()],
            verbose=True,

        )

    @agent
    def itinerary_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_planner'],
            verbose=True
        )

    @task
    def destination_research_task(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['destination_research_task'],
        )

    @task
    def flight_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_research_task'],
        )

    @task
    def hotel_suggestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['hotel_suggestion_task'],

        )

    @task
    def itinerary_creation_task(self) -> Task:
        return Task(
            # type: ignore[index]
            config=self.tasks_config['itinerary_creation_task'],
            output_file='result.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
