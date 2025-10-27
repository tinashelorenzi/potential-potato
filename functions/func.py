
def save_to_log(action,date_and_time):
    print(f"{action} happened at {date_and_time}")
    return "Done"



action_to_use = "Login Successful"

date_n_time="12/12/25 12:38"

output = save_to_log(action_to_use,date_n_time)
print(output)