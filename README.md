# BrayGPT: The Coding Tutor

BrayGPT is a personalized coding tutor powered by OpenAI's GPT-3.5. It offers a fun and interactive learning experience with the personality of comedian Kevin Hart. BrayGPT provides explanations, variations, and interactive games for learning various programming topics.

## Features

- Engaging and humorous responses
- Explains programming concepts in an easy-to-understand manner
- Offers variations and alternative approaches to problems
- Interactive games for learning programming topics
## DEMO

<img width="1408" alt="image" src="https://github.com/tsitirides/BRAYGPT_AI_TUTOR/assets/47327032/e28f0d01-e700-4009-8b7c-e7209c762aa2">

## Installation

To run BrayGPT locally, follow these steps:

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/BRAYGPT_AI_TUTOR
    cd braygpt
    ```

2. **Create a virtual environment**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**

    Install the dependencies listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**

    Create a `.env` file in the project root directory and add your OpenAI API key.

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

5. **Run the Streamlit app**

    Start the Streamlit application.

    ```bash
    streamlit run ai_tutor_test.py
    ```

## Usage

- Open the Streamlit app in your browser.
- Type your question or request in the input box and press Enter.
- BrayGPT will respond with an engaging and informative answer.

## Project Structure


- `.env.example`: Example file for environment variables.
- `.gitignore`: Git ignore file to exclude unnecessary files.
- `README.md`: This file.
- `ai_tutor_test.py`: Main application file.
- `requirements.txt`: List of required Python packages.

## Dependencies

- [Streamlit](https://streamlit.io/): For building the web interface.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables.
- [openai](https://pypi.org/project/openai/): For interacting with the OpenAI API.
- [streamlit-chat](https://pypi.org/project/streamlit-chat/): For creating a chat-like interface in Streamlit.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For any questions or feedback, please contact braydentsitirides@gmail.com

