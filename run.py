import sys, os
sys.path.append(os.pardir)

from service import websocket_subscribe_service

if __name__ == "__main__":
    websocket_subscribe_service.start()