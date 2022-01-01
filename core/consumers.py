import json
from channels.generic.websocket import WebsocketConsumer,AsyncConsumer,SyncConsumer
from asgiref.sync import async_to_sync


# *********************TO PRACTISE SYNCCONSUMER
# class TestConsumer(SyncConsumer):
#     # ws://
#     def websocket_connect(self,event):
#         print("Connected")
#
#     def websocket_receive(self,event):
#         print("Received")
#
#     def websocket_disconnect(self,event):
#         print("Disconnected")
#
#
#
# class EchoConsumer(WebsocketConsumer):
#     # ws://
#     def connect(self):
#         self.room_name = "test_consumer"
#         self.room_group_name = "test_consumer_group"
#
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_name, self.room_group_name
#         )
#         self.accept()
#         self.send(text_data=json.dumps({'status':'connected'}))
#
#     def receive(self,text_data):
#         print("Received")
#         self.send(text_data=json.dumps({"status":"We got you"}))
#
#     def disconnect(self,event):
#         pass



class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected", event)

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnect", event)
