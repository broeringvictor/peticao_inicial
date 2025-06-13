# tests/core/test_llm_factory.py

import pytest
from unittest.mock import patch, MagicMock
from core.llm_factory import LLMFactory  
import os


FAKE_LANGCHAIN_MODEL = MagicMock()
FAKE_LANGCHAIN_MODEL.invoke.return_value = "Resposta do modelo mockado."


@pytest.fixture(autouse=True)
def clear_env_vars(monkeypatch):
    """
    Fixture que roda automaticamente antes de cada teste para garantir
    que as chaves de API não estejam no ambiente, evitando interferência
    entre os testes.
    """
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)



@patch('core.llm_factory.init_chat_model', return_value=FAKE_LANGCHAIN_MODEL)
def test_create_success_with_key_present(mock_init_chat_model, monkeypatch):
    """
    Testa o "caminho feliz": a chave de API já existe no ambiente.
    Verifica se `init_chat_model` é chamada com os argumentos corretos.
    """
    # ARRANGE: Prepara o ambiente
    monkeypatch.setenv("GOOGLE_API_KEY", "minha-chave-falsa-123")
    
    # ACT: Executa a função
    model = LLMFactory.create(
        model_name="gemini-1.5-pro",
        model_provider="google_genai",
        temperature=0.8
    )

    # ASSERT: Verifica os resultados
    assert model is FAKE_LANGCHAIN_MODEL
    mock_init_chat_model.assert_called_once_with(
        "gemini-1.5-pro",
        model_provider="google_genai",
        temperature=0.8
    )


# CORREÇÃO AQUI (nas duas linhas): de 'llm_google' para 'llm_factory'
@patch('core.llm_factory.getpass.getpass', return_value="chave-digitada-pelo-mock")
@patch('core.llm_factory.init_chat_model', return_value=FAKE_LANGCHAIN_MODEL)
def test_create_prompts_for_key_if_missing(mock_init_chat_model, mock_getpass):
    """
    Testa o caso onde a chave de API não existe, verificando se o `getpass` é chamado.
    """
    # ARRANGE: O ambiente está limpo (garantido pela fixture `clear_env_vars`)

    # ACT: Executa a função
    LLMFactory.create(
        model_name="gemini-1.5-flash",
        model_provider="google_genai"
    )

    # ASSERT: Verifica se os mocks foram chamados
    mock_getpass.assert_called_once()
    mock_init_chat_model.assert_called_once()
    assert os.environ.get("GOOGLE_API_KEY") == "chave-digitada-pelo-mock"



@patch('core.llm_factory.init_chat_model')
def test_create_returns_none_on_error(mock_init_chat_model, monkeypatch, capsys):
    """
    Testa o tratamento de erro: se `init_chat_model` falhar, a factory deve retornar None.
    """
    # ARRANGE: Prepara o ambiente e configura o mock para levantar um erro
    monkeypatch.setenv("GOOGLE_API_KEY", "minha-chave-falsa-123")
    error_message = "API key is invalid"
    mock_init_chat_model.side_effect = ValueError(error_message)

    # ACT: Executa a função
    model = LLMFactory.create(
        model_name="gemini-1.5-flash",
        model_provider="google_genai"
    )

 
    assert model is None
    captured = capsys.readouterr()
    assert "❌ (LLMFactory60) Erro ao inicializar o modelo" in captured.out
    assert error_message in captured.out