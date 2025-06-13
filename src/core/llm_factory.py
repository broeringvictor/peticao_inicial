import getpass
import os
from typing import Any
from langchain.chat_models import init_chat_model


try:
    from dotenv import load_dotenv
    load_dotenv()
    print("📄 Variáveis de ambiente carregadas do .env")
except ImportError:
    print("⚠️ Biblioteca python-dotenv não encontrada, pulando carregamento do .env")
    pass



class LLMFactory:
    """
    Inicializa e gerencia qualquer Chat Model
    suportado pela LangChain usando a função init_chat_model.
    Exemplo de uso:
    
    gemini = LLMFactory.create(
            "gemini-1.5-flash", 
            model_provider="google_genai", 
            temperature=0.7
        )
    """

    @staticmethod
    def create(
        model_name: str,
        model_provider: str,
        **kwargs: Any
    ):
               
        if "google" in f"{model_name}{model_provider}" and not os.environ.get("GOOGLE_API_KEY"):
            print("🔑 Chave de API do Google não encontrada no ambiente.")
            os.environ["GOOGLE_API_KEY"] = getpass.getpass("Digite a sua GOOGLE_API_KEY: ")
        
        """
        if "openai" in f"{model_name}{model_provider}" and not os.environ.get("OPENAI_API_KEY"):
            print("🔑 Chave de API da OpenAI não encontrada no ambiente.")
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Digite a sua OPENAI_API_KEY: ")
        """
        

        print(f"\n🔄 Inicializando modelo: '{model_name}' com os parâmetros: {kwargs}")
        try:          
            
            model_instance = init_chat_model(
                model_name,
                model_provider=model_provider,
                **kwargs
            )
            print("✅ Modelo inicializado com sucesso!")
            return model_instance
        except (ValueError, ImportError) as e:
            print(f"❌ (LLMFactory60) Erro ao inicializar o modelo: {e}")
            print("-> Verifique se o nome do modelo está correto e se a biblioteca de integração está instalada. tente instalar: uv pip install -qU \"langchain[google-genai]\"")
            return None