# /self-drive D2 & D3 — tick 86 (2026-08-30 09:44Z) — state: ARMED

Covers tick 86 and the inter-tick acts since the tick-85 log (`0d73876849`, ON origin @`416a116c8b` — own
is-ancestor read at 09:4xZ after the 09:36Z CLOSE, 87150). Cron `1c261f82` :07/:37 (fired 09:44Z on idle).
Paired `/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete; denominator 10 from the two member sets, deduplicated).
Open TOs **23** on the register (D2 19 + D3 4; the tick-85 count of 25 included the two cells since closed —
P2-1-AE at the grader and the C02-g-7 close). Ledger **19 / 0 unconsumed**. Delivery state 50 of 50 ackable,
48 READ at the pull + 2 SENT (87199, 87202) read and acked inside the tick → 50/50.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 5** (R1–R5, unchanged; R2 = the W1/W2 census ask at Andrew via MSTR on 6a99820c40).
No pitch.

## Verdicts since the tick-85 log (§3)

**0 on pitched calls.** Grades read: CVO 87175 **P2-1-AE PA-1..PA-4 PASS — CLOSED at the grader**; PA-4
DISCRIMINATED on the grader's own boto3 read (CodeSha256 yO0R5JDS…, LastModified 09:14:51Z, CodeSize 33,902,
`DRY_RUN=0`, `INSURANCE_EGRESS=1`, 5 env keys — AE~Y's figures on a second instrument). Agrees with the
gate's 87038 close. The (k) carrier (source-map `last_deployed_commit` stale after the deploy, the recorder
correctly not run under the live half-write candidate) stays with the seats that hold it.

## Driver's own acts (tick 85 → 86)

1. **INF-ONEWRITER (iv) → the APPLY WORD, in two steps.** (a) 87190–87193: the rows (87146) ACCEPTED as the
   ruled shape (0/1/0 on `module.inf_silver_chain.aws_lambda_function.this`; changed set = last_modified,
   s3_object_version, source_code_hash R1bXqTmu… → y7hEGWsh…; "environment"/"variables" 0 in the plan
   file; COO's issuer half signed 87178), **the word HELD** — the gate's own pre-registration (87136/87138)
   read four items and only the wiring fix was in hand (`eb0694d45b`, LOCAL, 68 added lines: cygpath,
   UNREADABLE → REFUSE); (a′) was NOT in that commit (token census `signature`/`sentinel` 0 of 68 added
   lines, positive control REFUS 3 / cygpath 1 / UNREADABLE 2), the four arms unprinted, the signature
   unquoted. (b) 87206–87209: **APPLY** on AE base's 87202 — `dbbbfb89b2` ((a′) ran-sentinel; the ORDERING
   read in the diff: `rm -f` at :55 BEFORE the gate, the REFUSE "the gate did not RUN" at :64, OK at :72,
   clear at :73; the checker writes `members=N pin=…` only after a completed clean run) LOCAL;
   `5aeb66224d` ON origin; the four arms printed WITH the positive control and restore (ARM 2: digest
   columns MATCH, only raw CR fires — the CVO's oracle exercised; ARM 4: the forced-SKIP stub → BUILD_RC=1);
   the clean signature quoted (4 of 4 index-equal, LF, ran-sentinel present); **the artifact sha
   UNCHANGED at y7hEGWsh… across all three builds** — the control work moved zero shipped bytes. Arm 4's
   re-run cost (an upload) accepted as stated. The word: (v) safe-apply on the saved plan, exact target,
   NEVER#6 ledger, unfiltered, 0/1/0 or STOP; (vi) CodeSha256 AND LastModified post-apply, Layers unchanged
   == the manifest's `layer_dependencies` by name, the deployed package downloaded with the member LIST
   printed and the four declared on both oracles, 0-diff re-plan; closes at APPLIED. Not verified by the
   gate, cited from AE base: the sentinel is not in the zip and not left in the package dir — re-read at (vi).
2. **DS~V's baseline @`bc42f4d35b` (LOCAL) read, per key** (87186): performance / tax_unrealized /
   tax_realized VALUE-EQUAL cell-for-cell between the stale package's write and the served write (24,597 /
   32,796 / 32,796 cells, sorted on every column, NaN==NaN); billing SCHEMA-DIFFERENT 13/17 cols — **the
   111-day drift reaches the served output in exactly 1 of 4 keys**. ETag withdrawn as an instrument in both
   directions (parquet is not byte-deterministic; equal size is not equal content). Arm A's discriminating
   value is therefore concentrated on billing; arm B's pin unchanged (jCldmxzm… vs uNBX1q8U…). No ask.
3. **org/mcp queue +1** (MSTR 87199): Codex seats' app-server sends are Sender-unverified with no broker
   Msg-ID (8 of 8 recent frames: CVO~X ×5, CRO~X ×2, CRO~Y ×1); source `server.py:764/:1072` — `_my_serial`
   is set only in `register_agent`, which the Codex surface never exposes; `:862` skips the poll loop while
   unset. Proposal (not an act): seed from `OPAL_AGENT_SERIAL` at startup with an env-seeded attestation
   flag; falsifier + negative control named. Sibling of the Codex ACK helper. OBSERVATION / INERT at CVO.

## In motion, not mine

AE base: (v)/(vi) → APPLIED; the CVO's grade of (iv)–(vi); DS~V's two-arm read after the next scheduled
inf-silver-chain fire; M-4 at 12:50Z (the a06 fix's first scheduled exercise); Andrew's word on W1/W2 via
MSTR; S1e at the next 04:35Z fire; the next integration window carries `eb0694d45b`, `dbbbfb89b2`,
`bc42f4d35b` and this log.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, project JSON status read (denominator 10), `to-check.py --all`, the ledger
count, `get_delivery_state` (50/50); `git show`/`--stat`, a token census over the two commits' added lines,
`merge-base --is-ancestor` against an ls-remote read (the gate's own instruments for the (a′) read and the
push states). No comp-find, no comp-state.

state: ARMED · next log at a verdict or tick 92 (floor)
