"""teams-watch.py message_preview(): a preview is NEVER blank (CTO~Z ruling 35245; finding from 0.0.3_BG_BBGTerminal msg 35243).

The fixtures mirror the STRUCTURE measured on a real Alyssa 1:1 message (0.0.3_BG_BBGTerminal msg 35248): body.content is exactly
two <attachment> tags and no text; attachments[0] is a forwardedMessageReference whose .content is a JSON STRING holding the forwarded
text under originalMessageContent; attachments[1] is a `reference` with a name. Every text value here is a placeholder: no client
content is kept in the repo. The body-text message is the control, and it must come out byte-for-byte as the old strip produced it.
"""
import importlib.util
import json
import pathlib
import re

import pytest

SRC = pathlib.Path(__file__).resolve().parent / "teams-watch.py"
spec = importlib.util.spec_from_file_location("teams_watch_under_test", SRC)
tw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tw)

TAGS_ONLY = '<attachment id="1111"></attachment><attachment id="2222"></attachment>'


def fwd_att(original_html="<p>Placeholder forwarded instructions</p>", as_string=True):
    c = {"messageId": "m-1", "originalMessageContent": original_html, "originalSender": {"user": {"displayName": "Placeholder Sender"}}}
    return {"id": "1111", "contentType": "forwardedMessageReference", "contentUrl": None,
            "content": json.dumps(c) if as_string else c, "name": None}


def ref_att(name="placeholder-deck.pptx"):
    return {"id": "2222", "contentType": "reference", "contentUrl": "https://example.invalid/x", "name": name, "content": None}


def old_preview(m):
    raw = (m.get("body") or {}).get("content") or ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)).strip()[:400]


def test_measured_message_old_builder_was_blank_new_is_not():
    m = {"body": {"content": TAGS_ONLY}, "attachments": [fwd_att(), ref_att()]}
    assert old_preview(m) == ""                      # the defect, reproduced
    assert tw.message_preview(m) == "[forwarded] Placeholder forwarded instructions"


def test_control_body_text_is_unchanged_byte_for_byte():
    m = {"body": {"content": "<p>Hello  <b>there</b>,\nplease look</p>"}, "attachments": [fwd_att(), ref_att()]}
    assert tw.message_preview(m) == old_preview(m) == "Hello there , please look"


def test_body_text_wins_over_a_forward():
    m = {"body": {"content": "<p>see this</p>"}, "attachments": [fwd_att()]}
    assert tw.message_preview(m) == "see this"


def test_attachment_names_when_the_forward_has_no_readable_text():
    m = {"body": {"content": TAGS_ONLY}, "attachments": [ref_att("a.pptx"), ref_att("b.xlsx")]}
    assert tw.message_preview(m) == "[attachment] a.pptx, b.xlsx"


@pytest.mark.parametrize("bad", ["{not json", "[]", "\"text\"", "", None, {"originalMessageContent": 5}, {"x": "y"}])
def test_unreadable_forward_falls_through_never_raises(bad):
    a = fwd_att()
    a["content"] = bad
    m = {"body": {"content": TAGS_ONLY}, "attachments": [a, ref_att("deck.pptx")]}
    assert tw.message_preview(m) == "[attachment] deck.pptx"


def test_forward_content_already_a_dict_is_read_too():
    m = {"body": {"content": TAGS_ONLY}, "attachments": [fwd_att(as_string=False)]}
    assert tw.message_preview(m) == "[forwarded] Placeholder forwarded instructions"


def quote_att(preview="Placeholder quoted text", as_string=True):
    c = {"messageId": "m-2", "messagePreview": preview, "messageSender": {"user": {"displayName": "Placeholder Sender"}}}
    return {"id": "3333", "contentType": "messageReference", "contentUrl": None,
            "content": json.dumps(c) if as_string else c, "name": None}


def test_quote_reply_with_no_own_text_reads_the_quoted_preview():
    m = {"body": {"content": '<attachment id="3333"></attachment>'}, "attachments": [quote_att()]}
    assert old_preview(m) == ""
    assert tw.message_preview(m) == "[quoted] Placeholder quoted text"
    m["attachments"] = [quote_att(as_string=False)]
    assert tw.message_preview(m) == "[quoted] Placeholder quoted text"


def test_quote_reply_with_own_text_keeps_the_own_text():
    m = {"body": {"content": '<attachment id="3333"></attachment>my answer'}, "attachments": [quote_att()]}
    assert tw.message_preview(m) == "my answer"


def test_unreadable_quote_falls_through_to_the_marker():
    a = quote_att()
    a["content"] = "{not json"
    m = {"body": {"content": '<attachment id="3333"></attachment>'}, "attachments": [a]}
    assert tw.message_preview(m) == tw.ATTACHMENT_ONLY_MARKER


def test_two_forwards_are_joined():
    m = {"body": {"content": TAGS_ONLY}, "attachments": [fwd_att("<p>one</p>"), fwd_att("<p>two</p>")]}
    assert tw.message_preview(m) == "[forwarded] one | two"


def test_marker_when_there_is_nothing_at_all():
    for m in ({}, {"body": None}, {"body": {"content": None}}, {"body": {"content": TAGS_ONLY}},
              {"body": {"content": TAGS_ONLY}, "attachments": [{"contentType": "reference"}]},
              {"body": {"content": TAGS_ONLY}, "attachments": ["junk", 3, None]}):
        assert tw.message_preview(m) == tw.ATTACHMENT_ONLY_MARKER == "[attachment-only message]"


def test_cap_is_400_and_never_blank_over_a_sweep():
    long = "<p>" + ("word " * 400) + "</p>"
    assert len(tw.message_preview({"body": {"content": long}})) == 400
    assert len(tw.message_preview({"body": {"content": TAGS_ONLY}, "attachments": [fwd_att(long)]})) == 400
    shapes = [{}, {"body": {"content": ""}}, {"body": {"content": TAGS_ONLY}}, {"body": {"content": TAGS_ONLY}, "attachments": [fwd_att()]},
              {"body": {"content": "<p>x</p>"}}, {"attachments": [ref_att()]}]
    assert all(tw.message_preview(s).strip() for s in shapes)


def test_fresh_messages_emits_a_non_blank_preview_for_the_measured_message():
    page = {"value": [
        {"createdDateTime": "2026-10-16T19:55:00.000Z", "from": {"user": {"displayName": "Placeholder Sender"}},
         "body": {"content": TAGS_ONLY}, "attachments": [fwd_att(), ref_att()]},
        {"createdDateTime": "2026-10-16T19:56:00.000Z", "from": {"user": {"displayName": "Placeholder Sender"}},
         "body": {"content": "<p>plain text</p>"}},
    ]}
    out = tw.fresh_messages(page, "chat-1", "oneOnOne", "2026-10-16T19:00:00Z")
    assert [m["preview"] for m in out] == ["[forwarded] Placeholder forwarded instructions", "plain text"]
    assert all(m["preview"].strip() for m in out)
