from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
import openai

def classify_query(query, openai_api_key):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="text-davinci-003",  # Or whichever model you're using
        messages=[{"role": "system", "content": "Classify the following query into categories 'workouts', 'sleep', or 'other'."},
                  {"role": "user", "content": query}],
    )
    classification = response.choices[0].message['content'].strip().lower()
    return classification

def load_data_into_db(csv_path, db_path, table_name):
    engine = create_engine(db_path)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, index=False, if_exists='replace')
    return engine

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=openai_api_key)

    # Paths to CSV files and corresponding SQLite databases
    data_paths = {
        "workouts": ("export_workouts.csv", "sqlite:///workouts.db", "workouts"),
        "sleep": ("export_sleep.csv", "sqlite:///sleep.db", "sleep"),  # Placeholder for sleep data
    }

    while True:
        user_input = input("Enter your query or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break

        # Classify the user's query
        category = classify_query(user_input, openai_api_key)

        if category in data_paths:
            csv_path, db_path, table_name = data_paths[category]
            engine = load_data_into_db(csv_path, db_path, table_name)
        else:
            print("\nAI: I'm not sure how to classify your request. Please try again with more detail.\n")
            continue

        db = SQLDatabase(engine=engine)
        agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

        response = agent_executor.invoke({"input": user_input})
        formatted_response = response.get('output', 'Sorry, I could not process your request.')
        print("\nAI:", formatted_response, "\n")

if __name__ == "__main__":
    main()
