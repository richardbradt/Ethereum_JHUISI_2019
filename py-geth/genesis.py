# Richard Bradt, JHUISI 2019
#
# python3 genesis.py [arguments]
#   [-c chainID]
#   [-h homesteadBlock]
#   [-e eip155Block]
#   [-E eip158Block]
#   [-d difficulty] ["0x"]
#   [-g gasLimit] ["0x"]
#   [-a alloc] ['address1':'balance1' 'address2:'balance2' ...]
#   [-p $PATH]  Path to save new genesis file
#
# Take command-line arguments [sys.argv]. Create genesis.json in local directory if path not specified.

import os, sys
from random import randint

class Genesis():
    def __init__(self):
        # default variables
        self.chainID = self.getChainID()
        self.homeBlock = '0'
        self.e155 = '0'
        self.e158 = '0'
        self.difficulty = '0x400'
        self.gasLimit = '0x8000000'
        self.allocation = ''
        self.fpath = ''

    def getChainID(self):
        return "%d" % randint(10000, 99999)

    def getArguments(self):
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] == "-c":
                self.chainID = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == "-h":
                self.homeBlock = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == "-e":
                self.e155 = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == "-E":
                self.e158 = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == "-d":
                self.difficulty = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == "-g":
                self.gasLimit = sys.argv[i+1]
                i+=2
                continue
            elif sys.argv[i] == '-a':
                index = self.makeAllocString(i+1)
                i = index
                continue
            elif sys.argv[i] == '-p':
                self.fpath = sys.argv[i+1]
                i+=2
                continue
            else:
                if i >= len(sys.argv):
                    break
                else:
                    print('invalid argument')
                    i+=1

    def makeAllocString(self, index):
        # save arguments until next tag is found
        # expected "address":"balance"
        test_string = "-c-h-e-E-d-g-a-p"
        arg_list = []
        while index<len(sys.argv):
            if sys.argv[index] in test_string or index >= len(sys.argv):
                return_index = index
                break
            else:
                arg_list.append(sys.argv[index])
                index+=1

        # split by ':'
        # Create string >> "str[0]": {"Balance" : "str[1]"}
        for x in arg_list:
            splitArg = x.split(':')
            addString = '"%s": {"Balance":"%s"}' % (splitArg[0], splitArg[1])

            if len(self.allocation) == 0:
                self.allocation+=addString
            else:
                self.allocation+=', %s' % addString

        # return new sys.argv index
        return return_index

    def createFile(self, newpath=None):
        # Write variables to file in proper order and format
        # Create file. Give new filename if name already exists
        if newpath == None:
            newpath = self.fpath

        index = 1
        while os.path.exists("%spy_genesis_%s.json" % (newpath,index)):
            index += 1

        fname = "%spy_genesis_%s.json" % (newpath,index)

        # Write variables
        output = '{"config":{"chainID": %s, "homesteadBlock": %s, "eip155Block": %s, "eip158Block": %s},"difficulty": "%s", "gasLimit": "%s", "alloc":{%s}}' % (self.chainID, self.homeBlock, self.e155, self.e158, self.difficulty, self.gasLimit, self.allocation)

        newGen = open(fname, 'w')
        newGen.write(output)
        newGen.close

if __name__ == "__main__":
    gen = Genesis()
    for arg in sys.argv:
        print("%s\n" % arg)
    if len(sys.argv) > 1:
        gen.getArguments()
        gen.createFile()
    else:
        gen.createFile()
