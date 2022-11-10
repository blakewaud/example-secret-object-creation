*** Settings ***
Documentation       Template robot main suite.

Library             SecretObject.py


*** Tasks ***
Demonstrate secret object usage
    ${this_is_secret}=    Create secret object
    ...    my_precious
    ...    the one ring
    ...    color=gold
    ...    inscription=One Ring to rule them all, One ring to find them; One ring to bring them all and in the darkness bind them.
    Log    ${this_is_secret}
    ${got_value}=    Evaluate    $this_is_secret['inscription']
    Log    ${got_value}
