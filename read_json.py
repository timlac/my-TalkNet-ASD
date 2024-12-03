import json

def print_structure_with_examples(data, indent=0, list_sample_size=20, string_sample_length=50):
    """
    Recursively print the structure of the JSON object with a few example values.
    - list_sample_size: Number of list elements to show as examples.
    - string_sample_length: Number of characters to show for strings.
    """
    if isinstance(data, dict):
        for key in data:
            print(" " * indent + f"{key}:")
            print_structure_with_examples(data[key], indent + 2, list_sample_size, string_sample_length)
    elif isinstance(data, list):
        print(" " * indent + "[List] (showing up to {} examples)".format(list_sample_size))
        for item in data[:list_sample_size]:
            print_structure_with_examples(item, indent + 2, list_sample_size, string_sample_length)
    elif isinstance(data, str):
        example = data[:string_sample_length] + ("..." if len(data) > string_sample_length else "")
        print(" " * indent + f"[String]: \"{example}\"")
    elif isinstance(data, (int, float, bool, type(None))):
        print(" " * indent + f"[{type(data).__name__}]: {data}")
    else:
        print(" " * indent + "[Unknown Type]")

# Load the JSON file
file_path = "demo/output_video_20_sec/pywork_json/scores.json"  # Replace with the path to your JSON file
with open(file_path, "r") as file:
    json_data = json.load(file)

# Print the structure of the JSON with examples
print_structure_with_examples(json_data)
