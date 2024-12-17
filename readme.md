# README

This script is designed to generate a professional ATS "resistant" document (e.g., a resume or CV) in `.docx` format using the `python-docx` library. The script dynamically populates various sections of the document based on data provided in an external configuration file (`config.py`).

## Prerequisites

1. **Python 3.6 or higher**
   - Ensure you have Python installed on your system.

2. **Dependencies**
   - Install the `python-docx` library by running:
     ```bash
     pip install python-docx
     ```

3. **Configuration File**
   - The script depends on a `config.py` file to define the content of the document. Ensure you have this file in the same directory as the script.

## Configuration File (`config.py`)

The `config.py` file should contain the following variables:

### 1. `HEADER`
A dictionary defining the document's header information. Example:
```python
HEADER = {
    "name": "John Doe",
    "title": "Software Engineer"
}
```

### 2. `CONTACT_INFO`
A dictionary containing the contact details. Example:
```python
CONTACT_INFO = {
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "linkedin": "linkedin.com/in/johndoe"
}
```

### 3. `PROFESSIONAL_SUMMARY_DESC`
A string describing the professional summary. Example:
```python
PROFESSIONAL_SUMMARY_DESC = "Experienced software engineer with a passion for developing scalable web applications."
```

### 4. `COMPETENCIES`
A dictionary mapping core competencies to their details. Example:
```python
COMPETENCIES = {
    "Programming Languages": ["Python", "Java", "JavaScript"],
    "Frameworks": ["Django", "Flask", "React"]
}
```

### 5. `EXPERIENCES`
A list of dictionaries representing professional experience. Example:
```python
EXPERIENCES = [
    {
        "role": "Software Engineer",
        "company": "Tech Corp",
        "dates": "Jan 2020 - Present",
        "location": "New York, NY",
        "responsibilities": [
            "Developed RESTful APIs using Python and Flask.",
            "Improved application performance by 30%."
        ],
        "technologies": ["Python", "Flask", "Docker"]
    }
]
```

### 6. `EDUCATION`
A list of dictionaries representing educational background. Example:
```python
EDUCATION = [
    {
        "degree": "B.Sc. in Computer Science",
        "institution": "University of Example",
        "years": "2015 - 2019"
    }
]
```

### 7. `CERTIFICATION_PARAGRAPH`
A string listing certifications. Example:
```python
CERTIFICATION_PARAGRAPH = "Certified AWS Solutions Architect, Certified Scrum Master."
```

### 8. `LANGUAGES`
A dictionary representing languages and their proficiency levels. Example:
```python
LANGUAGES = {
    "English": "Native",
    "Spanish": "Fluent"
}
```

### 9. `OUTPUT_PATH`
The path to save the generated `.docx` file. Example:
```python
OUTPUT_PATH = "output/resume.docx"
```

## Running the Script

1. Place the `config.py` file in the same directory as the script.
2. Run the script using Python:
   ```bash
   python script.py
   ```
3. The generated document will be saved to the location specified by `OUTPUT_PATH` in the `config.py` file.

## Customization

- You can modify the `config.py` file to adjust the document content.
- The script structure allows for easy addition or removal of sections.

## Output

The output will be a `.docx` file containing:
1. A header with the name and title.
2. Contact information.
3. Professional summary.
4. Core competencies (with bullet points).
5. Professional experience (including role, company, responsibilities, and technologies).
6. Education.
7. Certifications.
8. Languages with proficiency levels.

## Notes
- Ensure the `config.py` file is properly formatted; otherwise, the script may throw errors.
- The script uses nested bullet points for detailed lists like core competencies and responsibilities.

## Example Output
An example output structure of the document:

```
John Doe
Software Engineer

Email: john.doe@example.com
Phone: +1234567890
LinkedIn: linkedin.com/in/johndoe

Professional Summary
Experienced software engineer with a passion for developing scalable web applications.

Core Competencies
- Programming Languages
  - Python
  - Java
  - JavaScript
- Frameworks
  - Django
  - Flask
  - React

Professional Experience
Software Engineer | Tech Corp
Jan 2020 - Present | New York, NY
- Developed RESTful APIs using Python and Flask.
- Improved application performance by 30%.
Technologies: Python, Flask, Docker

Education
B.Sc. in Computer Science | University of Example | 2015 - 2019

Certifications
Certified AWS Solutions Architect, Certified Scrum Master.

Languages
English: Native
Spanish: Fluent
```

