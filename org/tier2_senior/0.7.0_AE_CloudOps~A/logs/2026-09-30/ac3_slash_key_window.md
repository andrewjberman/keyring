# The slash-key window landed; AC3 failed on the issuer's instrument and I held instead of rolling back — 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

**Date:** 2026-09-30
**Task Order:** AMGT_RESAPP.TO-AMGT-ac-3 (round 53) — the slash-key window
**Status:** COMPLETE (issuer ruling msg 27250; 4 of 4 PASS under AMENDMENT 2; entry CLOSED, rollback not taken)

---

## Objective

Execute GO msg 27196: ONE act in TWO ORDERED legs under COO half `@bae8e66201` / CTO half
`@02eb2c5f9f` — leg (a) copy the 40 raw-slash objects to their encoded keys (raw KEPT), then leg (b)
redeploy `opal-amgt-scoped-api` at pin `cd70547173`. Leg (a) must precede leg (b): a build whose
readers use encoded keys must never serve before those keys exist.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (4 legs) / `close-leg` ×4 / `hold` / `hold --release` / `close` | PASS | The `hold` verb was the right instrument for a state I had not needed before: apply legs proven, one verify criterion unresolved. `close` refuses an unproven leg — that refusal is the tool working, not an obstacle. |
| safe-apply.sh | `-chdir=infra/aws/terraform/harvest apply C:/tmp/ac3.tfplan` | PASS | One apply against the exact graded plan, true exit 0 by redirect. |
| safe-commit.sh | ×4 (row, entry, rows, act, close) | PASS, with 3 correct refusals | An index.lock held by a concurrent seat; a "files remain staged" WARN; and one attempt whose stdout looked fine while HEAD did **not** carry the row. Every landing was confirmed by asking the repository. |
| surprise-row-gate.py | fired on each row commit | REFUSED then PASSED | Correctly rejected class `NON-BLOCKING`, which is not in the enum. I established the valid set **empirically** over the channel's own 686 rows (OBSERVATION 614, BLOCKING 71) rather than guessing. |
| proof-of-spec-check.py | on the instance, ×4 | rc=2 → rc=1 → rc=0 | Caught three of my defects: a **directory** listed as an artifact path (crashed it — and it says plainly that rc=2 is a tool failure, **not** an INVALID verdict), a non-hex `vintage_commit`, and `status=FAIL` without `status_reason`. |
| commit-gate.sh | on `capture_ac3.py` | PASS | 1 of 1. |
| comp-find --name | carried over from ab-6 this session | PASS | Denominators printed. |
| comp-iam / comp-schedule | issuer-side / NOT-APPLICABLE per preflight | SKIPPED | Declared in the instance's exclusions. |

**What worked:** the ledger's `hold` verb, and `proof-of-spec-check` — which refused three separate
shapes of a malformed instance before the CVO ever saw it.

**What failed:** two of my own instruments — see Postmortem. Nothing in the world.

**Gap found:** `build-and-upload-scoped-amgt.sh` corrupts `content-sha256` for ~1 build in 64
(row Z-S319, ruled INERT for served output by Z-S321; repair routed to round 54).

---

## Work Completed

### 1. Act-start gate, all four CTO clauses, before the entry was opened
Base `nKWCfQRQ` EQUAL; content diff at the pin `files 344, IDENTICAL 336, CHANGED 8, ADDED 0,
REMOVED 0` graded by parser in **both** directions; 40 of 40 raw sha256 equal, hashed **live**; 40 of
40 encoded destinations ABSENT.

### 2. Leg (a), then AC1, then leg (b) — never overlapping
COPIED 40, denominator 40, CopyObject only, raw kept. Each destination's absence re-asserted
immediately before **its own** write, not once at the gate. AC1 then read the world — 40/40 — and
only then did leg (b) begin. That ordering is limb 5 and it is provable from the ledger legs.

### 3. A defect caught between upload and apply (row Z-S319)
This build's base64 sha begins with `/`, and MSYS rewrote the `--metadata` argument, so the artifact
landed carrying `content-sha256: C:/Program Files/Git/QP4up…`. `cp` returned rc=0 with a correct
ContentLength — **no exit code or size check can see this**. `modules/yang-lambda` reads that metadata
*as* `source_code_hash`. Repaired server-side via boto3 `copy_object MetadataDirective=REPLACE`, then
verified the mangled string appears **0 times in the plan** — the control that the repair reached the
plane terraform actually reads, not merely the plane `head-object` reports.

