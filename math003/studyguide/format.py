import re
import pyperclip


def format_study_guide() -> None:
    with open("math003/studyguide/study_guide_raw.md", "r") as infile:
        def readlines(lines: int) -> str | list[str]:
            if lines == 1:
                return re.sub(r"\\(left|right)\\({|})", r"\\\1\\\\\2",
                              infile.readline().strip(" \n"))
            return [readlines(1) for _ in range(lines)]

        question_lines: list[str] = ["# Questions\n"]
        solution_lines: list[str] = ["# Solutions\n"]
        question_num: int = 1

        while True:
            header = readlines(1)
            if header == "MAIN":
                section, title = readlines(2)
                question_lines.append(f"## {section} {title}\n")
                continue
            
            if header == "QUESTION":
                prompt, question, solution = readlines(3)
                question_lines.append(f"> ### Question {question_num:>03}\n> {prompt}\n>\n"
                                      f"> {question} [[solution]](#solution-{question_num:>03})\n")
                solution_lines.append(f"> ## Solution {question_num:>03}\n> "
                                      f"{solution} [[question]](#question-{question_num:>03})\n")
                question_num += 1
                continue

            break

        pyperclip.copy("\n".join(question_lines) + "\n".join(solution_lines))

if __name__ == "__main__":
    format_study_guide()
    