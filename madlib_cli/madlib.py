
"""Madlibs! Open in the command line to play"""

import re



def greet_user_prompt():
    """
    This greets the user when they first start
    No input/output
    """

    ln_1 = 'Welcome to madlibs!!'
    ln_2 = 'You\'ll be prompted for words. '


    print((f'''
    {'*' * 80}
    {'{:^80}'.format(ln_1)}
    {'{:^80}'.format(ln_2)}
    {'*' * 80}
    '''))

def read_template(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError

def parse_template(template_text):

    # reg = r'(?<=\{).[^\}]+'
    reg = r'\{(.*?)\}'
    words = re.findall(reg, template_text)
    template_text = re.sub(reg, '{}', template_text)
    # print(template_text)
    return template_text, tuple(words)


def prompt_for_words(words):
    user_input = []
    for word in words:
        user_input.append(input(f'Enter a/an {word.lower()}: '))
    return user_input

def merge(template_text, user_input):
    """
    :param template_text:
    :param user_input:
    :return: Replace the text blanks with the user input and return a string
    """
    return template_text.format(*user_input)


def print_formatted(template_text):
    """
    :param template_text:
    :return: print the formatted text
    """
    print(template_text)

def write_to_a_file(filename, template_text):
    """
    :param filename:
    :param template_text:
    :return: the file with the template text printed into it
    """
    with open(filename, 'w') as output_file:
        output_file.write(template_text)

def run():
    greet_user_prompt()
    file_name = './madlib.txt'
    template_text = read_template(file_name)
    template_text, words = parse_template(template_text)
    user_input = prompt_for_words(words)
    template_text = merge(template_text, user_input)
    # print(template_text)
    print_formatted(template_text)
    output_filename = './madlib_result.txt'
    write_to_a_file(output_filename, template_text)


if __name__ == "__main__":
    run()