import anthropic
import os
import csv

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

input_file = 'ai_analysis_report.csv'
output_file = 'final_sentiment_results.csv'

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    # Define the headers for our new file
    fieldnames = ['Review Text', 'AI Sentiment Analysis']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    print(f"Processing reviews and saving to {output_file}...")

    for row in reader:
        review = row.get('Review Text', '')
        
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": f"Categorize this review sentiment as Positive, Negative, or Mixed, and give a 1-sentence reason: {review}"}]
        )
        
        ai_result = response.content[0].text.strip()
        
        # Save the result to the new CSV
        writer.writerow({'Review Text': review, 'AI Sentiment Analysis': ai_result})
        print(f"Analyzed: {review[:30]}...")

print("-" * 30)
print(f"DONE! You can now find '{output_file}' in your file explorer.")