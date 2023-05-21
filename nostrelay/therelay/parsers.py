from datetime import datetime
from therelay.models import Event
from asgiref.sync import sync_to_async

# Wrap the synchronous database operation in sync_to_async
async def save_model_async(model_instance):
    await sync_to_async(model_instance.save)()

async def parse_message(mtype, rest):
	if mtype == "EVENT":
		received_event = dict(rest[0])
		event_id = received_event['id']
		pubkey = received_event['pubkey']
		created_at = datetime.fromtimestamp(received_event['created_at'])
		kind = received_event['kind']
		tags = received_event['tags']
		content = received_event['content']
		sig = received_event['sig']

		event = Event(
		    event_id=event_id,
		    pubkey=pubkey,
		    created_at=created_at,
		    kind=kind,
		    tags=tags,
		    content=content,
		    sig=sig
		)
		await save_model_async(event)

		print(str(mtype) + "------->>>")
		for element in rest:
		  print(element)
		print("\n")
	elif mtype == "REQ":
		print(str(mtype) + "------->>")
		for element in rest:
		  print(element)
		print("\n")
	elif mtype == "CLOSE":
		print(str(mtype) + "<------->")
		for element in rest:
		  print(element)
		print("\n")