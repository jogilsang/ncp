



brew update
brew install pyenv

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

pyenv install --list
pyenv versions
pyenv install 3.7.13
pyenv global 3.7.13

```s
"2022-09-27T00:29:25.203855101Z stderr: Traceback (most recent call last):"
"2022-09-27T00:29:25.203955472Z stderr: File "exec__.py", line 67, in <module>"
"2022-09-27T00:29:25.203970427Z stderr: out.write(json.dumps(res, ensure_ascii=False).encode('utf-8'))"
"2022-09-27T00:29:25.203984676Z stderr: File "/usr/local/lib/python3.7/json/__init__.py", line 238, in dumps"
"2022-09-27T00:29:25.203991072Z stderr: **kw).encode(obj)"
"2022-09-27T00:29:25.203996615Z stderr: File "/usr/local/lib/python3.7/json/encoder.py", line 199, in encode"
"2022-09-27T00:29:25.204002468Z stderr: chunks = self.iterencode(o, _one_shot=True)"
"2022-09-27T00:29:25.204007843Z stderr: File "/usr/local/lib/python3.7/json/encoder.py", line 257, in iterencode"
"2022-09-27T00:29:25.204013907Z stderr: return _iterencode(o, 0)"
"2022-09-27T00:29:25.204019063Z stderr: File "/usr/local/lib/python3.7/json/encoder.py", line 179, in default"
"2022-09-27T00:29:25.204024746Z stderr: raise TypeError(f'Object of type {o.__class__.__name__} '"
"2022-09-27T00:29:25.204030354Z stderr: TypeError: Object of type KeyError is not JSON serializable"
```