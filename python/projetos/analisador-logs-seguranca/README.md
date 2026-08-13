# Analisador de Logs de Segurança

Projeto em Python que analisa registros de autenticação e identifica possíveis tentativas de ataque de força bruta.

## Funcionalidades

- Leitura de arquivos de log
- Contagem de logins com sucesso e falha
- Agrupamento de falhas por endereço IP
- Detecção de três falhas dentro de 60 segundos
- Tratamento de linhas vazias ou incompletas
- Tratamento de datas inválidas

## Formato do log

Cada registro deve seguir este formato:

```text
AAAA-MM-DD HH:MM:SS | ENDEREÇO_IP | EVENTO | USUÁRIO
```

## Eventos reconhecidos

- `LOGIN_SUCESSO`
- `LOGIN_FALHA`

## Como executar

Na pasta principal do repositório, execute:

```powershell
python python/projetos/analisador-logs-seguranca/analisador.py
```

## Exemplo de saída

```text
RESUMO DA ANÁLISE
Logins com sucesso: 3
Logins com falha: 6

Falhas por IP
192.168.1.25: 4 falhas
192.168.1.40: 2 falhas

ANÁLISE POR TEMPO
IP: 192.168.1.25
ALERTA: 3 falhas em 15.0 segundos
```

## Tecnologias e conceitos

- Python
- Manipulação de arquivos
- Listas e dicionários
- Estruturas condicionais e repetições
- Tratamento de exceções
- Datas e intervalos de tempo
- Análise básica de eventos de segurança

