final-unified.py
Long ago
Oct 13, 2017
C
Christopher Ng uploaded an item
Text
final-unified.py
import sys, time
import random
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup
import re

from collections import defaultdict

study_session_isRunning = False
reminder_queued = False  # Flag for presence of reminders
waiting_for_reminderText = False  # Flag to see if we're waiting for reminders
reminder_array = []  # expected format: [chat id, time to trigger, reminder text]


studyTime=0
totalStudyTime={}

module= defaultdict(dict)

init= 1
reply=0
 
def bot_pulse():
    """
    This function will be called everytime the bot refreshes
    itself. All logic which require checking time elapsed
    should be referenced via this function.
    """
    # START: Logic for reminder functionality
    global reminder_queued
    if study_session_isRunning:
        # check if time's up
        global session_end_time
        if (time.time() >= session_end_time):
            # time's up! do something
            end_study_session(False)
    if reminder_queued:
        # A reminder has been set. Check if it's due
        global reminder_array
        for i in range(len(reminder_array)):
            if (time.time() >= reminder_array[i][1]):
                trigger_reminder(i)


def initiate_study_session(chat_id, duration):
    # function to initiate study session proper
    global study_session_isRunning, session_end_time, session_requester
    session_end_time = time.time() + duration * 60
    session_requester = chat_id
    response = "Alright, I'll remind you in " + str(duration) + " minutes."
    bot.sendMessage(chat_id, response)
    study_session_isRunning = True


def end_study_session(is_cancelled):
    global study_session_isRunning, session_end_time, session_requester
    global studyTime, totalStudyTime
    
    study_session_isRunning = False
    session_end_time = 0
    if (is_cancelled):
        # cancelled by user
        bot.sendMessage(session_requester, "Session successfully cancelled.")
    else:
        # not cancelled by user
        bot.sendMessage(session_requester,
                        "Time's up! You studied for "+ str(studyTime) + " minutes! Take a well deserved break!")
        
    session_requester = 0
    
def reminder_heuristics(data_raw):
    """
    This function will process text from user input, and return
    a list with two values: three integers representing the timer
    duration in hours, minutes and seconds, and a string representing
    the reminder text. Input text should be restricted to the following
    format: <text> in <time>, and time should consist of integers.
    If an error is encountered, the function will return an empty list.
    """

    # split string to reminder text and timing fragments
    ds = data_raw.rsplit(" in ", 1)
    try:
        rf = ds[0]  # reminder text
        tf = ds[1]  # timing
    except IndexError:
        # string not properly formatted
        return []

    # clean reminder text fragment (ensure no trailing whitespace)
    rx = rf.rstrip()

    # extract fragments with timings
    sf = re.search(r'\d+\s?s', tf, re.I)
    mf = re.search(r'\d+\s?m', tf, re.I)
    hf = re.search(r'\d+\s?h', tf, re.I)

    # extract time from fragments
    tff_s = re.compile(r'\d+', re.I)
    st = tff_s.search(sf.group()) if sf is not None else None
    mt = tff_s.search(mf.group()) if mf is not None else None
    ht = tff_s.search(hf.group()) if hf is not None else None

    # format time nicely
    sx = int(st.group()) if st is not None else 0
    mx = int(mt.group()) if mt is not None else 0
    hx = int(ht.group()) if ht is not None else 0

    # check if time makes sense (all three calues being
    # 0 would imply that a formatting error has occurred)
    if (sx == 0 and mx == 0 and hx == 0):
        return []

    # return timer duration and reminder text
    return [sx, mx, hx, rx]

def set_reminder(chat_id, msg_text):
    global reminder_array, reminder_queued
    li = reminder_heuristics(msg_text)
    if li == []:
        # it seems parsing has failed. better let the user know
        bot.sendMessage(chat_id, "I'm sorry, I couldn't understand " +
                        "that. Please check the formatting of your " +
                        "reminder message!")
    else:
        # reminder array is expected to be in the form
        # [chat id, time to trigger, reminder text]
        lx = [chat_id, time.time() + li[0] + li[1] * 60 + li[2] * 3600, li[3]]
        reminder_array.append(lx)
        reminder_queued = True
        response = "Alright! I'll remind you to " + li[3] + " in: " + \
            str(li[2]) + " hours, " + str(li[1]) + " minutes and " + \
            str(li[0]) + " seconds."
        bot.sendMessage(chat_id, response)


