class Hardware:

    def get_cpu_temp(self):
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp = float(file.read()) / 1000
        return temp
