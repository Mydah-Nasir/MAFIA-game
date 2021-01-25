global list_role
list_role=['Mafia','Mafia','Mafia','Civilian','Civilian','Civilian','Civilian','Civilian'] #list of roles for players
global list_charcter
list_character=['baker','potter','housemaid','farmer','hair dresser','land lord','Sheriff','Hunter'] #list of characters for players

from tkinter import *
import time

#appearance
window=Tk()
window.title('Mafia')
window.geometry('500x750')
window.configure(background='#7c7c7c')

bg=PhotoImage(file='MAFIA.png') #background images
bg1=PhotoImage(file='wall.png')
bg2=PhotoImage(file='think.png')
bg3=PhotoImage(file='vote.png')
bg4=PhotoImage(file='sherrif.png')
global background
icon=PhotoImage(file='godfather.png') #icon

window.iconphoto(False,icon)

from pygame import mixer    #background music
mixer.init() 
mixer.music.load("Mafia Definitive Edition - Track 5 That Dont Square.mp3") 
mixer.music.set_volume(0.7) 
mixer.music.play(-1) 

#reset vote files everytime game is started
open('votes.txt','w').close()
open('votesm.txt','w').close()
#some variables used throughout
global playerdict
list_mafia,playerdict,count,count1,t,index,list,kit=[],{},1,0,5,0,[],0



#end game
def ended():
    '''Game end function with option of going back to start screen'''
    global announce
    announce.destroy()
    global ended1
    ended1=Label(window,text='Thank you for playing!',font=('Freestyle Script',30,'underline'),width=500,fg='#242424',bg='#9c9c9c',borderwidth=0)
    global goto
    goto=Button(window,width=500,text='Go to menu.',font=('Freestyle Script',25),fg='#242424',bg='#9c9c9c',borderwidth=0,command=startscreen)
    goto.pack(side=BOTTOM,expand=YES)
    ended1.pack(side=BOTTOM,expand=YES)

#check for game ending possibilities
def game_end():
    announce.pack(side=BOTTOM,expand=YES)
    '''conditions to decide winner of game'''
    listttt=[]
    for i in playerdict.values():
        listttt.append(i)
    mafia,civilian=listttt.count('Mafia'),listttt.count('Civilian')
    if mafia==civilian:
        announce.config(text='The Mafia have won the game!')
        announce.after(3000,ended)
    elif mafia==0:
        announce.config(text='The Civilians have won the game!')
        announce.after(3000,ended)
    else:
        con.place(x=0,y=500,height=70,width=500)


#votes by mafia
def nightresult():   
    def lol():
        con.config(text='Go to Village meeting. ▶',font=('Freestyle Script',40),command=discussiontime)
        if votedoutname1 in playerdict.keys():
            if playerdict[votedoutname1]=='Mafia':
                announce.config(text='Looks like those knuckleheads killed one\n of their own. REJOICE!')
                announce.after(5000,game_end)
            else:
                announce.config(text=f'{votedoutname1} was killed.\nSomeone needs to stop them! Oh lord.')
                announce.after(5000,game_end)
            del playerdict[votedoutname1]
        else:
            announce.config(text='They tried to kill a dead person. Amazing.')  #conditions for configuring story 
            announce.after(5000,game_end)
                    
    with open('votesm.txt','r')as file:
        votes=file.read()
        maxv=0
    for i in votes:
        count=votes.count(i)  #counting votes in text file for each character
        if count>maxv:
            votedout=i
            maxv=int(i)
      
    for player,value in playervalue:
        if int(votedout)==value:
            global votedoutname1
            votedoutname1=player        
    con.place_forget()
    announce.pack_forget()
    announce.config()
    announce.pack(side=BOTTOM,expand=YES)  #displaying who the majority mafia planned to kill
    announce.config(text=f'The Mafia raided the \nhouse of the {votedoutname} last night.')
    announce.after(5000,lol)
    open('votes.txt','w').close()
    open('votesm.txt','w').close()
