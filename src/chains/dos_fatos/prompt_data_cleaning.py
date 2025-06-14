from langchain_core.prompts import ChatPromptTemplate
from typing import Dict, Any

class PromptDataCleaning:
    """
    Classe que encapsula e gera um ChatPromptTemplate para limpeza de dados jurídicos.
    """

    def __init__(self, user_input: str):
        """
        Construtor da classe. Apenas armazena a entrada do usuário.

        Args:
            user_input (str): O texto de entrada do usuário (transcrição) a ser processado.
        """
        self.user_input = user_input

    def _get_system_prompt_text(self) -> str:
        """
        Método PRIVADO que retorna o texto base para a mensagem de "system".
        Este método agora contém um placeholder {transcricao_cliente} para formatação.
        """
        # O prompt agora tem um placeholder chamado {transcricao_cliente}
        system_prompt = """
# PERSONA E OBJETIVO

Você é um Assistente Jurídico de elite, especialista na elaboração da seção "Dos Fatos" para petições iniciais. Sua função é receber a transcrição de uma conversa e transformá-la em uma narrativa factual, clara, objetiva e cronologicamente ordenada, pronta para ser inserida em um documento judicial, utilizando exclusivamente a nomenclatura "Autor" e "Réu" para se referir às partes.

# PROCESSO E REGRAS OBRIGATÓRIAS

Para cada transcrição fornecida, você deve seguir RIGOROSAMENTE o seguinte processo de raciocínio em duas etapas antes de apresentar o resultado final:

**Etapa 1: Raciocínio Interno (Cadeia de Pensamento)**
1.  **Extração de Fatos Chave:** Leia a transcrição e liste todos os eventos, datas, locais, valores e ações relevantes mencionados. Ignore cumprimentos, desabafos emocionais e comentários do advogado.
2.  **Identificação das Partes:** Identifique claramente quem é o "Autor" (a pessoa que narrando os fatos para mover a ação) e o "Réu" (a pessoa ou entidade contra quem a ação será movida).
3.  **Ordenação Cronológica:** Organize a lista de fatos extraídos em uma sequência estritamente cronológica, do evento mais antigo para o mais recente.

**Etapa 2: Redação Final**
1.  **Narrativa em Terceira Pessoa:** Com base na lista ordenada, redija o texto final. Narre todos os fatos na terceira pessoa (ex: "O Autor fez...", "O Réu entregou...").
2.  **Linguagem Formal e Objetiva:** Use linguagem formal e neutra. Descreva os eventos sem qualquer juízo de valor, opinião, adjetivo subjetivo ou emoção.
3.  **Estrutura de Parágrafos:** Apresente a narrativa em parágrafos curtos e numerados. Cada parágrafo deve, idealmente, tratar de um único evento ou fato principal.
4.  **Fidelidade Absoluta:** NÃO adicione, omita ou altere qualquer informação factual. Sua tarefa é apenas reestruturar e reescrever os fatos conforme narrados pelo Autor.

# EXEMPLOS DE EXECUÇÃO
(Exemplos omitidos para brevidade, mas devem estar aqui como no seu original)
---

**INSTRUÇÃO FINAL:**

Agora, aplique este processo à transcrição abaixo. Apresente apenas o resultado final na seção `<FATOS_PARA_PETIÇÃO>`.

<TRANSCRIÇÃO_CLIENTE>
{transcricao_cliente}
</TRANSCRIÇÃO_CLIENTE>
"""
        return system_prompt

    def get_prompt_template(self) -> ChatPromptTemplate:
        """
        Método PÚBLICO que gera e retorna o objeto ChatPromptTemplate final.
        Este é o método que você chamará de fora da classe.
        """
        # 1. Pega o texto base do prompt de sistema.
        system_template = self._get_system_prompt_text()
        
        # 2. Cria o ChatPromptTemplate usando as mensagens de sistema e humana.
        #    O LangChain vai procurar a variável 'transcricao_cliente' quando for formatar.
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_template),
                # A mensagem "human" pode ficar vazia se toda a informação já está no system prompt.
                # Ou pode ser usada para um comando curto, como "Processe a transcrição.".
                ("human", "Por favor, estruture os fatos da transcrição fornecida."),
            ]
        )
        return prompt_template

    def format_prompt(self) -> Dict[str, Any]:
        """
        Método auxiliar que retorna o prompt formatado como um dicionário,
        pronto para ser passado para um modelo do LangChain.
        """
        template = self.get_prompt_template()
        # O método 'invoke' do template preenche os placeholders.
        formatted_prompt = template.invoke({"transcricao_cliente": self.user_input})
        return formatted_prompt