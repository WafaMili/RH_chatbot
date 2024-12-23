from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class CvHelper:
    """CvHelper crew"""


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def cv_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_matcher'],
            verbose=True
        )

    @agent
    def cv_improver(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_improver'],
            verbose=True

        )


    @task
    def cv_matcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['cv_matcher_task'],
        )

    @task
    def cv_improver_task(self) -> Task:
        return Task(
            config=self.tasks_config['cv_improver_task'],
            output_file='suggestions.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CvHelper crew"""
        return Crew(
            agents=self.agents,  # Agents créés par le décorateur @agent
            tasks=self.tasks,  # Tâches créées par le décorateur @task
            process=Process.sequential,  # Traitement séquentiel des tâches
            verbose=True
        )
