# ExerciseIdQuestionsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | **bool** | Defines if the question is a bonus question | [optional] [default to False]
**category** | **OneOfexerciseIdQuestionsBodyCategory** |  | [optional] 
**choice_type** | **OneOfexerciseIdQuestionsBodyChoiceType** |  | [optional] 
**layout** | **OneOfexerciseIdQuestionsBodyLayout** |  | [optional] 
**content** | **str** | The content of the question | 
**fill_content** | **str** | The content for a fill in the blanks question with a gap | [optional] 
**feedback_correct** | **str** | The feedback displayed if the question is correct | [optional] 
**feedback_incorrect** | **str** | The feedback displayed if the question is completely incorrect | [optional] 
**feedback_mistake** | **str** | The feedback displayed if the question is partially correct | [optional] 
**grading_description** | **str** | A description displayed when grading the question | [optional] 
**grading_type** | **OneOfexerciseIdQuestionsBodyGradingType** |  | [optional] 
**max_bound** | **bool** | Indicates if the student’s score is limited to the amount of question points | [optional] [default to True]
**new_page** | **bool** | Defines whether the question will start on a new page (handwritten tests only) | [optional] [default to False]
**partial_scoring** | **bool** | Defines whether a student can receive partial scores on this question | [optional] [default to True]
**points** | **str** | Defines the number of points allocated to this question | [optional] 
**predefined_answer** | **str** | Defines the question&#x27;s predefined answer (digital test only for question types open and code) | [optional] 
**skippable** | **bool** | Indicates that this question can be skipped by students who have the right to skip questions | [optional] [default to False]
**stack_vertically** | **bool** | Forces the question&#x27;s multiple choice options to be stacked vertically | [optional] [default to False]
**start_with_zero** | **bool** | The marking of the question will always start at zero points | [optional] [default to True]
**word_limit** | **int** | Defines the question&#x27;s word limit. If this value is 0, then the question has no word limit | [optional] [default to 0]
**zero_bound** | **bool** | Indicates if the student&#x27;s score cannot be lower than zero | [optional] [default to True]
**objective_ids** | **list[int]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

