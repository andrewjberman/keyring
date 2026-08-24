# 2.0.0_SA_COO~Z — ETFS_INGEST stage-3 decomp, certified, and round-1 dispatch complete (1950–2110Z)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, DIAGNOSE, VALIDATE, SCRIBE

Session: launch ~19:50Z → 21:10Z. **8 commits, all mine.** ~25 MCP sends, ~60 messages read and
READ-acked. Zero crons armed for the entire session.

---

## 1. ⛔ CURRENT STATE — READ THIS FIRST

### Safe position, measured not asserted

- **Every path I authored is COMMITTED.** Nothing of mine is uncommitted.
- **NOTHING APPLIED, NOTHING DEPLOYED, NOTHING PUSHED BY ME.** No S3 write, no served key moved.
- Commits `@babfb23e8c`, `@796c92888c`, `@4bf13f9d68`, `@fcdf042972`, `@22f00061ec`, `@857c8b65a7`
  are **on `origin/SITEZ`** (measured by `git branch -r --contains`, not assumed);
  `@ec2edee468` and `@efa80f37a4` are **LOCAL, riding integration**.
- **The certified decomp has not been re-entered since I froze it.**

### ⛔ THE ONE THING NOBODY HAS VERIFIED, and it is the certifier's line not mine

> `3.0.0_SA_CVO~Z`, 21:06Z: ***"the 22:00Z fire is the EXERCISED layer… Nobody has yet verified the
> pipeline WORKS — only that its code and config are right."***

Four seats verified DESIRED / APPLIED / CODE on the F2 deploy. **That is four seats on three rungs,
and EXERCISED is the fourth.** `ETFS_INGEST.TO-1` AC4 discharges on the 22:00Z scheduled fire;
`0.7.0_AE_CloudOps~Z` reads the log plane, `0.0.0_AB_MSTR~Z` watches the artifact plane. **A fresh
seat must not read "deployed and certified" as "working."**

### Round-1 dispatch — every seated seat holds a TO

| TO | cells | seat | state |
|---|---|---|---|
| **TO-1** TrueShares call-site deploy | `T0-3` `T1-3` `INV-1` `INV-2` | AE~Z | **DEPLOYED 20:31Z**; AC4 open until 22:00Z |
| **TO-2** canonical row conventions | `T2-3` `T2-4` `CONV-1..3` | DS~Z | pending, authoring |
| **TO-3** C2 gold re-point (scripts) | `T3-1` `INV-4` | DS~Z | staged, **queued behind TO-2** |
| **TO-5** condition (ii) | `T5-1` `T5-2` | DE~Z | GO'd; **AC1 discharged at issuance** |
| **TO-4** converter holdings feed | `T2-1` | DS-class | ⛔ **HELD BY DESIGN** — it implements TO-2's rulings; cutting it now specifies code against undecided conventions |

**Alignment, re-run at every cut (never re-typed):** 4 TO files · **36 cells** · 22 criteria, all
carrying `cell_refs`, **0 ghost refs** · **14 covered / 22 uncovered, 14+22=36**.

### Premises a fresh seat must RE-GROUND

| premise | oracle |
|---|---|
| the F2 deploy is live | `get-function-configuration etfs-netassets-daily` → `CodeSha256` **`BEITykjhm…`** (was `tHeVS53p…`), LastModified **2026-08-20T01:18:32Z → 2026-08-24T20:31:09Z** |
| the decomp is certified at ONE vintage | `git show fcdf042972:…/DECOMP.md` → sha256 `1bc5eba5de…`, 480 lines. **No other vintage is covered** |
| gold target still greenfield | `aws s3 ls s3://opal-data-etfs/gold/ --recursive \| wc -l` → **0** — ⛔ **pair with a sibling that must be NON-zero**, `silver/holdings/` → 72 |
| the universe is four | `aws s3 cp s3://opal-data-etfs/config/etf_universe.json -` (runtime-read; never restate in code) |

---

## 2. What I delivered

**Stage 3 opened on Andrew's word** (~19:5xZ, via CTO~Z msg 4835): *"run atom_decomp on the key
surfaces declared in the PRD, **validate SOT in the process**, and begin writing and issuing TOs."*

I read *"validate SOT"* as an **obligation on the run, not a description of it** — so all eight PRD
facts were re-derived at the live primitive with their own controls rather than cited.

- **Decomp:** `workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/` — 36 cells over the
  PRD's T0–T7 + the §5 conventions + **4 CROSS-PLANE INVARIANT cells**, Rule 24 four-postulate
  record with postulate (iv) **failing on a named axis**, degraded-cohort disclosure on its face.
