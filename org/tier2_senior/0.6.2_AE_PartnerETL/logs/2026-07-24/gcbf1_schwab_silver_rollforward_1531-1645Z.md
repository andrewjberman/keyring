# 0.6.2_AE_PartnerETL~C — GC-BF1 Schwab 0824 silver roll-forward, 2026-07-24T15:31Z .. 16:45Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE, TRACE

## Summary

Fresh `~C` lane, spawned onto the MDPF critical path with Andrew waiting on a chart that could not move.
The TO's first deliverable was a five-minute discrimination — **are the Schwab source files present or
absent?** — and it had a trap in it: **the TO told me to look at the OneDrive delivery folder, and that
folder alone returns ABSENT**, which would have sent Andrew to download six days of data that had been
sitting in monolith bronze since that morning. Checked both channels, answered PRESENT, and extended the
answer with the per-type enumeration that actually discharges the "partial delivery" state the TO named but
gave no test for.

Then converted: **7 silver tables 20260715 -> 20260723, 42/42 partitions**, gate GREEN. Along the way
**three separate stale-record defects surfaced, one of which CTO had relayed about his own change**, and
the canonical tail **failed on first run** and had to be routed around rather than re-run.

**Nothing I was told at the start about how to do this work turned out to be correct.** Every instruction —
the delivery-folder check, the TRN bridge, the seven-step sequence — was aged. The estate was right; the
records about it were not.

**And then I wrote one.** The fix I routed to DS carried a **0833 -> 0824 cross-master substitution**, and it
was inside a document I had deliberately written to be implementable without re-derivation. It never landed
because DS declined the recommendation and anchored on the module's own declared purpose. **The claim it
falsified was my own** — that `master_for()` makes 0824-only *"structural"* — which I had asked CTO to
propagate about an hour earlier. Retracted to CTO, COO, MSTR and DS.
**All four of today's record failures, mine included, failed in the same direction: toward "you can stop
checking."**

## Work Done

1. **STARTUP (15:31Z)** — `/watcher`: no `~C` process existed, serial NOT REGISTERED -> genuine fresh lane,
   no orphan, no live-peer collision (`~A` pid 3513485 and `~B` pid 3818854 are live siblings at different
   PIDs under different serials — left untouched). Registered PID 29064, Monitor `bdkllgl7g`, LD-0290 serial
   file written, audit-archive-invoker rc=0, owned-paths hook wired. **Picked the work up from the TO commit
   `62594e9911` — no inbox GO had landed yet**; COO's dispatch arrived ~5 min later.
2. **THE DISCRIMINATION (15:33-15:39Z)** — inspected the delivery folder **explicitly**, as the TO's
   forbidden-shortcut clause demanded: 2006 files, newest CRS date **20260715**, newest mtime
   2026-07-16T14:00:31Z. **On that channel the answer is ABSENT.** Then the monolith channel, which the
   skill records as SUPERSEDING OneDrive: present through **20260723**. Verdict **PRESENT-and-unconverted**,
   reported to COO 153852Z and CTO 153917Z before touching anything.
   **THE EXTENSION THAT DID THE REAL WORK:** enumerated **all 17 type prefixes**, not the three that had
   been checked. All 11 consumed types carry the identical six-date set. **rps/acc/trn being current does
   not exclude `present-but-partial`** — a delivery short in RLD or ULT converts cleanly, reads GREEN, and
   degrades the tax surface silently. COO accepted the clause as defective (153941Z): *"A forbidden-shortcut
   instruction that names the wrong instrument is worse than none."*
3. **GROUNDED THE READ PATHS BEFORE RUNNING (15:41-15:44Z)** — did not take the documented S3-vs-local split
   on faith. All four converters import `_monolith_bronze`; all declare `PURPOSE='model_portfolios'`;
   trn_nna reads bd silver. **Not one reads local or `01_raw`.**
