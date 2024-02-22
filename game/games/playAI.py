from random import randint


from django.views.generic import TemplateView
from django.shortcuts import render
from game.forms.play import ClassicQuestion, IntegerQuestion, CareerDataQuestion
from game.models import ScrapedWrestler, GameSetText

def random_wrestler_id(request) -> int:
    latest_id = ScrapedWrestler.objects.latest("id").id
    random_id = randint(0, int(latest_id))
    return random_id



class DatabaseQuestionCorrespondance:
    def __init__(self, QuestionSubject, QuestionAttribute, ChoosenWrestler, request) -> None:
        self.QuestionSubject = QuestionSubject.lower()
        self.QuestionAttribute = QuestionAttribute.lower()
        self.ChoosenWrestler = ChoosenWrestler
        self.QuestionDict = {
            "wrestler name": ChoosenWrestler.wrestler_name,
            "promotion": ChoosenWrestler.promotion,
            "active role": ChoosenWrestler.active_roles ,
            "birth place":ChoosenWrestler.birth_place,
            "gender":ChoosenWrestler.gender,
            "background in sports":ChoosenWrestler.background_in_sports,
            "website":ChoosenWrestler.website,
            "alter egos":ChoosenWrestler.alter_egos,
            "roles":ChoosenWrestler.roles,
            "year of beginning":ChoosenWrestler.year_of_beginning,
            "in ring experience":ChoosenWrestler.in_ring_experience,
            "wrestling style":ChoosenWrestler.wrestling_style,
            "signature moves": ChoosenWrestler.signature_moves
        }

        self.QuestionInteger = {
            "age": ChoosenWrestler.age,
            "weight": ChoosenWrestler.Weight
        }






        self.request = request
    def IsQuestionFound(self, Key, Value, MessageFound, MessageNotFound) -> str:

        Value = Value.lower()
        if self.QuestionAttribute == Value:
        
            return MessageFound
        else:
            return MessageNotFound
    
    def IterateQuestion(self) -> str:
        for Key, Value in self.QuestionDict.items():
            if self.QuestionSubject == Key:
                if self.QuestionSubject == "wrestler name":


                    self.request.session["points"] -= 1


                    return self.IsQuestionFound(Key, Value, Key + " found! +1 point or you!", Key + " not found! -1 point for you")
                
                
                return self.IsQuestionFound(Key, Value, Key + " found.", Key + " not found.")

    def IterateInteger(self) -> str:
        print(self.QuestionSubject)
        for Key, Value in self.QuestionInteger.items():
            if self.QuestionSubject == Key:
                if int(self.QuestionAttribute) < int(Value):
                    return "It's More!"
                elif int(self.QuestionAttribute) > int(Value):
                    
                    return "It's less!"
                return "It's that : " + str(Value)
            
def database_question_correspondance(question_subject, question_attribute, choosen_wrestler, request) -> str:

    question_subject = question_subject.lower()

    question_attribute = question_attribute.lower()
    
    data = DatabaseQuestionCorrespondance(question_subject, question_attribute, choosen_wrestler, request)
    return data.IterateQuestion()


def classic_generic_question(question, request, id_w):
    if question.is_valid():
        choosen_wrestler = ScrapedWrestler.objects.get(id=id_w)
        question_subject = request.POST.get('question_subject')
        question_attribute = request.POST.get('question_attribute', choosen_wrestler)
        return database_question_correspondance(question_subject, question_attribute, choosen_wrestler, request)




def database_integer_correspondance(question_subject, question_attribute, choosen_wrestler, request) -> str:
    question_subject = question_subject.lower()

    data = DatabaseQuestionCorrespondance(question_subject, question_attribute, choosen_wrestler, request)
    return data.IterateInteger()



