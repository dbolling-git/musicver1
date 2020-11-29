from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):	
	
	def enter(self):
		print("This scene is not yet configured")
		print("Subclass it and implement enter().")
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		#be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"You're lack of practice is disturbing.",
		"You are not even good enough to play a two bit dive.",
		"You should quit music and play a sport.",
		"May this shame follow you through the many sad years ahead.",
		"I can't even look at you."
		
	]
	
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)







class Question(Scene):
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer
		
question_prompts = [
	"How many sharps are there in E Major?\n> ",
	"How many flats are there in F Major?\n> ",
	"How many sharps are there in B major?\n> ",
	"How many sharps are in A Major?\n> ",
	"How many flats are in Bb Major?\n> ",
	"How many flats are in Db Major?\n> ",
	"How many shaprs are in C# Major?\n> "
]

questions = [
	Question(question_prompts[0], "4"),
	Question(question_prompts[1], "1"),
	Question(question_prompts[2], "5"),
	Question(question_prompts[3], "3"),
	Question(question_prompts[4], "2"),
	Question(question_prompts[5], "5"),	
	Question(question_prompts[6], "7"),
]

question_prompts_two = [
	"What is missing G _ D in G Major?\n> ",
	"What is missing E _ B in E minor?\n> ",
	"What is missing Ab C _ in Ab Major?\n> ",
	"What is missing Bb D _ in Bb Major?\n> ",
	"What is missing E _ B in E Major?\n> ",
	"What is missing C# _ G# in C# Minor?\n> ",
	"What is missing F# _ C# in F# Minor?\n> ",
]

questions_two = [
	Question(question_prompts_two[0], "B"),
	Question(question_prompts_two[1], "G"),
	Question(question_prompts_two[2], "Eb"),
	Question(question_prompts_two[3], "F"),
	Question(question_prompts_two[4], "G#"),
	Question(question_prompts_two[5], "E"),	
	Question(question_prompts_two[6], "A"),
]

question_prompts_three = [
	"What is missing G B D _ in G7?\n> ",
	"What is missing E G B D _ in E minor7b9?\n> ",
	"What is missing Ab C Eb G Bb _ in Ab Major7#11?\n> ",
	"What is missing Bb _ F in Bb minor?\n> ",
	"What is missing E G# B D# _ in E Major9?\n> ",
	"What is missing C# _ G# B in C# Minor7?\n> ",
	"What is missing F# A C# _ in F# Minor7?\n> ",
]

questions_three = [
	Question(question_prompts_three[0], "F"),
	Question(question_prompts_three[1], "F"),
	Question(question_prompts_three[2], "D"),
	Question(question_prompts_three[3], "Db"),
	Question(question_prompts_three[4], "F#"),
	Question(question_prompts_three[5], "E"),	
	Question(question_prompts_three[6], "E"),
]