- **CERTIFIED** by `3.0.0_SA_CVO~Z` @422bdb431b, bound to `@fcdf042972`.
- **Four TOs cut and GO'd**, four surprise items filed (Z-S-D/E/F/G), two amendment asks routed to
  the PRD author rather than silently cell-edited.

### The SOT result that mattered

**PRD F8's *"+1 (DIVZ 30 vs 29)"* is FALSIFIED.** Neither oracle CSV ends in a newline, so every
line-counting instrument undercounts by one. Three instruments (`tail` 29/43, `wc -l` 30/44,
`csv.reader` 30/44; distinct tickers 30/30 and 44/44). **True delta ZERO.**
And the surviving IDVZ **+2** differences a **2026-07-31** snapshot against an **2026-08-21** count —
**21 days apart**, so it cannot discriminate a reconciliation gap from turnover in either direction.
**The same-day compare cannot exist until `T0-3` lands**, so `T3-3` carries an OBSERVED-completion
dependency instead of a date.

**Five facts the PRD does not carry** (N1–N5), of which the load-bearing one: the source map's
`artifact_sha256` **equals** the live `CodeSha256` while the deployed code was 43 lines behind
source — **Rule 4's own warning, live, on the function this project first deploys.**

---

## 3. My own defects this session — five, none caught by care

| # | defect | what caught it |
|---|---|---|
| 1 | **Hand-counted the cells: 26/27 vs a true 36** — in the document whose entire point is printed denominators, after banking *"a denominator is an artifact, not a summary"* from three prior instances | a four-line extractor |
| 2 | **TO-1's criteria TABLE and its machine-readable `<criterion>` BLOCK disagreed** on `INV-2`. The block is what the validator reads | the same extractor — the count alone would never have shown it |
| 3 | **My 26→36 fix SWAPPED which cell was orphaned** (`T6-6`→`T6-5`) rather than closing the gap; §5 enumerated 34 of its own 36 | `3.0.0_SA_CVO~Z`'s partial cert |
| 4 | ⛔ **I wrote four negative-control ids into §5 IN BACKTICKS and my own extractor counted them — 40 instead of 36.** I contaminated my denominator with my controls, **in the paragraph asserting it was clean**, ~60 seconds after being warned about that exact class | re-running the extractor after the edit |
| 5 | **I promised to edit an artifact I had frozen 20 minutes earlier** — the freeze contract was still true, I just stopped applying it when a small obviously-useful edit came along | writing the sentence and reading it back |

Plus a **relay defect I propagated**: *"both carry SALXX"* meant the two TrueShares **funds** in
MSTR~Z's brief, became *"both issuers"* in the PRD, and I copied the PRD. **Each hop was a faithful
copy and the referent silently widened.** DS~Z measured it: SALXX is **0 of 114** live rows.

⛔ **THE PATTERN: EVERY ONE READ CLEAN, AND NOT ONE WAS CAUGHT BY BEING CAREFUL.** Four fell to a
control, one to a peer, one to reading my own sentence back. **#4 is the sharpest — I broke a rule
inside the paragraph that states it, having been told about that precise failure a minute before.**

### And a criterion of mine that was wrong in both directions

After landing the SALXX correction I ran `grep -c "both issuers carry"` expecting **0**. It returned
**1 — and the document was correct**; the survivor is the quotation inside my own retraction.
**A `0 remaining` criterion over a document that deliberately quotes what it retracts DEMANDS THE
DESTRUCTION OF ITS OWN CITATION.** I already had the mirror banked (a blanket replace that *ate* a
retraction's citation while the same check passed). **Same criterion, both failure directions:
passes when the citation is destroyed, fails when it is intact.** Memory updated to carry both.

---

## 4. What other seats found in MY specs — the channel working

- **`0.4.0_DS_ClientPlatform~Z`** — TO-2's premise oracles at pickup produced a **BLOCKING × ARMED**
  item: `etf_daily_pull.py:88`'s bare `~h["is_cash"]` **raises TypeError** the moment a TrueShares
  row lands — **which TO-1's own deploy arms tonight.** I censused the blast radius (**exactly one
  site**; constituents leg safe, gold already None-tolerant), named the remediation owner, and
  surfaced the **A2 conflict** (both branches break the L1-2 streak) without adjudicating it.
  CTO~Z amended A2; MSTR~Z owns the fix. **DS~Z was wrong twice on the way to the right finding and
  both wrong versions were more alarming and more plausible than the truth.**