def integer_generic_question(int_question, request, id_w):

    if int_question.is_valid():
        choosen_wrestler = ScrapedWrestler.objects.get(id=id_w)
        question_subject = request.POST.get('integer_question_subject')
        question_attribute = request.POST.get('integer_question_attribute')
        return database_integer_correspondance(question_subject, question_attribute, choosen_wrestler, request)
    

def parse_career_data(choosen_wrestler) -> list:
    
    right_value = choosen_wrestler.career_data

    this = ""

    for i in right_value:
        this += i
    right_value = "".join(right_value).replace(":", "|")
    right_value = "".join(right_value).replace("(", "|")
    right_value = "".join(right_value).replace(")", "|")

    return right_value.split("|")

def database_career_data_correspondance(number_of_matches, federation, choosen_wrestler, request) -> str:
    
    career_list = parse_career_data(choosen_wrestler)
    this = ""
    
    
    for i in career_list:
        print(i)
        if federation == i:
            print(i)
        if len(number_of_matches) == 4 and number_of_matches in i:
            this = "Yes, he do have played matches during this year"
            return this
        else:
            this = "No, he don't  have played matches during this year"
            
    return this  


def companies_maj(career_list) -> list:
    initials_company = []

    for i in range(len(career_list)):
        if "promotion" in career_list[i]:
            data = ""
            for j in career_list[i+1]:
                if j.isupper():
                    data += j
            initials_company.append(data)

    return initials_company

def federation_data_correspondance(federation, choosen_wrestler, request) -> str:
    career_list = parse_career_data(choosen_wrestler)
    this = ""

    federation = federation.lower()
    initials_company = companies_maj(career_list)
    c = ""

    for d in career_list:
        a = d
        a = a.lower()
        if federation in a:
            this = "yes, he have wrestled in this federation"
            return this
        else:
            this = "No, he do not have wrestled in this federation"
    
    federation_maj = federation.upper()

    for i in initials_company:
        if federation_maj == i:
            this = "yes, he have wrestled in this federation"
            return this
        else:
            this = "No, he do not have wrestled in this federation"
    return this



def year_between(year_min, year_max, choosen_wrestler, request) -> str:
    career_list = parse_career_data(choosen_wrestler)
    this = ""

    date = 0
    date_list = []
    for i in range(1850, 2024, 1):
        date_list.append(i)

    for i, j in enumerate(career_list):
        for c in date_list:
            if str(c) in career_list[i]:
                if int(c) > int(year_min) and int(c) < int(year_max):
                    this = "Yes, he have wrestled beteween these dates"
                    return this
                else:
                    this = "No, he don't have wrestled between these dates"
    return this




def year_and_federation(year, choosen_wrestler, federation, request) -> str:
    career_list = parse_career_data(choosen_wrestler)
    federations = federation.lower()
    this = ""

    initials_company = companies_maj(career_list)
    print(initials_company)
    for i, j in enumerate(career_list):       
        if len (year) == 4 and str(year) in career_list[i]:
            print(career_list[i])
            response = career_list[i+1].lower()
            response = response.replace("', '", "")
        
            if (federations in response and len(federation) >= 4 and " " in federation):
                this = "Yes, he do have played matches during this year in this federation"
            
            elif federation in initials_company:
                this = "Yes, he do have played matches during this year in this federation"
            
            else:
                this = "No, he don't  have played matches during this year"
    return this  
    

