from telethon.sync import TelegramClient
import asyncio
import vobject

filename = ''
api_id = ''
api_hash = ''

phone_number = '+98'
recipient_number = '+98'

session_name = 'test3'

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
    
async def send_message_to_number(contact_number, api_id, api_hash, phone_number, session_name):
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.start(phone_number)
        message = 'Write_your_message'
        try:
            await client.send_message(contact_number, message)
            print("Message sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        await client.disconnect()

#%% send a message to the recipient_number
asyncio.run(send_message_to_number(recipient_number, api_id, api_hash, phone_number, session_name))

#%% using vcard file
contacts = extract_contact_info(filename)
for i, contact in enumerate(contacts, start=1):
    asyncio.run(send_message_to_number(contact['num_phone_numbers'], api_id, api_hash, phone_number, session_name))