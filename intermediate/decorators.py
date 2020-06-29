
import time


def elapsed_time(function):
    def calculate_elapsed_time():
        time_of_start = time.time()
        function()
        time_of_end = time.time()
        print(f'The funtion took {(time_of_end - time_of_start) *1000} ms to execute')
    return calculate_elapsed_time;


@elapsed_time
def big_sum():
    num_list =[]
    for num in range(0,1000):
        num_list.append(num)
    print(f'The sum is: {sum(num_list)}') 

def main():
    big_sum()

if __name__ == '__main__' : main()