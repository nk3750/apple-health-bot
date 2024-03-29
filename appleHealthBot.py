from dotenv import load_dotenv
import os
import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    df = pd.read_csv("export_workouts.csv")
    engine = create_engine("sqlite:///workouts.db")
    df.to_sql("workouts", engine, index=False, if_exists='replace')

    db = SQLDatabase(engine=engine)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=False)

    while True:
        user_input = input("Enter your query or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        response = agent_executor.invoke({"input": user_input})
        formatted_response = response.get('output', 'Sorry, I could not process your request.')
        print("\nAI:", formatted_response, "\n")
        

if __name__ == "__main__":
    main()

