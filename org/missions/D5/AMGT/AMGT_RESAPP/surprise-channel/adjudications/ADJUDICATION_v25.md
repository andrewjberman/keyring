# AMGT_RESAPP round 23: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T09:4xZ at HEAD `a57bd0a068`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND23_L8_PACKET_20260922.md` @`a57bd0a068`; the two orders; the channel census;
live invokes of the print route and synthetic payloads to the gate hook, from this seat.

## Round state

**2 of 2 terminal** (`rk-94` print fix @`64e9cfb830`, `rk-95` GATE 5 parser @`fc2d043bf8`). Acceptance **PASS 15 /
FAIL 0 / UNVERIFIABLE 0 of 15 over 2 orders**; the order files carry 15 criterion ids (9 + 6); **judgment census 0 of 2.**

## rk-95 -- the gate, on this seat's own payloads

Four synthetic PreToolUse payloads piped to `.tools/hooks/never-rules-gate.sh` (text only; nothing executed):

| payload | verdict |
|---|---|
| `git -C "C:/Users/Opal Bloomberg/Desktop/ajb_workspace" push origin SITEZ` (quoted, space-containing path) | **deny** |
| `git push origin SITEZ` (relative form) | **deny** |
| `git -C "C:/tmp/wk amgt scratch" push origin wk-scratch-branch` | pass |
| `git status` | pass |

The negative controls hold and the quoted spaced path now resolves: `S209`'s remedy is in, and the fix narrows false
denials without opening a shared-branch push.

## rk-94 -- the sort-order 500 is gone; the print route's LATENCY now fails on a cold start

Live invokes of `/api/scoped/amgt/security/{key}/print` at CodeSha256 `r93CxQqrk8k8`, Lambda timeout 29 s:

| sweep | CAT | CSL | 6861 | BA | COST |
|---|---|---|---|---|---|
| sequential, ~09:3xZ | `FunctionError: Unhandled` at 30.1 s | Unhandled at 29.1 s | Unhandled at 29.1 s | 200, 23.9 s | 200, 13.2 s |
| CAT again, warm, twice | 200, 17.0 s | | | | |

**The drain's "/print returned 200 on all 5" held on a warm container and does not hold on a cold one.** The failures
cascade: an invocation cut off at the timeout tears down its execution environment, so the next call starts cold too --
3 of 5 validation-name prints failed in a row. The sort-order 500 `S215` named is gone (no 500 in either sweep);
what fails now is the separate latency defect `S216` the COO already filed. **`S216` is no longer an exposure: it
fires, on the path a manager's first open of the print view takes.**

