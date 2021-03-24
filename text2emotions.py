import text2emotion as te

def sort_emotions(emotions_dict):
    sorted_dict = {k: v for k, v in sorted(emotions_dict.items(), key=lambda item: item[1])}

    x = []

    for key, value in sorted_dict.items():
        x.append({
            'emotion': key,
            'value': value
        })

    return x

def get_sorted_emotions(text):
    emotions = sort_emotions(te.get_emotion(text))

    return emotions

def get_main_emotion(text):
    return get_sorted_emotions(text)[-1]['emotion']

def get_least_emotion(text):
    return get_sorted_emotions(text)[0]['emotion']

if __name__ == '__main__':
    input_file = 'text_sample.en.txt'
    output_file = 'text_output.en.txt'

    file1 = open(input_file, 'r')
    file2 = open(output_file, 'w')

    output_lines = []

    for line in file1.readlines():
        file2.write("{}\n".format(line.strip()))
        file2.write("  Main: {}\n".format(get_main_emotion(line)))
        file2.write("  Least: {}\n".format(get_least_emotion(line)))

        file2.write("\n  All:\n")

        for emotions in get_sorted_emotions(line):
            file2.write("    {}: {}\n".format(emotions['emotion'], emotions['value']))

        file2.write("\n")

    file1.close()
    file2.close()
