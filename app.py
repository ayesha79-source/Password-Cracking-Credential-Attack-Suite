
import streamlit as st

from password_analyzer import analyze_password
from dictionary_generator import generate_dictionary
from hash_analyzer import generate_hash, identify_hash_format
from brute_force_simulator import (
    estimate_cracking_time,
    simulate_password_test,
    get_character_set_size
)
from report_generator import (
    generate_csv_report,
    generate_pdf_report
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Password Cracking & Credential Attack Suite",
    page_icon="🔐",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "generated_wordlist" not in st.session_state:
    st.session_state.generated_wordlist = []

if "audit_results" not in st.session_state:
    st.session_state.audit_results = []


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🔐 Password Cracking & Credential Attack Suite")

st.caption(
    "Ethical Password Security Assessment and "
    "Controlled Simulation Toolkit"
)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Dictionary Generator",
        "Hash Analysis",
        "Brute-Force Simulation",
        "Password Strength Analyzer",
        "Security Audit Report Generator"
    ]
)


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if menu == "Dashboard":

    st.subheader("Project Overview")

    st.write(
        "A Python-based cybersecurity toolkit designed to "
        "generate test dictionaries, analyze synthetic hash "
        "formats, simulate controlled password-guessing "
        "scenarios, assess password strength, and generate "
        "security audit reports."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Core Modules", "5")
    col2.metric("Application", "Streamlit")
    col3.metric("Programming Language", "Python")

    st.divider()

    st.subheader("Available Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📚 Dictionary Generator")
        st.info("🔐 Hash Analysis")
        st.info("⚙️ Brute-Force Simulation")

    with col2:
        st.info("🛡️ Password Strength Analyzer")
        st.info("📋 Security Audit Report Generator")

    st.warning(
        "This application is intended for educational "
        "password security testing using synthetic data only."
    )


# --------------------------------------------------
# DICTIONARY GENERATOR
# --------------------------------------------------

elif menu == "Dictionary Generator":

    st.subheader("📚 Dictionary Generator")

    st.write(
        "Generate sample password variations for "
        "controlled password policy testing."
    )

    seeds = st.text_area(
        "Enter sample words (one word per line)",
        placeholder="security\nwelcome\nsample",
        height=120,
        key="dictionary_input"
    )

    if st.button("Generate Test Wordlist"):

        words = [
            word.strip()
            for word in seeds.splitlines()
            if word.strip()
        ]

        if words:

            st.session_state.generated_wordlist = (
                generate_dictionary(words)
            )

            st.success(
                f"Successfully generated "
                f"{len(st.session_state.generated_wordlist)} "
                "unique test entries."
            )

        else:

            st.session_state.generated_wordlist = []

            st.warning(
                "Please enter at least one sample word."
            )

    if st.session_state.generated_wordlist:

        st.subheader("Generated Wordlist")

        st.text_area(
            "Generated Entries",
            value="\n".join(
                st.session_state.generated_wordlist
            ),
            height=250,
            disabled=True
        )

        st.download_button(
            label="⬇️ Download Test Wordlist",
            data="\n".join(
                st.session_state.generated_wordlist
            ),
            file_name="generated_wordlist.txt",
            mime="text/plain"
        )


# --------------------------------------------------
# HASH ANALYSIS
# --------------------------------------------------

elif menu == "Hash Analysis":

    st.subheader("🔐 Hash Analysis Demonstration")

    st.write(
        "Generate sample password hashes and identify "
        "common hash formats."
    )

    password = st.text_input(
        "Enter a synthetic test password",
        type="password",
        key="hash_password"
    )

    algorithm = st.selectbox(
        "Select Hashing Algorithm",
        ["sha256", "sha512", "sha1", "md5"]
    )

    if st.button("Generate Sample Hash"):

        if password:

            result = generate_hash(password, algorithm)

            st.success(
                "Sample hash generated successfully."
            )

            st.write(
                "Selected Algorithm:",
                algorithm.upper()
            )

            st.code(result)

            st.write(
                "Detected Format:",
                identify_hash_format(result)
            )

        else:

            st.warning(
                "Please enter a test password."
            )

    st.divider()

    st.subheader("Identify Existing Hash Format")

    sample_hash = st.text_input(
        "Enter a synthetic sample hash",
        key="sample_hash"
    )

    if st.button("Identify Hash Format"):

        if sample_hash.strip():

            st.info(
                identify_hash_format(sample_hash)
            )

        else:

            st.warning(
                "Please enter a hash value."
            )

    st.caption(
        "Hash format identification is indicative, not definitive. "
        "Different algorithms can share the same output length."
    )


# --------------------------------------------------
# BRUTE-FORCE SIMULATION
# --------------------------------------------------

elif menu == "Brute-Force Simulation":

    st.subheader("⚙️ Controlled Brute-Force Simulation")

    st.write(
        "Test a synthetic password against a manually supplied "
        "sample candidate list. This is a local educational simulation."
    )

    test_password = st.text_input(
        "Enter a synthetic test password",
        type="password",
        key="simulation_password"
    )

    candidates = st.text_area(
        "Enter sample candidate passwords (one per line)",
        placeholder="welcome\npassword123\nSample123!",
        height=120
    )

    if st.button("Run Local Simulation"):

        if test_password and candidates.strip():

            candidate_list = [
                item.strip()
                for item in candidates.splitlines()
                if item.strip()
            ]

            result = simulate_password_test(
                test_password,
                candidate_list
            )

            if result["found"]:

                st.success(
                    "Test password found in the sample list."
                )

            else:

                st.info(
                    "Test password not found in the sample list."
                )

            st.metric(
                "Candidates Checked",
                result["attempts"]
            )

            charset = get_character_set_size(
                test_password
            )

            if charset:

                estimate = estimate_cracking_time(
                    len(test_password),
                    charset
                )

                st.subheader("Theoretical Search Space")

                col1, col2 = st.columns(2)

                col1.metric(
                    "Character Set Size",
                    charset
                )

                col2.metric(
                    "Password Length",
                    len(test_password)
                )

                st.write(
                    "Total Possible Combinations:",
                    f"{estimate['total_combinations']:,}"
                )

                st.write(
                    "Estimated Average Search Time:",
                    f"{estimate['average_case_seconds']:,.2f} seconds"
                )

                st.caption(
                    "Estimate assumes a uniform search space and "
                    "1,000 guesses per second. Actual results vary."
                )

            else:

                st.warning(
                    "Could not determine a character set "
                    "for the supplied test password."
                )

        else:

            st.warning(
                "Enter a test password and sample candidates."
            )


# --------------------------------------------------
# PASSWORD STRENGTH ANALYZER
# --------------------------------------------------

elif menu == "Password Strength Analyzer":

    st.subheader("🛡️ Password Strength Analyzer")

    st.write(
        "Evaluate password complexity and estimated entropy "
        "using a synthetic test password."
    )

    password = st.text_input(
        "Enter a synthetic test password",
        type="password",
        key="strength_password"
    )

    if st.button("Analyze Password"):

        if password:

            result = analyze_password(password)

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Password Strength",
                result["strength"]
            )

            col2.metric(
                "Complexity Score",
                f"{result['score']}/6"
            )

            col3.metric(
                "Estimated Entropy",
                f"{result['entropy']} bits"
            )

            st.divider()

            st.subheader("Security Recommendations")

            if result["feedback"]:

                for item in result["feedback"]:
                    st.warning(item)

            else:

                st.success(
                    "All basic complexity checks passed."
                )

            st.caption(
                "This is a basic educational assessment. "
                "Complexity and theoretical entropy alone do not "
                "guarantee password security."
            )

        else:

            st.warning(
                "Please enter a test password."
            )


