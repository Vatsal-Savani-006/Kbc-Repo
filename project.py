from random import choice
from inputimeout import inputimeout 
import pyttsx3
engine = pyttsx3.init()
print("*************** KAUN BANEGA CROREPATI ***************")
engine.say("Welcome To Kon Baaneega Karodpati")
engine.runAndWait()
q1 = ['Which indian cricketers were banned after an interview in Koffee With Karan','How many cards are there in a deck','where is Taj Mahal located','From what integer does a whole number starts with','Which company does indian actor shahrukh khan own','Name the owner of the e-commerce company amazon','Who among the following is known as the iron man of India','Who among  the following was the first president of India','Who Defeated Alexander The Great','Which State is Known as Wheat Bowl Of India','Who Among The Following is Known As Master Blaster Of India','Who Was The First Matyr Of The Revolt Of 1857 For Freedom Of India','Which state is also known as the “Fruit Bowl” of India','Which of these scientists does not have a chemical element on the periodic table named after him']
o1 = ['a.Yuvraj Singh and Harbhajan Singh b.Shreyas Iyer and Ishan Kishan c.Hardik Pandya and KL Rahul d.Mayank Aggrawal and Sanju Samson','a.52 b.26 c.49 d.34','a.Rajasthan b.Hydrabad c.Aligadh d.Agra','a.1 b.2 c.0 d.-1','a.Ed-a-Mamma b.Red Chillies Entertainment c.HRX d.82°E','a.Elon Musk b.Jeff Bezoz c.Arnold Bernault d.Rakesh Jhunjhunwala','a.Narendra Modi b.APJ Abdul Kalam c.Chandrashekhar Aazad d.Sardar Vallabhbhai Patel','a.Rajendra Prasad b.Indira Gandhi c.Draupati Murmu d.Atal Bihari Vajpayee','a.Raj Raja Chola b.Chhatrapati Shivaji Maharaj c.Samrat Prithviraj Chauhan d.King Porus','a.Gujarat b.Punjab c.Tamil Nadu d.Rajasthan','a.Virendra Sehwag b.Saurabh Ganguly c.Sachin Tendulkar d.Mahendra Singh Dhoni','a.Mangal Pandey b.Tatya Tope c.Bhagat Singh d.Ramprasad Bismil','a.Arunachal Pradesh b.Maharashtra c.Assam d.Himachal Pradesh','a.Albert Einstein b.Alfred Nobel c.Thomas Edison d.Enrico Fermi']
an1 = ['c','a','d','c','b','b','d','a','d','b','c','a','d','c']
q2 = ['Who among the following was the Second prime minister of India','Which among the following was the national animal of India before year 1963','Who among the following is Founder the digital currency Bitcoin','Who among the following heads the RBI','What is the name of the coldest planet in the solar system',' What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923','Which was the first mountain peak above 8,000 metres in height to be summited by humans','What was the aircraft that dropped the first atomic bomb on Hiroshima on 6th Aug 1945 named after?','What was the only dowry, apart from a few yards of khadi, that Lal Bahadur Shastri accepted in his marriage',"In mythology, what was the name of Hiranyakashipu's wife and Prahlad's mother?",'Since its inception, which category of the Nobel Prize has been awarded every single year','Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament','The International Literacy Day is observed on','In which group of places the Kumbha Mela is held every twelve years']
o2 = ['a.Lal Bahadur Shastri b.Indira Gandhi c.Jawaharlal Nehru d.Shri Gulzarilal Nanda',' a.Tiger b.Lion c.Horse d.Cheetah','a.Satoshi Nakamoto b.Dilip Asbe c.Vladimir Tenev d.Ashish Singhal','a.Prime Minister b.Governor c.President d.Home Minister','a.Venus b.Jupiter c.Pluto d.Neptune','a.The Want and Means of India b.The Problem of the Rupee c.National Dividend of India d.The Law and Lawyers','a.Annapurna b.Lhotse c.Kanchenjunga d.Makalu',"a.a mythical weapon b.a film character c.the pilot's mother d.the place where it was built",'a.Bhagavad Gita b.Khadaunm c.Gandhi topi d.Charkha','a.Kapinjala b.Kayadhu c.Kamalakshi d.Kaushiki','a.Chemistry b.Physics c.Peace d.Economics','a.Solicitor General b.Attorney General c.Cabinet Secretary d.Chief Justice','a.Sep 8 b.Nov 28 c.May 2 d.Sep 22','a.Ujjain. Purl; Prayag. Haridwar b.Prayag. Haridwar, Ujjain,. Nasik c.Rameshwaram. Purl, Badrinath. Dwarika d.Chittakoot, Ujjain, Prayag,Haridwar',]
an2 = ['d','b','a','b','d','b','a','c','d','b','d','b','a','b']
q3 = ['The first ever full-length Gujarati movie is based on the life of which of the following personalities','“Singhasan Khali Karo Janta Aati Hai” is a famous poem written by which of the following poets','Which case was heard by the largest ever constitution bench of 13 Supreme Court judges',"According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer's curse",' Leena Gade, a person of Indian origin, is the first female race engineer to win which of the following races','Launched in 1817, which of these ships built by the Wadia Group in Bombay is the oldest British warship still afloat','Which of these artists was principally entrusted with the task of ‘illuminating’ the original document of the Constitution of India','Which of these was an alias used by Noor Inayat Khan to work as a spy for Britain in France during the Second World War','Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868','Who is the first woman to successfully climb K2, the world’s second highest mountain peak','Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt','The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla','Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government','Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk']
o3 = ['a.Narsi Mehta b. Premchand Bhatt c.Mahatma Gandhi d.Mira Bai','a.Sumitranandan Pant b Suryakant Tripathi Nirala c.Harivansh Rai Bachchan d.Ramdhari Singh Dinkar','a.Golkanath Case b.Ashoka Kumar Thakur Case c.Shah Bano Case d.Keshwananda Bharati Case','a.Kshemadhurti b.Dharmadatta c.Mitadhvaja d.Prabhanjana','a.Indianapolis 500 b.24 Hours of Le Mans c.12 Hours of Sebring d.Monaco Grand Prix','a.HMS Minden b.HMS Cornwallis c.HMS Trincomalee d.HMS Meanee','a.Ram Kinker Baij b.Benode Behari Mukherjee c.Abanindranath Tagore d.Nandlal Bose','a.Vera Atkins b.Krystyna Skarbek c.Julienne Aisner d.Jeanne-Marie Renier','a.Belgium b. Italy  c.Denmark  d.France','a. Junko Tabei b.Wanda Rutkiewicz c.Tamae Watanabe d.Chantal Mauduit','a.Mir Taqi Mir b.Mohammad Ibrahim Zauq c.Zahir Dehlvi d.Abul-Qasim Ferdowsi','a. Viceregal Lodge b.Gorton Castle c.Barnes Court d.Cecil Hotel','a.Cathay Cinema Hall b.Fort Canning Park c.National University of Singapore d.National Gallery of Singapore','a.Asanga b.Nagasena c.Mahadharmarakshita d.Dharmaraksita']
an3 = ['a','d','d','d','b','c','d','d','c','b','c','c','a','b']
am = [1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
engine.say('Please select from the below')
engine.runAndWait()
print("a.Start or b.exit")
j = input()
if(j == 'a'):
    engine.say("Let's Play Kon Baanega Karodpati")
    engine.say("You can anytime quit the game by pressing contrl + c")
    for i in range(0,15):
        if(i<4):
                engine.say("You have 30 Seconds To Answer The Question\n")
                engine.runAndWait()
                g = choice(q1)
                steve = []
                while True:
                    if g not in steve:
                        steve.insert(0,g)
                        break
                    else:
                        g = choice(q1)
                c = q1.index(g)
                print(g)
                engine.say(g)
                print(f'{o1[c]}')
                o1[c] = o1[c].replace('a.','A.')
                o1[c] = o1[c].replace('.'," ")
                engine.say(f'{o1[c]}')
                engine.runAndWait()
                try:
                    k = inputimeout(prompt="Enter your answer : ",timeout = 30)
                    j = k.lower()
                    if(j == an1[c]):
                        print("You won",am[i],"\n")
                        hari = am[i]
                        hari = str(hari)
                        engine.say("You Won")
                        engine.say(hari)
                        engine.runAndWait()
                    else:
                        engine.say("Sorry it's wrong answer\n")
                        engine.say("You Won Nothing\n")
                        engine.runAndWait()
                        break
                except TimeoutError:
                    engine.say("TimeUp\n")
                    engine.say("Sorry You lose\n")
                    engine.say("You Won Nothing\n")
                    engine.runAndWait()
                    break
                except KeyboardInterrupt:
                     engine.say("You Just exited the game")
                     engine.say("You Won")
                     engine.say(am[i-1])
                     engine.runAndWait()
                     break
        elif(i>3 and i<=8):
                engine.say("You have 60 seconds To Answer The Question\n")
                g = choice(q2)
                steve = []
                while True:
                    if g not in steve:
                        steve.insert(0,g)
                        break
                    else:
                        g = choice(q2)
                c = q2.index(g)
                print(g)
                engine.say(g)
                print(f'{o2[c]}')
                o2[c] = o2.replace('a.','A.')
                o2[c] = o2[c].replace('.'," ")
                engine.say(f'{o2[c]}')
                engine.runAndWait()
                try:
                    k = inputimeout(prompt="Enter your answer : ",timeout = 60)
                    j = k.lower()
                    if(j == an2[c]):
                        print("You won",am[i],'\n')
                        hari = am[i]
                        hari = str(hari)
                        engine.say("You Won")
                        engine.say(hari)
                        engine.runAndWait()
                    else:
                        engine.say("Sorry it's wrong answer\n")
                        print("You Won 10000'\n'")
                        engine.say("You Won 10000")
                        engine.runAndWait()
                        break
                except TimeoutError:
                    engine.say("TimeUp\n")
                    engine.say("Sorry You lose\n")
                    engine.say("You Won 10000'\n'")
                    engine.runAndWait()
                    break
                except KeyboardInterrupt:
                     engine.say("You Just exited the game")
                     engine.say("You Won")
                     engine.say(am[i-1])
                     engine.runAndWait()
                     break
        elif(i>8 and i<14):
                    print("No Time Limit To Answer The Question\n")
                    g = choice(q3)
                    steve = []
                    while True:
                        if g not in steve:
                             steve.insert(0,g)
                             break
                        else:
                             g = choice(q3)
                    c = q3.index(g)
                    print(q3[c])
                    engine.say(q3[c])
                    print(f'{o3[c]}')
                    o3[c] = o3[c].replace('a.','A.')
                    o3[c] = o3[c].replace('.'," ")
                    engine.say(f'{o3[c]}')
                    engine.runAndWait()
                    try:
                        k = input("Enter your answer : ")
                        j = k.lower()
                        if(j == an3[c]):
                            print("You won",am[i],'\n')
                            hari = am[i]
                            hari = str(hari)
                            engine.say("You Won")
                            engine.say(hari)
                            engine.runAndWait()
                        else:
                            engine.say("Sorry it's wrong answer\n")
                            engine.say("You Won 320000'\n'")
                            engine.runAndWait()
                            break
                    except KeyboardInterrupt:
                     engine.say("You Just exited the game")
                     engine.say("You Won")
                     engine.say(am[i-1])
                     engine.runAndWait()
                     break
else:
     engine.say("You just exited the game\n")
     engine.runAndWait()
     exit()