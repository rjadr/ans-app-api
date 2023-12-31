# coding: utf-8

# flake8: noqa
"""
    API V2

    #### Authorization The API can only be accessed by creating a token at: [https://ans.app/users/tokens](https://ans.app/users/tokens).<br> The provided token is a Bearer token and needs to be set in the Request Header with key Authorization and value \"Bearer [token]\" for every request.<br>  #### Pagination The API generates several headers due to its use of pagination, this includes:      - Link, the standard link header defined in RFC 8288     - Current-Page, which shows the current page of the requested data     - Page-Items, which shows the amount of items per page     - Total-Pages, which shows the total amount of pages available     - Total-Count, which shows the total count of objects that was requested  #### Rate Limits The API enforces a rate limit of 500 request per minute per ip-address. If the rate limit is exceeded, the API responds with a HTTP 429 Too Many Requests response code.<br> You can use the following response headers to confirm the current rate limit and monitor the number of requests remaining in the current minute.<br>      - RateLimit-Limit, the current limit for your account     - RateLimit-Remaining, the number of remaining requests in the current minute     - RateLimit-Reset, the number of seconds until the limit is reset  #### Search The API offers search functionality through GET requests with a query. For all search endpoints see the [Search](#/Search) section.<br>      - The query must consist of the attribute and the search value connected with a colon (:) or a greater than (>) or smaller than (<) sign.     - You can use the greater and smaller than symbols for numeric and date values.     - If your search value contains whitespaces, you must quote your search query with single or double quotes.     - You can also combine searches by using a whitespace to separate the attributes.     - If your search value is equal to \"null\", all records with null values for that attribute will be found.     - We perform case sensitive exact match searches only.     - You can search for multiple values, by adding square brackets around the search parameters and seperating the parameters using commas without spaces.     - You can see some example queries in the documented search endpoints.   #### Webhooks The API offers you the ability to listen to specific events that occur within the application. For example, you can use webhooks to:      - Archive results when an assignment is archived     - Add users after an assignment is created     - Export a result after it has been approved  When creating a webhook you can specify which events you want to listen to. You can listen to all events, all events for a specific object or only one event for an object.<br> You can listen to 'create', 'update' and 'destroy' events on an object or a combination for example:      - '*' - all events for all objects     - 'assignment' - All events for an assignment     - 'assignment.update' - Only notify when an assignment is updated  The webhooks API returns a secret after creating a new webhook. This secret can be used to verify that the webhook call comes from Ans by creating a sha256 HMAC with the request body and this secret and comparing it to the X-Ans-Signature Header.<br>  Webhook requests are automatically retried up to five times if the endpoint returns certain HTTP response codes. The time interval between retries is gradually extended. Every webhook event is logged and contains the response code, headers and body of the response for debugging purposes.<br>  The following objects are currently supported:      - Assignment     - Result     - User   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from ans_app_api.models.apiv2coursescourse_idassignments_accessibility_settings import Apiv2coursescourseIdassignmentsAccessibilitySettings
from ans_app_api.models.apiv2coursescourse_idassignments_accessibility_settings1 import Apiv2coursescourseIdassignmentsAccessibilitySettings1
from ans_app_api.models.apiv2coursescourse_idassignments_exercise_reviewers import Apiv2coursescourseIdassignmentsExerciseReviewers
from ans_app_api.models.apiv2coursescourse_idassignments_grades_settings import Apiv2coursescourseIdassignmentsGradesSettings
from ans_app_api.models.apiv2coursescourse_idassignments_grades_settings1 import Apiv2coursescourseIdassignmentsGradesSettings1
from ans_app_api.models.apiv2coursescourse_idassignments_group_reviewers import Apiv2coursescourseIdassignmentsGroupReviewers
from ans_app_api.models.apiv2coursescourse_idassignments_integrations import Apiv2coursescourseIdassignmentsIntegrations
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1 import Apiv2coursescourseIdassignmentsIntegrations1
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_exam_services import Apiv2coursescourseIdassignmentsIntegrations1ExamServices
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_ouriginal import Apiv2coursescourseIdassignmentsIntegrations1Ouriginal
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_proctor_exam import Apiv2coursescourseIdassignmentsIntegrations1ProctorExam
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_proctorio import Apiv2coursescourseIdassignmentsIntegrations1Proctorio
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowser
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser_config import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfig
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_permitted_processes import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigPermittedProcesses
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_prohibited_processes import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigProhibitedProcesses
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_url_filter_rules import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigURLFilterRules
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_safe_exam_browser_server import Apiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserServer
from ans_app_api.models.apiv2coursescourse_idassignments_integrations1_step import Apiv2coursescourseIdassignmentsIntegrations1Step
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowser
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser_config import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserConfig
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser_config_permitted_processes import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserConfigPermittedProcesses
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser_config_prohibited_processes import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserConfigProhibitedProcesses
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser_config_url_filter_rules import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserConfigURLFilterRules
from ans_app_api.models.apiv2coursescourse_idassignments_integrations_safe_exam_browser_server import Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserServer
from ans_app_api.models.apiv2question_banksquestion_bank_idquestion_bank_assignments_grades_settings import Apiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings
from ans_app_api.models.apiv2question_banksquestion_bank_idquestion_bank_assignments_grades_settings1 import Apiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1
from ans_app_api.models.apiv2question_banksquestion_bank_idquestion_bank_exercises_tags import Apiv2questionBanksquestionBankIdquestionBankExercisesTags
from ans_app_api.models.apiv2schoolsschool_idcourses_invigilators import Apiv2schoolsschoolIdcoursesInvigilators
from ans_app_api.models.apiv2schoolsschool_idcourses_learners import Apiv2schoolsschoolIdcoursesLearners
from ans_app_api.models.apiv2schoolsschool_idusers_courses import Apiv2schoolsschoolIdusersCourses
from ans_app_api.models.apiv2schoolsschool_idusers_question_banks import Apiv2schoolsschoolIdusersQuestionBanks
from ans_app_api.models.apiv2webhooks_events import Apiv2webhooksEvents
from ans_app_api.models.assignment_id_cover_body import AssignmentIdCoverBody
from ans_app_api.models.assignment_id_exercises_body import AssignmentIdExercisesBody
from ans_app_api.models.assignment_id_publication_body import AssignmentIdPublicationBody
from ans_app_api.models.assignment_id_publication_timeslots_body import AssignmentIdPublicationTimeslotsBody
from ans_app_api.models.assignment_id_requirements_body import AssignmentIdRequirementsBody
from ans_app_api.models.assignment_id_results_body import AssignmentIdResultsBody
from ans_app_api.models.assignment_id_score_marks_body import AssignmentIdScoreMarksBody
from ans_app_api.models.assignment_id_tasks_body import AssignmentIdTasksBody
from ans_app_api.models.assignment_id_timeslots_body import AssignmentIdTimeslotsBody
from ans_app_api.models.assignments_id_body import AssignmentsIdBody
from ans_app_api.models.background_jobs_id_body import BackgroundJobsIdBody
from ans_app_api.models.class_id_courses_classes_body import ClassIdCoursesClassesBody
from ans_app_api.models.classes_id_body import ClassesIdBody
from ans_app_api.models.comments_id_body import CommentsIdBody
from ans_app_api.models.course_id_assignments_body import CourseIdAssignmentsBody
from ans_app_api.models.course_id_courses_classes_body import CourseIdCoursesClassesBody
from ans_app_api.models.course_id_courses_users_body import CourseIdCoursesUsersBody
from ans_app_api.models.course_id_domains_body import CourseIdDomainsBody
from ans_app_api.models.course_id_groups_body import CourseIdGroupsBody
from ans_app_api.models.courses_id_body import CoursesIdBody
from ans_app_api.models.courses_users_id_body import CoursesUsersIdBody
from ans_app_api.models.department_id_studies_body import DepartmentIdStudiesBody
from ans_app_api.models.departments_id_body import DepartmentsIdBody
from ans_app_api.models.domain_id_objectives_body import DomainIdObjectivesBody
from ans_app_api.models.domains_id_body import DomainsIdBody
from ans_app_api.models.exercise_id_questions_body import ExerciseIdQuestionsBody
from ans_app_api.models.exercises_id_body import ExercisesIdBody
from ans_app_api.models.group_id_groups_users_body import GroupIdGroupsUsersBody
from ans_app_api.models.groups_id_body import GroupsIdBody
from ans_app_api.models.inline_response200 import InlineResponse200
from ans_app_api.models.inline_response2001 import InlineResponse2001
from ans_app_api.models.inline_response20010 import InlineResponse20010
from ans_app_api.models.inline_response20011 import InlineResponse20011
from ans_app_api.models.inline_response20012 import InlineResponse20012
from ans_app_api.models.inline_response20013 import InlineResponse20013
from ans_app_api.models.inline_response20014 import InlineResponse20014
from ans_app_api.models.inline_response20015 import InlineResponse20015
from ans_app_api.models.inline_response20016 import InlineResponse20016
from ans_app_api.models.inline_response20017 import InlineResponse20017
from ans_app_api.models.inline_response20018 import InlineResponse20018
from ans_app_api.models.inline_response20019 import InlineResponse20019
from ans_app_api.models.inline_response20019_assignments import InlineResponse20019Assignments
from ans_app_api.models.inline_response2002 import InlineResponse2002
from ans_app_api.models.inline_response20020 import InlineResponse20020
from ans_app_api.models.inline_response20021 import InlineResponse20021
from ans_app_api.models.inline_response20022 import InlineResponse20022
from ans_app_api.models.inline_response20023 import InlineResponse20023
from ans_app_api.models.inline_response20023_exercise import InlineResponse20023Exercise
from ans_app_api.models.inline_response20023_proctor_exam import InlineResponse20023ProctorExam
from ans_app_api.models.inline_response20023_proctor_exam_student_session import InlineResponse20023ProctorExamStudentSession
from ans_app_api.models.inline_response20023_result import InlineResponse20023Result
from ans_app_api.models.inline_response20023_user import InlineResponse20023User
from ans_app_api.models.inline_response20024 import InlineResponse20024
from ans_app_api.models.inline_response20025 import InlineResponse20025
from ans_app_api.models.inline_response20025_scores import InlineResponse20025Scores
from ans_app_api.models.inline_response20026 import InlineResponse20026
from ans_app_api.models.inline_response20027 import InlineResponse20027
from ans_app_api.models.inline_response20028 import InlineResponse20028
from ans_app_api.models.inline_response20029 import InlineResponse20029
from ans_app_api.models.inline_response20029_courses import InlineResponse20029Courses
from ans_app_api.models.inline_response20029_departments import InlineResponse20029Departments
from ans_app_api.models.inline_response20029_question_banks import InlineResponse20029QuestionBanks
from ans_app_api.models.inline_response2003 import InlineResponse2003
from ans_app_api.models.inline_response20030 import InlineResponse20030
from ans_app_api.models.inline_response2004 import InlineResponse2004
from ans_app_api.models.inline_response2005 import InlineResponse2005
from ans_app_api.models.inline_response2006 import InlineResponse2006
from ans_app_api.models.inline_response2007 import InlineResponse2007
from ans_app_api.models.inline_response2008 import InlineResponse2008
from ans_app_api.models.inline_response2009 import InlineResponse2009
from ans_app_api.models.inline_response201 import InlineResponse201
from ans_app_api.models.inline_response2011 import InlineResponse2011
from ans_app_api.models.inline_response2011_courses import InlineResponse2011Courses
from ans_app_api.models.inline_response2011_users import InlineResponse2011Users
from ans_app_api.models.inline_response2012 import InlineResponse2012
from ans_app_api.models.inline_response2012_classes import InlineResponse2012Classes
from ans_app_api.models.inline_response2012_periods import InlineResponse2012Periods
from ans_app_api.models.inline_response2012_studies import InlineResponse2012Studies
from ans_app_api.models.inline_response2013 import InlineResponse2013
from ans_app_api.models.inline_response2014 import InlineResponse2014
from ans_app_api.models.inline_response2015 import InlineResponse2015
from ans_app_api.models.inline_response2015_users import InlineResponse2015Users
from ans_app_api.models.inline_response2016 import InlineResponse2016
from ans_app_api.models.inline_response2016_cells import InlineResponse2016Cells
from ans_app_api.models.inline_response2016_choices import InlineResponse2016Choices
from ans_app_api.models.inline_response2016_criteria import InlineResponse2016Criteria
from ans_app_api.models.inline_response2016_rows import InlineResponse2016Rows
from ans_app_api.models.inline_response2017 import InlineResponse2017
from ans_app_api.models.inline_response2017_files import InlineResponse2017Files
from ans_app_api.models.inline_response2017_review_requests import InlineResponse2017ReviewRequests
from ans_app_api.models.inline_response2017_reviews import InlineResponse2017Reviews
from ans_app_api.models.inline_response2017_submissions import InlineResponse2017Submissions
from ans_app_api.models.inline_response2017_variables import InlineResponse2017Variables
from ans_app_api.models.inline_response2018 import InlineResponse2018
from ans_app_api.models.inline_response201_accessibility_settings import InlineResponse201AccessibilitySettings
from ans_app_api.models.inline_response201_exercise_reviewers import InlineResponse201ExerciseReviewers
from ans_app_api.models.inline_response201_group_reviewers import InlineResponse201GroupReviewers
from ans_app_api.models.inline_response201_integrations import InlineResponse201Integrations
from ans_app_api.models.inline_response201_integrations_exam_services import InlineResponse201IntegrationsExamServices
from ans_app_api.models.inline_response201_integrations_ouriginal import InlineResponse201IntegrationsOuriginal
from ans_app_api.models.inline_response201_integrations_proctor_exam import InlineResponse201IntegrationsProctorExam
from ans_app_api.models.inline_response201_integrations_proctorio import InlineResponse201IntegrationsProctorio
from ans_app_api.models.inline_response201_integrations_schoolyear import InlineResponse201IntegrationsSchoolyear
from ans_app_api.models.inline_response201_integrations_step import InlineResponse201IntegrationsStep
from ans_app_api.models.inline_response201_requirements import InlineResponse201Requirements
from ans_app_api.models.labels_id_body import LabelsIdBody
from ans_app_api.models.locations_id_body import LocationsIdBody
from ans_app_api.models.objectives_id_body import ObjectivesIdBody
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_accessibility_settings1_calculator import OneOfapiv2coursescourseIdassignmentsAccessibilitySettings1Calculator
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_grades_settings1_grade_calculation import OneOfapiv2coursescourseIdassignmentsGradesSettings1GradeCalculation
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_grades_settings1_rounding import OneOfapiv2coursescourseIdassignmentsGradesSettings1Rounding
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_browser_view_mode import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigBrowserViewMode
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_choose_file_to_upload_policy import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigChooseFileToUploadPolicy
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_new_browser_window_by_link_policy import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigNewBrowserWindowByLinkPolicy
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_permitted_processes_os import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigPermittedProcessesOs
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_prohibited_processes_os import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigProhibitedProcessesOs
from ans_app_api.models.one_ofapiv2coursescourse_idassignments_integrations1_safe_exam_browser_config_url_filter_rules_action import OneOfapiv2coursescourseIdassignmentsIntegrations1SafeExamBrowserConfigURLFilterRulesAction
from ans_app_api.models.one_ofapiv2question_banksquestion_bank_idquestion_bank_assignments_grades_settings1_grade_calculation import OneOfapiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1GradeCalculation
from ans_app_api.models.one_ofapiv2question_banksquestion_bank_idquestion_bank_assignments_grades_settings1_rounding import OneOfapiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1Rounding
from ans_app_api.models.one_ofapiv2schoolsschool_idusers_courses_role import OneOfapiv2schoolsschoolIdusersCoursesRole
from ans_app_api.models.one_ofapiv2schoolsschool_idusers_question_banks_role import OneOfapiv2schoolsschoolIdusersQuestionBanksRole
from ans_app_api.models.one_ofassignment_id_cover_body_enumerate_exercises import OneOfassignmentIdCoverBodyEnumerateExercises
from ans_app_api.models.one_ofassignment_id_requirements_body_action_type import OneOfassignmentIdRequirementsBodyActionType
from ans_app_api.models.one_ofassignments_id_body_assignment_type import OneOfassignmentsIdBodyAssignmentType
from ans_app_api.models.one_ofbackground_jobs_id_body_status import OneOfbackgroundJobsIdBodyStatus
from ans_app_api.models.one_ofcourse_id_assignments_body_assignment_type import OneOfcourseIdAssignmentsBodyAssignmentType
from ans_app_api.models.one_ofcourse_id_courses_users_body_role import OneOfcourseIdCoursesUsersBodyRole
from ans_app_api.models.one_ofcourses_users_id_body_role import OneOfcoursesUsersIdBodyRole
from ans_app_api.models.one_ofexercise_id_questions_body_category import OneOfexerciseIdQuestionsBodyCategory
from ans_app_api.models.one_ofexercise_id_questions_body_choice_type import OneOfexerciseIdQuestionsBodyChoiceType
from ans_app_api.models.one_ofexercise_id_questions_body_grading_type import OneOfexerciseIdQuestionsBodyGradingType
from ans_app_api.models.one_ofexercise_id_questions_body_layout import OneOfexerciseIdQuestionsBodyLayout
from ans_app_api.models.one_oflabels_id_body_color import OneOflabelsIdBodyColor
from ans_app_api.models.one_ofquestion_bank_assignment_id_cover_body_enumerate_exercises import OneOfquestionBankAssignmentIdCoverBodyEnumerateExercises
from ans_app_api.models.one_ofquestion_bank_id_question_bank_labels_body_color import OneOfquestionBankIdQuestionBankLabelsBodyColor
from ans_app_api.models.one_ofquestion_bank_labels_id_body_color import OneOfquestionBankLabelsIdBodyColor
from ans_app_api.models.one_ofquestions_id_body_category import OneOfquestionsIdBodyCategory
from ans_app_api.models.one_ofquestions_id_body_choice_type import OneOfquestionsIdBodyChoiceType
from ans_app_api.models.one_ofquestions_id_body_grading_type import OneOfquestionsIdBodyGradingType
from ans_app_api.models.one_ofquestions_id_body_layout import OneOfquestionsIdBodyLayout
from ans_app_api.models.one_ofrequirements_id_body_action_type import OneOfrequirementsIdBodyActionType
from ans_app_api.models.one_ofschool_id_labels_body_color import OneOfschoolIdLabelsBodyColor
from ans_app_api.models.one_ofschool_id_users_body_role import OneOfschoolIdUsersBodyRole
from ans_app_api.models.one_ofuser_id_courses_users_body_role import OneOfuserIdCoursesUsersBodyRole
from ans_app_api.models.one_ofusers_id_body_role import OneOfusersIdBodyRole
from ans_app_api.models.one_ofv2_comments_body_commentable_type import OneOfv2CommentsBodyCommentableType
from ans_app_api.models.periods_id_body import PeriodsIdBody
from ans_app_api.models.plan_id_subscriptions_body import PlanIdSubscriptionsBody
from ans_app_api.models.plans_id_body import PlansIdBody
from ans_app_api.models.publication_timeslots_id_body import PublicationTimeslotsIdBody
from ans_app_api.models.publisher_id_plans_body import PublisherIdPlansBody
from ans_app_api.models.question_bank_assignment_id_cover_body import QuestionBankAssignmentIdCoverBody
from ans_app_api.models.question_bank_assignment_id_score_marks_body import QuestionBankAssignmentIdScoreMarksBody
from ans_app_api.models.question_bank_assignments_id_body import QuestionBankAssignmentsIdBody
from ans_app_api.models.question_bank_exercises_id_body import QuestionBankExercisesIdBody
from ans_app_api.models.question_bank_id_domains_body import QuestionBankIdDomainsBody
from ans_app_api.models.question_bank_id_question_bank_assignments_body import QuestionBankIdQuestionBankAssignmentsBody
from ans_app_api.models.question_bank_id_question_bank_exercises_body import QuestionBankIdQuestionBankExercisesBody
from ans_app_api.models.question_bank_id_question_bank_labels_body import QuestionBankIdQuestionBankLabelsBody
from ans_app_api.models.question_bank_id_tasks_body import QuestionBankIdTasksBody
from ans_app_api.models.question_bank_labels_id_body import QuestionBankLabelsIdBody
from ans_app_api.models.question_banks_id_body import QuestionBanksIdBody
from ans_app_api.models.questions_id_body import QuestionsIdBody
from ans_app_api.models.requirements_id_body import RequirementsIdBody
from ans_app_api.models.result_id_files_body import ResultIdFilesBody
from ans_app_api.models.results_id_body import ResultsIdBody
from ans_app_api.models.school_id_classes_body import SchoolIdClassesBody
from ans_app_api.models.school_id_courses_body import SchoolIdCoursesBody
from ans_app_api.models.school_id_departments_body import SchoolIdDepartmentsBody
from ans_app_api.models.school_id_labels_body import SchoolIdLabelsBody
from ans_app_api.models.school_id_locations_body import SchoolIdLocationsBody
from ans_app_api.models.school_id_periods_body import SchoolIdPeriodsBody
from ans_app_api.models.school_id_users_body import SchoolIdUsersBody
from ans_app_api.models.schools_id_body import SchoolsIdBody
from ans_app_api.models.score_marks_id_body import ScoreMarksIdBody
from ans_app_api.models.studies_id_body import StudiesIdBody
from ans_app_api.models.submissions_id_body import SubmissionsIdBody
from ans_app_api.models.subscriptions_id_body import SubscriptionsIdBody
from ans_app_api.models.tasks_id_body import TasksIdBody
from ans_app_api.models.timeslots_id_body import TimeslotsIdBody
from ans_app_api.models.user_id_courses_users_body import UserIdCoursesUsersBody
from ans_app_api.models.user_id_groups_users_body import UserIdGroupsUsersBody
from ans_app_api.models.users_id_body import UsersIdBody
from ans_app_api.models.v2_comments_body import V2CommentsBody
from ans_app_api.models.v2_question_banks_body import V2QuestionBanksBody
from ans_app_api.models.v2_webhooks_body import V2WebhooksBody
from ans_app_api.models.webhooks_id_body import WebhooksIdBody
