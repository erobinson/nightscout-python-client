# Xdripjs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **float** | CGM Sensor Session State Code | [optional] 
**state_string** | **str** | CGM Sensor Session State String | [optional] 
**state_string_short** | **str** | CGM Sensor Session State Short String | [optional] 
**tx_id** | **str** | CGM Transmitter ID | [optional] 
**tx_status** | **float** | CGM Transmitter Status | [optional] 
**tx_status_string** | **str** | CGM Transmitter Status String | [optional] 
**tx_status_string_short** | **str** | CGM Transmitter Status Short String | [optional] 
**tx_activation** | **float** | CGM Transmitter Activation Milliseconds After Epoch | [optional] 
**mode** | **str** | Mode xdrip-js Application Operationg: expired, not expired, etc. | [optional] 
**timestamp** | **float** | Last Update Milliseconds After Epoch | [optional] 
**rssi** | **float** | Receive Signal Strength of Transmitter | [optional] 
**unfiltered** | **float** | Most Recent Raw Unfiltered Glucose | [optional] 
**filtered** | **float** | Most Recent Raw Filtered Glucose | [optional] 
**noise** | **float** | Calculated Noise Value - 1&#x3D;Clean, 2&#x3D;Light, 3&#x3D;Medium, 4&#x3D;Heavy | [optional] 
**noise_string** | **float** | Noise Value String | [optional] 
**slope** | **float** | Calibration Slope Value | [optional] 
**intercept** | **float** | Calibration Intercept Value | [optional] 
**cal_type** | **str** | Algorithm Used to Calculate Calibration Values | [optional] 
**last_calibration_date** | **float** | Most Recent Calibration Milliseconds After Epoch | [optional] 
**session_start** | **float** | Sensor Session Start Milliseconds After Epoch | [optional] 
**battery_timestamp** | **float** | Most Recent Batter Status Read Milliseconds After Epoch | [optional] 
**voltagea** | **float** | Voltage of Battery A | [optional] 
**voltageb** | **float** | Voltage of Battery B | [optional] 
**temperature** | **float** | Transmitter Temperature | [optional] 
**resistance** | **float** | Sensor Resistance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

