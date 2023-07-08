# Apiv2coursescourseIdassignmentsGradesSettings1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_calculation** | **OneOfapiv2coursescourseIdassignmentsGradesSettings1GradeCalculation** |  | [optional] 
**grade_formula** | **str** | The formula used to grade the assignment. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**rounding** | **OneOfapiv2coursescourseIdassignmentsGradesSettings1Rounding** |  | [optional] 
**grade_lower_bound** | **bool** | Enables the use of a lower bound for the grade. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**grade_lower_limit** | **str** | The lowest grade possible, this will only be active if the grade_lower_bound is true. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**grade_upper_bound** | **bool** | Enables the use of an upper bound for the grade. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**grade_upper_limit** | **str** | The highest grade possible, this will only be active if the grade_upper_bound is true. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**guess_correction** | **bool** | This option only takes multiple choice questions into account with one correct answer and not multiple choice questions with multiple correct answers. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**guess_correction_lower_bound** | **bool** | Limit the guess correction to zero. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 
**passed_grade** | **float** | The grade needed to pass the assignment. This attribute will default to the university setting if not provided in the request. If a question_bank_assignment_id is provided, but this attribute is not, the attribute value will default to the value in the provided question bank assignment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

