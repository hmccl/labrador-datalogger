# Datalogger

O projeto implementa um datalogger na SBC Labrador 32.

## Instruções

1. Crie um ambiente virtual.

   ```bash
   python3 -m venv .venv
   ```

1. Ative o ambiente virtual.

   ```bash
   source .venv/bin/activate
   ```

1. Instale as dependências.

   ```bash
   pip install -r requirements.txt
   ```

1. Identifique e monte a unidade que deseja utilizar.

   ```bash
   lsblk
   sudo mount -m /dev/mmcblk0p1 /media/caninos/adata64
   ```

1. Altere os valores das variáveis se necessário.

   ```python
   SD_CARD = "/media/caninos/adata64"
   DATALOGGER = "/data.txt"
   ```

1. Execute o programa.
   Utiliza-se o superusuário para simplificar o uso das permissões.
   No entanto, não é recomendado.

   ```bash
   sudo $PWD/.venv/bin/python main.py
   ```
