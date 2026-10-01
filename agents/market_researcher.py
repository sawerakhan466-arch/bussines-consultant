from crewai import Agent
from crew.llm import get_llm


def create_market_researcher():

    return Agent(

        role="Market Research Specialist",

        goal=(
            "Research and organize relevant market information "
            "for the proposed business, including target customers, "
            "competitors, trends, opportunities and threats."
        ),

        backstory=(
            "You are an experienced market research specialist. "
            "You identify customer needs, competitors and market "
            "opportunities. You distinguish facts from assumptions "
            "and never invent statistics."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False
    )
