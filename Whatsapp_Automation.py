from pywinauto.application import Application
import time
import os

def WhatsAppBot(name, message, image_path):
    def startWhatsApp():
        os.system('start WhatsApp:')

    def connectApp():
        try:
            app = Application(backend="uia").connect(title="WhatsApp", timeout=5)
            print('Connected to WhatsApp')
            core_window = app.top_window()
            return core_window
        except Exception as e:
            print('Error: Unable to connect to WhatsApp')
            print(str(e))
            closeWhatsApp()
            quit()

    def pressButton(core_window, class_name= False, title= False, control_type= False, automation_id = False, error_text = 'button'):

        kwargs = {}
        if class_name != False:
            kwargs['class_name'] = class_name
        if title != False:
            kwargs['title'] = title
        if control_type != False:
            kwargs['control_type'] = control_type

        try:
            presses = core_window.descendants(**kwargs)
            if presses:
                if automation_id != False:
                    for press in presses:
                        if press.automation_id() == automation_id:
                            press.invoke()
                            return
                    print(f"{automation_id} not found")
                    raise Exception(f'automation_id {automation_id} not found')
                else:
                    presses[0].invoke()
                    return
            else:
                print(f"{error_text} not found.")
                quit()
        except Exception as e:
            print(f'Error: Unable to add {error_text}')
            print(str(e))
            closeWhatsApp()
            quit()

    def enterText(core_window, class_name= False, title= False, control_type= False, text = 'Hello', additional_movement = ['{DOWN}', '{ENTER}'], error_text = 'keyBox'):

        kwargs = {}
        if class_name != False:
            kwargs['class_name'] = class_name
        if title != False:
            kwargs['title'] = title
        if control_type != False:
            kwargs['control_type'] = control_type

        final_text = str()
        for char in text:
            if char == ' ': final_text += '{SPACE}'
            else:           final_text += char

        file = core_window.descendants(**kwargs)
        if file: search = file[0]
        else:
            print(f"{error_text} not found.")
            quit()

        search.type_keys(final_text)

        for moevement in additional_movement:
            search.type_keys(moevement, pause=0.1)

    def closeWhatsApp():
        os.system('taskkill /im WhatsApp.exe /f')

    startWhatsApp()
    
    time.sleep(4)
    core_window = connectApp()
    
    time.sleep(1)
    enterText(core_window, class_name="TextBox", title="Search or start a new chat", text = name, additional_movement = ['{DOWN}', '{ENTER}'], error_text='Group - Allah Karim')
    
    time.sleep(1.5)
    pressButton(core_window, class_name="Button", title="Add attachment", error_text= 'Add Attachment Button')
    
    time.sleep(1.5)
    pressButton(core_window, class_name="MenuFlyoutItem", title="Photos & videos", error_text= 'Add Photo Button')
    
    time.sleep(2)
    enterText(core_window, title="File name:", text = image_path, error_text= ' File Address Box')
    
    time.sleep(2)
    pressButton(core_window, automation_id = "SubmitButton", error_text= 'Final Send Button')
    
    time.sleep(3)
    closeWhatsApp()

WhatsAppBot()