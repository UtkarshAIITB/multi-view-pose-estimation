# Xi Peng, May 2017
import argparse
import os
from utils import util

class BaseOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.initialized = False

    def initialize(self):
        self.parser.add_argument('--data_dir', type=str, default='./dataset',
                    help='training data or listfile path')
        self.parser.add_argument('--exp_dir',type=str, default='./exp',
                    help='root experimental directory')
        self.parser.add_argument('--exp_id', type=str, default='multi-view',
                    help='experimental name')
        self.parser.add_argument('--gpu_id', type=str, default='0',
                    help='gpu ids: e.g. 0  0,1,2, 0,2') ##TO DO
        self.parser.add_argument('--nThreads', type=int, default=3,
                    help='number of data loading threads')
        self.parser.add_argument('--is_train', type=bool, default=True,
                    help='training mode')
        self.parser.add_argument('--use_visdom', type=bool, default=True,
                    help='use visdom to display')
        self.parser.add_argument('--use_html', type=bool, default=False,
                    help='use html to store images')
        self.parser.add_argument('--display_winsize', type=int, default=256,
                    help='display window size') ##TO DO

        self.initialized = True

    def parse(self):
        if not self.initialized:
            self.initialize()
        self.opt = self.parser.parse_args()
        args = vars(self.opt)

        print('------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------')

        # save to the disk
        if self.opt.exp_id == '':
            print('Please set the experimental ID with option --exp_id')
            return
        exp_dir = os.path.join(self.opt.exp_dir, self.opt.exp_id)
        util.mkdirs(exp_dir)
        file_name = os.path.join(exp_dir, 'opt.txt')
        with open(file_name, 'wt') as opt_file:
            opt_file.write('------------ Options -------------\n')
            for k, v in sorted(args.items()):
                opt_file.write('%s: %s\n' % (str(k), str(v)))
            opt_file.write('-------------- End ----------------\n')
        return self.opt
