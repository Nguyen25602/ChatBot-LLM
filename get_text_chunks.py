from langchain.text_splitter import CharacterTextSplitter

def get_text_chunks(text):
    """
    This is the function to split the text block just created from the file.

    .. note::
        Implement by Hoang Nguyen

    Parameters
    ----------
    text: Str and None
        
    Return
    ----------
    The text paragraphs have already been split into smaller chunks using the given parameters.
    """
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
    
    