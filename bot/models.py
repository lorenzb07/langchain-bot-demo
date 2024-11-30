class ChatModelFactory:

    @staticmethod
    def get_llm(provider: str, model_name: str):
        if provider == "openai":
            try:
                from langchain_openai import ChatOpenAI
            except ImportError:
                raise ImportError(
                    "ChatOpenAI module is not installed. "
                    "Please install it to use this model."
                )

            return ChatOpenAI(
                model=model_name,
                temperature=0,
                max_retries=2,
                # altri parametri...
            )
        elif provider == "azure_openai":
            try:
                from langchain_openai import AzureChatOpenAI
            except ImportError:
                raise ImportError(
                    "AzureChatOpenAI module is not installed. "
                    "Please install it to use this model."
                )

            return AzureChatOpenAI(
                model=model_name,
                temperature=0,
                max_retries=2,
                # altri parametri...
            )
        elif provider == "groq":
            try:
                from langchain_groq import ChatGroq
            except ImportError:
                raise ImportError(
                    "GroqChat module is not installed. "
                    "Please install it to use this model."
                )

            return ChatGroq(
                model=model_name,
                temperature=0,
                max_retries=2,
                # altri parametri...
            )
        else:
            raise ValueError(f"Model {provider} not supported")
