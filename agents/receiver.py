import pickle

import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template


class ReceiverAgent(Agent):
    class RecvBehav(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)  # Adjust the timeout as needed
            if msg:
                # print("Message received with content:", msg.body)
                # Convert the hex string back to bytes and deserialize
                received_data_bytes = bytes.fromhex(msg.body)
                received_data = pickle.loads(received_data_bytes)

                print("Received object:", received_data)
            else:
                print("Waiting for a message...")

    async def setup(self):
        print("ReceiverAgent started")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


async def main():
    receiver_jid = "rpygramar@xmpp.sphincz.ovh"  # Replace with the actual JID
    receiver_password = "abc123"  # Replace with the actual password
    receiver_agent = ReceiverAgent(receiver_jid, receiver_password)
    await receiver_agent.start(auto_register=True)
    print("Receiver started. Awaiting messages...")
    await spade.wait_until_finished(receiver_agent)


if __name__ == "__main__":
    spade.run(main())
