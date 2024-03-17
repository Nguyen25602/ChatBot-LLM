"""
Implement by Hoang Nguyen
    run app
"""

# import lib
import os
import streamlit as sl
from dotenv import load_dotenv

# import file process
from get_text_chunks import get_text_chunks
from get_vector_store import get_vector_store
from process_text_file import process_text_file

def main():
    # Setup env
    load_dotenv()
    # End
    # Setup GUI
    sl.set_page_config(page_title="Project LLM", page_icon=":cute:")
    sl.title("API Key")
    openaikey = None
    openaikey = sl.text_input("Nhập khóa API: ", type="password")
    os.environ["OPENAI_API_KEY"] = openaikey
    sl.header("Chat với nhóm :books:")
    sl.text_input("Nhập câu hỏi về tài liệu bạn vừa tải lên: ")
    
    with sl.sidebar:
        sl.subheader("Tài liệu")
        uploadedFiles = sl.file_uploader(
            label="Tải lên tài liệu bằng button dưới đây (pdf,csv,doc)",
            type=['pdf', '.csv', '.xlsx', '.xls', '.docx'],
            accept_multiple_files=True,
            help="Đây là phiên bản test nên đôi khi bị lỗi thông cảm ạ",
        )
            
        if sl.button("Xử lý"):
            with sl.spinner("Đang xử lý File"):
                # Process File
                raw_text = process_text_file(uploadedFiles)
                
                # Get the text Chunks
                text_chunks = get_text_chunks(raw_text)
                
                # Create Vector Store
                vector_store = get_vector_store(text_chunks)
                

if __name__ == '__main__':
    main()