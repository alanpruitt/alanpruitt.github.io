import os
from substack import Api

# Initialize your Substack connection securely using local environment variables
api = Api(
    email=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
    publication_url="https://alanpruitt.substack.com"
)

# Example loop to read local Markdown files and push them strictly as drafts
essay_files = ["essay-29.md", "essay-30.md", "essay-31.md"]

for file_path in essay_files:
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    
    # Creates an unpublished draft safely without triggering subscriber emails
    result = api.create_draft_from_markdown(
        title=f"Migrated Essay: {file_path}",
        markdown=markdown_content,
        tags=["Curriculum-as-Code", "EdTech"]
    )
    print(f"Staged draft successfully: {result['draft']['id']}")
