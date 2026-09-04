# QA Report

## PEP 8 Compliance

We successfully executed PEP 8 validation using `flake8` and code formatting using `black`. Any remaining compliance issues (such as line lengths and unused imports) were manually resolved. The codebase is now fully PEP 8 compliant.

## Unit Testing

The test suite in `quiz/tests.py` includes the following 12 test cases verifying model representations, views, and specific business rules.

### Models
1. **`test_exam_str`**: Validates string representation of the `Exam` model.
2. **`test_question_str`**: Validates string representation of the `Question` model.
3. **`test_choice_str`**: Validates string representation of the `Choice` model.

### Business Rules (Validation)
4. **`test_exactly_one_correct_choice_valid`**: Verifies that submitting precisely one correct choice passes formset validation.
5. **`test_zero_correct_choices_invalid`**: Verifies that submitting zero correct choices triggers a ValidationError ("Exactly one choice must be correct.").
6. **`test_multiple_correct_choices_invalid`**: Verifies that submitting multiple correct choices triggers a ValidationError ("Exactly one choice must be correct.").

### Views
7. **`test_exam_list_view`**: Validates HTTP 200 response and correct content rendering for the exam list page.
8. **`test_exam_detail_view`**: Validates HTTP 200 response and correct content rendering for the exam details page.
9. **`test_exam_create_view_get`**: Validates HTTP 200 response when accessing the exam creation form.
10. **`test_exam_create_view_post`**: Validates exam creation POST logic, checking successful redirection and database object creation.
11. **`test_question_create_view_get`**: Validates HTTP 200 response when accessing the question creation form.
12. **`test_question_create_view_post`**: Validates question creation POST logic with valid associated choices, checking successful redirection and database object creation.

## Test Execution Results

All tests execute successfully without errors.

```text
Creating test database for alias 'default'...
............
----------------------------------------------------------------------
Ran 12 tests in 0.111s

OK
Destroying test database for alias 'default'...
Found 12 test(s).
System check identified no issues (0 silenced).
```
