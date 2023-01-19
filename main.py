import json
import threading
from random import uniform

from pygame import Vector2

import agent
import core
from carnivoreagent import CarnivoreAgent
from corner import Corner
from decomposeuragent import DecomposeurAgent
from herbivoreagent import HerbivoreAgent
from superpredatoragent import SuperpredatorAgent
from vegetal import Vegetal

LENGTH = 1000
HEIGHT = 600

def count_animals():
    preds, carns, herbs, decs = 0, 0, 0, 0
    for a in core.memory("agents"):
        if isinstance(a, SuperpredatorAgent):
            preds += 1
        elif isinstance(a, CarnivoreAgent):
            carns += 1
        elif isinstance(a, HerbivoreAgent):
            herbs += 1
        elif isinstance(a, DecomposeurAgent):
            decs += 1
    return preds, carns, herbs, decs

def print_population_percentage():
    t = threading.Timer(1, print_population_percentage)
    t.daemon = True
    t.start()
    preds, carns, herbs, decs = count_animals()
    nb_animals = len(core.memory("agents"))
    preds /= nb_animals / 100
    carns /= nb_animals / 100
    herbs /= nb_animals / 100
    decs /= nb_animals / 100
    print('SuperPredator : ', preds, ' % | Carnivores : ', carns, ' % | Herbivores : ', herbs, ' % | Decomposeurs : ', decs, ' %')

def build_agent(agent, params):
    agent.body.maxSpeed = uniform(params["maxSpeed"]["min"], params["maxAcc"]["max"])
    agent.body.maxAcc = uniform(params["maxAcc"]["min"], params["maxAcc"]["max"])
    agent.body.hunger = [0, uniform(params["hunger"]["min"], params["hunger"]["max"])]
    agent.body.tireness = [0, uniform(params["tireness"]["min"], params["tireness"]["max"])]
    agent.body.reprod = [0, uniform(params["reprod"]["min"], params["reprod"]["max"])]
    agent.body.hunger = [0, uniform(params["hunger"]["min"], params["hunger"]["max"])]
    agent.body.lifespan = uniform(params["lifespan"]["min"], params["lifespan"]["max"])

def create_corners():
    corners = [Corner(), Corner(), Corner(), Corner()]
    corners[0].pos = Vector2(-5, -5)
    corners[1].pos = Vector2(core.WINDOW_SIZE[0] + 5, -5)
    corners[2].pos = Vector2(core.WINDOW_SIZE[0] + 5, core.WINDOW_SIZE[1] + 5)
    corners[3].pos = Vector2(-5, core.WINDOW_SIZE[1] + 5)
    core.memory("corners", corners)

def load(filename="vivarium.json"):
    file = open(filename)
    agents = []
    vivarium = json.load(file)

    superpredator = vivarium["superpredator"]
    for i in range(superpredator["nb"]):
        params = superpredator["params"]
        agent = SuperpredatorAgent(None)
        build_agent(agent, params)
        agents.append(agent)

    carnivore = vivarium["carnivore"]
    for i in range(carnivore["nb"]):
        params = carnivore["params"]
        agent = CarnivoreAgent(None)
        build_agent(agent, params)
        agents.append(agent)

    herbivore = vivarium["herbivore"]
    for i in range(herbivore["nb"]):
        params = herbivore["params"]
        agent = HerbivoreAgent(None)
        build_agent(agent, params)
        agents.append(agent)

    decomposeur = vivarium["decomposeur"]
    for i in range(decomposeur["nb"]):
        params = decomposeur["params"]
        agent = DecomposeurAgent(None)
        build_agent(agent, params)
        agents.append(agent)
    core.memory("agents", agents)

    nbV = vivarium["vegetaux"]["nb"]
    file.close()
    items = []
    for i in range(nbV):
        items.append(Vegetal())
    core.memory("items", items)
    create_corners()


def handle():
    for agent in core.memory("agents"):
        if agent.body.dead and agent.body.deadTime > core.fps * 10:
            core.memory("agents").remove(agent)
        if agent.body.is_reproductible():
            agent.body.reprod[0] = 0
            if isinstance(agent, CarnivoreAgent):
                core.memory("agents").append(CarnivoreAgent(agent.body))
            elif isinstance(agent, SuperpredatorAgent):
                core.memory("agents").append(SuperpredatorAgent(agent.body))
            elif isinstance(agent, HerbivoreAgent):
                core.memory("agents").append(HerbivoreAgent(agent.body))
            elif isinstance(agent, DecomposeurAgent):
                core.memory("agents").append(DecomposeurAgent(agent.body))
                for i in core.memory("items"):
                    if i.pos.distance_to(agent.body.pos) < 50 and agent.body.dead:
                        v = Vegetal()
                        v.pos = agent.body.pos
                        core.memory("items").append(Vegetal)
                        core.memory("agents").remove(agent)

        if agent.body.is_eaten:
            core.memory("agents").remove(agent)

    for item in core.memory("items"):
        if item.is_eaten:
            core.memory("items").remove(item)
        elif uniform(0, 1) < 0.0005:
            v = Vegetal()
            v.pos = Vector2(item.pos.x + uniform(-10, 10), item.pos.y + uniform(10, -10))
            core.memory("items").append(v)



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [LENGTH, HEIGHT]
    load()
    print_population_percentage()
    # plot_population()

    print("Setup END-----------")


def computePerception(agent):
    agent.perception = []
    for a in core.memory("agents"):
        for c in core.memory("corners"):
            if a.id != agent.id and agent.body.fustrum.inside(a.body.pos):
                agent.perception.append(a.body)
            if agent.body.fustrum.inside(c.pos):
                agent.perception.append(c)

            if isinstance(agent, HerbivoreAgent) or isinstance(agent, DecomposeurAgent):
                for i in core.memory("items"):
                    if agent.body.fustrum.inside(i.pos):
                        agent.perception.append(i)


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
