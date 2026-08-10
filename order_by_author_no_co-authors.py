import pandas as pd
import os
import shutil

corpus_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..', 'CCLAMP_Network', 'corpus')
)
print(corpus_dir)

corpus_out_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '', 'Corpus_ordered_by_author')
)
print(corpus_out_dir)

metadata_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'C-CLAMP_metadata_gender.txt')
)
metadata = pd.read_csv(metadata_file_path, sep='\t')
print(metadata)

# Loop over the metadata
for _, row in metadata.iterrows():

    file_name = row['File'] + '.txt'
    authors = row['Author']

    # Define the source path
    src_path = os.path.join(corpus_dir, file_name)

    # Check if the file exists before proceeding
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}. Skipping.")
        continue

    # Check if authors is a string
    if isinstance(authors, str):

        # Split multiple authors by ';'
        authors = [author.strip() for author in authors.split(';')]

        # Skip texts with multiple authors
        if len(authors) > 1:
            print(f"Multiple authors: {file_name} ({'; '.join(authors)}). Skipping.")
            continue

    else:
        # Place texts with no author in "No_Author"
        authors = ["No_Author"]

    # At this point there is exactly one author
    author = authors[0]

    # Define the destination path
    dest_dir = os.path.join(corpus_out_dir, author)
    dest_path = os.path.join(dest_dir, file_name)

    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy the file to the author's directory
    shutil.copy(src_path, dest_path)

print("Files grouped by author successfully!")