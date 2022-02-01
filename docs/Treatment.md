# Treatment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internally assigned id. | [optional] 
**event_type** | **str** | The type of treatment event. | [optional] 
**created_at** | **str** | The date of the event, might be set retroactively . | [optional] 
**glucose** | **str** | Current glucose. | [optional] 
**glucose_type** | **str** | Method used to obtain glucose, Finger or Sensor. | [optional] 
**carbs** | **float** |  Amount of carbs consumed in grams. | [optional] 
**protein** | **float** |  Amount of protein consumed in grams. | [optional] 
**fat** | **float** |  Amount of fat consumed in grams. | [optional] 
**insulin** | **float** | Amount of insulin, if any. | [optional] 
**units** | **str** | The units for the glucose value, mg/dl or mmol. | [optional] 
**transmitter_id** | **str** | The transmitter ID of the transmitter being started. | [optional] 
**sensor_code** | **str** | The code used to start a Dexcom G6 sensor. | [optional] 
**notes** | **str** | Description/notes of treatment. | [optional] 
**entered_by** | **str** | Who entered the treatment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

