# SSTv3 LLM MD

Simple SSTv3 Markdown to train an LLM to understand SSTv3
I have used crawl4ai to generate the markdown, and have provided this as is.
If you want to regenerate the sstv3.md clone, and follow the following.

```bash
# Clone Repo.
git clone https://github.com/michaelcuneo/sstv3-llm-md
# Go to the folder
cd sstv3-llm-md
# Install a Virtual Environment
python3 -m venv venv
# Activate the Virtual Environment
source venv/bin/activate
# Install Requirements, crawl4ai.
pip3 install -m requirements
# OPTIONAL IF YOU DO NOT HAVE HEADLESS CHROMIUM INSTALLED
python -m playwright install --with-deps chromium
# Run main.py to generate sstv3.md
python3 main.py
```

To use with an LLM, just download or clone, and upload sstv3.md to the LLM

The generated markdown is a little dirty, and will need a cleanup with a markdown linter. I have also had to find/replace *```* on newlines and replaced with typescript designator.
