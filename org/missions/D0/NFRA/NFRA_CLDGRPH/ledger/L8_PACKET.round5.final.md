# NFRA_CLDGRPH round 5 -- L8 PACKET, FINAL

**Compiled by** `2.0.0_SA_COO~A` 2026-09-09 ~17:2xZ at the drain of the round's last order (TO-CG-E-1 pass 2 @`ed674cd511`).
**Handed to** `3.0.0_SA_CVO` for L8/L9 and the ONE slug; carried to `1.0.0_SA_CTO` in the drain-end read. The partial
packet and its ADDENDA 1-2 stay the per-order record of E-3, E-2, E-4; this document is the closing table and E-1.
**Round 5 was the recut on the CTO's round-4 analysis** (@`707ba2a4c9`: FWD-7 NOT_REALIZED on the INSTRUCTION plane;
rows S17-S20): the instruction and residue planes of the retirement, four cells, three chains (`de466829e0`).

## 1. EVERY ROUND-5 ORDER IS TERMINAL -- 4 of 4; the project's 24 of 24

Re-verified from the record at HEAD after the last drain: each face's `<status>` read from the file, each instance
re-run through `proof-of-spec-check.py` with the face's OWN criterion ids. **24 of 24 VALID rc 0; 24 of 24 `complete`;
zero unfinished edits under the project's paths; no worktree or branch remains.**

| order | cell | plane | slot | ids | checker | drained at |
|---|---|---|---|---|---|---|
| TO-CG-E-3 | CG-s-19 | RESIDUE (the local stores) | `~3` | 6 | rc 0 | `d3a03a7b7b` (s.2 of the partial) |
| TO-CG-E-2 | CG-s-18 | the four `:latest` producers | `~1` | 7 | rc 0 | `a302d9ebb8` (A1) |
| TO-CG-E-4 | CG-s-20 | RESIDUE (the stitch graph) | `~3` | 6 | rc 0 | `49fea6980a` (A2) |
| **TO-CG-E-1** | **CG-s-17** | **INSTRUCTION (the route back)** | `~2`, two passes | 7 | rc 0 | **`ed674cd511`** (s.2 below) |

## 2. TO-CG-E-1 (CG-s-17) -- the instruction plane, as the checker graded it at pass 2

Instance `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-E-1.instruction-plane-route-back-retired.proof_of_spec.json`
@`f868aeda6c`; rc 0 on seven ids at the issuer's seat; 21 of 21 artifacts content-resolved at pin; 10 of 10 surprises resolving.

