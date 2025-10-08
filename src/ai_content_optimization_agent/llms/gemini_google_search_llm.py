from crewai import LLM
import os
from typing import Any, Optional

# Define a custom Gemini LLM integration with Google Search grounding
class GeminiWithGoogleSearch(LLM):
    """
    A Gemini-specific LLM that has the "google_search" tool enabled.
    """

    def __init__(self, model: str | None = None, **kwargs):
        if not model:
            # Use a default Gemini model.
            model = os.getenv("MODEL")

        super().__init__(model, **kwargs)


    def call(
        self,
        messages: str | list[dict[str, str]],
        tools: list[dict] | None = None,
        callbacks: list[Any] | None = None,
        available_functions: dict[str, Any] | None = None,
        from_task: Optional[Any] = None,
        from_agent: Optional[Any] = None,
    ) -> str | Any:
        if not tools:
            tools = []

        # LiteLLM will throw a warning if it sees `google_search`,
        # so you must use camel case here
        tools.insert(0, {"googleSearch": {}})

        return super().call(
            messages=messages,
            tools=tools,
            callbacks=callbacks,
            available_functions=available_functions,
            from_task=from_task,
            from_agent=from_agent,
        )
