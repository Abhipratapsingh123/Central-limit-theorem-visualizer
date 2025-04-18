import streamlit as st

# Function to convert marks to grade point
def get_grade_point(marks):
    if marks >= 95:
        return 10
    elif marks >= 85:
        return 9
    elif marks >= 75:
        return 8
    elif marks >= 70:
        return 7
    elif marks >= 60:
        return 6
    elif marks >= 50:
        return 5
    else:
        return 0

st.title("SGPA Calculator")
st.markdown("Enter your subjects, marks, and credit hours below to calculate your SGPA.")

# Input number of subjects
total_subjects = st.number_input("Enter total number of subjects:", min_value=1, step=1)

# Initialize data holders
sub_data = {}
total_credits = 0
total_weighted_points = 0

# Form for input
with st.form("sgpa_form"):
    for i in range(total_subjects):
        st.markdown(f"### Subject {i+1}")
        subject = st.text_input(f"Enter name for subject {i+1}", key=f"subject_{i}")
        marks = st.number_input(f"Enter marks for {subject}", min_value=0.0, max_value=100.0, key=f"marks_{i}")
        credits = st.number_input(f"Enter credits for {subject}", min_value=1, max_value=10, key=f"credits_{i}")
        grade_point = get_grade_point(marks)

        sub_data[subject] = {
            "Marks": marks,
            "Credit": credits,
            "Grade Point": grade_point
        }

    submitted = st.form_submit_button("Calculate SGPA")

# Calculate SGPA after form submission
if submitted:
    for subject, details in sub_data.items():
        total_weighted_points += details["Grade Point"] * details["Credit"]
        total_credits += details["Credit"]

    if total_credits > 0:
        sgpa = total_weighted_points / total_credits
        st.success(f"Your SGPA is: **{round(sgpa, 2)}**")

        with st.expander("Detailed Report"):
            for subject, details in sub_data.items():
                st.write(
                    f"**{subject}** - Marks: {details['Marks']} | Credits: {details['Credit']} | Grade Point: {details['Grade Point']}"
                )
    else:
        st.warning("Please enter valid credit and marks values.")
