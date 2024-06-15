import streamlit as st


def main():
    st.title("Brac You")

    student_id = st.text_input("Student ID", placeholder="XXXXXXXX")

    nick_name = st.text_input("Nickname", placeholder="Chicken")

    url = (
        f"https://usis.bracu.ac.bd/academia/docuJasper/index?studentId={student_id}&reportFormat=PDF&old_id_no"
        f"={student_id}&strMessage=&scholarProgramMsg=&companyLogo=%2Fvar%2Facademia%2Fimage%2FuniversityLogo"
        f"%2F1571986355.jpg&companyName=BRAC+University&headerTitle=GRADE+SHEET&companyAddress=66%2C"
        f"+MOHAKHALI+C%2FA%2C+DHAKA+-+1212.&academicStanding=Satisfactory&gradeSheetBackground=%2Fbits"
        f"%2Fusis%2Ftomcat%2Fwebapps%2Facademia%2Fimages%2FgradeSheetBackground.jpg&_format=PDF&_name="
        f"{nick_name}&_file=student%2FrptStudentGradeSheetForStudent.jasper"
    )

    if st.link_button("Download", url):
        if not student_id and nick_name:
            st.warning("Please enter proper credentials")

    footer_html = f"""
    <div style='text-align: center;'>
        <p>Developed with ❤️ by <a href="https://zunayedology.github.io/">Zunayed</a></p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

# streamlit run app.py
