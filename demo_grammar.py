from dataclasses import dataclass
from llama_cpp import LlamaGrammar, Llama  # Aka lama-cpp-python
from llm_core.schema import to_json_schema, SchemaConverter  # Aka py-llm-core

# Define the model path
model_path = "C:\\Users\\Peter\\.cache\\lm-studio\\models\\TheBloke\\Mistral-7B-Instruct-v0.1-GGUF\\" + \
             "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Create a Llama model instance
model = Llama(model_path=model_path, n_ctx=4096, n_threads=4)


@dataclass
class FamousPerson:
    full_name: str
    date_of_birth: str
    place_of_birth: str
    nationality: str
    date_of_death: str

    @classmethod
    def schema(cls):
        return to_json_schema(cls)


def generate_grammar(schema):
    converter = SchemaConverter({})
    converter.visit(schema, '')
    bnf_string = converter.format_grammar()
    return LlamaGrammar.from_string(bnf_string)


grammar = generate_grammar(FamousPerson.schema())
parameters = {
    "grammar": grammar,
    "temperature": 0.1,
    "max_tokens": 512
}

# Generate a response from the model
response_dictionary = model("Napoleon", **parameters)
response_text = response_dictionary['choices'][0]['text']
print(response_text)
