
class ChatModelFactory:

    @staticmethod
    def get_model(model_name: str):
        if model_name == "azure_openai":
            try:
                from langchain_openai import AzureChatOpenAI
            except ImportError:
                raise ImportError("AzureChatOpenAI module is not installed. Please install it to use this model.")

            return AzureChatOpenAI(
                model="gpt-4o",  # o il tuo deployment
                temperature=0,
                max_retries=2,
                # altri parametri...
            )
        elif model_name == "groq":
            try:
                from langchain_groq import ChatGroq
            except ImportError:
                raise ImportError("GroqChat module is not installed. Please install it to use this model.")

            return ChatGroq(
                model="mixtral-8x7b-32768",  # o il tuo deployment
                temperature=0,
                max_retries=2,
                # altri parametri...
            )
        else:
            raise ValueError(f"Model {model_name} not supported")