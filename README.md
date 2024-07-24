# Annotation Tool

This project is a Python-based application that provides an interface for annotating question-answer pairs with their quality grades, reasons for rejection, and additional notes. The application is built using the Tkinter library for the graphical user interface.

## Features

The application provides the following features:

- **Question and Answer Display:** The application displays the question, answer, and citation text for each entry.

- **Quality Grading:** Users can grade the quality of both the question and the answer on a scale they define.

- **Rejection Reasons:** Users can select a reason for rejecting a question or an answer from a predefined list. They can also add new reasons to this list.

- **Additional Notes:** Users can add additional notes for both the question and the answer.

- **Navigation:** Users can navigate through the entries using the "Save Entry" and "Skip Entry" buttons.

- **Data Saving:** Users can save their annotations to a JSON file.

## Buttons

- **Save Entry:** This button saves the current annotations (grade, reason, and note) for the question and answer. After saving, it automatically loads the next entry.

- **Skip Entry:** This button skips the current entry without saving any annotations and loads the next entry.

- **Add New Reason (Question/Answer):** These buttons allow the user to add a new rejection reason to the list of available reasons for both questions and answers.

- **Save Final Data:** This button saves all the annotated data to a JSON file.

## Running the Application

To run the application, execute the `app.py` script. The script reads data from a JSON file named `data.json` and starts the Tkinter GUI.

```bash
python app.py
```

## Dependencies

This project is written in Python and uses the following libraries:

- Tkinter for the graphical user interface.
- json for reading and writing JSON data.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

This project is [MIT](./LICENSE) licensed.
