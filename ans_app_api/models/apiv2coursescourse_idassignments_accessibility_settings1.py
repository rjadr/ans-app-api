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

class Apiv2coursescourseIdassignmentsAccessibilitySettings1(object):
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
        'attempts': 'int',
        'password': 'str',
        'restricted_access_to_other_pages': 'bool',
        'restricted_ip_access': 'bool',
        'location_ids': 'list[int]',
        'notes': 'bool',
        'spellchecker': 'bool',
        'config_keys': 'list[int]',
        'calculator': 'OneOfapiv2coursescourseIdassignmentsAccessibilitySettings1Calculator',
        'feedback': 'bool',
        'forced_test_navigation': 'bool',
        'cannot_reopen_question_groups': 'bool',
        'seb_server_enabled': 'bool'
    }

    attribute_map = {
        'attempts': 'attempts',
        'password': 'password',
        'restricted_access_to_other_pages': 'restricted_access_to_other_pages',
        'restricted_ip_access': 'restricted_ip_access',
        'location_ids': 'location_ids',
        'notes': 'notes',
        'spellchecker': 'spellchecker',
        'config_keys': 'config_keys',
        'calculator': 'calculator',
        'feedback': 'feedback',
        'forced_test_navigation': 'forced_test_navigation',
        'cannot_reopen_question_groups': 'cannot_reopen_question_groups',
        'seb_server_enabled': 'seb_server_enabled'
    }

    def __init__(self, attempts=None, password=None, restricted_access_to_other_pages=None, restricted_ip_access=None, location_ids=None, notes=None, spellchecker=None, config_keys=None, calculator=None, feedback=None, forced_test_navigation=None, cannot_reopen_question_groups=None, seb_server_enabled=None):  # noqa: E501
        """Apiv2coursescourseIdassignmentsAccessibilitySettings1 - a model defined in Swagger"""  # noqa: E501
        self._attempts = None
        self._password = None
        self._restricted_access_to_other_pages = None
        self._restricted_ip_access = None
        self._location_ids = None
        self._notes = None
        self._spellchecker = None
        self._config_keys = None
        self._calculator = None
        self._feedback = None
        self._forced_test_navigation = None
        self._cannot_reopen_question_groups = None
        self._seb_server_enabled = None
        self.discriminator = None
        if attempts is not None:
            self.attempts = attempts
        if password is not None:
            self.password = password
        if restricted_access_to_other_pages is not None:
            self.restricted_access_to_other_pages = restricted_access_to_other_pages
        if restricted_ip_access is not None:
            self.restricted_ip_access = restricted_ip_access
        if location_ids is not None:
            self.location_ids = location_ids
        if notes is not None:
            self.notes = notes
        if spellchecker is not None:
            self.spellchecker = spellchecker
        if config_keys is not None:
            self.config_keys = config_keys
        if calculator is not None:
            self.calculator = calculator
        if feedback is not None:
            self.feedback = feedback
        if forced_test_navigation is not None:
            self.forced_test_navigation = forced_test_navigation
        if cannot_reopen_question_groups is not None:
            self.cannot_reopen_question_groups = cannot_reopen_question_groups
        if seb_server_enabled is not None:
            self.seb_server_enabled = seb_server_enabled

    @property
    def attempts(self):
        """Gets the attempts of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        The amount of attempts students get to take the assignment  # noqa: E501

        :return: The attempts of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: int
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """Sets the attempts of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        The amount of attempts students get to take the assignment  # noqa: E501

        :param attempts: The attempts of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: int
        """

        self._attempts = attempts

    @property
    def password(self):
        """Gets the password of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        A password required to enter the assingment  # noqa: E501

        :return: The password of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        A password required to enter the assingment  # noqa: E501

        :param password: The password of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def restricted_access_to_other_pages(self):
        """Gets the restricted_access_to_other_pages of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Prevents the user from opening other assignments in Ans while taking this assignment  # noqa: E501

        :return: The restricted_access_to_other_pages of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_access_to_other_pages

    @restricted_access_to_other_pages.setter
    def restricted_access_to_other_pages(self, restricted_access_to_other_pages):
        """Sets the restricted_access_to_other_pages of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Prevents the user from opening other assignments in Ans while taking this assignment  # noqa: E501

        :param restricted_access_to_other_pages: The restricted_access_to_other_pages of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._restricted_access_to_other_pages = restricted_access_to_other_pages

    @property
    def restricted_ip_access(self):
        """Gets the restricted_ip_access of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Defines whether access should be restricted based on IP. Set location_ids to limit access to those locations  # noqa: E501

        :return: The restricted_ip_access of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_ip_access

    @restricted_ip_access.setter
    def restricted_ip_access(self, restricted_ip_access):
        """Sets the restricted_ip_access of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Defines whether access should be restricted based on IP. Set location_ids to limit access to those locations  # noqa: E501

        :param restricted_ip_access: The restricted_ip_access of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._restricted_ip_access = restricted_ip_access

    @property
    def location_ids(self):
        """Gets the location_ids of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        An array of location ids the assignment may be accessed from  # noqa: E501

        :return: The location_ids of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: list[int]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """Sets the location_ids of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        An array of location ids the assignment may be accessed from  # noqa: E501

        :param location_ids: The location_ids of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: list[int]
        """

        self._location_ids = location_ids

    @property
    def notes(self):
        """Gets the notes of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Allows students to take digital notes during their assignment  # noqa: E501

        :return: The notes of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Allows students to take digital notes during their assignment  # noqa: E501

        :param notes: The notes of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._notes = notes

    @property
    def spellchecker(self):
        """Gets the spellchecker of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Allows students to use spell checking  # noqa: E501

        :return: The spellchecker of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._spellchecker

    @spellchecker.setter
    def spellchecker(self, spellchecker):
        """Sets the spellchecker of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Allows students to use spell checking  # noqa: E501

        :param spellchecker: The spellchecker of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._spellchecker = spellchecker

    @property
    def config_keys(self):
        """Gets the config_keys of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Lockdown browser hash to sha256 with the request url and is compared to the configKeyHash sent in the request headers  # noqa: E501

        :return: The config_keys of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: list[int]
        """
        return self._config_keys

    @config_keys.setter
    def config_keys(self, config_keys):
        """Sets the config_keys of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Lockdown browser hash to sha256 with the request url and is compared to the configKeyHash sent in the request headers  # noqa: E501

        :param config_keys: The config_keys of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: list[int]
        """

        self._config_keys = config_keys

    @property
    def calculator(self):
        """Gets the calculator of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501


        :return: The calculator of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: OneOfapiv2coursescourseIdassignmentsAccessibilitySettings1Calculator
        """
        return self._calculator

    @calculator.setter
    def calculator(self, calculator):
        """Sets the calculator of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.


        :param calculator: The calculator of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: OneOfapiv2coursescourseIdassignmentsAccessibilitySettings1Calculator
        """

        self._calculator = calculator

    @property
    def feedback(self):
        """Gets the feedback of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Allows students to receive feedback during the assignment  # noqa: E501

        :return: The feedback of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Allows students to receive feedback during the assignment  # noqa: E501

        :param feedback: The feedback of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._feedback = feedback

    @property
    def forced_test_navigation(self):
        """Gets the forced_test_navigation of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Students may only answer questions once; they may not return to an exercise that they closed  # noqa: E501

        :return: The forced_test_navigation of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._forced_test_navigation

    @forced_test_navigation.setter
    def forced_test_navigation(self, forced_test_navigation):
        """Sets the forced_test_navigation of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Students may only answer questions once; they may not return to an exercise that they closed  # noqa: E501

        :param forced_test_navigation: The forced_test_navigation of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._forced_test_navigation = forced_test_navigation

    @property
    def cannot_reopen_question_groups(self):
        """Gets the cannot_reopen_question_groups of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Prevents students from reopening a flow group after closing  # noqa: E501

        :return: The cannot_reopen_question_groups of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._cannot_reopen_question_groups

    @cannot_reopen_question_groups.setter
    def cannot_reopen_question_groups(self, cannot_reopen_question_groups):
        """Sets the cannot_reopen_question_groups of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Prevents students from reopening a flow group after closing  # noqa: E501

        :param cannot_reopen_question_groups: The cannot_reopen_question_groups of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._cannot_reopen_question_groups = cannot_reopen_question_groups

    @property
    def seb_server_enabled(self):
        """Gets the seb_server_enabled of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501

        Restrict access to the assignment to Safe Exam Browser only  # noqa: E501

        :return: The seb_server_enabled of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :rtype: bool
        """
        return self._seb_server_enabled

    @seb_server_enabled.setter
    def seb_server_enabled(self, seb_server_enabled):
        """Sets the seb_server_enabled of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.

        Restrict access to the assignment to Safe Exam Browser only  # noqa: E501

        :param seb_server_enabled: The seb_server_enabled of this Apiv2coursescourseIdassignmentsAccessibilitySettings1.  # noqa: E501
        :type: bool
        """

        self._seb_server_enabled = seb_server_enabled

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
        if issubclass(Apiv2coursescourseIdassignmentsAccessibilitySettings1, dict):
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
        if not isinstance(other, Apiv2coursescourseIdassignmentsAccessibilitySettings1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other