from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts.example_selector.base import BaseExampleSelector
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)


examples = [
    {
        "question": "What do you know about France?",
        "answer": """        
        Here is what I know:        
        Capital: Paris        
        Language: French        
        Food: Wine and Cheese        
        Currency: Euro        
        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """        
        I know this:        
        Capital: Rome        
        Language: Italian        
        Food: Pizza and Pasta        
        Currency: Euro        
        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """        
        I know this:        
        Capital: Athens        
        Language: Greek        
        Food: Souvlaki and Feta Cheese        
        Currency: Euro        
        """,
    },
]

#RandomSelector 생성
class RandomExampleSelector(BaseExampleSelector):
    def __init__(self, examples):
        self.examples = examples
        
    def add_example(self, example):
        self.examples.append(example)
        
    def select_examples(self, input_variables):
        from random import choice
        return [choice(self.examples)]
    
    
example_selectors = RandomExampleSelector(
    examples = examples
    )    

example_prompt = PromptTemplate.from_template([
    "Human:{question}\nAI:{answer}"
])

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    # examples=examples,    예제 선택 모두 활용
    example_selector=example_selector, #랜덤하게 예제 선택 활용
    suffix="Human: What do you know about {country}?",
    input_variables=["country"],
)


chain = prompt | chat
chain.invoke({
    "country" : "Japan"
})