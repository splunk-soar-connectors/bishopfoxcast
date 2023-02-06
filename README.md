[comment]: # "Auto-generated SOAR connector documentation"
# Bishop Fox CAST

Publisher: Splunk Community  
Connector Version: 1\.1\.0  
Product Vendor: Bishop Fox  
Product Name: CAST  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.4\.0  

This app works with the Bishop Fox Continuous Attack Surface Testing \(CAST\) API to ingest and manage CAST findings

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a CAST asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_base\_url** |  required  | string | API Base URL
**verify\_server\_cert** |  required  | boolean | Verify Server Certificate
**auth\_token\_url** |  required  | string | Auth Token URL
**org\_id** |  required  | string | Organization ID
**api\_key** |  required  | password | API Key \(Client ID\)
**api\_secret** |  required  | password | API Secret \(Client Secret\)

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get findings](#action-get-findings) - Get findings based on provided filters  
[update status](#action-update-status) - Sets a findings's status  
[update client id](#action-update-client-id) - Updates a finding's clientId  
[update client note](#action-update-client-note) - Updates a finding's client note  
[on poll](#action-on-poll) - Ingest findings from Bishop Fox  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get findings'
Get findings based on provided filters

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**finding\_uid** |  optional  | Get a specific finding \(may have multiple subjects\) | string |  `bishopfox finding uid` 
**subject\_uid** |  optional  | Specify a specific subject\. This should only return 1 result | string |  `bishopfox subject uid` 
**since** |  optional  | Date parameter of the form 'YYYY\-MM\-DD' corresponding to the 'reportedAt' field of a finding\. Only findings published after this are returned | string | 
**status** |  optional  | Used to search for findings with a specific status\. Only findings with this status are returned | string |  `bishopfox status` 
**severity** |  optional  | Used to search for findings with a specific severity\. Only findings with this severity are returned | string |  `bishopfox severity` 
**client\_id** |  optional  | Used to search for a finding using the client defined identifier for a finding | string |  `bishopfox client id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.parameter\.finding\_uid | string |  `bishopfox finding uid`  |  
action\_result\.parameter\.subject\_uid | string |  `bishopfox subject uid`  |  
action\_result\.parameter\.since | string |  |  
action\_result\.parameter\.status | string |  `bishopfox status`  |  
action\_result\.parameter\.severity | string |  `bishopfox severity`  |  
action\_result\.parameter\.client\_id | string |  `bishopfox client id`  |  
action\_result\.data\.\*\.category | string |  |  
action\_result\.data\.\*\.clientId | string |  `bishopfox client id`  |  
action\_result\.data\.\*\.clientNote | string |  |  
action\_result\.data\.\*\.createdAt | string |  |  
action\_result\.data\.\*\.definition | string |  |  
action\_result\.data\.\*\.details | string |  |  
action\_result\.data\.\*\.findingId | string |  `bishopfox finding id`  |  
action\_result\.data\.\*\.findingUid | string |  `bishopfox finding uid`  |  
action\_result\.data\.\*\.orgUid | string |  `bishopfox org id`  |  
action\_result\.data\.\*\.recommendations | string |  |  
action\_result\.data\.\*\.remediatedAt | string |  |  
action\_result\.data\.\*\.remediatedDays | numeric |  |  
action\_result\.data\.\*\.report | string |  |  
action\_result\.data\.\*\.resources | string |  |  
action\_result\.data\.\*\.severity | string |  `bishopfox severity`  |  
action\_result\.data\.\*\.status | string |  `bishopfox status`  |  
action\_result\.data\.\*\.subject | string |  `bishopfox subject`  |  
action\_result\.data\.\*\.subjectUid | string |  `bishopfox subject uid`  |  
action\_result\.data\.\*\.target | string |  `bishopfox target`  |  
action\_result\.data\.\*\.updatedAt | string |  |  
action\_result\.data\.\*\.reportedAt | string |  |  
action\_result\.status | string |  |  
action\_result\.message | string |  |  
action\_result\.summary\.total\_findings | numeric |  |  
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'update status'
Sets a findings's status

Type: **generic**  
Read only: **False**

Sets an individual finding's status\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**finding\_uid** |  required  | Finding UUID | string |  `bishopfox finding uid` 
**subject\_uid** |  required  | Subject UUID | string |  `bishopfox subject uid` 
**status** |  required  | Status to set | string |  `bishopfox status` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.parameter\.finding\_uid | string |  `bishopfox finding uid`  |  
action\_result\.parameter\.subject\_uid | string |  `bishopfox subject uid`  |  
action\_result\.parameter\.status | string |  `bishopfox status`  |  
action\_result\.data\.\*\.clientNote | string |  |  
action\_result\.data\.\*\.createdAt | string |  |  
action\_result\.data\.\*\.findingUid | string |  `bishopfox finding uid`  |  
action\_result\.data\.\*\.remediatedAt | string |  |  
action\_result\.data\.\*\.remediatedDays | numeric |  |  
action\_result\.data\.\*\.status | string |  `bishopfox status`  |  
action\_result\.data\.\*\.subject | string |  `bishopfox subject`  |  
action\_result\.data\.\*\.subjectUid | string |  `bishopfox subject uid`  |  
action\_result\.data\.\*\.target | string |  `bishopfox target`  |  
action\_result\.data\.\*\.updatedAt | string |  |  
action\_result\.data\.\*\.clientId | string |  `bishopfox client id`  |  
action\_result\.status | string |  |  
action\_result\.message | string |  |  
action\_result\.summary | string |  |  
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'update client id'
Updates a finding's clientId

Type: **generic**  
Read only: **False**

Sets an individual finding's ClientID\. ClientID is an field that can be set to an identifier of your choice for easy access to a specific finding\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**finding\_uid** |  required  | Finding UUID | string |  `bishopfox finding uid` 
**subject\_uid** |  optional  | Subject UUID | string |  `bishopfox subject uid` 
**client\_id** |  required  | ClientID to set | string |  `bishopfox client id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.parameter\.finding\_uid | string |  `bishopfox finding uid`  |  
action\_result\.parameter\.subject\_uid | string |  `bishopfox subject uid`  |  
action\_result\.parameter\.client\_id | string |  `bishopfox client id`  |  
action\_result\.data\.\*\.clientId | string |  `bishopfox client id`  |  
action\_result\.data\.\*\.clientNote | string |  |  
action\_result\.data\.\*\.createdAt | string |  |  
action\_result\.data\.\*\.findingUid | string |  `bishopfox finding uid`  |  
action\_result\.data\.\*\.remediatedAt | string |  |  
action\_result\.data\.\*\.remediatedDays | numeric |  |  
action\_result\.data\.\*\.status | string |  `bishopfox status`  |  
action\_result\.data\.\*\.subject | string |  `bishopfox subject`  |  
action\_result\.data\.\*\.subjectUid | string |  `bishopfox subject uid`  |  
action\_result\.data\.\*\.target | string |  `bishopfox target`  |  
action\_result\.data\.\*\.updatedAt | string |  |  
action\_result\.status | string |  |  
action\_result\.message | string |  |  
action\_result\.summary | string |  |  
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'update client note'
Updates a finding's client note

Type: **generic**  
Read only: **False**

Sets an individual finding's client note\. The field 'clientNote' is for setting a note of your choice about this finding\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**finding\_uid** |  required  | Finding UUID | string |  `bishopfox finding uid` 
**subject\_uid** |  optional  | Subject UUID | string |  `bishopfox subject uid` 
**client\_note** |  required  | Client note to set | string |  `bishopfox client note` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action\_result\.parameter\.finding\_uid | string |  `bishopfox finding uid`  |  
action\_result\.parameter\.subject\_uid | string |  `bishopfox subject uid`  |  
action\_result\.parameter\.client\_note | string |  `bishopfox client note`  |  
action\_result\.data\.\*\.clientId | string |  `bishopfox client id`  |  
action\_result\.data\.\*\.clientNote | string |  |  
action\_result\.data\.\*\.createdAt | string |  |  
action\_result\.data\.\*\.findingUid | string |  `bishopfox finding uid`  |  
action\_result\.data\.\*\.remediatedAt | string |  |  
action\_result\.data\.\*\.remediatedDays | numeric |  |  
action\_result\.data\.\*\.status | string |  `bishopfox status`  |  
action\_result\.data\.\*\.subject | string |  `bishopfox subject`  |  
action\_result\.data\.\*\.subjectUid | string |  `bishopfox subject uid`  |  
action\_result\.data\.\*\.target | string |  `bishopfox target`  |  
action\_result\.data\.\*\.updatedAt | string |  |  
action\_result\.status | string |  |  
action\_result\.message | string |  |  
action\_result\.summary | string |  |  
summary\.total\_objects | numeric |  |   1 
summary\.total\_objects\_successful | numeric |  |   1   

## action: 'on poll'
Ingest findings from Bishop Fox

Type: **ingest**  
Read only: **True**

This ingesting findings from Bishop Fox CAST into containers in Splunk SOAR\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start\_time** |  optional  | Parameter ignored in this app | numeric | 
**end\_time** |  optional  | Parameter ignored in this app | numeric | 
**container\_id** |  optional  | Parameter ignored in this app | string | 
**container\_count** |  optional  | Maximum number of findings to be ingested during poll now | numeric | 
**artifact\_count** |  optional  | Parameter ignored in this app | numeric | 

#### Action Output
No Output