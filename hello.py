from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

information = """
    Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and political figure known for his key roles in the automotive company Tesla, Inc. and the space company SpaceX. Since January 2025, he is serving as Administrator of the Department of Government Efficiency, under the second Donald Trump presidential administration. He is also known for his ownership of X Corp. (the company that operates the social media platform X, formerly Twitter), and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI. Musk is the wealthiest individual in the world; as of January 2025, Forbes estimates his net worth to be US$427 billion.

A member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria. At the age of 18 he immigrated to Canada, acquiring its citizenship through his Canadian-born mother, Maye. Two years later, he matriculated at Queen's University in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University but never enrolled in classes, and with his brother Kimbal co-founded the online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In 2002, Musk acquired United States citizenship, and that October eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.

In 2004, Musk was an early investor in electric vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.), providing most of the initial financing and assuming the position of the company's chairman. He later became the product architect and, in 2008, the CEO. In 2006, Musk helped create SolarCity, a solar energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year Musk co-founded Neuralink, a neurotechnology company developing brain–computer interfaces, and the Boring Company, a tunnel construction company. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging he falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine. In 2022, he acquired Twitter for $44 billion, merged the company into his newly-created X Corp. and rebranded the service as X the following year. In 2023, Musk founded xAI, an artificial intelligence company.

Musk's actions and expressed views have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation, affirming antisemitic, homophobic and transphobic comments, and promoting conspiracy theories. His ownership of Twitter has been controversial because of large employee layoffs, an increase in posts containing hate speech, misinformation and disinformation on the service, and changes to service features, including verification. He became active in American politics leading up to the 2024 United States presidential election as a vocal and financial supporter of presidential candidate Donald Trump, becoming the largest political donor in the election. In January 2025, he was appointed as Administrator of the Department of Government Efficiency.
"""

if __name__ == "__main__":
    print("Hello Langchain!")
    summary_template = """
        given the information {information} about a person from I want you to create:
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
    res = chain.invoke(input={"information": information})
    
    print(res)
    
    print("          --------------------------------            ")
    print("          --------------------------------            ")
    

    llm_mistral = ChatOllama(model="mistral")

    # similar to making an api call to llm(open ai)
    chain_mistral = summary_prompt_template | llm_mistral | StrOutputParser()

    print("invoking the mistral chain")

    # invoke the chain defined above, also supply the values for the template
    res_mistral = chain_mistral.invoke(input={"information": information})

    print(res_mistral)
