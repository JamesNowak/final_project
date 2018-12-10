from tkinter import *
import tkinter.messagebox
import PIL.Image
import PIL.ImageTk
import pickle
import winsound


# main (root) GUI menu
class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        # create the label buttons
        im = PIL.Image.open("Darkest_Dungeon_Logo.png")
        photo = PIL.ImageTk.PhotoImage(im)

        ddl = Label(master, image=photo)
        ddl.image = photo
        # https://stackoverflow.com/questions/27599311/tkinter-photoimage-doesnt-not-support-png-image

        self.intro1 = tkinter.Label(self.top_frame, text='You are an exile, unwanted and alone. You have heard rumors about an nearly forgotten '
                                    'tomb filled with endless treasure and unknown horrors.')
        self.intro2 = tkinter.Label(self.top_frame, text='After months of searching you have finally found it. '
                                    'Do you dare enter?')
        # pack the intro
        ddl.pack()
        self.intro1.pack(side='top', anchor='n', padx=20)
        self.intro2.pack(side='top', anchor='n', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='Enter the dungeon', command=self.enter)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def enter(self):
        Outside(self.master)
        # this hides the main window


class Outside:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.window = tkinter.Toplevel(master)
        self.window.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.window, padx=10)
        self.bottom_frame = tkinter.Frame(self.window, padx=10)

        # widgets for top frame - label and entry box for name
        self.old_man1_label = tkinter.Label(self.top_frame, text='You aproach the ancient stone doors and notice an decrepit old man etching symbols into stone slabs.')
        self.old_man2_label = tkinter.Label(self.top_frame, text='Once you get close enough to the door his head snaps up in your direction. One of his eyes are covered in')
        self.old_man3_label = tkinter.Label(self.top_frame, text=' dirty bandages and his clothes look like tattered scribes robes.')
        self.old_man4_label = tkinter.Label(self.top_frame, text='')
        im = PIL.Image.open("old man.png")
        photo = PIL.ImageTk.PhotoImage(im)

        old_man_pic = Label(self.top_frame, image=photo)
        old_man_pic.image = photo

        self.old_man5_label = tkinter.Label(self.top_frame, text='Old man: Ahhh another victim of this tomb of eldritch horrors searching for the treasures so many others')
        self.old_man6_label = tkinter.Label(self.top_frame, text='have sought and died for. well if you must go in can I ask to know a little about you? I make sure no ')
        self.old_man7_label = tkinter.Label(self.top_frame, text='poor soul is forgotten when they enter and die in this foul place. So tell me about yourself.')

        # pack top frame

        self.old_man1_label.pack(side='top', anchor='w')
        self.old_man2_label.pack(side='top', anchor='w')
        self.old_man3_label.pack(side='top', anchor='w')
        self.old_man4_label.pack(side='top', anchor='w')
        old_man_pic.pack()
        self.old_man5_label.pack(side='top', anchor='w')
        self.old_man6_label.pack(side='top', anchor='w')
        self.old_man7_label.pack(side='top', anchor='w')

        # buttons for bottom frame
        self.con_button = tkinter.Button(self.bottom_frame, text='Continue', command=self.cont)

        # pack bottom frame
        self.con_button.pack(anchor='n')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def cont(self):
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        Questions(master=self.window)


class Questions:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.ques = master
        self.ques.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.ques, padx=40)
        self.bottom_frame = tkinter.Frame(self.ques, padx=40)

        self.radio_var1 = tkinter.IntVar()
        self.radio_var1.set(1)
        self.radio_var2 = tkinter.IntVar()
        self.radio_var2.set(1)

        # widgets for top frame - label and entry box for name
        self.quest_1_label = tkinter.Label(self.top_frame, text='What is your name?')
        self.quest_1_entry = tkinter.Entry(self.top_frame, width=20)
        self.quest_2_label = tkinter.Label(self.top_frame, text='What are you?')
        self.quest_2_button1 = tkinter.Radiobutton(self.top_frame, text='Man',
                                                   variable=self.radio_var1, value=1)
        self.quest_2_button2 = tkinter.Radiobutton(self.top_frame, text='Woman',
                                                   variable=self.radio_var1, value=2)
        self.quest_3_label = tkinter.Label(self.top_frame, text='What weapon do you use?')
        self.quest_3_button1 = tkinter.Radiobutton(self.top_frame, text='Sword and Shield',
                                                   variable=self.radio_var2, value=1)
        self.quest_3_button2 = tkinter.Radiobutton(self.top_frame, text='Dagger and Bow',
                                                   variable=self.radio_var2, value=2)
        # pack top frame
        self.quest_1_label.pack(side='top', anchor='n', padx=20)
        self.quest_1_entry.pack(side='top', anchor='n', padx=20)
        self.quest_2_label.pack(side='top', anchor='n', padx=20)
        self.quest_2_button1.pack(side='top', anchor='n', padx=20)
        self.quest_2_button2.pack(side='top', anchor='n', padx=20)
        self.quest_3_label.pack(side='top', anchor='n', padx=20)
        self.quest_3_button1.pack(side='top', anchor='n', padx=20)
        self.quest_3_button2.pack(side='top', anchor='n', padx=20)

        # buttons for bottom frame
        self.con_button = tkinter.Button(self.bottom_frame, text='continue', command=self.con)
        # pack bottom frame
        self.con_button.pack(side='top')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.sex = 0
        self.weapon = 0

    def con(self):
        if self.radio_var1.get() == 1:
            self.sex = 1
        else:
            self.sex = 2
        if self.radio_var2.get() == 1:
            self.weapon = 1
        else:
            self.weapon = 2
        character = {'name': self.quest_1_entry.get(), 'sex': self.sex}
        weapon = {'weapon_combo': self.weapon}
        with open('character.txt', 'wb') as char:
            pickle.dump(character, char)
        with open('weapon.txt', 'wb') as weap:
            pickle.dump(weapon, weap)
            # https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        Answers(master=self.ques)


