*** Settings ***
Library    RequestsLibrary
Library    SearchModule.py


*** Keywords ***
The Result Of Asking For ${PER_PAGE} Items Should Result In ${RESULT} Items
    [Documentation]    The default number of items returned is 30 if no per page value (or null) is passed.
    ${RESULT} =    Get Number Of Items On First Page    ${PER_PAGE}
    Run Keyword If    ${PER_PAGE} != ${None}    Should Be Equal As Strings    ${RESULT}    ${PER_PAGE}
    ...    ELSE    Should Be Equal As Strings    ${RESULT}    30


*** Test Cases ***
Make Request With Invalid Parameter
    Create Session    github    https://api.github.com
    ${resp} =    Get Request    github    /search/repositories?jv=test
    Log    ${resp.json()}
    Should Be Equal As Strings    ${resp.status_code}    422

Multiple Per Page Item Count For First Page
    [Template]    The Result Of Asking For ${PER_PAGE} Items Should Result In ${RESULT} Items
    5    5
    1    1
    37    37
    ${None}    30

Validate Search Returns Results With Stars
    Verify First Five Pages Contain Results With Stars Greater Than    100