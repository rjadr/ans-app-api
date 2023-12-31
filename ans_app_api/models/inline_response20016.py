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

class InlineResponse20016(object):
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
        'active': 'bool',
        'allow_export': 'bool',
        'created_at': 'str',
        'exclude_correctly_answered_questions': 'bool',
        'excluded_exercise_ids': 'list[int]',
        'location_ids': 'list[int]',
        'password': 'str',
        'restricted_ip_access': 'bool',
        'show_average_objective_score': 'bool',
        'show_criteria': 'bool',
        'show_domains': 'bool',
        'show_given_answers': 'bool',
        'show_grade': 'bool',
        'show_grading_description': 'bool',
        'show_letter_grade': 'bool',
        'show_objectives': 'bool',
        'show_points_per_question': 'bool',
        'show_preliminary_result': 'bool',
        'show_questions': 'bool',
        'show_review_consensus': 'bool',
        'show_total_points': 'bool',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'active': 'active',
        'allow_export': 'allow_export',
        'created_at': 'created_at',
        'exclude_correctly_answered_questions': 'exclude_correctly_answered_questions',
        'excluded_exercise_ids': 'excluded_exercise_ids',
        'location_ids': 'location_ids',
        'password': 'password',
        'restricted_ip_access': 'restricted_ip_access',
        'show_average_objective_score': 'show_average_objective_score',
        'show_criteria': 'show_criteria',
        'show_domains': 'show_domains',
        'show_given_answers': 'show_given_answers',
        'show_grade': 'show_grade',
        'show_grading_description': 'show_grading_description',
        'show_letter_grade': 'show_letter_grade',
        'show_objectives': 'show_objectives',
        'show_points_per_question': 'show_points_per_question',
        'show_preliminary_result': 'show_preliminary_result',
        'show_questions': 'show_questions',
        'show_review_consensus': 'show_review_consensus',
        'show_total_points': 'show_total_points',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, active=None, allow_export=None, created_at=None, exclude_correctly_answered_questions=None, excluded_exercise_ids=None, location_ids=None, password=None, restricted_ip_access=None, show_average_objective_score=None, show_criteria=None, show_domains=None, show_given_answers=None, show_grade=None, show_grading_description=None, show_letter_grade=None, show_objectives=None, show_points_per_question=None, show_preliminary_result=None, show_questions=None, show_review_consensus=None, show_total_points=None, updated_at=None):  # noqa: E501
        """InlineResponse20016 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._active = None
        self._allow_export = None
        self._created_at = None
        self._exclude_correctly_answered_questions = None
        self._excluded_exercise_ids = None
        self._location_ids = None
        self._password = None
        self._restricted_ip_access = None
        self._show_average_objective_score = None
        self._show_criteria = None
        self._show_domains = None
        self._show_given_answers = None
        self._show_grade = None
        self._show_grading_description = None
        self._show_letter_grade = None
        self._show_objectives = None
        self._show_points_per_question = None
        self._show_preliminary_result = None
        self._show_questions = None
        self._show_review_consensus = None
        self._show_total_points = None
        self._updated_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if allow_export is not None:
            self.allow_export = allow_export
        if created_at is not None:
            self.created_at = created_at
        if exclude_correctly_answered_questions is not None:
            self.exclude_correctly_answered_questions = exclude_correctly_answered_questions
        if excluded_exercise_ids is not None:
            self.excluded_exercise_ids = excluded_exercise_ids
        if location_ids is not None:
            self.location_ids = location_ids
        if password is not None:
            self.password = password
        if restricted_ip_access is not None:
            self.restricted_ip_access = restricted_ip_access
        if show_average_objective_score is not None:
            self.show_average_objective_score = show_average_objective_score
        if show_criteria is not None:
            self.show_criteria = show_criteria
        if show_domains is not None:
            self.show_domains = show_domains
        if show_given_answers is not None:
            self.show_given_answers = show_given_answers
        if show_grade is not None:
            self.show_grade = show_grade
        if show_grading_description is not None:
            self.show_grading_description = show_grading_description
        if show_letter_grade is not None:
            self.show_letter_grade = show_letter_grade
        if show_objectives is not None:
            self.show_objectives = show_objectives
        if show_points_per_question is not None:
            self.show_points_per_question = show_points_per_question
        if show_preliminary_result is not None:
            self.show_preliminary_result = show_preliminary_result
        if show_questions is not None:
            self.show_questions = show_questions
        if show_review_consensus is not None:
            self.show_review_consensus = show_review_consensus
        if show_total_points is not None:
            self.show_total_points = show_total_points
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this InlineResponse20016.  # noqa: E501


        :return: The id of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20016.


        :param id: The id of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this InlineResponse20016.  # noqa: E501


        :return: The active of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse20016.


        :param active: The active of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def allow_export(self):
        """Gets the allow_export of this InlineResponse20016.  # noqa: E501


        :return: The allow_export of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._allow_export

    @allow_export.setter
    def allow_export(self, allow_export):
        """Sets the allow_export of this InlineResponse20016.


        :param allow_export: The allow_export of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._allow_export = allow_export

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20016.  # noqa: E501


        :return: The created_at of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20016.


        :param created_at: The created_at of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def exclude_correctly_answered_questions(self):
        """Gets the exclude_correctly_answered_questions of this InlineResponse20016.  # noqa: E501


        :return: The exclude_correctly_answered_questions of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_correctly_answered_questions

    @exclude_correctly_answered_questions.setter
    def exclude_correctly_answered_questions(self, exclude_correctly_answered_questions):
        """Sets the exclude_correctly_answered_questions of this InlineResponse20016.


        :param exclude_correctly_answered_questions: The exclude_correctly_answered_questions of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._exclude_correctly_answered_questions = exclude_correctly_answered_questions

    @property
    def excluded_exercise_ids(self):
        """Gets the excluded_exercise_ids of this InlineResponse20016.  # noqa: E501


        :return: The excluded_exercise_ids of this InlineResponse20016.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_exercise_ids

    @excluded_exercise_ids.setter
    def excluded_exercise_ids(self, excluded_exercise_ids):
        """Sets the excluded_exercise_ids of this InlineResponse20016.


        :param excluded_exercise_ids: The excluded_exercise_ids of this InlineResponse20016.  # noqa: E501
        :type: list[int]
        """

        self._excluded_exercise_ids = excluded_exercise_ids

    @property
    def location_ids(self):
        """Gets the location_ids of this InlineResponse20016.  # noqa: E501


        :return: The location_ids of this InlineResponse20016.  # noqa: E501
        :rtype: list[int]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """Sets the location_ids of this InlineResponse20016.


        :param location_ids: The location_ids of this InlineResponse20016.  # noqa: E501
        :type: list[int]
        """

        self._location_ids = location_ids

    @property
    def password(self):
        """Gets the password of this InlineResponse20016.  # noqa: E501


        :return: The password of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineResponse20016.


        :param password: The password of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def restricted_ip_access(self):
        """Gets the restricted_ip_access of this InlineResponse20016.  # noqa: E501


        :return: The restricted_ip_access of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_ip_access

    @restricted_ip_access.setter
    def restricted_ip_access(self, restricted_ip_access):
        """Sets the restricted_ip_access of this InlineResponse20016.


        :param restricted_ip_access: The restricted_ip_access of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._restricted_ip_access = restricted_ip_access

    @property
    def show_average_objective_score(self):
        """Gets the show_average_objective_score of this InlineResponse20016.  # noqa: E501


        :return: The show_average_objective_score of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_average_objective_score

    @show_average_objective_score.setter
    def show_average_objective_score(self, show_average_objective_score):
        """Sets the show_average_objective_score of this InlineResponse20016.


        :param show_average_objective_score: The show_average_objective_score of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_average_objective_score = show_average_objective_score

    @property
    def show_criteria(self):
        """Gets the show_criteria of this InlineResponse20016.  # noqa: E501


        :return: The show_criteria of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_criteria

    @show_criteria.setter
    def show_criteria(self, show_criteria):
        """Sets the show_criteria of this InlineResponse20016.


        :param show_criteria: The show_criteria of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_criteria = show_criteria

    @property
    def show_domains(self):
        """Gets the show_domains of this InlineResponse20016.  # noqa: E501


        :return: The show_domains of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_domains

    @show_domains.setter
    def show_domains(self, show_domains):
        """Sets the show_domains of this InlineResponse20016.


        :param show_domains: The show_domains of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_domains = show_domains

    @property
    def show_given_answers(self):
        """Gets the show_given_answers of this InlineResponse20016.  # noqa: E501


        :return: The show_given_answers of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_given_answers

    @show_given_answers.setter
    def show_given_answers(self, show_given_answers):
        """Sets the show_given_answers of this InlineResponse20016.


        :param show_given_answers: The show_given_answers of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_given_answers = show_given_answers

    @property
    def show_grade(self):
        """Gets the show_grade of this InlineResponse20016.  # noqa: E501


        :return: The show_grade of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_grade

    @show_grade.setter
    def show_grade(self, show_grade):
        """Sets the show_grade of this InlineResponse20016.


        :param show_grade: The show_grade of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_grade = show_grade

    @property
    def show_grading_description(self):
        """Gets the show_grading_description of this InlineResponse20016.  # noqa: E501


        :return: The show_grading_description of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_grading_description

    @show_grading_description.setter
    def show_grading_description(self, show_grading_description):
        """Sets the show_grading_description of this InlineResponse20016.


        :param show_grading_description: The show_grading_description of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_grading_description = show_grading_description

    @property
    def show_letter_grade(self):
        """Gets the show_letter_grade of this InlineResponse20016.  # noqa: E501


        :return: The show_letter_grade of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_letter_grade

    @show_letter_grade.setter
    def show_letter_grade(self, show_letter_grade):
        """Sets the show_letter_grade of this InlineResponse20016.


        :param show_letter_grade: The show_letter_grade of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_letter_grade = show_letter_grade

    @property
    def show_objectives(self):
        """Gets the show_objectives of this InlineResponse20016.  # noqa: E501


        :return: The show_objectives of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_objectives

    @show_objectives.setter
    def show_objectives(self, show_objectives):
        """Sets the show_objectives of this InlineResponse20016.


        :param show_objectives: The show_objectives of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_objectives = show_objectives

    @property
    def show_points_per_question(self):
        """Gets the show_points_per_question of this InlineResponse20016.  # noqa: E501


        :return: The show_points_per_question of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_points_per_question

    @show_points_per_question.setter
    def show_points_per_question(self, show_points_per_question):
        """Sets the show_points_per_question of this InlineResponse20016.


        :param show_points_per_question: The show_points_per_question of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_points_per_question = show_points_per_question

    @property
    def show_preliminary_result(self):
        """Gets the show_preliminary_result of this InlineResponse20016.  # noqa: E501


        :return: The show_preliminary_result of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_preliminary_result

    @show_preliminary_result.setter
    def show_preliminary_result(self, show_preliminary_result):
        """Sets the show_preliminary_result of this InlineResponse20016.


        :param show_preliminary_result: The show_preliminary_result of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_preliminary_result = show_preliminary_result

    @property
    def show_questions(self):
        """Gets the show_questions of this InlineResponse20016.  # noqa: E501


        :return: The show_questions of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_questions

    @show_questions.setter
    def show_questions(self, show_questions):
        """Sets the show_questions of this InlineResponse20016.


        :param show_questions: The show_questions of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_questions = show_questions

    @property
    def show_review_consensus(self):
        """Gets the show_review_consensus of this InlineResponse20016.  # noqa: E501


        :return: The show_review_consensus of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_review_consensus

    @show_review_consensus.setter
    def show_review_consensus(self, show_review_consensus):
        """Sets the show_review_consensus of this InlineResponse20016.


        :param show_review_consensus: The show_review_consensus of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_review_consensus = show_review_consensus

    @property
    def show_total_points(self):
        """Gets the show_total_points of this InlineResponse20016.  # noqa: E501


        :return: The show_total_points of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._show_total_points

    @show_total_points.setter
    def show_total_points(self, show_total_points):
        """Sets the show_total_points of this InlineResponse20016.


        :param show_total_points: The show_total_points of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._show_total_points = show_total_points

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse20016.  # noqa: E501


        :return: The updated_at of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse20016.


        :param updated_at: The updated_at of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(InlineResponse20016, dict):
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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
