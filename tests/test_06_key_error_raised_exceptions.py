max_score = 15  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    round_match,
    get_similarity_feedback,
    clear_database,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    default_module_to_test
)
import sys

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_06_key_error_raised_exceptions(current_test_name, input_test_cases):
    rec = pc_get_or_create(current_test_name, max_score)
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(input_test_cases, list):
            input_test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), test_case=input_test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.
        
        exception_being_tested = "KeyError"

        # FIRST LOOK FOR TEST CASES WHERE THIS EXCEPTION SHOULD BE RAISED
        input_test_cases_subset = [input_test_cases[3], input_test_cases[4]]
        for input_test_case in input_test_cases_subset:
            case_id = input_test_case["id_input_test_case"]
            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]

            # Load in the student's code and capture output
            manager_payload = load_student_code(current_test_name, inputs, input_test_case, module_to_test=default_module_to_test)

            if not manager_payload:
                continue # if there was an error in running student code, it's already been logged. Just skip to the next test case.

            raised_exceptions = manager_payload.get("raised_exceptions")

            correct_exception_found = False

            for raised_exception in raised_exceptions:
                if raised_exception["exception"] == exception_being_tested and raised_exception["handled_by"] == exception_being_tested:
                    correct_exception_found = True

            # Check if ValueError was raised during the execution
            if not correct_exception_found:
                formatted = format_error_message(
                    custom_message=(f"Your code was supposed to raise a \"{exception_being_tested}\" exception but one was never raised. "
                                    f"Make sure your code actually allows for a \"{exception_being_tested}\" exception by "
                                    f"doing an illegal conversion, like an improper string to an int or float. "
                                    f"You can see the inputs below. Try setting a break point in your code and step through "
                                    f"your code with the inputs shown below, "
                                    f"and if your code never jumps to an \"except {exception_being_tested}\" section of code, that is "
                                    f"why this test is failing.\n"),
                    input_test_case=input_test_case,
                    display_inputs=True,
                    current_test_name=current_test_name
                )
                rec.fail_case(case_id, custom_message=formatted)
            else:
                rec.pass_case(case_id)
        
        # NOW LOOK AT TEST CASES WHEN IT SHOULD NOT BE RAISED
        test_cases_subset = [input_test_cases[0], input_test_cases[1], input_test_cases[2]]
        for input_test_case in test_cases_subset:
            case_id = input_test_case["id_input_test_case"]
            # Grab the necessary data from the test case dictionary
            inputs = input_test_case["inputs"]

            # Load in the student's code and capture output
            manager_payload = load_student_code(current_test_name, inputs, input_test_case, module_to_test=default_module_to_test)

            if not manager_payload:
                continue # if there was an error in running student code, it's already been logged. Just skip to the next test case.

            raised_exceptions = manager_payload.get("raised_exceptions")

            correct_exception_found = False

            for raised_exception in raised_exceptions:
                if raised_exception["exception"] == exception_being_tested and raised_exception["handled_by"] == exception_being_tested:
                    correct_exception_found = True

            # Check if ValueError was raised during the execution
            if correct_exception_found:
                formatted = format_error_message(
                    custom_message=(f"Your code was NOT supposed to raise a \"{exception_being_tested}\" exception but one was raised. "
                                    f"You can see the inputs below. Try running your code with the inputs shown below, "
                                    f"and if your code jumps to an \"except KeyError\" section of code, that is "
                                    f"why this test is failing.\n"),
                    input_test_case=input_test_case,
                    display_inputs=True,
                    current_test_name=current_test_name
                )
                rec.fail_case(case_id, custom_message=formatted)
            else:
                rec.pass_case(case_id)

    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case, current_test_name=current_test_name)
    finally:
        sys.setprofile(None)
        pc_finalize_and_maybe_fail(rec)

