# AMGT_RESAPP round 24: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T10:3xZ at HEAD `27cc18ecd1`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND24_L8_PACKET_20260922.md` @`27cc18ecd1`; the two orders; the channel census;
read-only instruments from this seat: the live Lambda configuration, the function's CloudWatch logs since the apply, and
an in-process probe of rk-96's serialiser.

## Round state

**2 of 2 terminal** (`rk-96` NaN rule @`0221cbef39`, `rk-97` memory 1769 MB @`3fc2ffd89f`). The sweep reads PASS 15 /
FAIL 0 / UNVERIFIABLE 0 of 15 over 2 orders; the order files carry 15 criterion ids (6 + 9); **judgment census 0 of 2.**
**One arm is re-graded here: rk-97 AC5 (c), which the worker recorded PASS on a literal miss** (below).

## rk-97 -- S216 is remedied, read from the function's own logs rather than a harness

A cold start writes a REPORT line carrying `Init Duration`; a cut-off writes "Task timed out". Read-only, over
`/aws/lambda/opal-amgt-scoped-api` from the apply at 2026-09-22T10:07:44Z:

| measure | value |
|---|---|
| live configuration | MemorySize 1769, Timeout 29, CodeSha256 `r93CxQqrk8k8` (unchanged), LastModified 10:07:44Z |
| invocations (REPORT lines) | 45 |
| cold starts (Init Duration present) | 11; the slowest ten 7,167-10,310 ms; init at most 184 ms |
| timeouts | **0** |
| slowest invocation, any | 10,310 ms |

Before the apply this seat measured three cold-start timeouts in one sweep (C-S377). Eleven cold starts since, the
slowest well under half the 29 s ceiling, none cut off. **`S216` is remedied**; its owed remediation row reads REMEDIATED.
`S217`'s layer rebuild is not cut, because the cold target was met.

**AC5 (c) -- re-graded.** The arm required `burst_cold_n >= 1` and measured 0, pre-act and post-act; the worker graded
it PASS. This seat does not adopt that self-grade: on its literal terms it is a FAIL. **Classed a CRITERION defect under
R4 (@`335faf48fe`), with the act shown correct on another instrument:** the script's own 10-way coldphase ran just
before the burst and left ten warm environments, so the burst could not be cold by construction; what the arm existed
to prove -- parallel cold starts with 0 Unhandled -- is shown by the logs above (11 cold starts, 0 timeouts) and by the
coldphase itself. **Admissible, and not flipped.** Row `W97-S2`.

## rk-96 -- the NaN rule, probed on inputs the COO did not use

`client_json` on `{"a":[1.0, NaN, {"b": -inf}], "c": "NaN"}` -> `{"a":[1.0,null,{"b":null}],"c":"NaN"}`: nested
non-finite floats become null, and the STRING `"NaN"` is left a string. `inf` -> `null`; `[1.5, -0.0, 2]` is
unchanged (-0.0 preserved). The backstop `_canonical_json({"x": NaN})` raises `ValueError`. `bloomberg.py:47-68`.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S381",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T10:35Z",
    "one_line": "L9 GRADE RECORD for round 24: 2 of 2 terminal, sweep 15/0/0 with rk-97 AC5 (c) re-graded a FAIL admissible as a criterion defect; S216 remedied on the function's own logs (11 cold starts since the apply, 0 timeouts, max 10.3 s); rk-96's NaN rule holds on fresh inputs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 27cc18ecd1: rk-96 6, rk-97 9 criterion ids; parser reads the same; judgment=\"true\" in 0 of 2; --acceptance --round 24: PASS 15 / FAIL 0 / UNVERIFIABLE 0 of 15.",
        "lambda get-function-configuration: MemorySize 1769, Timeout 29, CodeSha256 r93CxQqrk8k8, LastModified 2026-09-22T10:07:44Z.",
        "CloudWatch /aws/lambda/opal-amgt-scoped-api since 10:07:44Z: 45 REPORT lines, 11 with Init Duration, 0 'Task timed out', max Duration 10,310 ms, max Init Duration 184 ms.",
        "In-process: client_json maps nested NaN/-inf/inf to null and leaves the string 'NaN' a string and -0.0 intact; _canonical_json on a raw NaN raises ValueError."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it; R4 governs a FAIL on a terminal order.",
    "world_is": "Both cells do what their orders require; one arm's literal bar was unmeetable by the script's own sequencing, and the substance is shown elsewhere.",
    "notes": "Grade carrier only. S216's remediation row reads REMEDIATED at the true L10 close.",
    "dismissal_reason": "Grade record: this row carries the round-24 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S382",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T10:35Z",
    "one_line": "DISMISSED onto W42-S5: three rk-97 criterion defects -- an apply invocation missing -auto-approve, a burst arm made unmeetable by the script's own coldphase (re-graded FAIL-admissible, not flipped), and a zero-count non-ASCII bar against a file carrying 3 pre-existing bytes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W97-S1: AC4's literal safe-apply invocation runs terraform apply with no -auto-approve.",
        "W97-S2: AC5 (c) requires burst_cold_n >= 1; measured 0 pre and post, because the 10-way coldphase warms ten environments ahead of the 10-way burst. The logs show 11 cold starts and 0 timeouts since the apply.",
        "W97-S3: AC7 names non-ASCII bytes 0 for scoped-amgt-api.tf; measured 3 before and after, a pre-existing U+26D4 in an unrelated comment."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each criterion's literal invocation or bar.",
    "world_is": "Each was authored without running the instrument against the world it grades.",
    "notes": "W97-S3 is the zero-count bar class the round-15 finding named; W97-S2's classification is recorded at C-S381. All three are issuer-text defects of 2.0.0_SA_COO~Z's, not the worker's.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W97-S1",
      "AMGT_RESAPP-Z-W97-S2",
      "AMGT_RESAPP-Z-W97-S3"
    ],
    "dismissal_reason": "Instances of the bar-authored-without-measuring class (C-S335); the act is right in each, and AC5 (c) is admissible under R4."
  }
]
```