global background4
background4=Label(window,image=bg4)    
#votes by civilians
def dayresult():
    global background4
    background4=Label(window,image=bg4)
    def drumrolls():
        if playerdict[votedoutname]=='Mafia':
            announce.config(text='Rejoice! You voted out a member of the infamous Mafia.',font=('Freestyle Script',25))
        else:
            announce.config(text='Unfortunate.The majority voted out an innocent.\n Tread carefully everyone! Mafia is still out there.',font=('Freestyle Script',25))
        del playerdict[votedoutname]
        game_end()

    background4.place(x=0,y=0,relwidth=1,relheight=1)
    voteend.destroy()
    results.destroy()
    with open('votes.txt','r')as file:
        votes=file.read()
        print (votes)
    maxv=0
    for i in votes:
        x=votes.count(i)
        if x>maxv:
            global votedout
            votedout=i
            maxv=int(i)
    for player,value in playervalue:

        if int(votedout)==value:
            global votedoutname
            votedoutname=player
    global announce
    announce=Label(window,width=500,text=f'The person voted out by Majority of \n the Village was the {votedoutname}',font=('Freestyle Script',30),fg='#242424',bg='#9c9c9c',borderwidth=0)
    announce.pack(side=BOTTOM,expand=YES)
    announce.after(3000,drumrolls)
    global con
    con=Button(window,text=f'''Continue''',font=('Freestyle Script',50),fg='#242424',bg='#9c9c9c',borderwidth=0,command=nightresult)



                       
    
