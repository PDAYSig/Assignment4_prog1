'''This program shows results from an election in Iceland. 
It givest the user options to prompts the user to '''




def command_1(constituance : str, electorals : int, constituance_dict : dict) -> None:
    '''If the user wants to see contituances, we store the constituances and electorals in a
    Dictionary, with the constituance as the key and electorals as the value'''
    constituance_dict[constituance] = int(electorals)
    return

def command_2(party_letter, party_name, parties_dict : dict) -> None:
    '''If the user wants to see the parties and their letters, we store the party letters and name in
    a dictionary, with the letter as the key and the name as the value'''
    parties_dict[party_letter] = party_name
    return

def add_to_result_list(line : str, result_list : list) -> None:
    '''Adds a given value to result_list in the form of a tuple'''
    letter, votes = line.split(";")
    value_tuple = (letter, votes)
    result_list.append(value_tuple)
    return

def command_3(line, results_dict : dict, result_list : list, constituance):
    '''If the user wants to see the results, we store the results from each constituency as a list of tuple,
    in a dictionary with the constituency name as the key and the list as the value'''
    
    #We first check if we are reading the constituance or the results
    if ";" in line:
        add_to_result_list(line, result_list)
    
    else:
        #The constituace starts as none, so if this is the first time this function is called we set it
        if constituance == None:
            constituance = line
        #If we are looking at a new constituance, we add the previous one, along with the list, to the dictionary
        else: 
            results_dict[constituance] = result_list
            result_list = []
        constituance = line
    return (constituance, result_list)

def read_file(action : int, file_name : str) -> dict:
    '''This function reads the file and returns a dictionary. 
    If it cannot find the file, it returns an empty dictionary.'''
    constituance_dict = {}
    parties_dict = {}
    results_dict = {}
    result_list = []
    constituance = None

    try:
        with open(file_name) as election_file:
            for line in election_file:
                line = line.strip()
                if action == 1:
                    constituance, electorals = line.split(";")
                    command_1(constituance, int(electorals), constituance_dict)
                    continue
                elif action == 2:
                    party_letter, party_name = line.split(";")
                    command_2(party_letter, party_name, parties_dict)
                    continue
                elif action == 3:
                    constituance, result_list = command_3(line, results_dict, result_list, constituance)
                    continue
    
    except FileNotFoundError:
        return
    
    if action == 1:
        return constituance_dict
    elif action == 2:
        return parties_dict
    elif action == 3:
        return results_dict



CONSTIT_WIDTH_1 = 20
CONSTIT_WIDTH_2 = 10

def show_constituances(constituance_dict : dict) -> None:
    '''This function displays the constituances as a table'''

    print(f'\n{"Constituency" :<{CONSTIT_WIDTH_1}}{"Electorals" :>{CONSTIT_WIDTH_2}}')
    print("-" * (CONSTIT_WIDTH_1 + CONSTIT_WIDTH_2))
    total_electorals = 0
    for constituance in constituance_dict:
        constituance = str(constituance)
        electorals = int(constituance_dict[constituance])
        print(f'{constituance :<{CONSTIT_WIDTH_1}}{electorals :>{CONSTIT_WIDTH_2}d}')
        total_electorals += electorals
    print("-" * (CONSTIT_WIDTH_1 + CONSTIT_WIDTH_2))
    total_print = "Total: "
    print(f"{total_print :<{CONSTIT_WIDTH_1}}{total_electorals :>{CONSTIT_WIDTH_2}d}")

PARTY_WIDTH_1 = 6
PARTY_WIDTH_2 = 26

def show_parties(parties_dict : dict):
    '''This function displays the parties as a table'''
    print(f"\n{'List' :<{PARTY_WIDTH_1}}{'Party' :>{PARTY_WIDTH_2}}")
    print("--------------------------------")
    for party_letter in parties_dict:
        party_name = parties_dict[party_letter]
        print(f"{party_letter :<{PARTY_WIDTH_1}}{party_name :>{PARTY_WIDTH_2}}")


RESULTS_WIDTH_1 = 10
RESULTS_WIDTH_2 = 26

def show_results(results_dict : dict, parties_dict : dict, constit_dict : dict):
    '''This function shows the election results in a constituency'''
    constit = input("Constituency: ")
    try:
        result_list = results_dict[constit]
    except KeyError:
        return
    print("\n",constit, sep="")
    print(f'{"List" :<{RESULTS_WIDTH_1}}{"Party" :>{RESULTS_WIDTH_2}}{"Votes" :>{RESULTS_WIDTH_1}}{"Ratio" :>{RESULTS_WIDTH_1}}')
    print("-"*56)

    totalvoters = 0
    for letter in result_list: 
        party_letter, votes = letter
        totalvoters += int(votes)
    ratio_total = 0
    for party in result_list:
        party = tuple(party)  #We make sure that party is treated as a tuple
        letter, votes = party
        ratio = int(votes)/totalvoters
        ratio_total += ratio
        ratio = round(ratio * 100, 1)
        party = parties_dict[letter]
        print(f'{letter :<{RESULTS_WIDTH_1}}{party :>{RESULTS_WIDTH_2}}{votes :>{RESULTS_WIDTH_1}}{ratio :>{RESULTS_WIDTH_1}.1f}')
    
    ratio_total = 100 * round(ratio_total, 1)
    print("-"*(RESULTS_WIDTH_1 * 3 + RESULTS_WIDTH_2))
    print(f'{"Total:" :<{RESULTS_WIDTH_1}}{" " * RESULTS_WIDTH_2}{totalvoters :>{RESULTS_WIDTH_1}}{ratio_total :>{RESULTS_WIDTH_1}.1f}')
    eligable_voters = constit_dict[constit]
    turnout = round(100 * (totalvoters/eligable_voters), 1)
    
    print(f'{"Turnout:" :<{RESULTS_WIDTH_1}}{" " * (RESULTS_WIDTH_2 + RESULTS_WIDTH_1)}{turnout :>{RESULTS_WIDTH_1}}')


def main():
    constituance_dict = {}
    parties_dict = {}
    results_dict = {}
    const_file_exists = False
    parties_file_exists = False
    results_file_exists = False

    action = 0 # We set action as 0 to enter the loop
    while action != 9:
        action = int(input("\n1. Show constituencies\n2. Show parties\n3. Show results\n9. Quit\n\nSelect an action: "))

        if action == 1:
            if const_file_exists:
                show_constituances(constituance_dict)
            
            else:
                file_name = "src/" + input("File name: ")
                constituance_dict = read_file(action, file_name)
            
                if constituance_dict == None:
                    continue

                show_constituances(constituance_dict)
                const_file_exists = True
    
        elif action == 2:
            if parties_file_exists:
                show_parties(parties_dict)

            else:
                file_name = "src/" + input("File name: ")
                parties_dict = read_file(action, file_name)
                
                if parties_dict == None:
                    continue

                show_parties(parties_dict)
                parties_file_exists = True


        elif action == 3:

            if results_file_exists:
                show_results(results_dict, parties_dict, constituance_dict)

            else:
                file_name = "src/" + input("File name for results: ")
                if parties_file_exists and const_file_exists:
                    results_dict = read_file(action, file_name)
                    if results_dict == None:
                        continue
                
                    results_file_exists = True
                    show_results(results_dict, parties_dict, constituance_dict)

                else:
                    continue


if __name__ == "__main__":
    main()

