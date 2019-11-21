from utils.yaml import YAMLParser


class DQNMain(object):
    @classmethod
    def main(cls, *args):
        topology = YAMLParser.parse("../../data/topology-1.yml")
        print(topology)


if __name__ == '__main__':
    import sys

    DQNMain.main(sys.argv)