# --------------------------------------------------
# SECURITY AUDIT REPORT GENERATOR
# --------------------------------------------------

elif menu == "Security Audit Report Generator":

    st.subheader("📋 Security Audit Report Generator")

    st.write(
        "Generate CSV and PDF reports from password "
        "strength assessment results."
    )

    st.info(
        "Reports use synthetic assessment data and do not "
        "include plaintext passwords."
    )

    if st.button("Add Sample Audit Result"):

        sample_password = "Sample@12345"

        result = analyze_password(sample_password)

        st.session_state.audit_results.append({
            "strength": result["strength"],
            "score": result["score"],
            "entropy": result["entropy"],
            "feedback": result["feedback"]
        })

        st.success(
            "Sample audit result added successfully."
        )

    if st.session_state.audit_results:

        st.subheader("Audit Summary")

        st.metric(
            "Total Samples Assessed",
            len(st.session_state.audit_results)
        )

        csv_data = generate_csv_report(
            st.session_state.audit_results
        )

        pdf_data = generate_pdf_report(
            st.session_state.audit_results
        )

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="⬇️ Download CSV Audit Report",
                data=csv_data,
                file_name="password_security_audit.csv",
                mime="text/csv"
            )

        with col2:

            st.download_button(
                label="⬇️ Download PDF Audit Report",
                data=pdf_data,
                file_name="password_security_audit.pdf",
                mime="application/pdf"
            )

    else:

        st.warning(
            "No audit results available. "
            "Click Add Sample Audit Result to begin."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Password Cracking & Credential Attack Suite | "
    "Educational Cybersecurity Project | 2026"
)
