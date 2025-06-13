#### ⛓️ **`chains/`**: O Coração da Lógica LangChain

Aqui você constrói e organiza suas cadeias (chains). Cada arquivo pode representar uma cadeia específica com uma responsabilidade clara.

- **`qa_chain.py`**: Por exemplo, pode conter uma função que monta e retorna uma cadeia de "Perguntas e Respostas" (QA). Ela importa os modelos de `app/models/llm.py`, define os _prompts_ e constrói a `RunnableSequence` ou a cadeia LCEL (LangChain Expression Language).
