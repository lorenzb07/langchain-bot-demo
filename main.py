import sys

from bot import run_agent


def main():
    model = sys.argv[1]
    question = sys.argv[2]

    if question != "":
        run_agent(
            model_name=model,
            question=question,
        )

if __name__ == "__main__":
    main()
