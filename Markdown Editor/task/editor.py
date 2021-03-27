lst_format = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
res = ''


def check_input():
    ch_a_form = str(input('- Choose a formatter: '))
    if ch_a_form == '!done':
        with open('output.md', 'w', encoding='utf-8') as f:
            f.write(res)
            f.close()
        quit()
    elif ch_a_form == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
        check_input()
    elif ch_a_form in lst_format:
        check_func(ch_a_form)
    else:
        print('Unknown formatting type or command. Please try again.')
        check_input()


def header_func():
    global res
    level = int(input('- Level: '))
    if 1 <= level <= 6:
        text = str(input('- Text: '))
        res += str(level * '#' + ' ' + text + '\n')
        output_lines(res)
    else:
        print('The level should be within the range of 1 to 6')


def plain_func():
    global res
    text = str(input('- Text: '))
    res += text
    output_lines(res)


def link_func():
    global res
    label = str(input('- Label: '))
    url = str(input('- URL: '))
    res += '[' + label + '](' + url + ')'
    output_lines(res)


def bold_func():
    global res
    text = str(input('- Text: '))
    res += '**' + text + '**'
    output_lines(res)


def italic_func():
    global res
    text = str(input('- Text: '))
    res += '*' + text + '*'
    output_lines(res)


def inline_code_func():
    global res
    text = str(input('- Text: '))
    res += '`' + text + '`'
    output_lines(res)
    check_input()


def list_func(n=0):
    global res
    n_rows = int(input('- Number of rows: '))
    if n_rows < 1:
        print('The number of rows should be greater than zero')
        if n == 0:
            list_func()
        else:
            list_func(1)
    else:
        print(n)
        for i in range(n_rows):
            row = str(input('- Row #' + str(i + 1) + ' '))
            if n == 0:
                res += str(i + 1) + '. ' + row + '\n'
            else:
                res += '* ' + row + '\n'
        output_lines(res)
        check_input()


def check_func(command):
    global res
    if command == 'plain':
        plain_func()
        check_input()
    elif command == 'header':
        header_func()
        check_input()
    elif command == 'link':
        link_func()
        check_input()
    elif command == 'new-line':
        res += '\n'
        output_lines(res)
        check_input()
    elif command == 'bold':
        bold_func()
        check_input()
    elif command == 'italic':
        italic_func()
        check_input()
    elif command == 'inline-code':
        inline_code_func()
        check_input()
    elif command == 'ordered-list':
        list_func()
        check_input()
    elif command == 'unordered-list':
        list_func(1)
        check_input()


def output_lines(lst):
    # for line in lst:
    #     print(line, end='')
    print(lst)


check_input()
