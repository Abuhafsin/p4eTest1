"""Create a function that receives a list of strings that are arithmetic problems and returns the
problems arranged vertically and side-by-side. The function should optionally take a second argument.
When the second argument is set to True, the answers should be displayed."""


def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems exceeds the limit (5).
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_operand1 = []
    arranged_operand2 = []
    arranged_line = []
    arranged_answer = []
    arranged_problems = []
    for problem in problems:
        elements = problem.split()
        operand1, operator, operand2 = elements

        # Check if the operator is valid (+ or -).
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Check if operands are numeric.
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the numeric digit is within the limit (4)
        if max(len(operand1), len(operand2)) > 4:
            return "ERROR: Numbers can not be more than 4 digit"

        # Determine the length of the longest operand.
        max_length = max(len(operand1), len(operand2))

        # Create formatted strings for operands.
        formatted_operand1 = operand1.rjust(max_length + 2)
        formatted_operand2 = operator + operand2.rjust(max_length + 1)

        # Calculate the width of the arranged problem.
        width = max(len(formatted_operand1), len(formatted_operand2))

        # Create a line of dashes for the problem.
        line = "-" * width

        # Append the formatted strings to the arranged problems list.
        arranged_operand1.append(formatted_operand1)
        arranged_operand2.append(formatted_operand2)
        arranged_line.append(line)

        # If show_answers is True, calculate and append answers.
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
        else:
            answer = ' '
        arranged_answer.append(answer.rjust(width))
    arranged_problems.append(arranged_operand1)
    arranged_problems.append(arranged_operand2)
    arranged_problems.append(arranged_line)
    arranged_problems.append(arranged_answer)

    # Combine all arranged problems into a single string separated by empty.
    # Combine all arranged problems into a new line
    arranged_str = "\n".join(("    ".join(i) for i in arranged_problems))

    return arranged_str


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
