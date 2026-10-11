"""IRPT_ANLREQ AR-g-41: build_resident_package.optional_bindings and the three optional flags. Offline; no build is run."""
import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("build_resident_package_under_test", HERE / "build_resident_package.py")
builder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(builder)
fn = builder.optional_bindings

Q1 = "https://sqs.us-east-1.amazonaws.com/000000000000/example-analysis-ready"
Q2 = "https://sqs.us-east-1.amazonaws.com/000000000000/example-commentary-ready"
PK = {"api_base": "https://example.invalid", "email": "svc-example@example.invalid", "secret_name": "example/name"}


def test_none_given_gives_the_empty_dict():
    assert fn() == {}


def test_all_three_given_gives_all_three():
    assert fn(analysis_ready_queue_url=Q1, commentary_ready_queue_url=Q2, packager=dict(PK)) == {
        "analysis_ready_queue_url": Q1, "commentary_ready_queue_url": Q2, "packager": PK}


def test_the_analysis_queue_alone_is_enough():
    assert fn(analysis_ready_queue_url=Q1) == {"analysis_ready_queue_url": Q1}


@pytest.mark.parametrize("key", ["analysis_ready_queue_url", "commentary_ready_queue_url"])
@pytest.mark.parametrize("value", ["http://sqs.example", "queue", "", 5, ["https://sqs.x"]])
def test_a_bad_queue_url_is_refused_with_its_key(key, value):
    with pytest.raises(ValueError) as raised:
        fn(**{key: value}, packager=dict(PK))
    assert str(raised.value) == "BINDING_QUEUE_URL:" + key


@pytest.mark.parametrize("packager", [
    "x", [], {}, {"api_base": PK["api_base"]}, {**PK, "extra": "1"}, {**PK, "email": ""}, {**PK, "secret_name": " "},
    {**PK, "api_base": "http://example.invalid"}, {**PK, "api_base": 5}])
def test_a_malformed_packager_is_refused(packager):
    with pytest.raises(ValueError) as raised:
        fn(commentary_ready_queue_url=Q2, packager=packager)
    assert str(raised.value) == "BINDING_PACKAGER_KEYS"


def test_a_commentary_queue_without_a_packager_is_refused():
    with pytest.raises(ValueError) as raised:
        fn(commentary_ready_queue_url=Q2)
    assert str(raised.value) == "BINDING_PACKAGER_REQUIRED"


def test_a_packager_without_a_commentary_queue_is_refused():
    with pytest.raises(ValueError) as raised:
        fn(packager=dict(PK))
    assert str(raised.value) == "BINDING_PACKAGER_WITHOUT_QUEUE"
    with pytest.raises(ValueError) as raised:
        fn(analysis_ready_queue_url=Q1, packager=dict(PK))
    assert str(raised.value) == "BINDING_PACKAGER_WITHOUT_QUEUE"


def test_the_packager_flag_text_parses_to_the_three_keys():
    text = "api_base=https://example.invalid,email=svc-example@example.invalid,secret_name=example/name"
    assert builder.parse_packager(text) == PK
    with pytest.raises(ValueError) as raised:
        fn(commentary_ready_queue_url=Q2, packager=builder.parse_packager("api_base=https://example.invalid,email"))
    assert str(raised.value) == "BINDING_PACKAGER_KEYS"


def test_importing_the_module_runs_no_build_and_a_refusal_ends_main_before_any_read(capsys):
    with pytest.raises(SystemExit) as raised:
        builder.main(["--pin", "HEAD", "--enrolled-user-id", "1", "--out", "unused-nowhere", "--dry-run",
                      "--commentary-ready-queue-url", Q2])
    assert str(raised.value) == "BINDING_PACKAGER_REQUIRED"
    assert not Path("unused-nowhere").exists()
    assert capsys.readouterr().out == ""
