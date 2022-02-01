# Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **str** | Default units for glucose measurements across the server. | [optional] 
**time_format** | **str** | Default time format | [optional] 
**custom_title** | **str** | Default custom title to be displayed system wide. | [optional] 
**night_mode** | **bool** | Should Night mode be enabled by default? | [optional] 
**theme** | **str** | Default theme to be displayed system wide, &#x60;default&#x60;, &#x60;colors&#x60;, &#x60;colorblindfriendly&#x60;. | [optional] 
**language** | **str** | Default language code to be used system wide | [optional] 
**show_plugins** | **str** | Plugins that should be shown by default | [optional] 
**show_rawbg** | **str** | If Raw BG is enabled when should it be shown? &#x60;never&#x60;, &#x60;always&#x60;, &#x60;noise&#x60; | [optional] 
**alarm_types** | **list[str]** | Enabled alarm types, can be multiple | [optional] 
**alarm_urgent_high** | **bool** | Enable/Disable client-side Urgent High alarms by default, for use with &#x60;simple&#x60; alarms. | [optional] 
**alarm_high** | **bool** | Enable/Disable client-side High alarms by default, for use with &#x60;simple&#x60; alarms. | [optional] 
**alarm_low** | **bool** | Enable/Disable client-side Low alarms by default, for use with &#x60;simple&#x60; alarms. | [optional] 
**alarm_urgent_low** | **bool** | Enable/Disable client-side Urgent Low alarms by default, for use with &#x60;simple&#x60; alarms. | [optional] 
**alarm_timeago_warn** | **bool** | Enable/Disable client-side stale data alarms by default. | [optional] 
**alarm_timeago_warn_mins** | **float** | Number of minutes before a stale data warning is generated. | [optional] 
**alarm_timeago_urgent** | **bool** | Enable/Disable client-side urgent stale data alarms by default. | [optional] 
**alarm_timeago_urgent_mins** | **float** | Number of minutes before a stale data warning is generated. | [optional] 
**enable** | **list[str]** | Enabled features | [optional] 
**thresholds** | [**Threshold**](Threshold.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

