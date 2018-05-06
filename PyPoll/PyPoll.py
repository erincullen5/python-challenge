import os
import csv

path_poll_1 = os.path.join("Resources","election_data_1.csv")
path_poll_2 = os.path.join("Resources","election_data_2.csv")

file_to_output = os.path.join("Resources","text_file.txt")


def final_report (csvpath):
    #Create empty lists 
    votes = []
    candidates_list = []

    with open(csvpath, newline="") as csvfile:
        csvread = csv.reader(csvfile, delimiter=',')
        next(csvread)

        #Read in the CSV   
        csvread = list(csvread)        
        for row in csvread: 
            #add voter Id's to votes list
            votes.append(row[0])
            #add candidates to Candidates List
            candidates_list.append(row[2])

        # calculate the len of votes for the total number of votes
        votes = len(votes)
        
        candidates = list(set(candidates_list))
        results =[0,0,0,0]

        #Determine the canidates names based on the list
        cand_1 = candidates[0]
        cand_2 = candidates[1]
        cand_3 = candidates[2]
        cand_4 = candidates[3]

        for cand in candidates_list: 
            if cand == cand_1:
                results[0] += 1
            elif cand == cand_2:
                results[1] += 1
            elif cand == cand_3:
                results[2] += 1
            elif cand == cand_4:
                results[3] += 1
            else:
                print("This candidate is invalid")
                return
        
        #Calculate each percentage and round to 2 decimal points
        perc_cand_1 = ((results[0])/votes)*100
        perc_cand_1 = round(perc_cand_1,2) 
        
        perc_cand_2 = ((results[1])/votes)*100
        perc_cand_2 = round(perc_cand_2,2) 
        
        perc_cand_3 = ((results[2])/votes)*100
        perc_cand_3 = round(perc_cand_3,2) 

        perc_cand_4 = ((results[3])/votes)*100
        perc_cand_4 = round(perc_cand_4,2) 

        #calculate winner
        win_num = max(results)
        win_index = results.index(win_num)
        win_cand = candidates[win_index]

        #Print Results 
        election_results = (
            f"Election Results:'\n"
            f"------------------------------\n"
            f'Total Votes:{votes}\n'
            f'------------------------------\n'
            f'{cand_1} : {perc_cand_1}% ({results[0]})\n'
            f'{cand_2} : {perc_cand_2}%  ({results[1]})\n'
            f'{cand_3} : {perc_cand_3}% ({results[2]})\n'
            f'{cand_4} : {perc_cand_4}%  ({results[3]})\n'
            f'------------------------------\n'
            f'Winner: {win_cand}!\n'
            f'--------------------------------'
        )
        print(election_results)
        
        with open(file_to_output,"a") as text_file:
            text_file.write(election_results)    

final_report(path_poll_1)
final_report(path_poll_2)