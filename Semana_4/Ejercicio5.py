counter = 1
passed = 0
failed = 0
average_passed = 0
average_failed = 0
average = 0

print("Provide your tests and I will show you how many you passed, failed, and an average for both")
total_tests = int(input("How many tests have you done? "))

while (counter <= total_tests):
    current_score = int(input(f"What score did you have for test number {counter}: "))
    counter = counter + 1
    average = average + (current_score / total_tests) 
    if (current_score < 70):
        failed = failed + 1
        average_failed = average_failed + current_score
    else:
        passed = passed + 1
        average_passed = average_passed + current_score

if (average_passed == 0):
    average_passed = 0
else:
    average_passed = average_passed / passed

if (average_failed == 0):
    average_failed = 0
else:
    average_failed = average_failed / failed

print(f"You have passed {passed} tests")
print(f"You have failed {failed} tests")
print(f"Your average for the passed tests is {average_passed}")
print(f"Your average for the failed tests is {average_failed}")
print(f"Your average for all tests is {average}")