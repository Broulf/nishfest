from datetime import datetime as dt
import obsws_python as obs
import time

# LIBRARY FOR OBS-WEBSOCKETS
def nishfunctions():
    cl = obs.ReqClient(host='127.0.0.1',
                   port=4455,
                   password='omXgda5Es0B1zVTK',
                   timeout=30)
    cl.set_scene_item_enabled('MAIN-SCENE', 3, True) # DELCAMBRE
    cl.set_scene_item_enabled('MAIN-SCENE', 4, True) # KAPLAN
    cl.set_scene_item_enabled('MAIN-SCENE', 5, True) # MORGAN-CITY
    cl.set_scene_item_enabled('MAIN-SCENE', 12, True) # BREAK
    cl.set_scene_item_enabled('MAIN-SCENE', 6, True) # ACADIANA
    cl.set_scene_item_enabled('MAIN-SCENE', 7, True) # ERATH
    cl.set_scene_item_enabled('MAIN-SCENE', 8, True) # NORTH-VERMILLION
    cl.set_scene_item_enabled('MAIN-SCENE', 9, True) # NISH
    cl.set_scene_item_enabled('MAIN-SCENE', 10, True) # AWARDS

def main():
    # LOGIN TO OBS-WEBSOCKETS
    cl = obs.ReqClient(host='127.0.0.1',
                   port=4455,
                   password='omXgda5Es0B1zVTK',
                   timeout=30)
    print("Connected succesfully...\n")
    
    # GET THE CURRENT DATE IN ISO FORMAT IN FOR LOOP, LOOPING EVERY MINUTE
    while True:
        # Get the current date and time
        current_datetime = dt.now()
        
        # Format and print the current date and time without seconds
        print("Current Time:")
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
        print(formatted_datetime)
        print()
        
        # If the current date and time is equal to the time of the event, enable the scene item, else disable it
        if formatted_datetime == "2023-10-14 14:00":
            cl.set_scene_item_enabled('MAIN-SCENE', 3, True)
            print("Enabled Delcambre")
        elif formatted_datetime == "2023-10-14 14:20":
            cl.set_scene_item_enabled('MAIN-SCENE', 4, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 3, False)
            print("Enabled Kaplan")
        elif formatted_datetime == "2023-10-14 14:40":
            cl.set_scene_item_enabled('MAIN-SCENE', 5, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 4, False)
            print("Enabled Morgan City")
        elif formatted_datetime == "2023-10-14 15:00":
            cl.set_scene_item_enabled('MAIN-SCENE', 12, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 5, False)
            print("Enabled Break")
        elif formatted_datetime == "2023-10-14 15:20":
            cl.set_scene_item_enabled('MAIN-SCENE', 6, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 12, False)
            print("Enabled Acadiana")
        elif formatted_datetime == "2023-10-14 15:40":
            cl.set_scene_item_enabled('MAIN-SCENE', 7, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 6, False)
            print("Enabled Erath")
        elif formatted_datetime == "2023-10-14 16:00":
            cl.set_scene_item_enabled('MAIN-SCENE', 8, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 7, False)
            print("Enabled North Vermillion")
        elif formatted_datetime == "2023-10-14 16:20":
            cl.set_scene_item_enabled('MAIN-SCENE', 9, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 8, False)
            print("Enabled NISH")
        elif formatted_datetime == "2023-10-14 16:40":
            cl.set_scene_item_enabled('MAIN-SCENE', 10, True)
            cl.set_scene_item_enabled('MAIN-SCENE', 9, False)
            print("Enabled Awards")

        # Sleep for 60 seconds
        time.sleep(60)

main()
