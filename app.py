import streamlit as st


# Streamlit app
def main():
    st.title("Grade Sheet Downloader")

    # Get student_id from the user
    student_id = st.text_input("Student ID")

    # Get student_id from the user
    student_name = st.text_input("Student Name")

    if st.button("Generate Link"):
        if student_id:
            # Generate the URL
            url = (
                f"https://usis.bracu.ac.bd/academia/docuJasper/index?studentId={student_id}&reportFormat=PDF&old_id_no"
                f"={student_id}&strMessage=&scholarProgramMsg=&companyLogo=%2Fvar%2Facademia%2Fimage%2FuniversityLogo"
                f"%2F1571986355.jpg&companyName=BRAC+University&headerTitle=GRADE+SHEET&companyAddress=66%2C"
                f"+MOHAKHALI+C%2FA%2C+DHAKA+-+1212.&academicStanding=Satisfactory&gradeSheetBackground=%2Fbits"
                f"%2Fusis%2Ftomcat%2Fwebapps%2Facademia%2Fimages%2FgradeSheetBackground.jpg&_format=PDF&_name="
                f"{student_name}&_file=student%2FrptStudentGradeSheetForStudent.jasper")
            # Display the link
            st.markdown(f"[Download]({url})", unsafe_allow_html=True)
        else:
            st.warning("Please enter proper credentials.")


if __name__ == "__main__":
    main()
