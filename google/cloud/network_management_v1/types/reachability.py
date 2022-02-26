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

from google.cloud.network_management_v1.types import connectivity_test
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.networkmanagement.v1",
    manifest={
        "ListConnectivityTestsRequest",
        "ListConnectivityTestsResponse",
        "GetConnectivityTestRequest",
        "CreateConnectivityTestRequest",
        "UpdateConnectivityTestRequest",
        "DeleteConnectivityTestRequest",
        "RerunConnectivityTestRequest",
        "OperationMetadata",
    },
)


class ListConnectivityTestsRequest(proto.Message):
    r"""Request for the ``ListConnectivityTests`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the Connectivity Tests:
            ``projects/{project_id}/locations/global``
        page_size (int):
            Number of ``ConnectivityTests`` to return.
        page_token (str):
            Page token from an earlier query, as returned in
            ``next_page_token``.
        filter (str):
            Lists the ``ConnectivityTests`` that match the filter
            expression. A filter expression filters the resources listed
            in the response. The expression must be of the form
            ``<field> <operator> <value>`` where operators: ``<``,
            ``>``, ``<=``, ``>=``, ``!=``, ``=``, ``:`` are supported
            (colon ``:`` represents a HAS operator which is roughly
            synonymous with equality). can refer to a proto or JSON
            field, or a synthetic field. Field names can be camelCase or
            snake_case.

            Examples:

            -  Filter by name: name =
               "projects/proj-1/locations/global/connectivityTests/test-1

            -  Filter by labels:

               -  Resources that have a key called ``foo`` labels.foo:\*
               -  Resources that have a key called ``foo`` whose value
                  is ``bar`` labels.foo = bar
        order_by (str):
            Field to use to sort the list.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)
    order_by = proto.Field(proto.STRING, number=5,)


class ListConnectivityTestsResponse(proto.Message):
    r"""Response for the ``ListConnectivityTests`` method.

    Attributes:
        resources (Sequence[google.cloud.network_management_v1.types.ConnectivityTest]):
            List of Connectivity Tests.
        next_page_token (str):
            Page token to fetch the next set of
            Connectivity Tests.
        unreachable (Sequence[str]):
            Locations that could not be reached (when querying all
            locations with ``-``).
    """

    @property
    def raw_page(self):
        return self

    resources = proto.RepeatedField(
        proto.MESSAGE, number=1, message=connectivity_test.ConnectivityTest,
    )
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable = proto.RepeatedField(proto.STRING, number=3,)


class GetConnectivityTestRequest(proto.Message):
    r"""Request for the ``GetConnectivityTest`` method.

    Attributes:
        name (str):
            Required. ``ConnectivityTest`` resource name using the form:
            ``projects/{project_id}/locations/global/connectivityTests/{test_id}``
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateConnectivityTestRequest(proto.Message):
    r"""Request for the ``CreateConnectivityTest`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the Connectivity Test to
            create: ``projects/{project_id}/locations/global``
        test_id (str):
            Required. The logical name of the Connectivity Test in your
            project with the following restrictions:

            -  Must contain only lowercase letters, numbers, and
               hyphens.
            -  Must start with a letter.
            -  Must be between 1-40 characters.
            -  Must end with a number or a letter.
            -  Must be unique within the customer project
        resource (google.cloud.network_management_v1.types.ConnectivityTest):
            Required. A ``ConnectivityTest`` resource
    """

    parent = proto.Field(proto.STRING, number=1,)
    test_id = proto.Field(proto.STRING, number=2,)
    resource = proto.Field(
        proto.MESSAGE, number=3, message=connectivity_test.ConnectivityTest,
    )


class UpdateConnectivityTestRequest(proto.Message):
    r"""Request for the ``UpdateConnectivityTest`` method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least
            one path must be supplied in this field.
        resource (google.cloud.network_management_v1.types.ConnectivityTest):
            Required. Only fields specified in update_mask are updated.
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=1, message=field_mask_pb2.FieldMask,
    )
    resource = proto.Field(
        proto.MESSAGE, number=2, message=connectivity_test.ConnectivityTest,
    )


class DeleteConnectivityTestRequest(proto.Message):
    r"""Request for the ``DeleteConnectivityTest`` method.

    Attributes:
        name (str):
            Required. Connectivity Test resource name using the form:
            ``projects/{project_id}/locations/global/connectivityTests/{test_id}``
    """

    name = proto.Field(proto.STRING, number=1,)


class RerunConnectivityTestRequest(proto.Message):
    r"""Request for the ``RerunConnectivityTest`` method.

    Attributes:
        name (str):
            Required. Connectivity Test resource name using the form:
            ``projects/{project_id}/locations/global/connectivityTests/{test_id}``
    """

    name = proto.Field(proto.STRING, number=1,)


class OperationMetadata(proto.Message):
    r"""Metadata describing an [Operation][google.longrunning.Operation]

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Target of the operation - for example
            projects/project-1/locations/global/connectivityTests/test-1
        verb (str):
            Name of the verb executed by the operation.
        status_detail (str):
            Human-readable status of the operation, if
            any.
        cancel_requested (bool):
            Specifies if cancellation was requested for
            the operation.
        api_version (str):
            API version.
    """

    create_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    target = proto.Field(proto.STRING, number=3,)
    verb = proto.Field(proto.STRING, number=4,)
    status_detail = proto.Field(proto.STRING, number=5,)
    cancel_requested = proto.Field(proto.BOOL, number=6,)
    api_version = proto.Field(proto.STRING, number=7,)


__all__ = tuple(sorted(__protobuf__.manifest))
