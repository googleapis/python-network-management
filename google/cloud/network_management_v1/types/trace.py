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


__protobuf__ = proto.module(
    package="google.cloud.networkmanagement.v1",
    manifest={
        "Trace",
        "Step",
        "InstanceInfo",
        "NetworkInfo",
        "FirewallInfo",
        "RouteInfo",
        "ForwardingRuleInfo",
        "LoadBalancerInfo",
        "LoadBalancerBackend",
        "VpnGatewayInfo",
        "VpnTunnelInfo",
        "EndpointInfo",
        "DeliverInfo",
        "ForwardInfo",
        "AbortInfo",
        "DropInfo",
        "GKEMasterInfo",
        "CloudSQLInstanceInfo",
    },
)


class Trace(proto.Message):
    r"""Trace represents one simulated packet forwarding path.

    -  Each trace contains multiple ordered steps.
    -  Each step is in a particular state with associated configuration.
    -  State is categorized as final or non-final states.
    -  Each final state has a reason associated.
    -  Each trace must end with a final state (the last step).

    ::

         |---------------------Trace----------------------|
         Step1(State) Step2(State) ---  StepN(State(final))

    Attributes:
        endpoint_info (google.cloud.network_management_v1.types.EndpointInfo):
            Derived from the source and destination endpoints definition
            specified by user request, and validated by the data plane
            model. If there are multiple traces starting from different
            source locations, then the endpoint_info may be different
            between traces.
        steps (Sequence[google.cloud.network_management_v1.types.Step]):
            A trace of a test contains multiple steps
            from the initial state to the final state
            (delivered, dropped, forwarded, or aborted).
            The steps are ordered by the processing sequence
            within the simulated network state machine. It
            is critical to preserve the order of the steps
            and avoid reordering or sorting them.
    """

    endpoint_info = proto.Field(proto.MESSAGE, number=1, message="EndpointInfo",)
    steps = proto.RepeatedField(proto.MESSAGE, number=2, message="Step",)


