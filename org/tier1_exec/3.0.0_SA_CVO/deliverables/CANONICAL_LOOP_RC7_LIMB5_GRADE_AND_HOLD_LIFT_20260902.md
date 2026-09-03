# CVO VERDICT — ETFS_GUARDRAIL release ladder: RC7 GREEN, step-6 limb 5 GREEN, the RED/HOLD is LIFTED

**Seat:** `3.0.0_SA_CVO` base, holding the fabric-workflow lane `3.0.0_SA_CVO~A` held until 20:15Z (Andrew-direct
takeover @`91325bbf48`; lane stays merged @`840f841c83`). **Objects graded:** `1.0.0_SA_CTO` @`38f60078c4` (limb 5
pass 5 + RC7), LOCAL at grade time. **Instrument:** this seat's own — the gate's functions imported by path and fed
constructed cases; `jsonschema` Draft-7 on the header schema; the notifier's designed `selftest` on the live broker.
Not CTO's controls file, which is repetition of the author's method.
**archetype:** VALIDATE

---

## Inherited ladder state (CVO~A's own regrade files, unchanged by the handover)
RC1 GREEN (`7f5bc19cc6` 2nd pass) · RC2 GREEN · RC3 GREEN · RC4 GREEN (`d019922d68`) · RC5 GREEN final (`5dbca15a4a`,
on `03cf4d17ac`, re-confirmed by this seat at 0.07 s collect) · RC6 GREEN · **RC7 OPEN** · **step-6 limb 5 PARTIAL**
(`ce5c82750f`: fence grammar covers only exact column-0 three-char markers; `brief_ref` domain admits CR/LF path
chars and a `$` that matches before a final newline).

## Limb 5 pass 5 — GREEN on both of ~A's bars

**ROOT 2, `brief_ref` domain** — `org/standards/PRD_HEADER.schema.json` pattern now leads with
`(?![\s\S]*[\s\\])`, forbidding any whitespace or backslash at any position, with a newline-crossing dot-segment
lookahead. Exercised, six cases:
```
  OK  positive: the real Andrew-direct record path @f90ab3936b        accepted
  OK  NEG  CR inside the path                                          REFUSED
  OK  NEG  LF inside the path                                          REFUSED
  OK  NEG  trailing newline after the hash ($ before final \n)         REFUSED   <- ~A's exact hole
  OK  NEG  backslash path separator                                    REFUSED
  OK  NEG  dot-segment traversal                                       REFUSED
```
All three of ~A's named values refuse; the positive passes. **GREEN.**

**ROOT 1, fence grammar** — `_blank_fences` + `_top_section` shared by limbs 4 and 5 (`PRD_FENCE_RE`,
`_FENCE_OPEN_RE`). Exercised on the REAL draft with constructed decoys at ~A's boundaries:
```
  OK  my draft, one real heading                                       0 violations
  OK  a CLOSED 2-space-INDENTED ```text fence holding the heading, placed BEFORE the real one   0 violations
  OK  a ~~~ fence decoy before the real heading                        0 violations
  OK  an EOF-UNCLOSED fence after the whole document                   0 violations
```
Every decoy was blanked; the real heading was found; the FWD bidirectional check ran against the real section.
**A fifth case of mine is RETRACTED as a harness-scope error, stated so it is not mistaken for a gate defect:** I
fenced the ONLY heading and expected limb 5 to refuse; it returned 0 violations — because `_prd_conformance:52`
returns when no ENDPOINT section is found: *"limb 4 owns the missing-ENDPOINT complaint; do not double-report."*
The fence WAS blanked (correct); the complaint belongs to limb 4 by design. **GREEN.**

## RC7 — the R3 PRD-commit notifier: GREEN on its own control, run live
`.tools/prd-header-notify.py selftest` at this seat, on the live broker:
```
  OK  probe sent to self, id=92775
  OK  before ack: delivery_state=QUEUED  (a transport state -- NOT READ, NOT UNKNOWN)
  OK  is_read() before ack -> False
  OK  after ack: delivery_state=READ, is_read()=True
  selftest: 0 defect(s)
```
That is the RC7 property — *"R3/R4-c/R7 delivery tests distinguish emitted from recipient ACK"* — exercised, not
asserted. **Carried, not verified by this seat:** CTO's claim that the post-commit hook fired on this seat's two
PRD-draft commits (hook log 20:51:37Z / 20:52:52Z); I could not locate that log by name from the script's source
in the time given. The designed control passing on the live broker is the load-bearing evidence; the hook-fire
claim is CTO's attributed measurement. **GREEN, with that attribution stated.**

## VERDICT
**RC1–RC7 GREEN. Step-6 limb 5 GREEN. THE ETFS_GUARDRAIL RED/HOLD IS LIFTED** as of this record. Step 6 (task
orders against ETFS_GUARDRAIL) may proceed, subject to `to-pipeline-gate.py`'s five limbs as always and to
`2.0.0_SA_COO`'s sequencing. **Not lifted by this:** `NFRA_CLDGRPH`'s step 6, which Andrew separately sequenced
behind the project-tree prerequisite set (COO 92772, CALL 1) — a different project and his word.

**Two carriers move on this verdict and both are named:** ETFS_GUARDRAIL_PRD.md's own status line (CTO, as PRD
owner) and the register row's `blocking` (MSTR/COO). This file is the verdict; those are the carriers.

— 3.0.0_SA_CVO
