import argparse
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import vstack, load_npz, save_npz
import numpy as np

def read_files(file_list):
    texts = []
    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as file:
            texts.append(file.read())
    return texts

class TfIdfTokenizer:
    def __init__(self):
        pass

    def __call__(self, doc):
        tokens = doc.split()
        return {token: 1 for token in tokens}

def save_sparse_matrix_as_text(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix:
            row_str = ' '.join([f"{i}:{val:.6f}" for i, val in zip(row.indices, row.data)])
            f.write(row_str + '\n')

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate TF-IDF term vectors for text files")
    parser.add_argument("-i", "--inputfile", help="inputfile", required=True)
    args = parser.parse_args()

    # Read list of filenames
    with open(args.inputfile, 'r') as f:
        filenames = f.read().splitlines()

    # Read file contents
    texts = read_files(filenames)

    # Initialize TfidfVectorizer with custom tokenizer
    vectorizer = TfidfVectorizer(tokenizer=TfIdfTokenizer(), lowercase=False)

    # Fit and transform the data
    tfidf_matrices = [vectorizer.fit_transform(texts)]

    # Concatenate the TF-IDF matrices
    tfidf_matrix = vstack(tfidf_matrices)

    # Save the concatenated TF-IDF matrix to a single .npz file
    npz_file = "combined_tfidf_matrix.npz"
    save_npz(npz_file, tfidf_matrix)
    print(f"Combined sparse TF-IDF matrix saved to {npz_file}")

    # Convert the TF-IDF matrix to text format
    txt_file = "combined_tfidf_matrix.txt"
    tfidf_matrix_text = load_npz(npz_file)
    save_sparse_matrix_as_text(tfidf_matrix_text, txt_file)
    print(f"Combined TF-IDF matrix saved to {txt_file} in text format")

if __name__ == "__main__":
    main()

# import argparse
# import os
# from sklearn.feature_extraction.text import TfidfVectorizer
# from scipy.sparse import vstack, save_npz

# def read_files(file_list):
#     texts = []
#     for filename in file_list:
#         with open(filename, 'r', encoding='utf-8') as file:
#             texts.append(file.read())
#     return texts

# class TfIdfTokenizer:
#     def __init__(self):
#         pass

#     def __call__(self, doc):
#         tokens = doc.split()
#         return {token: 1 for token in tokens}

# def main():
#     # Parse command line arguments
#     parser = argparse.ArgumentParser(description="Generate TF-IDF term vectors for text files")
#     parser.add_argument("-i", "--inputfile", help="inputfile", required=True)
#     args = parser.parse_args()

#     # Read list of filenames
#     with open(args.inputfile, 'r') as f:
#         filenames = f.read().splitlines()

#     # Read file contents
#     texts = read_files(filenames)

#     # Initialize TfidfVectorizer with custom tokenizer
#     vectorizer = TfidfVectorizer(tokenizer=TfIdfTokenizer(), lowercase=False)

#     # Fit and transform the data
#     tfidf_matrices = [vectorizer.fit_transform(texts)]

#     # Concatenate the TF-IDF matrices
#     tfidf_matrix = vstack(tfidf_matrices)

#     # Save the concatenated TF-IDF matrix to a single .npz file
#     output_file = "combined_tfidf_matrix.npz"
#     save_npz(output_file, tfidf_matrix)
#     print(f"Combined sparse TF-IDF matrix saved to {output_file}")

# if __name__ == "__main__":
#     main()


# # import argparse
# # import os
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from scipy.sparse import save_npz

# # def read_files(file_list):
# #     texts = []
# #     for filename in file_list:
# #         with open(filename, 'r', encoding='utf-8') as file:
# #             texts.append(file.read())
# #     return texts

# # class TfIdfTokenizer:
# #     def __init__(self):
# #         pass

# #     def __call__(self, doc):
# #         tokens = doc.split()
# #         return {token: 1 for token in tokens}

# # def main():
# #     # Parse command line arguments
# #     parser = argparse.ArgumentParser(description="Generate TF-IDF term vectors for text files")
# #     parser.add_argument("-i", "--inputfile", help="inputfile", required=True)
# #     args = parser.parse_args()

# #     # Read list of filenames
# #     with open(args.inputfile, 'r') as f:
# #         filenames = f.read().splitlines()

# #     # Read file contents
# #     texts = read_files(filenames)

# #     # Initialize TfidfVectorizer with custom tokenizer
# #     vectorizer = TfidfVectorizer(tokenizer=TfIdfTokenizer(), lowercase=False)

# #     # Fit and transform the data
# #     tfidf_matrix = vectorizer.fit_transform(texts)

# #     # Save the TF-IDF vectors to separate .npz files
# #     for i, filename in enumerate(filenames):
# #         # Extract filename without extension
# #         filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
# #         # Save the TF-IDF vector for the corresponding file
# #         output_file = f"{filename_without_ext}.npz"
# #         save_npz(output_file, tfidf_matrix[i])
# #         print(f"Sparse TF-IDF vectors for {filename} saved to {output_file}")

# # if __name__ == "__main__":
# #     main()
