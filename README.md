# 🗂️ Organizador Automático de Arquivos

Script Python que organiza automaticamente os arquivos de uma pasta em subpastas por tipo.

## ✨ O que ele faz

Antes:
```
Downloads/
  foto.jpg
  curriculo.pdf
  musica.mp3
  script.py
  video.mp4
```

Depois:
```
Downloads/
  Imagens/
    foto.jpg
  Documentos/
    curriculo.pdf
  Musicas/
    musica.mp3
  Codigos/
    script.py
  Videos/
    video.mp4
  organizador_log.txt
```

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/fabiopy-creator/organizador-arquivos
```

2. Execute o script:
```bash
python organizador.py
```

3. Digite o caminho da pasta que quer organizar (ou pressione Enter para usar a pasta Downloads)

## 📁 Categorias suportadas

| Categoria | Extensões |
|-----------|-----------|
| Imagens | .jpg, .jpeg, .png, .gif, .svg, .webp |
| Vídeos | .mp4, .mov, .avi, .mkv |
| Músicas | .mp3, .wav, .aac, .flac |
| Documentos | .pdf, .doc, .docx, .txt, .xlsx |
| Compactados | .zip, .rar, .tar, .gz |
| Programas | .exe, .msi, .apk |
| Códigos | .py, .js, .html, .css, .java |
| Outros | tudo que não se encaixar acima |

## 🛠️ Tecnologias usadas

- Python 3
- Bibliotecas nativas: `os`, `shutil`, `datetime`
- Não precisa instalar nada extra!

## 👨‍💻 Autor

**Fabio Alexandre** — 17 anos, aprendendo Python com foco em automação.

[![GitHub](https://img.shields.io/badge/GitHub-fabiopy--creator-black)](https://github.com/fabiopy-creator)
