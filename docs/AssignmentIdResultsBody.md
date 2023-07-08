# AssignmentIdResultsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | Determines whether a result is approved, disapproved or undetermined. True will approve the result, false will disapprove it and null will mark it as undetermined | [optional] 
**trashed** | **bool** | Determines whether a result has been soft deleted | [optional] [default to False]
**status** | **str** | Determines the status of a result. Update the status to &#x27;submitted&#x27; after uploading the student files to enable grading for this result | [optional] [default to 'new']
**external_id** | **str** | An external id to reference the result | [optional] 
**user_id** | **int** | The id of the user, null if the result is for a group assignment. Can only be set on creation and cannot be changed on existing results | [optional] 
**group_id** | **int** | The id of the group, null if the result is for an individual assignment. Can only be set on creation and cannot be changed on existing results | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

