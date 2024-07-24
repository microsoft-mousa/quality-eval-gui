import json


def format_entries_with_reasons(input_file, question_output_file, answer_output_file):
    with open(input_file, 'r', encoding='utf8') as f:
        data = json.load(f)

    question_entries = []
    answer_entries = []

    for entry in data:
        question_reason = entry.get("question_reject_reason")
        answer_reason = entry.get("answer_reject_reason")

        # Process question quality
        if question_reason:
            question = entry["question"]
            citation = entry["textCitations"][0]["text"] if entry["textCitations"] else "No citation available"
            q_grade = entry.get("question_grade")
            q_note = entry.get("question_note")

            formatted_question = f"## Question\n**Question:** {question}\n"
            if q_grade:
                formatted_question += f"**Grade:** {q_grade}\n"
            formatted_question += f"**Reason:** {question_reason}\n"
            if q_note:
                formatted_question += f"**Note:** {q_note}\n"
            formatted_question += f"\n### Citation\n{citation}\n\n---\n\n"

            question_entries.append(formatted_question)

        # Process answer quality
        if answer_reason:
            answer = entry["answer"]
            citation = entry["textCitations"][0]["text"] if entry["textCitations"] else "No citation available"
            a_grade = entry.get("answer_grade")
            a_note = entry.get("answer_note")

            formatted_answer = f"## Answer\n**Answer:** {answer}\n"
            if a_grade:
                formatted_answer += f"**Grade:** {a_grade}\n"
            formatted_answer += f"**Reject Reason:** {answer_reason}\n"
            if a_note:
                formatted_answer += f"**Note:** {a_note}\n"
            formatted_answer += f"\n### Citation\n{citation}\n\n---\n\n"

            answer_entries.append(formatted_answer)

    formatted_question_output = "\n".join(question_entries)
    formatted_answer_output = "\n".join(answer_entries)

    with open(question_output_file, 'w', encoding='utf8') as f:
        f.write(formatted_question_output)

    with open(answer_output_file, 'w', encoding='utf8') as f:
        f.write(formatted_answer_output)

    print(f"Question quality output saved to {question_output_file}")
    print(f"Answer quality output saved to {answer_output_file}")


# Example usage
input_file = '1_annotated_data.json'
question_output_file = 'question_quality.md'
answer_output_file = 'answer_quality.md'
format_entries_with_reasons(input_file, question_output_file, answer_output_file)