def federation_years(min_year, max_year, choosen_wrestler, federation, request) -> str:
    career_list = parse_career_data(choosen_wrestler)


    this = ""
    c = ""
    date = 0
    date_list = []
    counter = 0
    initials_company = []

    for i in range(1800, 2025, 1):
        counter += 1
        date_list.append(i)

    cd = []

    for i, j in enumerate(career_list):
 

        liste = []

        for d in federation:
            df = ""
            if d.isupper():
                pass
        for c in date_list:
            if str(c) in career_list[i]:

                if int(c) > int(min_year) and int(c) < int(max_year):
                    f = career_list[i+1].replace(", '", "")
                    f = f.replace("'", "")
                   
                    cd.append(f)   

        d = ""
        for c in date_list:
            if str(c) in career_list[i]:
                if int(c) >= int(min_year) and int(c) <= int(max_year):
                    f = career_list[i+1].replace(", '", "")
                    f = f.replace("'", "")
                    ejhffh = ""    

                    for ijk in cd:
                        if federation.lower() + " " == ijk.lower():
                            this = "Yes he have wrestled in this federation between thoses two dates"
                            return this
                        
                        for t in ijk:

                            if t.isupper():
                                ejhffh += t
                        d += ejhffh
                    initials_company.append(d)

                else:
                    this = "No, he don't have wrestled in thid federation between thoses two dates"


    print(initials_company)
    for dt in initials_company:
        if federation == dt:
            this = "Yes"
    return this


def career_data_question(career_questions, request, id_w):
    if career_questions.is_valid():
        choosen_wrestler = ScrapedWrestler.objects.get(id=id_w)
        year = request.POST.get('year')
        
        min_year = request.POST.get("year_between_min")
        max_year = request.POST.get("year_between_max")

        federation = request.POST.get('federation')        
        
        number_of_matches = request.POST.get("number_of_matches")

        to_return = ""
        if federation is not None:
            if len(federation) == 0 and len(number_of_matches) != 0 and len(year) == 0 and len(min_year) == 0 and len(max_year)== 0:
                print("1")
                to_return = database_career_data_correspondance(year, federation, choosen_wrestler, request)
            elif len(federation) != 0 and len(number_of_matches) == 0 and len(year) == 0 and len(min_year) == 0 and len(max_year)== 0:
                print("2")
                
                to_return = federation_data_correspondance(federation, choosen_wrestler, request)
            elif len(federation) != 0 and len(year) != 0 and len(number_of_matches) == 0 and len(min_year) == 0 and len(max_year)== 0:
                print("3")

                to_return = year_and_federation(year, choosen_wrestler, federation, request)
            
            
            elif len(min_year) != 0 and len(max_year) != 0 and len(federation) == 0 and len(year) == 0 and len(number_of_matches) == 0:
                print("4")

                to_return = year_between(min_year, max_year, choosen_wrestler, request)
            elif len(max_year) != 0 and len(federation) != 0 and len(min_year) != 0 and len(year) == 0 and len(number_of_matches) == 0:
                print("5")
                to_return = federation_years(min_year, max_year, choosen_wrestler, federation, request)
            else:
                print("none")
        return to_return

class PlayAI(TemplateView):
    
    template_name = "playAI.html"


    def get(self, request):
        game_set_text = GameSetText()


        return render(self.request, self.template_name, context={"classic_question": ClassicQuestion,
                                                  "game_setting": game_set_text.game_set}

                      )  

    def post(self, request):


        classic_question = ClassicQuestion(self.request.POST)

        integer_question = IntegerQuestion(self.request.POST)

        career_data_questions = CareerDataQuestion(self.request.POST)

        choosen_wrestler = ScrapedWrestler.objects.get(id=int(self.request.session.get("random_wrestler")   ))

        generic = classic_generic_question(classic_question, self.request, self.request.session["random_wrestler"]) 

        integer = integer_generic_question(integer_question, self.request, self.request.session["random_wrestler"]), 

        career = career_data_question(career_data_questions, self.request, self.request.session["random_wrestler"]),

        game_set_text = GameSetText.objects.get()
        if generic is None:
            generic = ""


        if integer is None:
            integer = ""
        return render(self.request, self.template_name, 
                      context=
                      {
                            "classic_question": ClassicQuestion, 
                            "integer_question": integer_question, 
                            "generic_question": generic, 
                            "integer": integer[0], 
                            "career_data_questions": career_data_questions,
                            "career_data_response": career[0],
                            "game_setting": game_set_text.game_set
                       })  