### 4. AC3 failed, and I did not roll back
Four hypotheses tested; three rejected: an incomplete object list (a 7,111-object full-bucket sweep
found exactly 40 raw-slash keys, all listed), the `publishers_found_codes` key AC2 adds (0 occurrences
in those bodies), and `CopyObject`'s mtime reset (no 15:xx timestamp anywhere in the body). The fourth
was confirmed **by a control, not by argument**: both code versions run in process on the *same plane*
against the *same data* gave BP/_LN thesis 13,621 leaf fields each, **DIFFERING 3, all three only by
the `-SLASH-` path encoding**.

So the body reports its own read path and the act moves that path by design. I filed row Z-S318, put
the entry to HELD-SOVEREIGN-GATED, and asked. The issuer ruled the same way (row Z-S320, AMENDMENT 2,
msg 27250): rollback trigger not met, close COMPLETE. I re-ran all four on the served plane myself
before closing — 12 read-path strings rewritten, 6 of 6 equal — matching the issuer's figures exactly.

---

## The judgment call, stated plainly

Both halves name a failing criterion as the rollback trigger. I did not fire it. That deserves to be
recorded as a decision and not buried in a pass:

- The trigger exists to catch a **served regression**, and I had measured that there was none —
  13,618 of 13,621 fields identical, the three that moved being path strings.
- Firing it would have reverted AC2, which the CTO half names as the DSGN round-13 unblock, on the
  strength of an instrument I had just shown could not pass.
- So the conservative-**looking** act was the more destructive one.

What I did **not** do is decide the criterion was wrong. That is the issuer's call. I filed the row,
held the entry in a state that asserts neither success nor abandonment, named the rollback as still
available, and asked one question. The ruling agreed — but the correctness of the process does not
depend on that, and it would have been the same process had the ruling gone the other way.

---

## Postmortem — two instruments of mine were wrong

1. **My path normalisation invented a defect.** Rewriting `-SLASH-`→`/` across the served bodies
   matched 5 of 6 and failed on BP thesis — because it *also* rewrote `dossier_fields` citation paths
   that were **already** encoded before this act. BP thesis was the only body carrying 19 of them. I
   reported that as a possible sixth defect before the same-plane control settled it. The lesson: a
   normalisation that cannot distinguish "encoded by this act" from "encoded already" is not a
   control, it is a second hypothesis.
2. **I listed a directory as an artifact path** and crashed `proof-of-spec-check` (rc=2). The tool
   says explicitly that rc=2 is a tool failure and **not** an INVALID verdict — had I read rc as the
   verdict I would have recorded a clean bill from a checker that never ran.

---

## Environment notes

- `ack_messages` reported "broker call FAILED. Nothing acked" on a call that **had** written the ack
  (row Z-S317). `heartbeat`/`get_agent_status` succeeded throughout and the broker was LISTENING, so
  it was per-primitive, not an outage. My broker summary briefly carried the false claim "27196
  acked", written before the first result returned; corrected in the next heartbeat.
- The inbox watcher expired roughly every 30 minutes and was re-armed the same turn each time; one
  silent expiry was diagnosed (0 script rows, 0 unread, newest `read/` unchanged) before re-arming,
  to tell "no mail" from "deaf".
- Build residue (`/c/tmp/ac3-pin` 2.2 GB, its zip, two ~7 MB lib extracts) was **not** deleted: the
  `rm -rf` was declined, correctly — Andrew's earlier cleanup instruction named the ab-6 artifacts,
  not these, and I had over-extended it.

---

## Outcome

Both world legs landed and were verified. Entry CLOSED, all four legs proven, sentinel removed;
rollback explicitly not taken, on the issuer's ruling. Instance VALID (`proof-of-spec-check` rc=0,
violations=0, 4 of 4 PASS, surprises 3 of 3 resolving to channel rows). Commits `f4f9da33f7` (entry),
`3b1e4062c4` (Z-S317), `4237bf93d5` (Z-S318/Z-S319), `e1367c77ba` (the act), `e1e6603ee5` (the close).
Push state **LOCAL** — this seat commits and does not push shared branches. The `<status>` flip was
the issuer's and reads `complete`.
