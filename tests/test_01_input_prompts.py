max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students
import re

# Checks if the input prompts (from using input()) contain the expected prompts.
def test_01_input_prompts(test_cases):
    try:
        # Ensure test_cases is valid and iterable
        if not isinstance(test_cases, list):
            test_case = {"id_test_case": None}
            exception_message_for_students(ValueError("test_cases should be a list of dictionaries. Contact your professor."), test_case=test_case) 
            return  # Technically not needed, as exception_message_for_students throws a pytest.fail Error, but included for clarity that this ends the test.

        # Loop through each test case
        for test_case in test_cases:
            
            # Grab the necessary data from the test case dictionary
            inputs = test_case["inputs"]
            expected_input_prompts = test_case["input_prompts"]
            invalid_input_prompts = test_case["invalid_input_prompts"]

            # Load in the student's code using the updated function
            captured_input_prompts, _, _, _, _ = load_student_code(inputs, test_case)

            # Normalize the captured input prompts to remove spaces, punctuation, and symbols
            normalized_captured_input_prompts = [normalize_text(captured_prompt) for captured_prompt in captured_input_prompts]
            normalized_captured_input_prompts = '\n'.join(normalized_captured_input_prompts)

            # Check that each required phrase (regex pattern) is found in the normalized captured output
            for expected_phrase in expected_input_prompts:
                expected_phrase = normalize_text(expected_phrase)
                regex_pattern = expected_phrase.replace("wildcard", r".+?")
                match = re.search(regex_pattern, normalized_captured_input_prompts)

                assert match, format_error_message(
                    custom_message=("The expected input prompt (ignoring punctuation / capitalization):\n\n"
                                    f"\"{expected_phrase}\"\n\n"
                                    f"wasn't found in the input() function output.\n\n"
                                    f"Below are all the input prompts from your code (ignoring punctuation / capitalization):\n\n"
                                    f"{normalized_captured_input_prompts}\n\n"),
                    test_case=test_case,
                    display_inputs=True,
                    display_input_prompts=True,
                    display_invalid_input_prompts=True
                )

            # Ensure none of the invalid phrases are found in the normalized captured output
            for invalid_phrase in invalid_input_prompts:
                invalid_phrase = normalize_text(invalid_phrase)
                regex_pattern = invalid_phrase.replace("wildcard", r".+?")
                match = re.search(regex_pattern, normalized_captured_input_prompts)

                assert not match, format_error_message(
                    custom_message=("You used an invalid input() prompt (ignoring punctuation / capitalization):\n\n"
                                    f"\"{invalid_phrase}\"\n\n"
                                    f"Below are all the input prompts from your code (ignoring punctuation / capitalization):\n\n"
                                    f"{normalized_captured_input_prompts}\n\n"),
                    test_case=test_case,
                    display_inputs=True,
                    display_input_prompts=True,
                    display_invalid_input_prompts=True
                )
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, test_case)
    