#ENGLISH_LETTER = ("x", "k", "y", "w", "j") #Tuple of letters not in italian dictionary

class CifrarioVernam():
    def __init__(self, message = "ciaosonosamueleemiopadresichiamaalberto", key = "itismariodelpozzocuneocorsoalcidedegasperi"):
        self.LETTER_NUMBER = (2 ** 8) - 1   #26
        self.message = message.lower()
        self.key = key.lower()

        #print(len(self.message), len(self.key))

        self.letter_to_number = {}  #{letter : number}
        self.number_to_letter = {}  #{number : letter}
        
        #if len(key) >= len(message):
        for number in range(self.LETTER_NUMBER):
            letter = chr(ord("a") + number)         #ord() -> letter to ascii ----- chr() -> ascii to letter
            self.letter_to_number[letter] = number

        for key, value in self.letter_to_number.items():
            self.number_to_letter[value] = key
        #else:
            #print("L'algoritmo non può essere eseguito perché non rispetta il vincolo: len(key) >= len(message)")
    

    def encoding(self):
        """
        Function to encode a message
        """
        if len(self.key) >= len(self.message):
            numerical_message = [self.letter_to_number[letter] for letter in self.message]
            numerical_key = [self.letter_to_number[letter] for letter in self.key]

            numerical_secret_message = [(message_number + key_number) % self.LETTER_NUMBER for message_number, key_number in zip(numerical_message, numerical_key)]

            literary_secret_message_list = [self.number_to_letter[number] for number in numerical_secret_message]
            literary_secret_message = ""
            for letter in literary_secret_message_list:
                literary_secret_message += letter
            return literary_secret_message
       
        return f"L'algoritmo non può essere eseguito perché non rispetta il vincolo: len(key) >= len(message)"

    def decoding(self, literary_secret_message):
        """
        Function to decode a message
        """
        if len(self.key) >= len(literary_secret_message):
            numerical_message = [self.letter_to_number[letter] for letter in literary_secret_message]
            numerical_key = [self.letter_to_number[letter] for letter in self.key]
            
            numerical_decoded_message = []
            #numerical_decoded_message = [(message_number - key_number) % self.LETTER_NUMBER for message_number, key_number in zip(numerical_message, numerical_key)]
            for message_number, key_number in zip(numerical_message, numerical_key):
                difference = message_number - key_number #difference between message_number and key_number
                while difference < 0:
                    difference += self.LETTER_NUMBER
                numerical_decoded_message.append(difference % self.LETTER_NUMBER)

            literary_decoded_message_list = [self.number_to_letter[number] for number in numerical_decoded_message]
            literary_decoded_message = ""
            for letter in literary_decoded_message_list:
                literary_decoded_message += letter
            return literary_decoded_message
        
        return f"L'algoritmo non può essere eseguito perché non rispetta il vincolo: len(key) >= len(message)"

def main():
    cifrario_vernam = CifrarioVernam()
    print(cifrario_vernam.decoding(cifrario_vernam.encoding()))

if __name__ == "__main__":
    main()