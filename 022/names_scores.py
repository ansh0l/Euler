import sys

    
def get_name_list(filename):
    """
    names are in format:
    "name1", "name2", "name3"
    """
    names_text = None 
    with open(filename, 'r') as f:
        names_text = f.read()
    names = names_text.replace('"', '').split(",")
    names.sort()
    return names

def get_name_score(index, name):
    name_worth, A = 0, ord('A')
    for char in name:
        name_worth += (ord(char) - A + 1)
    name_score = name_worth * index
    return name_score
    
def main():
    sigma_name_score = 0
    names = get_name_list("names.txt")
    for idx, name in enumerate(names):
        sigma_name_score += get_name_score(idx + 1, name)
    print sigma_name_score

if __name__ == "__main__":
    main()
