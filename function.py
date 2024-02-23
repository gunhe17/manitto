from datetime import datetime
import random
import json

def get_manittos(
    participants="./participants.json", 
    history="./history.json"
):
    with open(participants, 'r') as file:
        data = json.load(file)
    participant_list = data["PARTICIPANTS"]
    
    with open(history, 'r') as file:
        previous_pairs = json.load(file)
    
    max_attempts = 100 
    for attempt in range(max_attempts):
        try:
            result = {}
            available_pairs = {participant: set(participant_list) - {participant} for participant in participant_list}

            for giver, receivers in previous_pairs.items():
                available_pairs[giver] -= set(receivers)
            
            for giver in participant_list:
                if not available_pairs[giver]: 
                    raise ValueError(f"{giver}에게 할당할 수 있는 마니또가 없습니다.")
                receiver = random.choice(list(available_pairs[giver]))
                result[giver] = receiver
                
                for participant in available_pairs:
                    available_pairs[participant].discard(receiver)
            break
        except ValueError as e:
            continue
    else:
        return "할당에 여러 번 실패했습니다. 조건을 다시 확인해 주세요."

    for giver, receiver in result.items():
        if giver in previous_pairs:
            if receiver not in previous_pairs[giver]: 
                previous_pairs[giver].append(receiver)
        else:
            previous_pairs[giver] = [receiver]
    
    with open(history, 'w') as file:
        json.dump(previous_pairs, file, ensure_ascii=False, indent=4)

    print(":: random choosen complete ::")
    
    return result

def create_notification(
    random_data,
):
    notification = f"./shared/{datetime.now().strftime('%m%d')}_notification.txt"

    with open(notification, 'w', encoding='utf-8') as file:
        for giver, receiver in random_data.items():
            file.write(f":: to.{giver}\n")
            file.write(f"금주 리더님의 기도 마니또는 {receiver} 리더님입니다. 최선의 방법으로 교제하고, 사랑하며 기도를 실천해주세요!\n\n")

    print(":: file creation complete ::")

######################
# Main Function
######################

def get_weekly_manitto():
    random_data = get_manittos()
    create_notification(random_data)

    print(":: all function run complete ::")

if __name__ == '__main__':
    get_weekly_manitto()