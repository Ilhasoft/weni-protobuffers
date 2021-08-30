# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.flows import channel_pb2 as weni_dot_protobuf_dot_flows_dot_channel__pb2


class WeniWebChatControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/weni.flows.channel.WeniWebChatController/Create',
                request_serializer=weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChatCreateRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChat.FromString,
                )


class WeniWebChatControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeniWebChatControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChatCreateRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.flows.channel.WeniWebChatController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WeniWebChatController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.flows.channel.WeniWebChatController/Create',
            weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChatCreateRequest.SerializeToString,
            weni_dot_protobuf_dot_flows_dot_channel__pb2.WeniWebChat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