#voting system       
def voting_system(dictionary):
    '''taking votes from user and giving the option to veiw results once voting is finished'''
    def next():
        '''ends voting when all the players are done'''
        try:
            R1.destroy()  #destroying all radio buttons once the user has selected one
            R2.destroy()
            R3.destroy()
            R4.destroy()
            R5.destroy()
            R6.destroy()
            R7.destroy()
            R8.destroy()
        except NameError:
            pass
        voting.destroy()
        with open('votes.txt','r')as file:
            c=file.read()
        with open('votesm.txt','r')as file:
            m=file.read()
        cnum,mnum=len(c),len(m)
        if (cnum+mnum)==players:
            global results
            results=Button(window,width=500,text='Results',font=('Freestyle Script',25),fg='#480048',bg='#7c7c7c',borderwidth=0,command=dayresult)
            results.pack(side=BOTTOM,expand=YES)
            global voteend
            voteend=Label(window,width=500,text=f'The Voting has ended.',font=('Freestyle Script',25),fg='#7c7c7c',bg='#480048' ,borderwidth=0)
            voteend.pack(side=BOTTOM,expand=YES)
        else:
            global index
            index+=1
            voting_system(dictionary)
            
    def vote(value):
        with open('votes.txt','a+')as file: #storing the votes in a file
            file.write(f'{value}')    
        voting.destroy()
        next()
            
    def votem(value):
        with open('votesm.txt','a+')as file:
            file.write(f'{value}')
        next()
    def proceed():
        buttonp.destroy()
        r=IntVar()
        r.set(-1)
        global R1, R2, R3, R4, R5, R6, R7, R8
        who=list[index]
        if dictionary[who]== 'Mafia':
            voting.config(text='Who do you plan on killing tonight?')  #radio buttons for mafia to kill
            voting.pack(side=TOP,expand=YES)
            try:
                R1=Radiobutton(window,text=list[0],variable=r,value=0,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                R2=Radiobutton(window,text=list[1],variable=r,value=1,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                R3=Radiobutton(window,text=list[2],variable=r,value=2,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                R1.pack(side=BOTTOM,expand=YES)
                R2.pack(side=BOTTOM,expand=YES)
                R3.pack(side=BOTTOM,expand=YES)
                R4=Radiobutton(window,text=list[3],variable=r,value=3,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                R4.pack(side=BOTTOM,expand=YES)
                if players==6:
                    R5=Radiobutton(window,text=list[4],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R5.pack(side=BOTTOM,expand=YES)
                    R6=Radiobutton(window,text=list[5],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R6.pack(side=BOTTOM,expand=YES)
                elif players==8:
                    R5=Radiobutton(window,text=list[4],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R5.pack(side=BOTTOM,expand=YES)
                    R6=Radiobutton(window,text=list[5],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R6.pack(side=BOTTOM,expand=YES)
                    R7=Radiobutton(window,text=list[6],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R7.pack(side=BOTTOM,expand=YES)
                    R8=Radiobutton(window,text=list[7],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: votem(r.get()))
                    R8.pack(side=BOTTOM,expand=YES)
            except IndexError:
                pass
        elif dictionary[who]== 'Civilian':
            voting.config(text='Vote for one the following people \n   who you are suspicious of:') #radio buttons for civilians to vote
            voting.pack(side=TOP,expand=YES)
            try:
                R1=Radiobutton(window,text=list[0],variable=r,value=0,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                R2=Radiobutton(window,text=list[1],variable=r,value=1,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                R3=Radiobutton(window,text=list[2],variable=r,value=2,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                R1.pack(side=BOTTOM,expand=YES)
                R2.pack(side=BOTTOM,expand=YES)
                R3.pack(side=BOTTOM,expand=YES)
                R4=Radiobutton(window,text=list[3],variable=r,value=3,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                R4.pack(side=BOTTOM,expand=YES)
                if players==6:
                    R5=Radiobutton(window,text=list[4],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R5.pack(side=BOTTOM,expand=YES)
                    R6=Radiobutton(window,text=list[5],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R6.pack(side=BOTTOM,expand=YES)
                elif players==8:
                    R5=Radiobutton(window,text=list[4],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R5.pack(side=BOTTOM,expand=YES)
                    R6=Radiobutton(window,text=list[5],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R6.pack(side=BOTTOM,expand=YES)
                    R7=Radiobutton(window,text=list[6],variable=r,value=4,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R7.pack(side=BOTTOM,expand=YES)
                    R8=Radiobutton(window,text=list[7],variable=r,value=5,bg='#7c7c7c',font=('Freestyle Script',25),fg='#480048',command=lambda: vote(r.get()))
                    R8.pack(side=BOTTOM,expand=YES)
            except IndexError:
                pass
                
    def poll():
          global voting
          voting=Label(window,text=f'Its time for {list[index]} to vote!, \nhand over the device to them.',font=('Freestyle Script',25),fg='black',bg='#7c7c7c',borderwidth=0)
          global buttonp
          buttonp=Button(window,text='Proceed.',font=('Freestyle Script',25),fg='#480048',bg='#7c7c7c',borderwidth=0,command=proceed)
          buttonp.pack(side=BOTTOM,expand=YES)
          voting.pack(side=TOP,expand=YES)
    def startpressed():
        Startvote.destroy()
        poll()

    
    countlabel.destroy()    
    global playervalue
    playervalue=[]
    list=[]
    abc=playerdict.keys()
    players=len(abc)
    for i in abc:
        list.append(i)
    j=0
    for i in list:
        playervalue.append((i,j))
        j+=1
    background3=Label(window,image=bg3)
    background3.place(x=0,y=0,relwidth=1,relheight=1)
    global kit
    if kit==0:
        global index
        index=0
        Startvote=Button(window,bg='#7c7c7c',text='START VOTING',fg='#480048',font=('Freestyle Script',60),borderwidth=0,command=startpressed)
        Startvote.pack(side=BOTTOM,expand=YES) #giving option to player to proceed voting
        kit+=1
    else:
        Startvote=Button(window,bg='#7c7c7c',text='Continue to the \nnext player.',fg='#480048',font=('Freestyle Script',60),borderwidth=0,command=startpressed)
        Startvote.pack(side=BOTTOM,expand=YES)
        
    
def discussiontime():
    '''to give time to users for discussion '''
    global t1
    t1=t
    global kit
    kit=0
    def update():
        countdown.destroy()
        counter()
    def counter():
        global t1
        if t1>0:
            countlabel.config(text=f'{t1} s')
            t1=t1-1
            countlabel.after(1000,counter)
        elif t1==0:
            countlabel.config(text='Discussion time has ended.',font=('Freestyle Script',50))
            countlabel.pack(side=BOTTOM,expand=YES)
            voting_system(playerdict)
    background2=Label(window,image=bg2)
    background2.place(x=0,y=0,relwidth=1,relheight=1)
    global countlabel
    countlabel=Label(window,bg='black',text='000 s',fg='white',font=('Freestyle Script',100,'bold','underline'),borderwidth=0)
    countlabel.place(x=0,y=580,width=500,height=120)
    countdown=Button(window,bg='black',text=f'''Start discussion''',fg='#480048',font=('Freestyle Script',22,'bold'),borderwidth=0,command=update)
    countdown.place(x=0,y=700,width=500)


#assignment of roles
def role_display():
    #storyline
    def narrator_intro5():
        narrator.pack_forget()
        narrator.config(text='Hence, the meetings commence.')
        narrator.pack(side=BOTTOM,expand=YES)
        skip.destroy()
        narrator.after(3000,end)
    def narrator_intro4():
        blood.destroy()
        narrator.config(text='The Council the town decide to hold one\n meeting per day to eliminate one person voted\n by majority onsuspicion of being one of the mafia.')
        narrator.after(7000,narrator_intro5)
    def narrator_intro3():
        global blood
        blood=Label(window,text='MAFIA',font=('Chiller',80,'underline'),width=500,height=300,fg='#990000',bg='#949494')
        narrator.pack_forget()
        narrator.config(text='It says in big bold letters')
        narrator.pack(side=BOTTOM,expand=YES)
        blood.pack(side=BOTTOM,expand=YES)
        narrator.after(5000,narrator_intro4)
    def narrator_intro2():
        narrator.config(text='A letter held by its cold hands.\n Seemingly written by blood. Oh lord!')
        narrator.after(5000,narrator_intro3) 
    def narrator_intro1():
        narrator.config(text='One unfortunate morning, the sun rises and in \nthe 4th sqaure of town lies a body!')
        narrator.after(5000,narrator_intro2)
    def narrator_intro():
        narrator.config(text='The worst crime to ever happen was someone’s \ncat got kidnapped. But...')
        narrator.after(5000,narrator_intro1)
    def narrator1():
        btn_4.destroy()
        lbl_1.destroy()
        global skip
        skip=Button(window,width=500,bg='#949494',text=f'''Skip Intro''',fg='#480048',font=('Freestyle Script',25),borderwidth=0,command=narrator_intro5)
        global narrator
        narrator=Label(window,text='A small town called Beacon Hills was known as\n one of the most normal towns to exist.',width=500,bg='#949494',fg='black',font=('Freestyle Script',30),borderwidth=0)
        skip.pack(side=BOTTOM,expand=YES)
        narrator.pack(side=BOTTOM,expand=YES)
        narrator.after(5000,narrator_intro)
    #storyline
    global background1
    background1=Label(window,image=bg1)
    background1.place(x=0,y=0,relwidth=1,relheight=1)
    global btn
    btn.destroy()
    global count,count1
    count1+=1
    count+=1
    import random
    if len(list_role)>0:
        #continue random role assigning to all characters
        role=random.choice(list_role)
        character=random.choice(list_character)
        list_role.remove(role)
        list_character.remove(character)
        d={character:role}
        playerdict.update(d)
        if role=='Mafia':
            global list_mafia
            if len(list_mafia)==0:
                lbl_1=Label(text=f'''ROLE : Mafia\nCHARACTER : {character}''',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',30),borderwidth=0)
            elif len(list_mafia)==1:
                lbl_1=Label(text=f'''ROLE : Mafia\nCHARACTER : {character}\n\nFELLOW MAFIA:-\n{list_mafia[0]}''',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',30),borderwidth=0)
            else:
                 lbl_1=Label(text=f'''ROLE : Mafia\nCHARACTER : {character}\n\nFELLOW MAFIA:-\n{list_mafia[0]}\n{list_mafia[1]}''',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',30),borderwidth=0)
            lbl_1.place(x=250,y=400,anchor='center')
            list_mafia.append(character)
        else:
            lbl_1=Label(text=f'''ROLE : Civilian\nCHARACTER : {character}''',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',30),borderwidth=0)
            lbl_1.place(x=250,y=400,anchor='center')
            
        def previous():
            lbl_1.destroy()  #destroying previous roles and character label and buttons
            btn_3.destroy()
            global btn
            btn=Button(window,width=500,bg='#7c7c7c',text=f'''Player {count}\nClick here to reveal role.''',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=role_display)
            btn.pack(side=BOTTOM,expand=YES)
        def end():
            narrator.destroy()
            btn_4.destroy()
            lbl_1.destroy()
            btn_2=Button(window,bg='#7c7c7c',text=f'''Proceed to discussion time.''',fg='#480048',font=('Freestyle Script',50),borderwidth=0,command=discussiontime)
            btn_2.place(x=250,width=500,y=350,anchor='center')
            
        btn_3=Button(window,bg='#7c7c7c',text=f'''▶''',fg='#480048',font=('Freestyle Script',50),borderwidth=0,command=previous)
        btn_3.place(x=470,y=400,anchor='center',height=50)
        if list_role==[]:
            btn.destroy()
            btn_3.destroy()
            btn_4=Button(window,width=500,bg='#565656',text=f'''FINISH''',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=narrator1)#end
            btn_4.place(x=250,y=700,anchor='center')
            
#start game
def start():
        edit_time.place_forget()
        button_start.destroy()
        global btn
        btn=Button(window,width=500,bg='#565656',text=f'''Player {count}\nClick here to reveal role.''',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=role_display)
        btn.pack(side=BOTTOM,expand=YES)


#selection of number of players       

def selection():
    rules_button.place_forget()
    global edit_time
    edit_time.place_forget()
    button_selection.place_forget()
    back_button.pack_forget()
    def player4():
        option.place_forget() 
        global button_start
        button_start=Button(window,width=500,bg='#565656',text='START THE GAME',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=start)
        button_start.pack(side=TOP,expand=YES)
        global list_role
        list_role=['Mafia','Civilian','Civilian','Civilian'] #roles and characters for four players
        global list_character
        list_character=['baker','potter','housemaid','farmer','hair dresser','land lord','Sheriff','Hunter']
        button_4.destroy()
        button_6.destroy()
        button_8.destroy()
        
    def player6():
        option.place_forget()
        global button_start
        button_start=Button(window,width=500,bg='#565656',text='START THE GAME',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=start)
        button_start.pack(side=TOP,expand=YES)
        global list_character
        list_character=['baker','potter','housemaid','farmer','hair dresser','land lord','Sheriff','Hunter']
        global list_role    #roles and characters for six players
        list_role=['Mafia','Mafia','Civilian','Civilian','Civilian','Civilian']
        button_4.destroy()
        button_6.destroy()
        button_8.destroy()

    def player8():
        option.place_forget()
        global button_start
        button_start=Button(window,width=500,bg='#565656',text='START THE GAME',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=start)
        button_start.pack(side=TOP,expand=YES)
        global list_character
        list_character=['baker','potter','housemaid','farmer','hair dresser','land lord','Sheriff','Hunter']
        global list_role   #roles and characters for eight players
        list_role=['Mafia','Mafia','Mafia','Civilian','Civilian','Civilian','Civilian','Civilian']
        button_4.destroy()
        button_6.destroy()
        button_8.destroy()
    

        
    global list_role
    list_role=['Mafia','Civilian','Civilian','Civilian']
    list_character=['baker','potter','farmer','land lord','Sheriff','Hunter']
    global button_4
    button_4=Button(window,width=500,bg='#565656',text='• 4 Players',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=player4)
    button_4.place(x=270,anchor='center',y=300,height=50)
 
    global button_6
    button_6=Button(window,width=500,bg='#565656',text='• 6 Players',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=player6)
    button_6.place(x=270,y=400,anchor='center',height=50)
    
    global button_8
    button_8=Button(window,width=500,bg='#565656',text='• 8 players',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=player8)
    button_8.place(x=270,y=500,anchor='center',height=50)
    #button_exit.destroy()


#rules
with open("Text for Project.txt", "r") as f:  
    label_story=Label(window,width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',29),borderwidth=0,text=f.read())
global rules
rules=Label(window,text='Rules',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)

def storyline_rules():
    '''displaying rules of games when rules button is clicked'''
    edit_time.place_forget()
    option.place_forget()   #removing previous options from the screen
    button_selection.place_forget()
    rules_button.place_forget()
    global label_story
    with open("Text for Project.txt", "r") as w:  
     label_story=Label(window,width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',29),borderwidth=0,text=w.read())
    global rules
    rules=Label(window,text='Rules',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
    rules.pack(side=TOP,expand=YES)
    label_story.pack(side=BOTTOM,expand=YES)


global time
time=Entry(window,bg='light grey',width=40)  #buttons and labels for edit time
global currenttime
currenttime=Label(window,text=f' Current time: {t}s',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
global enter
enter=Label(window,text='Enter Here:',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
global arrow
arrow=Button(window,text='→',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold'),borderwidth=0)
global number
number=Label(window,text='Enter a number please.',bg='#7c7c7c',fg='red',font=('Freestyle Script',25,'bold','underline'),borderwidth=0)

def editdiscussiontime():
    '''to edit discussion time and display the edited time'''
    def change():
        global t
        time=time.get()
        try:
            t=int(time)
            number.place_forget()
            currenttime.config(text=f' Current time: {t}s')
        except ValueError:
            number.place(x=500,width=500,y=700,height=50,anchor='ne')
            
           
    edit_time.place_forget()
    button_selection.place_forget()  #destroying all previous menu options
    rules_button.place_forget()
    option.place_forget()
    time.place(x=500,width=500,y=300,height=50,anchor='ne')
    enter.place(x=500,width=500,y=200,height=50,anchor='ne')
    arrow.place(x=500,width=500,y=400,height=50,anchor='ne')
    currenttime.place(x=500,width=500,y=500,height=50,anchor='ne')
    arrow.config(command=change)

def goback():
    '''giving the option to user to go back to the start screen'''
    number.place_forget()
    back_button.pack_forget()
    rules.pack_forget()      #removing all buttons when the go back button is clicked
    button_selection.place_forget()
    rules_button.place_forget()
    global label_story
    label_story.pack_forget()
    option.place_forget()
    time.place_forget()
    currenttime.place_forget()
    enter.place_forget()
    arrow.place_forget()
    edit_time.place_forget()
    startscreen()
    

def menu():
    '''options given when menu button is clicked'''
    global t
    t=5
    global time
    time=Entry(window,bg='light grey',width=40)  #buttons and labels for edit time
    global currenttime
    currenttime=Label(window,text=f' Current time: {t}s',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
    global enter
    enter=Label(window,text='Enter Here:',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
    global arrow
    arrow=Button(window,text='→',bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold'),borderwidth=0)
    global number
    number=Label(window,text='Enter a number please.',bg='#7c7c7c',fg='red',font=('Freestyle Script',25,'bold','underline'),borderwidth=0)

    global back_button
    back_button=Button(window,bg='#7c7c7c',text='◀',fg='#480048',font=('Freestyle Script',50),borderwidth=0,command=goback)
    background.place_forget()
    goto.pack_forget()
    global playerdict
    playerdict.clear()
    global list
    list.clear()
    global kit
    kit=0
    with open('votes.txt','w')as file:
            c=file.write('')
    with open('votesm.txt','w')as file:
            m=file.write('')
    global count
    count=1
    global count1
    count1=0
    global index
    index=0
    list_mafia.clear()
    ended1.pack_forget()
    background4.place_forget()
    button_menu.place_forget()
    button_exit.place_forget()
    with open("Text for Project.txt", "r") as w:  
     label_story=Label(window,width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',29),borderwidth=0,text=w.read())
    global rules
    rules=Label(window,text='Rules',width=500,bg='#7c7c7c',fg='#480048',font=('Freestyle Script',34,'bold','underline'),borderwidth=0)
    global option
    option=Label(window,bg='#7c7c7c',text='OPTIONS',fg='#480048',font=('Freestyle Script',50,'bold','underline'),borderwidth=0)
    global button_selection
    button_selection=Button(window,bg='#7c7c7c',text='START',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=selection)
    global rules_button
    rules_button=Button(window,bg='#7c7c7c',text='RULES',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=storyline_rules)
    global edit_time
    edit_time=Button(window,bg='#7c7c7c',text='EDIT DISCUSSION TIME',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=editdiscussiontime)
    edit_time.place(x=500,y=500,width=500,height=50,anchor='ne')
    button_selection.place(x=500,y=300,width=500,height=50,anchor='ne')
    rules_button.place(x=500,y=400,width=500,height=50,anchor='ne')
    back_button.pack(side=BOTTOM,anchor=SW)
    option.place(x=500,y=100,width=500,height=50,anchor='ne')
#exit
def exit1():
    window.destroy()
def startscreen():
    #menu
    global background
    background=Label(window,image=bg)
    background.place(x=0,y=0,relwidth=1,relheight=1)
    back_button.pack_forget()
    rules.pack_forget()
    button_selection.place_forget()
    rules_button.place_forget()
    global label_story
    label_story.pack_forget()
    option.place_forget()
    background.place(x=0,y=0,relwidth=1,relheight=1)
    global button_menu
    button_menu=Button(window,bg='#7c7c7c',text='Menu',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=menu)
    button_menu.place(x=500,y=450,width=500,height=50,anchor='ne')
    global button_exit    
    button_exit=Button(window,bg='#7c7c7c',text='Exit',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=exit1)
    button_exit.place(x=500,y=520,width=500,height=50,anchor='ne')
    
    
global goto
goto=Button(window,width=500,text='Go to menu.',font=('Freestyle Script',25),fg='#242424',bg='#9c9c9c',borderwidth=0,command=startscreen)
global ended1
ended1=Label(window,text='Thank you for playing!',font=('Freestyle Script',30,'underline'),width=500,fg='#242424',bg='#9c9c9c',borderwidth=0)  
#menu options
global option
option=Label(window,bg='#7c7c7c',text='OPTIONS',fg='#480048',font=('Freestyle Script',50,'bold','underline'),borderwidth=0)
global back_button
back_button=Button(window,bg='#7c7c7c',text='◀',fg='#480048',font=('Freestyle Script',50),borderwidth=0,command=goback)
global button_selection
button_selection=Button(window,bg='#7c7c7c',text='START',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=selection)
global rules_button
rules_button=Button(window,bg='#7c7c7c',text='RULES',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=storyline_rules)
global edit_time
edit_time=Button(window,bg='#7c7c7c',text='EDIT DISCUSSION TIME',fg='#480048',font=('Freestyle Script',30),borderwidth=0,command=editdiscussiontime)
#narrator


startscreen()

window.mainloop()