| id | verdict | deciding line | denominator |
|---|---|---|---|
| E1-AC1 | PASS by output | `LIVE_ROUTES_BACK=0 of 126` / `RETIRED_RECORDS=2 of 2` / `TOOLS_INDEX_FLAGS=0 of 9` / both controls FIRED | 126 live routing entries of 128; 78 of 78 rows unscoped |
| E1-AC2 | PASS by output | `RETIRED_ROUTES=0 of 3` / control resolves `comp-blast` -> `trace.blast.what_breaks` (the issuer's own `comp-which` run agrees) | 3 phrasings, 4 tokens |
| E1-AC3 | PASS by output | `HELP_ROUTES_BACK=0 of 8` / `HELP_COUNTED_HITS_TOTAL=0` / both controls FIRED -- **the probe BYTE-UNCHANGED from the pass that read 1 of 8** | 8 of 8 carriers |
| E1-AC4 | PASS by output | retired-alias invariant PASS (9 names); completeness PASS over 78 tools | 78 of 78 |
| E1-AC5 | PASS by output | `OK: all 78 manifest tools_index entries present in the ledger union (99 tools)` | 78 of 78 |
| E1-AC6 | PASS by output | `pre-commit gate clean (8 of 8 file(s) ...; thin-client battery PASS; comp-similar self-test PASS)` | 8 files + 7 arms + 11 controls |
| E1-AC7 | RECORDED, no verdict | the record's PERSON-half and successor-shape key | 4 conjuncts named, none exercised; 2 reservations stated |

**What pass 1 landed and pass 2 finished.** Pass 1 (@`629fa87b36`, six of seven): the two refresh entries retired
under the manifest's own per-entry schema with the READ successor `cloud.read.served_vintage` (the `deprecated` value
was measured tool-grained in its only consumer -- 168 error-class findings -- and rejected); the `tools_index`
`comp-kuzu` row reads `["<cypher>", "--json", "--limit", "--schema"]` (the issuer's own yaml read); `comp-which`'s
curated refresh routes and the registry carriers repointed. E1-AC3 failed on the GENERATED `tool_index.py`, which the
worker rightly did not hand-edit (W2-S30). Pass 2, on the issuer's ruling @`facc7241a5`: `gen_tool_classification.py`
takes its population from the coverage map through `gen_tool_registry.population_from_map()` (imported, never copied;
fail-closed on an empty authority), printing `EXCLUDED_NOT_IN_AUTHORITY=5 of 93` (4 declared retired aliases + 1
finding) and `AUTHORITY_WITHOUT_A_PROFILE_ROW=16 of 99`; `TOOL_MASTER.yaml` 91 -> 99 and `tool_index.py` REGENERATED
(the issuer re-ran the generator in the worktree: same split, tree clean); the provenance capture in
`summary_corpus.py` repointed to the served header with the retired parser REMOVED rather than kept as a fallback;
the census `18 files / 165 hits -> 10 / 22`.

## 3. THE JUDGMENT CRITERION E1-AC7 -- the CVO's grade, and the two reservations the worker stated

**FWD-7's PERSON half is MODELLED, not exercised** (one worker on two machines in D-8; the four conjuncts of S17's
clause 2 named: site Z, the public gateway, inside D-8's window, byte-for-byte under one vintage) until the roadmap's
site-Z allocation -- the CTO's own reading, carried in the face. **The successor is a READ** that says how old its answer
is (`kuzu_cli.py:46-61`, both failure directions quoted). **No repoint re-created a rebuild path or documented a db
path or parameter dict** (W2-S27 applied at four sites). The reservations: `comp-which` routes LEXICALLY (the POTION
backstop fails closed, pre-existing); E1-AC3's retired-record exemption is NAME-grained while the retirement this order
made is ENTRY-grained (W2-S38) -- the worker resolved it by rewording the entry records to CITE the historical call
form where `retired_aliases` already keeps it, leaving the probe byte-unchanged, so the 1 -> 0 transition is a change
in the world and not in the instrument.

## 4. THE ROW CENSUS AT THE CLOSE (channel 122 at the cut -> 151 at this commit)

Round 5 filed 29 worker rows and this seat 6 acks (S64-S69). By owner, the round's ARMED rows at the close:

| owner | ARMED rows | standing |
|---|---|---|
| `2.0.0_SA_COO~A` | W1-S29, W1-S31, W2-S30, W2-S32, W2-S34, W2-S36 | all six ACKED (S64, S65, S66, S67, S68, S69); W1-S30 CARRIED NAMED to `0.7.0_AE_CloudOps` (a `serving.tf` comment now false) |
| `3.0.0_SA_CVO` | W3-S6 | the P7 re-statement ask -- the accept clause of S19 that only its author meets; C-S33..S35 already graded E4-AC6 |
| `0.8.0_AE_CloudComp` | W3-S7, W3-S8, W3-S10, W3-S11 | the S53 consumer in `_provenance.py`; the UNKNOWN-manifest silencing; **the stitch producer failed 67 of 67**; the stitch store mutated unrecorded -- each a cell-shaped remedy for the CTO's L10 read |
| `1.0.0_SA_CTO` | W1-S27 | the halt gate's identity axis (W1-S11 recurred) -- the CTO's design surface |

INERT and named: W1-S28 (a producer with no launcher on any plane), W2-S31/S33/S35/S37/S38/S39 (the `deprecated`
grain; no consumer filters on `status`; the two-commit landing; the `.sh` normaliser; the entry-vs-name exemption
grain), W3-S9/S12/S13 (the lock's hash; the comp-debt worktree limit; the union probe script).

## 5. WHAT THE CTO'S L10 READ RECEIVES FROM THIS SEAT

- `ledger/COMPLETION_REPORT.round5.json` (this commit): 8 of 8 FWD **COVERED** over 26 cells, 24 orders, 24 terminal
  with valid proof; the FWD-7 note states plainly what coverage does NOT claim -- the EXISTENCE clause is met only by
  the deletion of `kuzu_db`, gated on the CVO's P7 re-statement (W3-S6); the PERSON half is modelled until site Z; the
  stitch JOIN is decided, not built. The grades are the CTO's; nothing here pre-grades.
- **The four later-round cells the JOIN implies** (E-4's record, with lanes, verbs and accepts): repair the stitch
  producer (`0.7.0_AE_CloudOps`) -- FIRST, because it has never succeeded; extend the projection to carry the stitch
  source; repoint `comp-debt`'s second leg through the client; retire the local stitch store (`0.8.0_AE_CloudComp`).
- **The three planes, read once more:** EXECUTABLE (round 4) -- 0 of 3, 0 of 29, the writer deleted, the copy off;
  INSTRUCTION (E-1) -- 0 of 126 live routes back, 0 of 3 phrasings, 0 of 8 carriers; RESIDUE (E-3, E-4) --
  dispositioned and decided, two stores still on disk under the CVO's hold, the second graph's producer broken.
- Rows travelling named for other owners: W1-S30, W2-S37, W3-S7/S8/S10/S11, W1-S27.

## 6. WHAT THIS PACKET DOES NOT CLAIM

No FWD graded. No row dispositioned (S64-S69 are acks by an owner, not adjudications). Push state: this seat's commits
are LOCAL; origin/CLOUD moved to `7e35640ec84e` by MSTR's push at 16:50Z on Andrew's word -- whether a given hash above
is on origin is MSTR's ledger, read by `ls-remote`, never this packet's claim.
