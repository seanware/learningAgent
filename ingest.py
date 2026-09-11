import requests
from minsearch import Index


def load_faq_data():
    docs_url = 'https://datatalks.club/faq/json/courses.json'
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = 'https://datatalks.club/faq'

    for course in courses_raw:
        course_url = f'{url_prefix}{course["path"]}'
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents

def course_documents():
    docs = [
    {'id' :1,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question': "How long is the CAST TEST" ,
    'answer' :  "The cast test is four sections",
    },
    {'id' :2,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : "What are the two types of electrical ciruits" ,
    'answer' :  " The types of circuits are parrallell and series",
    },
    {'id' :3,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What are the two types of energy from physics',
    'answer' :  " Kinetic energy and potential energy",
    },
    {'id' :4,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What is longer a meter or a foot',
    'answer' :  "1 meter is approximately 3.2 ft" , 
    },
    {'id' :5,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : "what has higher pressure a smaller diameter hose or a larger diameter hose",
    'answer' :  "A smaller house has higher pressure due to the Bernoulli principal",
    },
    {'id' :6,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What score should I get on the CASt test to get into the union',
    'answer' :  'It is unknown, but we recommend a score of 80%',
    },
    {'id' :8,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'How many liters are in a gallon',
    'answer' :  'There are 3.875 liters in a gallon',
    },
    {'id' :9,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What is the process for quick unit conversion',
    'answer' :  "Divide then multiply",
    }
    ]
    return docs


dcs= [
    {'id' :1,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question': "How long is the CAST TEST" ,
    'answer' :  "The cast test is four sections",
    },
    {'id' :2,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : "What are the two types of electrical ciruits" ,
    'answer' :  " The types of circuits are parrallell and series",
    },
    {'id' :3,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What are the two types of energy from physics',
    'answer' :  " Kinetic energy and potential energy",
    },
    {'id' :4,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What is longer a meter or a foot',
    'answer' :  "1 meter is approximately 3.2 ft" , 
    },
    {'id' :5,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : "what has higher pressure a smaller diameter hose or a larger diameter hose",
    'answer' :  "A smaller house has higher pressure due to the Bernoulli principal",
    },
    {'id' :6,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What score should I get on the CASt test to get into the union',
    'answer' :  'It is unknown, but we recommend a score of 80%',
    },
    {'id' :8,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'How many liters are in a gallon',
    'answer' :  'There are 3.875 liters in a gallon',
    },
    {'id' :9,
    'course' : "CAST Prep",
    'section' : "CONSTRUCT",
    'question' : 'What is the process for quick unit conversion',
    'answer' :  "Divide then multiply",
    }
    ]

def build_index(documents):
    index = Index(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course']
    )
    index.fit(documents)
    return index

if __name__  == "__main__":
    print(build_index(dcs))

