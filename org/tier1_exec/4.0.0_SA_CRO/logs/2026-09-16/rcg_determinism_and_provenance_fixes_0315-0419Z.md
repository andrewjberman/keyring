# 4.0.0_SA_CRO -- RCG: the marker made non-deterministic answers and the scorer stamped provenance nobody computed (0315-0419Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

## Window

2026-09-16 ~03:15Z (spawn) -> 04:19Z. First log of this session; no prior entry to delta from.
Seat spawned on an ANDREW-DIRECT relayed by `0.0.0_AB_MSTR` as msg 97284.

## Mandate

Andrew-direct ~03:1xZ 2026-09-16, VERBATIM and entire, relayed by `0.0.0_AB_MSTR`:

  "now i want you to go into the repo coherence graph work, look for it in the repo RCG. we
  had developed a system to clean up and maintain our local repo with this function, i want to
  see where that's at, because it's probably a good time to explore some cleaning while the
  fabric is quiet."

  "spawn 4.0.0_SA_CRO and have them work with this"

Routed here because `rcg/MANIFEST.yaml` names `4.0.0_SA_CRO` the SINGLE WRITER for `rcg/**`
and `org/projects/NFRA_REPOCOHERENCEGRAPH.json` names this seat owner. MSTR wrote zero bytes
into `rcg/` and handed measurement only, correctly.

## What happened

Startup per `org/XXX.md` (A.1 session serial, A.2 audit-archive 0 findings, A.3 PATH 104/104
resolve + forwarder EXERCISED, B.0 delivery ledger, B.1 to-check, C watcher, D hook, E comp
context). Delivery ledger surfaced two OFFER-EXHAUSTED rows from the ~23:3xZ managed wind-down
(97258, 97271); both opened, both acted, all three acked. Zero task orders held.

Then the substance: I re-derived MSTR's two defects on a DIFFERENT INSTRUMENT, fixed both,
ran the W1 chain end to end, and found two MORE in the stage MSTR had declined to run.

### D1/D2 -- rcg/bin/mark.py (commit af7ee8fc55)

**D2, the one that mattered.** `mark.py` decides which files are DELETION CANDIDATES and it
returned a different answer every run on identical input. MSTR measured it by comparing
PRINTED AGGREGATES; I re-derived by sha256 OF THE OUTPUT BYTES -- finer, and independent, so
this is corroboration and not repetition. MSTR's measurement reproduced exactly (its
PYTHONHASHSEED=0 `marked.jsonl` and my two seeded runs are the same `d2741c04` file).

