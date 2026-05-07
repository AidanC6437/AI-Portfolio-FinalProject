"""
This file stores personal portfolio content in one place.

Why this is useful:
- It keeps beginner edits simple.
- You can update your bio, links, and resume text without touching HTML.
- It avoids adding extra database models before you actually need them.
"""

SITE_PROFILE = {
    "full_name": "Aidan Chiu",
    "headline": "Passionate Developer focused on AI, automation, and Django web development",
    "home_intro": (
        "This website showcases my Django-made portfolio, which features all of my different projects utilizing AI, automation, machine "
        "learning, and software development, along with my resume, skills, and contact information. The projects included here are the work I completed throughout my course, and they represent a variety of different tools, technologies, and use cases. "
    ),
    "about_intro": (
        "My name is Aidan Chiu, a Baylor University Undergraduate Student, majoring in Management Information Systems and Accounting. I am a novice student developer building practical AI and software projects "
        "that connect technical ideas to real business needs. I am also pursuing my Masters of Science in Information Systems (MSIS) right after my undergraduate studies to continue building my skills and experience in the field of information systems, with a focus on AI, automation, and software development."
        
    ),
    "about_body": (
        "This portfolio highlights the work I completed throughout my course, "
        "including chatbot development, automation workflows via N8N, AI agents, "
        "machine learning, and Django web applications. My goal is to present "
        "each project in a way that is technically clear, professionally useful, "
        "and easy to discuss during interviews. In my downtime, I enjoy learning about new AI tools, exploring how they can be applied to solve problems, "
        "and building projects that connect technology to practical use cases. "
        "I am also an avid gym goer, video game player, Star Wars lover, 3D-print developer, and movie/TV show enthusiast!"
    ),
    "academic_focus": (
        "In this day and age, I believe being AI-literate is essential for success in the world of business. "
        "I am interested in using technology, notably AI, to assist in solving problems, improving "
        "workflows, and communicating ideas clearly. I enjoy learning how AI "
        "tools can support smarter decision-making and better user experiences in more streamlined ways."
        " Upon graduation, I will be working at Ernst & Young, one of the Big 4 accounting firms, where I hope to apply my skills "
        "in a role that allows me to continue learning and building projects that connect AI and automation to real business needs."
    ),
    "personal_email": "AidanCChiu@gmail.com",
    "school_email": "aidan_chiu1@baylor.edu",
    "linkedin_url": "https://www.linkedin.com/in/aidan-chiu-79598b26a/",
    "github_url": "https://github.com/AidanC6437",
    "resume_pdf_path": "files/Aidan_Chiu_Resume.pdf",
}

FOCUS_AREAS = [
    "AI tools and workflows",
    "Python and Django development",
    "Automation with agent-based systems",
    "Clear technical communication",
]

RESUME_CONTENT = {
    "summary": (
        "A concise overview of my academic background, technical strengths, and the experience I bring to AI, automation, and web development projects."
    ),
    "education_items": [
        "Baylor University undergraduate student majoring in Management Information Systems and Accounting",
        "Coursework and applied project experience in AI, programming, business technology, and web development",
        "Certified to procure, clean, and understand data and its applications through completion of Google's Data Analytics and Business Intelligence programs.",
    ],
    "strength_items": [
        "Building full-stack class projects with Django, Python, HTML, CSS, and Bootstrap",
        "Applying AI tools and workflow automation to solve practical business problems",
        "Communicating technical concepts clearly in both written and verbal settings",
        "Using Microsoft Excel, SQL, and Power BI to organize data, analyze trends, and support clearer business decision-making.",
    ],
    "experience_items": [
        "Technology Risk Assurance Intern at Ernst & Young in Los Angeles, where I evaluated IT general controls and application controls through integrated audit procedures for a large public company.",
        "Supported client security and risk mitigation efforts at EY by creating process documentation and flowcharts to assess technology implementation risks and recommend improvements.",
        "Worked in accounting and operations at Island Pacific Seafood Market, using store and operational data to improve efficiency, inventory flow, and point-of-sale processes.",
    ],
    "interview_points": [
        "Able to explain project goals, tools used, implementation choices, and lessons learned",
        "Comfortable discussing how AI tools, agents, and automation workflows were used in practical projects",
        "Prepared to connect technical work to business value, usability, and problem-solving",
    ],
}

SKILLS_LIST = [
    {
        "name": "Python",
        "details": [
            "Used Python as the core language for coursework in AI, machine learning, automation, and web development.",
            "Built project logic, backend workflows, and data-driven features across multiple portfolio applications.",
        ],
    },
    {
        "name": "Django",
        "details": [
            "Developed full-stack web applications using Django models, views, templates, forms, and authentication.",
            "Applied Django to organize and present portfolio content in a structured, professional web application.",
        ],
    },
    {
        "name": "Bootstrap",
        "details": [
            "Used Bootstrap to create responsive page layouts, navigation, cards, and forms. Even this site is built with Bootstrap components!",
            "Improved the visual consistency and usability of the website across different pages.",
        ],
    },
    {
        "name": "HTML/CSS",
        "details": [
            "Built and customized page structure, layouts, and styling for multiple sections of the portfolio site.",
            "Used CSS to improve spacing, hierarchy, color balance, and overall page presentation.",
        ],
    },
    {
        "name": "JavaScript",
        "details": [
            "Worked with front-end scripting concepts to support interactive web features and modern browser behavior.",
        ],
    },
    {
        "name": "LangChain",
        "details": [
            "Used LangChain to explore agent-based workflows, tool usage, and structured AI response handling.",
            "Applied LangChain concepts in projects that required multi-step reasoning and tool-assisted outputs.",
        ],
    },
    {
        "name": "n8n",
        "details": [
            "Utilized n8n nodes and workflow tools to create AI-driven automation centered around task routing and customer-service style processes.",
            "Connected services, triggers, and logic steps to reduce repetitive manual work through workflow automation.",
        ],
    },
    {
        "name": "Google AI Studio",
        "details": [
            "Explored prompt design and media-focused AI workflows using Google AI Studio.",
            "Tested how generative AI tools can support content creation, experimentation, and business use cases.",
        ],
    },
    {
        "name": "scikit-learn",
        "details": [
            "Applied scikit-learn to prepare datasets, train models, and evaluate prediction results in machine learning coursework.",
            "Used the library to better understand model selection, performance evaluation, and data-driven decision-making.",
        ],
    },
    {
        "name": "Git and GitHub",
        "details": [
            "Used Git and GitHub to track project changes, manage version history, and organize portfolio code.",
            "Maintained project files and updates in a format suitable for sharing, review, and professional presentation.",
        ],
    },
]
