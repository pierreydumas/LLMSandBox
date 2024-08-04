# demo_grammar.py

`requirements.txt`:
```
py-llm-core==2.8.12
attrs==23.2.0
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
referencing==0.35.1
typing_extensions==4.12.2
```

On Windows, using a virtualenv based on Python 3.9. GPU acceleration may require more digging.

```
C:\_\run\Python\Python39\python.exe -m venv venv
venv\Scripts\activate
pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.2.82-cu124/llama_cpp_python-0.2.82-cp39-cp39-win_amd64.whl
pip install -r requirements.txt
python demo_grammar.py
```