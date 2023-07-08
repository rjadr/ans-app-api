# coding: utf-8

"""
    API V2

    #### Authorization The API can only be accessed by creating a token at: [https://ans.app/users/tokens](https://ans.app/users/tokens).<br> The provided token is a Bearer token and needs to be set in the Request Header with key Authorization and value \"Bearer [token]\" for every request.<br>  #### Pagination The API generates several headers due to its use of pagination, this includes:      - Link, the standard link header defined in RFC 8288     - Current-Page, which shows the current page of the requested data     - Page-Items, which shows the amount of items per page     - Total-Pages, which shows the total amount of pages available     - Total-Count, which shows the total count of objects that was requested  #### Rate Limits The API enforces a rate limit of 500 request per minute per ip-address. If the rate limit is exceeded, the API responds with a HTTP 429 Too Many Requests response code.<br> You can use the following response headers to confirm the current rate limit and monitor the number of requests remaining in the current minute.<br>      - RateLimit-Limit, the current limit for your account     - RateLimit-Remaining, the number of remaining requests in the current minute     - RateLimit-Reset, the number of seconds until the limit is reset  #### Search The API offers search functionality through GET requests with a query. For all search endpoints see the [Search](#/Search) section.<br>      - The query must consist of the attribute and the search value connected with a colon (:) or a greater than (>) or smaller than (<) sign.     - You can use the greater and smaller than symbols for numeric and date values.     - If your search value contains whitespaces, you must quote your search query with single or double quotes.     - You can also combine searches by using a whitespace to separate the attributes.     - If your search value is equal to \"null\", all records with null values for that attribute will be found.     - We perform case sensitive exact match searches only.     - You can search for multiple values, by adding square brackets around the search parameters and seperating the parameters using commas without spaces.     - You can see some example queries in the documented search endpoints.   #### Webhooks The API offers you the ability to listen to specific events that occur within the application. For example, you can use webhooks to:      - Archive results when an assignment is archived     - Add users after an assignment is created     - Export a result after it has been approved  When creating a webhook you can specify which events you want to listen to. You can listen to all events, all events for a specific object or only one event for an object.<br> You can listen to 'create', 'update' and 'destroy' events on an object or a combination for example:      - '*' - all events for all objects     - 'assignment' - All events for an assignment     - 'assignment.update' - Only notify when an assignment is updated  The webhooks API returns a secret after creating a new webhook. This secret can be used to verify that the webhook call comes from Ans by creating a sha256 HMAC with the request body and this secret and comparing it to the X-Ans-Signature Header.<br>  Webhook requests are automatically retried up to five times if the endpoint returns certain HTTP response codes. The time interval between retries is gradually extended. Every webhook event is logged and contains the response code, headers and body of the response for debugging purposes.<br>  The following objects are currently supported:      - Assignment     - Result     - User   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'config_keys': 'list[int]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'config_keys': 'config_keys'
    }

    def __init__(self, enabled=False, config_keys=None):  # noqa: E501
        """Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._config_keys = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if config_keys is not None:
            self.config_keys = config_keys

    @property
    def enabled(self):
        """Gets the enabled of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501

        Enables the Safe Exam Browser Server integration  # noqa: E501

        :return: The enabled of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.

        Enables the Safe Exam Browser Server integration  # noqa: E501

        :param enabled: The enabled of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def config_keys(self):
        """Gets the config_keys of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501

        Lockdown browser hash to sha256 with the request url and is compared to the configKeyHash sent in the request headers  # noqa: E501

        :return: The config_keys of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501
        :rtype: list[int]
        """
        return self._config_keys

    @config_keys.setter
    def config_keys(self, config_keys):
        """Sets the config_keys of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.

        Lockdown browser hash to sha256 with the request url and is compared to the configKeyHash sent in the request headers  # noqa: E501

        :param config_keys: The config_keys of this Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer.  # noqa: E501
        :type: list[int]
        """

        self._config_keys = config_keys

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other