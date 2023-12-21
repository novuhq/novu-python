import types
from unittest import TestCase, mock

import pkg_resources

from novu.api import ChangeApi
from novu.config import NovuConfig
from novu.dto.change import ChangeDetailDto, ChangeDto, PaginatedChangeDto
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class ChangeApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = ChangeApi()
        cls.change_response_sample = {
            "data": [
                {
                    "_id": "63dd582b7779f5925855ed77",
                    "enabled": False,
                    "type": "NotificationTemplate",
                    "change": [
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 0],
                            "val": {"name": "kind", "type": "String", "_id": "63dd5ddacac5cff32870270f"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 1],
                            "val": {"name": "start", "type": "String", "_id": "63dd5ddacac5cff328702710"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 2],
                            "val": {"name": "end", "type": "String", "_id": "63dd5ddacac5cff328702711"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 3],
                            "val": {"name": "action", "type": "String", "_id": "63dd5ddacac5cff328702712"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 4],
                            "val": {"name": "sender", "type": "String", "_id": "63dd5ddacac5cff328702713"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 5],
                            "val": {"name": "reimbursment_id", "type": "String", "_id": "63dd5ddacac5cff328702714"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 6],
                            "val": {"name": "firstName", "type": "String", "_id": "63dd5ddacac5cff328702715"},
                        },
                        {
                            "op": "update",
                            "path": ["triggers", 0, "subscriberVariables", 0, "_id"],
                            "val": "63dd5ddacac5cff32870270e",
                            "oldVal": "63daff1a117f8c850991f01c",
                        },
                        {
                            "op": "delete",
                            "path": ["steps", 1, "filters", 0],
                            "oldVal": {"children": [], "_id": "63daff1a117f8c850991f01b"},
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "_templateId"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "_id"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "id"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "add",
                            "path": ["steps", 1, "metadata"],
                            "val": {"amount": 1, "unit": "hours", "type": "regular"},
                        },
                        {
                            "op": "add",
                            "path": ["steps", 2],
                            "val": {
                                "active": True,
                                "shouldStopOnFail": False,
                                "filters": [{"children": [], "_id": "63daff1a117f8c850991f01b"}],
                                "_templateId": "63daff1a117f8c850991f00f",
                                "_parentId": "63dd582b7779f5925855ed8a",
                                "_id": "63daff1a117f8c850991f00f",
                                "id": "63daff1a117f8c850991f00f",
                            },
                        },
                        {
                            "op": "update",
                            "path": ["updatedAt"],
                            "val": "2023-02-03T19:17:46.629Z",
                            "oldVal": "2023-02-02T00:08:58.308Z",
                        },
                    ],
                    "_environmentId": "63dafed97779f59258e38445",
                    "_organizationId": "63dafed97779f59258e3843f",
                    "_entityId": "63dafeec7779f59258e38545",
                    "_creatorId": "63dafed4117f8c850991ec4a",
                    "createdAt": "2023-02-03T18:53:31.742Z",
                    "updatedAt": "2023-02-03T19:17:46.662Z",
                    "__v": 0,
                    "user": {
                        "_id": "63dafed4117f8c850991ec4a",
                        "firstName": "john",
                        "lastName": "doe",
                        "email": "john.doe@novu.com",
                        "profilePicture": "",
                        "showOnBoarding": False,
                        "tokens": [
                            {
                                "providerId": "22155261",
                                "provider": "github",
                                "accessToken": "",
                                "valid": True,
                                "_id": "63dafed4117f8c850991ec4b",
                            }
                        ],
                        "createdAt": "2023-02-02T00:07:48.374Z",
                        "updatedAt": "2023-02-06T22:18:01.399Z",
                        "__v": 0,
                        "id": "63dafed4117f8c850991ec4a",
                    },
                    "id": "63dd582b7779f5925855ed77",
                    "templateId": "63dafeec7779f59258e38545",
                    "templateName": "Transports",
                },
                {
                    "_id": "63de7a275fd0df473167aa30",
                    "enabled": False,
                    "type": "NotificationTemplate",
                    "change": [
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 0],
                            "val": {"name": "kind", "type": "String", "_id": "63dd5ddacac5cff32870270f"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 1],
                            "val": {"name": "start", "type": "String", "_id": "63dd5ddacac5cff328702710"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 2],
                            "val": {"name": "end", "type": "String", "_id": "63dd5ddacac5cff328702711"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 3],
                            "val": {"name": "action", "type": "String", "_id": "63dd5ddacac5cff328702712"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 4],
                            "val": {"name": "sender", "type": "String", "_id": "63dd5ddacac5cff328702713"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 5],
                            "val": {"name": "reimbursment_id", "type": "String", "_id": "63dd5ddacac5cff328702714"},
                        },
                        {
                            "op": "add",
                            "path": ["triggers", 0, "variables", 6],
                            "val": {"name": "firstName", "type": "String", "_id": "63dd5ddacac5cff328702715"},
                        },
                        {
                            "op": "update",
                            "path": ["triggers", 0, "subscriberVariables", 0, "_id"],
                            "val": "63dd5ddacac5cff32870270e",
                            "oldVal": "63daff1a117f8c850991f01c",
                        },
                        {
                            "op": "delete",
                            "path": ["steps", 1, "filters", 0],
                            "oldVal": {"children": [], "_id": "63daff1a117f8c850991f01b"},
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "_templateId"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "_id"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "update",
                            "path": ["steps", 1, "id"],
                            "val": "63dd582b7779f5925855ed8a",
                            "oldVal": "63daff1a117f8c850991f00f",
                        },
                        {
                            "op": "add",
                            "path": ["steps", 1, "metadata"],
                            "val": {"amount": 1, "unit": "hours", "type": "regular"},
                        },
                        {
                            "op": "add",
                            "path": ["steps", 2],
                            "val": {
                                "active": True,
                                "shouldStopOnFail": False,
                                "filters": [{"children": [], "_id": "63daff1a117f8c850991f01b"}],
                                "_templateId": "63daff1a117f8c850991f00f",
                                "_parentId": "63dd582b7779f5925855ed8a",
                                "_id": "63daff1a117f8c850991f00f",
                                "id": "63daff1a117f8c850991f00f",
                            },
                        },
                        {"op": "update", "path": ["deleted"], "val": True, "oldVal": False},
                        {
                            "op": "update",
                            "path": ["updatedAt"],
                            "val": "2023-02-04T15:30:47.973Z",
                            "oldVal": "2023-02-02T00:08:58.308Z",
                        },
                        {"op": "add", "path": ["deletedAt"], "val": "2023-02-04T15:30:47.973Z"},
                    ],
                    "_environmentId": "63dafed97779f59258e38445",
                    "_organizationId": "63dafed97779f59258e3843f",
                    "_entityId": "63dafeec7779f59258e38545",
                    "_creatorId": "63dafed4117f8c850991ec4a",
                    "createdAt": "2023-02-04T15:30:48.043Z",
                    "updatedAt": "2023-02-04T15:30:48.043Z",
                    "__v": 0,
                    "user": {
                        "_id": "63dafed4117f8c850991ec4a",
                        "firstName": "john",
                        "lastName": "doe",
                        "email": "john.doe@novu.com",
                        "profilePicture": "",
                        "showOnBoarding": False,
                        "tokens": [
                            {
                                "providerId": "22155261",
                                "provider": "github",
                                "accessToken": "",
                                "valid": True,
                                "_id": "63dafed4117f8c850991ec4b",
                            }
                        ],
                        "createdAt": "2023-02-02T00:07:48.374Z",
                        "updatedAt": "2023-02-06T22:18:01.399Z",
                        "__v": 0,
                        "id": "63dafed4117f8c850991ec4a",
                    },
                    "id": "63de7a275fd0df473167aa30",
                    "templateId": "63dafeec7779f59258e38545",
                    "templateName": "Transports",
                },
                {
                    "_id": "63e003995fd0df473199a46c",
                    "enabled": False,
                    "type": "Layout",
                    "change": [
                        {"op": "add", "path": ["_id"], "val": "63e003995fd0df473199a468"},
                        {"op": "add", "path": ["_environmentId"], "val": "63dafed97779f59258e38445"},
                        {"op": "add", "path": ["_organizationId"], "val": "63dafed97779f59258e3843f"},
                        {"op": "add", "path": ["_creatorId"], "val": "63dafed4117f8c850991ec4a"},
                        {"op": "add", "path": ["name"], "val": "TEST"},
                        {"op": "add", "path": ["description"], "val": ""},
                        {"op": "add", "path": ["variables"], "val": []},
                        {"op": "add", "path": ["content"], "val": "{{{body}}}"},
                        {"op": "add", "path": ["contentType"], "val": "customHtml"},
                        {"op": "add", "path": ["isDefault"], "val": False},
                        {"op": "add", "path": ["channel"], "val": "email"},
                        {"op": "add", "path": ["deleted"], "val": True},
                        {"op": "add", "path": ["createdAt"], "val": "2023-02-05T19:29:29.096Z"},
                        {"op": "add", "path": ["updatedAt"], "val": "2023-02-05T19:33:10.294Z"},
                        {"op": "add", "path": ["__v"], "val": 0},
                        {"op": "add", "path": ["deletedAt"], "val": "2023-02-05T19:33:10.294Z"},
                        {"op": "add", "path": ["id"], "val": "63e003995fd0df473199a468"},
                        {"op": "add", "path": ["isDeleted"], "val": True},
                    ],
                    "_environmentId": "63dafed97779f59258e38445",
                    "_organizationId": "63dafed97779f59258e3843f",
                    "_entityId": "63e003995fd0df473199a468",
                    "_creatorId": "63dafed4117f8c850991ec4a",
                    "createdAt": "2023-02-05T19:29:29.170Z",
                    "updatedAt": "2023-02-05T19:33:10.366Z",
                    "__v": 0,
                    "user": {
                        "_id": "63dafed4117f8c850991ec4a",
                        "firstName": "john",
                        "lastName": "doe",
                        "email": "john.doe@novu.com",
                        "profilePicture": "",
                        "showOnBoarding": False,
                        "tokens": [
                            {
                                "providerId": "22155261",
                                "provider": "github",
                                "accessToken": "",
                                "valid": True,
                                "_id": "63dafed4117f8c850991ec4b",
                            }
                        ],
                        "createdAt": "2023-02-02T00:07:48.374Z",
                        "updatedAt": "2023-02-06T22:18:01.399Z",
                        "__v": 0,
                        "id": "63dafed4117f8c850991ec4a",
                    },
                    "id": "63e003995fd0df473199a46c",
                    "templateName": "TEST",
                },
                {
                    "_id": "63e59af2105a61b054458218",
                    "enabled": False,
                    "type": "NotificationGroup",
                    "change": [
                        {"op": "add", "path": ["name"], "val": "testing-groups"},
                        {"op": "add", "path": ["_organizationId"], "val": "63dafed97779f59258e3843f"},
                        {"op": "add", "path": ["_environmentId"], "val": "63dafed97779f59258e38445"},
                        {"op": "add", "path": ["_parentId"], "val": "63dafed97779f59258e38449"},
                        {"op": "add", "path": ["_id"], "val": "63e59af2105a61b054458216"},
                        {"op": "add", "path": ["createdAt"], "val": "2023-02-10T01:16:34.455Z"},
                        {"op": "add", "path": ["updatedAt"], "val": "2023-02-10T01:16:34.455Z"},
                        {"op": "add", "path": ["__v"], "val": 0},
                        {"op": "add", "path": ["id"], "val": "63e59af2105a61b054458216"},
                    ],
                    "_environmentId": "63dafed97779f59258e38445",
                    "_organizationId": "63dafed97779f59258e3843f",
                    "_entityId": "63e59af2105a61b054458216",
                    "_creatorId": "63dafed4117f8c850991ec4a",
                    "createdAt": "2023-02-10T01:16:34.527Z",
                    "updatedAt": "2023-02-10T01:16:34.527Z",
                    "__v": 0,
                    "user": {
                        "_id": "63dafed4117f8c850991ec4a",
                        "firstName": "john",
                        "lastName": "doe",
                        "email": "john.doe@novu.com",
                        "profilePicture": "",
                        "showOnBoarding": False,
                        "tokens": [
                            {
                                "providerId": "22155261",
                                "provider": "github",
                                "accessToken": "",
                                "valid": True,
                                "_id": "63dafed4117f8c850991ec4b",
                            }
                        ],
                        "createdAt": "2023-02-02T00:07:48.374Z",
                        "updatedAt": "2023-02-06T22:18:01.399Z",
                        "__v": 0,
                        "id": "63dafed4117f8c850991ec4a",
                    },
                    "id": "63e59af2105a61b054458218",
                    "templateName": "testing-groups",
                },
            ],
            "totalCount": 4,
            "page": 0,
            "pageSize": 10,
        }

        cls.expected_dto = [
            ChangeDto(
                _id="63dd582b7779f5925855ed77",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                _entity_id="63dafeec7779f59258e38545",
                _parent_id=None,
                enabled=False,
                type="NotificationTemplate",
                change=[
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 0],
                        val={"name": "kind", "type": "String", "_id": "63dd5ddacac5cff32870270f"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 1],
                        val={"name": "start", "type": "String", "_id": "63dd5ddacac5cff328702710"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 2],
                        val={"name": "end", "type": "String", "_id": "63dd5ddacac5cff328702711"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 3],
                        val={"name": "action", "type": "String", "_id": "63dd5ddacac5cff328702712"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 4],
                        val={"name": "sender", "type": "String", "_id": "63dd5ddacac5cff328702713"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 5],
                        val={"name": "reimbursment_id", "type": "String", "_id": "63dd5ddacac5cff328702714"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 6],
                        val={"name": "firstName", "type": "String", "_id": "63dd5ddacac5cff328702715"},
                    ),
                    ChangeDetailDto(
                        op="update",
                        path=["triggers", 0, "subscriberVariables", 0, "_id"],
                        val="63dd5ddacac5cff32870270e",
                    ),
                    ChangeDetailDto(op="delete", path=["steps", 1, "filters", 0], val=None),
                    ChangeDetailDto(op="update", path=["steps", 1, "_templateId"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(op="update", path=["steps", 1, "_id"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(op="update", path=["steps", 1, "id"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(
                        op="add", path=["steps", 1, "metadata"], val={"amount": 1, "unit": "hours", "type": "regular"}
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["steps", 2],
                        val={
                            "active": True,
                            "shouldStopOnFail": False,
                            "filters": [{"children": [], "_id": "63daff1a117f8c850991f01b"}],
                            "_templateId": "63daff1a117f8c850991f00f",
                            "_parentId": "63dd582b7779f5925855ed8a",
                            "_id": "63daff1a117f8c850991f00f",
                            "id": "63daff1a117f8c850991f00f",
                        },
                    ),
                    ChangeDetailDto(op="update", path=["updatedAt"], val="2023-02-03T19:17:46.629Z"),
                ],
                created_at="2023-02-03T18:53:31.742Z",
                updated_at="2023-02-03T19:17:46.662Z",
            ),
            ChangeDto(
                _id="63de7a275fd0df473167aa30",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                _entity_id="63dafeec7779f59258e38545",
                _parent_id=None,
                enabled=False,
                type="NotificationTemplate",
                change=[
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 0],
                        val={"name": "kind", "type": "String", "_id": "63dd5ddacac5cff32870270f"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 1],
                        val={"name": "start", "type": "String", "_id": "63dd5ddacac5cff328702710"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 2],
                        val={"name": "end", "type": "String", "_id": "63dd5ddacac5cff328702711"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 3],
                        val={"name": "action", "type": "String", "_id": "63dd5ddacac5cff328702712"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 4],
                        val={"name": "sender", "type": "String", "_id": "63dd5ddacac5cff328702713"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 5],
                        val={"name": "reimbursment_id", "type": "String", "_id": "63dd5ddacac5cff328702714"},
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["triggers", 0, "variables", 6],
                        val={"name": "firstName", "type": "String", "_id": "63dd5ddacac5cff328702715"},
                    ),
                    ChangeDetailDto(
                        op="update",
                        path=["triggers", 0, "subscriberVariables", 0, "_id"],
                        val="63dd5ddacac5cff32870270e",
                    ),
                    ChangeDetailDto(op="delete", path=["steps", 1, "filters", 0], val=None),
                    ChangeDetailDto(op="update", path=["steps", 1, "_templateId"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(op="update", path=["steps", 1, "_id"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(op="update", path=["steps", 1, "id"], val="63dd582b7779f5925855ed8a"),
                    ChangeDetailDto(
                        op="add", path=["steps", 1, "metadata"], val={"amount": 1, "unit": "hours", "type": "regular"}
                    ),
                    ChangeDetailDto(
                        op="add",
                        path=["steps", 2],
                        val={
                            "active": True,
                            "shouldStopOnFail": False,
                            "filters": [{"children": [], "_id": "63daff1a117f8c850991f01b"}],
                            "_templateId": "63daff1a117f8c850991f00f",
                            "_parentId": "63dd582b7779f5925855ed8a",
                            "_id": "63daff1a117f8c850991f00f",
                            "id": "63daff1a117f8c850991f00f",
                        },
                    ),
                    ChangeDetailDto(op="update", path=["deleted"], val=True),
                    ChangeDetailDto(op="update", path=["updatedAt"], val="2023-02-04T15:30:47.973Z"),
                    ChangeDetailDto(op="add", path=["deletedAt"], val="2023-02-04T15:30:47.973Z"),
                ],
                created_at="2023-02-04T15:30:48.043Z",
                updated_at="2023-02-04T15:30:48.043Z",
            ),
            ChangeDto(
                _id="63e003995fd0df473199a46c",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                _entity_id="63e003995fd0df473199a468",
                _parent_id=None,
                enabled=False,
                type="Layout",
                change=[
                    ChangeDetailDto(op="add", path=["_id"], val="63e003995fd0df473199a468"),
                    ChangeDetailDto(op="add", path=["_environmentId"], val="63dafed97779f59258e38445"),
                    ChangeDetailDto(op="add", path=["_organizationId"], val="63dafed97779f59258e3843f"),
                    ChangeDetailDto(op="add", path=["_creatorId"], val="63dafed4117f8c850991ec4a"),
                    ChangeDetailDto(op="add", path=["name"], val="TEST"),
                    ChangeDetailDto(op="add", path=["description"], val=""),
                    ChangeDetailDto(op="add", path=["variables"], val=[]),
                    ChangeDetailDto(op="add", path=["content"], val="{{{body}}}"),
                    ChangeDetailDto(op="add", path=["contentType"], val="customHtml"),
                    ChangeDetailDto(op="add", path=["isDefault"], val=False),
                    ChangeDetailDto(op="add", path=["channel"], val="email"),
                    ChangeDetailDto(op="add", path=["deleted"], val=True),
                    ChangeDetailDto(op="add", path=["createdAt"], val="2023-02-05T19:29:29.096Z"),
                    ChangeDetailDto(op="add", path=["updatedAt"], val="2023-02-05T19:33:10.294Z"),
                    ChangeDetailDto(op="add", path=["__v"], val=0),
                    ChangeDetailDto(op="add", path=["deletedAt"], val="2023-02-05T19:33:10.294Z"),
                    ChangeDetailDto(op="add", path=["id"], val="63e003995fd0df473199a468"),
                    ChangeDetailDto(op="add", path=["isDeleted"], val=True),
                ],
                created_at="2023-02-05T19:29:29.170Z",
                updated_at="2023-02-05T19:33:10.366Z",
            ),
            ChangeDto(
                _id="63e59af2105a61b054458218",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                _entity_id="63e59af2105a61b054458216",
                _parent_id=None,
                enabled=False,
                type="NotificationGroup",
                change=[
                    ChangeDetailDto(op="add", path=["name"], val="testing-groups"),
                    ChangeDetailDto(op="add", path=["_organizationId"], val="63dafed97779f59258e3843f"),
                    ChangeDetailDto(op="add", path=["_environmentId"], val="63dafed97779f59258e38445"),
                    ChangeDetailDto(op="add", path=["_parentId"], val="63dafed97779f59258e38449"),
                    ChangeDetailDto(op="add", path=["_id"], val="63e59af2105a61b054458216"),
                    ChangeDetailDto(op="add", path=["createdAt"], val="2023-02-10T01:16:34.455Z"),
                    ChangeDetailDto(op="add", path=["updatedAt"], val="2023-02-10T01:16:34.455Z"),
                    ChangeDetailDto(op="add", path=["__v"], val=0),
                    ChangeDetailDto(op="add", path=["id"], val="63e59af2105a61b054458216"),
                ],
                created_at="2023-02-10T01:16:34.527Z",
                updated_at="2023-02-10T01:16:34.527Z",
            ),
        ]

    @mock.patch("requests.request")
    def test_list(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.change_response_sample)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedChangeDto)
        self.assertEqual(list(result.data), self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/changes",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"promoted": "false"},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_with_pagination(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.change_response_sample)

        result = self.api.list(1, 10)
        self.assertIsInstance(result, PaginatedChangeDto)
        self.assertEqual(list(result.data), self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/changes",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1, "limit": 10, "promoted": "false"},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_count(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": 4})

        result = self.api.count()
        self.assertEqual(result, 4)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/changes/count",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_apply(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.change_response_sample)

        result = self.api.apply("63e59af2105a61b054458218")
        self.assertIsInstance(result, PaginatedChangeDto)
        self.assertEqual(list(result.data), self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/changes/63e59af2105a61b054458218/apply",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_bulk_apply(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": [
                    [
                        {
                            "_id": "63e003995fd0df473199a46c",
                            "enabled": True,
                            "type": "Layout",
                            "change": [
                                {"op": "add", "path": ["_id"], "val": "63e003995fd0df473199a468"},
                                {"op": "add", "path": ["_environmentId"], "val": "63dafed97779f59258e38445"},
                                {"op": "add", "path": ["_organizationId"], "val": "63dafed97779f59258e3843f"},
                                {"op": "add", "path": ["_creatorId"], "val": "63dafed4117f8c850991ec4a"},
                                {"op": "add", "path": ["name"], "val": "TEST"},
                                {"op": "add", "path": ["description"], "val": ""},
                                {"op": "add", "path": ["variables"], "val": []},
                                {"op": "add", "path": ["content"], "val": "{{{body}}}"},
                                {"op": "add", "path": ["contentType"], "val": "customHtml"},
                                {"op": "add", "path": ["isDefault"], "val": False},
                                {"op": "add", "path": ["channel"], "val": "email"},
                                {"op": "add", "path": ["deleted"], "val": True},
                                {"op": "add", "path": ["createdAt"], "val": "2023-02-05T19:29:29.096Z"},
                                {"op": "add", "path": ["updatedAt"], "val": "2023-02-05T19:33:10.294Z"},
                                {"op": "add", "path": ["__v"], "val": 0},
                                {"op": "add", "path": ["deletedAt"], "val": "2023-02-05T19:33:10.294Z"},
                                {"op": "add", "path": ["id"], "val": "63e003995fd0df473199a468"},
                                {"op": "add", "path": ["isDeleted"], "val": True},
                            ],
                            "_environmentId": "63dafed97779f59258e38445",
                            "_organizationId": "63dafed97779f59258e3843f",
                            "_entityId": "63e003995fd0df473199a468",
                            "_creatorId": "63dafed4117f8c850991ec4a",
                            "createdAt": "2023-02-05T19:29:29.170Z",
                            "updatedAt": "2023-02-10T01:42:10.324Z",
                            "__v": 0,
                            "id": "63e003995fd0df473199a46c",
                        }
                    ],
                    [
                        {
                            "_id": "63e59af2105a61b054458218",
                            "enabled": False,
                            "type": "NotificationGroup",
                            "change": [
                                {"op": "add", "path": ["name"], "val": "testing-groups"},
                                {"op": "add", "path": ["_organizationId"], "val": "63dafed97779f59258e3843f"},
                                {"op": "add", "path": ["_environmentId"], "val": "63dafed97779f59258e38445"},
                                {"op": "add", "path": ["_parentId"], "val": "63dafed97779f59258e38449"},
                                {"op": "add", "path": ["_id"], "val": "63e59af2105a61b054458216"},
                                {"op": "add", "path": ["createdAt"], "val": "2023-02-10T01:16:34.455Z"},
                                {"op": "add", "path": ["updatedAt"], "val": "2023-02-10T01:16:34.455Z"},
                                {"op": "add", "path": ["__v"], "val": 0},
                                {"op": "add", "path": ["id"], "val": "63e59af2105a61b054458216"},
                            ],
                            "_environmentId": "63dafed97779f59258e38445",
                            "_organizationId": "63dafed97779f59258e3843f",
                            "_entityId": "63e59af2105a61b054458216",
                            "_creatorId": "63dafed4117f8c850991ec4a",
                            "createdAt": "2023-02-10T01:16:34.527Z",
                            "updatedAt": "2023-02-10T01:16:34.527Z",
                            "__v": 0,
                            "id": "63e59af2105a61b054458218",
                        }
                    ],
                ]
            },
        )

        result = self.api.bulk_apply(["63e59af2105a61b054458218", "63e003995fd0df473199a46c"])
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(
            list(result),
            [
                ChangeDto(
                    _id="63e003995fd0df473199a46c",
                    _environment_id="63dafed97779f59258e38445",
                    _organization_id="63dafed97779f59258e3843f",
                    _entity_id="63e003995fd0df473199a468",
                    _parent_id=None,
                    enabled=True,
                    type="Layout",
                    change=[
                        ChangeDetailDto(op="add", path=["_id"], val="63e003995fd0df473199a468"),
                        ChangeDetailDto(op="add", path=["_environmentId"], val="63dafed97779f59258e38445"),
                        ChangeDetailDto(op="add", path=["_organizationId"], val="63dafed97779f59258e3843f"),
                        ChangeDetailDto(op="add", path=["_creatorId"], val="63dafed4117f8c850991ec4a"),
                        ChangeDetailDto(op="add", path=["name"], val="TEST"),
                        ChangeDetailDto(op="add", path=["description"], val=""),
                        ChangeDetailDto(op="add", path=["variables"], val=[]),
                        ChangeDetailDto(op="add", path=["content"], val="{{{body}}}"),
                        ChangeDetailDto(op="add", path=["contentType"], val="customHtml"),
                        ChangeDetailDto(op="add", path=["isDefault"], val=False),
                        ChangeDetailDto(op="add", path=["channel"], val="email"),
                        ChangeDetailDto(op="add", path=["deleted"], val=True),
                        ChangeDetailDto(op="add", path=["createdAt"], val="2023-02-05T19:29:29.096Z"),
                        ChangeDetailDto(op="add", path=["updatedAt"], val="2023-02-05T19:33:10.294Z"),
                        ChangeDetailDto(op="add", path=["__v"], val=0),
                        ChangeDetailDto(op="add", path=["deletedAt"], val="2023-02-05T19:33:10.294Z"),
                        ChangeDetailDto(op="add", path=["id"], val="63e003995fd0df473199a468"),
                        ChangeDetailDto(op="add", path=["isDeleted"], val=True),
                    ],
                    created_at="2023-02-05T19:29:29.170Z",
                    updated_at="2023-02-10T01:42:10.324Z",
                ),
                ChangeDto(
                    _id="63e59af2105a61b054458218",
                    _environment_id="63dafed97779f59258e38445",
                    _organization_id="63dafed97779f59258e3843f",
                    _entity_id="63e59af2105a61b054458216",
                    _parent_id=None,
                    enabled=False,
                    type="NotificationGroup",
                    change=[
                        ChangeDetailDto(op="add", path=["name"], val="testing-groups"),
                        ChangeDetailDto(op="add", path=["_organizationId"], val="63dafed97779f59258e3843f"),
                        ChangeDetailDto(op="add", path=["_environmentId"], val="63dafed97779f59258e38445"),
                        ChangeDetailDto(op="add", path=["_parentId"], val="63dafed97779f59258e38449"),
                        ChangeDetailDto(op="add", path=["_id"], val="63e59af2105a61b054458216"),
                        ChangeDetailDto(op="add", path=["createdAt"], val="2023-02-10T01:16:34.455Z"),
                        ChangeDetailDto(op="add", path=["updatedAt"], val="2023-02-10T01:16:34.455Z"),
                        ChangeDetailDto(op="add", path=["__v"], val=0),
                        ChangeDetailDto(op="add", path=["id"], val="63e59af2105a61b054458216"),
                    ],
                    created_at="2023-02-10T01:16:34.527Z",
                    updated_at="2023-02-10T01:16:34.527Z",
                ),
            ],
        )

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/changes/bulk/apply",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"changeIds": ["63e59af2105a61b054458218", "63e003995fd0df473199a46c"]},
            params=None,
            timeout=5,
        )
