from heppy.framework.analyzer import Analyzer
from heppy.papas.aliceproto.aliceblockbuilder import BlockBuilder
from heppy.papas.pfalgo.distance  import Distance

class PapasPFBlockBuilder(Analyzer):

    def __init__(self, *args, **kwargs):
        super(PapasPFBlockBuilder, self).__init__(*args, **kwargs)
                
    def process(self, event):
        ecal = event.ECALclusters
        hcal = event.HCALclusters
        tracks = event.tracks
        blockbuilder = BlockBuilder(tracks, ecal, hcal)
        event.blocks = blockbuilder.blocks
        
