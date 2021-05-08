from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('ChatBot')

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Hey Bot, Help me",
    "Hi, May I know what are you looking for!",
    "Admission",
    "Download Brochure",
    "Admission",
    "Application Form",
    "Ask any Query",
    "Please provide Mail ID to get more details",
    "courses",
    "UG: B.Sc and B.Com\nPG: M.Sc and M.Com",
    "General Info"
    "College Address\nGeneral Info\nContact\nGeneral Info\nWebsite"
    "Faculty"
    "Mrs Amba Ramaswamy - Principal & Correspondent",
    "B.Sc",
    """Maths, Physics and Computer Science\nMaths Electronics and Computer Science\n
     Maths Statistics and Computer Science\nMath, Physics and Chemistry\n
     Computer Science and Bio-Technology\nMicrobiology\nChemistry""",
    "B.Com",
    "Computer Science\nGeneral",
    "M.Sc",
    "Organic Chemistry",
    "M.Com",
    "Download the brochure",
    "Available course?",
    "Available courses are: B.Sc, B.Com, M.Sc and M.Com",
    "course available?",
    "Available courses are: B.Sc, B.Com, M.Sc and M.Com",
    "PG courses",
    "Available Courses are: M.Com and M.Sc",
    "Available PG courses",
    "Available Courses are: M.Com and M.Sc",
    "UG courses",
    "Available Courses are: B.Com and B.Sc",
    "Available PG courses",
    "Available Courses are: B.Com and B.Sc",
    "B.Sc",
    """it is a full time online graduation(3 year) course. it has 6 branches: Maths, Physics and Computer Science, 
    Maths Electronics and Computer Science, Maths Statistics and Computer Science, Math, Physics and Chemistry, 
    Computer Science and Bio-Technology, Microbiology, Chemistry,  
    Please select 12 for brochure or 13 for application form""",
    "B.Com?",
    """it is a full time online graduation(3 year) course. it has 2 branches: Computer Science and General""",
    "M.Com",
    """it is a full time online post graduation(2 year) course. it has 2 branches: Computer Science and General""",
    "M.Sc",
    "it is a full time online post graduation(2 year) course",
    "brochure",
    "please provide your mail id. we will send you a detailed brochure",
    "application form",
    "please provide your mail id. we will send you the Application form"
    "what is the admission process.",
    """You need to fill the application form. please provide your mail id to get application form. 
    filled application must be send to collage mail.""",
    "what is the fees for B.Sc Maths, Physics and Computer Science?",
    "Download the brochure",
    "what is the fees for B.Sc Maths Electronics and Computer Science?",
    "Download the brochure",
    "what is the fees for B.Sc Maths Statistics and Computer Science?",
    "Download the brochure",
    "what is the fees for B.Sc Math, Physics and Chemistry?",
    "Download the brochure",
    "what is the fees for B.Sc Computer Science and Bio-Technology?",
    "Download the brochure",
    "what is the fees for B.Sc Microbiology?",
    "Download the brochure",
    "what is the fees for B.Sc Chemistry?",
    "Download the brochure",
    "facilities",
    """	A well equipped Air conditioned Science and Computer Lab to suit the taste of the students\n
    	A full fledged Library""",
    "infrastructure",
    """	A well equipped Air conditioned Science and Computer Lab to suit the taste of the students\n
    	A full fledged Library""",
    "Campus Interviews",
    """Cordial tie-ups have been arranged with leading Industrial, 
    Business and Technological groups of the state for campus-interview to feed needy hours of the students.""",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)