def trigger_reminder(reminder_ref):
    """
    This function will send the reminder message to the user when called.
    It takes in an integer reminder_ref, which should point to the index
    number of the reminder that is due (as stored in reminder_array).
    """
    global reminder_array
    lx = reminder_array.pop(reminder_ref)
    response = "Hi! This is a reminder for you to " + lx[2] + "!"
    bot.sendMessage(lx[0], response)
    remaining_reminders()
	
	
def remaining_reminders():
    """
    This function checks if there are any reminders still pending.
    If there are no more, it unsets the reminder_queued flag.
    Otherwise, it does nothing. Should be called whenever reminders
    are removed.
    """
    global reminder_array, reminder_queued
    if (len(reminder_array) == 0):
        # no reminders left! unset the flag
        reminder_queued = False


def studyModule(from_id):

    
        
    response = 'Select the module you want to do: '

    foo_list = []
    for i in (module[from_id].keys()):
        foo_list.append([InlineKeyboardButton(
            text=str(i), callback_data=str(i))])

    muh_buttons = InlineKeyboardMarkup(inline_keyboard=foo_list)

    # send response with keyboard
    
    bot.sendMessage(from_id, response,
                    reply_markup=muh_buttons)
    # terminate early to avoid sending message twice
    return

	
def main(msg):

    global module, reply, record, totalStudyTime, init
    content_type, chat_type, chat_id= telepot.glance(msg)
    
    if content_type == "text":
        msg_text = msg["text"]
        global waiting_for_reminderText

        if (msg_text.startswith("/")):
            
            command = msg_text[1:].lower()
            global study_session_isRunning

            if(command=='add'):
                
                response= "Enter new module: "
                reply= 1
                

            elif(command=="show"):

                for key in (module[chat_id].keys()):
                            
                    bot.sendMessage(chat_id,str(key))

                return


            elif (command == 'weekend' ):

                response = 'When does your week begin ?: '
                bot.sendMessage(chat_id, response, reply_markup=
                                InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text='Monday', callback_data='Mon')],
                                [InlineKeyboardButton(text='Tuesday', callback_data='Tues')],
                                [InlineKeyboardButton(text='Wednesday', callback_data='Wed')],
                                [InlineKeyboardButton(text='Thursday', callback_data='Thurs')],
                                [InlineKeyboardButton(text='Friday', callback_data='Fri')],
                                [InlineKeyboardButton(text='Saturday', callback_data='Sat')],
                                [InlineKeyboardButton(text='Sunday', callback_data='Sun')]

                                ]))
                return

            elif (command == "study"):

                if(init==1):
                    totalStudyTime[chat_id]=0
                    init=0
                
                if (study_session_isRunning):
                    # session currently running, do not start another
                    response = "A study session is currently in progress!" + \
                        " To cancel the current session and start a " + \
                        "new one, first send /stop"
                else:
                    # initialise new study session
                    # prepare duration options
                    duration_keyboard = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(
                            text='15 min', callback_data='study-15')],
                        [InlineKeyboardButton(
                            text='30 min', callback_data='study-30')],
                        [InlineKeyboardButton(
                            text='45 min', callback_data='study-45')],
                        [InlineKeyboardButton(
                            text='60 min', callback_data='study-60')],
                    ])

                    # send response with keyboard
                    response = "How long would you like this session to be?"
                    bot.sendMessage(chat_id, response,
                                    reply_markup=duration_keyboard)
                    # terminate early to avoid sending message twice
                    return
            elif (command=='tips'):
                a="""Set up your study space - Your study space should be quiet,
                    comfortable and distraction-free.
                    """
                b="""Find your best time - Some people work better in the morning.
                    Others work better at night."""
                c="""Make to-do lists - Lists break tasks down into manageable chunks."""
                d="""Set time limits - Before you start your study session, have a
                    look at your to-do list and give yourself a set time."""
                e="""Quiz yourself - Get a friend or family member to quiz you on
                    key concepts. Offer to help your friends with their work too.
                    Quizzes are great ways to get confident about
                    what you know and find out what you still need to learn."""
                f="""It's important to take breaks while you're studying, especially
                    if you're feeling tired or frustrated."""
                g="""When you're studying it helps to keep in mind your reasons
                    for doing all this hard work."""
                h="""Talk to your teachers or lecturers about the things you don't understand."""




                tips=[a,b,c,d,e,f,g,h]
                bot.sendMessage(chat_id=chat_id, text=random.choice(tips))
                

               
                

            elif (command == "stop"):
                if (study_session_isRunning):
                    end_study_session(True)
                    # message not being sent here, terminate
                    return
                else:
                    response = "No study session in progress! To start" + \
                        " a new session, send /study"
            elif (command == "remind"):
                waiting_for_reminderText = True
                response = "Sure thing! What would you like to be reminded" + \
                    " of? Please enter in the format: <text> in <time> " + \
                    "(eg. grab lunch in 30 min), or enter nevermind to cancel."
                

            elif(command=="clearmod"):

                for i in (module[chat_id].keys()):
                    module[chat_id][i]=0


                totalStudyTime[chat_id]=0
                
                module[chat_id].clear()

                return
            elif(command=="clearall"):

                for i in (module[chat_id].keys()):
                    module[chat_id][i]= int(0)


                totalStudyTime[chat_id]= int(0)

                return
      
            elif (command =="report"):
                for i in (module[chat_id].keys()):

                    if( int(module[chat_id][i]) >= 60):

                        
                        mins=  (int( module[chat_id][i] )%60)
                        hours= int(int( totalmins - (int( module[chat_id][i] )%60))/60)
                        

                        bot.sendMessage(chat_id, str(i) + ": " + str(hours) + " hours and " + str( mins )+ " minutes." )

                    else:                        

                        bot.sendMessage(chat_id, str(i) + ": " +str( module[chat_id][i] )+ " minutes.")

                if( int(totalStudyTime[chat_id]) >= 60):

                    mins=  (int( totalStudyTime[chat_id] )%60)
                    hours= int(int( totalStudyTime[chat_id] - mins)/60)
                        

                    bot.sendMessage(chat_id, "Total study time thus far is "+ str(hours) + " hours and " + str( mins )+ " minutes." )

                else:                        

                    bot.sendMessage(chat_id, "Total study time thus far is "+ str(totalStudyTime[chat_id]) +" minutes.")

                
                    
                return
        elif (waiting_for_reminderText):
            # catch and process reminder information
            waiting_for_reminderText = False
            if (msg_text.lower() == "nevermind"):
                response = "Okay, no problem!"
            else:
                set_reminder(chat_id, msg_text)
                # no text to send here, returning early
                return
        
        elif(reply== 1):




            module[(chat_id)][(msg_text)]=int(0)
            
            
            reply=0
            response="Got it!"

            return

        else:

            bot.sendMessage(chat_id, "Invalid. Please enter a valid command or input")
            return


    bot.sendMessage(chat_id, response)

	
