from generator import Generator, load_yaml


def main():
    data = load_yaml("cv.yaml")
    generator = Generator(data)
    generator.generate_typst_code()
    generator.save_typst_code("resume.typ")
    generator.compile_typst_code("resume.typ", "resume.pdf")


if __name__ == "__main__":
    main()
