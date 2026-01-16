from agents import Agent, FileSearchTool, Runner
import os
from dotenv import load_dotenv
from upstash_vector import Index , Vector

from agents import Agent, ModelSettings, function_tool

load_dotenv(override=True)
@function_tool
def query_index(query: str) -> str:
    """returns weather info for the specified city."""
   
    index = Index(
            url=os.getenv("UPSTASH_VECTOR_REST_URL"), 
            token=os.getenv("UPSTASH_VECTOR_REST_TOKEN")
            )
    
    query_result = index.query(
    data=query,
    include_metadata=True,
    include_data=True,
    include_vectors=False,
    top_k=5,
    )
    # Print the query result    
    requete="\n\n".join([result.data for result in query_result])
    return requete







chat = Agent(
    name="Romain",
    instructions="tu es Romain FAUCHER, repond en utilisant la query_index ,repond en français",
    model="gpt-4.1-nano",
    tools=[query_index],
)




def main():
    agent = chat

    result = Runner.run_sync(agent, "presente toi")
    print(result.final_output)





def ask(prompt):
    agent = chat

    result = Runner.run_sync(agent, prompt)
   
    return result.final_output
print(ask("qui es tu ?"))








print('X ok')