def smartdoor():
    for password in range(1,4):
        seq_ans = "london"
        org_pass = "open@123"
        pass_code = input("Please Enter Password: ")
        if pass_code ==  org_pass:
            print("Welcome!....You can Enter")
            break
        elif password != 3:
            print("Wrong Password..Try Again")
        else:
            print("You Have To Answer Security Question to reset pass...what is your fav place?")
            seq_code = input("Please Enter secret answer : ")
            if seq_code == seq_ans:
                print("answer acepted")
                print("give new password :")
                new_arg_pass = input()
                smartdoor()
            else:
                print("wrong Sequrity Answer...Door is Locked")
                exit()

smartdoor()    
