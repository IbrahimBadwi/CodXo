import random 
import requests # type: ignore
import string
import argparse
def number_guessing_game():
    print("welcome to the number guessing game !")
    print("i have selected a random number between 1 nd 100")
    print("can you guess what it is?")
    
target_number=random.randint(1,100)
attempts=0
while True:
    try:
        guess=int(input("enter your guess: "))
        attempts+=1
        if guess < target_number:
            print("low ! try again")
        elif guess > target_number:
                print("high ! try again" )
        else:
                    print(f"good ! you are smart you guess the number in {attempts} time ")
                    break
                
    except ValueError:
                        print("please enter a valid number")
                        print("thanks you for try my task ")
                        print("thanks for codeSognal to test me")
                        


class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.rates = {}
        self.update_rates()

    def update_rates(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.rates = response.json()['rates']
            else:
                raise Exception(f"Error fetching data: {response.status_code}")
        except Exception as e:
            print(f"Failed to update rates: {e}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency != "USD":
            amount = amount / self.rates.get(from_currency, 1)
        converted_amount = amount * self.rates.get(to_currency, 1)
        return converted_amount

def main():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    converter = CurrencyConverter(url)

    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency (e.g., USD, EUR): ").upper()
        to_currency = input("To currency (e.g., INR, GBP): ").upper()

        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the amount.")

if __name__ == "__main__":
    main()

class PasswordGenerator:
    def __init__(self, length=12,use_uppercase= True,use_digit=True,use_special=True):
        self.length=length
        self.use_uppercase = use_uppercase
        self.use_digit=use_digit
        self.use_special=use_special
    def generate(self):
        chaeacters=string.ascii_lowercase
        if self.use_uppercase:
            characters+=string.ascii_uppercase
        if self.use_digit:
            characters+=string.digit
        if self.use_special:
            characters+=string.punctuation
        if len(characters)==0:
            raise ValueError("no characters sets selected here!")
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
    def evaluate_strength(self,password):
        length_criteria = len(password) >= 12
        uppercase_criteria = any(c.isupper() for c in password)
        digit_criteria =any(c.isdigit() for c in password)
        special_criteria= any(c in string.punctuation for c in password)
        criteria_met = sum([length_criteria,uppercase_criteria,digit_criteria,special_criteria])
        if criteria_met == 4:
            return "strong"
        elif criteria_met == 3:
            return "medium"
        else:
            return "weak"
def main():
        parser = argparse.ArgumentParser(description="generate a secure password")
        parser.add_argument("-l","--length", type=int , default=12, help="length of the password(defualt: 12)")
        parser.add_argument("-u", "--no-uppercase", action="store_true", help="Exclude uppercase letters")
        parser.add_argument("-d", "--no-digits", action="store_true", help="Exclude digits")
        parser.add_argument("-s", "--no-special", action="store_true", help="Exclude special characters")

        args = parser.parse_args()

        generator = PasswordGenerator(
        length=args.length,
        use_uppercase=not args.no_uppercase,
        use_digits=not args.no_digits,
        use_special=not args.no_special
    )

        password = generator.generate()
        strength = generator.evaluate_strength(password)

        print(f"Generated password: {password}")
        print(f"Password strength: {strength}")

if __name__ == "_main_":
    main()