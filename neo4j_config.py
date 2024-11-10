# neo4j_config.py
from neo4j import GraphDatabase

def get_neo4j_driver():
    return GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
