import sys

from bot.langgraph_agents import init_langgraph_agent, stream_langgraph_agent


def main():
    """
    Main function to run the agent with the specified model and question.

    This function retrieves the model name and question from the
    command line arguments and calls the `run_agent` function
    if a question is provided.

    Command line arguments:
    model_name (str): The name of the model to use.
    question (str): The question to ask the model.
    """
    provider = sys.argv[1]
    model_name = sys.argv[2]
    question = sys.argv[3]

    if question != "":
        agent_executor = init_langgraph_agent(provider, model_name)

        answer = stream_langgraph_agent(
            agent_executor=agent_executor,
            question=question,
        )
        print(answer)


if __name__ == "__main__":
    main()
