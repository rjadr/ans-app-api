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

class CourseIdAssignmentsBody(object):
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
        'name': 'str',
        'assignment_type': 'OneOfcourseIdAssignmentsBodyAssignmentType',
        'number_of_forms': 'int',
        'question_bank_assignment_id': 'int',
        'summative': 'bool',
        'external_id': 'str',
        'label_id': 'int',
        'trashed': 'bool',
        'accessibility_settings': 'Apiv2coursescourseIdassignmentsAccessibilitySettings1',
        'grades_settings': 'Apiv2coursescourseIdassignmentsGradesSettings1',
        'integrations': 'Apiv2coursescourseIdassignmentsIntegrations1',
        'exercise_reviewers': 'list[Apiv2coursescourseIdassignmentsExerciseReviewers]',
        'group_reviewers': 'list[Apiv2coursescourseIdassignmentsGroupReviewers]'
    }

    attribute_map = {
        'name': 'name',
        'assignment_type': 'assignment_type',
        'number_of_forms': 'number_of_forms',
        'question_bank_assignment_id': 'question_bank_assignment_id',
        'summative': 'summative',
        'external_id': 'external_id',
        'label_id': 'label_id',
        'trashed': 'trashed',
        'accessibility_settings': 'accessibility_settings',
        'grades_settings': 'grades_settings',
        'integrations': 'integrations',
        'exercise_reviewers': 'exercise_reviewers',
        'group_reviewers': 'group_reviewers'
    }

    def __init__(self, name=None, assignment_type=None, number_of_forms=0, question_bank_assignment_id=None, summative=None, external_id=None, label_id=None, trashed=False, accessibility_settings=None, grades_settings=None, integrations=None, exercise_reviewers=None, group_reviewers=None):  # noqa: E501
        """CourseIdAssignmentsBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._assignment_type = None
        self._number_of_forms = None
        self._question_bank_assignment_id = None
        self._summative = None
        self._external_id = None
        self._label_id = None
        self._trashed = None
        self._accessibility_settings = None
        self._grades_settings = None
        self._integrations = None
        self._exercise_reviewers = None
        self._group_reviewers = None
        self.discriminator = None
        self.name = name
        if assignment_type is not None:
            self.assignment_type = assignment_type
        if number_of_forms is not None:
            self.number_of_forms = number_of_forms
        if question_bank_assignment_id is not None:
            self.question_bank_assignment_id = question_bank_assignment_id
        if summative is not None:
            self.summative = summative
        if external_id is not None:
            self.external_id = external_id
        if label_id is not None:
            self.label_id = label_id
        if trashed is not None:
            self.trashed = trashed
        if accessibility_settings is not None:
            self.accessibility_settings = accessibility_settings
        if grades_settings is not None:
            self.grades_settings = grades_settings
        if integrations is not None:
            self.integrations = integrations
        if exercise_reviewers is not None:
            self.exercise_reviewers = exercise_reviewers
        if group_reviewers is not None:
            self.group_reviewers = group_reviewers

    @property
    def name(self):
        """Gets the name of this CourseIdAssignmentsBody.  # noqa: E501

        The name of the assignment  # noqa: E501

        :return: The name of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CourseIdAssignmentsBody.

        The name of the assignment  # noqa: E501

        :param name: The name of this CourseIdAssignmentsBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def assignment_type(self):
        """Gets the assignment_type of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The assignment_type of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: OneOfcourseIdAssignmentsBodyAssignmentType
        """
        return self._assignment_type

    @assignment_type.setter
    def assignment_type(self, assignment_type):
        """Sets the assignment_type of this CourseIdAssignmentsBody.


        :param assignment_type: The assignment_type of this CourseIdAssignmentsBody.  # noqa: E501
        :type: OneOfcourseIdAssignmentsBodyAssignmentType
        """

        self._assignment_type = assignment_type

    @property
    def number_of_forms(self):
        """Gets the number_of_forms of this CourseIdAssignmentsBody.  # noqa: E501

        The amount of forms to be generated for written assignments. Increasing this amount will trigger the generation of forms  # noqa: E501

        :return: The number_of_forms of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: int
        """
        return self._number_of_forms

    @number_of_forms.setter
    def number_of_forms(self, number_of_forms):
        """Sets the number_of_forms of this CourseIdAssignmentsBody.

        The amount of forms to be generated for written assignments. Increasing this amount will trigger the generation of forms  # noqa: E501

        :param number_of_forms: The number_of_forms of this CourseIdAssignmentsBody.  # noqa: E501
        :type: int
        """

        self._number_of_forms = number_of_forms

    @property
    def question_bank_assignment_id(self):
        """Gets the question_bank_assignment_id of this CourseIdAssignmentsBody.  # noqa: E501

        An id of a question bank assignment. When creating a new assignment with this attribute, all questions from the question bank assignment will be copied into the assignment. When updating an assignment, no action is taken  # noqa: E501

        :return: The question_bank_assignment_id of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: int
        """
        return self._question_bank_assignment_id

    @question_bank_assignment_id.setter
    def question_bank_assignment_id(self, question_bank_assignment_id):
        """Sets the question_bank_assignment_id of this CourseIdAssignmentsBody.

        An id of a question bank assignment. When creating a new assignment with this attribute, all questions from the question bank assignment will be copied into the assignment. When updating an assignment, no action is taken  # noqa: E501

        :param question_bank_assignment_id: The question_bank_assignment_id of this CourseIdAssignmentsBody.  # noqa: E501
        :type: int
        """

        self._question_bank_assignment_id = question_bank_assignment_id

    @property
    def summative(self):
        """Gets the summative of this CourseIdAssignmentsBody.  # noqa: E501

        Defines if an assignment is summative if set to true, formative if set to false  # noqa: E501

        :return: The summative of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: bool
        """
        return self._summative

    @summative.setter
    def summative(self, summative):
        """Sets the summative of this CourseIdAssignmentsBody.

        Defines if an assignment is summative if set to true, formative if set to false  # noqa: E501

        :param summative: The summative of this CourseIdAssignmentsBody.  # noqa: E501
        :type: bool
        """

        self._summative = summative

    @property
    def external_id(self):
        """Gets the external_id of this CourseIdAssignmentsBody.  # noqa: E501

        An external id to reference the assignment  # noqa: E501

        :return: The external_id of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CourseIdAssignmentsBody.

        An external id to reference the assignment  # noqa: E501

        :param external_id: The external_id of this CourseIdAssignmentsBody.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def label_id(self):
        """Gets the label_id of this CourseIdAssignmentsBody.  # noqa: E501

        A label id to set the label on the assignment  # noqa: E501

        :return: The label_id of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this CourseIdAssignmentsBody.

        A label id to set the label on the assignment  # noqa: E501

        :param label_id: The label_id of this CourseIdAssignmentsBody.  # noqa: E501
        :type: int
        """

        self._label_id = label_id

    @property
    def trashed(self):
        """Gets the trashed of this CourseIdAssignmentsBody.  # noqa: E501

        Defines if an assignment has been soft deleted  # noqa: E501

        :return: The trashed of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """Sets the trashed of this CourseIdAssignmentsBody.

        Defines if an assignment has been soft deleted  # noqa: E501

        :param trashed: The trashed of this CourseIdAssignmentsBody.  # noqa: E501
        :type: bool
        """

        self._trashed = trashed

    @property
    def accessibility_settings(self):
        """Gets the accessibility_settings of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The accessibility_settings of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: Apiv2coursescourseIdassignmentsAccessibilitySettings1
        """
        return self._accessibility_settings

    @accessibility_settings.setter
    def accessibility_settings(self, accessibility_settings):
        """Sets the accessibility_settings of this CourseIdAssignmentsBody.


        :param accessibility_settings: The accessibility_settings of this CourseIdAssignmentsBody.  # noqa: E501
        :type: Apiv2coursescourseIdassignmentsAccessibilitySettings1
        """

        self._accessibility_settings = accessibility_settings

    @property
    def grades_settings(self):
        """Gets the grades_settings of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The grades_settings of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: Apiv2coursescourseIdassignmentsGradesSettings1
        """
        return self._grades_settings

    @grades_settings.setter
    def grades_settings(self, grades_settings):
        """Sets the grades_settings of this CourseIdAssignmentsBody.


        :param grades_settings: The grades_settings of this CourseIdAssignmentsBody.  # noqa: E501
        :type: Apiv2coursescourseIdassignmentsGradesSettings1
        """

        self._grades_settings = grades_settings

    @property
    def integrations(self):
        """Gets the integrations of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The integrations of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: Apiv2coursescourseIdassignmentsIntegrations1
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this CourseIdAssignmentsBody.


        :param integrations: The integrations of this CourseIdAssignmentsBody.  # noqa: E501
        :type: Apiv2coursescourseIdassignmentsIntegrations1
        """

        self._integrations = integrations

    @property
    def exercise_reviewers(self):
        """Gets the exercise_reviewers of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The exercise_reviewers of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: list[Apiv2coursescourseIdassignmentsExerciseReviewers]
        """
        return self._exercise_reviewers

    @exercise_reviewers.setter
    def exercise_reviewers(self, exercise_reviewers):
        """Sets the exercise_reviewers of this CourseIdAssignmentsBody.


        :param exercise_reviewers: The exercise_reviewers of this CourseIdAssignmentsBody.  # noqa: E501
        :type: list[Apiv2coursescourseIdassignmentsExerciseReviewers]
        """

        self._exercise_reviewers = exercise_reviewers

    @property
    def group_reviewers(self):
        """Gets the group_reviewers of this CourseIdAssignmentsBody.  # noqa: E501


        :return: The group_reviewers of this CourseIdAssignmentsBody.  # noqa: E501
        :rtype: list[Apiv2coursescourseIdassignmentsGroupReviewers]
        """
        return self._group_reviewers

    @group_reviewers.setter
    def group_reviewers(self, group_reviewers):
        """Sets the group_reviewers of this CourseIdAssignmentsBody.


        :param group_reviewers: The group_reviewers of this CourseIdAssignmentsBody.  # noqa: E501
        :type: list[Apiv2coursescourseIdassignmentsGroupReviewers]
        """

        self._group_reviewers = group_reviewers

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
        if issubclass(CourseIdAssignmentsBody, dict):
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
        if not isinstance(other, CourseIdAssignmentsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other