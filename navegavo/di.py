from llama_index.core.multi_modal_llms.base import MultiModalLLM
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from llama_index.multi_modal_llms.gemini import GeminiMultiModal # type: ignore

def llm_factory() -> MultiModalLLM:
    return GeminiMultiModal()
