# How to pytest

Run [pytest](https://docs.pytest.org/) tests with `pytest` in the root directory of the project (active venv).  

On first run initialize cassette files with `pytest --vcr-record=once`.  

*Rule*: Add docstrings to all fixtures!  


## config options

pytest is configured in the `pyproject.toml` file in `[tool.pytest.ini_options]`.

- `norecursedirs` will exclude the listed directories from being searched for tests
- `xfail_strict` will pass tests that fail and are marked as `xfail` but will complain about tests that are marked as `xfail` but pass
- `addopts` will add the listed options to the command line options


## cli options

```bash
# only run tests marked as slow (skipped by default - see pyproject.toml[tool.pytest.ini_options].addopts)
pytest -m slow

# Record vcr cassettes once
pytest --vcr-record=once

# Show all fixtures (that's the reason we always write docstrings for our fixtures)
pytest --fixtures

# Show the slowest n tests
pytest --durations=n

# Show coverage
pytest --cov

# Only run tests that failed in the last run
pytest --last-failed

# Show fixture setup/teardown output
pytest --setup-show

# Drop into pdb on test failure
pytest --pdb

```


## database access

```python
# use a decorator, that might be atomic
@pytest.mark.django_db(transaction=True)
def test_db_access(some_db_instance):
    ...

```


## builtin fixtures

```python
# capsys -> captures stdout and stderr
def test_output(capsys)
    print("test")
    out, err = capsys.readouterr()
    assert out == "test\n"

# capfd -> captures stdout and stderr at file descriptor level (for subprocesses etc)
def test_descriptors(capfd)
    subprocess.run(["echo", "test"])
    out, err = capfd.readouterr()
    assert out == "..."

# caplog -> lets you capture log messages
def test_logging(caplog):
    logging.warning("test")
    assert caplog.messages == ["test"]

# request -> gives access to the requesting test context and markers
@pytest.fixture
@pytest.mark.marker_name("arg1", arg2="value")
def test_testcontext(request: pytest.FixtureRequest):
    # context
    request.function    # test function/method
    request.cls         # class of test
    request.instance    # class instance
    request.module      # module of test
    request.fspath      # path object of module
    request.node        # collection node
    request.config      # pytest config object
    request.param       # parameter of test function

    # markers
    marker = request.node.get_closest_marker("marker_name") # get marker
    if marker is None:
        return Config()
    return Config(*marker.args, **marker.kwargs)

# add command line options
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--endpoint-url", type=str)

@pytest.fixture
def endpoint_url(request: pytest.FixtureRequest) -> str:
    return request.config.option.endpoint_url

def test_endpoint(endpoint_url):
    ...

```

## coverage reports

Using [pytest-cov](https://github.com/pytest-dev/pytest-cov).

```bash
# run pytest with coverage
pytest --cov

# basic report
coverage report

# html report (writes to htmlcov/)
coverage html

...
```


## vcr

Record requests with [vcrpy](https://vcrpy.readthedocs.io/en/latest/) to save
all request-response data to a cassette file and replay them on subsequent
runs. Decorate with `pytest.mark.vcr`.

As the default `addopts` is `--vcr-record=none` run `pytest --vcr-record=once`
to initialize the cassette files.

```python
@pytest.mark.vcr
def test_some_api_endpoint():
    r = httpx.get("https://example.com")
    assert r.status_code == 200

```


## async

Install the [async library you are using](https://github.com/pytest-dev/pytest-asyncio) (e.g. `pytest-asyncio`).

```python
@pytest_asyncio.fixture
async def async_fixture():
    yield 42

@pytest.mark.asyncio
async def test_async(async_fixture):
    answer = await asyncio.sleep(1, result=async_fixture)
    assert answer == 42

```


## freezegun

Freeze time with [https://github.com/spulec/freezegun](freezegun) to make tests deterministic.

```python
from freezegun import freeze_time

# decorate
@freeze_time("2222-22-22")
def test_now_is_the_future():
    assert datetime.datetime.now() == datetime.datetime(2222, 22, 22)

# context manager
def test_now_is_the_future():
    with freeze_time("2222-22-22"):
        assert datetime.datetime.now() == datetime.datetime(2222, 22, 22)

```

## hypothesis

Randomized _fuzzing_ tests with [hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python).

Probably mark fuzzing-tests as `slow` and run them with `pytest -m slow`.

```python

...  # see https://hypothesis.readthedocs.io/en/latest/quickstart.html

```


## extra: BDD - behaviour driven development

To support [BDD style tests](https://pytest-bdd.readthedocs.io/en/stable/) install `pytest-bdd`. Make your PO happy 👽.
