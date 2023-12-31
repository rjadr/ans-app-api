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

class Apiv2coursescourseIdassignmentsIntegrations1Proctorio(object):
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
        'cache': 'bool',
        'clipboard': 'bool',
        'closetabs': 'bool',
        'downloads': 'bool',
        'fullscreen': 'str',
        'onescreen': 'bool',
        '_print': 'bool',
        'recording': 'list[str]',
        'reentry': 'str',
        'rightclick': 'bool',
        'tabs': 'str',
        'verify': 'list[str]',
        'whiteboard': 'bool'
    }

    attribute_map = {
        'cache': 'cache',
        'clipboard': 'clipboard',
        'closetabs': 'closetabs',
        'downloads': 'downloads',
        'fullscreen': 'fullscreen',
        'onescreen': 'onescreen',
        '_print': 'print',
        'recording': 'recording',
        'reentry': 'reentry',
        'rightclick': 'rightclick',
        'tabs': 'tabs',
        'verify': 'verify',
        'whiteboard': 'whiteboard'
    }

    def __init__(self, cache=False, clipboard=False, closetabs=False, downloads=False, fullscreen='', onescreen=False, _print=False, recording=None, reentry='', rightclick=False, tabs='', verify=None, whiteboard=False):  # noqa: E501
        """Apiv2coursescourseIdassignmentsIntegrations1Proctorio - a model defined in Swagger"""  # noqa: E501
        self._cache = None
        self._clipboard = None
        self._closetabs = None
        self._downloads = None
        self._fullscreen = None
        self._onescreen = None
        self.__print = None
        self._recording = None
        self._reentry = None
        self._rightclick = None
        self._tabs = None
        self._verify = None
        self._whiteboard = None
        self.discriminator = None
        if cache is not None:
            self.cache = cache
        if clipboard is not None:
            self.clipboard = clipboard
        if closetabs is not None:
            self.closetabs = closetabs
        if downloads is not None:
            self.downloads = downloads
        if fullscreen is not None:
            self.fullscreen = fullscreen
        if onescreen is not None:
            self.onescreen = onescreen
        if _print is not None:
            self._print = _print
        if recording is not None:
            self.recording = recording
        if reentry is not None:
            self.reentry = reentry
        if rightclick is not None:
            self.rightclick = rightclick
        if tabs is not None:
            self.tabs = tabs
        if verify is not None:
            self.verify = verify
        if whiteboard is not None:
            self.whiteboard = whiteboard

    @property
    def cache(self):
        """Gets the cache of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The cache of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param cache: The cache of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._cache = cache

    @property
    def clipboard(self):
        """Gets the clipboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The clipboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._clipboard

    @clipboard.setter
    def clipboard(self, clipboard):
        """Sets the clipboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param clipboard: The clipboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._clipboard = clipboard

    @property
    def closetabs(self):
        """Gets the closetabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The closetabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._closetabs

    @closetabs.setter
    def closetabs(self, closetabs):
        """Sets the closetabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param closetabs: The closetabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._closetabs = closetabs

    @property
    def downloads(self):
        """Gets the downloads of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The downloads of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._downloads

    @downloads.setter
    def downloads(self, downloads):
        """Sets the downloads of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param downloads: The downloads of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._downloads = downloads

    @property
    def fullscreen(self):
        """Gets the fullscreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The fullscreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: str
        """
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, fullscreen):
        """Sets the fullscreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param fullscreen: The fullscreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: str
        """

        self._fullscreen = fullscreen

    @property
    def onescreen(self):
        """Gets the onescreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The onescreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._onescreen

    @onescreen.setter
    def onescreen(self, onescreen):
        """Sets the onescreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param onescreen: The onescreen of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._onescreen = onescreen

    @property
    def _print(self):
        """Gets the _print of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The _print of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self.__print

    @_print.setter
    def _print(self, _print):
        """Sets the _print of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param _print: The _print of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self.__print = _print

    @property
    def recording(self):
        """Gets the recording of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The recording of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: list[str]
        """
        return self._recording

    @recording.setter
    def recording(self, recording):
        """Sets the recording of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param recording: The recording of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: list[str]
        """

        self._recording = recording

    @property
    def reentry(self):
        """Gets the reentry of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The reentry of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: str
        """
        return self._reentry

    @reentry.setter
    def reentry(self, reentry):
        """Sets the reentry of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param reentry: The reentry of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: str
        """

        self._reentry = reentry

    @property
    def rightclick(self):
        """Gets the rightclick of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The rightclick of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._rightclick

    @rightclick.setter
    def rightclick(self, rightclick):
        """Sets the rightclick of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param rightclick: The rightclick of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._rightclick = rightclick

    @property
    def tabs(self):
        """Gets the tabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The tabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: str
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """Sets the tabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param tabs: The tabs of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: str
        """

        self._tabs = tabs

    @property
    def verify(self):
        """Gets the verify of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The verify of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: list[str]
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """Sets the verify of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param verify: The verify of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: list[str]
        """

        self._verify = verify

    @property
    def whiteboard(self):
        """Gets the whiteboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501


        :return: The whiteboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :rtype: bool
        """
        return self._whiteboard

    @whiteboard.setter
    def whiteboard(self, whiteboard):
        """Sets the whiteboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.


        :param whiteboard: The whiteboard of this Apiv2coursescourseIdassignmentsIntegrations1Proctorio.  # noqa: E501
        :type: bool
        """

        self._whiteboard = whiteboard

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
        if issubclass(Apiv2coursescourseIdassignmentsIntegrations1Proctorio, dict):
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
        if not isinstance(other, Apiv2coursescourseIdassignmentsIntegrations1Proctorio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
