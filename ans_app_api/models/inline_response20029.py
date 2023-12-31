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

class InlineResponse20029(object):
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
        'id': 'int',
        'student_number': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'role': 'str',
        'role_id': 'int',
        'active': 'bool',
        'school_id': 'int',
        'trashed': 'bool',
        'trashed_at': 'str',
        'alumni': 'bool',
        'uid': 'str',
        'external_id': 'str',
        'current_sign_in_at': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'courses': 'list[InlineResponse20029Courses]',
        'question_banks': 'list[InlineResponse20029QuestionBanks]',
        'departments': 'list[InlineResponse20029Departments]'
    }

    attribute_map = {
        'id': 'id',
        'student_number': 'student_number',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name',
        'email': 'email',
        'role': 'role',
        'role_id': 'role_id',
        'active': 'active',
        'school_id': 'school_id',
        'trashed': 'trashed',
        'trashed_at': 'trashed_at',
        'alumni': 'alumni',
        'uid': 'uid',
        'external_id': 'external_id',
        'current_sign_in_at': 'current_sign_in_at',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'courses': 'courses',
        'question_banks': 'question_banks',
        'departments': 'departments'
    }

    def __init__(self, id=None, student_number=None, first_name=None, middle_name=None, last_name=None, email=None, role=None, role_id=None, active=None, school_id=None, trashed=None, trashed_at=None, alumni=None, uid=None, external_id=None, current_sign_in_at=None, created_at=None, updated_at=None, courses=None, question_banks=None, departments=None):  # noqa: E501
        """InlineResponse20029 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._student_number = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._email = None
        self._role = None
        self._role_id = None
        self._active = None
        self._school_id = None
        self._trashed = None
        self._trashed_at = None
        self._alumni = None
        self._uid = None
        self._external_id = None
        self._current_sign_in_at = None
        self._created_at = None
        self._updated_at = None
        self._courses = None
        self._question_banks = None
        self._departments = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if student_number is not None:
            self.student_number = student_number
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if role_id is not None:
            self.role_id = role_id
        if active is not None:
            self.active = active
        if school_id is not None:
            self.school_id = school_id
        if trashed is not None:
            self.trashed = trashed
        if trashed_at is not None:
            self.trashed_at = trashed_at
        if alumni is not None:
            self.alumni = alumni
        if uid is not None:
            self.uid = uid
        if external_id is not None:
            self.external_id = external_id
        if current_sign_in_at is not None:
            self.current_sign_in_at = current_sign_in_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if courses is not None:
            self.courses = courses
        if question_banks is not None:
            self.question_banks = question_banks
        if departments is not None:
            self.departments = departments

    @property
    def id(self):
        """Gets the id of this InlineResponse20029.  # noqa: E501


        :return: The id of this InlineResponse20029.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20029.


        :param id: The id of this InlineResponse20029.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def student_number(self):
        """Gets the student_number of this InlineResponse20029.  # noqa: E501


        :return: The student_number of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._student_number

    @student_number.setter
    def student_number(self, student_number):
        """Sets the student_number of this InlineResponse20029.


        :param student_number: The student_number of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._student_number = student_number

    @property
    def first_name(self):
        """Gets the first_name of this InlineResponse20029.  # noqa: E501


        :return: The first_name of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this InlineResponse20029.


        :param first_name: The first_name of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this InlineResponse20029.  # noqa: E501


        :return: The middle_name of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this InlineResponse20029.


        :param middle_name: The middle_name of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this InlineResponse20029.  # noqa: E501


        :return: The last_name of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this InlineResponse20029.


        :param last_name: The last_name of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this InlineResponse20029.  # noqa: E501


        :return: The email of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20029.


        :param email: The email of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this InlineResponse20029.  # noqa: E501


        :return: The role of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse20029.


        :param role: The role of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def role_id(self):
        """Gets the role_id of this InlineResponse20029.  # noqa: E501


        :return: The role_id of this InlineResponse20029.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this InlineResponse20029.


        :param role_id: The role_id of this InlineResponse20029.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def active(self):
        """Gets the active of this InlineResponse20029.  # noqa: E501


        :return: The active of this InlineResponse20029.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse20029.


        :param active: The active of this InlineResponse20029.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def school_id(self):
        """Gets the school_id of this InlineResponse20029.  # noqa: E501


        :return: The school_id of this InlineResponse20029.  # noqa: E501
        :rtype: int
        """
        return self._school_id

    @school_id.setter
    def school_id(self, school_id):
        """Sets the school_id of this InlineResponse20029.


        :param school_id: The school_id of this InlineResponse20029.  # noqa: E501
        :type: int
        """

        self._school_id = school_id

    @property
    def trashed(self):
        """Gets the trashed of this InlineResponse20029.  # noqa: E501


        :return: The trashed of this InlineResponse20029.  # noqa: E501
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """Sets the trashed of this InlineResponse20029.


        :param trashed: The trashed of this InlineResponse20029.  # noqa: E501
        :type: bool
        """

        self._trashed = trashed

    @property
    def trashed_at(self):
        """Gets the trashed_at of this InlineResponse20029.  # noqa: E501


        :return: The trashed_at of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._trashed_at

    @trashed_at.setter
    def trashed_at(self, trashed_at):
        """Sets the trashed_at of this InlineResponse20029.


        :param trashed_at: The trashed_at of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._trashed_at = trashed_at

    @property
    def alumni(self):
        """Gets the alumni of this InlineResponse20029.  # noqa: E501


        :return: The alumni of this InlineResponse20029.  # noqa: E501
        :rtype: bool
        """
        return self._alumni

    @alumni.setter
    def alumni(self, alumni):
        """Sets the alumni of this InlineResponse20029.


        :param alumni: The alumni of this InlineResponse20029.  # noqa: E501
        :type: bool
        """

        self._alumni = alumni

    @property
    def uid(self):
        """Gets the uid of this InlineResponse20029.  # noqa: E501


        :return: The uid of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this InlineResponse20029.


        :param uid: The uid of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def external_id(self):
        """Gets the external_id of this InlineResponse20029.  # noqa: E501


        :return: The external_id of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this InlineResponse20029.


        :param external_id: The external_id of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def current_sign_in_at(self):
        """Gets the current_sign_in_at of this InlineResponse20029.  # noqa: E501


        :return: The current_sign_in_at of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._current_sign_in_at

    @current_sign_in_at.setter
    def current_sign_in_at(self, current_sign_in_at):
        """Sets the current_sign_in_at of this InlineResponse20029.


        :param current_sign_in_at: The current_sign_in_at of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._current_sign_in_at = current_sign_in_at

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20029.  # noqa: E501


        :return: The created_at of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20029.


        :param created_at: The created_at of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse20029.  # noqa: E501


        :return: The updated_at of this InlineResponse20029.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse20029.


        :param updated_at: The updated_at of this InlineResponse20029.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def courses(self):
        """Gets the courses of this InlineResponse20029.  # noqa: E501


        :return: The courses of this InlineResponse20029.  # noqa: E501
        :rtype: list[InlineResponse20029Courses]
        """
        return self._courses

    @courses.setter
    def courses(self, courses):
        """Sets the courses of this InlineResponse20029.


        :param courses: The courses of this InlineResponse20029.  # noqa: E501
        :type: list[InlineResponse20029Courses]
        """

        self._courses = courses

    @property
    def question_banks(self):
        """Gets the question_banks of this InlineResponse20029.  # noqa: E501


        :return: The question_banks of this InlineResponse20029.  # noqa: E501
        :rtype: list[InlineResponse20029QuestionBanks]
        """
        return self._question_banks

    @question_banks.setter
    def question_banks(self, question_banks):
        """Sets the question_banks of this InlineResponse20029.


        :param question_banks: The question_banks of this InlineResponse20029.  # noqa: E501
        :type: list[InlineResponse20029QuestionBanks]
        """

        self._question_banks = question_banks

    @property
    def departments(self):
        """Gets the departments of this InlineResponse20029.  # noqa: E501


        :return: The departments of this InlineResponse20029.  # noqa: E501
        :rtype: list[InlineResponse20029Departments]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """Sets the departments of this InlineResponse20029.


        :param departments: The departments of this InlineResponse20029.  # noqa: E501
        :type: list[InlineResponse20029Departments]
        """

        self._departments = departments

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
        if issubclass(InlineResponse20029, dict):
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
        if not isinstance(other, InlineResponse20029):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