class Answers:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.ans = master
        self.ans.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.ans)
        self.bottom_frame = tkinter.Frame(self.ans)

        with open("character.txt", "rb") as char:
            self.char = pickle.load(char)
        with open("weapon.txt", "rb") as weap:
            self.weap = pickle.load(weap)
            # https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file

        # widgets for top frame -
        if self.char['sex'] == 1:
            im = PIL.Image.open("male character.png")
            photo = PIL.ImageTk.PhotoImage(im)

            main_character_pic = Label(self.top_frame, image=photo)
            main_character_pic.image = photo

        else:
            im = PIL.Image.open("female character.png")
            photo = PIL.ImageTk.PhotoImage(im)

            main_character_pic = Label(self.top_frame, image=photo)
            main_character_pic.image = photo
        if self.weap['weapon_combo'] == 1:
            self.weap['weapon_combo'] = 'Sword and Shield'
        else:
            self.weap['weapon_combo'] = 'Dagger and Bow'
        self.name = tkinter.Label(self.top_frame, text='My name is ' + self.char['name'] + '.')
        self.weapon = tkinter.Label(self.top_frame, text='I use a ' + self.weap['weapon_combo'] + '.')

        # pack top frame
        main_character_pic.pack(side='top', anchor='n')
        self.name.pack(side='top', anchor='n')
        self.weapon.pack(side='top', anchor='n')
        # buttons for bottom frame
        self.con_button = tkinter.Button(self.bottom_frame, text='continue', command=self.con)

        # pack bottom frame
        self.con_button.pack(side='top')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def con(self):

        self.top_frame.destroy()
        self.bottom_frame.destroy()
        Response(master=self.ans)


class Response:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.res = master
        self.res.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.res)
        self.bottom_frame = tkinter.Frame(self.res)

        # widgets for top frame
        with open("character.txt", "rb") as myFile:
            self.char = pickle.load(myFile)

        im = PIL.Image.open("old man.png")
        photo = PIL.ImageTk.PhotoImage(im)

        old_man_pic = Label(self.top_frame, image=photo)
        old_man_pic.image = photo

        self.old_man_label_1 = tkinter.Label(self.top_frame, text='Very well, I hope you have a more prosperous '
                                             'delve into this tomb them the others before you ' + self.char['name'] + '.')
        self.old_man_label_2 = tkinter.Label(self.top_frame, text='May the gods have mercy on your soul.')
        # pack top frame
        old_man_pic.pack(side='top', anchor='n')
        self.old_man_label_1.pack(side='top', anchor='w')
        self.old_man_label_2.pack(side='top', anchor='n')
        # buttons for bottom frame
        self.con_button = tkinter.Button(self.bottom_frame, text='continue', command=self.con)

        # pack bottom frame
        self.con_button.pack(side='top')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def con(self):
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        Door(master=self.res)


class Door:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.door = master
        self.door.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.door)
        self.bottom_frame = tkinter.Frame(self.door)

        # widgets for top frame
        self.door_1 = tkinter.Label(self.top_frame, text='You turn away from the old man without another word')
        self.door_2 = tkinter.Label(self.top_frame, text='and stare at the ancient door thatstands before you.')
        self.door_3 = tkinter.Label(self.top_frame, text='You know damn well that you could never come back out,')
        self.door_4 = tkinter.Label(self.top_frame, text='but the tresure promised is to tempting and your greed')
        self.door_5 = tkinter.Label(self.top_frame, text='begins to grow as you put your hands on the door.')
        im = PIL.Image.open("download.png")
        photo = PIL.ImageTk.PhotoImage(im)

        door = Label(self.top_frame, image=photo)
        door.image = photo  # keep a reference!

        # pack top frame
        door.pack()
        self.door_1.pack(side='top', anchor='w')
        self.door_2.pack(side='top', anchor='w')
        self.door_3.pack(side='top', anchor='w')
        self.door_4.pack(side='top', anchor='w')
        self.door_5.pack(side='top', anchor='w')

        # buttons for bottom frame
        self.con_button = tkinter.Button(self.bottom_frame, text='open the door', command=self.con)

        # pack bottom frame
        self.con_button.pack(side='top')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def con(self):
        winsound.PlaySound('door sound.wav', winsound.SND_FILENAME)
        # https://stackoverflow.com/questions/307305/play-a-sound-with-python
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        End(master=self.door)


class End:
    def __init__(self, master):

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.end = master
        self.end.title('Outside the dungeon...')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.end)
        self.bottom_frame = tkinter.Frame(self.end)

        # widgets for top frame
        self.end1 = tkinter.Label(self.top_frame, text='And this is the end of the demo!')
        self.end2 = tkinter.Label(self.top_frame, text='I hope you enjoyed! this was an experience')
        self.end3 = tkinter.Label(self.top_frame, text='to create, it was fun despite the ups and downs.')
        self.end4 = tkinter.Label(self.top_frame, text='And I truly thank you for the class.')

        # pack top frame
        self.end1.pack()
        self.end2.pack()
        self.end3.pack()
        self.end4.pack()
        # buttons for bottom frame
        self.end_button = tkinter.Button(self.bottom_frame, text='main menu', command=self.endit)

        # pack bottom frame
        self.end_button.pack(side='top')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def endit(self):
        self.end.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    MainMenu(root)

    # control the mainloop from main instead of the class
    root.mainloop()


main()
