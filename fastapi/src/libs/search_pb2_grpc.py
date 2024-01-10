# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import search_pb2 as search__pb2


class SearchServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestSearch = channel.unary_unary(
                '/SearchService/RequestSearch',
                request_serializer=search__pb2.Search.SerializeToString,
                response_deserializer=search__pb2.Result.FromString,
                )


class SearchServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RequestSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestSearch,
                    request_deserializer=search__pb2.Search.FromString,
                    response_serializer=search__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SearchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SearchService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RequestSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SearchService/RequestSearch',
            search__pb2.Search.SerializeToString,
            search__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
