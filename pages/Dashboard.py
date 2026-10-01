import streamlit as st

from utils.style import apply_custom_style
from utils.medical import extract_medical_data

apply_custom_style()

st.title("Medical Report Dashboard")

st.write(
    "View key laboratory information extracted from the active medical report."
)


active_document = st.session_state.get(
    "active_document",
    None
)


if not active_document:

    st.warning(
        "Please upload and index a medical report first."
    )

    st.stop()


st.info(
    f"Active document: {active_document}"
)


if st.button(
    "Analyze Medical Report",
    use_container_width=True
):

    with st.spinner(
        "Analyzing laboratory results..."
    ):

        data = extract_medical_data(
            active_document
        )

        st.session_state["medical_data"] = data


data = st.session_state.get(
    "medical_data",
    None
)


if data is None:

    st.info(
        "Click 'Analyze Medical Report' to generate the dashboard."
    )

    st.stop()


tests = data.get(
    "tests",
    []
)


if not tests:

    st.warning(
        "No structured laboratory results could be extracted from the report."
    )

    st.stop()


normal_count = 0
abnormal_count = 0


for test in tests:

    status = str(
        test.get("status", "")
    ).lower()

    if status == "normal":

        normal_count += 1

    elif status in [
        "low",
        "high",
        "abnormal"
    ]:

        abnormal_count += 1


total_count = len(tests)


st.markdown(
    "### Report Overview"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Tests Analyzed",
        total_count
    )


with col2:

    st.metric(
        "Normal",
        normal_count
    )


with col3:

    st.metric(
        "Abnormal",
        abnormal_count
    )


st.divider()


st.markdown(
    "### Laboratory Results"
)


table_data = []


for test in tests:

    table_data.append(
        {
            "Test": test.get(
                "name",
                "Unknown"
            ),
            "Result": test.get(
                "result",
                "Not available"
            ),
            "Unit": test.get(
                "unit",
                ""
            ),
            "Reference Range": test.get(
                "reference_range",
                "Not available"
            ),
            "Status": test.get(
                "status",
                "Not available"
            )
        }
    )


st.dataframe(
    table_data,
    use_container_width=True,
    hide_index=True
)


st.divider()


st.markdown(
    "### Report Notes"
)


st.info(
    "This dashboard reports laboratory information extracted from the "
    "uploaded document. It does not provide a medical diagnosis or "
    "replace evaluation by a qualified healthcare professional."
)
