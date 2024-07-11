# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/shadowsocks_2022/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.net import network_pb2 as common_dot_net_dot_network__pb2
from xray_api.proto.common.net import address_pb2 as common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proxy/shadowsocks_2022/config.proto\x12\x1bxray.proxy.shadowsocks_2022\x1a\x18\x63ommon/net/network.proto\x1a\x18\x63ommon/net/address.proto\"t\n\x0cServerConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x05\x12)\n\x07network\x18\x05 \x03(\x0e\x32\x18.xray.common.net.Network\"\x91\x01\n\x15MultiUserServerConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x30\n\x05users\x18\x03 \x03(\x0b\x32!.xray.proxy.shadowsocks_2022.User\x12)\n\x07network\x18\x04 \x03(\x0e\x32\x18.xray.common.net.Network\"y\n\x10RelayDestination\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\r\n\x05level\x18\x05 \x01(\x05\"\xa0\x01\n\x11RelayServerConfig\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x43\n\x0c\x64\x65stinations\x18\x03 \x03(\x0b\x32-.xray.proxy.shadowsocks_2022.RelayDestination\x12)\n\x07network\x18\x04 \x03(\x0e\x32\x18.xray.common.net.Network\"1\n\x04User\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\"\x9b\x01\n\x0c\x43lientConfig\x12,\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\x14\n\x0cudp_over_tcp\x18\x05 \x01(\x08\x12\x1c\n\x14udp_over_tcp_version\x18\x06 \x01(\rBr\n\x1f\x63om.xray.proxy.shadowsocks_2022P\x01Z0github.com/xtls/xray-core/proxy/shadowsocks_2022\xaa\x02\x1aXray.Proxy.Shadowsocks2022b\x06proto3')



_SERVERCONFIG = DESCRIPTOR.message_types_by_name['ServerConfig']
_MULTIUSERSERVERCONFIG = DESCRIPTOR.message_types_by_name['MultiUserServerConfig']
_RELAYDESTINATION = DESCRIPTOR.message_types_by_name['RelayDestination']
_RELAYSERVERCONFIG = DESCRIPTOR.message_types_by_name['RelayServerConfig']
_USER = DESCRIPTOR.message_types_by_name['User']
_CLIENTCONFIG = DESCRIPTOR.message_types_by_name['ClientConfig']
ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)

MultiUserServerConfig = _reflection.GeneratedProtocolMessageType('MultiUserServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MULTIUSERSERVERCONFIG,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.MultiUserServerConfig)
  })
_sym_db.RegisterMessage(MultiUserServerConfig)

RelayDestination = _reflection.GeneratedProtocolMessageType('RelayDestination', (_message.Message,), {
  'DESCRIPTOR' : _RELAYDESTINATION,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.RelayDestination)
  })
_sym_db.RegisterMessage(RelayDestination)

RelayServerConfig = _reflection.GeneratedProtocolMessageType('RelayServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _RELAYSERVERCONFIG,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.RelayServerConfig)
  })
_sym_db.RegisterMessage(RelayServerConfig)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.User)
  })
_sym_db.RegisterMessage(User)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.shadowsocks_2022.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.shadowsocks_2022.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.xray.proxy.shadowsocks_2022P\001Z0github.com/xtls/xray-core/proxy/shadowsocks_2022\252\002\032Xray.Proxy.Shadowsocks2022'
  _SERVERCONFIG._serialized_start=120
  _SERVERCONFIG._serialized_end=236
  _MULTIUSERSERVERCONFIG._serialized_start=239
  _MULTIUSERSERVERCONFIG._serialized_end=384
  _RELAYDESTINATION._serialized_start=386
  _RELAYDESTINATION._serialized_end=507
  _RELAYSERVERCONFIG._serialized_start=510
  _RELAYSERVERCONFIG._serialized_end=670
  _USER._serialized_start=672
  _USER._serialized_end=721
  _CLIENTCONFIG._serialized_start=724
  _CLIENTCONFIG._serialized_end=879
# @@protoc_insertion_point(module_scope)