class Step(proto.Message):
    r"""A simulated forwarding path is composed of multiple steps.
    Each step has a well-defined state and an associated
    configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            A description of the step. Usually this is a
            summary of the state.
        state (google.cloud.network_management_v1.types.Step.State):
            Each step is in one of the pre-defined
            states.
        causes_drop (bool):
            This is a step that leads to the final state
            Drop.
        project_id (str):
            Project ID that contains the configuration
            this step is validating.
        instance (google.cloud.network_management_v1.types.InstanceInfo):
            Display information of a Compute Engine
            instance.

            This field is a member of `oneof`_ ``step_info``.
        firewall (google.cloud.network_management_v1.types.FirewallInfo):
            Display information of a Compute Engine
            firewall rule.

            This field is a member of `oneof`_ ``step_info``.
        route (google.cloud.network_management_v1.types.RouteInfo):
            Display information of a Compute Engine
            route.

            This field is a member of `oneof`_ ``step_info``.
        endpoint (google.cloud.network_management_v1.types.EndpointInfo):
            Display information of the source and
            destination under analysis. The endpoint
            information in an intermediate state may differ
            with the initial input, as it might be modified
            by state like NAT, or Connection Proxy.

            This field is a member of `oneof`_ ``step_info``.
        forwarding_rule (google.cloud.network_management_v1.types.ForwardingRuleInfo):
            Display information of a Compute Engine
            forwarding rule.

            This field is a member of `oneof`_ ``step_info``.
        vpn_gateway (google.cloud.network_management_v1.types.VpnGatewayInfo):
            Display information of a Compute Engine VPN
            gateway.

            This field is a member of `oneof`_ ``step_info``.
        vpn_tunnel (google.cloud.network_management_v1.types.VpnTunnelInfo):
            Display information of a Compute Engine VPN
            tunnel.

            This field is a member of `oneof`_ ``step_info``.
        deliver (google.cloud.network_management_v1.types.DeliverInfo):
            Display information of the final state
            "deliver" and reason.

            This field is a member of `oneof`_ ``step_info``.
        forward (google.cloud.network_management_v1.types.ForwardInfo):
            Display information of the final state
            "forward" and reason.

            This field is a member of `oneof`_ ``step_info``.
        abort (google.cloud.network_management_v1.types.AbortInfo):
            Display information of the final state
            "abort" and reason.

            This field is a member of `oneof`_ ``step_info``.
        drop (google.cloud.network_management_v1.types.DropInfo):
            Display information of the final state "drop"
            and reason.

            This field is a member of `oneof`_ ``step_info``.
        load_balancer (google.cloud.network_management_v1.types.LoadBalancerInfo):
            Display information of the load balancers.

            This field is a member of `oneof`_ ``step_info``.
        network (google.cloud.network_management_v1.types.NetworkInfo):
            Display information of a Google Cloud
            network.

            This field is a member of `oneof`_ ``step_info``.
        gke_master (google.cloud.network_management_v1.types.GKEMasterInfo):
            Display information of a Google Kubernetes
            Engine cluster master.

            This field is a member of `oneof`_ ``step_info``.
        cloud_sql_instance (google.cloud.network_management_v1.types.CloudSQLInstanceInfo):
            Display information of a Cloud SQL instance.

            This field is a member of `oneof`_ ``step_info``.
    """

    class State(proto.Enum):
        r"""Type of states that are defined in the network state machine.
        Each step in the packet trace is in a specific state.
        """
        STATE_UNSPECIFIED = 0
        START_FROM_INSTANCE = 1
        START_FROM_INTERNET = 2
        START_FROM_PRIVATE_NETWORK = 3
        START_FROM_GKE_MASTER = 21
        START_FROM_CLOUD_SQL_INSTANCE = 22
        APPLY_INGRESS_FIREWALL_RULE = 4
        APPLY_EGRESS_FIREWALL_RULE = 5
        APPLY_ROUTE = 6
        APPLY_FORWARDING_RULE = 7
        SPOOFING_APPROVED = 8
        ARRIVE_AT_INSTANCE = 9
        ARRIVE_AT_INTERNAL_LOAD_BALANCER = 10
        ARRIVE_AT_EXTERNAL_LOAD_BALANCER = 11
        ARRIVE_AT_VPN_GATEWAY = 12
        ARRIVE_AT_VPN_TUNNEL = 13
        NAT = 14
        PROXY_CONNECTION = 15
        DELIVER = 16
        DROP = 17
        FORWARD = 18
        ABORT = 19
        VIEWER_PERMISSION_MISSING = 20

    description = proto.Field(proto.STRING, number=1,)
    state = proto.Field(proto.ENUM, number=2, enum=State,)
    causes_drop = proto.Field(proto.BOOL, number=3,)
    project_id = proto.Field(proto.STRING, number=4,)
    instance = proto.Field(
        proto.MESSAGE, number=5, oneof="step_info", message="InstanceInfo",
    )
    firewall = proto.Field(
        proto.MESSAGE, number=6, oneof="step_info", message="FirewallInfo",
    )
    route = proto.Field(
        proto.MESSAGE, number=7, oneof="step_info", message="RouteInfo",
    )
    endpoint = proto.Field(
        proto.MESSAGE, number=8, oneof="step_info", message="EndpointInfo",
    )
    forwarding_rule = proto.Field(
        proto.MESSAGE, number=9, oneof="step_info", message="ForwardingRuleInfo",
    )
    vpn_gateway = proto.Field(
        proto.MESSAGE, number=10, oneof="step_info", message="VpnGatewayInfo",
    )
    vpn_tunnel = proto.Field(
        proto.MESSAGE, number=11, oneof="step_info", message="VpnTunnelInfo",
    )
    deliver = proto.Field(
        proto.MESSAGE, number=12, oneof="step_info", message="DeliverInfo",
    )
    forward = proto.Field(
        proto.MESSAGE, number=13, oneof="step_info", message="ForwardInfo",
    )
    abort = proto.Field(
        proto.MESSAGE, number=14, oneof="step_info", message="AbortInfo",
    )
    drop = proto.Field(proto.MESSAGE, number=15, oneof="step_info", message="DropInfo",)
    load_balancer = proto.Field(
        proto.MESSAGE, number=16, oneof="step_info", message="LoadBalancerInfo",
    )
    network = proto.Field(
        proto.MESSAGE, number=17, oneof="step_info", message="NetworkInfo",
    )
    gke_master = proto.Field(
        proto.MESSAGE, number=18, oneof="step_info", message="GKEMasterInfo",
    )
    cloud_sql_instance = proto.Field(
        proto.MESSAGE, number=19, oneof="step_info", message="CloudSQLInstanceInfo",
    )


class InstanceInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    instance.

    Attributes:
        display_name (str):
            Name of a Compute Engine instance.
        uri (str):
            URI of a Compute Engine instance.
        interface (str):
            Name of the network interface of a Compute
            Engine instance.
        network_uri (str):
            URI of a Compute Engine network.
        internal_ip (str):
            Internal IP address of the network interface.
        external_ip (str):
            External IP address of the network interface.
        network_tags (Sequence[str]):
            Network tags configured on the instance.
        service_account (str):
            Service account authorized for the instance.
    """

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    interface = proto.Field(proto.STRING, number=3,)
    network_uri = proto.Field(proto.STRING, number=4,)
    internal_ip = proto.Field(proto.STRING, number=5,)
    external_ip = proto.Field(proto.STRING, number=6,)
    network_tags = proto.RepeatedField(proto.STRING, number=7,)
    service_account = proto.Field(proto.STRING, number=8,)


class NetworkInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    network.

    Attributes:
        display_name (str):
            Name of a Compute Engine network.
        uri (str):
            URI of a Compute Engine network.
        matched_ip_range (str):
            The IP range that matches the test.
    """

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    matched_ip_range = proto.Field(proto.STRING, number=4,)


class FirewallInfo(proto.Message):
    r"""For display only. Metadata associated with a VPC firewall
    rule, an implied VPC firewall rule, or a hierarchical firewall
    policy rule.

    Attributes:
        display_name (str):
            The display name of the VPC firewall rule.
            This field is not applicable to hierarchical
            firewall policy rules.
        uri (str):
            The URI of the VPC firewall rule. This field
            is not applicable to implied firewall rules or
            hierarchical firewall policy rules.
        direction (str):
            Possible values: INGRESS, EGRESS
        action (str):
            Possible values: ALLOW, DENY
        priority (int):
            The priority of the firewall rule.
        network_uri (str):
            The URI of the VPC network that the firewall
            rule is associated with. This field is not
            applicable to hierarchical firewall policy
            rules.
        target_tags (Sequence[str]):
            The target tags defined by the VPC firewall
            rule. This field is not applicable to
            hierarchical firewall policy rules.
        target_service_accounts (Sequence[str]):
            The target service accounts specified by the
            firewall rule.
        policy (str):
            The hierarchical firewall policy that this
            rule is associated with. This field is not
            applicable to VPC firewall rules.
        firewall_rule_type (google.cloud.network_management_v1.types.FirewallInfo.FirewallRuleType):
            The firewall rule's type.
    """

    class FirewallRuleType(proto.Enum):
        r"""The firewall rule's type."""
        FIREWALL_RULE_TYPE_UNSPECIFIED = 0
        HIERARCHICAL_FIREWALL_POLICY_RULE = 1
        VPC_FIREWALL_RULE = 2
        IMPLIED_VPC_FIREWALL_RULE = 3

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    direction = proto.Field(proto.STRING, number=3,)
    action = proto.Field(proto.STRING, number=4,)
    priority = proto.Field(proto.INT32, number=5,)
    network_uri = proto.Field(proto.STRING, number=6,)
    target_tags = proto.RepeatedField(proto.STRING, number=7,)
    target_service_accounts = proto.RepeatedField(proto.STRING, number=8,)
    policy = proto.Field(proto.STRING, number=9,)
    firewall_rule_type = proto.Field(proto.ENUM, number=10, enum=FirewallRuleType,)


class RouteInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    route.

    Attributes:
        route_type (google.cloud.network_management_v1.types.RouteInfo.RouteType):
            Type of route.
        next_hop_type (google.cloud.network_management_v1.types.RouteInfo.NextHopType):
            Type of next hop.
        display_name (str):
            Name of a Compute Engine route.
        uri (str):
            URI of a Compute Engine route.
            Dynamic route from cloud router does not have a
            URI. Advertised route from Google Cloud VPC to
            on-premises network also does not have a URI.
        dest_ip_range (str):
            Destination IP range of the route.
        next_hop (str):
            Next hop of the route.
        network_uri (str):
            URI of a Compute Engine network.
        priority (int):
            Priority of the route.
        instance_tags (Sequence[str]):
            Instance tags of the route.
    """

    class RouteType(proto.Enum):
        r"""Type of route:"""
        ROUTE_TYPE_UNSPECIFIED = 0
        SUBNET = 1
        STATIC = 2
        DYNAMIC = 3
        PEERING_SUBNET = 4
        PEERING_STATIC = 5
        PEERING_DYNAMIC = 6

    class NextHopType(proto.Enum):
        r"""Type of next hop:"""
        NEXT_HOP_TYPE_UNSPECIFIED = 0
        NEXT_HOP_IP = 1
        NEXT_HOP_INSTANCE = 2
        NEXT_HOP_NETWORK = 3
        NEXT_HOP_PEERING = 4
        NEXT_HOP_INTERCONNECT = 5
        NEXT_HOP_VPN_TUNNEL = 6
        NEXT_HOP_VPN_GATEWAY = 7
        NEXT_HOP_INTERNET_GATEWAY = 8
        NEXT_HOP_BLACKHOLE = 9
        NEXT_HOP_ILB = 10

    route_type = proto.Field(proto.ENUM, number=8, enum=RouteType,)
    next_hop_type = proto.Field(proto.ENUM, number=9, enum=NextHopType,)
    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    dest_ip_range = proto.Field(proto.STRING, number=3,)
    next_hop = proto.Field(proto.STRING, number=4,)
    network_uri = proto.Field(proto.STRING, number=5,)
    priority = proto.Field(proto.INT32, number=6,)
    instance_tags = proto.RepeatedField(proto.STRING, number=7,)


class ForwardingRuleInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    forwarding rule.

    Attributes:
        display_name (str):
            Name of a Compute Engine forwarding rule.
        uri (str):
            URI of a Compute Engine forwarding rule.
        matched_protocol (str):
            Protocol defined in the forwarding rule that
            matches the test.
        matched_port_range (str):
            Port range defined in the forwarding rule
            that matches the test.
        vip (str):
            VIP of the forwarding rule.
        target (str):
            Target type of the forwarding rule.
        network_uri (str):
            Network URI. Only valid for Internal Load
            Balancer.
    """

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    matched_protocol = proto.Field(proto.STRING, number=3,)
    matched_port_range = proto.Field(proto.STRING, number=6,)
    vip = proto.Field(proto.STRING, number=4,)
    target = proto.Field(proto.STRING, number=5,)
    network_uri = proto.Field(proto.STRING, number=7,)


class LoadBalancerInfo(proto.Message):
    r"""For display only. Metadata associated with a load balancer.

    Attributes:
        load_balancer_type (google.cloud.network_management_v1.types.LoadBalancerInfo.LoadBalancerType):
            Type of the load balancer.
        health_check_uri (str):
            URI of the health check for the load
            balancer.
        backends (Sequence[google.cloud.network_management_v1.types.LoadBalancerBackend]):
            Information for the loadbalancer backends.
        backend_type (google.cloud.network_management_v1.types.LoadBalancerInfo.BackendType):
            Type of load balancer's backend
            configuration.
        backend_uri (str):
            Backend configuration URI.
    """

    class LoadBalancerType(proto.Enum):
        r"""The type definition for a load balancer:"""
        LOAD_BALANCER_TYPE_UNSPECIFIED = 0
        INTERNAL_TCP_UDP = 1
        NETWORK_TCP_UDP = 2
        HTTP_PROXY = 3
        TCP_PROXY = 4
        SSL_PROXY = 5

    class BackendType(proto.Enum):
        r"""The type definition for a load balancer backend
        configuration:
        """
        BACKEND_TYPE_UNSPECIFIED = 0
        BACKEND_SERVICE = 1
        TARGET_POOL = 2

    load_balancer_type = proto.Field(proto.ENUM, number=1, enum=LoadBalancerType,)
    health_check_uri = proto.Field(proto.STRING, number=2,)
    backends = proto.RepeatedField(
        proto.MESSAGE, number=3, message="LoadBalancerBackend",
    )
    backend_type = proto.Field(proto.ENUM, number=4, enum=BackendType,)
    backend_uri = proto.Field(proto.STRING, number=5,)


