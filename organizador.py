import os
import shutil
from datetime import datetime

# ================================================
# ORGANIZADOR AUTOMÁTICO DE ARQUIVOS
# Criado por: Fabio Alexandre
# Descrição: Move arquivos de uma pasta para
#            subpastas organizadas por tipo
# ================================================

# --- CONFIGURAÇÃO ---
# Troca esse caminho pela pasta que quer organizar
# Exemplo Windows: "C:/Users/Fabio/Downloads"
PASTA_ALVO = os.path.expanduser("~/Downloads")

# Dicionário de categorias: tipo -> extensões
CATEGORIAS = {
    "Imagens":      [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos":       [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Musicas":      [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Documentos":   [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".pptx"],
    "Compactados":  [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programas":    [".exe", ".msi", ".dmg", ".apk"],
    "Codigos":      [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts"],
    "Outros":       []  # arquivos sem categoria conhecida
}


def obter_categoria(extensao):
    """Retorna a categoria de um arquivo pela extensão."""
    extensao = extensao.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"


def organizar(pasta):
    """Organiza os arquivos da pasta em subpastas por tipo."""

    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"❌ Pasta não encontrada: {pasta}")
        return

    arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

    if not arquivos:
        print("📂 Nenhum arquivo encontrado na pasta.")
        return

    print(f"\n🚀 Iniciando organização de: {pasta}")
    print(f"📄 {len(arquivos)} arquivo(s) encontrado(s)\n")

    movidos = 0
    ignorados = 0
    log = []

    for arquivo in arquivos:
        # Ignora arquivos ocultos (começam com ponto)
        if arquivo.startswith("."):
            ignorados += 1
            continue

        caminho_origem = os.path.join(pasta, arquivo)
        extensao = os.path.splitext(arquivo)[1]
        categoria = obter_categoria(extensao)

        # Cria a subpasta se não existir
        pasta_destino = os.path.join(pasta, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        caminho_destino = os.path.join(pasta_destino, arquivo)

        # Evita sobrescrever arquivos com o mesmo nome
        if os.path.exists(caminho_destino):
            nome, ext = os.path.splitext(arquivo)
            timestamp = datetime.now().strftime("%H%M%S")
            arquivo = f"{nome}_{timestamp}{ext}"
            caminho_destino = os.path.join(pasta_destino, arquivo)

        shutil.move(caminho_origem, caminho_destino)

        print(f"  ✅ {arquivo:<40} → {categoria}/")
        log.append(f"{arquivo} → {categoria}/")
        movidos += 1

    # Salva um log da operação
    salvar_log(pasta, log)

    print(f"\n{'='*50}")
    print(f"✨ Organização concluída!")
    print(f"   📦 Movidos:   {movidos} arquivo(s)")
    print(f"   ⏭️  Ignorados: {ignorados} arquivo(s)")
    print(f"   📝 Log salvo em: organizador_log.txt")
    print(f"{'='*50}\n")


def salvar_log(pasta, log):
    """Salva um arquivo de log com o histórico da organização."""
    caminho_log = os.path.join(pasta, "organizador_log.txt")
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Organização realizada em {agora}\n")
        f.write(f"{'='*50}\n")
        for linha in log:
            f.write(f"  {linha}\n")


# --- EXECUÇÃO ---
if __name__ == "__main__":
    print("=" * 50)
    print("  ORGANIZADOR AUTOMÁTICO DE ARQUIVOS 🗂️")
    print("  Criado por Fabio Alexandre")
    print("=" * 50)

    pasta = input(f"\nDigite o caminho da pasta (Enter para usar Downloads):\n> ").strip()

    if not pasta:
        pasta = PASTA_ALVO

    organizar(pasta)