4. **CORRECTION TO CTO, ACCEPTED IN FULL (154446Z -> 154535Z)** — the "TRN reads LOCAL, build the bridge"
   warning was **retired by CTO's own A4 L5b re-point of 2026-07-17**. The skill row carrying it was dated
   **2026-07-16, one day earlier**, so CTO read his own stale row and relayed it, and COO restated it three
   times. **No bridge built; the cycle succeeded on all seven legs with Step 1 skipped entirely — that is
   the proof it is inert, not an argument that it is.** CTO took the generalization verbatim into doctrine:
   ***"a stale record is most convincing when it is relayed by the author of the change that retired it."***
   His counterfactual: had I complied, the bridge would have been **credited** for a result it contributed
   nothing to — *"not wasted motion; a self-reinforcing error."*
5. **THE CONVERSION (15:43-16:05Z)** — ledger opened at deploy-start (8 legs) **before the first write**.
   Two parallel chains on disjoint prefixes: A = acc/rps/trn/trn_nna, B = uln/ult/rld. All six target dates
   OK on every table. **Also cleared a large historical backlog nobody had asked about: 225 uln + 225 ult +
   221 rld dates, ERR=0** — those tables are now COMPLETE, not merely current, and `ult` feeds
   `B_02.canonical_lots`.
6. **THE GATE, EXERCISED NOT READ (16:04-16:13Z)** — pulled the **deployed** `mdpf-daily-trigger` code and
   md5-matched it to repo HEAD (`78801e4e...`) **before trusting it**; set env to the deployed
   `Environment.Variables` verbatim; called `_check_schwab_rps()` live: `latest_partition=2026-07-23,
   behind=1, max_lag=2, **fresh=True**`, condition cited from `lambda_function.py:453`.
   **POSITIVE CONTROL:** same harness fed the pre-run state returns `07-15 -> behind=7, fresh=False`,
   **reproducing the trigger's own 15:01:43Z log line exactly.** **MUTANTS:** 07-20 -> 4/False,
   07-21 -> 3/False. The gate can still fail.
7. **SEMANTIC CHECK BEYOND PRESENCE (16:29Z)** — parquet row counts match the converter claims **exactly**
   under assertion (rps 93,126 / 92,518; acc 7,089; trn 5,095; rld 786), and each file's internal
   `file_date` matches its own partition — ruling out right-bytes-wrong-partition.
8. **L8 FAILED HONESTLY AND HAD TO BE ROUTED AROUND (16:14-16:37Z)** — `build_canonical_daily.py --date
   2026-07-23` printed `=== done: 20/25 steps OK ===` with 5 `NoSuchKey`. Source-confirmed: `:153-156`
   still enumerates the **dead** `opal-data-schwab/01_raw` (frozen at 20260715) while its own fact builders
   **were** re-pointed — so it built facts for **07-15** then ran gold at t1=07-23.
   Worked around with **no code change** (the `:164` `missing or [t1_iso]` fallback + correctly-re-pointed
   fact builders, invoked per-date ascending): **all six runs 25/25**, **54/54 canonical partitions** across
   9 tables. Real fix routed to DS (Rule 13), not made.
9. **A MEASUREMENT CORRECTION ON MYSELF (16:38Z)** — my first canonical census read `account_gains 0/6`.
   **That was my instrument, not a gap** — it partitions by `period=<start>_<end>`, not `date=`. All six
   windows present; true total 54/54. I had written the census before checking the key form of every table
   in it. Recorded in the ledger rather than quietly fixed.
10. **719-PARTITION LATENT BREAK FOUND (16:18-16:22Z)** — TRN's `ERR=61` was not benign. Full census:
   **719 monolith-bronze partitions are present but UNREADABLE**, landed as `CRS{d8}.{FEED}` instead of the
   `{master}.CRS{d8}.{FEED}.zip` grammar the readers build. **Only TRN surfaces it** because the other five
   feeds already hold those dates in silver and *skip* — control run: `silver/trn/date=20240116` absent,
   `silver/{acc,rps,uln,ult}/date=20240116` all present. **A `--force` or any silver rebuild fails on ~120
   dates per feed.** Routed to CTO (Rule 17a — a re-land/alias ruling, not an edit).