CAUSE, located at file:line rather than inferred: `build_edges()` built `dotted` by iterating
`population`, a SET, and the import channel TRUNCATES it -- `dotted.get(m, [])[:4]`
(`rcg/bin/mark.py:222` @af7ee8fc55's parent). Set-iteration order therefore selected WHICH FOUR
candidates became edges. That is the mechanism behind the part of MSTR's report that read as
impossible: the IMPORT EDGE COUNT ITSELF moving on unchanged input. Secondary leak:
`build_root_set()`'s `for p in population` loops with `break`, where two matching `source_dir`s
give a different `why[p]` label, which lands in `marked.jsonl`'s `reach_root_type` column.

I did NOT take MSTR's suggested remedy (pin `PYTHONHASHSEED`). That fixes the symptom for
whoever remembers to type it; the leak is in the tool, so the sort belongs at the BUILD SITES
(`py_files`, `basename_index`, `dirs`, `sdirs`, four population loops). MSTR explicitly left
the remedy to this lane and the remedy moved.

EVIDENCE, one pinned vintage `20260916T024704Z_955e7767`, sha256 of `marked.jsonl`:

    NEGATIVE CONTROL -- UNPATCHED, so the test can actually fail:
      seed=1      efab7b6077dbf152...
      seed=999    7308039acb389b97...      DIFFER
    unseeded, unpatched, 3 runs: 099936bd / 4532fc53 / d2741c04 -- three distinct answers
    PATCHED:
      seed=1 / seed=999 / seed=random  ->  cb601ac2af3ee944... BYTE-IDENTICAL, no env var set
    On the fresh vintage 20260916T033918Z_af7ee8fc: two unseeded runs -> 402bb312 twice.

**D1.** `build_edges()` read `lexicon.json` behind a bare `if lexicon_path.exists():`. A run
before `lexicon.py` had ever run contributed ZERO tool-invocation edges, printed a clean
aggregate with NO warning, and still advertised that channel as LIVE in the boundary
declaration the tool prints every run. Now BLOCKED + rc=3 naming the remedy, with
`--no-lexicon` as an audited escape that DOWNGRADES the boundary declaration rather than
silencing it (prints the channel DISABLED and states `invoke_edges` reads 0 BY CONSTRUCTION,
not by absence of invocations). Positive control run both ways: absent -> rc=3 with the
BLOCKED line; escape -> rc=0, WARNING printed, invoke 0.

### D3/D4 -- rcg/bin/model.py (commit 74385b5fd5)

Found by RUNNING the chain, not by reading the file. Both are the same class: a value
asserting a claim nobody computed (CLAUDE.md "A VALUE MUST CARRY ITS CLAIM").

**D3.** `label_provenance` was the HARDCODED STRING `"seed-only (OBSERVED-derived; zero
RATIFIED yet)"` at `rcg/bin/model.py:118`. The SAME RUN printed `[model] ratified labels
folded: 17537` two lines below it. The docstring at `:8-10` promises the stamp "carries both";
it carried neither. Second half of the same hole: `labels_md5` hashed `seed_labels.jsonl` ONLY,
so two runs over DIFFERENT ratified ledgers stamped IDENTICALLY -- and `rcg/ledger/LABELS.jsonl`
is 17537 of the 19456 training labels.

**D4, the better catch, and it was involuntary.** The stamp read the LIVE head while scoring a
PINNED vintage. `0.0.0_AB_MSTR` committed D12 WS-3 (`6328a6fbb2`) between my scan and my score,
so the stamp read `head=6328a6fb` over a population measured at `af7ee8fc` -- every prediction
claiming to describe a commit it had never seen. WHEN THE TWO AGREE THE DEFECT IS INVISIBLE,
which is the usual case and why it survived nine model versions. It took a concurrent committer
to expose it, and I did not go looking for it.

FIX: both stamp fields COMPUTED from the run; `ratified_labels_md5` + `n_ratified_folded`
added; `head` is now the VINTAGE's with `run_head` and `head_drifted_from_run` beside it and a
printed WARNING naming the remedy; the whole stamp PERSISTED as `model_stamp.json` beside
`predictions.jsonl` (a stamp that only reached stdout could not be read back off the artifact).

`predictions.jsonl`'s `model_version` field KEEPS ITS SHAPE (head only) DELIBERATELY: the
frozen E-0004 calibration prior at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/E0004_FROZEN/predictions_prior_c4259ace.jsonl` keys
on that shape, and widening it would break the one comparison the freeze exists for. Census
run before deciding (`comp-find model_version --limit 40`, denominator 112172 hits / 165412
files) -- that frozen artifact is the consumer that constrained the choice.

DISCRIMINATING PAIR, ledger moved aside and restored:
    ledger PRESENT   ratified_labels_md5 849d98ad  n 17537  "MIXED: 17537 RATIFIED ..."
    ledger ABSENT    ratified_labels_md5 ABSENT    n 0      "seed-only ... zero RATIFIED"
`rcg/ledger/LABELS.jsonl` restored byte-identical (sha256 `9d3967ac968be314b2e4` both sides;
`git status --porcelain` clean on the path). An append-only ledger was never at risk but the
restore was verified rather than assumed.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 second half -- scored on OUTPUT, not rc; forwarder RAN |
| comp-find | `comp-find "model_version" --limit 40` | PASS | denominator 112172 hits / 165412 files scanned; found the E0004 frozen prior that constrained the D4 fix |
| comp-find | `comp-find "model_version" --band CODE` | FAIL | unknown band 'CODE'; valid set is HEAD/DEF/SURFACED/CONFIG/TEST/DOC/COLD |
| sequence-check | `.tools/sequence-check.py --project NFRA_REPOCOHERENCEGRAPH` | PASS | UNPLACED -- not sequenced, its own directive's rules govern |
| to-check | `.tools/to-check.py --all --assignee 4.0.0_SA_CRO` | PASS | 0 active TOs, scanned 2801 |
| owned-paths-validate | `printf 'rcg/bin/mark.py' \| ... --check-agent <serial>` | PASS | BOTH arms: admits 4.0.0_SA_CRO rc=0; REFUSES 0.1.0_DS_MarketIntelligence by name |
| manifest_check | `rcg/bin/manifest_check.py` | PASS | CLEAN; 20 tracked vs 21 allowed; append-only 6; 4904 paths / 24 prefixes, 0 violations |
| audit-archive-invoker | `.tools/audit-archive-invoker.py` | PASS | rc=0, 0 findings, snapshot not-due |
| safe-commit | x2, `-F <file>` non-shell-written | PASS | risk-reflex CLEAN, naming-gate PASS, both gates' denominators printed |

**What worked.** `comp-find`'s printed denominator is what made the D4 decision safe -- the
frozen E-0004 prior would not have surfaced from reading `model.py` alone, and it is the single
consumer that forbade widening the field. The owned-paths NEGATIVE arm is the check that makes
the positive arm mean anything; an empty stdin admits every serial, so naming a foreign serial
is the only honest form.

**What failed.** `comp-find --band CODE` -- I assumed a band name instead of reading the enum.
One wasted call, corrected by the tool's own error text.

**Gap found.** The comp-rail's CENSUS-PIPE denial fires on `comp-find ... | head` and ABORTS
THE WHOLE BASH CALL. My call was a single segment so nothing was silently lost, but the
CLAUDE.md Rule 21 warning about later segments becoming silent no-ops is live and I hit the
denial path that produces it.

## MCP traffic

4 messages total. Inbound 3, all acked from their own `Msg-ID` lines: 97284 (the SPAWN-DIRECT
state handoff), 97258 (MSTR closing my predecessor's 97244 daily-sprint handoff -- L5 held on
the 2026-09-16 20:10Z scheduled fire, an external gate, no act owed here), 97271 (the ~23:3xZ
managed wind-down, SUPERSEDED by this spawn). Outbound 1: RAVC close of 97284 to
`0.0.0_AB_MSTR` with all four defects and their evidence.

A `heartbeat()` re-emitted 97284 after it was already acked and acted on; no second action
taken. Broker re-surface, not new mail.

## Files Modified

See commit messages: `af7ee8fc55`, `74385b5fd5`. Both carry per-defect cause, fix, and the
control arms.

| File | Note |
|---|---|
| `rcg/bin/mark.py` | +43/-13. Sorts at build sites; lexicon fail-closed + `--no-lexicon`; boundary gains a `determinism` row |
| `rcg/bin/model.py` | +43/-4. Stamp computed and persisted; `head` re-grained to the vintage |

## Blockers

None at this seat. The stop is TWO SOVEREIGN CALLS at Andrew, not a dependency:

1. **Reopen `NFRA_REPOCOHERENCEGRAPH`?** Closed 2026-08-25 in the SPRING CLEAN for a purely
   structural reason (not attached to `org/missions/DIRECTIVES.yaml`). Its own record says "NOT
   a work verdict", names no successor, and states recovery is explicit in his ruling ("we can
   reinvent a project"). Zero open task orders at close. Reopening is his, not this seat's.
2. **The 267 UNCHARTERED files.** `scan.py` prints "UNCHARTERED 267 (amend charters.yaml)".
   Until chartered they sit OUTSIDE the scoreable denominator, and an unscoreable file reads
   identical to a clean one. `rcg/charters.yaml` is in this lane's allowlist; the amendment is
   one act once he says which way.

Not a blocker, stated so a reader does not re-derive it: D12 WS-3 is NOT this seat's. Owner
`1.0.0_SA_CTO~Z`. `0.0.0_AB_MSTR` built it this window as `6328a6fbb2`.

## Current State

**The RCG pipeline is WHOLE AND REPRODUCIBLE at HEAD, and it was not before tonight.**

FILES (all under `C:\Users\AndrewBerman\Desktop\ajb_workspace\`):
- `rcg/bin/` -- `scan.py`, `lexicon.py`, `mark.py`, `features.py`, `model.py`, `packet.py`,
  `manifest_check.py` all PRESENT and all RUN. `post_review.py` is ABSENT and that is NOT a
  regression: `rcg/MANIFEST.yaml` lists it under "P2 loop (planned)", an allowlist CEILING
  entry never built.
- `rcg/scans/20260916T033918Z_af7ee8fc/` (DIR, gitignored `local_only`) -- the current vintage:
  `census.json`, `inventory.jsonl`, `lexicon.json`, `edges.jsonl`, `marked.jsonl`,
  `features.jsonl`, `seed_labels.jsonl`, `predictions.jsonl`, `model_stamp.json`, `packet.md`.
- `rcg/ledger/` -- LABELS 26659 rows, BATCHES 48, DISPOSITIONS 22, MODEL_EVAL 9;
  `rcg/rulings/` -- RULINGS 32, VERDICTS 32. All intact, none appended to this window.
- `rcg/models/` (DIR, gitignored) -- nine `.cbm` plus this window's `rcg_v0_af7ee8fc.cbm`.

W1 stages A-E, GREEN end to end on vintage `20260916T033918Z_af7ee8fc`:

    scan      36404 tracked files = protected 10947 + scoreable 25457; UNCHARTERED 267
    lexicon   968 identifiers (tools 264 LIVE / 19 RETIRED; project codes 323 RETIRED / 46 LIVE)
    mark      MARKED 10953 / 36404 (30.1%); UNMARKED-SCOREABLE 16263; edges import 34690 +
              path 115854 + invoke 4585
    features  25457 scoreable rows, 6483 seeds (KEEP 6002 / ARCHIVE_CANDIDATE 481)
    model     scored 25457, uncertain band 913, holdout ARCHIVE precision 0.976 recall 0.991
              -- OVERSTATES by the tool's own declared seed-circularity, not a real number
    packet    S1 disagreements 1666 | S2 band 889 files / 103 cohorts | S3 archive 41 files /
              30 cohorts | PLANTED CONTROLS 4/4 PASS -> packet.md written

**16263 is an UPPER BOUND on candidates and never a delete list.** `mark.py`'s own declared
`failure_direction` is UNDER-MARKING (false cruft), the sweep PROPOSES, and Andrew ratifies at
cohort grain. MSTR's earlier "16258 candidates" was correctly retracted by its author as a
SAMPLE; 16263 is a measurement because the tool is now byte-stable across seeds.

THE CASE FOR CLEANING, this vintage against the last real scan (2026-08-04):
tracked 22659 -> 36404 (+61%); `org/` 11947 -> 22913 (nearly doubled); dead markers 141 -> 477.

NOT DONE, deliberately: no ledger append, no disposition, no sweep, no deletion, no project
reopen, no `charters.yaml` amendment. Nothing was deleted from this repo this window.

PUSH STATE: `af7ee8fc55` and `74385b5fd5` are LOCAL on CLOUD. `origin/CLOUD` read at
`6328a6fbb2` by `git ls-remote` at ~04:08Z -- this seat is two commits ahead of the remote and
pushes stay with Andrew through `0.0.0_AB_MSTR`. Claim is perishable; re-measure at send time.

## Next Steps

1. [Andrew] The two sovereign calls above -- reopen the project, and which way on the 267
   uncharted files.
2. [4.0.0_SA_CRO] On a reopen: amend `rcg/charters.yaml` for the 267, re-scan, and walk the
   packet cohort by cohort. On a no: the fixes stand on their own merit and the seat parks.
3. [0.0.0_AB_MSTR] Holds the push. RAVC close of 97284 delivered ~04:08Z as
   `20260916T040851Z_4.0.0_SA_CRO_RAVC_close_97284__both_defects_FIXED_and.md`.
4. [4.0.0_SA_CRO] Ledger record for the four defects if the project reopens -- `MODEL_EVAL` is
   the wrong carrier (they are tool defects, not model evaluations) and no ledger here fits
   them, which is itself worth raising rather than forcing a row.
