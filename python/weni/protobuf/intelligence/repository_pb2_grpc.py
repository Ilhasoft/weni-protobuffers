# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weni.protobuf.intelligence import repository_pb2 as weni_dot_protobuf_dot_intelligence_dot_repository__pb2


class RepositoryControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/weni.bothub.repository.RepositoryController/List',
                request_serializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryListRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.FromString,
                )
        self.RetrieveAuthorization = channel.unary_unary(
                '/weni.bothub.repository.RepositoryController/RetrieveAuthorization',
                request_serializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryAuthorizationRetrieveRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.FromString,
                )


class RepositoryControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveAuthorization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepositoryControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryListRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.SerializeToString,
            ),
            'RetrieveAuthorization': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveAuthorization,
                    request_deserializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryAuthorizationRetrieveRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.bothub.repository.RepositoryController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RepositoryController(object):
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
        return grpc.experimental.unary_stream(request, target, '/weni.bothub.repository.RepositoryController/List',
            weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryListRequest.SerializeToString,
            weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveAuthorization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.bothub.repository.RepositoryController/RetrieveAuthorization',
            weni_dot_protobuf_dot_intelligence_dot_repository__pb2.RepositoryAuthorizationRetrieveRequest.SerializeToString,
            weni_dot_protobuf_dot_intelligence_dot_repository__pb2.Repository.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
