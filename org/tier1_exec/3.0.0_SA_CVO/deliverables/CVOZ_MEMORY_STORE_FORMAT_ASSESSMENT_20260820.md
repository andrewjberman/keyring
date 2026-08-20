# CVO~Z assessment -- memory-store FORMAT (Andrew-direct ~20:0xZ, routed via CTO~Z 2776)
**Date:** 2026-08-20 ~2020Z | **Assessor:** 3.0.0_SA_CVO~Z (named by his word: "their logging
should be highly structured by nature, id recommend a json aproach but maybe yaml works, i
would have CVO~Z assess how to best handle this")
**Assessed:** the three store surfaces (threads/INDEX.md / THREAD.md / daily files) x
{MD-as-is, JSONL, YAML} x {recall speed, append safety, machine use, human audit}.
**Method:** claims exercised, not asserted -- four measured exhibits (E1-E4 below), run
2026-08-20 ~2015Z, python 3.11 / pyyaml 6.0.3 on this box. Rulings in 2776 (BG commits
nothing; no new owned-paths lane) are FENCED -- nothing here touches or needs them.

## VERDICT

**CTO~Z's prior GRADES OUT: PASS with amendments.** Daily entry files move to **JSONL, one
object per exchange**; **INDEX.md and THREAD.md stay MD** with their existing one-line row
grammars NAMED as rigid formats in the contract. **YAML is REJECTED for every surface** --
dominated, not merely disfavored (E3). Amendments A1-A5 below are conditions on the PASS.

## The deciding argument (it is the store's own recent history)

MD's machine path is regex-over-prose-templates: template drift produces a CLEAN EMPTY --
the silent-recall class BG measured on 08-20 (an en dash returned two clean-empty greps on a
rule present the whole time). **JSONL inverts the failure mode: a malformed line fails LOUD
and NAMED at parse.** A store whose whole recent incident history is silent-empty retrieval
should choose the format whose failures announce themselves.

## Measured exhibits

- **E1 (ASCII synergy):** the en-dash specimen in MD renders perfectly and greps as nothing;
  the same content JSON-encoded (ensure_ascii) carries a VISIBLE `\u2013` in the byte
  stream. Neither form matches a naive "2-3" grep -- but only the JSONL form shows a reader
  and a grep THAT an escape is there. The format converts the silent defect class to a loud
  one; the ASCII-only contract line binds the writer regardless (A2).
- **E2 (JSONL residual hazard, measured):** a quoted phrase inside content is stored escaped
  (`\"hello\"`); a naive quoted-phrase grep MISSES it. Discipline line required: token-grep
  or parse -- never quoted-phrase grep over JSON content (A4).
- **E3 (append blast radius, measured):** JSONL with one torn line: 3 of 4 entries
  recovered, failure NAMED at line 4 -- LOCAL. YAML with a one-space indent slip on append:
  whole-document ScannerError -- TOTAL (every prior entry unreadable until repaired). YAML's
  silent-coercion class also confirmed: `confirmed: no` parses CLEAN to boolean False (the
  norway problem). *Honest bound: two other coercion specimens (`08:30`, `019`) stayed
  strings in pyyaml 6.0.3 -- the class is real but narrower than folklore; the TOTAL blast
  radius alone disqualifies YAML for an append-per-exchange record.*
- **E4 (recall speed, measured):** 200 entries (5x a heavy real day, 40.8KB) parse in
  0.40 ms. The <=3-read budget is untouched; parse cost is noise against the S3 clocks.

## Per-surface reasoning (the split is load-bearing, not aesthetic)

| Surface | Format | Why |
|---|---|---|
| daily files | **JSONL** (new files only) | append-per-exchange record; machine use is the growth axis (recall denominator, outcome enum, recurrence mining, M2/M4 measurement); local blast radius; loud failures; Andrew's own lean ("json aproach") |
| INDEX.md | **MD, unchanged** | the map rows are ALREADY a rigid greppable grammar (`id -> dir`, exactly-once verified by count -- M6's own instrument); the STANDING blocks carry sovereign verbatims, and **verbatim-anchoring is byte-anchoring: JSON escaping would ALTER the bytes of a quoted ruling** (a `"` becomes `\"`) and break the phrasing-IS-the-ruling grep. Keeping standing blocks MD is what keeps rulings byte-greppable |
| THREAD.md | **MD, unchanged** | maintained-not-appended (folding, ~40 lines) -- the append-safety axis does not apply; standing context is prose by nature; the Ticket index rows are already rigid one-line pointers |

## Amendments (conditions on the PASS)

- **A1 -- MIGRATION IS A DATE BOUNDARY, NOT A REWRITE.** Daily files are immutable after
  their day closes by the store's own law -- existing MD dailies stay as records forever;
  the first daily file created after the contract touch is `<date>.jsonl`. NOTHING is
  migrated, which also means the format change costs BG zero acts and trivially honors the
  no-git ruling. (The 2776 "BG migrates its own files" clause is thereby VACATED BY
  VERDICT-SHAPE, not contradicted: there is nothing to migrate.)
- **A2 -- the writer emits ASCII-escaped JSON** (ensure_ascii semantics): non-ASCII content
  becomes a visible `\uXXXX`, never a silent grep-miss (E1). The contract's ASCII-only line
  binds the composed TEXT; the encoder is the backstop, not the license.
- **A3 -- the field schema is the owner's authoring act WITH its Rule-24 filing** (not
  minted here). My assessment binds only the INVARIANTS the key set must carry to preserve
  the contract it replaces: the verbatim ask; the RECALLED denominator (reads list);
  the outcome enum exactly as ruled (the five incl. FAILED as amended; WITHDRAWN when its
  filing lands); vintage + catalog row; told-what on FAILED (the "where the channel
  permits" clause); the residual open field; the off-record flag. Plus ONE STABLE KEY ORDER
  (human audit + diff stability -- Andrew reads these raw).
- **A4 -- grep discipline line in the contract:** token-grep or parse over JSONL content;
  never quoted-phrase grep (E2). The <=3-read budget and no-scan law unchanged (E4).
- **A5 -- the INDEX.md map row and Ticket index row grammars get NAMED as rigid one-line
  formats in the contract** -- they are already de-facto structured; naming them is what
  prevents drift without a format change.

## Not reopened, per the 2776 rulings
BG commits nothing (the no-git design stands); no new owned-paths lane. Nothing in this
verdict requires either.

## What you should have asked but did not
1. **Which clock is authoritative for latency once entries carry `ts` natively?** The PRD
   says the S3 clocks measure the recall budget; a JSONL `ts` field creates a second,
  cheaper-looking oracle one grep away. Name it in the contract: entry `ts` is RECORD
  metadata; the S3 clocks remain the latency instrument -- or the first latency claim
  quoted from entry timestamps will be a plane error wearing a denominator.
2. **Structured dailies make mining nearly free -- and the cheapest next deliverable will
   be a dashboard/miner over them.** The build ladder and the moratorium already answer
   this (consumption lives IN the serve loop; no new instrument without Andrew's word) --
   stated here so the temptation arrives pre-adjudicated.

-- 3.0.0_SA_CVO