- **`0.4.0_DE_ClientPlatform~Z`** — rendered Z-S-G against the **real artifact as fixture** and
  returned a third answer neither position could produce: **labels fine, colour channel DEAD** —
  *"it renders UNDIFFERENTIATED, not wrong."* They found a **third lookup table my premise missed**
  (the mechanism site), so **my two-map figure was a FLOOR I presented without saying so** — in a TO
  whose own AC2 warns that a census is a floor. And they showed **`T5-1` is TWO acts**: a field-only
  swap inherits the dead colour channel at finer grain, **strictly worse**. Folded in as AC6
  **before the GO**, so it reached the seat already scoped.

**Both surfaced a scope gap in a frozen spec and left the scoping to the issuer.** That is Rule 27's
surprise channel behaving exactly as designed.

---

## 5. Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-trigger` | ×3 (`etfs-netassets-daily`, `opal-assets-silver-etf`, `positioning`) | schedules + fired-evidence, **denominator printed every time (136 rules + 18 schedules)** | ⚠ Surfaced **Z-S-E**: `opal-assets-silver-etf-sweep-daily` is LIVE+ENABLED and reported *"not found in `infra/aws/**/*.tf`"* — **a TEXT MISS, declared-ness only**, not a claim it is unmanaged |
| `comp-find -i` | portal censuses | `sub_asset_class` 16 in-plane; `GICS` **5 / 412 files, ZERO in the Positioning plane** | The `GICS` zero is the useful one: his *"GICS replaced"* is a **VALUE** change, not a token to find |
| `comp-estate --definitions` | mandated into TO-2 phase 1 | — | Build-ladder rung 2 applied to **vocabulary**, not just code |
| `comp-pipescript io --pipeline etfs` | mandated into TO-3 phase 1 | — | `--pipeline` REQUIRED; flagless is rc=2 REFUSED |
| `comp-iam service` | mandated into TO-1 phase 1 | — | Written into the TO as a **FLOOR** with the live-primitive escalation for the new bronze prefix |
| `safe-commit.sh` | 8 invocations, all `-F` msgfiles authored with the Write tool | **8/8 rc=0**, risk-reflex CLEAN each time with its denominator (1–4 files vs 1,324 danger nodes) | 0 gate failures, 0 owned-paths refusals |
| `.tools/audit-archive-invoker.py` | startup A.2 | rc=1, **18 findings** | Pre-existing append-only/coverage drift; **not mine, not chased** — non-D4 under the fabric-scope word |
| A.3 PATH probe + EXERCISE | startup | **98 of 102 resolve bare**; forwarder RAN | The exercise limb is the load-bearing half — resolution is not execution |

**Gaps found:** `comp-trigger` cannot render Scheduler expressions and says so; **no comp-tool
compares a Lambda package member to the source it was built from** — the F2 verification was raw
`get-function` + zip census + `git show`, and I marked those calls `# rail-checked` with the reason.
That is a real coverage gap on Rule 22a's CODE layer, not a rail evasion.

---

## 6. Blockers

**None BLOCKED at this seat.** Open and owned elsewhere:

- **`ETFS_INGEST.TO-1` AC4** — EXERCISED evidence, discharges on the 22:00Z fire. AE~Z + MSTR~Z.
- **Z-S14 remediation** — `etf_daily_pull.py:88`. MSTR~Z owns it, executing after the fire per A5.
- **D4 register member-add for `ETFS_INGEST`** — base MSTR is sole writer; requested, not written
  from this lane (`INGEST-T7-1`). ⚠ **CVO~Z/CTO~Z note it becomes a REAL blocker on the `/self-drive`
  stop-condition**: a claimed-but-unregistered member cannot be read as complete.
- **Rule 17b amendment** for the C2 gold home — bridged to base CTO. Does **not** gate TO-3.

---

## 7. Next Steps

1. **[AE~Z]** TO-1 AC4 on the 22:00Z fire — the first EXERCISED evidence this pipeline has ever had.
2. **[DS~Z]** TO-2's four four-postulate records against the **corrected** premises, then TO-3.
3. **[me]** Cut **TO-4** (`convert_trueshares()` holdings feed) once TO-2's conventions are ruled —
   held deliberately, not forgotten.
4. **[DE~Z]** TO-5 AC6/AC7; T5-1 unblocks when the additive field lands.
5. **[whoever edits the characteristics field list]** ⛔ **Re-check the overlap.** MSTR~Z measured
   that `characteristics` survives a missed day only because its fast-moving members are captured by
   the constituents leg — **an OVERLAP, not a mechanism, and C3's edit touches that exact list.**
6. **[a fresh COO~Z]** The decomp is CERTIFIED at **`@fcdf042972` and no other vintage**. If a cell
   must change: amend, commit, hand CVO~Z the new commit-ish, and **their verdict is VOID rather
   than silently carried forward.** That contract is mine and I nearly broke it once already.
