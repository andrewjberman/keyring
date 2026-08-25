# SESSION LOG — `0.4.0_DS_ClientPlatform~I` — 2026-08-25 ~10:00–11:10Z

**seat:** `0.4.0_DS_ClientPlatform~I` (fresh instance, seated this session)
**archetype:** MEASURE
**scope:** ONE project — `COT_CANON458`, `TO-R1-DS` (surfaces (a)+(b) + 3 invariants, 10 cells, measurement-only)

---

## Current State

`COT_CANON458.TO-R1-DS` **COMPLETE** — all 5 criteria PASS, proof-of-spec instance **VALID rc=0**
(0 violations; alignment 5/5 criteria → cell, 10/10 cell_refs → decomp, 10/10 declared cells → criterion).

Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform~I/deliverables/COT_CANON458.TO-R1-DS_SERVED_CENSUS_AND_EXCLUSION_PREDICATE.md`

**MEASUREMENT-ONLY, discharged by construction: zero S3 writes, zero infrastructure, zero served bytes moved.**
This TO produced exactly 3 files (report, proof-of-spec instance, this log).

### The three findings

1. **The canonical `458,053,742.19` is served NOWHERE** — 0 occurrences across all 21 served-leaf types, against
   a positive control of 73 occurrences / 12 types for `488,460,108.95`. A *controlled* zero.
2. **The exclusion predicate cannot be applied at the served plane today, for two independent reasons.**
   `D_05`'s `firm_daily` ends **2026-08-19**; every served leaf is `data_as_of` **2026-08-21** (probed: 08-20/21/22/24
   all absent). And `D_05` is DataMining-plane with a self-declared **−$8,697,205.48** gap to the served plane.
3. **Applying it anyway reproduces the number Andrew called wrong, MEASURED not inherited:**
   `D_05.firm_daily[-1].aum_supervised` @08-19 = **`449,733,561.36`**.

### The two findings I did not expect to make

- **A leaf can carry the firm total without carrying a total FIELD.** `firm/client_directory.json` has no total
  field; its 222 household `aua` values sum to **488,460,108.90** (headline less $0.05). `firm/cumulative_chart.json`
  `geo`/`adv`/`ofc` last rows each sum to **488,460,108.95** exactly. A field-name-keyed census marks both as
  carrying no total and is **silently wrong** — and these are precisely the leaves that would still read 488M beside
  a 458M headline.
- **AC3's filename trap fired exactly as written.** `platinum/firm/header_metrics.json` is declared as `SERVED_KEY`
  in **two** files and **neither writes to S3** (`grep put_object|boto3` → 0 hits in both; `d01`'s docstring says
  *"NO S3 writes"*). The `runners_cot/d*` family is an unported re-implementation. Resolved the real producers on
  the **deployed artifact** instead, via the `CacheControl` header the two live producers set differently:
  **D_04 = 20 of 21 types (all 14 total-bearing); D_00 = 1.**

---

## Controls

- **MUTANT — FIRED-AS-EXPECTED.** The load-bearing claim is a *negative* one, so I mutated its target to a
  known-present value: 0 → **73 hits**. The matcher discriminates; the negative finding stands.
- **DETERMINISM — STABLE, after catching a false instability.** Re-run showed 1,125 keys but **2,252 diff lines
  and a different md5**. `od -c` → run 2 carried `\r\n`, run 1 `\n`. After `tr -d '\r'`: **0 diff, identical md5.**
  A uniform difference across a whole set is an **instrument** signature. Recording the first reading would have put
  a fabricated instability on the estate's served census.
- Census cross-instrument agreement (`s3 ls --summarize` = 1125), negative control (`None`), positive control on the
  absence-probe shape (1 hit), 3 live 404s, 21/21 byte-size-verified downloads.

## Compiler Tools

- `comp-find --name 'D_05*'` / `'*supervised_split*'` → unique hit, DENOMINATOR 1/28,444 scanned.
- `comp-find 'platinum/firm' data/cot` → 90 hits / 114 files, bands HEAD=9 DEF=7 SURFACED=58 CONFIG=16.
  **The DEF band is what surfaced the two write-nothing `SERVED_KEY` declarations** — the AC3 finding came out of
  the band split, not out of the raw hits.
- `comp-which "census S3 platinum served objects and leaf names for a firm"` → near-tie, no tool fits an
  object-and-leaf-name census; ran it as an operational `s3 list` (explicitly not rail-nudged), auto-paginated,
  denominator printed. Recorded as a coverage observation, not a routing failure.

## Blockers

**None.** Nothing is held on this seat and nothing is asked of anyone by me.

## Next Steps

1. **[`2.0.0_SA_COO`]** Accept or rework `TO-R1-DS`. Reported at completion with the instance path and rc.
2. **[`3.0.0_SA_CVO`, cc COO]** 5 OBSERVATION-class surprise items filed (S-1..S-5). **No BLOCKING, no ARMED item** —
   nothing needs a disarm owner.
3. **[not mine, flagged only]** The (a)-surface classification's Rule 24 postulate **(iv) FAILS and is named**:
   a remedy that edits total-bearing *fields* covers **11 of 14** — `mix_summary` sits on a third total and the two
   implicit-total leaves move only if their component rows move.

## Notes for a successor

- The lane inbox `org/mcp/inbox/0.4.0_DS_ClientPlatform/~I/` **did not exist** at seating; I created it. Mail sent to
  this lane before ~10:2xZ had nowhere to land.
- `find … -iname '*CANON458*'` over `org/` returned **0** at ~10:0xZ and the TO landed at **10:05Z** — a genuine
  race, not an instrument failure. The TO is at the **base** `0.4.0_DS_ClientPlatform/task_orders/` path, not `~I`.
- Both `list_task_orders` and `to-check --assignee` are broken for lane seats (XXX.md's own 09:4xZ correction:
  the discriminator is the `**SEATED: \`serial\`**` prose notation, **not** the tilde). The TO's file path came
  from COO's message; there is no query that returns it.
- Native `aws.exe` cannot resolve a `/cygdrive/...` **outfile** path — `s3api get-object` fails `[Errno 2]`.
  Route content through stdout (`aws s3 cp s3://… -`) and let bash own the redirect.

---

*Zero crons armed (Tier-2 lane row, XXX.md Step 1b-F). `/watcher` armed once at load: task `b0pjl2tsf`.*
