#import library
import tkinter as tk
from tkinter import messagebox,ttk
import time
import pygame
import sys

class Pomodoro_session:
    def __init__(self):
        self.root = tk.Tk()                                                 # create main window
        self.screen_width = self.root.winfo_screenwidth()                   # get the window screen width and height
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")     # set the window size to the screen size
        self.root.state('zoomed')                                           # maximizes/zoom the window
        self.root.configure(bg='#E0F2F1')                                   # set the background colour                                 
        self.root.title("Pomodoro timer")                                   # set the title of main window

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.root.protocol("WM_DELETE_WINDOW", self.exit)                   # set a protocol for the window manager when user try to close the window trigger the method   

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        pygame.mixer.init()                                                 # initializes the mixer module,prepare the mixer
        audio_file = 'focus_music.mp3'                                      # defines audio file path
        pygame.mixer.music.load(audio_file)                                 # load the audio file into the mixer for playback

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #act as a flag to check the conditon whether
        self.running=False              #timer is running
        self.reset=False                #timer got reset
        self.isbreaktime=False          #is break time 

        self.time_left=0                #initialize to zero
        self.session_count=0            #initialize to zero

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #create current session label
        self.current = tk.Label(self.root, text="Pomodoro session", font=("Helvetica", 40),bg="#E0F2F1",fg="#000000") 
        self.current.pack(pady=5)

        #create time label
        self.time_label = tk.Label(self.root, text="00:00", font=("Helvetica", 80),bg="#E0F2F1",fg="#000000")
        self.time_label.pack(pady=50)
        
        #create outer central frame
        maincentral_frame = tk.Frame(self.root,bg='#E0F2F1')
        maincentral_frame.pack(expand=True)

        #create inner frame 
        self.button_frame= tk.Frame(maincentral_frame,bg='#E0F2F1')
        self.button_frame.pack(pady=20)

        #create start button
        self.start_button = tk.Button(self.button_frame, text="Start",font=("Helvetica", 15), command=self.button_prompt_window,width=25, height=4,bg="#009688",fg="#FFFFFF")
        self.start_button.pack(side=tk.LEFT)

        #create resume button
        self.resume_button = tk.Button(self.button_frame, text="Resume", font=("Helvetica", 15),command=self.resume_timer,state="disabled",width=25, height=4,bg="#009688",fg="#FFFFFF")
        self.resume_button.pack(side=tk.LEFT,padx=10)

        #create pause button
        self.pause_button = tk.Button(self.button_frame, text="Pause",font=("Helvetica", 15), command=self.pause_timer,state="disabled",width=25, height=4,bg="#009688",fg="#FFFFFF")
        self.pause_button.pack(side=tk.LEFT,padx=10)

        #create reset button
        self.reset_button = tk.Button(self.button_frame, text="Reset", font=("Helvetica", 15),command=self.reset_timer,state="disabled",width=25, height=4,bg="#009688",fg="#FFFFFF")
        self.reset_button.pack(side=tk.LEFT,padx=10)

        #create skip button
        self.skip_button=tk.Button(self.button_frame,text="Skip",font=("Helvetica", 15),command=self.skip_break,width=25,height=4,bg="#009688",fg="#FFFFFF",state=tk.DISABLED)
        self.skip_button.pack(side=tk.LEFT,padx=10)

        #create inner frame
        self.history_frame = tk.Frame(maincentral_frame,bg='#E0F2F1')
        self.history_frame.pack(pady=20)

        #create history log button
        self.history_button=tk.Button(self.history_frame,text="History log",font=("Helvetica", 15),command=self.button_history_window,width=25,height=4,bg="#009688",fg="#FFFFFF")
        self.history_button.pack()

        #create inner frame
        self.music_frame = tk.Frame(maincentral_frame,bg='#E0F2F1')
        self.music_frame.pack(pady=20)

        #create focus music button
        self.music_button=tk.Button(self.music_frame,text="Focus music OFF",font=("Helvetica", 15),command=self.focus_music,width=25,height=4,bg="#009688",fg="#FFFFFF")
        self.music_button.pack()
        
        #create inner frame
        self.sessioncount_frame = tk.Frame(maincentral_frame,bg='#E0F2F1')
        self.sessioncount_frame.pack()

        #create session count label
        self.sessioncount_label = tk.Label(self.sessioncount_frame, text=f"Session count: {self.session_count}", font=("Times New Roman", 15),bg="#E0F2F1",fg="#000000")
        self.sessioncount_label.pack()
       
        self.root.mainloop()        #start event loop

        self.button_prompt_window() #call prompt window

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def exit(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):  # Show a confirmation messagebox
            self.root.destroy()                                            # Close main window
            pygame.mixer.quit()                                            # Quit the pygame mixer
            sys.exit()                                                     # Exit the program
        else:
            pass                                                           # Do nothing if the user cancels the quit action

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def button_prompt_window(self):
        self.prompt_window=tk.Toplevel(self.root)                                   # create a top level window
        self.prompt_window.geometry(f"{self.screen_width}x{self.screen_height}")    # set the window size to the screen size
        self.prompt_window.state('zoomed')                                          # maximizes/zoom the window
        self.prompt_window.configure(bg='#E0F2F1')                                  # set the background colour 
        self.prompt_window.title("Pomodoro timer")                                  # set the title of main window
        self.prompt_window.focus_force()                                            # bring window to the front and foucs forces to this window
        
        #create outer central frame
        central_frame = tk.Frame(self.prompt_window,bg='#E0F2F1')
        central_frame.pack(expand=True)

        #create inner frame
        self.session_Min_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.session_Min_frame.pack()

        #create prompt session in minutes label
        label = tk.Label(self.session_Min_frame, text="Please enter the study session in minutes:",font=("Helvetica", 30),width=35, height=2,bg="#E0F2F1",fg="#000000")
        label.pack()

        #create inner frame
        self.session_Min_frame2 = tk.Frame(central_frame,bg='#E0F2F1')
        self.session_Min_frame2.pack()

        #create entry for session in minutes   
        self.entry = tk.Entry(self.session_Min_frame2,font=("Helvetica", 25),width=40) 
        self.entry.pack(side=tk.LEFT)

        #create inner frame
        self.session_Sec_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.session_Sec_frame.pack()

        #create prompt session in seconds label
        label_seconds= tk.Label(self.session_Sec_frame, text="Please enter the study session in seconds:",font=("Helvetica", 30),width=35, height=2,bg="#E0F2F1",fg="#000000")
        label_seconds.pack()

        #create inner frame
        self.session_Sec_frame2 = tk.Frame(central_frame,bg='#E0F2F1')
        self.session_Sec_frame2.pack()

        #create entry for session in seconds
        self.entry_seconds = tk.Entry(self.session_Sec_frame2,font=("Helvetica", 25),width=40) 
        self.entry_seconds.pack()

        #create inner frame
        self.break_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.break_frame.pack()

        #create prompt break session in minutes label
        label_breaktime = tk.Label(self.break_frame, text="Please enter the break time in minutes:",font=("Helvetica", 30),width=35, height=2,bg="#E0F2F1",fg="#000000")
        label_breaktime.pack()

        #create inner frame
        self.break_frame2 = tk.Frame(central_frame,bg='#E0F2F1')
        self.break_frame2.pack()

        #create entry for break time session in minutes
        self.entry_breaktime = tk.Entry(self.break_frame2,font=("Helvetica", 25),width=40) 
        self.entry_breaktime.pack(side=tk.LEFT,padx=10)

        #create inner frame
        self.break_Sec_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.break_Sec_frame.pack()

        #create prompt break session in seconds label
        label_break_seconds= tk.Label(self.break_Sec_frame, text="Please enter the break session in seconds:",font=("Helvetica", 30),width=35, height=2,bg="#E0F2F1",fg="#000000")
        label_break_seconds.pack()

        #create inner frame
        self.break_Sec_frame2 = tk.Frame(central_frame,bg='#E0F2F1')
        self.break_Sec_frame2.pack()

        #create entry for break sesion in seconds
        self.entry_break_seconds = tk.Entry(self.break_Sec_frame2,font=("Helvetica", 25),width=40) 
        self.entry_break_seconds.pack()

        #create inner frame
        self.okay_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.okay_frame.pack(pady=20)

        #create ok button
        ok_button = tk.Button(self.okay_frame, text="OK",font=("Helvetica", 13), command=self.validate_time_entry,width=30, height=4,bg="#009688",fg="#FFFFFF")
        ok_button.pack(side=tk.LEFT)

        #create default button
        default_button = tk.Button(self.okay_frame,text="Default Value",font=("Helvetica", 13),command=self.set_default_value,width=30, height=4,bg="#009688",fg="#FFFFFF")
        default_button.pack(side=tk.LEFT,padx=20)

        #create inner frame
        self.back_frame = tk.Frame(central_frame,bg='#E0F2F1')
        self.back_frame.pack()

        #create back button
        back_button=tk.Button(self.back_frame, text="Back",font=("Helvetica", 13), command=self.back_prompt_window,width=30, height=4,bg="#009688",fg="#FFFFFF")
        back_button.pack()

    def set_default_value(self):
        default_value = "25"                        # Initialize the default value to 25
        self.entry.delete(0, tk.END)                # Clear the entry field
        self.entry.insert(0, default_value)         # Insert the default value into entry field

        self.entry_seconds.delete(0,tk.END)         # Clear the entry field
        self.entry_seconds.insert(0,"0")            # Insert zero into the entry field
        
        self.entry_break_seconds.delete(0,tk.END)   
        self.entry_break_seconds.insert(0,"0")      
        
        default_breaktime_value = "5"                           # Initialize the default beaktime value to 5
        self.entry_breaktime.delete(0, tk.END)                  # Clear the entry field
        self.entry_breaktime.insert(0, default_breaktime_value) # Insert the default value

    def back_prompt_window(self):                       # back to previous window
        self.prompt_window.destroy()                    # destroy/close the window
        self.pause_button.config(state=tk.DISABLED)     # disable the pause button since timer didnt start
        self.resume_button.config(state=tk.DISABLED)    # disable the resume button
        self.reset_button.config(state=tk.DISABLED)     # disable the reset button

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def validate_time_entry(self):
        '''4 entry will be validate
            self.entry                 
            self.entry_seconds         
            self.entry_breaktime       
            self.entry_break_seconds'''   
        user_input = self.entry.get()                                   # Get user input from entry field
        try:
            self.minutes=int(user_input)                                # Convert user input to integer and store into self.minutes
            if self.minutes > 60:                                       # Check if time in minutes exceed 60 
                messagebox.showerror("Input Error", "Time must be less than 60 minutes.",parent=self.prompt_window)  # Show error message
                self.entry.delete(0, tk.END)                            # Clear the entry field
            else:
                user_input2 = self.entry_seconds.get()                  # Get user input from entry field
                try:
                    self.seconds=int(user_input2)                       # Convert user input to integer and store into self.seconds
                    if self.seconds>60:
                        messagebox.showerror("Input Error", "Time must be less than 60 seconds.",parent=self.prompt_window)  # Show error message
                        self.entry_seconds.delete(0,tk.END)
                    else:
                        if self.seconds<=4 and self.minutes<=0:             # Check if time in seconds are less than or equal to 4 and minutes are zero
                            messagebox.showerror("Input Error", "Time must be greater than 4 seconds.",parent=self.prompt_window)   # Show error message
                            self.entry.delete(0, tk.END)                    # Clear the first entry field
                            self.entry_seconds.delete(0, tk.END)            # Clear the second entry field
                        else:
                            user_input3=self.entry_breaktime.get()          # Get user input from entry field
                            try:
                                self.breakminutes=int(user_input3)          # Convert user input to integer and store into self.breakminutes
                                if self.breakminutes >60:                   # Check if break time in minues is exceed 60
                                    messagebox.showerror("Input Error", "Time must be less than 60 minutes.",parent=self.prompt_window) # Show error message
                                    self.entry_breaktime.delete(0,tk.END)   # Clear the entry field         
                                else:
                                    user_input4 = self.entry_break_seconds.get()        # Get user input from entry field
                                try:
                                    self.breakseconds=int(user_input4)                  # Convert user input to integer and store into self.breakseconds
                                    if self.breakseconds>60:
                                        messagebox.showerror("Input Error", "Time must be less than 60 seconds.",parent=self.prompt_window)  # Show error message
                                        self.entry_break_seconds.delete(0,tk.END)
                                    else:
                                        if self.breakseconds<=4 and self.breakminutes<=0:   # Check if time in seconds are less than or equal to 4 and minutes are zero
                                            messagebox.showerror("Input Error", "Time must be greater than 4 seconds.",parent=self.prompt_window)   # Show error message
                                            self.entry_breaktime.delete(0, tk.END)          # Clear the third entry field
                                            self.entry_break_seconds.delete(0, tk.END)      # Clear the fouth entry field
                                        else:
                                            self.close_prompt_window()                      # Proceed to another method if passed all validation check
                                except ValueError:                                      # Handle case where the input is not integer/number
                                    messagebox.showerror("Input Error", "Please enter only numbers.\nNo alphabet or decimal point number is allowed",parent=self.prompt_window)
                                    self.entry_break_seconds.delete(0, tk.END)          # Clear the entry field
                            except ValueError:
                                messagebox.showerror("Input Error", "Please enter only numbers.\nNo alphabet or decimal point number is allowed",parent=self.prompt_window)
                                self.entry_breaktime.delete(0, tk.END)                  # Clear the entry field
                                self.entry_break_seconds.delete(0, tk.END)              # Clear the entry field
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter only numbers.\nNo alphabet or decimal point number is allowed",parent=self.prompt_window)
                    self.entry_seconds.delete(0, tk.END)                            # Clear the entry field
                    self.entry_breaktime.delete(0, tk.END)                          # Clear the entry field
                    self.entry_break_seconds.delete(0, tk.END)                      # Clear the entry field
        except ValueError:
            messagebox.showerror("Input Error", "Please enter only numbers.\nNo alphabet or decimal point number is allowed",parent=self.prompt_window)
            self.entry.delete(0, tk.END)                                            # Clear the entry field
            self.entry_seconds.delete(0, tk.END)                                    # Clear the entry field
            self.entry_breaktime.delete(0, tk.END)                                  # Clear the entry field
            self.entry_break_seconds.delete(0, tk.END)                              # Clear the entry field

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def close_prompt_window(self):
        self.minutes *= 60                                         # covert session in minutes to seconds 
        self.time_left=self.minutes+self.seconds                   # calculate session time left in seconds
        
        self.breakminutes *=60                                     # covert break time in minutes to seconds 
        self.break_duration=self.breakminutes+self.breakseconds    # calculate break time duration in seconds
        
        self.prompt_window.destroy()                               # destroy/close the window
        self.start_button.config(text="New duration")              # Update start button text
        self.pause_button.config(state=tk.NORMAL)                  # Enable pause button
        self.start_button.config(state=tk.DISABLED)                # Disable start button
        self.resume_button.config(state=tk.DISABLED)               # disable resume button
        self.reset_button.config(state=tk.NORMAL)                  # Enable reset button
        self.history_button.config(state=tk.DISABLED)              # Disable history log button

        self.running=True                                          #set the running flag to true
        self.update_timer()                                        #Call methods

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_timer(self):     
        while self.running and self.time_left > 0:  #whlle timer is running and time left is more than zero
            time.sleep(1)                           #pause execution for 1 seconds
            self.time_left -= 1                     #decrease the time left by zero
            self.update_label()                     #call methods to update label
        else:
            self.check_timeleft_zero()              #call methods if timer is not running and time left is equal or less tha zero

    def update_label(self):
        minutes = int(self.time_left //60)                          #Calculate minutes 
        seconds = int(self.time_left %60)                           #Calculate seconds
        self.time_label.config(text=f"{minutes:02d}:{seconds:02d}") #Update time label 
        self.root.update()                                          #update the gui,redraw window,and ensure immediate feedbacak which avoid freezing

    def check_timeleft_zero(self):
        if self.time_left <=0:                       #if time left is equal to zerp
            if self.reset or not self.running:       #check if reset flag is true or timer is not running
                self.update_label()                  #call methods to update label 
                self.reset=False                     #set reset flag to false after done 
            elif self.reset==False and self.running: #else check reset flag is not false and timer is runnig
                self.session_complete()              #call methods session completed

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def session_complete(self):
        if self.isbreaktime==False:                                                     #Check if it is not break time
            self.session_count += 1                                                     #increase one to session count
            self.sessioncount_label.config(text=f"Session count: {self.session_count}") #update session counter label

            with open("pomodoro_sessions.txt", "a+") as file:                               #Open file and append the data
                current_time = time.localtime()                                             #Get current local time
                formatted_time = time.strftime("%a | %d %b %Y | %H:%M:%S", current_time)    #Format time 

                file.write(f"Session: {self.session_count}\n")                          #Write data into file
                file.write(f"Day: {formatted_time.split('|')[0].strip()}\n")            #use separator to split up data according to category
                file.write(f"Date: {formatted_time.split('|')[1].strip().upper()}\n")
                file.write(f"Time: {formatted_time.split('|')[2].strip()}\n")
                file.write("\n")                                                        # Add a newline as sepearator between sessions

            messagebox.showinfo("Time's Up!", "Pomodoro session completed!")
            messagebox.showinfo("Break start!", "Break session started!")
            
            self.time_left=self.break_duration              #set break duration to time left

            self.isbreaktime=True                           #Set break time is True
            self.current.configure(text="Break Session")    #Update current session label
            self.reset_button.config(state=tk.DISABLED)     #Disable reset button
            self.skip_button.config(state=tk.NORMAL)        #Enable skip button

            self.update_timer()                             #call method to update timer
        else:
            messagebox.showinfo("Time's Up!", "Break session completed!")
            messagebox.showinfo("Session start!", "Pomodoro session started!")
            
            self.time_left=self.minutes+self.seconds           #Set stored minute and seconds to current time left 
            
            self.isbreaktime=False                             #Set break time is False
            self.current.configure(text="Pomodoro Session")    #Update current session label
            self.reset_button.config(state=tk.NORMAL)          #Enable reset button
            self.skip_button.config(state=tk.DISABLED)         #Disable skip button

            self.running=True
            self.update_timer()                    #call update timer

        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def pause_timer(self):  
        if self.isbreaktime == True:                        # Check if it is break time
            self.running = False                            # Stop the timer from running
            self.pause_button.config(state=tk.DISABLED)     # Disable the pause button
            self.start_button.config(state=tk.DISABLED)     # Disable the start button
            self.resume_button.config(state=tk.NORMAL)      # Enable the resume button
            self.reset_button.config(state=tk.DISABLED)     # Disable the reset button
        else:     # If it is not break time
            self.running = False                         # Stop the timer from running
            self.pause_button.config(state=tk.DISABLED)  # Disable the pause button
            self.start_button.config(state=tk.DISABLED)  # Disable the start button
            self.resume_button.config(state=tk.NORMAL)   # Enable the resume button
            self.reset_button.config(state=tk.NORMAL)    # Enable the reset button

    def resume_timer(self):  
        if self.isbreaktime == True:                        # Check if it is break time
            self.running = True                             # Continue the timer 
            self.resume_button.config(state=tk.DISABLED)    # Disable the resume button
            self.start_button.config(state=tk.DISABLED)     # Disable the start button
            self.pause_button.config(state=tk.NORMAL)       # Enable the pause button
            self.reset_button.config(state=tk.DISABLED)     # Disable the reset button
            self.update_timer()                             # Call the method to update timer 
        else:  # If it is not break time
            self.running = True                             # Continue the timer
            self.resume_button.config(state=tk.DISABLED)    # Disable the resume button
            self.start_button.config(state=tk.DISABLED)     # Disable the start button
            self.pause_button.config(state=tk.NORMAL)       # Enable the pause button
            self.reset_button.config(state=tk.NORMAL)       # Enable the reset button
            self.update_timer()                             # Call the method to update timer

    def reset_timer(self):  
        self.reset = True           # Set reset flag to True
        self.running = False        # Stop the timer from running
        self.time_left = 0          # Reset the time left to 0
        self.update_label()         # Call the method to update time label
        messagebox.showinfo("Reset timer", "The timer has been successfully reset!")  
        self.pause_button.config(state=tk.DISABLED)     # Disable the pause button
        self.resume_button.config(state=tk.DISABLED)    # Disable the resume button
        self.reset_button.config(state=tk.DISABLED)     # Disable the reset button
        self.start_button.config(state=tk.NORMAL)       # Enable the start button
        self.history_button.config(state=tk.NORMAL)     # Enable the history button

    def skip_break(self):           
        self.time_left = 0                          # Set the time left to 0
        self.skip_button.config(state=tk.DISABLED)  # Disable the skip button
        self.session_complete()                     # Skip to the session complete method

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def button_history_window(self):
        self.running=False                                                          #Stop the timer from running
        self.history_window=tk.Toplevel(self.root)                                  #Create a top level window
        self.history_window.geometry(f"{self.screen_width}x{self.screen_height}")   #Set window size to scren size
        self.history_window.state('zoomed')                                         #Maximizes/zoom the window
        self.history_window.configure(bg='#E0F2F1')                                 #Set background colour
        self.history_window.title("Pomodoro timer")                                 #Set window title
        self.history_window.focus_force()                                           #Bring window to the front and foucs forces to this window
 
        self.filename = 'pomodoro_sessions.txt'      #Define the file name
        self.data = self.read_data_from_file()       #Call method and save data into self.data

        self.tree = self.create_treeview()           #Call method and create a treeview

        #Create a delete Button
        self.delete_button=tk.Button(self.history_window, text="Delete",font=("Helvetica", 15), command=self.delete_history,width=20, height=2,bg="#009688",fg="#FFFFFF")
        self.delete_button.pack()

        #Creat a back button
        self.back_button=tk.Button(self.history_window, text="Back", font=("Helvetica", 15),command=self.close_history_window,width=20, height=2,bg="#009688",fg="#FFFFFF")
        self.back_button.pack(pady=10)

    def read_data_from_file(self):
        data = []                                   #Initialize a list to store session data
        with open(self.filename, 'r') as file:      #Open the file for reading
            session_data = {}                       #Intialize a dictionary to store session data
            
            for line in file:                           #For loop every line of the file
                line = line.strip()                     #Remove leading and trailling space
                if line:                                    #If the line is true(not empty)
                    key, value = line.split(': ', 1)        #Split the line on the first ': ', before : will be key and after : will be value
                    session_data[key] = value               #Store a key-value pair in a dictionary 
                else:                               #Else the line is empty
                    if 'Session' in session_data:   #Check if the session exits in session data
                        data.append({               #append a new dictionary into data
                            "Session": session_data['Session'], #retrieve value with key 'Session' from session data and append into new dictionary
                            "Day": session_data.get("Day"),     #retrive value with key 'Day' from session data 
                            "Date": session_data.get("Date"),   #retrive value with key 'Date' from session data 
                            "Time": session_data.get("Time")    #retrive value with key 'Time' from session data 
                        })
                    session_data = {}                 # Reset to empty for the next session
    
        return data

    def create_treeview(self):
        tree = ttk.Treeview(self.history_window, columns=("Session", "Day", "Date", "Time"), show='headings')#create the treeview
        
        # Define column headings
        tree.heading("Session", text="Session")
        tree.heading("Day", text="Day")
        tree.heading("Date", text="Date")
        tree.heading("Time", text="Time")

        # Set column widths
        tree.column("Session", width=100)
        tree.column("Day", width=100)
        tree.column("Date", width=150)
        tree.column("Time", width=100)

        # Insert data into the Treeview
        for entry in self.data:  # Iterate the data in dictionaries format
            tree.insert("", "end", values=(entry["Session"], entry["Day"], entry["Date"], entry["Time"]))   #insert data into treeview

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.history_window, orient="vertical", command=tree.yview)   #orient vertical which is scroll vertical,yview function is get the scroll position and uppdate it
        tree.configure(yscroll=scrollbar.set)       #scrollbar will update to the current scrolled position
        scrollbar.pack(side='right', fill='y')

        tree.pack(side='left', fill='both', expand=True)

        return tree
    
    def delete_history(self):
        selected_item = self.tree.selection()       #selected item from widget treeview will stored into selected item variable
        if not selected_item:                       #if no item selected
            messagebox.showwarning("Warning", "Please select a row to delete.", parent=self.history_window)
            return
        
        confirm_delete = messagebox.askyesno("Delete caution", "Are you really sure want to delete?", parent=self.history_window)
        if confirm_delete:
            for item in selected_item:
                session = self.tree.item(item, 'values')[0]  #Retrieve values with selected item,since first index is session number 
                
                # Find and remove the first occurrence of the entry from the list
                for i, entry in enumerate(self.data): 
                    if entry["Session"] == session:     #if the entry match the session identifier 
                        del self.data[i]                # Delete the first matching entry
                        break                           # Exit loop after delete one entry
                
                self.tree.delete(item)                  # Delete the item from the Treeview
                messagebox.showinfo("Success", "The record has been removed.", parent=self.history_window)
                break  
            
            # Write the updated data back to the file
            with open(self.filename, 'w') as file:
                for entry in self.data:                             
                    file.write(f"Session: {entry['Session']}\n") 
                    file.write(f"Day: {entry['Day']}\n")
                    file.write(f"Date: {entry['Date']}\n")
                    file.write(f"Time: {entry['Time']}\n")
                    file.write("\n")  

    def close_history_window(self):         
        self.pause_button.config(state=tk.DISABLED)     #Disable pause button
        self.resume_button.config(state=tk.DISABLED)    #Disable resume button
        self.history_window.destroy()                   #Destiry this window
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    def focus_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.music_button.config(text="Focus music OFF")
        else:
            pygame.mixer.music.play()
            self.music_button.config(text="Focus music ON")
            pygame.mixer.music.play(loops=-1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
app=Pomodoro_session()