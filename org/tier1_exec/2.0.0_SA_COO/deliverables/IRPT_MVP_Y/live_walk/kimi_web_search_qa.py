#!/usr/bin/env python3
"""Y-5 packet 2's provider QA (the Kimi swap gate): does Moonshot's built-in web search work for the swap prompt, and in
what request shape? Kimi is VEW-3, "can be called freely" (org/ref/VENDOR_EGRESS_WHITELIST.yaml).

    python kimi_web_search_qa.py <symbol> <receipt.json> <transcript.json>

One swap-shaped request (resolution_kimi.prompt_for("swap", symbol)) to the advisory's model with the built-in tool
`{"type": "builtin_function", "function": {"name": "$web_search"}}`. While the answer's finish_reason is `tool_calls`
naming only `$web_search`, the assistant message is appended as returned and each call's arguments are echoed back as a
`tool` message (Moonshot's built-in protocol), at most MAX_ROUNDS sends. The final answer is parsed with the advisory's
own `_parse("swap", ...)`. The key is read BY NAME (kimi_port.secret_reader) into memory and never printed.

The RECEIPT holds shapes only: per send, the finish_reason, the tool-call names and counts, usage, elapsed seconds; the
parse outcome; the parsed answer's identified asset, candidate symbols and source URLs (public facts about a ticker); and
the sha256 of the full transcript. The transcript (the messages and answers) is written to its own path. ASCII only.
"""
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, *[".."] * 6))
LAMBDA = os.path.join(ROOT, "infra", "aws", "lambda", "investor-reporting")
for sub in ("intake", os.path.join("ycharts", "generate")):
    sys.path.insert(0, os.path.join(LAMBDA, sub))

import urllib.error  # noqa: E402
import urllib.request  # noqa: E402

import boto3  # noqa: E402
from kimi_port import kimi_send, secret_reader  # noqa: E402
from resolution_kimi import BUDGETS, MODEL, KimiFailure, _parse, prompt_for  # noqa: E402

TOOL = {"type": "builtin_function", "function": {"name": "$web_search"}}
MAX_ROUNDS = 4
QA_MODEL = os.environ.get("QA_MODEL", MODEL)  # a control run on another Moonshot model names it in the receipt
QA_TIMEOUT = int(os.environ.get("QA_TIMEOUT", "0"))  # a timing run past the swap budget; the receipt names it
QA_MAX_TOKENS = int(os.environ.get("QA_MAX_TOKENS", "0"))
LAST_HTTP_ERROR = {}


def capturing_opener(request, timeout):
    """urlopen that keeps an HTTP error's status and body (the provider's message, never the request's key)."""
    try:
        return urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.HTTPError as exc:
        LAST_HTTP_ERROR.update(status=exc.code, body=exc.read(4096).decode("utf-8", "replace"))
        raise