class LoadBalancerBackend(proto.Message):
    r"""For display only. Metadata associated with a specific load
    balancer backend.

    Attributes:
        display_name (str):
            Name of a Compute Engine instance or network
            endpoint.
        uri (str):
            URI of a Compute Engine instance or network
            endpoint.
        health_check_firewall_state (google.cloud.network_management_v1.types.LoadBalancerBackend.HealthCheckFirewallState):
            State of the health check firewall
            configuration.
        health_check_allowing_firewall_rules (Sequence[str]):
            A list of firewall rule URIs allowing probes
            from health check IP ranges.
        health_check_blocking_firewall_rules (Sequence[str]):
            A list of firewall rule URIs blocking probes
            from health check IP ranges.
    """

    class HealthCheckFirewallState(proto.Enum):
        r"""State of a health check firewall configuration:"""
        HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED = 0
        CONFIGURED = 1
        MISCONFIGURED = 2

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    health_check_firewall_state = proto.Field(
        proto.ENUM, number=3, enum=HealthCheckFirewallState,
    )
    health_check_allowing_firewall_rules = proto.RepeatedField(proto.STRING, number=4,)
    health_check_blocking_firewall_rules = proto.RepeatedField(proto.STRING, number=5,)


class VpnGatewayInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    VPN gateway.

    Attributes:
        display_name (str):
            Name of a VPN gateway.
        uri (str):
            URI of a VPN gateway.
        network_uri (str):
            URI of a Compute Engine network where the VPN
            gateway is configured.
        ip_address (str):
            IP address of the VPN gateway.
        vpn_tunnel_uri (str):
            A VPN tunnel that is associated with this VPN
            gateway. There may be multiple VPN tunnels
            configured on a VPN gateway, and only the one
            relevant to the test is displayed.
        region (str):
            Name of a Google Cloud region where this VPN
            gateway is configured.
    """

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    network_uri = proto.Field(proto.STRING, number=3,)
    ip_address = proto.Field(proto.STRING, number=4,)
    vpn_tunnel_uri = proto.Field(proto.STRING, number=5,)
    region = proto.Field(proto.STRING, number=6,)


class VpnTunnelInfo(proto.Message):
    r"""For display only. Metadata associated with a Compute Engine
    VPN tunnel.

    Attributes:
        display_name (str):
            Name of a VPN tunnel.
        uri (str):
            URI of a VPN tunnel.
        source_gateway (str):
            URI of the VPN gateway at local end of the
            tunnel.
        remote_gateway (str):
            URI of a VPN gateway at remote end of the
            tunnel.
        remote_gateway_ip (str):
            Remote VPN gateway's IP address.
        source_gateway_ip (str):
            Local VPN gateway's IP address.
        network_uri (str):
            URI of a Compute Engine network where the VPN
            tunnel is configured.
        region (str):
            Name of a Google Cloud region where this VPN
            tunnel is configured.
        routing_type (google.cloud.network_management_v1.types.VpnTunnelInfo.RoutingType):
            Type of the routing policy.
    """

    class RoutingType(proto.Enum):
        r"""Types of VPN routing policy. For details, refer to `Networks and
        Tunnel
        routing <https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing/>`__.
        """
        ROUTING_TYPE_UNSPECIFIED = 0
        ROUTE_BASED = 1
        POLICY_BASED = 2
        DYNAMIC = 3

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    source_gateway = proto.Field(proto.STRING, number=3,)
    remote_gateway = proto.Field(proto.STRING, number=4,)
    remote_gateway_ip = proto.Field(proto.STRING, number=5,)
    source_gateway_ip = proto.Field(proto.STRING, number=6,)
    network_uri = proto.Field(proto.STRING, number=7,)
    region = proto.Field(proto.STRING, number=8,)
    routing_type = proto.Field(proto.ENUM, number=9, enum=RoutingType,)


class EndpointInfo(proto.Message):
    r"""For display only. The specification of the endpoints for the
    test. EndpointInfo is derived from source and destination
    Endpoint and validated by the backend data plane model.

    Attributes:
        source_ip (str):
            Source IP address.
        destination_ip (str):
            Destination IP address.
        protocol (str):
            IP protocol in string format, for example:
            "TCP", "UDP", "ICMP".
        source_port (int):
            Source port. Only valid when protocol is TCP
            or UDP.
        destination_port (int):
            Destination port. Only valid when protocol is
            TCP or UDP.
        source_network_uri (str):
            URI of the network where this packet
            originates from.
        destination_network_uri (str):
            URI of the network where this packet is sent
            to.
    """

    source_ip = proto.Field(proto.STRING, number=1,)
    destination_ip = proto.Field(proto.STRING, number=2,)
    protocol = proto.Field(proto.STRING, number=3,)
    source_port = proto.Field(proto.INT32, number=4,)
    destination_port = proto.Field(proto.INT32, number=5,)
    source_network_uri = proto.Field(proto.STRING, number=6,)
    destination_network_uri = proto.Field(proto.STRING, number=7,)


class DeliverInfo(proto.Message):
    r"""Details of the final state "deliver" and associated resource.

    Attributes:
        target (google.cloud.network_management_v1.types.DeliverInfo.Target):
            Target type where the packet is delivered to.
        resource_uri (str):
            URI of the resource that the packet is
            delivered to.
    """

    class Target(proto.Enum):
        r"""Deliver target types:"""
        TARGET_UNSPECIFIED = 0
        INSTANCE = 1
        INTERNET = 2
        GOOGLE_API = 3
        GKE_MASTER = 4
        CLOUD_SQL_INSTANCE = 5

    target = proto.Field(proto.ENUM, number=1, enum=Target,)
    resource_uri = proto.Field(proto.STRING, number=2,)


class ForwardInfo(proto.Message):
    r"""Details of the final state "forward" and associated resource.

    Attributes:
        target (google.cloud.network_management_v1.types.ForwardInfo.Target):
            Target type where this packet is forwarded
            to.
        resource_uri (str):
            URI of the resource that the packet is
            forwarded to.
    """

    class Target(proto.Enum):
        r"""Forward target types."""
        TARGET_UNSPECIFIED = 0
        PEERING_VPC = 1
        VPN_GATEWAY = 2
        INTERCONNECT = 3
        GKE_MASTER = 4
        IMPORTED_CUSTOM_ROUTE_NEXT_HOP = 5
        CLOUD_SQL_INSTANCE = 6

    target = proto.Field(proto.ENUM, number=1, enum=Target,)
    resource_uri = proto.Field(proto.STRING, number=2,)


class AbortInfo(proto.Message):
    r"""Details of the final state "abort" and associated resource.

    Attributes:
        cause (google.cloud.network_management_v1.types.AbortInfo.Cause):
            Causes that the analysis is aborted.
        resource_uri (str):
            URI of the resource that caused the abort.
    """

    class Cause(proto.Enum):
        r"""Abort cause types:"""
        CAUSE_UNSPECIFIED = 0
        UNKNOWN_NETWORK = 1
        UNKNOWN_IP = 2
        UNKNOWN_PROJECT = 3
        PERMISSION_DENIED = 4
        NO_SOURCE_LOCATION = 5
        INVALID_ARGUMENT = 6
        NO_EXTERNAL_IP = 7
        UNINTENDED_DESTINATION = 8
        TRACE_TOO_LONG = 9
        INTERNAL_ERROR = 10
        SOURCE_ENDPOINT_NOT_FOUND = 11
        MISMATCHED_SOURCE_NETWORK = 12
        DESTINATION_ENDPOINT_NOT_FOUND = 13
        MISMATCHED_DESTINATION_NETWORK = 14

    cause = proto.Field(proto.ENUM, number=1, enum=Cause,)
    resource_uri = proto.Field(proto.STRING, number=2,)


class DropInfo(proto.Message):
    r"""Details of the final state "drop" and associated resource.

    Attributes:
        cause (google.cloud.network_management_v1.types.DropInfo.Cause):
            Cause that the packet is dropped.
        resource_uri (str):
            URI of the resource that caused the drop.
    """

    class Cause(proto.Enum):
        r"""Drop cause types:"""
        CAUSE_UNSPECIFIED = 0
        UNKNOWN_EXTERNAL_ADDRESS = 1
        FOREIGN_IP_DISALLOWED = 2
        FIREWALL_RULE = 3
        NO_ROUTE = 4
        ROUTE_BLACKHOLE = 5
        ROUTE_WRONG_NETWORK = 6
        PRIVATE_TRAFFIC_TO_INTERNET = 7
        PRIVATE_GOOGLE_ACCESS_DISALLOWED = 8
        NO_EXTERNAL_ADDRESS = 9
        UNKNOWN_INTERNAL_ADDRESS = 10
        FORWARDING_RULE_MISMATCH = 11
        FORWARDING_RULE_NO_INSTANCES = 12
        FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK = 13
        INSTANCE_NOT_RUNNING = 14
        TRAFFIC_TYPE_BLOCKED = 15
        GKE_MASTER_UNAUTHORIZED_ACCESS = 16
        CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS = 17
        DROPPED_INSIDE_GKE_SERVICE = 18
        DROPPED_INSIDE_CLOUD_SQL_SERVICE = 19
        GOOGLE_MANAGED_SERVICE_NO_PEERING = 20
        CLOUD_SQL_INSTANCE_NO_IP_ADDRESS = 21

    cause = proto.Field(proto.ENUM, number=1, enum=Cause,)
    resource_uri = proto.Field(proto.STRING, number=2,)


class GKEMasterInfo(proto.Message):
    r"""For display only. Metadata associated with a Google
    Kubernetes Engine (GKE) cluster master.

    Attributes:
        cluster_uri (str):
            URI of a GKE cluster.
        cluster_network_uri (str):
            URI of a GKE cluster network.
        internal_ip (str):
            Internal IP address of a GKE cluster master.
        external_ip (str):
            External IP address of a GKE cluster master.
    """

    cluster_uri = proto.Field(proto.STRING, number=2,)
    cluster_network_uri = proto.Field(proto.STRING, number=4,)
    internal_ip = proto.Field(proto.STRING, number=5,)
    external_ip = proto.Field(proto.STRING, number=6,)


class CloudSQLInstanceInfo(proto.Message):
    r"""For display only. Metadata associated with a Cloud SQL
    instance.

    Attributes:
        display_name (str):
            Name of a Cloud SQL instance.
        uri (str):
            URI of a Cloud SQL instance.
        network_uri (str):
            URI of a Cloud SQL instance network or empty
            string if the instance does not have one.
        internal_ip (str):
            Internal IP address of a Cloud SQL instance.
        external_ip (str):
            External IP address of a Cloud SQL instance.
        region (str):
            Region in which the Cloud SQL instance is
            running.
    """

    display_name = proto.Field(proto.STRING, number=1,)
    uri = proto.Field(proto.STRING, number=2,)
    network_uri = proto.Field(proto.STRING, number=4,)
    internal_ip = proto.Field(proto.STRING, number=5,)
    external_ip = proto.Field(proto.STRING, number=6,)
    region = proto.Field(proto.STRING, number=7,)


__all__ = tuple(sorted(__protobuf__.manifest))
