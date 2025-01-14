# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08\x61i.proto\x12\x0cgoogle.reply\"G\n\x0cReplyRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12(\n\x06status\x18\x02 \x01(\x0e\x32\x18.google.reply.StatusCode\"J\n\rReplyResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12(\n\x06status\x18\x02 \x01(\x0e\x32\x18.google.reply.StatusCode*\xa2\x02\n\nStatusCode\x12\x07\n\x03\x45RR\x10\x00\x12\x11\n\rUNRAG_REQUEST\x10\x01\x12\x0f\n\x0bRAG_REQUEST\x10\x02\x12\x19\n\x15\x44\x45\x43RYPTED_RAG_REQUEST\x10\x03\x12!\n\x1dPRIVATE_AGENT_RETRIVE_REQUEST\x10\x04\x12\x1d\n\x19PRIVATE_AGENT_LLM_REQUEST\x10\x05\x12\'\n#PRICATE_AGENT_ENCRYPTED_LLM_REQUEST\x10\x06\x12\x1d\n\x19PUBLIC_AGENT_LLM_RESPONSE\x10\x07\x12&\n\"PUBLIC_AGENT_ENCYPTED_LLM_RESPONSE\x10\x08\x12\x1a\n\x16PRIVATE_AGENT_RESPONSE\x10\t2U\n\x0cReplyService\x12\x45\n\x08GetReply\x12\x1a.google.reply.ReplyRequest\x1a\x1b.google.reply.ReplyResponse\"\x00\x62\x06proto3')

_STATUSCODE = DESCRIPTOR.enum_types_by_name['StatusCode']
StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
ERR = 0
UNRAG_REQUEST = 1
RAG_REQUEST = 2
DECRYPTED_RAG_REQUEST = 3
PRIVATE_AGENT_RETRIVE_REQUEST = 4
PRIVATE_AGENT_LLM_REQUEST = 5
PRICATE_AGENT_ENCRYPTED_LLM_REQUEST = 6
PUBLIC_AGENT_LLM_RESPONSE = 7
PUBLIC_AGENT_ENCYPTED_LLM_RESPONSE = 8
PRIVATE_AGENT_RESPONSE = 9


_REPLYREQUEST = DESCRIPTOR.message_types_by_name['ReplyRequest']
_REPLYRESPONSE = DESCRIPTOR.message_types_by_name['ReplyResponse']
ReplyRequest = _reflection.GeneratedProtocolMessageType('ReplyRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPLYREQUEST,
  '__module__' : 'ai_pb2'
  # @@protoc_insertion_point(class_scope:google.reply.ReplyRequest)
  })
_sym_db.RegisterMessage(ReplyRequest)

ReplyResponse = _reflection.GeneratedProtocolMessageType('ReplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPLYRESPONSE,
  '__module__' : 'ai_pb2'
  # @@protoc_insertion_point(class_scope:google.reply.ReplyResponse)
  })
_sym_db.RegisterMessage(ReplyResponse)

_REPLYSERVICE = DESCRIPTOR.services_by_name['ReplyService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUSCODE._serialized_start=176
  _STATUSCODE._serialized_end=466
  _REPLYREQUEST._serialized_start=26
  _REPLYREQUEST._serialized_end=97
  _REPLYRESPONSE._serialized_start=99
  _REPLYRESPONSE._serialized_end=173
  _REPLYSERVICE._serialized_start=468
  _REPLYSERVICE._serialized_end=553
# @@protoc_insertion_point(module_scope)
