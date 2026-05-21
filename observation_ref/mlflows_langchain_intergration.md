```python


import mlflow
from langchain.tools import tool
from langchain.agents import create_agent


# Enable MLflow tracing
mlflow.langchain.autolog()


# Define a tool
@tool
def count_words(text: str) -> str:
    """Counts the number of words in a text."""
    word_count = len(text.split())
    return f"This text contains {word_count} words."


# Create a LangGraph agent
llm = ChatOpenAI(model="gpt-5.4")
tools = [count_words]
graph = create_agent(llm, tools)

# Run the agent
result = graph.invoke(
    {"messages": [{"role": "user", "content": "Write me a 71-word story about a cat."}]}
)
````