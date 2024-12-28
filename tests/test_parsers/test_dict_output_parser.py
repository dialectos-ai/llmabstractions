import pytest

from llmabstractions import json_data_parser

dict_output = {
    'key1': 'value1',
    'key2': 'value2'
}

array_output = [
    {
        "key1": "value1"
    },
    {
        "key2": "value2"
    }
]

json_dict_output = """
```json
{
    "key1": "value1",
    "key2": "value2"
}
```
"""

json_array_output = """
```json
[
    {
        "key1": "value1"
    }, 
    {
        "key2": "value2"
    }
]
```
"""

code_snippet_dict_output = """
```
{
    "key1": "value1",
    "key2": "value2"
}
```
"""

code_snippet_array_output = """
```
[
    {
        "key1": "value1"
    }, 
    {
        "key2": "value2"
    }
]
```
"""

python_snippet_output = """
```python
{
    "key1": "value1",
    "key2": "value2"
}
```
"""

json_with_dict_snippet = """
Here is my response

```json
{
    "key1": "value1",
    "key2": "value2"
}
```
"""
json_with_array_snippet = """
Here is my response

```json
[
    {
        "key1": "value1"
    }, 
    {
        "key2": "value2"
    }
]
```
"""

snippet_with_dict = """
Here is the response

```
{
    "key1": "value1",
    "key2": "value2"
}
```
Is there something else?
"""

snippet_with_array = """
Here is the response

```
[
    {
        "key1": "value1"
    }, 
    {
        "key2": "value2"
    }
]
```
Is there something else?
"""

text_with_dict = """
Here is the response

{
    "key1": "value1",
    "key2": "value2"
}

Is there something else?
"""


text_with_array = """
Here is the response

[
    {
        "key1": "value1"
    }, 
    {
        "key2": "value2"
    }
]

Is there something else?
"""

@pytest.mark.parametrize("llm_output,type", [
    (dict_output, 'dictionary'),
    (array_output, 'array'),
    (json_dict_output, 'dictionary'),
    (json_array_output, 'array'),
    (code_snippet_dict_output, 'dictionary'),
    (code_snippet_array_output, 'array'),
    (python_snippet_output, 'dictionary'),
    (json_with_dict_snippet, 'dictionary'),
    (json_with_array_snippet, 'array'),
    (snippet_with_dict, 'dictionary'),
    (snippet_with_array, 'array'),
    (text_with_dict, 'dictionary'),
    (text_with_array, 'array')
])
def test_dictionary_output_parser_outputs(llm_output, type):
    # action
    parsed_output = json_data_parser(llm_output)

    # assertions
    if type == 'dictionary':
        assert parsed_output['key1'] == 'value1'
        assert parsed_output['key2'] == 'value2'
    else:
        assert parsed_output[0]['key1'] == 'value1'
        assert parsed_output[1]['key2'] == 'value2'
