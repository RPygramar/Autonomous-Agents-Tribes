import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

import pickle
from algorithm.sarsa import Pessoa


class SenderAgent(Agent):
    class InformBehav(CyclicBehaviour):
        async def run(self):
            msg_body = input("Enter your message (or type 'quit' to stop): ")
            # Create a CustomData object
            data = Pessoa(msg_body, 32)
            serialized_data = pickle.dumps(data)

            if msg_body == "quit":
                await self.agent.stop()
                return

            # print("Sending message:", msg_body)
            msg = Message(to="rpygramar@xmpp.sphincz.ovh")  # Adjust the recipient's address
            msg.set_metadata("performative", "inform")
            # msg.body = msg_body
            # await self.send(msg)
            # print("Message sent!")

            msg.body = serialized_data.hex()  # Convert bytes to hex string for sending
            await self.send(msg)
            print("Serialized object sent!")

    async def setup(self):
        print("SenderAgent started")
        b = self.InformBehav()
        self.add_behaviour(b)


async def main():
    sender_jid = "sphincz@xmpp.sphincz.ovh"  # Replace with the actual JID
    sender_password = "abc123"  # Replace with the actual password
    sender_agent = SenderAgent(sender_jid, sender_password)
    await sender_agent.start(auto_register=True)
    print("Sender started. You can now send messages.")
    await spade.wait_until_finished(sender_agent)


if __name__ == "__main__":
    spade.run(main())
