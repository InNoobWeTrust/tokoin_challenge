# TokoinChallenge

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/InNoobWeTrust/tokoin_challenge)

Data searching challenge.

## Assumptions:
- json data is valid
- Each json data is an array
- Open and closing bracket is on its own line. No open or closing bracket inside each object
- key-value or array's item is on its own line
- No character needs to be escaped inside each key/value

## Searching strategy:
- Stream file content line by line
- On open bracket, begin storing values in temporary object store in memory
- Check for value matching with search term when iterating each line. If yes raise a flag so that object will be printed
- On closing bracket, if the flag is raise, print the object in memory. And either printing object or not, clear memory to process new object
- On closing square bracket, stop processing

## Error logging
**TODO**: Setup python logger to report logs to file and also on stdout

## Development

Install the project with poetry and start a shell

```shell
pip install --user poetry
poetry install
poetry shell
```

Then just start development inside the virtual environment that poetry created

## Running
Usage follow the principle of normal *NIX commandline tools

```shell
❯ poetry run search -h

Successfully set up prettification!
> All function returns will now be pretty-printed,

'[245 italic]Including [/italic 210]Markup!'

usage: search [-h] -m {user,ticket,organization} -s TERM [-f FIELD]

optional arguments:
  -h, --help            show this help message and exit
  -m {user,ticket,organization}, --mode {user,ticket,organization}
                        Search mode
  -s TERM, --term TERM  Search term
  -f FIELD, --field FIELD
                        Field to search for
```

If you just provide the mode, the command will suggest searchable fields for you to choose

```shell
❯ poetry run search -m user

Successfully set up prettification!
> All function returns will now be pretty-printed,

'[245 italic]Including [/italic 210]Markup!'

'Please provide search term!'
'For fine grained, you can filter by the specific fields below:'
[
  '_id',
  'url',
  'external_id',
  'name',
  'alias',
  'created_at',
  'active',
  'verified',
  'shared',
  'locale',
  'timezone',
  'last_login_at',
  'email',
  'phone',
  'signature',
  'organization_id',
  'tags',
  'suspended',
  'role',
]
```

## Commandline interface (TUI)
- For fantastic TUI, [pytermgui](https://github.com/bczsalba/pytermgui) is chosen.

**TODO**: make a TUI so that user can have master-detail view layout (to load metadata to show on demand)

## Testing

```shell
poetry install
poetry run pytest -s -v
```

## Building

With `poetry`, building python package is simple

```shell
poetry build
```

## Possible improvements:
- Using [pyrser](https://pythonhosted.org/pyrser/tutorial1.html#hooks) to parse json file iteratively into AST and doing the search string matcher on the hooks.
