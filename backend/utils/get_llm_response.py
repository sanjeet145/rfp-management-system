from config.llm import llm,groq
import os
from config.logger import logging
from utils.exception_handler import ExceptionHandler
import sys
from utils.file_reader import extract_pdf_text,extract_docx, extract_excel

# def get_llm_repsonse(prompt, input):
#     try:
#         response = llm.chat.completions.create(
#             model=os.getenv("LLM_MODEL"),
#             messages=[
#                     {
#                         "role": "system",
#                         "content": prompt
#                     },
#                     {
#                         "role": "user",
#                         "content": input
#                     }
#                     ],
#             temperature=0
#             )
#         return response.choices[0].message.content
#     except Exception as e:
#         raise ExceptionHandler(e,sys)


def get_llm_repsonse(prompt:str, input:str)->str:
    try:
        response = groq.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": input
                    }
                    ],
            include_reasoning=False,
            temperature=0
            )
        logging.info("response has been generated from llm")
        return response.choices[0].message.content
    except Exception as e:
        raise ExceptionHandler(e,sys)
    



def get_llm_response_with_attachments(prompt: str, packet: dict, input:str) -> str:
    attachments = packet.get("attachments", [])

    if not attachments:
        logging.info("No attachments found in the vendor response.")
        return get_llm_repsonse(prompt, input)
    extracted_texts = []
    for att in packet["attachments"]:
        raw = att["raw_bytes"]
        filename = att["filename"].lower()

        if filename.endswith(".pdf"):
            text = extract_pdf_text(raw)
        elif filename.endswith(".docx"):
            text = extract_docx(raw)
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            text = extract_excel(raw)
        else:
            text = f"[Unsupported file type: {filename}]"

        extracted_texts.append(f"### {att['filename']}\n{text}")
    input_text = f"""
        {input}\n\n
        ATTACHMENTS TEXT:
        {'\n\n'.join(extracted_texts)}
    """
    return get_llm_repsonse(prompt, input_text)
