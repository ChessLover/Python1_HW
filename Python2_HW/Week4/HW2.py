# Follow the diagram below and use Composite Design Pattern to implement and test the logic. 
# Add any other classes of your choice. The top of your hierchy will be the box which will contain Instrument Collection which will contain instruments. 


class Instrument:
  
    def __init__(self, functionality):
        self.functionality = functionality
  
    def make(self):
        print('\t', end = '')
        print(self.functionality)
        

class InstrumentCollection:
  
    def __init__(self, collection_id):
        self.collection_id = collection_id
        self.instruments = []
  
    def add(self, instrument):
        self.instruments.append(instrument)
        
    def remove(self, child):
        self.instruments.remove(child)
        
    def make(self):
        print(self.collection_id)

        for instrument in self.instruments:
            print('\t', end = '')
            instrument.make()
  
  
class Box:
  
    def __init__(self, functionality):
        self.functionality = functionality
        self.instrument_collections = []
        
    def make(self):
        print(self.functionality)

        for instrument_c in self.instrument_collections:
            print('\t', end = '')
            instrument_c.make()
  
    def add(self, instrument_c):
        self.instrument_collections.append(instrument_c)
  
    def remove(self, instrument_c):
        self.instrument_collections.remove(instrument_c)
  
  
box = Box('Box')
col1 = InstrumentCollection('Collection 1')
col2 = InstrumentCollection('Collection 2')
pen = Instrument('Pen')
pencil = Instrument('Pencil')
rubber = Instrument('Rubber')

col1.add(pen)
col1.add(pencil)

col2.add(pen)
col2.add(rubber)

box.add(col1)
box.add(col2)

box.make()