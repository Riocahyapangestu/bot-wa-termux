import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

print("""
 ▄     ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ 
█ █ ▄ █ █       █  █▄█  █       █  █ █  █
█ ██ ██ █    ▄▄▄█       █    ▄  █  █▄█  █
█       █   █▄▄▄█       █   █▄█ █       █
█       █    ▄▄▄█       █    ▄▄▄█▄     ▄█
█   ▄   █   █▄▄▄█ ██▄██ █   █     █   █  
█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄█     █▄▄▄█  

      ░ ░\x1b[00m\033[041m TERMUX WHATSAPP BOT WEM  \033[00m\x1b[1;00m░░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░\x1b[00m
""")
m('\x1b[00m\033[041m Sedang Memulai...  \033[00m')
m('\x1b[00m\033[041m Silahkan Scan Kode QR Nya Ya  \033[00m')
os.system("node index.js")
m("DONE")
