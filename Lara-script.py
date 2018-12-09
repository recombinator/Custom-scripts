from netmiko import ConnectHandler
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()


def menu():
    def er_disable_int_lara():

        edgerouter = {
            "device_type": "vyos",
            "ip": "192.168.10.254",
            "username": "admin",
            "password": "G1zm0123!",
        }

        net_connect = ConnectHandler(**edgerouter)

        config_commands = ['set firewall name IOT-WAN rule 1 disable',
                           'set firewall name IOT-WAN rule 2 disable',
                           'set firewall name IOT-WAN rule 3 disable',
                           'set firewall name IOT-WAN rule 4 disable',
                           'set firewall name IOT-WAN rule 5 disable',
                           'set firewall name IOT-WAN rule 6 disable',
                           'set firewall name IOT-WAN rule 7 disable',
                           'set firewall name IOT-WAN rule 8 disable',
                           'set firewall name IOT-WAN rule 9 disable',
                           'set firewall name IOT-WAN rule 10 disable',
                           'set firewall name IOT-WAN rule 11 disable',
                           'set firewall name IOT-WAN rule 12 disable',
                           'set firewall name IOT-WAN rule 13 disable',
                           'set firewall name IOT-WAN rule 14 disable',
                           'set firewall name IOT-WAN rule 15 disable',
                           'delete firewall name IOT-WAN rule 50 disable',
                           'delete firewall name IOT-WAN rule 51 disable',
                           'delete firewall name IOT-WAN rule 52 disable',
                           'set firewall name LAN-IOT rule 1 disable',
                           'set firewall name LAN-IOT rule 2 disable',
                           'set firewall name LAN-IOT rule 3 disable',
                           'set firewall name LAN-IOT rule 4 disable',
                           'set firewall name LAN-IOT rule 5 disable',
                           'set firewall name LAN-IOT rule 6 disable',
                           'set firewall name LAN-IOT rule 7 disable',
                           'set firewall name LAN-IOT rule 8 disable',
                           'set firewall name LAN-IOT rule 9 disable',
                           'set firewall name LAN-IOT rule 10 disable',
                           'set firewall name LAN-IOT rule 11 disable',
                           'set firewall name LAN-IOT rule 12 disable',
                           'set firewall name LAN-IOT rule 13 disable',
                           'set firewall name LAN-IOT rule 14 disable',
                           'set firewall name LAN-IOT rule 15 disable',
                           'delete firewall name LAN-IOT rule 50 disable',
                           'delete firewall name LAN-IOT rule 51 disable',
                           'delete firewall name LAN-IOT rule 52 disable',
                           'delete firewall name IOT-LAN rule 1 disable',
                           'delete firewall name IOT-LAN rule 2 disable',
                           'delete firewall name IOT-LAN rule 3 disable',
                           'delete firewall name IOT-LAN rule 4 disable',
                           'delete firewall name IOT-LAN rule 5 disable',
                           'commit',
                           'exit'
                           ]

        output = net_connect.send_config_set(config_commands)
        print(output)

    def er_enable_int_lara():

        edgerouter = {
            "device_type": "vyos",
            "ip": "192.168.10.254",
            "username": "admin",
            "password": "G1zm0123!",
        }

        net_connect = ConnectHandler(**edgerouter)

        config_commands = ['set firewall name IOT-WAN rule 1 disable',
                           'set firewall name IOT-WAN rule 2 disable',
                           'set firewall name IOT-WAN rule 3 disable',
                           'set firewall name IOT-WAN rule 4 disable',
                           'set firewall name IOT-WAN rule 5 disable',
                           'set firewall name IOT-WAN rule 6 disable',
                           'set firewall name IOT-WAN rule 7 disable',
                           'set firewall name IOT-WAN rule 8 disable',
                           'set firewall name IOT-WAN rule 9 disable',
                           'set firewall name IOT-WAN rule 10 disable',
                           'set firewall name IOT-WAN rule 11 disable',
                           'set firewall name IOT-WAN rule 12 disable',
                           'set firewall name IOT-WAN rule 13 disable',
                           'set firewall name IOT-WAN rule 14 disable',
                           'set firewall name IOT-WAN rule 15 disable',
                           'set firewall name IOT-WAN rule 50 disable',
                           'set firewall name IOT-WAN rule 51 disable',
                           'set firewall name IOT-WAN rule 52 disable',
                           'set firewall name LAN-IOT rule 1 disable',
                           'set firewall name LAN-IOT rule 2 disable',
                           'set firewall name LAN-IOT rule 3 disable',
                           'set firewall name LAN-IOT rule 4 disable',
                           'set firewall name LAN-IOT rule 5 disable',
                           'set firewall name LAN-IOT rule 6 disable',
                           'set firewall name LAN-IOT rule 7 disable',
                           'set firewall name LAN-IOT rule 8 disable',
                           'set firewall name LAN-IOT rule 9 disable',
                           'set firewall name LAN-IOT rule 10 disable',
                           'set firewall name LAN-IOT rule 11 disable',
                           'set firewall name LAN-IOT rule 12 disable',
                           'set firewall name LAN-IOT rule 13 disable',
                           'set firewall name LAN-IOT rule 14 disable',
                           'set firewall name LAN-IOT rule 15 disable',
                           'set firewall name LAN-IOT rule 50 disable',
                           'set firewall name LAN-IOT rule 51 disable',
                           'set firewall name LAN-IOT rule 52 disable',
                           'set firewall name IOT-LAN rule 1 disable',
                           'set firewall name IOT-LAN rule 2 disable',
                           'set firewall name IOT-LAN rule 3 disable',
                           'set firewall name IOT-LAN rule 4 disable',
                           'set firewall name IOT-LAN rule 5 disable',
                           'commit',
                           'exit'
                           ]

        output = net_connect.send_config_set(config_commands)
        print(output)

    def er_schedule_int_lara():

        edgerouter = {
            "device_type": "vyos",
            "ip": "192.168.10.254",
            "username": "admin",
            "password": "G1zm0123!",
        }

        net_connect = ConnectHandler(**edgerouter)

        config_commands = ['delete firewall name IOT-WAN rule 1 disable',
                           'delete firewall name IOT-WAN rule 2 disable',
                           'delete firewall name IOT-WAN rule 3 disable',
                           'delete firewall name IOT-WAN rule 4 disable',
                           'delete firewall name IOT-WAN rule 5 disable',
                           'delete firewall name IOT-WAN rule 6 disable',
                           'delete firewall name IOT-WAN rule 7 disable',
                           'delete firewall name IOT-WAN rule 8 disable',
                           'delete firewall name IOT-WAN rule 9 disable',
                           'delete firewall name IOT-WAN rule 10 disable',
                           'delete firewall name IOT-WAN rule 11 disable',
                           'delete firewall name IOT-WAN rule 12 disable',
                           'delete firewall name IOT-WAN rule 13 disable',
                           'delete firewall name IOT-WAN rule 14 disable',
                           'delete firewall name IOT-WAN rule 15 disable',
                           'set firewall name IOT-WAN rule 50 disable',
                           'set firewall name IOT-WAN rule 51 disable',
                           'set firewall name IOT-WAN rule 52 disable',
                           'delete firewall name LAN-IOT rule 1 disable',
                           'delete firewall name LAN-IOT rule 2 disable',
                           'delete firewall name LAN-IOT rule 3 disable',
                           'delete firewall name LAN-IOT rule 4 disable',
                           'delete firewall name LAN-IOT rule 5 disable',
                           'delete firewall name LAN-IOT rule 6 disable',
                           'delete firewall name LAN-IOT rule 7 disable',
                           'delete firewall name LAN-IOT rule 8 disable',
                           'delete firewall name LAN-IOT rule 9 disable',
                           'delete firewall name LAN-IOT rule 10 disable',
                           'delete firewall name LAN-IOT rule 11 disable',
                           'delete firewall name LAN-IOT rule 12 disable',
                           'delete firewall name LAN-IOT rule 13 disable',
                           'delete firewall name LAN-IOT rule 14 disable',
                           'delete firewall name LAN-IOT rule 15 disable',
                           'set firewall name LAN-IOT rule 50 disable',
                           'set firewall name LAN-IOT rule 51 disable',
                           'set firewall name LAN-IOT rule 52 disable',
                           'delete firewall name IOT-LAN rule 1 disable',
                           'delete firewall name IOT-LAN rule 2 disable',
                           'delete firewall name IOT-LAN rule 3 disable',
                           'delete firewall name IOT-LAN rule 4 disable',
                           'delete firewall name IOT-LAN rule 5 disable',
                           'commit',
                           'exit'
                           ]

        output = net_connect.send_config_set(config_commands)
        print(output)

    while True:
        print("""
        1.Fully disable Internet Access for Lara
        2.Enable Full Internet Access for Lara
        3.Enable Scheduled Internet Access for Lara (Default Option)
        4.Exit/Quit
        """)
        answer = input("What punishment would you like to invoke?\n")
        if answer == "1":
            cls()
            print("\nFully disable Internet Access..... HELL YES!!")
            er_disable_int_lara()
        elif answer == "2":
            cls()
            print("\nEnable Full Internet Access..... Yeah Whatever :-( ")
            er_enable_int_lara()
        elif answer == "3":
            cls()
            print("\nEnable Scheduled Internet Access..... Well, at least it's something :-) ")
            er_schedule_int_lara()
        elif answer == "4":
            cls()
            print("\nSo long and thanks for all the fish!!\n")
            break
        else:
            print("\nChoose one of the provided options, smartass!!")


menu()