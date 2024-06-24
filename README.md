# Text-Summarization

## Overview
This project is a web application designed to summarize PubMed articles. It combines web development and data science skills to provide a user-friendly interface for summarizing medical research articles.

## Features

- Upload or input PubMed articles for summarization.
- Display both original and summarized versions of the articles.

## Project Structure

- **app.py**: Main application file developed using Streamlit or Flask.
- **main.ipynb**: Jupyter notebook for data exploration, preprocessing, and model fine-tuning.
- **project.pdf**: Detailed project instructions and requirements.

## Instructions

### Data Exploration and Preparation

1. Load the PubMed Summarization dataset from Hugging Face.
2. Explore the dataset to understand its structure and contents.
3. Preprocess the dataset to clean and prepare the text for summarization.

### Web Application Development

1. Develop the web application using Streamlit or Flask.
2. Implement the summarization feature using the T5-small model from Hugging Face.
   - Model documentation: [T5-small](https://huggingface.co/docs/transformers/en/model_doc/t5)
3. Allow users to input or upload PubMed articles and display the summarized version.

### Jupyter Notebook (`main.ipynb`)

In the `main.ipynb` notebook, the following steps are carried out:

1. **Data Loading**: Load the PubMed Summarization dataset from Hugging Face.
2. **Data Exploration**: Explore the dataset to understand its structure, including the format of articles and summaries.
3. **Data Preprocessing**: Clean and preprocess the text data to prepare it for the summarization task.
4. **Model Integration**: Integrate the T5-small model for text summarization.
5. **Model Fine-tuning**: Fine-tune the T5-small model on the cleaned and preprocessed dataset to improve summarization performance.
6. **Evaluation**: Evaluate the performance of the fine-tuned model using appropriate metrics.
7. **Saving the Model**: Save the fine-tuned model for deployment in the web application.

## Evaluation Criteria

- **Data Exploration and Preparation (25%)**: Quality and thoroughness of data cleaning and preprocessing.
- **Web Application Development (35%)**: Functionality, usability, and design of the web application.
- **Generative AI Model Integration (30%)**: Model selection, fine-tuning, and performance evaluation.
- **Documentation (30%)**: Clarity, organization, and completeness.

## References

- [T5-small Model Documentation](https://huggingface.co/docs/transformers/en/model_doc/t5)
