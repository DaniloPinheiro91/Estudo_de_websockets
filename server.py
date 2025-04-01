import asyncio
import websockets

# Função handler que deve receber os parâmetros websocket e path corretamente
async def handler(websocket, path):
    print(f"Nova conexão estabelecida, path: {path}")  # Imprime o path para verificar se está correto

    try:
        # Envia uma mensagem inicial ao cliente
        await websocket.send("Conexão estabelecida! Envie sua mensagem.")
        
        while True:
            # Espera e recebe uma mensagem do cliente
            message = await websocket.recv()
            print(f"Mensagem recebida: {message}")  # Verifica a mensagem recebida do cliente

            # Responde ao cliente
            await websocket.send(f"Servidor: Você enviou '{message}'")

    except Exception as e:
        # Se ocorrer algum erro na comunicação, imprime o erro
        print(f"Ocorreu um erro durante a comunicação: {e}")
    finally:
        # Quando a conexão for fechada, imprime uma mensagem
        print("A conexão foi fechada.")

# Função principal para rodar o servidor WebSocket
async def main():
    try:
        # Inicia o servidor WebSocket na URL e porta especificadas
        server = await websockets.serve(handler, "localhost", 8765)
        print("Servidor WebSocket em execução na ws://localhost:8765")

        # Aguarda o servidor continuar em execução
        await server.wait_closed()
    except Exception as e:
        # Se o servidor não conseguir iniciar, imprime o erro
        print(f"Ocorreu um erro ao iniciar o servidor: {e}")

# Executa o servidor WebSocket
if __name__ == "__main__":
    asyncio.run(main())