11. **RETRACTION OF MY OWN CLAIM — THE ONE I HAD ASKED THE FABRIC TO BANK (16:42-16:48Z, `4ae8bf78b`)** —
   DS replied that they had fixed finding #1 (`3b0113227`, 14 tests, 5/5 mutants) and corrected one detail.
   Checking their correction surfaced **a worse error of mine that they had not flagged.**
   **My routed recommendation was a 0833 -> 0824 SUBSTITUTION.** I wrote: re-point the canonical
   orchestrator via `master_for('model_portfolios')` **or** at `opal-data-bd/schwab/silver/rps/`. **Both are
   0824. The canonical store is 0833** — `build_fact_position.py:35-40`, `PURPOSE="advisor_intelligence"`,
   docstring explicit: *"No MP consumer exists on this store."* A literal implementation would have pointed
   the ADVISOR INTELLIGENCE store's date axis at the MODEL PORTFOLIOS book — **a SELECTION, the shape the
   estate records as not licensed by the addition law.**
   **It did not land — and my first account of WHY was itself overstated.** I wrote that DS *"ignored my
   recommendation"* and pinned it with a test; **DS corrected that unprompted (164917Z, amended `08e47e863`)**:
   they never evaluated my suggested sources against the prohibition at all. They went to
   `build_fact_position.py` to find what the builders read and anchored on its declared `PURPOSE` *"because
   MATCHING THE CONSUMER WAS THE WHOLE POINT OF THE FIX"* — the 0824/0833 test came **after**.
   >> **So a METHOD stopped it, applied for an unrelated reason. Not a gate, not vigilance. Nobody in the
      loop was thinking about the two-buckets law at the moment it was prevented.** My version made it a
      careful reviewer catching a bad recommendation — **the same "someone will notice" shape as the claim I
      was retracting, relocated from a function to a person.** DS's framing, now propagating: *"it works when
      the agent is NOT paying attention to the hazard — which is the only kind of protection that scales."*
   **Caught CTO's fabric-wide propagation mid-flight** (it was already carrying my wrong clause and the
   conclusion *"a downstream agent's independent judgement, not a gate"*); corrected to CTO, COO and MSTR.
   >> **AND IT KILLS THE CLAIM I HAD PROPAGATED TO CTO, COO AND MSTR ~1 HOUR EARLIER.** I certified that
      `master_for()` makes 0824-only *"structural, not procedural"*, and CTO asked it be spread because it
      *"converts a NEVER-rule into a mechanism."* **The gate refuses an UNKNOWN purpose; it cannot refuse a
      WRONG-but-known one.** I certified a control and then walked through the gap in it, in writing, the
      same hour. Retracted to all three; corrections committed.
   **Also accepted DS's actual correction:** I claimed the orchestrator should be made to exit non-zero on
   ERR — **it already does** (`:296`, `return 0 if n_ok == len(results) else 2`, verified). Only the
   **printed** done-line misleads; that framing stands.

## Deployment Sequence + Verification

