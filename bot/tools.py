from datetime import datetime

from langchain_core.tools import tool


@tool
def today():
    """
    Get the current date in the format YYYY-MM-DD.

    Returns:
        str: The current date in the format YYYY-MM-DD.
    """
    return datetime.now().strftime("%Y-%m-%d")
