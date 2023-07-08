# CourseIdAssignmentsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the assignment | 
**assignment_type** | **OneOfcourseIdAssignmentsBodyAssignmentType** |  | [optional] 
**number_of_forms** | **int** | The amount of forms to be generated for written assignments. Increasing this amount will trigger the generation of forms | [optional] [default to 0]
**question_bank_assignment_id** | **int** | An id of a question bank assignment. When creating a new assignment with this attribute, all questions from the question bank assignment will be copied into the assignment. When updating an assignment, no action is taken | [optional] 
**summative** | **bool** | Defines if an assignment is summative if set to true, formative if set to false | [optional] 
**external_id** | **str** | An external id to reference the assignment | [optional] 
**label_id** | **int** | A label id to set the label on the assignment | [optional] 
**trashed** | **bool** | Defines if an assignment has been soft deleted | [optional] [default to False]
**accessibility_settings** | [**Apiv2coursescourseIdassignmentsAccessibilitySettings1**](Apiv2coursescourseIdassignmentsAccessibilitySettings1.md) |  | [optional] 
**grades_settings** | [**Apiv2coursescourseIdassignmentsGradesSettings1**](Apiv2coursescourseIdassignmentsGradesSettings1.md) |  | [optional] 
**integrations** | [**Apiv2coursescourseIdassignmentsIntegrations1**](Apiv2coursescourseIdassignmentsIntegrations1.md) |  | [optional] 
**exercise_reviewers** | [**list[Apiv2coursescourseIdassignmentsExerciseReviewers]**](Apiv2coursescourseIdassignmentsExerciseReviewers.md) |  | [optional] 
**group_reviewers** | [**list[Apiv2coursescourseIdassignmentsGroupReviewers]**](Apiv2coursescourseIdassignmentsGroupReviewers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

