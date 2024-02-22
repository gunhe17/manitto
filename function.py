import random

def get_random_data(participants):
    pass

def create_result_file(
    assignments, 
    file_path='./results.txt'
):
    pass


###############
#   main
###############

def get_weekly_manitto(
    participants=[
        '김철수', '이영희', '박영수', '최영희', '정철수', '박영희'
    ]
):
    random_data = get_random_data(participants)
    create_result_file(random_data)

    print(":: complete ::")

if __name__ == '__main__':
    get_weekly_manitto()