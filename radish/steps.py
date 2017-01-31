import redis
from expects import *
from radish import given, when, then


@given("I set the key {key:w} to {value:w}")
def have_numbers(step, key, value):
    client = redis.StrictRedis()
    client.set(key, value)


@when("I read the key {key:w}")
def sum_numbers(step, key):
    client = redis.StrictRedis()
    step.context.value = client.get(key).decode('utf-8')


@then("I expect the value to be {value:w}")
def expect_result(step, value):
    expect(step.context.value).to(equal(value))
