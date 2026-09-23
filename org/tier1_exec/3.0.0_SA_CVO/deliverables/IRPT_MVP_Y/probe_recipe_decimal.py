"""Pinned offline upload-echo and actual create-wire precision review."""
import argparse
from decimal import Decimal
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import zipfile


AMOUNT = "9007199254740993.01"
SOURCE_ROOT = "infra/aws/lambda/investor-reporting/ycharts/generate"


def deny_network(*args, **kwargs):
    raise AssertionError("independent review forbids network")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def snapshot(root, short_pin):
    pin = subprocess.check_output(["git", "rev-parse", "--verify", short_pin + "^{commit}"],
                                  cwd=root, text=True).strip()
    target = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/decimal-review" / pin
    target.mkdir(parents=True, exist_ok=True)
    archive = subprocess.check_output(["git", "archive", "--format=zip", pin, SOURCE_ROOT,
        "infra/aws/lambda/investor-reporting/intake/settings.json"], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            path = (target / member.filename).resolve()
            if not path.is_relative_to(target.resolve()):
                raise ValueError("snapshot path escape")
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
                continue
            data = bundle.read(member)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            hashes[member.filename] = hashlib.sha256(data).hexdigest()
    return pin, target, hashes


def holdings(amount=AMOUNT, identifier="S:AAPL"):
    return [{"identifier": identifier, "quantity": {"units": "USD", "value": amount}}]


def echo(rows):
    entries = [('{"security_id":' + json.dumps(identifier)
                + ',"display_security_id":' + json.dumps(identifier)
                + ',"display_name":"Synthetic","weighting":' + amount + '}')
               for identifier, amount in rows]
    return ('{"status":"ok","errors":[],"weight":"Dollars",'
            '"upload_record_id":1,"rows":[' + ",".join(entries) + ']}').encode()


class OfflineTransport:
    def __init__(self, reply):
        self.reply, self.calls = reply, []

    def request(self, path, method, payload, mime):
        self.calls.append((path, method, payload, mime))
        if path == "/model_portfolios/fixed/holdings_upload/client":
            return {"status": 200}, self.reply
        if path == "/model_portfolios/fixed/":
            return {"status": 201}, b'{"model_portfolio_id":123}'
        raise AssertionError("unexpected offline route")


def multipart_parts(payload, mime):
    message = BytesParser(policy=policy.default).parsebytes(
        ("Content-Type: " + mime + "\r\nMIME-Version: 1.0\r\n\r\n").encode() + payload)
    return {part.get_param("name", header="content-disposition"): part.get_payload(decode=True)
            for part in message.iter_parts()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="386f2e1b49")
    parser.add_argument("--baseline", default="bfe5a33e17")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    baseline_pin, baseline, baseline_hashes = snapshot(root, args.baseline)
    candidate_pin, candidate, hashes = snapshot(root, args.pin)
    load("transport", baseline / SOURCE_ROOT / "transport.py")
    old = load("decimal_baseline_recipe", baseline / SOURCE_ROOT / "recipe.py")
    negative_reply = echo([("S:AAPL", "9007199254740993.02")])
    baseline_result = old.step_upload(OfflineTransport(negative_reply), holdings())
    load("transport", candidate / SOURCE_ROOT / "transport.py")
    recipe = load("decimal_candidate_recipe", candidate / SOURCE_ROOT / "recipe.py")
    candidate_result = recipe.step_upload(OfflineTransport(negative_reply), holdings())
    controls = []

    def record(name, passed, **observed):
        controls.append({"name": name, "passed": bool(passed), "observed": observed})

    record("original_one_cent_echo_mismatch",
           baseline_result["ok"] and baseline_result["reconciled"]
           and not candidate_result["ok"] and not candidate_result["reconciled"]
           and candidate_result["rows"] == [],
           source_amount=AMOUNT, echo_amount="9007199254740993.02",
           baseline=baseline_result, candidate=candidate_result)
    for label, source_rows, returned in (
        ("original_large_cent", holdings(), [("S:AAPL", AMOUNT)]),
        ("one_cent", holdings("0.01"), [("S:AAPL", "0.01")]),
        ("high_precision_fraction", holdings("0.1000000000000000000000000001"),
         [("S:AAPL", "0.1000000000000000000000000001")]),
        ("reordered_security_and_cash", holdings() + holdings("123.45", "$:CASH"),
         [("$:CASH", "123.45"), ("S:AAPL", AMOUNT)]),
    ):
        client = OfflineTransport(echo(returned))
        uploaded = recipe.step_upload(client, source_rows)
        retained = json.loads(json.dumps(uploaded))
        created = recipe.step_create(client, "offline-independent-precision", retained["upload_record_id"],
                                     retained["rows"], recipe.load_settings())
        upload_parts = multipart_parts(client.calls[0][2], client.calls[0][3])
        parts = multipart_parts(client.calls[1][2], client.calls[1][3])
        parsed = json.loads(parts["items"], parse_float=Decimal, parse_int=Decimal)
        expected = {row["identifier"]: Decimal(row["quantity"]["value"]) for row in source_rows}
        actual = {row["security_id"]: row["weighting"] for row in parsed}
        numeric = all(isinstance(row["weighting"], Decimal) for row in parsed)
        text_exact = all(Decimal(row["weight_text"]) == row["weighting"] for row in parsed)
        source_csv = upload_parts["holdings"].decode()
        record(label + "_through_checkpoint_and_actual_step_create",
               uploaded["ok"] and created["ok"] and expected == actual and numeric and text_exact
               and set(parts) == {"portfolio", "items"}
               and all(str(row["quantity"]["value"]) in source_csv for row in source_rows),
               upload_ok=uploaded["ok"], create_ok=created["ok"], checkpoint_rows=retained["rows"],
               csv=source_csv, actual_items_json=parts["items"].decode(),
               actual_route=client.calls[1][0], actual_method=client.calls[1][1],
               values={key: str(value) for key, value in actual.items()},
               numeric_not_strings=numeric, text_matches_number=text_exact)
    client = OfflineTransport(echo([("S:AAPL", AMOUNT), ("S:AAPL", AMOUNT)]))
    duplicate = recipe.step_upload(client, holdings())
    record("duplicate_echo_refused", not duplicate["ok"] and not duplicate["reconciled"]
           and duplicate["rows"] == [], result=duplicate)
    client = OfflineTransport(echo([("S:AAPL", AMOUNT)]))
    try:
        recipe.step_upload(client, holdings() * 2)
        reason = "RETURNED"
    except recipe.RecipeRefused as exc:
        reason = str(exc)
    record("duplicate_source_refused_before_transport", reason != "RETURNED" and not client.calls,
           reason=reason, transport_calls=len(client.calls))
    suite_code = ("import socket,pytest; "
                  "deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError('NETWORK_FORBIDDEN')); "
                  "socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; "
                  "raise SystemExit(pytest.main(['-q','" + SOURCE_ROOT + "/tests/test_recipe_decimal.py']))")
    suite = subprocess.run([sys.executable, "-c", suite_code], cwd=candidate,
                           capture_output=True, text=True, check=False)
    evidence = {"candidate_pin": candidate_pin, "baseline_pin": baseline_pin,
                "candidate_file_sha256": hashes, "baseline_file_sha256": baseline_hashes,
                "supplied_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "controls": controls, "passed": sum(row["passed"] for row in controls), "total": len(controls),
                "limits": ["Actual recipe upload/create and transport multipart serializer; injected offline replies",
                           "Original numeric scenario reproduced independently; no producer probe file supplied",
                           "JSON checkpoint is local serialization, not persistent worker restart",
                           "Socket connections forbidden; no vendor/session access or worker assembly proof"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in evidence.items() if not k.endswith("file_sha256")}, indent=2))
    if evidence["passed"] != evidence["total"] or suite.returncode:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
