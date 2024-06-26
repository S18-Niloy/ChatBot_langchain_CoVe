######################################################################## BASELINE PROMPTS ########################################################################
BASELINE_PROMPT_WIKI = """Answer the below question which is asking for a list of entities (names, places, locations etc). Output should be a numbered list and only contains the relevant & concise enitites as answer. NO ADDITIONAL DETAILS.

Question: {original_question}

Answer:"""

BASELINE_PROMPT_MULTI = """Answer the below question correctly and in a concise manner without much details. Only answer what the question is asked.

Question: {original_question}

Answer:"""

BASELINE_PROMPT_LONG = """Answer the below question correctly.

Question: {original_question}

Answer:"""

################################################################### PLAN VERIFICATION PROMPTS ###################################################################
VERIFICATION_QUESTION_TEMPLATE_PROMPT_WIKI = """Your task is to create a verification question based on the below question provided.
Example Question: Who are allowed to open student bank account?
Example Verification Question: Is a [student] allwed to open [bank account]
Explanation: In the above example the verification question focused only on the ANSWER_ENTITY (creating student bank account) and QUESTION_ENTITY (student).
Similarly you need to focus on the ANSWER_ENTITY and QUESTION_ENTITY from the actual question and generate verification question.

Actual Question: {original_question}

Final Verification Question:"""

VERIFICATION_QUESTION_PROMPT_WIKI = """Your task is to create a series of verification questions based on the below question, the verfication question template and baseline response.
Example Question: Who are allowed to open student bank account?
Example Verification Question Template: Is a [student] allwed to open bank account?
Example Baseline Response: 1. Verifying NID and Student ID card
2. Verifying nominee with his/her NID
Verification questions: 1. Are all students allowed to open bank account?
2. Is nominee needed in creating student bank account?
etc.
Example Verification Question: 1. Are all students allowed to open bank account?
2. Is nominee needed in creating student bank account?

Explanation: In the above example the verification questions focused only on the ANSWER_ENTITY (student bank account) and QUESTION_ENTITY (creating student bank account) based on the template and substitutes entity values from the baseline response.
Similarly you need to focus on the ANSWER_ENTITY and QUESTION_ENTITY from the actual question and substitute the entity values from the baseline response to generate verification questions.

Actual Question: {original_question}
Baseline Response: {baseline_response}
Verification Question Template: {verification_question_template}

Final Verification Questions:"""

VERIFICATION_QUESTION_PROMPT_MULTI = """Your task is to create verification questions based on the below original question and the baseline response. The verification questions are meant for verifying the factual acuracy in the baseline response.
Example Question: What is Home Loan?
Example Baseline Response: A home loan, also known as a mortgage, is a type of loan specifically designed for purchasing a residential property, such as a house or an apartment. When individuals or families want to buy a home but do not have enough savings to make the purchase outright, they typically turn to a home loan to finance the purchase.
Example Verification Questions: 1. Is home loan for purchasing a residential property
2. Is it only applicable during shortage of savings?
Explanation: The verification questions are highly aligned with both the qctual question and baseline response. The actual question is comprises of multiple independent questions which in turn has multiple independent answers in the baseline response. Hence, the verification questions should also be independent for factual verification.

Actual Question: {original_question}
Baseline Response: {baseline_response}

Final Verification Questions:"""

VERIFICATION_QUESTION_PROMPT_LONG = """Your task is to create verification questions based on the below original question and the baseline response. The verification questions are meant for verifying the factual acuracy in the baseline response. Output should be numbered list of verification questions.

Actual Question: {original_question}
Baseline Response: {baseline_response}

Final Verification Questions:"""

################################################################## EXECUTE VERIFICATION PROMPTS ##################################################################
EXECUTE_PLAN_PROMPT_SEARCH_TOOL = """Answer the following question correctly based on the provided context. The question could be tricky as well, so think step by step and answer it correctly.

Context: {search_result}

Question: {verification_question}

Answer:"""


EXECUTE_PLAN_PROMPT_SELF_LLM = """Answer the following question correctly.

Question: {verification_question}

Answer:"""

EXECUTE_PLAN_PROMPT = "{verification_questions}"

################################################################## FINAL REFINED PROMPTS ##################################################################
FINAL_REFINED_PROMPT = """Given the below `Original Query` and `Baseline Answer`, analyze the `Verification Questions & Answers` to finally filter the refined answer.
Original Query: {original_question}
Baseline Answer: {baseline_response}

Verification Questions & Answer Pairs:
{verification_answers}

Final Refined Answer:"""

################################################################## ROUTER PROMPTS ##################################################################
ROUTER_CHAIN_PROMPT = """Please classify the below question in on of the following categories. The output should be a JSON as shown in the Examples.

Categories:
WIKI_CHAIN: Good for answering questions which asks for a list or set of entites as its answer. 
MULTI_CHAIN: Good for answering questions which  comprises of questions that have multiple independent answers (derived from a series of multiple discontiguous spans in the text) and multiple questions are asked in the original question.
LONG_CHAIN: Good for answering questions whose answer is long.

Examples:
WIKI_CHAIN:
    Question: Name some types of loan available in banks.
    JSON Output: {{"category": "WIKI_CHAIN"}}
    Question: Who are allowed to have credit card?
    JSON Output: {{"category": "WIKI_CHAIN"}}
    Question: List some banks who provide student bank account.
    JSON Output: {{"category": "WIKI_CHAIN"}}
MULTI_CHAIN:
    Question: Who is allowed to have student account, and is it applicable for school students?
    JSON Output: {{"category": "MULTI_CHAIN"}}
    Question: Who is allowed to have checkbook, and is it applicable with debit card?
    JSON Output: {{"category": "MULTI_CHAIN"}}
    Question: What is the highest deposited amount ina day, and how many times a person can deposit?
    JSON Output: {{"category": "MULTI_CHAIN"}}
LONG_CHAIN:
    Question: Write few lines about credit card system.
    JSON Output: {{"category": "LONG_CHAIN"}}
    Question: Tell me in short about ATMs.
    JSON Output: {{"category": "LONG_CHAIN"}}
    Question: Write a short desciption on agent banking.
    JSON Output: {{"category": "LONG_CHAIN"}}
    
Actual Question: {}
Final JSON Output:"""
