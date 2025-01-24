from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from external.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello Langchain!")
    summary_template = """
        given the linkedin information {information} about a person from I want you to create:
        1. a short summary within 100 words.
        2. two interesting facts about them.
    """
    # input variables are the list of keys, template is a placeholder
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Making use of langchain makes switching llm easy
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    llm = ChatOllama(model="llama3.2")

    print("defining the chain")

    # similar to making an api call to llm(open ai)
    chain = summary_prompt_template | llm | StrOutputParser()

    print("invoking the chain")

    # invoke the chain defined above, also supply the values for the template
    linkedin_data = scrape_linkedin_profile("abc", True)
    
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
