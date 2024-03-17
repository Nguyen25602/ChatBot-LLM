from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def get_vector_store(text_chucks):
    """
    Create Vector Store

    .. note::
        Implement by Hoang Nguyen

    Parameters
    ----------
    text: Str and None
        Text_chucks
    Return
    ----------
    Vector Store
    """
    embeddings = OpenAIEmbeddings()
    # model = INSTRUCTOR('hkunlp/instructor-xl')
    # sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
    # instruction = "Represent the Science title:"
    # embeddings = model.encode([[instruction,sentence]])
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chucks, embedding=embeddings)
    return vectorstore
    