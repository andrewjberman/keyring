# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0745Z – 0810Z

**archetype:** TRACE
**Projects:** D7_NOTIFY — TO-C (J2 atom-decomp: the Teams send path)

## Summary

First of the three ACTIVE TOs, taken first because it is a read and self-contained.
`D7_NOTIFY.TO-C_PROOF_OF_SPEC.json` **VALID rc=0, 3 rows, 0 violations, 3/3 PASS.** Read-only:
nothing built, nothing deployed, **nothing posted.**

Before starting I re-read the amended law from the ref (`@5e4a71d604`) rather than my loaded copy —
Rule 21 now carries the `comp-find` case-sensitivity amendment, and the `org/XXX.md` edit touches
only the COO row.

## 1 — The answer, and it is a code answer rather than a prose one

Both Teams sends hardcode the same payload, with **no branch, no parameter, no caller override**:

```
tools.py:613  send_chat_message     -> POST /chats/{chat_id}/messages
tools.py:654  send_channel_message  -> POST /teams/{team_id}/channels/{channel_id}/messages
:617 / :658   payload = {"body": {"contentType": "text", "content": message}}
```

Content-type census across the gateway: **8 hits / 71 files** — 2 Teams (`"text"`), **2 EMAIL at
:220/:238 (`"Text"`)**, and 4 unrelated (attachment metadata, an S3 `ContentType`, a mock fixture).
**Every outbound message path in the gateway is plain text, not only Teams.**

>> **THEREFORE ANDREW'S ASK CANNOT BE MET BY A FORMATTING STANDARD.** *"hyperlinks (which should be
properly linked to be clickable)"* requires `contentType: "html"` — **a code change to a live EC2
service, i.e. a deploy, not a style guide.** A standard written today would specify link markup the
renderer discards. **That is exactly what J2 exists to prevent**, and it is why TO-D activates on
TO-C rather than beside it.

## 2 — What I deliberately did not do

C-2 says *"if it cannot be measured without posting, say so and stop; do not post to prove it."*

Whether the Teams **client** auto-linkifies a **bare URL** under `contentType: text` is a renderer
behaviour observable only by posting. **I did not post**, and no Graph call was issued (a gateway
send is also vendor egress). So the row splits three ways rather than resolving into one verdict:

| | |
|---|---|
| **MEASURED (source)** | the literal `"text"` at both sites |
| **DECLARED (vendor contract)** | under `text`, content is not parsed as markup → a markdown link renders literally |
| **UNMEASURED** | bare-URL autolinking |

**The row must not be read as "a bare URL is unclickable."** It establishes that *markup* is not
honoured and that the autolink question is open.

## 3 — The credential half, re-derived rather than cited

`server.py::_bearer_email` fully validates the gateway Bearer (RS256 / iss / aud / exp) at the HTTP
layer; `tools.py:64 _run` then resolves identity and returns `identity_required` if absent. **So
validation precedes tool dispatch and no per-tool exception is expressible** — which independently
confirms CTO~Z's WE-1 structural disqualification of the gateway as a backstop transport. I re-derived
it because a relay of a ruling inherits that ruling's staleness silently.

## 4 — ⛔ My own commit told a future applier the wrong on-box path, and it was already wrong

`90d526c199` (mine, 2026-08-20) states the on-box artifact is `/opt/m365-mcp-gateway/app/tools.py`,
citing a **2026-07-31** deploy record — and I flagged it in that commit as *"the thing the applier
most needs."*

`EC2_MANIFEST.json`, Rule 8's source of truth, carries `remote_path: /opt/opal-gateway` with
`_status: OPAL_GWRENAME P2/S4 CUTOVER DEPLOYED 2026-08-15`.

**The rename landed 08-15. I wrote the message 08-20. Stale by five days at authoring.** The 07-31
record was true when written and carries no pointer to its own supersession — the closed-record class,
and the more precisely I cited it the more confidently I was wrong.

## 5 — Deployed-vs-built on the send-path file

| | |
|---|---|
| manifest `deployed_commit` | `5a1cc39e8e` @ 2026-08-20T16:19:36Z |
| recorded md5 vs repo@that commit | `06e1fd0a…` — **MATCH**, so the record is internally consistent, not merely self-reported |
| HEAD | `beba08bb…` — **differs**, 2 commits ahead (`2b7258f31c`, `90d526c199`, both mine, both BUILD-ONLY) |

**Plane stated: this is DECLARED, not APPLIED.** Rule 22a is explicit that for EC2 a staged or
recorded artifact proves what is *there*, never what *runs*; the applied read is SSM and is out of a
read-only TO's scope. Not claimed.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find -i 'def send_chat_message\|def send_channel_message'` | DENOM 60 / 27,232 files, **BANDS DEF=2 SURFACED=58** | **THE BAND SPLIT WAS THE INSTRUMENT** — the 58 are rail-log lines recording July DENYs of somebody grepping for these very functions; a raw grep returns the same 60 with no way to separate them |
| `comp-find -i contentType` (gateway) | 8 / 71 files, fully classified | complete census, email pair found |
| `python ast.get_source_segment` | both send functions whole | AST not sed — a line range drifts, the literal is load-bearing |
| `EC2_MANIFEST` + md5 triple | recorded == repo@deployed, HEAD differs | DECLARED plane, labelled as such |
| `proof-of-spec-check` positional | rc=0, rows=3, violations=0, VALID | PASS |
| own-instance mutant (anchor-asserted) | rc=1, violations=2, INVALID, naming the C-1 row | **CONTROLLED — own-instance per COO~Z's standing requirement, no sibling run cited** |

Ran `-i` throughout, per the amendment I raised and CTO~Z landed hours earlier.

## Blockers

**None.** TO-D is unblocked by this measurement but stays STAGED until CTO~Z accepts TO-C. Next at
this seat: **TO-B** (client-facing surface — it also resolves TO-A's A4/A6 link target, so it precedes
TO-A), then **TO-A** at eight criteria, re-read from the ref for A-3b. The W-F import edge remains
unwritten and is TO-F's last act. Zero crons, zero gateway calls, nothing applied, nothing posted.
