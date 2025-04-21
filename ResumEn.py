import argparse

# from openai import OpenAI

# response = gpt.responses.create(
#     model="gpt-4.1",
#     input="write a short haiku about love."
# )

# print(response.output_text)


def main():
    #provide user with help about the tool and how to use it
    parser = argparse.ArgumentParser(
        prog="ResumEn.py",
        description="Modifies your resume based on job descriptions to combat ATS filtering.",
        usage="ResumEn.py [arguments] [file]"
    )

    #accepted command-line arguments
    parser.add_argument("-f","--file", help="specifies the path to your resume (.docx only supported)", required=True)
    parser.add_argument("-i", "--input", help="path of input file containing job descriptions", required=True)

    #enables argparse; displays/prints to command line
    args = parser.parse_args()



if __name__=="__main__":
    main()