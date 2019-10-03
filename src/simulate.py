import pyspark
from pyspark import SparkConf,SparkContext
import operator
import sys
import time
import random


data_source = "../data/csv/"
sc=SparkContext()

bat_1_rdd = sc.textFile(data_source + "bat_1.csv")
bat_bowl_1_rdd = sc.textFile(data_source + "bat_bowl_1.csv")
bat_grd_1_rdd = sc.textFile(data_source + "bat_ground_1.csv")
bat_bowl_grd_1_rdd = sc.textFile(data_source + "bat_bowl_ground_1.csv")
bowl_1_rdd = sc.textFile(data_source + "bowl_1.csv")
grd_1_rdd = sc.textFile(data_source + "ground_1.csv")
bowl_grd_1_rdd = sc.textFile(data_source + "bowl_ground_1.csv")
all_ipl_1_rdd = sc.textFile(data_source + "all_ipl_1.csv")

bat_2_rdd = sc.textFile(data_source + "bat_2.csv")
bat_bowl_2_rdd = sc.textFile(data_source + "bat_bowl_2.csv")
bat_grd_2_rdd = sc.textFile(data_source + "bat_ground_2.csv")
bat_bowl_grd_2_rdd = sc.textFile(data_source + "bat_bowl_ground_2.csv")
bowl_2_rdd = sc.textFile(data_source + "bowl_2.csv")
grd_2_rdd = sc.textFile(data_source + "ground_2.csv")
bowl_grd_2_rdd = sc.textFile(data_source + "bowl_ground_2.csv")
all_ipl_2_rdd = sc.textFile(data_source + "all_ipl_2.csv")
'''
print all_ipl_2_rdd.collect()
print "\n-----------------\n"
print all_ipl_1_rdd.collect()
exit()

ground=""
team1_name = ""
team2_name = ""
team1 = []
team2 = []
team1_bowlers = {}
team2_bowlers = {}
'''
def init(filename):
	input_data = open(filename,"r").read()

	ground,team1,team2,bowl_set1,bowl_set2 = input_data.split("----")
	team1_inter = team1.split("\n")
	team2_inter = team2.split("\n")

	team1_name = team1_inter[1]
	team2_name = team2_inter[1]
	#print team1_name

	team1 = team1_inter[2:-1]
	team2 = team2_inter[2:-1]

	#print team1[0]

	bowl1 = bowl_set1.split("\n")[1:-1]
	bowl2 = bowl_set2.split("\n")[1:-1]
	'''
	print bowl1
	print bowl2
	exit()
	'''
	team1_bowlers = {}
	team2_bowlers = {}
	for bowl in bowl1:
		over,name = bowl.split(";")
		team1_bowlers[over] = name

	for bowl in bowl2:
		over,name = bowl.split(";")
		team2_bowlers[over] = name

	return ground,team1,team2,team1_name,team2_name,team1_bowlers,team2_bowlers

