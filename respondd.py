#!/usr/bin/env python3

import omada_respondd.config as config
from omada_respondd.respondd_client import ResponddClient as ResponddClient


def main():
    cfg = config.Config.from_dict(config.load_config())
    extResponddClient = ResponddClient(cfg)
    extResponddClient.start()


if __name__ == "__main__":
    main()
