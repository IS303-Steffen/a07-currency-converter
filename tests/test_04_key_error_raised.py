max_score = 25  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students, round_match
import re, sys

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_04_value_error_raised(test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(test_cases, list):
            test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), test_case=test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.
        
        exception_being_tested = "KeyError"

        # FIRST LOOK FOR TEST CASES WHERE THIS EXCEPTION SHOULD BE RAISED
        test_cases_subset = [test_cases[2], test_cases[3]]
        for test_case in test_cases_subset:

            # Grab the necessary data from the test case dictionary
            inputs = test_case["inputs"]

            # Load in the student's code and capture output
            _, _, _, _, raised_exceptions = load_student_code(inputs, test_case)

            correct_exception_found = False

            for raised_exception in raised_exceptions:
                if raised_exception["exception"] == exception_being_tested and raised_exception["handled_by"] == exception_being_tested:
                    correct_exception_found = True

            # Check if ValueError was raised during the execution
            assert correct_exception_found, format_error_message(
                    custom_message=(f"Your code was supposed to raise a \"{exception_being_tested}\" exception "
                                    f"during test case {test_case["id_test_case"]} but one was never raised. "
                                    f"Make sure your code actually allows for a \"ValueError\" exception by "
                                    f"doing an illegal conversion, like an improper string to an int or float. "
                                    f"You can see the inputs below. Try running your code with the inputs shown below, "
                                    f"and if your code never jumps to an \"except ValueError\" section of code, that is "
                                    f"why this test is failing."),
                    test_case=test_case,
                    display_inputs=True,
                )
        
        # NOW LOOK AT TEST CASES WHEN IT SHOULD NOT BE RAISED
        test_cases_subset = [test_cases[0], test_cases[1]]
        for test_case in test_cases_subset:

            # Grab the necessary data from the test case dictionary
            inputs = test_case["inputs"]

            # Load in the student's code and capture output
            _, _, _, _, raised_exceptions = load_student_code(inputs, test_case)

            correct_exception_found = False

            for raised_exception in raised_exceptions:
                if raised_exception["exception"] == exception_being_tested and raised_exception["handled_by"] == exception_being_tested:
                    correct_exception_found = True

            # Check if ValueError was raised during the execution
            assert not correct_exception_found, format_error_message(
                    custom_message=(f"Your code was NOT supposed to raise a \"{exception_being_tested}\" exception "
                                    f"during test case {test_case["id_test_case"]} but one was raised. "
                                    f"You can see the inputs below. Try running your code with the inputs shown below, "
                                    f"and if your code jumps to an \"except ValueError\" section of code, that is "
                                    f"why this test is failing."),
                    test_case=test_case,
                    display_inputs=True,
                )
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, test_case)
    finally:
        sys.setprofile(None)

