from pathlib import Path
import streamlit as st
from PIL import Image
import random

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "core" / "M.Nabeel Asad_Resume.pdf"
profile_pic = current_dir / "core" / "LinkedIn Pic.jpg"

# --- General Details ---
PAGE_TITLE = "IAV GmbH | M.Nabeel Asad"
PAGE_ICON = ":wave:"
NAME = "Muhammad Nabeel Asad"
DESCRIPTION = """
I am a professional Python developer with a year of experience, currently pursuing an AI Master's degree. Skilled in
machine learning algorithms like Linear Regression and Random Forest using Pandas and PyTorch. Actively learning
DevOps practices with Docker, Kubernetes, and Jenkins for CI/CD pipelines. Passionate about leveraging AI to drive
innovation and solve complex problems.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load CSS, PDF & Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Side Panel ---

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Resume", "Joke Generator"])

# --- Resume Page ---
if page == "Resume":
    # it is section where i work on resume downloaded part button
    
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    # Social Links
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/mnabeelasadevops/",
        "GitHub": "https://www.github.com/mnabeelasad",
        "Email": "mailto:mnabeelasad@gmail.com",
    }
    
    st.write('\n')
    st.write(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']}) &nbsp; | &nbsp; [GitHub]({SOCIAL_MEDIA['GitHub']}) &nbsp; | &nbsp; [Email]({SOCIAL_MEDIA['Email']})", unsafe_allow_html=True)

    # Education
    st.subheader("EDUCATION")
    st.write("---")
    st.write("""
    - **► Brandenburgische Technische Universität** (Cottbus, Germany)
      - Masters in Artificial Intelligence (April 2023 - Present)
    - **► IQRA University** (Karachi, Pakistan)
      - Bachelor in Computer Science (Sept 2017- July 2021)
    """)

    # Technical Skills
    st.subheader("TECHNICAL SKILLS")
    st.write("---")
    st.markdown("""
    - **► Scripting & Programming Languages:** Python, R, Flask, Fast API, PowerShell Scripting, JavaScript.
    - **► CI/CD and Version Control Tools:** Git, GitHub, Jenkins, CI/CD Pipelines, GitLab, Ansible.
    - **► Cloud Platforms & Containerization Tools:** AWS, Azure, Kubernetes, Docker, Docker Compose.
    - **► Infrastructure as Code:** Terraform.
    - **► Monitoring Tools:** Prometheus, Grafana.
    - **► Data Science and Deep Learning Libraries:** Pandas, Scikit-Learn, PyTorch, Keras.
    - **► Machine Learning Algorithms:** Linear Regression, Logistic Regression, Random Forest, K-means.
    - **► Soft Skills:** Critical Thinking, Problem Solving, Research and Analysis, Agile.
    """)

    # Experience
    st.subheader("PROFESSIONAL EXPERIENCE")
    st.write("---")
    st.write("**Software Engineer | DTS Inc. Pakistan**")
    st.write("""
    - ► Developed RESTful APIs using Flask and Fast API, significantly improving backend efficiency.
    - ► Automated deployment workflows with Python scripts, optimizing software delivery speed by 50%.
    - ► Managed GitHub for version control and orchestrated CI/CD pipelines with Jenkins, optimizing software delivery workflows.
    - ► Implemented Docker, Docker Compose, and Docker Hub to streamline containerization and deployment processes, ensuring smooth software delivery.
    - ► Implemented Terraform and Ansible for Infrastructure as Code (IaC), integrated Grafana.
    """)

    # Projects
    st.subheader("PERSONAL PROJECTS")
    st.write("---")
    st.write("**Deployment of a Three-Tier Application on AWS EKS (Managed Kubernetes Service)**")
    st.write("""
    - ► Successfully deployed a scalable three-tier application (ReactJS, NodeJS, MongoDB) on AWS EKS (Elastic Kubernetes Service), utilizing Kubernetes for efficient orchestration and management.
    - ► Implemented AWS ALB (Application Load Balancer) for effective load balancing, ensuring optimal distribution of traffic across application tiers.
    - ► Acquired practical experience in cloud-native technologies, containerization, and cloud infrastructure management, strengthening proficiency in full-stack development and Kubernetes deployment in production environments.
    """)
    st.write("**GitLab CI/CD Pipeline for Django/Node Application Deployment on AWS EC2**")
    st.write("""
    - ► Developed and deployed a Django/Node application using a GitLab CI/CD hub pipeline, Docker, and AWS-EC2.
    - ► Configured a complete CI/CD pipeline for automated testing, building, and deploying the application.
    - ► Gained hands-on experience in DevOps practices, Docker containerization, and cloud deployment, enhancing my skills in software development and deployment automation.
    """)

    #--- Achievements
    st.subheader("HONOUR AND AWARDS")
    st.write("---")
    st.write("**Special Achievement Award – DTS Inc. Pakistan**")
    st.write("**DTS Inc. Pakistan [25/03/2023]**")
    st.write("- ► Awarded in appreciation of outstanding contribution to the organization.")

    # Languages
    st.subheader("SPRACHEN")
    st.write("---")
    st.write("""
    - **► English:** C1
    - **► German:** (derzeitiges Niveau A2 und weiter lernen für B1).
    """)

# --- Joke Generator Section ---
elif page == "Joke Generator":
    st.subheader("JOKE GENERATOR")
    st.write("---")

    # Local Joke Dataset
    jokes = [
        "• What did the pirate say when he turned 80? Aye matey.",
        "Why do French people eat snails? They don’t like fast food.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    if st.button("Tell me a joke"):
        joke = random.choice(jokes)
        st.write(joke)
