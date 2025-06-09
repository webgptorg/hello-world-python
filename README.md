# ✨ Hello World!

Welcome! In this repository, you'll find a simple example of how to write your first [Book](https://github.com/webgptorg/book) and run it using the [Promptbook Engine](https://github.com/webgptorg/promptbook) via the Python.

## Getting Started

Follow these steps to get up and running:

### 1. Clone the Repository
First, clone this repository to your local machine.

```bash
git clone https://github.com/webgptorg/hello-world-python.git
cd hello-world-python
```

### 2. Install Dependencies


1) Install Python
2) Install Node.js and NPM
3) Install the NPM dependencies

```bash
npm ci
```

**Note:** Currently, installation is supported only via NPM. We are actively working on adding support for other package managers and installer files such as `.msi`, `.rpm`, and `.deb`.

### 3. Configure Environment Variables
Create a `.env` file in the root of the project to configure the necessary API keys for the model providers you plan to use:

```conf
# Note: You can configure just one of the keys, but you need to set at least one.
OPENAI_API_KEY=sk-proj-...
DEEPSEEK_GENERATIVE_AI_API_KEY=sk-...
GOOGLE_GENERATIVE_AI_API_KEY=AI...
ANTHROPIC_CLAUDE_API_KEY=sk-ant-api03-...

```

### 4. Run the Example
From the root of the repository, execute the following command to run the example:

```bash
python ./generate-poem.py
```

### Expected Output
If everything is set up correctly, you should see the following output:

```bash
$ python ./generate-poem.py

--- output ---
{'result': '{"result": "..."}'}
```

🚀✨ **Congratulations!** You've successfully created **your first book** with Promptbook! Now you can [continue with the examples](/books/) or [the book language blueprint](https://github.com/webgptorg/book) to dive deeper into the book language, [integrate books into your app]() or [create instant miniapps](#!!!!!!) without classical programming.
