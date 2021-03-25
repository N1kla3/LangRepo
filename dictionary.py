import nltk.tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


class Dictionary():
    data = []

    def addDataFromText(self, text):
        if not text:
            return
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        words = tokenizer.tokenize(text)

        lemmatized = []
        lem = WordNetLemmatizer()
        for w in words:
            lemmatized.append(lem.lemmatize(w))

        freq = nltk.FreqDist(lemmatized)
        tags = nltk.pos_tag(lemmatized)

        for i in range(len(lemmatized)):
            tupel = self.find(lemmatized[i])
            tupel[1] += freq[lemmatized[i]]
            tupel[2] = tags[i][1]

    def setAtPosition(self, row, column, value):
        self.data[row][column] = value

    def find(self, word):
        for tupl in self.data:
            if tupl[0] == word:
                return tupl
        res = [word, 0, ""]
        self.data.append(res)
        return res


def show_words():
    text = """Amy normally hated Monday mornings, but this year was different. Kamal was in her art class and she liked Kamal. She was waiting outside the classroom when her friend Tara arrived.

“Hi Amy! Your mum sent me a text. You forgot your inhaler. Why don’t you turn your phone on?” Amy didn’t like technology. She never sent text messages and she hated Facebook too.

“Did Kamal ask you to the disco?” Tara was Amy’s best friend, and she wanted to know everything that was happening in Amy’s life. “I don’t think he likes me,” said Amy. “And I never see him alone. He’s always with Grant.” Amy and Tara didn’t like Grant.

“Do you know about their art project?” asked Amy. “It’s about graffiti, I think,” said Tara. “They’re working on it at the old house behind the factory.” “But that building is dangerous,” said Amy. “Aah, are you worried he’s going to get hurt?" Tara teased. “Shut up, Tara! Hey look, here they come!”

Kamal and Grant arrived. “Hi Kamal!” said Tara. “Are you going to the Halloween disco tomorrow?” “Yes. Hi Amy,” Kamal said, smiling. “Do you want to come and see our paintings after school?” “I’m coming too!” Tara insisted.

    """

