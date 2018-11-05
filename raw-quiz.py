# Sam Gomena  https://stackoverflow.com/questions/42526243/making-quiz-how-to-allow-user-to-have-multiple-trys-python

helpMessage = "The quotes have escaped their books and the library is in chaos! To earn bananas, tell each quote which Terry Pratchett book it belongs to."

quotes = [
    { "quote": "Tourist, Rincewind had decided, meant \'idiot\'.", 
    "book": "The Colour Of Magic"},
    
  { "quote": "Unseen University had never admitted women, muttering something about problems with the plumbing, but the real reason was an unspoken dread that if women were allowed to mess around with magic they would probably be embarrassingly good at it.", 
    "book": "The Light Fantastic"},
  
  { "quote": "She was already learning that if you ignore the rules people will, half the time, quietly rewrite them so that they don\'t apply to you.", 
    "book": "Equal Rites" },
  
  { "quote": "If you can't learn to ride an elephant, you can at least learn to ride a horse.", 
    "book": "Equal Rites" },
  
  { "quote": "History unravels gently, like an old sweater. It has been patched and darned many times, reknitted to suit different people, shoved in a box under the sink of censorship to be cut up for the dusters of propaganda, yet it always - eventually - manages to spring back into its old familiar shape.", 
    "book": "Mort"},

  { "quote": "People don't alter history any more than birds alter the sky, they just make brief patterns in it.", 
    "book": "Mort"},

  { "quote": "If there's one thing that really annoys a god, it\'s not knowing something.", 
    "book": "Mort"},

  { "quote": "I DON'T KNOW ABOUT YOU, he said, BUT I COULD MURDER A CURRY.", 
    "book": "Mort"},
    
  { "quote": "'What is there in this world that makes living worthwhile?' Death thought about it. CATS, he said eventually, CATS ARE NICE.", 
    "book": "Sourcery"},
    
  { "quote": "Things that try to look like things often do look more like things than things", 
    "book": "Wyrd Sisters" },

  { "quote": "The old king told me once that the gods gave people a sense of humour to make up for giving them sex.", "book": "Pyramids"},

  { "quote": "'Anti-dragon cream. Personal guarantee: if you\'re incinerated you get your money back, no quibble.'", "book": "Guards! Guards!"},

  { "quote": "Like all beekeepers, Death wore a veil. It wasn\'t that he had anything to sting, but sometimes a bee would get inside his skull and buzz around and give him a headache.", 
    "book": "Eric"},

  { "quote": "\'Woof bloody woof\' said Gaspode the Wonder Dog", 
    "book": "Moving Pictures"},

  { "quote": "Death\'s pale horse\'s name was Binky. He was a real horse. Death had tried fiery steeds and skeletal horses in the past, and found them impractical, especially the fiery ones, which tended to set light to their own bedding and stand in the middle of it looking embarrassed.", 
    "book": "Reaper Man"},
  
  { "quote": "If anyone's going to bury a wizard at a crossroads with a stake hammered through him then wizards ought to do it. After all, we\'re his friends.", 
    "book": "Reaper Man" },
  
  { "quote": "Vampires have risen from the dead, the grave and the crypt, but have never managed it from the cat.", "book": "Witches Abroad"},
  
  { "quote": "If you spend your whole time thinking about the universe, you tend to forget the less important bits of it. Like your pants.", 
    "book": "Small Gods"},
  
  { "quote": "You know... this reminds me of that famous logical puzzle.", 
    "book": "Lords and Ladies" },
  
  { "quote": "If the Creator had said, 'Let there be light' in Ankh-Morpork, he\'d have got no further because of all the people saying \'What colour?\'", 
    "book": "Men At Arms"},
  
  { "quote": "The question seldom addressed is where Medusa had snakes. Underarm hair is an even more embarrassing problem when it keeps biting the top of the deodorant bottle.", 
    "book": "Soul Music"},
  
  { "quote": "Probably the last sound heard before the Universe folded up like a paper hat would be someone saying \'What happens if I do this?\'", 
    "book": "Interesting Times"},
  
  { "quote": "Ahahahahaha! Ahahahaha! Aahahaha! BEWARE!!!!! Yrs sincerely, The Opera Ghost", 
    "book": "Maskerade"},
  
  { "quote": "The Ankh-Morpork view of crime and punishment was that the penalty for the first offence should prevent the possibility of a second offence.", 
    "book": "Feet Of Clay"},
  
  { "quote": "I... think my name is Bilious. I\'m the ... I\'m the oh God of Hangovers.", 
    "book": "Hogfather"},
  
  { "quote": "Lord Vetinari looked attentive, because he\'d always found that listening keenly to people tended to put them off. ", 
    "book": "Jingo"},
  
  { "quote": "Ridcully was good at doing without other people\'s sleep.", 
    "book": "The Last Continent"},
  
  { "quote": "Not many people ever tasted Nanny Ogg\'s home-made brandy; it was technically impossible. Once it encountered the warmth of the human mouth it immediately turned into fumes. You drank it via your sinuses.", 
    "book": "Carpe Jugulum"},
  
  { "quote": "It wasn\'t just that his brain was writing cheques that his body couldn\'t cash. It had gone beyond that. Now his feet were borrowing money that his legs hadn't got, and his back muscles were looking for loose change under the sofa cushions.", 
    "book": "The Fifth Elephant"},
  
  { "quote": "Sometimes glass glitters more than diamonds because it has more to prove.", 
    "book": "The Truth" },
  
  { "quote": "If you put a large switch in somecave somewhere, with a sign on it saying \'End-of-the-World Switch. PLEASE DO NOT TOUCH,\' the paint wouldn\'t even have time to dry.", 
    "book": "Thief of Time"},
  
  { "quote": "Lots of people would be as cowardly as me if they were brave enough.", 
    "book": "The Last Hero"},
  
  { "quote": "The second mouse gets the cheese!", 
    "book": "The Amazing Maurice And His Educated Rodents"},  

  { "quote": "To be a leader you have to learn to shout! But after you've learned to shout, you have to learn not to!", 
    "book": "The Amazing Maurice And His Educated Rodents"},
  
  { "quote": "Ninety percent of most magic merely consists of knowing one extra fact.", 
    "book": "Night Watch"},

  { "quote": "Two types of people laugh at the law\: those that break it and those that make it.", 
    "book": "Night Watch"},

  { "quote": "His movements could be called cat-like, except that he did not stop to spray urine up against things.", 
    "book": "Night Watch"},

  { "quote": "Truth! Freedom! Justice! And a hard-boiled egg!", 
    "book": "Night Watch"},
  
  { "quote": "If you trust in yourself and believe in your dreams and follow your star, you\'ll still get beaten by people who spent their time working hard and learning things and weren\'t so lazy.", 
    "book": "The Wee Free Men" },
  
  { "quote": "The enemy isn\'t men, or women, it\'s bloody stupid people and no-one has the right to be stupid.", 
    "book": "Monstrous Regiment" },
  
  { "quote": "It\'s still magic even if you know how it\'s done.", 
    "book": "A Hat Full Of Sky"},

  { "quote": "Some people believe that when you die, you cross the River of Death and have to pay the ferryman. People don\'t seem to worry about that these days. Perhaps there\'s a bridge now.", 
    "book": "A Hat Full Of Sky"},
  
  { "quote": "See a pin and pick it up, and all day long you\'ll have a pin.", 
    "book": "Going Postal"},
  
  { "quote": "What we could do is die valiantly. I\'ve seen men die valiantly. There\'s no future in it.", 
    "book": "Thud!"},
  
  { "quote": "Your own brain ought to have the decency to be on your side!", 
    "book": "Wintersmith"},

  { "quote": "They say that there can never be two snowflakes that are exactly alike, but has anyone checked lately?", 
    "book": "Wintersmith"},
  
  { "quote": "Students, eh? Love \'em or hate \'em, you can\'t hit them with a shovel!", 
    "book": "Making Money"},

  { "quote": "I wouldn\'t trust you with a bucket of water if my knickers were on fire!", 
    "book": "Making Money"},
  
  { "quote": "Juliet's version of cleanliness was next to godliness, which was to say it was erratic, past all understanding and was seldom seen.", 
    "book": "Unseen Academicals"},

  { "quote": "Don\'t be smart. Smart is only a polished version of dumb. Try intelligence. It will surely see you through.", 
    "book": "Unseen Academicals"},

  { "quote": "I think the Librarian has a motto in these cases: \'If you try to take my bananas from me, I will reclaim them from your cold dead hands.\'", 
    "book": "Unseen Academicals"},
  
  { "quote": "Evil begins when you begin to treat people as things.", 
    "book": "I Shall Wear Midnight" },
  
  { "quote": "If there were such a thing as an inter-city thieving contest, Ankh-Morpork would bring home the trophy and probably everyone\'s wallets.", 
    "book": "Snuff"},
  
  { "quote": "The commander went, as they say in Ankh-Morpork, totally Librarian on them.", 
    "book": "Raising Steam"},

  { "quote": "I see embarrassment among all of you. That\'s good. The thing about being embarrassed is that sooner or later you aren\'t, but you remember that you were.", 
    "book": "Raising Steam"},

  { "quote": "Moist groaned. It was the crack of seven and he was allergic to the concept of two seven o\'clocks in one day.", 
    "book": "Raising Steam"},

  { "quote": "It was like... like wizardry, but without the wizards and the mess.", 
    "book": "Raising Steam"},
  
  { "quote": "No shame in tears for them as you\'ve loved.", 
    "book":"The Shepherd\'s Crown" }
]

import random

questions = random.sample(range(0, 26), 5)
# print(questions)

score = 0

print(helpMessage + "\n")
for number in questions:
  print(quotes[number].get('quote'))

  answerCorrect = False
  attempts = 3

  while not answerCorrect:
    answer = input("Name the book for this quote:")
    attempts -= 1
    if answer.title() == quotes[number].get('book'):
      score += 1
      print('Well done! Here is your banana!\n')
      answerCorrect = True

    elif attempts > 0:
      print('Oops Try Again?\n')

    else:
      print("Sorry, no banana for you! The correct title is " + quotes[number].get('book') + "\n")
      break
      
print("Thanks for your help! You got " + str(score) + " banana" + ("s" if score != 1 else "") + "!")
