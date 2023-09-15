from aiogram import types
from datetime import datetime
import psutil
import matplotlib.pyplot as plt
from matplotlib import dates
from io import BytesIO

# Устанавливаем стандартные команды бота

async def set_default_commands(dp):
    await dp.bot.set_my_commands([types.BotCommand("start", "Запустить бота")])


# Получаем текущее состояние машины

async def get_stats():
    stats = dict()

    stats['timestamp'] = datetime.now()
    stats['cpu_usage'] = psutil.cpu_percent()
    stats['memory_usage'] = psutil.virtual_memory().percent
    stats['swap_usage'] = psutil.swap_memory().percent
    stats['disk_usage'] = psutil.disk_usage('/').percent
    stats['cpu_temperature'] = psutil.sensors_temperatures()["acpitz"][0].current

    return stats


# Построение графиков

async def draw_plots(history):
    fmt = dates.DateFormatter('%H:%M %d.%m.%Y')
    timestamps = [i.timestamp for i in history]

    cpu_u_fig, cpu_u_plt = plt.subplots()
    cpu_u_plt.set_title("CPU usage")
    cpu_usages = [i.cpu_usage for i in history]
    cpu_u_plt.plot(timestamps, cpu_usages, "-o")
    cpu_u_plt.xaxis.set_major_formatter(fmt)
    cpu_u_fig.autofmt_xdate()
    cpu_u_img = BytesIO()
    cpu_u_fig.savefig(cpu_u_img)

    cpu_t_fig, cpu_t_plt = plt.subplots()
    cpu_t_plt.set_title("CPU temperature")
    cpu_usages = [i.cpu_usage for i in history]
    cpu_t_plt.plot(timestamps, cpu_usages, "-o")
    cpu_t_plt.xaxis.set_major_formatter(fmt)
    cpu_t_fig.autofmt_xdate()
    cpu_t_img = BytesIO()
    cpu_t_fig.savefig(cpu_t_img)

    memory_u_fig, memory_u_plt = plt.subplots()
    memory_u_plt.set_title("RAM usage")
    memory_usages = [i.memory_usage for i in history]
    memory_u_plt.plot(timestamps, memory_usages, "-o")
    memory_u_plt.xaxis.set_major_formatter(fmt)
    memory_u_fig.autofmt_xdate()
    memory_u_img = BytesIO()
    memory_u_fig.savefig(memory_u_img)

    swap_u_fig, swap_u_plt = plt.subplots()
    swap_u_plt.set_title("Swap usage")
    swap_usages = [i.swap_usage for i in history]
    swap_u_plt.plot(timestamps, swap_usages, "-o")
    swap_u_plt.xaxis.set_major_formatter(fmt)
    swap_u_fig.autofmt_xdate()
    swap_u_img = BytesIO()
    swap_u_fig.savefig(swap_u_img)

    disk_u_fig, disk_u_plt = plt.subplots()
    disk_u_plt.set_title("Disk usage")
    disk_usages = [i.disk_usage for i in history]
    disk_u_plt.plot(timestamps, disk_usages, "-o")
    disk_u_plt.xaxis.set_major_formatter(fmt)
    disk_u_fig.autofmt_xdate()
    disk_u_img = BytesIO()
    disk_u_fig.savefig(disk_u_img)

    return [cpu_u_img, cpu_t_img, memory_u_img, swap_u_img, disk_u_img]

    
