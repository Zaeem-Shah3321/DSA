import os
from preprocessing import preprocess
from similarity import cosine_similarity
import nltk

def load_document(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    nltk.download('stopwords')
    
    doc1 = load_document('F:\DSA\Week 16\data\Docs\doc1.txt')
    doc2 = load_document('F:\DSA\Week 16\data\Docs/doc2.txt')
    
    tokens1 = preprocess(doc1)
    tokens2 = preprocess(doc2)
    
    similarity = cosine_similarity(tokens1, tokens2)
    print(f"Cosine Similarity: {similarity}")

if __name__ == "__main__":
    main()