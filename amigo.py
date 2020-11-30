from nltk.chat.util import Chat, reflections
pairs = [
['my name is (.*)', ['hello ! % 1']],
['(hi|hello|hey)',['hey there']],
['(.*) your name ?', ['my name is AMIGO']],
['(.*) help?', [ 'Sure! I can help you']],
['(.*) name?', [ 'BMS INSTITUE OF TECHNOLOGY AND MANAGEMENT']],
['(.*) contact?', [ '080 2856 1576']],
['(.*) address?', [ 'Doddaballapur Main Road, Avalahalli, Yelahanka, Bengaluru, Karnataka 560064']],
['(.*) about college?', [ 'The B.M.S. Institute of Technology and Management is a private engineering college in Bangalore, Karnataka, India affiliated to the Visvesvaraya Technological University, Belgaum. It was founded by B S Narayana, son of educationist B M Sreenivasaiah, and is managed by the B M S Educational Trust.']],
['(.*) website?', [ 'https://bmsit.ac.in']],
['(.*) email address?', [ 'principal@bmsit.in']],
['(.*) departments in total', [ 'Totally there are 9 departments \n1 Artificial Intelligence and Machine Learning \n2 Electronics and Communication Engineering \n3 Computer Science and Engineering \n4 Electronics and Telecommunication Engineering \n5 Mechanical Engineering \n6 Information Science and Engineering \n7 Electrical and Electronic Engineering \n8 Master of Computer Application \n9 Civil Engineering ']],
['(.*) about departments', [ 'Which department you would like to know about?']],
['(.*) information ISE', [ 'The Department of Information Science and Engineering started in the Year 2010.']],
['(.*)faculty A section', ['Mathematics: Dr Chetan \nData Structures and Application: Prof S Mahalakshmi S \nAnalog and Digital Electronics: Prof Vinutha K \nComputer Organization: Prof Chandra Shekhar K T \nSoftware Engineering: Dr Sheela K \nDiscrete Mathematical Structures: Dr Pushpa S K']],
['(.*)faculty B section', ['Mathematics: Prof Anitha Kiran \nData Structures and Application: Dr Veena N \nAnalog and Digital Electronics: Prof Vinutha K \nComputer Organization: Prof Swetha M S \nSoftware Engineering: Dr Sheela K \nDiscrete Mathematical Structures: Dr Pushpa S K']],
['(.*)faculty C section', ['Mathematics: Dr Shiva Prakash \nData Structures and Application: Prof Shanthi D L \nAnalog and Digital Electronics: Prof Ravi Kumar \nComputer Organization: Prof Swetha M S \nSoftware Engineering: Dr Rudresh S  \nDiscrete Mathematical Structures: Dr Aruna Kumari']],
['(.*) Number of students in each class?', [ 'between 70-80']],
['(.*) Email Id of Faculty?', [ 'xyz@gmail.com']],
['(.*) Club names', [ '\nEdc \nDance \nMusic \nCoding \nCodeChef chapter \nRotract \nNSS \nOikos \nArt']],
['(.*) contact details of club head?', [ '0000000000000']],
['(.*) do you do?', [ 'we answer your queries']],
['(.*)comedk fee structure?', ['comedk fee structure is 222870']],
['(.*)kcet fee structure?', ['comedk fee structure is 87261']],
['(.*)management fee structure?', ['comedk fee structure is 222870']],
['(.*)third internals?', ['7 to 9 dec']]
]
chat = Chat(pairs, reflections)
chat.converse()