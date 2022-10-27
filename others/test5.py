"""
i = 0
while i < 3:
    print('i =', i) # loop body
    # Restart loop logic
    i = i + 1
    if input() == 'r':
        i = 0 # force restart

"""
org_pass = "open@123"
password = 1
while password < 4:
    seq_ans = "london"
    pass_code = input("Please Enter Password: ")
    if pass_code ==  org_pass:
        print("Welcome!....You can Enter")
        break
    elif password != 3:
        print("Wrong Password..Try Again")
    else:
        print("You Have To Answer Security Question to reset pass...what is your fav place?")
        seq_code = input("Please Enter secret answer :")
        if seq_code == seq_ans:
            print("answer acepted")
            new_org_pass = input("give new password :")
            org_pass = new_org_pass
            print("New password has been updated")            
            password = 0
        else:
            print("wrong Sequrity Answer...Door is Locked")
    
    #org_pass = new_arg_pass
    password += 1