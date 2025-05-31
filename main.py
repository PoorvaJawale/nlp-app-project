import google.generativeai as genai

class NLPModel:

    def get_model(self):
        GOOGLE_API_KEY="AIzaSyBKKAlFKiELXdbKr22n9OuJGnuWWpIwCXg"
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            model=genai.GenerativeModel("models/gemini-1.5-flash-latest")
            return model
        except Exception as e:
            print(e)
    
class NLPApp(NLPModel):

    def __init__(self):
        self.database={}
        self.first_menu()

    def first_menu(self):
        first_input=input("Hi! How would you like to proceed? \n 1.Not a member? Register \n 2.Already a member? Login \n 3.Exit anyways ")

        if first_input=='1':
            #register
            self.__register()
        
        elif first_input=='2':
            #login
            self.__login()

        else:
            exit()

    def second_menu(self):
        second_input=input("Hi! How would you like to proceed? \n 1.Sentiment analysis \n 2.Language translation \n 3.Language detection ")

        if second_input=='1':
            #sentiment analysis
            self.__sentiment_analysis()

        elif second_input=='2':
            #language translation 
            self.__language_translation()

        elif second_input=='3':
            #language detection
            self.__language_detection()

        else:
            exit()

    def __register(self):
        name=input("Enter your name: ")
        email=input("Enter your email id: ")
        password=input("Enter your password: ")

        if email in self.database:
            print("Email already exits.")
        
        else:
            self.database[email]=[name, password]
            print("Registration successful. Login next. ")
            self.first_menu()

    def __login(self):
        email=input("Enter your email id: ")
        password=input("Enter your password: ")

        if email in self.database:
            if self.database[email][1]==password:
                print("Login successful.")
                self.second_menu()
            
            else:
                print("Incorrect password.")
                self.__login()

        else:
            print("Email not found. Register first.")
            self.first_menu()

    def __sentiment_analysis(self):
        user_text=input("Enter prompt: ")
        model=super().get_model()
        response=model.generate_content(f"Give the sentiment of the sentence: {user_text}")
        print(response.text)
        self.second_menu()

    def __language_translation(self):
        user_text=input("Enter prompt: ")
        model=super().get_model()
        response=model.generate_content(f"Give the hindi translation of the sentence: {user_text}")
        print(response.text)
        self.second_menu()

    def __language_detection(self):
        user_text=input("Enter prompt: ")
        model=super().get_model()
        response=model.generate_content(f"Give the language of the sentence: {user_text}")
        print(response.text)
        self.second_menu()


if __name__=='__main__':
    nlp=NLPApp()


