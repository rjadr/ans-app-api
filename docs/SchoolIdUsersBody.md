# SchoolIdUsersBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_number** | **int** | A unique set of numbers which is required for students (validated against the length set on the school) | [optional] 
**first_name** | **str** | The first name of a user | [optional] 
**middle_name** | **str** | The middle name of a user | [optional] 
**last_name** | **str** | The last name of a user | [optional] 
**email** | **str** | The email tied to the user account | 
**role** | **OneOfschoolIdUsersBodyRole** |  | [optional] 
**role_id** | **int** | A custom role id when using custom defined roles | [optional] 
**active** | **bool** | Displays whether a user is active, if false the user will be shown a screen telling them that their account is disabled | [optional] [default to True]
**trashed** | **bool** | Defines if a user has been soft deleted | [optional] [default to False]
**alumni** | **bool** | Defines if a user is an alumni | [optional] [default to False]
**uid** | **str** | A unique id for the user which is used for SSO | [optional] 
**external_id** | **str** | An external id to reference the user | [optional] 
**courses** | [**list[Apiv2schoolsschoolIdusersCourses]**](Apiv2schoolsschoolIdusersCourses.md) |  | [optional] 
**question_banks** | [**list[Apiv2schoolsschoolIdusersQuestionBanks]**](Apiv2schoolsschoolIdusersQuestionBanks.md) |  | [optional] 
**department_ids** | **list[int]** | An array of department ids which the user will be added to. This field is ignored for any role except operators | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

