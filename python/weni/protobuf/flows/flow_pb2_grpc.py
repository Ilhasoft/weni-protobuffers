# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.flows import flow_pb2 as weni_dot_protobuf_dot_flows_dot_flow__pb2


class FlowControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/weni.flows.flow.FlowController/List',
                request_serializer=weni_dot_protobuf_dot_flows_dot_flow__pb2.FlowListRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_flows_dot_flow__pb2.Flow.FromString,
                )


class FlowControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlowControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=weni_dot_protobuf_dot_flows_dot_flow__pb2.FlowListRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_flows_dot_flow__pb2.Flow.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.flows.flow.FlowController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlowController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/weni.flows.flow.FlowController/List',
            weni_dot_protobuf_dot_flows_dot_flow__pb2.FlowListRequest.SerializeToString,
            weni_dot_protobuf_dot_flows_dot_flow__pb2.Flow.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
