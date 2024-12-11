import asyncio
import socket
from colorama import Fore

input(Fore.LIGHTCYAN_EX + ''' 
███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗    ██████╗  ██████╗ ██████╗ ████████╗███████╗
████╗ ████║██╔══██╗██╔════╝ ██║██╔════╝    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
██╔████╔██║███████║██║  ███╗██║██║         ██████╔╝██║   ██║██████╔╝   ██║   ███████╗
██║╚██╔╝██║██╔══██║██║   ██║██║██║         ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╗    ██║     ╚██████╔╝██║  ██║   ██║   ███████║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                                                                     ENTER TO USE PORT SCANNER ''')

# Function to scan a single port
async def scan_port(target_host, port):
    conn = asyncio.open_connection(target_host, port)
    try:
        # Attempt to establish a connection with a short timeout
        reader, writer = await asyncio.wait_for(conn, timeout=1.0)
        writer.close()
        await writer.wait_closed()
        print(Fore.LIGHTGREEN_EX +f""" PORT {port} is           
   ___  ___ ___ _  _ ___ ___  
  / _ \| _ \ __| \| | __|   \  
 | (_) |  _/ _|| .` | _|| |) |
  \___/|_| |___|_|\_|___|___/ """)
    except (asyncio.TimeoutError, ConnectionRefusedError):
        # If connection is refused or times out, port is closed
        print(Fore.LIGHTRED_EX +f""" PORT {port} is            
   ___ _    ___  ___ ___ ___  
  / __| |  / _ \/ __| __|   \ 
 | (__| |_| (_) \__ \ _|| |) |
  \___|____\___/|___/___|___/ """)
# Function to scan multiple ports concurrently
async def scan_ports_concurrently(target_host, ports):
    tasks = []
    for port in ports:
        tasks.append(scan_port(target_host, port))
    await asyncio.gather(*tasks)
async def main():
    # Prompt for the target IP address
    target_host = input(Fore.LIGHTRED_EX + """        
               |))    |))
 .             |  )) /   ))
 \\   ^ ^      |    /      ))
  \\(((  )))   |   /        ))
   / G    )))  |  /        ))
  |o  _)   ))) | /       )))
   --' |     ))`/      )))
    ___|              )))
   / __\             ))))`()))
  /\@   /             `(())))
  \/   /  /`_______/\   \  ))))
       | |          \ \  |  )))
       | |           | | |   )))
       |_@           |_|_@    ))
      /_/           /_/_/  Enter TARGET IP... """)
    while True:
        user_input = input(Fore.LIGHTWHITE_EX +""" 
                           ENTER A PORT TO SCAN (OR TYPE 'EXIT' TO QUIT """)
        if user_input.lower() == 'exit':
            print(Fore.LIGHTYELLOW_EX +''' 
   EXITING PORT SCANNER... 🦄 ''') 
            break
        elif user_input.isdigit():
            port = int(user_input)
            await scan_ports_concurrently(target_host, [port])
        else:
            print("Please enter a valid port number or 'exit' to quit.")
# Run the program
asyncio.run(main())
