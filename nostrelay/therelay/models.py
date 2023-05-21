from django.db import models

class User(models.Model):
    pubkey = models.CharField(max_length=64)
    	# "pubkey": <32-bytes lowercase hex-encoded public key of the event creator>,

class Message(models.Model):
    type = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey('therelay.User', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        abstract = True  # Make Message an abstract base class
    
class Event(Message):
    event_id = models.CharField(max_length=64)
		# "id": <32-bytes lowercase hex-encoded sha256 of the serialized event data>
    pubkey = models.CharField(max_length=64)
		# "pubkey": <32-bytes lowercase hex-encoded public key of the event creator>,
    created_at = models.DateTimeField()
		# "created_at": <unix timestamp in seconds>,
    kind = models.IntegerField()
		# "kind": <integer>,
    tags = models.TextField()
		# "tags": [
		#   ["e", <32-bytes hex of the id of another event>, <recommended relay URL>],
		#   ["p", <32-bytes hex of a pubkey>, <recommended relay URL>],
		#   ... // other kinds of tags may be included later
		# ],
    content = models.TextField()
		# "content": <arbitrary string>,
    sig = models.TextField()
		# "sig": <64-bytes hex of the signature of the sha256 hash of the serialized event data, which is the same as the "id" field>

class Filter(models.Model):
    filter_id = models.CharField(max_length=64)
    
class EtagPositional(models.Model):
    resolution = models.TextField()
    
class EtagMarked(models.Model):
    resolution = models.TextField()
    
class Ptag(models.Model):
    resolution = models.TextField()

class Req(Message):
    title = models.CharField(max_length=100)
    
class Close(Message):
    resolution = models.TextField()

