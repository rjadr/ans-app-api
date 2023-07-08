# Apiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_calculation** | **OneOfapiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1GradeCalculation** |  | [optional] 
**rounding** | **OneOfapiv2questionBanksquestionBankIdquestionBankAssignmentsGradesSettings1Rounding** |  | [optional] 
**grade_formula** | **str** |  | [optional] [default to '1 + 9 * points / total']
**grade_lower_bound** | **bool** | Enables the use of a lower bound for the grade | [optional] [default to True]
**grade_lower_limit** | **float** | The lowest grade possible, this will only be active if the grade_lower_bound is true | [optional] [default to 1.0]
**grade_upper_bound** | **bool** | Enables the use of an upper bound for the grade | [optional] [default to True]
**grade_upper_limit** | **float** | The highest grade possible, this will only be active if the grade_upper_bound is true | [optional] [default to 10.0]
**passed_grade** | **float** | The grade needed to pass the assignment | [optional] [default to 5.5]
**guess_correction** | **bool** | Enables the use of guess correction for the grade | [optional] [default to False]
**guess_correction_lower_bound** | **bool** | Limit the guess correction to zero | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

