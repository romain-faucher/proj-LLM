
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os
from upstash_vector import Index , Vector



from dotenv import load_dotenv
load_dotenv(override=True)
# path = str et return lst de chunk
def chunk(path)   :
    headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)



    lstchunk = markdown_splitter.split_text(text)
    return lstchunk

def upsert(lstdoc,md) :
    index = Index(
            url=os.getenv("UPSTASH_VECTOR_REST_URL"), 
            token=os.getenv("UPSTASH_VECTOR_REST_TOKEN")
            )
    vectors=[]
    for i in range(len(lstdoc)):
        vectors.append(
            Vector(id=md+"-"+str(i), data=lstdoc[i].page_content, metadata=lstdoc[i].metadata)
            )
        
    index.upsert(vectors)

import os
from indexation import chunk, upsert

from dotenv import load_dotenv




data = ["data/expériences.md","data/competence.md","data/projet.md"]
lstbloc = []




for md in data :

    bloc = chunk(md)

    upsert(bloc,md)

print("fin")