def run_quiz(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
		print("you got", score, "out of", len(questions))
	return score











class RiverTroll(Scene):

	def enter(self):
		print(dedent("""
			You are walking through a beautiful meadow on a warm spring day.
			It's a path you've never taken before. As you reach the crest of
			a hill you notice in the distance a long spanning bridge that is 
			broken in the middle. It draws your curiosity. As you approach a 
			hideous troll climbs from underneath the bridge and blocks your
			path. He smells to high heaven and asks to answer these questions
			or die. (Please answer with numbers only!)
			"""))
		results = run_quiz(questions) # results from the first quiz bank
		if results < 4:
			print(dedent("""
				The troll is not impressed, he picks up an oar and smashes you 
				hard to the ground. He unleashes a barrage of blows releasing his 
				fury, sharp pain fills your mind, and then everything vanishes. You
				are dead.
			    """))
			return 'death'	
		elif results < 6: 
			print(dedent("""
				The troll is incensed and lunges at you, you quickly dodge his attack and 
				counter. You land a nice combo of a straight jab and two quick kicks to
				it's shin. The troll strikes back and scratches your chest. You see red
				and unleash an amazing combo of roundhouses that sends the troll flying
				into the water. You grab the oar and the troll runs away.
				"""))
			return 'the_river'
		else:
			print(dedent("""
				The troll lowers his head, and looks you in the eye. He tells you that
				you are the most brilliant musician he's ever heard and retrieves a lute
				for you to play, you play lovely ballad, the troll is captivated. But,
				you notice that he's tightly gripping a sharp knife behind his back. You 
				get a bad feeling about it, and just that moment he slashes at you. You
				were prepared and you smash the lute over his head. He's completely 
				stunned and drops the knife. You take the knife and throw it into the 
				water. You grab a a nearby oar.
				"""))
			return 'the_river'	

class TheRiver(Scene):
	def enter(self):
		print(dedent("""
			You are completely out of your breath after the encounter with
			the troll. You see a boat near the river and you push it in. The 
			current sends you drifting downstream.
			"""))
		
		print(dedent("""
			You row the boat with the oar you took from the vanquished 
			troll. You make good time, and you eventually reach a fork 
			in the river. To your left you have a nice gentle channel, 
			to the right you can see rapids. Which direction are you 
			headed- left or right? (no caps)
			"""))
				
		action = input("> ")
		
		if action == "left":
			print(dedent("""
				You err on the side of caution and steer the boat down the easier
				of the paths. You take a nice calming deep breath as you pass
				a few cherry trees in full bloom
				"""))
			return 'left_path'
		elif action == "right":
			print(dedent("""
				You are filled with supreme confidence, the thought that keeps
				playing through your head is- There must be something at the 
				end of this channel. You push the boat into the rapids and your 
				boat begins to rock and tumble, but you hold on the best you can!
				"""))
			return 'right_path'
		else:
			print("I SAID NO CAPS!!! You are so dead!")
			return 'death'
						
class LeftChannel(Scene):
	def enter(self):
		print(dedent("""
			The day rolls along as you slowly drift. You have relaxed
			since your brush with the troll. Your guard is completely
			down when a swampy sea creature emerges from the river, and 
			lands into your boat with a thud. He demands that you answer
			his questions or prepare to meet your maker! (Please answer 
			with capital letters for pitch and # and b for sharp and 
			flat respectively.)
			"""))		
		results_two = run_quiz(questions_two) #results from the second quiz
		if results_two < 2:
			print("The river creature smashes your head, and tips the boat,- you die!")
			return 'death'
		elif results_two < 6:
			print("The river creature lowers his head, turns around and leaves.")
			return 'the_end' #change this after testing
		else:
			print("The river creature turns to smoke, and gold is left behind!")
			return 'the_end' #test
			
class RightChannel(Scene):
	def enter(self):
		print(dedent("""
			Things get really rough, the current tosses you to an fro.
			For a moment the boat almost completely capsizes but, with 
			your full strength to get it balanced. Things calm down, you
			collapse catching your breath. Overhead something blocks out 
			the sun with it's shadow. It's a giant golden Eagle!!! It is 
			quiet a sight to behold, the creature stares a moment and then
			instructs you to answer these questions or he will dispatch you!
			(Please answer with capital letters for pitch and # and b for sharp 
			and flat respectively.)
			"""))	
		results_three = run_quiz(questions_three) #results from third quiz
		if results_three < 2:
			print("The eagle pecks your eyes out, you fall into the water and drown.")
			return 'death'
		elif results_three < 6: 
			print ("The Eagle stares at you intently and takes off.")
			return 'the_end' #test
		else:
			print("The Eagle leaves, and returns a few minutes later with gold!")
			return 'the_end' #test
			
class TheEnd:
	
	def enter(self):
		print(dedent("""
			You pull the boat over and in the distance you see a neighboring
			town. You walk into town and reflect on the day you had. You 
			could kiss the ground you're so happy to be alive! A rainbow
			forms above your head and rose petals rain down. The air fills
			with a pleasant aroma, and a smile creeps upon your face. Tears
			of relief streak down your cheek, as you stumble into a chest filled
			to the brim with gold!
			"""))
		return 'finished'


class Finished(Scene):

	def enter(self):
		print("You won! Good job.")
		exit(1)
		
		
		
		
		
		
		
		
		
		
		
class Map(object):

	scenes = {
		'river_troll': RiverTroll(),				
		'finished': Finished(),
		'death': Death(),
		'the_river': TheRiver(),
		'left_path': LeftChannel(),
		'right_path': RightChannel(),
		'the_end': TheEnd(),
		'finished': Finished(),
	}

	def __init__ (self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)		
		

a_map = Map('river_troll')
a_game = Engine(a_map)
a_game.play()

