# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simpleServer_pb2 as simpleServer__pb2


class SimpleServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Service = channel.unary_unary(
        '/simpleServer.SimpleServer/Service',
        request_serializer=simpleServer__pb2.SimpleServerRequest.SerializeToString,
        response_deserializer=simpleServer__pb2.SimpleServerResponse.FromString,
        )


class SimpleServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Service(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimpleServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Service': grpc.unary_unary_rpc_method_handler(
          servicer.Service,
          request_deserializer=simpleServer__pb2.SimpleServerRequest.FromString,
          response_serializer=simpleServer__pb2.SimpleServerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'simpleServer.SimpleServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
