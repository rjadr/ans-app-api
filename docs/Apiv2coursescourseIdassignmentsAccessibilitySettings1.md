# Apiv2coursescourseIdassignmentsAccessibilitySettings1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** | The amount of attempts students get to take the assignment | [optional] 
**password** | **str** | A password required to enter the assingment | [optional] 
**restricted_access_to_other_pages** | **bool** | Prevents the user from opening other assignments in Ans while taking this assignment | [optional] 
**restricted_ip_access** | **bool** | Defines whether access should be restricted based on IP. Set location_ids to limit access to those locations | [optional] 
**location_ids** | **list[int]** | An array of location ids the assignment may be accessed from | [optional] 
**notes** | **bool** | Allows students to take digital notes during their assignment | [optional] 
**spellchecker** | **bool** | Allows students to use spell checking | [optional] 
**config_keys** | **list[int]** | Lockdown browser hash to sha256 with the request url and is compared to the configKeyHash sent in the request headers | [optional] 
**calculator** | **OneOfapiv2coursescourseIdassignmentsAccessibilitySettings1Calculator** |  | [optional] 
**feedback** | **bool** | Allows students to receive feedback during the assignment | [optional] 
**forced_test_navigation** | **bool** | Students may only answer questions once; they may not return to an exercise that they closed | [optional] 
**cannot_reopen_question_groups** | **bool** | Prevents students from reopening a flow group after closing | [optional] 
**seb_server_enabled** | **bool** | Restrict access to the assignment to Safe Exam Browser only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

