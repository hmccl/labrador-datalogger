# Datalogger

O projeto implementa um datalogger na SBC Labrador 32.

## Conexão

A seguir descreve-se as conexões dos sensores com a Labrador.

### AHT10

 Sensor AHT10     Interface Serial Labrador
-------------- --------------------------------
     VDD               Pino 01 (3.3 V)
     GND                Pino 06 (GND)
     SDA        Pino 03 (GPIO-E03, I2C2_SDATA)
     SCL        Pino 05 (GPIO-E02, I2C2_SCLK)

### BH1750

 Sensor BH1750     Interface Serial Labrador
--------------- --------------------------------
      VDD               Pino 17 (3.3 V)
      GND                Pino 25 (GND)
      SDA        Pino 19 (GPIO-C25, I2C3_SDATA)
      SCL        Pino 23 (GPIO-C22, I2C3_SCLK)

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

1. Altere os valores das variáveis globais se necessário.

   ```python
   INTERVAL_SEC = 1
   SD_CARD = "/media/caninos/adata64"
   DATALOGGER = "/data.txt"
   ```

1. Execute o programa.
   Utiliza-se o superusuário para simplificar o uso das permissões.
   No entanto, não é recomendado.

   ```bash
   sudo $PWD/.venv/bin/python main.py
   ```
