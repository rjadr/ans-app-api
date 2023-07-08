# AssignmentIdTimeslotsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_datetime** | **str** | The date and time at which the assignment opens | [optional] 
**deadline_datetime** | **str** | The date and time at which the assignment ends | [optional] 
**duration** | **int** | Amount of time in minutes the students have to make the exam | [optional] 
**group_id** | **int** | The id of the group for which the exam opens, null if a klass id is present or both group_id and klass_id null if all students are selected | [optional] 
**klass_id** | **int** | The id of the klass for which the exam opens, null if a group id is present or both group_id and klass_id null if all students are selected | [optional] 
**external_id** | **str** | An external id to reference the timeslot | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

