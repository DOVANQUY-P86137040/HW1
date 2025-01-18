def process_file(file_path):
    """
    Reads the RNA secondary structure file and extracts the title, sequence, and structure symbols.

    Args:
        file_path (str): Path to the RNA file.

    Returns:
        tuple: (title, sequence, symbol)
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    title = lines[0].strip()
    sequence = lines[1].strip()
    symbol = lines[2].strip()
    return title, sequence, symbol

def process_brackets(symbol):
    """
    Processes the bracket notation and returns a list of paired positions.

    Args:
        symbol (str): The bracket notation string.

    Returns:
        list: A list of tuples representing paired positions.
    """
    stack = []
    pairs = []

    for i, char in enumerate(symbol):
        if char in "(<[{":
            stack.append((char, i + 1))
        elif char in ")>]}":
            if stack:
                open_char, open_pos = stack.pop()
                pairs.append((open_pos, i + 1))
    
    return sorted(pairs)

def generate_results(sequence, pairs, title, output_file):
    """
    Generates the output file in the required format.

    Args:
        sequence (str): The RNA sequence.
        pairs (list): The list of paired positions.
        title (str): The title of the structure.
        output_file (str): Path to the output file.
    """
    with open(output_file, 'w') as f:
        f.write(f"{len(sequence)} {title}\n")

        for i in range(len(sequence)):
            base = sequence[i]
            pair = 0
            for p1, p2 in pairs:
                if p1 == i + 1:
                    pair = p2
                elif p2 == i + 1:
                    pair = p1

            f.write(f"{i + 1}\t{base}\t{i}\t{i + 2}\t{pair}\t{i + 1}\n")

def process_rna_file(input_file, output_file):
    """
    Integrates all steps to process an RNA file and generates the output file.

    Args:
        input_file (str): Path to the input RNA file.
        output_file (str): Path to the output file.
    """
    title, sequence, symbol = process_file(input_file)
    pairs = process_brackets(symbol)
    generate_results(sequence, pairs, title, output_file)

# Example usage
if __name__ == "__main__":
    input_path = "Fluoride_riboswitch-P._syringae_full.fa"  # Update with actual path
    output_path = "output.txt"
    process_rna_file(input_path, output_path)
    print("Output file generated.")