**Grade of rk-94:** its criteria pass (200 on all five, measured at drain), and its act -- the normalised sort -- is
right; it is not charged with the latency. The instrument was blind to warmth: a warm-only read cannot distinguish a
route that works from one that works only after someone has already paid the cold start.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S376",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T09:45Z",
    "one_line": "L9 GRADE RECORD for round 23: 2 of 2 terminal, acceptance 15/0/0 of 15, no judgment criterion; the GATE 5 fix denies shared-branch pushes on quoted spaced paths; the print sort fix holds, and the route now fails on a cold start (S216).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at a57bd0a068: rk-94 9, rk-95 6 criterion ids; parser reads the same; judgment=\"true\" in 0 of 2; --acceptance --round 23: PASS 15 / FAIL 0 / UNVERIFIABLE 0 of 15.",
        "never-rules-gate.sh on synthetic payloads: quoted spaced-path push to SITEZ deny; relative push to SITEZ deny; scratch-branch push in a quoted spaced worktree pass; git status pass.",
        "Live print invokes at CodeSha256 r93CxQqrk8k8, timeout 29 s: CAT, CSL, 6861 Unhandled at 29-30 s in a sequential sweep; BA 200 at 23.9 s; COST 200 at 13.2 s; CAT warm 200 at 17.0 s twice. No 500 in either sweep."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "Both cells pass their criteria; the print route passes warm and times out cold.",
    "notes": "Grade carrier only. S209 and S215 (graduated at C-S373 and C-S371) are remedied by rk-95 and rk-94; their remediation rows read REMEDIATED at the true L10 close.",
    "dismissal_reason": "Grade record: this row carries the round-23 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S377",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T09:45Z",
    "one_line": "GRADUATED, and it FIRES: the print route runs ~17 s warm against a 29 s timeout, so a cold start times out -- and each timeout tears down the environment, so the next call is cold too. 3 of 5 validation-name prints failed in one sweep.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S216 (2.0.0_SA_COO~Z): 15-17 s warm against the 29 s Lambda timeout; invocations have hit 29,000 ms; the HTTP API's integration limit fixes the ceiling, so the lever is render time.",
        "This seat's sequential sweep: CAT, CSL, 6861 each FunctionError Unhandled at 29-30 s; CAT warm afterwards 200 at 17.0 s twice (REPORT Duration 16,944 and 16,976 ms, no Init Duration)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Every served route answers for the validation names.",
    "world_is": "The print route answers warm and times out cold, and the failure cascades.",
    "notes": "Remedy: round 24's rk-97 (memory 512 -> 1769, lever b), target cold under 20 s; S217's layer rebuild if it misses. Until it lands, a manager's first open of the print view will likely fail, and the headed look that closes rk-43 AC5 should not treat a print failure as a render defect of the tab.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S216"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S378",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T09:45Z",
    "one_line": "DISMISSED onto S216: the print-deps layer ships with compiled .pyc stripped, so every fresh environment recompiles matplotlib, numpy, pillow and fonttools on its first print -- a lever under S216's remedy, cut only if rk-97 misses.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S217 (2.0.0_SA_COO~Z): opal-amgt-print-deps:1 built with .pyc stripped, /opt read-only; per 1.0.0_SA_CTO~Z msg 24170, a later cell only if rk-97 misses the cold target."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Its own row.",
    "world_is": "One of the levers of S216's single remedy.",
    "notes": "Consistent with the cascade measured at C-S377: the cold cost is paid again after every timeout.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S217"
    ],
    "dismissal_reason": "A lever of S216's remedy (C-S377), conditional on rk-97."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S379",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T09:45Z",
    "one_line": "GRADUATED: the print route runs a pypdf text extraction on every print and discards the text -- dead work on the served path, removable on its own merits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S218 (2.0.0_SA_COO~Z): 0.22-0.40 s locally, roughly 10-15% of a print; per 1.0.0_SA_CTO~Z msg 24170 carried into chain G's first adapter-touching cell in any case."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The served path does only the work its answer needs.",
    "world_is": "It extracts text it never returns.",
    "notes": "Remedy, holder 1.0.0_SA_CTO~Z: remove the extraction in chain G's first adapter cell, after a whole-repo census proves no caller reads the text, under the pre-deploy closure check.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S218"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S380",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T09:45Z",
    "one_line": "DISMISSED: rk-95's criterion gap is closed -- the COO compared all 106 arms against the pinned hook (5 verdicts changed, all DENY to PASS, all S209 positives), and this seat's own payloads keep both negative controls denied.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Round-23 drain message (msg 24171): 106/0; exactly 5 verdicts changed, DENY to PASS, all S209 positives; negative controls still DENY.",
        "This seat's payloads (C-S376): shared-branch pushes denied in both the quoted spaced and the relative form."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W95-S1: the criterion did not prove the fix changed only the intended verdicts.",
    "world_is": "A full-population comparison and an independent payload test both show it did.",
    "notes": "An issuer-text defect of the COO's (the bar-from-memory class, C-S335), closed on evidence.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W95-S1"
    ],
    "dismissal_reason": "Closed by a full-population verdict diff and an independent negative control."
  }
]
```
