from add_status import status_message


def start_chat(name, age, rating):
    from spy_details import current_status_message

    if not age > 12 and age < 50:
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print(error_message)
    else:
        # authentication complete
        # show all the spy details
        # show a greeting message.
        welcome_message = "Authentication complete. Welcome\n\n" \
                          "Name : " + name + "\n" \
                                             "Age: " + str(age) + "\n" \
                                                                  "Rating: " + str(rating) + "\n" \
                                                                                             "Proud to have you on board\n"
        print(welcome_message)

        # displaying menu for user.

    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n " \
                   "2. Add a friend \n 3. Send a secret message \n " \
                   "4. Read a secret message \n 5. Read chats from a user \n 6. Close application \n"
        menu_choice = int(input(menu_choices))

        if menu_choice == 1:
            print('status')
            current_status_message = status_message(current_status_message)
        elif menu_choice == 2:
            print('Add a friends')

        elif menu_choice == 3:
            # send a secret message
            print('send secret msg')

        elif menu_choice == 4:
            # read the secret message sent by friend
            print('Read secret msg')

        elif menu_choice == 5:
            # read the chat history
            print('Read chats form a user')

        elif menu_choice == 6:
            # close application
            print('close application')
            show_menu = False

        # if user chooses other than menu choices.
        else:
            print("wrong choice try again.")
            exit()