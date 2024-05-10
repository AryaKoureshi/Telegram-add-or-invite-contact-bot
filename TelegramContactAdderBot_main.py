import vobject
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPhoneContact, InputPeerUser
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError
import asyncio

#%% functions
def extract_contact_info(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        vcard_string = file.read()
        vcard_list = list(vobject.readComponents(vcard_string))
        
        contact_info = []
        for vcard in vcard_list:
            contact = {
                'name': vcard.n.value,
                'num_phone_numbers': vcard.tel.value,
            }
            contact_info.append(contact)
        
        return contact_info

async def add_contact_to_channel(channel_username, contact, api_id, api_hash, phone_number, session_name):
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.start(phone_number)

        channel_entity = await client.get_entity(channel_username)

        new_contact_phone_number = '+98' + contact['num_phone_numbers']
        new_contact_first_name = str(contact['name'])
        new_contact_last_name = ''
        
        contact = InputPhoneContact(
            client_id=0,
            phone=new_contact_phone_number,
            first_name=new_contact_first_name,
            last_name=new_contact_last_name
        )
        
        try:
            result = await client(ImportContactsRequest([contact]))
            if result.imported != []:
                input_peer_user = InputPeerUser(result.users[0].id, result.users[0].access_hash)
                await client(InviteToChannelRequest(channel_entity, [input_peer_user]))
    
                print(f"Successfully added {new_contact_first_name} to the channel.")
            else:
                print(f"Can not add {new_contact_first_name} to the channel.")
                return
        
        except UserPrivacyRestrictedError:
            print(f"Privacy settings don't allow adding {new_contact_first_name} to the channel.")
            return

        await client.disconnect()

#%% parameters
filename = ''
api_id = ''
api_hash = ''
phone_number = '+98'
session_name = ''
channel_username = '@'

#%% main
contacts = extract_contact_info(filename)
for i, contact in enumerate(contacts, start=1):
    print(f"Contact {i}: {contact['name']}")
    print(f"Number of phone numbers: {contact['num_phone_numbers']}")
    print()
    
for contact in contacts:
    asyncio.run(add_contact_to_channel(channel_username, contact, api_id, api_hash, phone_number, session_name))
