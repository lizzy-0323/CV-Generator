import yaml
from typst import _typst as typst
from typing import Literal

default_header = """#import "@preview/cuti:0.2.1": show-cn-fakebold
#show: show-cn-fakebold
#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommended resume text size is from `10pt` to `12pt`
// #set text(
//   size: 12pt,
// )

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/  

#set par(justify: true)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}

#let fontbold(s,t) = {text(size:s,weight: "bold")[#t]}
"""

small_words = [
    "a",
    "an",
    "the",
    "and",
    "but",
    "or",
    "for",
    "nor",
    "on",
    "at",
    "to",
    "from",
]

english_chinese_mapping = {
    "education-experience": "教育经历",
    "work-experience": "工作经历",
    "research-experience": "研究经历",
    "project-experience": "项目经历",
    "opensource-experience": "开源经历",
    "skills": "技能",
}


class Generator:
    def __init__(self, data):
        self.data = data
        self.typst_code = ""
        self.version = self.get_version()
        self.write_header()

    def get_version(self) -> Literal["english", "chinese"]:
        if "metadata" in self.data and "version" in self.data["metadata"]:
            version = self.data["metadata"]["version"]
        else:
            version = "english"

        print(f"Version: {version}")
        return version

    def write(self, string: str):
        self.typst_code += string

    def write_header(self, header: str = ""):
        if header == "":
            header = default_header
        self.write(header)

    def write_section(self, title):
        title_case_title = (
            to_title_case(title)
            if self.version == "english"
            else to_chinese_case(title)
        )
        self.write(f"== {title_case_title} \n")
        self.write("#chiline()\n")
        for item in self.data[title]:
            self.write(f"*{item['name']}*")
            self.write(" #h(1fr) ")
            self.write(f"{item['duration']}")
            self.write(" \\")
            self.write("\n")
            if "award" in item:
                self.write(f"{item['award']}")
                self.write("\n")
                self.write("\n")
            if "summary" in item:
                self.write("*Summary*:")
                self.write(f"{item['summary']}")
            if "details" in item:
                for detail in item["details"]:
                    self.write("- ")
                    self.write(f"{detail['item']}")
                    self.write("\n")
                    self.write("\n")
        self.write("\n")

    def save_typst_code(self, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(self.typst_code)

    def compile_typst_code(self, input_file: str, output_file: str):
        typst.compile(input_file, output_file)

    def generate_typst_code(self):
        self.write("\n")
        self.write(f"= {self.data['name']}\n")
        if "picture" in self.data:
            self.write(
                f'#place(top+right,[#image("{self.data["picture"]}",width: 7.5%, height: auto)])\n'
            )
        if "email" in self.data:
            email = self.data["email"].replace("@", "\\@")
            self.write(f'#link("{email}")')
            self.write(f"[{email}]")
            self.write("\n")

        if "homepage" in self.data:
            homepage = self.data["homepage"]
            self.write(f'#link("{homepage}")')
            self.write(f"[{homepage}]")
            self.write("\n")

        if "github" in self.data:
            github = self.data["github"]
            self.write(f'#link("{github}")')
            self.write(f"[{github}]")
            self.write("\n")

        if "phone" in self.data:
            phone = self.data["phone"]
            self.write(f"Phone: {phone}")
            self.write("\n")

        if "education-experience" in self.data:
            self.write_section("education-experience")

        if "work-experience" in self.data:
            self.write_section("work-experience")

        if "research-experience" in self.data:
            self.write_section("research-experience")

        if "project-experience" in self.data:
            self.write_section("project-experience")

        if "opensource-experience" in self.data:
            self.write_section("opensource-experience")

        if "skills" in self.data:
            skills = self.data["skills"]
            title_case_title = (
                to_title_case("skills")
                if self.version == "english"
                else to_chinese_case("skills")
            )
            self.write(f"== {title_case_title} \n")
            self.write("#chiline()\n")
            for skill in skills:
                self.write("- ")
                self.write(f"*{skill['name']}*: ")
                self.write(f"{skill['details']}")
                self.write("\n")
            self.write("\n")


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def to_chinese_case(text):
    return english_chinese_mapping[text]


def to_title_case(text: str):
    words = text.replace("-", " ").split(" ")

    title_case_words = [
        word if word.lower() in small_words else word.capitalize()
        for position, word in enumerate(words)
    ]

    return " ".join(title_case_words)
