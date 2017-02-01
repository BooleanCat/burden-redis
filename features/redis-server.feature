Feature: Interacting with Redis
    In order to write burden-redis functionality
    As a software engineer
    I need a Redis server to be running

    Scenario: Set and get a key
        Given I set the key foo to bar
        When I read the key foo
        Then I expect the value to be bar
