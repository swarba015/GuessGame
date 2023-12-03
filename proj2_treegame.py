import ast

def isLeaf(tree):
    """
    Determines if a given node in the tree is a leaf node. A leaf node is defined as having no children.

    Parameters:
    tree (tuple): A node in the decision tree, represented as a tuple.

    Returns:
    bool: True if the node is a leaf (i.e., it has no left or right children), False otherwise.
    """
    if tree[2] is None and tree[1] is None:
        return True
    else:
        return False
    

def printTree(tree, prefix = '', bend = '', answer = ''):
    """
    Recursively prints the decision tree. It uses a combination of prefixes and visuals 
    to represent the structure of the tree, which helps in debugging or visualizing the tree structure.

    Parameters:
    tree (tuple): The decision tree or a subtree.
    prefix (str): The prefix used for printing the current node, helping to visualize the tree structure.
    bend (str): A visual cue ('+-' or '`-') used to represent the branching in the tree.
    answer (str): A label ('Yes: ' or 'No: ') indicating the decision at the current node.

    Returns:
    None: This function prints the tree structure to the console and does not return any value.
    """

    text, left, right = tree
    if left is None and right is None:
        print(f'{prefix}{bend}{answer}It is {text}')
    else:
        print(f'{prefix}{bend}{answer}{text}')
        if bend == '+-':
            prefix = prefix + '| '
        elif bend == '`-':
            prefix = prefix + ' '
            printTree(left, prefix, '+-', "Yes: ")
            printTree(right, prefix, '`-', "No: ")

    

def simplePlay(tree):
    """
    A simplified version of the guessing game. It traverses the decision tree based on user input 
    until it reaches a leaf node, and then makes a guess.

    Parameters:
    tree (tuple): The decision tree or a subtree.

    Returns:
    bool: True if the guess is correct, False otherwise.
    """

    if isLeaf(tree):
        ans = input(f"Is your object {tree[0]}? ").lower()
        if ans == "yes":
            return True
        else:
            return False
    else:
        ques = tree[0]
        user_response = input(ques).lower()
        if user_response == 'yes':
            return simplePlay(tree[1])
        else:
            return simplePlay(tree[2])
        
def play(tree):
    """
    The main game function. It walks through the decision tree based on user responses. If the guess
    is wrong, it updates the tree with new information provided by the user.

    Parameters:
    tree (tuple): The decision tree or a subtree.

    Returns:
    tuple: The updated decision tree after incorporating the new information from the user.
    """
    if isLeaf(tree):
        """
    Saves the current state of the decision tree to a file. This function is used for persisting the game
    state across sessions.

    Parameters:
    tree (tuple): The decision tree to be saved.
    treeFile (file object): A writable file object where the tree will be saved.

    Returns:
    None: This function writes to a file and does not return any value.
    """
        user_response = input(f"Is your object {tree[0]}? ").lower()
        if user_response == "yes":
            print("I got it!")
            return tree
        else:
            print("Drats! What was it? ")
            user_response = input().lower()
            query = input(f"What's a question that distinguishes a {user_response} from a {tree[0]}? ")
            query1= f"Does it has {query} ?"
            query_response = input(f"Does it has {query} ? ").lower()
            if query_response == "yes":
                new_tree = (query1, (user_response, None, None) ,tree)
                print("Thanks. Got it!")
                return new_tree
            else:
                new_tree = (query1,tree,(user_response, None, None))
                return new_tree
    else:
        user_response = input(f"{tree[0]}").lower()
        if user_response == 'yes':
            return (tree[0],play(tree[1]), tree[2])
        else:
            return (tree[0],tree[1],play(tree[2]))


def saveTree(tree, treeFile):
    """
    Loads a saved decision tree from a file. This function enables the game to continue learning 
    from where it left off in a previous session.

    Parameters:
    file (file object): A readable file object from which to load the tree.

    Returns:
    tuple: The loaded decision tree.
    """
    if isLeaf(tree):
        treeFile.write("Leaf" + "\n" + str(tree) + "\n")
    else:
        treeFile.write("Internal Node" + "\n" + str(tree[0]) + "\n")
        saveTree(tree[1], treeFile)
        saveTree(tree[2], treeFile)



def loadTree(file):
    """
    Loads a saved decision tree from a file. This function enables the game to continue learning 
    from where it left off in a previous session.

    Parameters:
    file (file object): A readable file object from which to load the tree.

    Returns:
    tuple: The loaded decision tree.
    """
    line = file.readline().strip()

    if not line:
        return None

    if line == "Leaf":
        tree_data = file.readline().strip()
        tree_data = ast.literal_eval(tree_data)
        return tree_data
    else:
        question = file.readline().strip()
        left_subtree = loadTree(file)
        right_subtree = loadTree(file)
        return (question, left_subtree, right_subtree)


def main():
    """
    The main driver of the program. It initializes the game, handles user interactions for playing the game, 
    loading and saving trees, and repeats the game cycle until the user decides to quit.

    Parameters:
    None

    Returns:
    None: This function controls the flow of the program and does not return any value.
    """
    print("Welcome to Guess Game!")

    tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))
    
    query = input("Would you like to load a tree from a file? (YES/NO) ").lower()
    if query == "yes":
        file_name = input("What's the name of the file? ")
        try:
            with open(file_name, "r") as treeFile:
                tree = loadTree(treeFile)
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with the default tree.")
            
    while True:
        tree = play(tree)  
        play_again = input("Would you like to play again? (YES/NO) ").lower()
        if play_again == "no":
            save_game = input("Would you like to save this tree for later? (YES/NO) ").lower()
            if save_game == "yes":
                filename = input("Please enter a file name: ")
                try:
                    with open(filename, "w") as treeFile:
                        saveTree(tree, treeFile)
                    print("Thank you! The file has been saved.")
                except IOError as e:
                    print(f"Error saving file: {e}")
            print("Goodbye! Thanks for playing!")
            break


if __name__ == "__main__":
    main()