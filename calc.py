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

# Form for input
with st.form("sgpa_form"):
    sub_data = []
    for i in range(int(total_subjects)):
        st.markdown(f"### Subject {i+1}")
        subject = st.text_input(f"Subject name", key=f"subject_{i}")
        marks = st.number_input("Marks", min_value=0.0, max_value=100.0, key=f"marks_{i}")
        credits = st.number_input("Credits", min_value=1, max_value=10, key=f"credits_{i}")
        
        sub_data.append({
            "Subject": subject,
            "Marks": marks,
            "Credits": credits
        })

    submitted = st.form_submit_button("Calculate SGPA")

# After submission
if submitted:
    total_weighted_points = 0
    total_credits = 0
    detailed_data = []

    for item in sub_data:
        if item["Subject"].strip() == "":
            continue  # Skip blank subject names
        grade_point = get_grade_point(item["Marks"])
        weighted_point = grade_point * item["Credits"]
        total_weighted_points += weighted_point
        total_credits += item["Credits"]

        detailed_data.append({
            "Subject": item["Subject"],
            "Marks": item["Marks"],
            "Credits": item["Credits"],
            "Grade Point": grade_point
        })

    if total_credits > 0:
        sgpa = total_weighted_points / total_credits
        st.success(f"Your SGPA is: **{round(sgpa, 2)}**")

        with st.expander("Detailed Report"):
            for item in detailed_data:
                st.write(
                    f"**{item['Subject']}** - Marks: {item['Marks']} | Credits: {item['Credits']} | Grade Point: {item['Grade Point']}"
                )
    else:
        st.warning("Please enter valid data for at least one subject.")
