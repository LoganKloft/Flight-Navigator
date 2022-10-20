from neo4j import GraphDatabase

import os
from dotenv import load_dotenv

def init():
    load_dotenv()
    
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    driver = init_driver(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

    return driver

def init_driver(uri, username, password):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    driver.verify_connectivity()

    return driver