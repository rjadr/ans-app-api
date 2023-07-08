# CoursesIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the course | 
**year** | **int** | The school year in which the course takes place. For example, select year 2022 for school year 2022/2023. Ans will select the current school year by default if no year is set | [optional] 
**course_code** | **str** | Code used to refer to the course | [optional] 
**self_enroll** | **bool** | Allows a student to enroll themselves in the course if set to true | [optional] [default to False]
**external_id** | **str** | An external id to reference the course | [optional] 
**trashed** | **bool** | Defines if a course has been soft deleted | [optional] [default to False]
**class_ids** | **list[int]** | An array of class ids that are part of the course | [optional] 
**study_ids** | **list[int]** | An array of study ids that the course belongs to | [optional] 
**period_ids** | **list[int]** | An array of period ids that the course takes place in | [optional] 
**learners** | [**list[Apiv2schoolsschoolIdcoursesLearners]**](Apiv2schoolsschoolIdcoursesLearners.md) | An array of user ids that will be in the course and have the learner role | [optional] 
**invigilators** | [**list[Apiv2schoolsschoolIdcoursesInvigilators]**](Apiv2schoolsschoolIdcoursesInvigilators.md) | An array of user ids that will be in the course that have the invigilator role | [optional] 
**reviewers** | [**list[Apiv2schoolsschoolIdcoursesInvigilators]**](Apiv2schoolsschoolIdcoursesInvigilators.md) | An array of user ids that will be in the course that have the reviewer role | [optional] 
**instructors** | [**list[Apiv2schoolsschoolIdcoursesInvigilators]**](Apiv2schoolsschoolIdcoursesInvigilators.md) | An array of user ids that will be in the course that have the instructor role | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

