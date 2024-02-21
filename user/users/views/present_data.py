from .scrape import main_function


def parse_function(WRESTLERS_OVERVIEWS, data) -> list:
    my_list = list()

    for i, n in enumerate(WRESTLERS_OVERVIEWS):
        
        if WRESTLERS_OVERVIEWS[i] == data:
            ac = list(WRESTLERS_OVERVIEWS[i+1])

            for a in range(len(ac)):
                if a > 1 and ac[a].isupper() and ac[a-1] != " " and ac[a-1].islower():
                    ac[a-1] += "," 

    my_list = "".join(ac)
    
    return my_list


class ScrapedWrestlerData():

    def __init__(self) -> None:
        pass

    def parse_list_scraped_data(self) -> None:
        pass

    

class GeneralScrapedData(ScrapedWrestlerData):
    def __init__(self, listing) -> None:
        super().__init__()
        self.wrestler_name = ""
        self.age = ""
        self.promotion = "" 
        self.active_roles = ""
        self.listing = list(listing)

    def parse_list_scraped_data(self) -> None:
        for position, letter in enumerate(self.listing):
            match letter:
                case "Current gimmick:":
                    self.wrestler_name = self.listing[position+1]
                case "Age:":
                    age = self.listing[position+1]    
                    if age != "":
                        age = age.replace(" years", "")
                        self.age =  age
                case "Promotion:":
                    self.promotion = self.listing[position+1]
                case "Active roles:":
                    self.active_roles =  self.listing[position+1]

class PersonnalScrapedData(ScrapedWrestlerData):
    def __init__(self, listing) -> None:
        super().__init__()
        self.birth_place = ""
        self.gender = ""
        self.Weight = ""
        self.background_in_sports = "" 
        self.website = ""
        self.listing = list(listing)

    
    
    def parse_list_scraped_data(self) -> None:
         for position, letter in enumerate(self.listing):
            match letter:
                case "Birthplace:":
                    self.wrestler_name = self.listing[position+1]
                case "Gender:":
                    self.gender =  self.listing[position+1]    
                case "Weight:":
                    weight = self.listing[position+1]
                    if weight != "":
                        weight = weight.split("(")
                        kg_weight = weight[-1].replace(" kg)", "")

                        self.weight = kg_weight

                case "Background in sports:":
                    self.background_in_sports =  self.listing[position+1]
                case "WWW:":
                    self.website =  self.listing[position+1]







class CareerScrapedData(ScrapedWrestlerData):
    def __init__(self, listing) -> None:
        super().__init__()   
        self.alter_egos = ""
        self.roles = ""
        self.year_of_beginning = "" 
        self.in_ring_experience  = ""
        self.wrestling_style = ""
        self.trainer = ""
        self.nickname = ""
        self.signature_moves = "" 
        self.listing = list(listing)
 
    def parse_list_scraped_data(self) -> None:
        for position, letter in enumerate(self.listing):
            match letter:
                case "Alter egos:":
                    alter_egos = parse_function(self.listing, "Alter egos:")
                    self.alter_egos = alter_egos
                case "Roles:":
                    self.roles =  self.listing[position+1]    
                case "Beginning of in-ring career:":
                    self.year_of_beginning = self.listing[position+1]
                case "In-ring experience:":
                    self.in_ring_experience = self.listing[position+1]
                case "Wrestling style:":
                    self.wrestling_style = self.listing[position+1]

                case "Trainer:":
                    self.trainer = self.listing[position+1]

                case "Nickname:":    
                    self.nickname = self.listing[position+1]

                case "Signature moves:":    
                    signature_moves = parse_function(self.listing, "Signature moves:")
                    self.signature_moves = signature_moves



class CareerListScrapedData(ScrapedWrestlerData):
    def __init__(self, listing) -> None:
        super().__init__()  
        self.listing = list(listing)
        self.career_list_field = ""

    def parse_list_scraped_data(self) -> None:
        for e in self.listing:
            self.career_list_field = e




class TournamentsListScrapedData(ScrapedWrestlerData):
    def __init__(self, listing) -> None:
        super().__init__()  
        self.listing = list(listing)
        self.tournaments_field = ""

    def parse_list_scraped_data(self) -> None:
        for e in self.listing:
            self.tournaments_field = e
