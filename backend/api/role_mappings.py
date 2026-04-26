ROLE_REQUIREMENTS = {
    # TECH ROLES
    "Software Developer": {"python", "java", "c++", "c#", "git", "sql", "javascript", "linux", "agile", "docker"},
    "Web Developer": {"html", "css", "javascript", "react", "vue", "angular", "node.js", "git", "api"},
    "Frontend Developer": {"html", "css", "javascript", "typescript", "react", "angular", "vue", "next.js", "tailwind", "ui/ux"},
    "Backend Developer": {"python", "java", "node.js", "django", "flask", "spring", "sql", "postgresql", "mongodb", "docker", "aws", "rest api", "redis"},
    "Full Stack Developer": {"html", "css", "javascript", "react", "node.js", "python", "sql", "mongodb", "docker", "git", "aws"},
    "Mobile App Developer": {"swift", "kotlin", "java", "react native", "flutter", "dart", "ios", "android", "firebase"},
    "Game Developer": {"c++", "c#", "unity", "unreal engine", "3d modeling", "physics", "opengl", "directx"},
    "Data Analyst": {"python", "sql", "excel", "power bi", "tableau", "data visualization", "pandas", "numpy", "statistics"},
    "Data Scientist": {"python", "r", "sql", "machine learning", "deep learning", "pandas", "numpy", "tensorflow", "pytorch", "scikit-learn", "nlp"},
    "Machine Learning Engineer": {"python", "c++", "tensorflow", "pytorch", "scikit-learn", "neural networks", "docker", "aws", "mlops"},
    "AI Engineer": {"python", "nlp", "computer vision", "deep learning", "tensorflow", "pytorch", "openai", "llm", "neural networks"},
    "Cybersecurity Analyst": {"network security", "linux", "wireshark", "ethical hacking", "firewalls", "penetration testing", "siem"},
    "Ethical Hacker": {"penetration testing", "kali linux", "metasploit", "nmap", "burp suite", "cryptography", "owasp"},
    "Network Engineer": {"cisco", "tcp/ip", "routing", "switching", "firewalls", "vpn", "bgp", "ospf"},
    "Cloud Engineer": {"aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ci/cd", "linux"},
    "DevOps Engineer": {"linux", "bash", "aws", "docker", "kubernetes", "jenkins", "terraform", "ansible", "ci/cd"},
    "Site Reliability Engineer": {"linux", "python", "go", "kubernetes", "docker", "monitoring", "prometheus", "grafana", "incident response"},
    "QA Engineer": {"selenium", "cypress", "junit", "pytest", "jira", "agile", "manual testing", "automated testing"},
    "Automation Tester": {"selenium", "java", "python", "appium", "cucumber", "testng", "api testing"},
    "Technical Support Engineer": {"troubleshooting", "linux", "windows", "networking", "customer service", "jira", "active directory"},
    
    # DESIGN ROLES
    "UI Designer": {"figma", "sketch", "adobe xd", "photoshop", "illustrator", "wireframing", "typography", "color theory"},
    "UX Designer": {"figma", "wireframing", "prototyping", "user research", "usability testing", "information architecture", "persona creation"},
    
    # BUSINESS / NON-TECH ROLES
    "Product Manager": {"agile", "scrum", "jira", "product strategy", "roadmap", "user research", "data analysis", "stakeholder management"},
    "Business Analyst": {"sql", "excel", "requirements gathering", "process modeling", "jira", "visio", "power bi", "tableau"},
    "Sales Executive": {"crm", "salesforce", "b2b", "negotiation", "lead generation", "cold calling", "communication"},
    "Marketing Specialist": {"seo", "sem", "content marketing", "google analytics", "social media marketing", "email marketing", "hubspot"}
}

# Dynamically generate PREDEFINED_SKILLS by taking the union of all role skills
PREDEFINED_SKILLS = set()
for skills in ROLE_REQUIREMENTS.values():
    PREDEFINED_SKILLS.update(skills)