def on_callback_query(msg):

    global studyTime, totalStudyTime,currentModule
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    # close inline keyboard
    inline_message_id = msg['message']['chat']['id'], msg['message']['message_id']
    bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)

    # process query data



    if (query_data == 'study-15'):

        initiate_study_session(from_id, 15)       
        studyModule(from_id)

        response="Study for 15 mins"
        

        studyTime= studyTime+15
        totalStudyTime[from_id] = totalStudyTime[from_id] + 15

    elif (query_data == 'study-30'):
        
        initiate_study_session(from_id, 30)
        studyModule(from_id)
        
        response="Study for 30 mins"

        studyTime= studyTime+30
        totalStudyTime[from_id] = totalStudyTime[from_id] + 30
        
    elif (query_data == 'study-45'):
        
        initiate_study_session(from_id, 45)
        studyModule(from_id)
        
        response="Study for 45 mins"

        studyTime= studyTime+45
        totalStudyTime[from_id] = totalStudyTime[from_id] + 45
        
    elif (query_data == 'study-60'):
        
        initiate_study_session(from_id, 60)
        studyModule(from_id)
        
        response="Study for 60 mins"
        

        studyTime= studyTime+60
        totalStudyTime[from_id] = totalStudyTime[from_id] + 60

    else:
        
        module[from_id][query_data]= module[from_id][query_data]+ studyTime
        
        response= str(query_data)+ " selected."

        



    bot.sendMessage(from_id, response) 
    bot.answerCallbackQuery(query_id)

    return
    
    

    
TOKEN = ''
bot = telepot.Bot(TOKEN)

MessageLoop(bot,{'chat': main, 'callback_query': on_callback_query}).run_as_thread()
print("listening")

while 1:
    time.sleep(10)
    bot_pulse()