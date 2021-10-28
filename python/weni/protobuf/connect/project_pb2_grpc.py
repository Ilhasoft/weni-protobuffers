# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from weni.protobuf.connect import project_pb2 as weni_dot_protobuf_dot_connect_dot_project__pb2


class ProjectControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Classifier = channel.unary_stream(
                '/weni.connect.project.ProjectController/Classifier',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierListRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
                )
        self.CreateClassifier = channel.unary_unary(
                '/weni.connect.project.ProjectController/CreateClassifier',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierCreateRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
                )
        self.CreateChannel = channel.unary_unary(
                '/weni.connect.project.ProjectController/CreateChannel',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelResponse.FromString,
                )
        self.RetrieveClassifier = channel.unary_unary(
                '/weni.connect.project.ProjectController/RetrieveClassifier',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierRetrieveRequest.SerializeToString,
                response_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
                )
        self.DestroyClassifier = channel.unary_unary(
                '/weni.connect.project.ProjectController/DestroyClassifier',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierDestroyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReleaseChannel = channel.unary_unary(
                '/weni.connect.project.ProjectController/ReleaseChannel',
                request_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ReleaseChannelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ProjectControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Classifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateClassifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveClassifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyClassifier(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Classifier': grpc.unary_stream_rpc_method_handler(
                    servicer.Classifier,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierListRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.SerializeToString,
            ),
            'CreateClassifier': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateClassifier,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierCreateRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.SerializeToString,
            ),
            'CreateChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChannel,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelResponse.SerializeToString,
            ),
            'RetrieveClassifier': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveClassifier,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierRetrieveRequest.FromString,
                    response_serializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.SerializeToString,
            ),
            'DestroyClassifier': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyClassifier,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierDestroyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReleaseChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseChannel,
                    request_deserializer=weni_dot_protobuf_dot_connect_dot_project__pb2.ReleaseChannelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weni.connect.project.ProjectController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Classifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/weni.connect.project.ProjectController/Classifier',
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierListRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateClassifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.ProjectController/CreateClassifier',
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierCreateRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.ProjectController/CreateChannel',
            weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_project__pb2.CreateChannelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveClassifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.ProjectController/RetrieveClassifier',
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierRetrieveRequest.SerializeToString,
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyClassifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.ProjectController/DestroyClassifier',
            weni_dot_protobuf_dot_connect_dot_project__pb2.ClassifierDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReleaseChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weni.connect.project.ProjectController/ReleaseChannel',
            weni_dot_protobuf_dot_connect_dot_project__pb2.ReleaseChannelRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
