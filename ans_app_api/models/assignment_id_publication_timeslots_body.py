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

class AssignmentIdPublicationTimeslotsBody(object):
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
        'allow_discussions': 'bool',
        'discussion_start_datetime': 'str',
        'discussion_end_datetime': 'str',
        'group_id': 'int',
        'klass_id': 'int',
        'notify_students': 'bool',
        'publish_start_datetime': 'str',
        'publish_end_datetime': 'str',
        'with_extra_time': 'bool'
    }

    attribute_map = {
        'allow_discussions': 'allow_discussions',
        'discussion_start_datetime': 'discussion_start_datetime',
        'discussion_end_datetime': 'discussion_end_datetime',
        'group_id': 'group_id',
        'klass_id': 'klass_id',
        'notify_students': 'notify_students',
        'publish_start_datetime': 'publish_start_datetime',
        'publish_end_datetime': 'publish_end_datetime',
        'with_extra_time': 'with_extra_time'
    }

    def __init__(self, allow_discussions=True, discussion_start_datetime=None, discussion_end_datetime=None, group_id=None, klass_id=None, notify_students=False, publish_start_datetime=None, publish_end_datetime=None, with_extra_time=False):  # noqa: E501
        """AssignmentIdPublicationTimeslotsBody - a model defined in Swagger"""  # noqa: E501
        self._allow_discussions = None
        self._discussion_start_datetime = None
        self._discussion_end_datetime = None
        self._group_id = None
        self._klass_id = None
        self._notify_students = None
        self._publish_start_datetime = None
        self._publish_end_datetime = None
        self._with_extra_time = None
        self.discriminator = None
        if allow_discussions is not None:
            self.allow_discussions = allow_discussions
        if discussion_start_datetime is not None:
            self.discussion_start_datetime = discussion_start_datetime
        if discussion_end_datetime is not None:
            self.discussion_end_datetime = discussion_end_datetime
        if group_id is not None:
            self.group_id = group_id
        if klass_id is not None:
            self.klass_id = klass_id
        if notify_students is not None:
            self.notify_students = notify_students
        if publish_start_datetime is not None:
            self.publish_start_datetime = publish_start_datetime
        if publish_end_datetime is not None:
            self.publish_end_datetime = publish_end_datetime
        if with_extra_time is not None:
            self.with_extra_time = with_extra_time

    @property
    def allow_discussions(self):
        """Gets the allow_discussions of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        Defines whether discussions will be allowed  # noqa: E501

        :return: The allow_discussions of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: bool
        """
        return self._allow_discussions

    @allow_discussions.setter
    def allow_discussions(self, allow_discussions):
        """Sets the allow_discussions of this AssignmentIdPublicationTimeslotsBody.

        Defines whether discussions will be allowed  # noqa: E501

        :param allow_discussions: The allow_discussions of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: bool
        """

        self._allow_discussions = allow_discussions

    @property
    def discussion_start_datetime(self):
        """Gets the discussion_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The date and time after which discussions will be allowed  # noqa: E501

        :return: The discussion_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: str
        """
        return self._discussion_start_datetime

    @discussion_start_datetime.setter
    def discussion_start_datetime(self, discussion_start_datetime):
        """Sets the discussion_start_datetime of this AssignmentIdPublicationTimeslotsBody.

        The date and time after which discussions will be allowed  # noqa: E501

        :param discussion_start_datetime: The discussion_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: str
        """

        self._discussion_start_datetime = discussion_start_datetime

    @property
    def discussion_end_datetime(self):
        """Gets the discussion_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The date and time after which discussions will no longer be allowed  # noqa: E501

        :return: The discussion_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: str
        """
        return self._discussion_end_datetime

    @discussion_end_datetime.setter
    def discussion_end_datetime(self, discussion_end_datetime):
        """Sets the discussion_end_datetime of this AssignmentIdPublicationTimeslotsBody.

        The date and time after which discussions will no longer be allowed  # noqa: E501

        :param discussion_end_datetime: The discussion_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: str
        """

        self._discussion_end_datetime = discussion_end_datetime

    @property
    def group_id(self):
        """Gets the group_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The id of the group for this publication timeslot  # noqa: E501

        :return: The group_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AssignmentIdPublicationTimeslotsBody.

        The id of the group for this publication timeslot  # noqa: E501

        :param group_id: The group_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def klass_id(self):
        """Gets the klass_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The id of the klass for this publication timeslot  # noqa: E501

        :return: The klass_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: int
        """
        return self._klass_id

    @klass_id.setter
    def klass_id(self, klass_id):
        """Sets the klass_id of this AssignmentIdPublicationTimeslotsBody.

        The id of the klass for this publication timeslot  # noqa: E501

        :param klass_id: The klass_id of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: int
        """

        self._klass_id = klass_id

    @property
    def notify_students(self):
        """Gets the notify_students of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        When enabled notifies the students when the publication timeslot will be active  # noqa: E501

        :return: The notify_students of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: bool
        """
        return self._notify_students

    @notify_students.setter
    def notify_students(self, notify_students):
        """Sets the notify_students of this AssignmentIdPublicationTimeslotsBody.

        When enabled notifies the students when the publication timeslot will be active  # noqa: E501

        :param notify_students: The notify_students of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: bool
        """

        self._notify_students = notify_students

    @property
    def publish_start_datetime(self):
        """Gets the publish_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The start date and time for the publication  # noqa: E501

        :return: The publish_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: str
        """
        return self._publish_start_datetime

    @publish_start_datetime.setter
    def publish_start_datetime(self, publish_start_datetime):
        """Sets the publish_start_datetime of this AssignmentIdPublicationTimeslotsBody.

        The start date and time for the publication  # noqa: E501

        :param publish_start_datetime: The publish_start_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: str
        """

        self._publish_start_datetime = publish_start_datetime

    @property
    def publish_end_datetime(self):
        """Gets the publish_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        The end date and time for the publication  # noqa: E501

        :return: The publish_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: str
        """
        return self._publish_end_datetime

    @publish_end_datetime.setter
    def publish_end_datetime(self, publish_end_datetime):
        """Sets the publish_end_datetime of this AssignmentIdPublicationTimeslotsBody.

        The end date and time for the publication  # noqa: E501

        :param publish_end_datetime: The publish_end_datetime of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: str
        """

        self._publish_end_datetime = publish_end_datetime

    @property
    def with_extra_time(self):
        """Gets the with_extra_time of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501

        Enables extra time for the publication timeslot  # noqa: E501

        :return: The with_extra_time of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :rtype: bool
        """
        return self._with_extra_time

    @with_extra_time.setter
    def with_extra_time(self, with_extra_time):
        """Sets the with_extra_time of this AssignmentIdPublicationTimeslotsBody.

        Enables extra time for the publication timeslot  # noqa: E501

        :param with_extra_time: The with_extra_time of this AssignmentIdPublicationTimeslotsBody.  # noqa: E501
        :type: bool
        """

        self._with_extra_time = with_extra_time

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
        if issubclass(AssignmentIdPublicationTimeslotsBody, dict):
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
        if not isinstance(other, AssignmentIdPublicationTimeslotsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
