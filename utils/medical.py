import re

from utils.rag import retrieve_documents


def extract_medical_data(source_name):
    """
    Extract structured laboratory results from the
    active medical report.

    The report text is parsed directly so the dashboard
    does not depend on LLM-generated JSON.
    """

    documents = retrieve_documents(
        "laboratory test results hemoglobin WBC platelet RBC "
        "hematocrit glucose cholesterol LDL HDL triglycerides "
        "reference range status",
        k=6,
        source_name=source_name
    )

    if not documents:
        return {"tests": []}

    # Combine retrieved chunks
    context = "\n".join(
        document.page_content
        for document in documents
    )

    # Normalize line endings and spaces
    context = context.replace("\r", "")

    lines = [
        line.strip()
        for line in context.split("\n")
        if line.strip()
    ]

    tests = []

    # Find rows in the extracted PDF table.
    # Expected structure:
    #
    # Test Name
    # Result
    # Unit
    # Reference Range
    # Status

    i = 0

    while i < len(lines) - 4:

        name = lines[i]
        result = lines[i + 1]
        unit = lines[i + 2]
        reference = lines[i + 3]
        status = lines[i + 4]

        valid_status = status.lower() in [
            "normal",
            "low",
            "high",
            "abnormal"
        ]

        valid_result = re.fullmatch(
            r"[<>]?\s*-?\d[\d,]*(?:\.\d+)?",
            result
        )

        if (
            valid_status
            and valid_result
            and name.lower() not in [
                "test",
                "result",
                "unit",
                "reference range",
                "status"
            ]
        ):

            tests.append(
                {
                    "name": name,
                    "result": result,
                    "unit": unit,
                    "reference_range": reference,
                    "status": status
                }
            )

            i += 5

        else:

            i += 1


    # Remove duplicate tests
    unique_tests = []
    seen = set()

    for test in tests:

        key = test["name"].lower()

        if key not in seen:

            seen.add(key)
            unique_tests.append(test)


    return {
        "tests": unique_tests
    }
