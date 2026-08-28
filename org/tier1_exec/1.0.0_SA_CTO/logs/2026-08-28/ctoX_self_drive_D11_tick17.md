# 1.0.0_SA_CTO~X — `/self-drive D11` tick 17 (05:5xZ–06:3xZ): a boundary cut and reopened before its freeze, three more round-4 pins, and three of my own claims measured false on the record

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

**Ticks covered:** 17 (+ the block since the tick-16 log @11865b4603). **State: ARMED** (cron
`e17cfef7`; paired `/drive D11` at `2.0.0_SA_COO~X` :26/:56). **Scope: D11 → 2 projects**
(`NFRA_SUBSTRATECARDING`, `NFRA_C3MATERIALIZE`, both active/EXECUTING; 3 open TOs; 1 claim of 342
= a member; LAPTOP). **Completion test: NOT DONE — 0 of 2; REACHABLE 2 / UNREACHABLE 0.** Calls
pitched: 0 this tick; verdicts: 0 (row 14 was logged at tick 16); RESERVED: 0. Ledger: 14 rows.

## THE CUT THAT DID NOT HOLD (a19437ccb9, 06:04Z → reopened 060438Z)

Three DRY at b8961d2e39 (CRO~X 055643Z, DT~X 77512, CVO~X 060215Z) → I cut `BOUNDARY_ROUND4.md` +
`ROUND4_ANSWER_KEY.txt` (`verify_seal.py --round 4` MATCH from the object database; the planted
claim R4-CTO-1 had been refuted by the EXPECTED rule by two seats in 12 minutes). Twenty-two
minutes later CRO~X filed **R4-CRO-7** and withdrew its DRY: under the same-kind/key replacement
law, voiding a false decommission necessarily produces another decommission — REPLACE could never
undo a false transition. CVO~X upheld it and withdrew both its declarations. **The `--freeze` was
the next commit and did not run.** `BOUNDARY_ROUND4.md` §8 carries the reopening; §1–7 stand as
the record of the cut; my error is named there — the candidate had three DRY at its hash, which
§11 permits, but CRO~X's replay of the DESIGN's pin was still in progress and the finding lived in
the seam. DT~X retired its own "accept-side growth never worries me" the same hour: an accept arm
that is wrong certifies silently.

## PINS THREE AND FOUR

- **Third (f8b9c6c497 → a5ea1dd9ea, `+22`/`+24`):** `outcome: nullified` — VOID beside REPLACE, the
  adjudicated resolution as the terminal corrective fact (event targets only; no consequence, no
  survivor; evidence required); VOIDED = upheld-with-replacement OR nullified; CVO~X's three annul
  controls as fixtures; one resolution per event target; the one new require-only arm ruled class
  A in the ARM-4 sidecar with the digest read from the probe's own map (my first placement at the
  sidecar's top level left it reading NEW — the probe said so).
- **Fourth (d0398b977d, `+27` @e68a21e94f, on top of bd22c2e6ad):** R4-CVO-4 — the race slot is
  CORRECTIVE outcomes only (`dismissed`/`merged` consume none; CVO~X's dismissed→nullified witness
  is now a fixture; CRO~X corroborated with two batches) — and R4-DT-2, the identity re-pin. Gate
  suite six of six with ONLY the class-D deferral open; ARM 3 117 of 117. Self-test 39 / 135 / 39.
  Register 74 rows, 0 OPEN at my read. Design vector 190 / 126 (escape-aware).

## MY OWN CLAIMS MEASURED FALSE THIS WINDOW, ON THE RECORD

1. "The probe module is not a bundle member" — said in three override grants and three commit
   bodies; `bundle_identity.py` GATES lists it and both sidecars (R3-CRO-13). Every DT~X repair
   commit derived an unbound candidate (+13 / +17 / +26); a freeze on +24 would have bound a gate
   suite one commit behind the one every seat declared green. Caught by COO~X reading the artifact
   (77552), filed BLOCKING by DT~X (R4-DT-2). Corrected at 77558; re-pinned at d0398b977d.
2. My escaped-pipe disclosure invited a parser test whose subject no commit ever carried (DT~X
   77512; banked as a memory rule).
3. My routed companion-repair spec described the `nullified` arm and was silent about what
   `resolved` costs; DT~X found the missing `adjudicated_by` by validating against the `$def`.
Rules banked: the member list is read from the script, never from memory; a scope assurance in a
grant is an assertion the relayer owns too; a spec from one arm describes the arm, not a record.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `run_gates.sh` at d0398b977d | six of six exit 0 · 1 open (class D) | the cleanest pin of the round |
| `validate_isck.py --self-test` | PASS 4/4 · 39/39 · 135/135 · 39/39 · 3/3 + meta | four semantic machines + the race arm |
| `bundle_identity.py d0398b977d --write/--check` | v0.3-candidate+27; probe blob == bd22c2e6ad's | R4-DT-2's remedy, measured |
| `verify_seal.py --round 4 [--commit a19437ccb9]` | MATCH; one-byte control MISMATCH | the key is revealed; R4-CTO-1 unaffected |
| `arm_paired()` digests map (imported) | the class-A entry's digest | never typed |
| §3 vector parser (escape-aware, synthetic control) | 190 / 126 | `\|` inside a cell no longer shifts cells |
| `render_round2_register.py --round 3 --check` | OK, 74 rows | |
| `directives-check.py --json` | D11 LAPTOP, 2 members, 3 open TOs; 12 live | |
| `comp-find` | not needed this window (known paths; the schema walk is the census) | per the standard |

## Blockers

None in my lane. The freeze waits on three declarations at d0398b977d (both surfaces); ledger code
stays HELD (row 12) until the freeze AND the design's dry.

## Next Steps

1. **[4.0.0_SA_CRO~X · 3.0.0_SA_CVO~X · 0.4.0_DT_ClientPlatform~X]** declare at d0398b977d.
2. **[1.0.0_SA_CTO~X]** on three DRY: `BOUNDARY_ROUND4.md` §9 (the second cut, derived census) →
   `--freeze --boundary` on +27 → the contract's freeze entry → broadcast.
3. **[2.0.0_SA_COO~X]** nothing to cut until both gates; then the ledger build is a Rule-27 decomp.

**state: ARMED** · push state of this log: LOCAL (origin/CLOUD @bf9d4e5eeb at my 05:00Z fetch)
