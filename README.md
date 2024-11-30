# LangChain Bot Demo

This is a simple demo of a chatbot that uses different language models to generate responses to user prompts using the `LangChain` library.

## Usage

### Requirements

To install the required packages, run the following command:

```bash
pip3 install -r requirements.txt
```


### Environment variables

In order to use the `OpenAI API`, you need to set the environment variables:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
export OPENAI_API_VERSION="YOUR_OPENAI_API_VERSION"
```

In order to use the `Azure OpenAI API`, you need to set the environment variables:

```bash
export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export OPENAI_API_VERSION="YOUR_OPENAI_API_VERSION"
```

In order to use the `GROQ API`, you need to set the environment variables:

```bash
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

To run the _Streamlit_ application, you need also to set the environment variables:

```bash
export STREAMLIT_LLM_PROVIDER="YOUR_PROVIDER"
export STREAMLIT_LLM_MODEL="YOUR_MODEL_NAME"
```

### Running the application

To run the python application, run the following command:

```bash
python3 main.py "[PROVIDER]" "[MODEL_NAME]" "[YOUR_PROMPT]"
```

The supported providers are:
- `openai`
- `azure_openai`
- `groq`

To run the _Streamlit_ application, run the following command:

```bash
streamlit run chatbot.py
```
