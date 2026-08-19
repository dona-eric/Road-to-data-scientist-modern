""" Avec la librairie langchain """
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
docs = """Machine learning is a subset of artificial intelligence (AI) that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention.
At its core, machine learning involves training algorithms on data to develop models that can perform specific tasks. These models learn relationships within the data, allowing them to generalize and make predictions or decisions on new, unseen data.
There are three primary types of machine learning:
1. Supervised Learning: In supervised learning, the algorithm learns from labeled data, meaning each data point is associated with a correct output or label. The goal is to learn a mapping function that can predict outputs for new inputs.
2. Unsupervised Learning: Unsupervised learning deals with unlabeled data, where the algorithm must discover patterns and structures on its own. Common tasks include clustering, dimensionality reduction, and association rule learning
3. Reinforcement Learning: Reinforcement learning involves an agent learning to make decisions by interacting with an environment. The agent receives rewards or penalties based on its actions, and its goal is to maximize cumulative reward over time.
Machine learning has applications across numerous industries, including healthcare, finance, retail, and manufacturing. From powering recommendation systems and fraud detection to enabling self-driving cars and medical diagnostics, 
machine learning continues to drive innovation and transform how we interact with technology and the world around us.
"""

splitter = CharacterTextSplitter(
    chunk_size=500 ,# taille maximale de tokens , vous pouvez en choisir autre
    chunk_overlap=100 ,# 20% de chevauchement pour éviter de perdre du contexte
    separator="\n", # separateur de chunk 
    length_function=len,
    is_separator_regex=False
)

chunks = splitter.split_text(docs)
# afficher les chuncks

for i, chunk in enumerate(chunks):
    print(f"=====Chunk {i+1}: {chunk}===========")

#### avec un document pdf

loader = PyPDFLoader("../data/fairmlbook.pdf")

document = loader.load()
splitter = CharacterTextSplitter(
    chunk_size=500 ,# taille maximale de tokens , vous pouvez en choisir autre
    chunk_overlap=100 ,# 20% de chevauchement pour éviter de perdre du contexte
    )

chunks = splitter.split_documents(document)

print(len(document))
print(len(chunks))
# afficher les chuncks
for i, chunk in enumerate(chunks):
    print(f"=====Chunk {i+1}: {chunk}===========")
    print(chunk.page_content[:500])
    print("\n \n", chunk.metadata)



"""avec la librairie llamaindex"""

