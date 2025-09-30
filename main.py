import time
from datetime import datetime
from periphery import I2C

# Path
SD_CARD = "/media/caninos/adata64"
DATALOGGER = "/datalogger/data.txt"

# AHT10 config
I2C_2_BUS = "/dev/i2c-2"
I2C_2_ADDRESS = 0x38
i2c_2 = I2C(I2C_2_BUS)

# BH1750 config
# I2C_3_BUS = "/dev/i2c-3"
# I2C_3_ADDRESS = 0x38 ??
# i2c_3 = I2C(I2C_3_BUS)


def aht10_init():
    """
    AHT10 sensor init.
    """

    init_command = [0xBE, 0x08, 0x00]
    i2c_2.transfer(I2C_2_ADDRESS, [I2C.Message(init_command)])
    time.sleep(0.5)


def aht10_measure():
    """
    AHT10 sensor measure.
    """

    measure_command = [0xAC, 0x33, 0x00]
    i2c_2.transfer(I2C_2_ADDRESS, [I2C.Message(measure_command)])
    time.sleep(1)


def aht10_read():
    """
    AHT10 sensor read.
    Returns 6 bytes os data.
    """

    read_command = I2C.Message([0x00] * 6, read=True)
    i2c_2.transfer(I2C_2_ADDRESS, [read_command])

    return read_command.data


def aht10_data(data):
    """
    Receives 6 bytes of data.
    Humidity: bytes 1, 2, 3 (half).
    Temperature: bytes 3 (half), 4, 5.
    Returns humidity (percentage) and temperature (degree Celsius)
    """

    humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) * 100 / (1 << 20)
    temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) * 200 / (
        1 << 20
    ) - 50

    return humidity, temperature


def main():
    aht10_init()

    try:
        while True:
            timestamp = datetime.now()
            aht10_measure()
            hum, temp = aht10_data(aht10_read())
            print(f"{timestamp} --- Umid: {hum:.2f}% | Temp: {temp:.2f}°C")
            with open(SD_CARD + DATALOGGER, "a") as f:
                f.write(f"{timestamp} --- Umid: {hum:.2f}% | Temp: {temp:.2f}°C\n")

    except KeyboardInterrupt:
        i2c_2.close()
        # i2c_3.close()
        print("\nFim da execução!")


if __name__ == "__main__":
    main()
