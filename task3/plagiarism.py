# Combat-Online-Plagiarism-with-AI
import requests

def check_plagiarism(text):
  api_key = "YOUR_API_KEY"
  url = "https://api.plagiarismdetection.com/check"
  headers = {"Authorization": f"Bearer {api_key}"}
  data = {"text": text}

  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    results = response.json()
    if results["plagiarism_found"]:
      print("Plagiarism detected:")
      for match in results["matches"]:
        print(f"Match: {match['source']}")
        print(f"Copied text: {match['text']}")
    else:
      print("No plagiarism found.")
  else:
    print("API request failed.")

# Example usage:
content = "This is an example text to check for plagiarism."
check_plagiarism(content)
