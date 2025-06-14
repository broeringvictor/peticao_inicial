from core.llm_factory import LLMFactory

class DosFatosModel:    
    """
    Classe que encapsula o modelo de linguagem para a aplicação Dos Fatos.    
    """

    def __init__(self):
        self.model = self._initialize_model()

    def _initialize_model(self):
        data_cleaning = self._data_cleaning()

        return{
            "data_cleaning": data_cleaning
        }            
        

    def _data_cleaning(self):
        """
        Método para limpeza de dados.
        """
        data_cleaning = LLMFactory.create(
            "gemini-2.5-flash-preview-05-20", 
            model_provider="google_genai", 
            temperature=0.7)
        
        return data_cleaning


