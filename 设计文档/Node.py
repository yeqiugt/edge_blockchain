import time
import numpy as np
import random
from Crypto.Hash import SHA256

from block import *

class Node():
    def __init__(self, id):
        self.id = id    # 同self.account
        self.token = []     # 挖出块的数量
        self.storage = []   # 存储的item数量
        self.init_time = time.time()    # 初始时间
        self.B = None       # B，在计算pos时用到的值

        self.total_num_nodes = 10   # 节点总数，10~50
        self.t0 = 0     # 每个产生一个块的预期时间
        self.M = 0      # 最大随机数

        self.lable = True   # 判断是否接收到了新块，默认为0，即没有接受到新块

    def generate_data_and_metadata(self):
        random.seed(self.id)
        data = [random.randint(0,10) for i in range(350*350)] # 产生一个大小约为1MB的随机数数组

        data_dict = {       # 可以考虑把data_dict做成双重字典，主键是id，做十个data出来
            'data_type': 'AirQuality/PM2.5',    # 然后再通过改时间构造出n*10个data
            'time': '11:00AM06-11-2018',
            'location': 'NewYorkNY/40.72,-74.00',
            'producer': self.id,
            'signature':SHA256.new(self.id).hexdigest(),
            'properties':'NULL'
        }
        block_demo = MetaData(data_dict)

        return block_demo

    def receive_block(self, block):
        '''
            接收到一个块，如果这个块是最新的块，请求最新的块
            验证块的信息
            更新token、storage、init_time
            重新计算B
            如果 poshash计算尚未停止，停止
            重新开始计算poshash
        '''
        self.token[block.node_index] += 1
        for metadata in block.content:
            for node_index in metadata.store_nodes:
                self.storage[node_index] += 1
        self.init_time = block.timestamp
        self.B = self.calulate_B()

    def generate_block(self,h):
        pass


    def pos_hash(self, block:Block, t):
        '''
            计算poshash值，
        '''
        poshash = SHA256.new((block.pos_hash+self.id).encode()).hexdigest()
        h = int(poshash, 16)%self.M
        u = self.storage[self.id] * self.token[self.id]
        b = self.B
        t = 1
        r = u*b*t
        while self.lable and h<=r:
            t = t + 1
            r = u*b*t
            time.sleep(1)
        if h > r:
            self.generate_block(h)
            return True
        else:
            return False


    def calulate_B(self):
        token = np.ndarray(self.token)
        storage = np.ndarray(self.storage)
        u = token*storage
        u = u.sum()/self.total_num_nodes
        b = self.M/((self.total_num_nodes+1)*self.t0*u)
        return b


if __name__ == '__main__':
        first_node = Node(0)
        black_demo = first_node.generate_data_and_metadata()
        print(black_demo)