def simulate_ball(batsman,bowler,ball_no,ground,second_innings):

	run = []
	probabilty = []
	run_comp_dict = {}
	a=0
	if(second_innings):
		bat_rdd = bat_2_rdd
		bowl_rdd = bowl_2_rdd
		grd_rdd = grd_2_rdd
		bat_bowl_rdd = bat_bowl_2_rdd
		bat_grd_rdd = bat_grd_2_rdd
		bowl_grd_rdd = bowl_grd_2_rdd
		bat_bowl_grd_rdd = bat_bowl_grd_2_rdd
		all_ipl_rdd = all_ipl_2_rdd

	else:
		bat_rdd = bat_1_rdd
		bowl_rdd = bowl_1_rdd
		grd_rdd = grd_1_rdd
		bat_bowl_rdd = bat_bowl_1_rdd
		bat_grd_rdd = bat_grd_1_rdd
		bowl_grd_rdd = bowl_grd_1_rdd
		bat_bowl_grd_rdd = bat_bowl_grd_1_rdd
		all_ipl_rdd = all_ipl_1_rdd

	bat = bat_rdd.filter(lambda line: (batsman in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bat)>0):
		bat = bat[0].split(":")
		run.append(bat[a-2])
		probabilty.append(bat[a-1])
	bowl = bowl_rdd.filter(lambda line: (bowler in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bowl)>0):
		bowl = bowl[0].split(":")
		run.append(bowl[a-2])
		probabilty.append(bowl[a-1])
	grd = grd_rdd.filter(lambda line: (ground in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(grd)>0):
		grd = grd[0].split(":")
		run.append(grd[a-2])
		probabilty.append(grd[a-1])
	bat_bowl = bat_bowl_rdd.filter(lambda line: (batsman in line and bowler in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bat_bowl)>0):
		bat_bowl = bat_bowl[0].split(":")
		run.append(bat_bowl[a-2])
		probabilty.append(bat_bowl[a-1])
	bat_grd = bat_grd_rdd.filter(lambda line: (batsman in line and ground in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bat_grd)>0):
		bat_grd = bat_grd[0].split(":")
		run.append(bat_grd[a-2])
		probabilty.append(bat_grd[a-1])
	bowl_grd = bowl_grd_rdd.filter(lambda line: (ground in line and bowler in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bowl_grd)>0):
		bowl_grd = bowl_grd[0].split(":")
		run.append(bowl_grd[a-2])
		probabilty.append(bowl_grd[a-1])
	bat_bowl_grd = bat_bowl_grd_rdd.filter(lambda line: (batsman in line and bowler in line and ground in line and ":"+str(ball_no)+":" in line)).collect()
	if(len(bat_bowl_grd)>0):
		bat_bowl_grd = bat_bowl_grd[0].split(":")
		run.append(bat_bowl_grd[a-2])
		probabilty.append(bat_bowl_grd[a-1])
	all_ipl = all_ipl_rdd.filter(lambda line: str(ball_no)+":" in line).collect()	
	if(len(all_ipl)>0):
		all_ipl = all_ipl[0].split(":")
		run.append(all_ipl[a-2])
		print all_ipl[a-2]
		probabilty.append(all_ipl[a-1])

	#print run
	total = 0.0
	for i in range(len(run)):
		if(str(run[i]) not in run_comp_dict.keys()):
			run_comp_dict[str(run[i])] = float(probabilty[i])
			total += float(probabilty[i])
		else:
			run_comp_dict[str(run[i])] += float(probabilty[i])
			total += float(probabilty[i])

	for key in run_comp_dict.keys():
		run_comp_dict[key] = run_comp_dict[key]/total 

	sorted_tups = sorted(run_comp_dict.items(), key=operator.itemgetter(1))
	#sorted_tups = sorted(sorted_tups,key=lambda x: x[0])
	#sorted_tups = sorted(sorted_tups,key=lambda x: x[1])
	print run_comp_dict,sorted_tups
	#try:
	runs = int(sorted_tups[-1][0])
	#except:
	#	runs = random.randint(-1,6)

	return runs

def inning_simulate(batting_team,bowling_team,first_total,ground):
	fp = open(sys.argv[3],"w")
	striker = batting_team[0]
	non_striker = batting_team[1]
	next_in = 2 
	wickets = 0
	total = 0

	batsman_card = {}
	batsman_card[striker] = [0,0]
	batsman_card[non_striker] = [0,0]

	second_innings = False

	if(first_total > 0):
		second_innings = True

	
	for ball_no in range(1,121):
		if(wickets == 10):
			break
		bowler = bowling_team[str((((ball_no-1)/6)+1))]	
		runs = simulate_ball(striker,bowler,ball_no,ground,second_innings)
		batsman_card[striker][1] += 1
		if(runs == -1):
			wickets += 1 
			fp.write(str((ball_no-1)/6)+"."+str(((ball_no-1)%6+1))+" : "+bowler+" to "+striker+" , OUT .....total :"+str(total)+"/"+str(wickets)+"....."+striker+" "+str(batsman_card[striker][0])+"("+str(batsman_card[striker][1])+")"+"\n")
			striker = batting_team[next_in]
			batsman_card[striker] = [0,0]
			next_in += 1
		else:
			batsman_card[striker][0] += runs
			total += runs
			fp.write(str((ball_no-1)/6)+"."+str(((ball_no-1)%6+1))+" : "+bowler+" to "+striker+" , "+str(runs)+" runs .....total :"+str(total)+"/"+str(wickets)+"\n") 

			if(runs%2 == 1):
				striker,non_striker = non_striker,striker

		if(((ball_no-1)%6+1) == 6):
			striker,non_striker = non_striker,striker
			fp.write("-------------End of over "+str((ball_no)/6)+"----------\n")			

		if(first_total > 0 and total > first_total):
			break
		#time.sleep(2)
	fp.write("Not out batsmen:\n")
	try:
		fp.write(striker+" "+str(batsman_card[striker][0])+"("+str(batsman_card[striker][1])+")\n")
	except:
		pass
	finally:
		fp.write(non_striker+" "+str(batsman_card[non_striker][0])+"("+str(batsman_card[non_striker][1])+")\n")
	fp.write("End of Innings........Final Score: "+str(total)+"/"+str(wickets)+"\n")
	fp.close()
	return total

def match_simulate(bat_first,ground,team1,team2,team1_name,team2_name,team1_bowlers,team2_bowlers):
	fp = open(sys.argv[3],"w")
	if(bat_first == 1):
		team_bat_first = team1
		team_bat_first_name = team1_name
		team_bowl_first = team2_bowlers
		team_bat_next = team2
		team_bat_next_name = team2_name
		team_bowl_next = team1_bowlers
	else:
		team_bat_first = team2
		team_bat_first_name = team2_name
		team_bowl_first = team1_bowlers
		team_bat_next = team1
		team_bat_next_name = team1_name
		team_bowl_next = team2_bowlers

	#fp.write("\nFirst Innings\n")
	#print team_bat_first,team1
	first_total = inning_simulate(team_bat_first,team_bowl_first,0,ground)
	#fp.write("\nSecond Innings\n")
	second_total = inning_simulate(team_bat_next,team_bowl_next,first_total,ground)

	if(first_total > second_total):
		print team_bat_first_name+" WINS"
		fp.write(team_bat_first_name+" WINS\n")
	elif(second_total > first_total):
		print team_bat_next_name+" WINS"
		fp.write(team_bat_next_name+" WINS\n")
	else:
		print "OH ITS A TIE!WE ARE GONNA HAVE A SUPER OVER!BUT UNFORTUNATELY WE ARE NOT SIMULATING THE SUPER OVER BECAUSE VIVEK SAID HE WILL KILL ME."
		fp.write("OH ITS A TIE!WE ARE GONNA HAVE A SUPER OVER!BUT UNFORTUNATELY WE ARE NOT SIMULATING THE SUPER OVER BECAUSE VIVEK SAID HE WILL KILL ME.\n")
	fp.close()   		
'''
if __name__ == "__main__":
	print(
	
		NOTE:The input file is expected to be in the following format:
		ground
		----
		team1_name
		team1 players seperated by newline
		----
		team2_name
		team2 players seperated by newline
		----
		team1_bowlers(over;bowler seperated by newline)
		----
		team2_bowlers(over;bowler seperated by newline)
	)

print sys.argv[1:]
exit()

Call the program as follows -- spark simulate.py input_file 1/2 output_file --master local[4]
'''
filename = sys.argv[1]
ground,team1,team2,team1_name,team2_name,team1_bowlers,team2_bowlers = init(filename)
print team1
bat_first = int(sys.argv[2])
match_simulate(bat_first,ground,team1,team2,team1_name,team2_name,team1_bowlers,team2_bowlers)	






