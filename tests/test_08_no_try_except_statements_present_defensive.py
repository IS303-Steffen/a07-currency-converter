max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students, check_forbidden_statements, module_to_test_2
import re, sys, ast


# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_08_no_try_except_statements_present_defensive(current_test_name):
    try:    
        student_code_path = f"{module_to_test_2}.py"  # Update with actual file name
        with open(student_code_path, "r", encoding="utf-8") as f:
            student_code = f.read()

        forbidden_statements = check_forbidden_statements(student_code, (ast.Try,))

        assert not forbidden_statements, format_error_message(
                    custom_message=(f"Your {module_to_test_2}.py file included at least one \"try\" statement, which the tests are "
                                    f"forbidding to encourage you to only use defensive programming with if statements. You can write all needed functionality without any try/except statements "
                                    f"in the {module_to_test_2}.py file. Reach out to a TA or the professor if you're not sure how that is possible."),
                    input_test_case={"id_input_test_case": None, "input_test_case_description": None},
                    current_test_name=current_test_name
                )
 
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, {"id_input_test_case": None, "input_test_case_description": None}, current_test_name=current_test_name)

