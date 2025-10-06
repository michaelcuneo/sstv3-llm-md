# SSTv3 LLM MD

Simple SSTv3 Markdown to train an LLM to understand SSTv3
I have used crawl4ai to generate the markdown, and have provided this as is.
If you want to regenerate the sstv3.md clone, and follow the following.

```terminal
git clone https://github.com/michaelcuneo/sstv3-llm-md
cd sstv3-llm-md
python3 -m venv venv
source venv/bin/activate
pip3 install -m requirements
python -m playwright install --with-deps chromium # OPTIONAL IF YOU DO NOT HAVE HEADLESS CHROMIUM INSTALLED
python3 main.py
```

To use with an LLM, just download or clone, and upload sstv3.md to the LLM
