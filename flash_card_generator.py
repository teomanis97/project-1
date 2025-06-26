from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

num = int(input("How many questions do you want to create in this card? "))

flashcards = []
for i in range(num):
    print(f"\nFlashcard {i+1}")
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards.append({"question": question, "answer": answer})

doc = Document()
doc.add_heading('Flashcards', 0)

for i, card in enumerate(flashcards, 1):
    
    q_para = doc.add_paragraph()
    q_para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    q_run = q_para.add_run(f"{i}. Q: {card['question']}")
    q_run.font.size = Pt(12)
    q_run.bold = True

    
    a_para = doc.add_paragraph()
    a_para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    a_run = a_para.add_run(f"A: {card['answer']}")
    a_run.font.size = Pt(12)

    doc.add_paragraph("")  
    
filename = "flashcards.docx"
doc.save(filename)

print(f"\n Flashcards saved to '{filename}'")
