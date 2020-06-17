
class Block():
    def __init__(self):
        self.id = id
        self.pre_block_hash = None
        self.node_index = None
        self.timestamp = None
        self.content = []
        self.block_storage = []
        self.pos_hash = None
        self.current_block_hash = None

class MetaData():
    def __init__(self, kwargs):
        self.data_type = kwargs['data_type']
        self.time = kwargs['time']
        self.location = kwargs['location']
        self.producer = kwargs['producer']
        self.signature = kwargs['signature']
        self.storing_nodes = None  # 这个字段由node填充
        self.valid_time = None     # 这个字段由node填充
        self.properties = kwargs['properties']
    def __repr__(self):
        print(f'data_type : {self.data_type}')
        print(f'time : {self.time}')
        print(f'location : {self.location}')
        print(f'producer : {self.producer}')
        print(f'signature : {self.signature}')
        print(f'storing_nodes : {self.storing_nodes}')
        print(f'valid_time : {self.valid_time}')
        print(f'properties : {self.properties}')
        return ''
