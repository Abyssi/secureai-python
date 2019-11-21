from utils.yaml import YAMLParser


class QNMain(object):
    @classmethod
    def main(cls, *args):
        topology = YAMLParser.parse("../../data/topology-1.yml")
        print(topology)


if __name__ == '__main__':
    import sys

    QNMain.main(sys.argv)
