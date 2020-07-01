def copy_text():
    input_file = open('mytext.txt', 'rt')
    output_file = open('output_copy.txt','wt')

    for line in input_file:
        print(line.rstrip(), file = output_file)
        print('.', end="", flush=True)
    output_file.close()
    print('\ndone')

if __name__ == '__main__' :copy_text()