def main(argv):
    symbol, receipt_path, transcript_path = argv[1], argv[2], argv[3]
    prompt, _ = prompt_for("swap", symbol)
    budget = BUDGETS["swap"]
    send = kimi_send(secret_reader(boto3.client("secretsmanager", region_name="us-east-1")), opener=capturing_opener)
    messages = [{"role": "user", "content": prompt}]
    if os.environ.get("QA_PROMPT_SHAPE") == "system":
        # QA variant: the instruction as a system message, the data (prompt_for's last line) as the user message.
        instruction, _, data = prompt.rpartition(chr(10))
        messages = [{"role": "system", "content": instruction}, {"role": "user", "content": data}]
    transcript, rounds = [], []
    answer = None
    for n in range(1, MAX_ROUNDS + 1):
        payload = {"model": QA_MODEL, "temperature": 1, "max_tokens": QA_MAX_TOKENS or budget["max_tokens"], "messages": messages,
                   "tools": [TOOL]}
        if os.environ.get("QA_JSON_MODE") == "1":
            payload["response_format"] = {"type": "json_object"}
        started = time.monotonic()
        try:
            answer = send(payload, timeout_seconds=QA_TIMEOUT or budget["timeout_seconds"])
            error = None
        except (KimiFailure, TimeoutError) as exc:
            answer, error = None, getattr(exc, "code", None) or str(exc)
            if LAST_HTTP_ERROR:
                error = "%s %s %s" % (error, LAST_HTTP_ERROR.get("status"), LAST_HTTP_ERROR.get("body", "")[:300])
                LAST_HTTP_ERROR.clear()
        elapsed = round(time.monotonic() - started, 1)
        transcript.append({"round": n, "request_messages": len(messages), "answer": answer, "error": error})
        choice = (answer or {}).get("choices", [{}])[0] if isinstance(answer, dict) else {}
        message = choice.get("message") or {}
        calls = message.get("tool_calls") or []
        names = [((c.get("function") or {}).get("name")) for c in calls]
        usage = (answer or {}).get("usage") if isinstance(answer, dict) else None
        rounds.append({"round": n, "error": error, "elapsed_seconds": elapsed, "finish_reason": choice.get("finish_reason"),
                       "tool_call_names": names, "has_reasoning_content": "reasoning_content" in message,
                       "usage": {k: v for k, v in (usage or {}).items() if isinstance(v, int)}})
        print("round %d: %s finish=%s tools=%s %.1fs" % (n, error or "OK", choice.get("finish_reason"), names, elapsed))
        if error or choice.get("finish_reason") != "tool_calls" or not calls or any(x != "$web_search" for x in names):
            break
        # QA variants (env): QA_TOOL_NAME=0 omits the tool message's name; QA_ASSISTANT_CONTENT=null sends None for an
        # empty assistant content. Each run's receipt names the variant it ran.
        echoed = dict(message)
        if os.environ.get("QA_ASSISTANT_CONTENT") == "null" and not echoed.get("content"):
            echoed["content"] = None
        tool_messages = []
        for c in calls:
            tm = {"role": "tool", "tool_call_id": c.get("id"), "content": (c.get("function") or {}).get("arguments") or "{}"}
            if os.environ.get("QA_TOOL_NAME", "1") != "0":
                tm["name"] = "$web_search"
            tool_messages.append(tm)
        messages = messages + [echoed] + tool_messages
    parsed, parse_failure = None, None
    try:
        parsed = _parse("swap", answer)
    except KimiFailure as exc:
        parse_failure = exc.code
    text = json.dumps(transcript, sort_keys=True, ensure_ascii=True, default=str)
    with open(transcript_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    receipt = {
        "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "model": QA_MODEL, "advisory_model": MODEL, "symbol": symbol, "tool": TOOL,
        "max_rounds": MAX_ROUNDS, "sends": len(rounds),
        "variant": {"QA_TOOL_NAME": os.environ.get("QA_TOOL_NAME", "1"), "QA_TIMEOUT": QA_TIMEOUT,
                    "QA_MAX_TOKENS": QA_MAX_TOKENS, "QA_PROMPT_SHAPE": os.environ.get("QA_PROMPT_SHAPE", "user"),
                    "QA_JSON_MODE": os.environ.get("QA_JSON_MODE", "0"),
                    "QA_ASSISTANT_CONTENT": os.environ.get("QA_ASSISTANT_CONTENT", "as-returned")}, "rounds": rounds, "parse_failure": parse_failure,
        "parsed": None if parsed is None else {
            "identified_asset": parsed.get("identified_asset"), "security_type": parsed.get("security_type"),
            "candidates": [c.get("symbol") for c in parsed.get("candidates") or []],
            "sources": parsed.get("sources") or [],
            "candidate_sources": [len(c.get("sources") or []) for c in parsed.get("candidates") or []]},
        "transcript_sha256": hashlib.sha256(text.encode()).hexdigest(),
    }
    with open(receipt_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True)
    print("sends %d | parse %s | transcript sha256 %s" % (len(rounds), parse_failure or "OK",
                                                          receipt["transcript_sha256"][:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
