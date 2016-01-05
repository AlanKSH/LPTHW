class lexicon(object):

    def __init__(self):
        self.directions = ['north', 'south', 'east', 'west',
                           'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stops = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']
        self.results = []
        self.words =[]

    def convert_number(self,s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self, sent):
        self.words = sent.split()
        self.results = []
        for x in self.words:
            if x in self.directions:
                self.results.append(('direction', x))
            elif x in self.verbs:
                self.results.append(('verb', x))
            elif x in self.stops:
                self.results.append(('stop', x))
            elif x in self.nouns:
                self.results.append(('noun', x))
            elif self.convert_number(x) != None:
                self.results.append(('number', self.convert_number(x))) 
            else:
                self.results.append(('error', x))
        return self.results
         
    