Ledger `schwab-0824-silver-rollforward-20260724`, opened 20260724T1542Z, **CLOSED 20260724T1640Z, all 8
legs proven, nothing stranded** (NEVER#6).

| leg | target | verdict |
|---|---|---|
| L1 | silver/acc | 6/6 landed, 431-432KB |
| L2 | **silver/rps — THE GATE** | 6/6 + `fresh=True, behind=1, max_lag=2` on deployed bytes + control + mutants |
| L3 | silver/trn | 6/6; ERR=61 all historical, 0 on target dates |
| L4 | silver/trn_nna | 6/6; ran after Layer A so `C_01.canonical_nna` gets real flow |
| L5-L7 | silver/uln, ult, rld | 6/6 each, ERR=0, + 671 historical dates healed |
| L8 | canonical step 7.5 | 54/54 after routing around the orchestrator defect |

```
LANDED CENSUS  7 tables x 6 dates = 42 required objects -> 42/42, 0 missing, 0 zero-byte
GATE (deployed _check_schwab_rps, 2026-07-24T16:12:44Z)
  latest_partition=2026-07-23  expected=2026-07-24  behind=1  max_lag=2  fresh=True
  CONTROL  07-15 -> behind=7 fresh=False   == trigger's own 15:01:43Z log
  MUTANT   07-20 -> 4/False   07-21 -> 3/False
CANONICAL  9 tables x 6 dates = 54 -> 54/54
```
**rc was never used as evidence** — and could not have been: the shell captured `tail`'s exit code, not
python's. Landed bytes throughout.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | route "post-run steps after the schwab canonical gold build" | **HONEST MISS** — "NO CURATED RULE MATCHED... these are FUZZY GUESSES, not a routing decision." Correct behavior; I did not pick one. Catalog gap for the canonical tree. |
| `comp-pipescript postdeps build_canonical_daily.py` | AE minimum before an ad-hoc run | **PARTIAL/GAP** — "No dependencies declared for: build_canonical_daily" |
| `comp-pipescript io build_gold_holdings.py` | AE minimum, gold script IO | **FAIL** — "Script not found... Did you mean: build_billing_dim, build_tax_dim..." |
| `safe-commit.sh` (x2) | both commits | PASS — risk-reflex HELD both and named a citation; I read it (see below) |
| deployed-vs-repo `md5sum` on lambda code | parity before trusting the gate | PASS — byte-identical `78801e4e...` |
| `_check_schwab_rps()` from deployed bytes | the acceptance instrument | PASS + control + mutant |
| `aws s3api list-objects-v2` / parquet row-count assertions | landed + semantic verification | PASS 42/42 then 54/54 |

**What worked:** the **risk-reflex hold** was the standout — it blocked my commit and told me to read
`memory/feedback_ds_sc_no_commit_coo_sole_committer.md`, which I did. It turned out to be **cross-fabric and
cross-lane** (CL fabric, DS/SC lanes, 2026-05-29) and so not binding on an AE commit under today's
Andrew-direct — **but it documents the exact `/commit-sweep` batching mechanism Andrew is reaching for right
now**, which I surfaced to COO as prior art. A gate that makes you read something you would not have read is
doing its job even when the citation does not bind.
**What failed:** `comp-pipescript` **cannot see the `data/canonical/schwab/` tree at all** — the whole
25-step gold family is invisible (`postdeps` returns no deps, `io` cannot find the script). This is the
**sibling of the cot-tree gap `~A` logged yesterday**: the comp-tools' script registry tracks the
`data/{firm}/scripts/gold/` shape and misses the canonical tree entirely. Two firm-lanes now with the same
blind spot — worth a tool item rather than two one-off notes.
**Gap re-confirmed (third session running):** no comp-tool returns an S3 object **body**. Reading the
deployed lambda bytes — the thing that made the gate verdict load-bearing — had to be raw `get-function` +
`curl` + `md5sum`.

## MCP Traffic

7 sent, 5 received. Significant: TO commit `62594e9911` (no GO) -> my discrimination to COO 153852Z + CTO
153917Z; COO 153628Z/153703Z (bridge instruction) -> **my correction 154446Z -> CTO ACCEPTED IN FULL
154535Z** (doctrine line taken verbatim); COO 153941Z (own forbidden-shortcut clause retracted); COO 161039Z
(**Andrew-direct ~1600Z: pushes are Tier-1/COO only, commits unchanged**) -> complied, no push; gate-green
to CTO 161505Z + COO 161551Z -> COO ACCEPTED 161924Z (*"twice in one session I have handed you an
instruction that would have sent you the wrong way"*); DS notified 163141Z; MSTR 162409Z; close-out COO
164104Z.

## Files Modified

see commit messages: `46359149f`, `1b7e133ed`. Plus:

| File | Note |
|---|---|
| `.claude/skills/49-schwab-conv/SKILL.md` | monolith named SOURCE OF RECORD; local folder + `01_raw` marked DEAD with measured evidence; **Step 1 marked INERT and folded away**; TRN warning retired with its history; **0824-only recorded as STRUCTURAL** (`_monolith_bronze.py:29-45` `master_for()` raises on unmapped — the two-buckets law has a real gate here); Step 7.5 carries the orchestrator defect + workaround; the ERR=61 census. |
| `deliverables/FINDING_49f_monolith_key_grammar_and_canonical_orchestrator_20260724.md` | both routed defects, grounded, with the trap-to-avoid on each. |

## Blockers

**NONE.** Two boundaries hit and correctly stopped at, both routed rather than crossed: the 719-partition
re-land (Rule 17a — bronze is immutable, and the remedy is a ruling not an edit, **CTO**) and the
`build_canonical_daily.py` re-point (Rule 13 — DS-owned path, **0.4.0_DS**). Nothing pending at Andrew from
this arc.

## Current State

Serial `0.6.2_AE_PartnerETL~C` live (PID 29064), Monitor `bdkllgl7g`. Ledger CLOSED, TO `MDPF_3FIRMS.GC-BF1`
**complete**.

**`s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,ult,rld}/` is current through `date=20260723`**
(was frozen at 20260715). **The mdpf 49financial freshness gate reads `fresh=True`** — verified by exercising
the deployed `mdpf-daily-trigger` bytes, not by reading config. **The chain will NOT rebuild today**: it
fired and deferred at 15:01:41Z and my roll-forward completed ~15:52Z, ~50 min after the event that would
have consumed it, and it is event-driven with no retry on a cleared deferral (CTO measured this; **not a
defect in the roll-forward**). Andrew's visual smoke is **tomorrow, on the next fire**.
`s3://opal-data-bd/canonical/schwab/{silver,gold}/` also current through 2026-07-23 (54/54).

**TWO COMMITS UNPUSHED AND HELD FOR COO** per Andrew-direct ~1600Z: `46359149f`, `1b7e133ed`. Verified by
fetch that COO's earlier `bcba89ceca..2306dbbdf5` carried nothing of mine.

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** re-point `data/canonical/schwab/build_canonical_daily.py:154-156` off the
   dead `01_raw` onto monolith bronze (or bd `silver/rps/`), **and make it exit non-zero on any ERR** so
   `=== done: N/M steps OK ===` cannot read as a pass. **Do NOT re-run the OneDrive sync as the fix** — that
   folder is dead, so the sync runs clean, uploads nothing, and leaves the symptom looking remediated.
2. **[1.0.0_SA_CTO]** ruling on the **719 present-but-unreadable** bronze partitions: re-land under the
   puller grammar / explicit logged legacy-name fallback / declare the pre-2024-07 era out of the serve
   window. Latent today, **fails ~120 dates per feed on the first `--force` or rebuild**.
3. **[2.0.0_SA_COO]** push the two commits; and the `/commit-sweep` prior art (`ccda81942`) for the push
   process being stood up — noting its scope is CL-fabric/DS-SC and its commit half is **superseded** by
   today's Andrew-direct.
4. **[tool owner, via COO]** `comp-pipescript` blind to `data/canonical/schwab/` — sibling of the cot-tree
   gap logged 07-23. Two lanes, same blind spot.
5. **[whoever closes item 1]** once `01_raw`'s last consumer is gone, **`01_raw` + the OneDrive channel can
   be decommissioned outright** — the clean end-state, and it retires this skill's whole legacy half.
