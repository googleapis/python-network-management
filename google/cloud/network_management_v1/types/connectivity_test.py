# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.cloud.network_management_v1.types import trace
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.networkmanagement.v1",
    manifest={"ConnectivityTest", "Endpoint", "ReachabilityDetails",},
)


class ConnectivityTest(proto.Message):
    r"""A Connectivity Test for a network reachability analysis.

    Attributes:
        name (str):
            Required. Unique name of the resource using the form:
            ``projects/{project_id}/locations/global/connectivityTests/{test_id}``
        description (str):
            The user-supplied description of the
            Connectivity Test. Maximum of 512 characters.
        source (google.cloud.network_management_v1.types.Endpoint):
            Required. Source specification of the
            Connectivity Test.
            You can use a combination of source IP address,
            virtual machine (VM) instance, or Compute Engine
            network to uniquely identify the source
            location.

            Examples:
            If the source IP address is an internal IP
            address within a Google Cloud Virtual Private
            Cloud (VPC) network, then you must also specify
            the VPC network. Otherwise, specify the VM
            instance, which already contains its internal IP
            address and VPC network information.
            If the source of the test is within an
            on-premises network, then you must provide the
            destination VPC network.

            If the source endpoint is a Compute Engine VM
            instance with multiple network interfaces, the
            instance itself is not sufficient to identify
            the endpoint. So, you must also specify the
            source IP address or VPC network.
            A reachability analysis proceeds even if the
            source location is ambiguous. However, the test
            result may include endpoints that you don't
            intend to test.
        destination (google.cloud.network_management_v1.types.Endpoint):
            Required. Destination specification of the
            Connectivity Test.
            You can use a combination of destination IP
            address, Compute Engine VM instance, or VPC
            network to uniquely identify the destination
            location.

            Even if the destination IP address is not
            unique, the source IP location is unique.
            Usually, the analysis can infer the destination
            endpoint from route information.

            If the destination you specify is a VM instance
            and the instance has multiple network
            interfaces, then you must also specify either a
            destination IP address  or VPC network to
            identify the destination interface.

            A reachability analysis proceeds even if the
            destination location is ambiguous. However, the
            result can include endpoints that you don't
            intend to test.
        protocol (str):
            IP Protocol of the test. When not provided,
            "TCP" is assumed.
        related_projects (Sequence[str]):
            Other projects that may be relevant for
            reachability analysis. This is applicable to
            scenarios where a test can cross project
            boundaries.
        display_name (str):
            Output only. The display name of a
            Connectivity Test.
        labels (Sequence[google.cloud.network_management_v1.types.ConnectivityTest.LabelsEntry]):
            Resource labels to represent user-provided
            metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the test was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the test's
            configuration was updated.
        reachability_details (google.cloud.network_management_v1.types.ReachabilityDetails):
            Output only. The reachability details of this
            test from the latest run. The details are
            updated when creating a new test, updating an
            existing test, or triggering a one-time rerun of
            an existing test.
    """

    name = proto.Field(proto.STRING, number=1,)
    description = proto.Field(proto.STRING, number=2,)
    source = proto.Field(proto.MESSAGE, number=3, message="Endpoint",)
    destination = proto.Field(proto.MESSAGE, number=4, message="Endpoint",)
    protocol = proto.Field(proto.STRING, number=5,)
    related_projects = proto.RepeatedField(proto.STRING, number=6,)
    display_name = proto.Field(proto.STRING, number=7,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=8,)
    create_time = proto.Field(
        proto.MESSAGE, number=10, message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE, number=11, message=timestamp_pb2.Timestamp,
    )
    reachability_details = proto.Field(
        proto.MESSAGE, number=12, message="ReachabilityDetails",
    )


class Endpoint(proto.Message):
    r"""Source or destination of the Connectivity Test.

    Attributes:
        ip_address (str):
            The IP address of the endpoint, which can be an external or
            internal IP. An IPv6 address is only allowed when the test's
            destination is a `global load balancer
            VIP </load-balancing/docs/load-balancing-overview>`__.
        port (int):
            The IP protocol port of the endpoint.
            Only applicable when protocol is TCP or UDP.
        instance (str):
            A Compute Engine instance URI.
        gke_master_cluster (str):
            A cluster URI for `Google Kubernetes Engine
            master <https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture>`__.
        cloud_sql_instance (str):
            A `Cloud SQL <https://cloud.google.com/sql>`__ instance URI.
        network (str):
            A Compute Engine network URI.
        network_type (google.cloud.network_management_v1.types.Endpoint.NetworkType):
            Type of the network where the endpoint is
            located. Applicable only to source endpoint, as
            destination network type can be inferred from
            the source.
        project_id (str):
            Project ID where the endpoint is located.
            The Project ID can be derived from the URI if
            you provide a VM instance or network URI.
            The following are two cases where you must
            provide the project ID: 1. Only the IP address
            is specified, and the IP address is within a GCP
            project.
            2. When you are using Shared VPC and the IP
            address that you provide is from the service
            project. In this case, the network that the IP
            address resides in is defined in the host
            project.
    """

    class NetworkType(proto.Enum):
        r"""The type definition of an endpoint's network. Use one of the
        following choices:
        """
        NETWORK_TYPE_UNSPECIFIED = 0
        GCP_NETWORK = 1
        NON_GCP_NETWORK = 2

    ip_address = proto.Field(proto.STRING, number=1,)
    port = proto.Field(proto.INT32, number=2,)
    instance = proto.Field(proto.STRING, number=3,)
    gke_master_cluster = proto.Field(proto.STRING, number=7,)
    cloud_sql_instance = proto.Field(proto.STRING, number=8,)
    network = proto.Field(proto.STRING, number=4,)
    network_type = proto.Field(proto.ENUM, number=5, enum=NetworkType,)
    project_id = proto.Field(proto.STRING, number=6,)


class ReachabilityDetails(proto.Message):
    r"""Results of the configuration analysis from the last run of
    the test.

    Attributes:
        result (google.cloud.network_management_v1.types.ReachabilityDetails.Result):
            The overall result of the test's
            configuration analysis.
        verify_time (google.protobuf.timestamp_pb2.Timestamp):
            The time of the configuration analysis.
        error (google.rpc.status_pb2.Status):
            The details of a failure or a cancellation of
            reachability analysis.
        traces (Sequence[google.cloud.network_management_v1.types.Trace]):
            Result may contain a list of traces if a test
            has multiple possible paths in the network, such
            as when destination endpoint is a load balancer
            with multiple backends.
    """

    class Result(proto.Enum):
        r"""The overall result of the test's configuration analysis."""
        RESULT_UNSPECIFIED = 0
        REACHABLE = 1
        UNREACHABLE = 2
        AMBIGUOUS = 4
        UNDETERMINED = 5

    result = proto.Field(proto.ENUM, number=1, enum=Result,)
    verify_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    error = proto.Field(proto.MESSAGE, number=3, message=status_pb2.Status,)
    traces = proto.RepeatedField(proto.MESSAGE, number=5, message=trace.Trace,)


__all__ = tuple(sorted(__protobuf__.manifest))
