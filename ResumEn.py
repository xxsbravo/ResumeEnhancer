import argparse
from docx import Document
from openai import OpenAI

def main():
    #provide user with help about the tool and how to use it
    parser = argparse.ArgumentParser(
        prog="ResumEn.py",
        description="Modifies your resume based on job descriptions to combat ATS filtering.",
        usage="ResumEn.py [arguments] [file]"
    )

    #accepted command-line arguments
    parser.add_argument("-f","--file", help="specifies the path to your resume (.docx only supported)")
    parser.add_argument("-i", "--input", help="path of input file containing job descriptions", required=True)

    #enables argparse; displays/prints to command line
    args = parser.parse_args()

    #get skills
    skills = extractSkills(args.input)

    #write skills to file
    skills2Docx(args.file, skills)

#takes job description from input file; extracts skills.
def extractSkills(path):
    #opens path to job description file
    with open(path, "r") as file:
        description = file.read()

    #specifies openai chatgpt prompt and expected output
    response = gpt.responses.create(
        model="gpt-4.1-2025-04-14",
        input=f"Extract exactly five of the most important skills from this job description and insert them in chronological order. Do not include any other text, and separate each skill with a comma.:\n{description}",
    )

    #gets skills, adds each element separated by commas into array
    skills = str.split(response.output_text, ', ')

    #return skills array to write later to .docx resume
    return skills 

def skills2Docx(path, skills):
    doc = Document(path)
    
    #finds 'Skills' header
    for index, paragraph in enumerate(doc.paragraphs):
        if 'PROFESSIONAL SKILLS' in paragraph.text:
            skillsLine = index    

    #writes skills list to resume
    #TODO: Copy correct style (fonts, font-size, etc.) of document
    for i in range(5):
        skillsLine += 1
        doc.paragraphs[skillsLine].text = skills[i]
        print(doc.paragraphs[skillsLine].text)        
        doc.save('updated_resume.docx')

    for paragraph in doc.paragraphs:
        print(paragraph.text)
    
if __name__=="__main__":
    main()