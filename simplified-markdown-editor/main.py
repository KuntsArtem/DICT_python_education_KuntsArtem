final_text = ''
user_text = ''
command_list = ['plain', 'bold', 'italic', 'inline_code', 'link', 'header', 'unordered_list', 'ordered_list', 'done', 'newline', 'help']
def done():
    print("Thanks for using, all text saved to 'text.txt'!")
def help():
    print("Possible commands >" + str(command_list))
def plain():
    global final_text
    user_text = input("Enter plain text >")
    final_text = final_text + user_text
    print(final_text)
def bold():
    global final_text
    global user_text
    user_text = input("Enter bold text >")
    user_text = ("**" + str(user_text) + "**")
    final_text = final_text + user_text
    print(final_text)
def italic():
    global user_text
    global final_text
    user_text = input("Enter italic text >")
    user_text = ("*" + str(user_text) + "*")
    final_text = final_text + user_text
    print(final_text)
def inline_code():
    global user_text
    global final_text
    user_text = input("Enter inline-code text >")
    user_text = ("***" + str(user_text) + "***")
    final_text = final_text + user_text
    print(final_text)
def link():
    global final_text
    global user_text
    global user_text_link
    user_text = input("Enter link label text >")
    user_text_link = input("Enter URL text >")
    user_text = ("[" + str(user_text) + "]" + "(" + str(user_text_link) + ")")
    final_text = final_text + user_text
    print(final_text)
def header():
    global user_text
    global header_lvl
    global final_text
    header_lvl = input("Enter header level >")
    user_text = input("Enter header text >")
    user_text = (str('#' * int(header_lvl))) + ' ' + str(user_text)
    final_text = final_text + user_text
    print(final_text)
def ordered_list():
    global user_text
    global number_of_rows
    global final_text
    un_list = []
    user_text = str
    number_of_rows = int(input("Enter number of rows >"))
    x = 0
    z = number_of_rows
    while number_of_rows != 0:
        number_of_rows = number_of_rows - 1
        x = x + 1
        un_list.append(str(x) + ". " + str(input("Enter " + str(x) + " row >")))
    un_list.reverse()
    while z != 0:
        z = z - 1
        if z == 0:
            final_text = final_text + un_list[z]
        else:
            final_text = final_text + un_list[z] + "\n"
    print(final_text)
def unordered_list():
    global user_text
    global number_of_rows
    global final_text
    un_list = []
    user_text = str
    number_of_rows = int(input("Enter number of rows >"))
    x = 0
    z = number_of_rows
    while number_of_rows != 0:
        number_of_rows = number_of_rows - 1
        x = x + 1
        un_list.append("- " + input("Enter " + str(x) + " row >"))
    un_list.reverse()
    while z != 0:
        z = z - 1
        if z == 0:
            final_text = final_text + un_list[z]
        else:
            final_text = final_text + un_list[z] + "\n"
    print(final_text)
def newline():
    global final_text
    final_text = final_text + "\n"
    print(final_text)
user_command = ""
print("*******Markdown editor******* \n   Type <help> for show list of possible commands or <done> for save progress")
while user_command != 'done':
    user_command = str(input("Choose a formatter  >"))
    if user_command in command_list:
        eval(user_command)()
    else:
        print("Choose possible command")
f = open('text.txt', 'w')
f.write(final_text)