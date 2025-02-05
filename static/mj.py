import json

file_path = r"static\horrer250.json"

# Load JSON data into the 'data' variable with UTF-8 encoding
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON. Details: {e}")
    exit()
except UnicodeDecodeError as e:
    print(f"Unicode decoding error: {e}. Try using 'utf-8' encoding.")
    exit()

# Function to clean the data
def clean_json(data):
    return {
        "title": data.get("title"),
        "url": data.get("url"),
        "description": {
            "@type": data["description"].get("@type"),
            "name": data["description"].get("name"),
            "description": data["description"].get("description"),
            "aggregateRating": {
                "ratingValue": data["description"].get("aggregateRating", {}).get("ratingValue")
            } if "aggregateRating" in data["description"] else None,
            "genre": data["description"].get("genre"),
            "datePublished": data["description"].get("datePublished"),
            "director": [
                {"name": director.get("name")}
                for director in data["description"].get("director", [])
            ] if "director" in data["description"] else []
        }
    }

# Clean the data
movies = []
for item in data:
    cleaned_item = clean_json(item)
    movies.append(cleaned_item)

# Save cleaned data back to a new JSON file
output_file = "cleanedMovieData.json"
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(movies, file, indent=4)

print(f"Cleaned data has been saved to {output_file}")
