#input_path: String of the file path for the input time-series CSV
#N: the threshold of wheel turn that signifies a turn in an automobile (in degrees)
#E1: the amount of time (in tenths of second) to capture before the turn begins
#E2: the amount of time (in tenths of second) to capture after the turn ends 
def turn_chunks(input_path, N = 180, E1 = 50, E2 = 0):
    df = pd.read_csv(input_path, na_values = ' ')
    end = 0
    for i in range(len(df)-1):
        i = end
        end = i + 1
        #sometimes can jump past the length of array; if so: terminate, we're done
        if i >= len(df):
            break
        if df['vtti.steering_wheel_position'][i] > N:
            start = i

            while df['vtti.steering_wheel_position'][end] > N:
                end += 1
            print("RIGHT",i)
            print(time(start - E1),",",time(end + E2))
        elif df['vtti.steering_wheel_position'][i] < -N:
            start = i
            while df['vtti.steering_wheel_position'][end] < -N:
                end += 1
            print("LEFT",i)
            print(time(start - E),",",time(end))

#takes input s representing time in tenths of a second. Returns tuple representing (hours, minutes, seconds) equivalent 
def time(s):
    s = s/10
    hour = int(s//3600)
    minute = int((s%3600)*60//3600)
    second = int(round(s - (hour*3600 + minute*60)))
    return((hour,minute,second))
