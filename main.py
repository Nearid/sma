import core

from carnivoreagent import CarnivoreAgent
from decomposeuragent import DecomposeurAgent
from herbivoreagent import HerbivoreAgent
from superpredatoragent import SuperpredatorAgent

LENGTH = 500
HEIGHT = 500

def handle():
    for agent in core.memory("agents"):
        if agent.body.is_reproductible():
            agent.body.reprod[0] = 0
            if isinstance(agent, CarnivoreAgent):
                core.memory("agents").append(CarnivoreAgent())
            elif isinstance(agent, SuperpredatorAgent):
                core.memory("agents").append(SuperpredatorAgent())
            elif isinstance(agent, HerbivoreAgent):
                core.memory("agents").append(HerbivoreAgent())
            elif isinstance(agent, DecomposeurAgent):
                core.memory("agents").append(DecomposeurAgent())


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [LENGTH, HEIGHT]
    agents = []
    agents.append(SuperpredatorAgent())
    agents.append(CarnivoreAgent())
    agents.append(HerbivoreAgent())
    agents.append(DecomposeurAgent())
    core.memory("agents", agents)
    core.memory("items", [])

    print("Setup END-----------")

def computePerception(agent):
    agent.perception = []
    for a in core.memory("agents"):
        if a.id != agent.id and agent.body.fustrum.inside(a.body.pos):
            agent.perception.append(a)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.move()
    agent.body.update()


def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("items"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    handle()

core.main(setup, run)


