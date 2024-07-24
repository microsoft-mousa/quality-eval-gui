import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import json


class AnnotationApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.annotated_data = []
        self.current_index = 0
        self._reasons = ["Incorrect", "Incomplete", "Outdated", "Not Relevant"]

        self.root.title("Annotation Tool")

        # Define custom font
        self.custom_font = tkFont.Font(family="Helvetica", size=14)
        self.custom_font_bold = tkFont.Font(family="Helvetica", size=14, weight="bold")

        self.question_label = tk.Label(root, text="Question:", font=self.custom_font_bold)
        self.question_label.pack()
        self.question_text = tk.Text(root, height=2, width=100, font=self.custom_font)
        self.question_text.pack()

        self.answer_label = tk.Label(root, text="Answer:", font=self.custom_font_bold)
        self.answer_label.pack()
        self.answer_text = tk.Text(root, height=2, width=100, font=self.custom_font)
        self.answer_text.pack()

        self.citation_label = tk.Label(root, text="Citation:", font=self.custom_font_bold)
        self.citation_label.pack()
        self.citation_text = tk.Text(root, height=5, width=100, font=self.custom_font)
        self.citation_text.pack()

        # Create frames for question and answer quality
        self.quality_frame = tk.Frame(root)
        self.quality_frame.pack()

        self.question_quality_frame = tk.Frame(self.quality_frame)
        self.question_quality_frame.grid(row=0, column=0, padx=10, pady=10)

        self.answer_quality_frame = tk.Frame(self.quality_frame)
        self.answer_quality_frame.grid(row=0, column=1, padx=10, pady=10)

        # Question Quality Section
        self.q_section_label = tk.Label(self.question_quality_frame, text="Question Quality",
                                        font=self.custom_font_bold)
        self.q_section_label.grid(row=0, column=0, columnspan=2)

        self.q_grade_label = tk.Label(self.question_quality_frame, text="Grade:", font=self.custom_font_bold)
        self.q_grade_label.grid(row=1, column=0)
        self.q_grade_entry = tk.Entry(self.question_quality_frame, font=self.custom_font)
        self.q_grade_entry.grid(row=1, column=1)

        self.q__reason_label = tk.Label(self.question_quality_frame, text=" Reason:",
                                              font=self.custom_font_bold)
        self.q__reason_label.grid(row=2, column=0)
        self.q__reason_combobox = ttk.Combobox(self.question_quality_frame, values=self._reasons,
                                                     font=self.custom_font)
        self.q__reason_combobox.grid(row=2, column=1)

        self.q_add_reason_button = tk.Button(self.question_quality_frame, text="Add New Reason", font=self.custom_font,
                                             command=self.add_new_question_reason)
        self.q_add_reason_button.grid(row=2, column=2)

        self.q_note_label = tk.Label(self.question_quality_frame, text="Note:", font=self.custom_font_bold)
        self.q_note_label.grid(row=3, column=0)
        self.q_note_entry = tk.Entry(self.question_quality_frame, font=self.custom_font)
        self.q_note_entry.grid(row=3, column=1)

        # Answer Quality Section
        self.a_section_label = tk.Label(self.answer_quality_frame, text="Answer Quality", font=self.custom_font_bold)
        self.a_section_label.grid(row=0, column=0, columnspan=2)

        self.a_grade_label = tk.Label(self.answer_quality_frame, text="Grade:", font=self.custom_font_bold)
        self.a_grade_label.grid(row=1, column=0)
        self.a_grade_entry = tk.Entry(self.answer_quality_frame, font=self.custom_font)
        self.a_grade_entry.grid(row=1, column=1)

        self.a__reason_label = tk.Label(self.answer_quality_frame, text=" Reason:",
                                              font=self.custom_font_bold)
        self.a__reason_label.grid(row=2, column=0)
        self.a__reason_combobox = ttk.Combobox(self.answer_quality_frame, values=self._reasons,
                                                     font=self.custom_font)
        self.a__reason_combobox.grid(row=2, column=1)

        self.a_add_reason_button = tk.Button(self.answer_quality_frame, text="Add New Reason", font=self.custom_font,
                                             command=self.add_new_answer_reason)
        self.a_add_reason_button.grid(row=2, column=2)

        self.a_note_label = tk.Label(self.answer_quality_frame, text="Note:", font=self.custom_font_bold)
        self.a_note_label.grid(row=3, column=0)
        self.a_note_entry = tk.Entry(self.answer_quality_frame, font=self.custom_font)
        self.a_note_entry.grid(row=3, column=1)

        self.save_button = tk.Button(root, text="Save Entry", font=self.custom_font, command=self.save_entry_and_next)
        self.save_button.pack()

        self.skip_button = tk.Button(root, text="Skip Entry", font=self.custom_font, command=self.skip_entry)
        self.skip_button.pack()

        self.save_final_button = tk.Button(root, text="Save Final Data", font=self.custom_font,
                                           command=self.save_to_json)
        self.save_final_button.pack()

        self.load_entry(self.current_index)

    def load_entry(self, index):
        entry = self.data[index]
        self.question_text.delete('1.0', tk.END)
        self.question_text.insert(tk.END, entry["question"])
        self.answer_text.delete('1.0', tk.END)
        self.answer_text.insert(tk.END, entry["answer"])
        citation_text = entry["textCitations"][0]["text"] if entry["textCitations"] else "No citation available"
        self.citation_text.delete('1.0', tk.END)
        self.citation_text.insert(tk.END, citation_text)

        self.q_grade_entry.delete(0, tk.END)
        self.q__reason_combobox.set("")
        self.q_note_entry.delete(0, tk.END)

        self.a_grade_entry.delete(0, tk.END)
        self.a__reason_combobox.set("")
        self.a_note_entry.delete(0, tk.END)

    def save_entry_and_next(self):
        self.save_entry()
        self.annotated_data.append(self.data[self.current_index])
        self.next_entry()

    def skip_entry(self):
        self.next_entry()

    def next_entry(self):
        self.current_index = (self.current_index + 1) % len(self.data)
        self.load_entry(self.current_index)

    def save_entry(self):
        self.data[self.current_index]["question_grade"] = self.q_grade_entry.get()
        self.data[self.current_index]["question__reason"] = self.q__reason_combobox.get()
        self.data[self.current_index]["question_note"] = self.q_note_entry.get()
        self.data[self.current_index]["answer_grade"] = self.a_grade_entry.get()
        self.data[self.current_index]["answer__reason"] = self.a__reason_combobox.get()
        self.data[self.current_index]["answer_note"] = self.a_note_entry.get()

    def add_new_question_reason(self):
        new_reason = self.q__reason_combobox.get()
        if new_reason and new_reason not in self._reasons:
            self._reasons.append(new_reason)
            self.q__reason_combobox['values'] = self._reasons
            self.a__reason_combobox['values'] = self._reasons
            messagebox.showinfo("Info", "New  reason added.")

    def add_new_answer_reason(self):
        new_reason = self.a__reason_combobox.get()
        if new_reason and new_reason not in self._reasons:
            self._reasons.append(new_reason)
            self.q__reason_combobox['values'] = self._reasons
            self.a__reason_combobox['values'] = self._reasons
            messagebox.showinfo("Info", "New reason added.")

    def save_to_json(self):
        with open('1_annotated_data.json', 'w') as f:
            json.dump(self.annotated_data, f, indent=4)
        messagebox.showinfo("Info", "Final data saved successfully!")


if __name__ == "__main__":
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    root = tk.Tk()
    app = AnnotationApp(root, data['flashcards']['cards'])
    root.mainloop()
