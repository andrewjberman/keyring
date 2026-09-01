# ADVI_BDPARITY T2-3 -- the dim-436 denominator, and the consumer arm that drops the blocker to "egress"

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, TRACE

**Seat:** `0.4.0_DS_ClientPlatform~B` | **Date:** 2026-09-01 | **Window:** session start -> now
(first log of this session; prior log `2026-08-20/broker_queue_duplication_finding_2350-0020Z.md`)
**Scope as spawned (COO --say):** ADVI_BDPARITY ONLY -- T1-ORACLE + T2-DIMS, BUILD-ONLY, serve gate
downstream and STAYS. Held throughout.
**Commit:** `9b1946010a` (3 files, 334+/23-)

---

## Current State

Read at session start: **T1-ORACLE 4 of 4 PASS** (complete, nothing owed). **T2-DIMS 4 of 5** --
`T2-3` FAIL. One open ASK also sat unanswered from `2.0.0_SA_COO` msg `20260819T224419Z` (ten days):
*prove "dim 436 absent" with a denominator and a positive control before it gets escalated.*

**T2-3 still FAILs and that is still the right record.** What this session changed is the QUALITY of
the escalation under it and the COST of closing it.

**The measurement (MEASURED-BY-ME, current vintage).** Bronze `allocation_390224` **date=2026-08-31**,
pulled 2026-09-01T06:30:40Z, `template_id 390224`, `run_id 524910` -- the vendor's own xlsx, one plane
ABOVE our silver: **92 header columns; "primary" 0 of 92; POSITIVE CONTROL "portfolio" 8 of 92.** Same
figures on landed silver `fact_bd_allocation/date=2026-08-18`. **All 92 header names read UNSCOPED on
both planes**, because a token census cannot see a flag under a name I did not guess -- there is none.
The only account-to-advisor columns are the ROLE-SPLIT set (`Architect`, `Consultant`, `Implementor`,
`Local Ops`, `Additional Advisor`, `49 House Split %`), which is the OTHER basis.

**The finding that reroutes the escalation.** COO's question offered three readings; the true answer is
a FOURTH. The 92 columns are **a persisted template's SELECTION, not the vendor's catalogue.** So
*"dim 436 absent, therefore the ruled basis has no source"* is **too strong to forward**. The survivable
sentence: the ruled basis has no source **in the feed we pull daily** (measured, discriminating,
current); whether it has one at the vendor is **unverified in-estate**. Those route differently -- a
sovereign alarm vs a scoped request for one read-scoped call.

**A single-carrier claim I could not corroborate.** `4.0.0_SA_CRO~A`'s
`BD_PORTFOLIO_GROUP_KEYING_SCAN_20260819.md` s.2 asserts dim 436 exists (Portfolio level). I tried to
re-derive it at source and **could not**: the catalog that seat staged to
`s3://opal-data-bd/code/bronze/endpoint_catalog/` carries only per-querytype COUNTS (`qt6 n_dims 150`)
and measure names -- **no dim ids**. **My positive control caught this**: I searched for `436`, for
`primary`, AND for `1140` (that seat's own probe dim, which must be present if any dim ids are). **All
three returned zero, including the control.** A dead arm and a true absence read identically, so that
read produced NO evidence in either direction and is recorded as such -- not as a second finding.

**The build half is done and exercised.** `bd49f_dim_portfolio_group.py` now consumes dim 436 when it
appears (`attach_is_primary` + `assert_primary_partitions_accounts` + a partition reconciliation in
`guard`). It derives nothing -- it reads the vendor's assertion; a wrong-name miss reads ABSENT, never
a false PRESENT. **Blocker reduced from "build + egress" to "egress".**

**Live artifacts (MEASURED in S3 today, unchanged by this session):**
`s3://opal-data-49financial/gold/advi/dimensions/dim_portfolio_group/date=2026-08-18/data.parquet`
10,411 B etag `b26d6cce17f530ade96abb86e8ccba92`; `bridge_group_account/.../data.parquet` 197,188 B
etag `d937238efba43e2d97d102e6bf4c2a7e`; both `2026-08-19T22:50:1xZ`. Upstream
`opal-data-assets/blackdiamond/49f/silver/fact_bd_allocation/date=2026-08-18/data.parquet` 3,726,932 B.

---

## Controls run (the reason any of the above is evidence)

| Arm | Result |
|---|---|
| POSITIVE -- synthetic clean partition | 6,155 accounts, one primary each; primary-only total **$1,550,733,057.94** == distinct-account universe **$1,550,733,057.94**; **residual $0.00** |
| FALSIFIER A -- one account given TWO primaries | **FIRED**, named the account, refused |
| FALSIFIER B -- one account given NO primary | **FIRED**, named the account, refused |
| INERTNESS -- pre-edit file vs post-edit, same input | both tables **FRAME-EQUAL**; manifest differs only by 3 ADDED informational fields |
| POSITIVE CONTROL on the column census | `portfolio` 8 of 92 on both planes -- the zero for `primary` discriminates |
| POSITIVE CONTROL on the catalog read | `1140` = 0 alongside `436` = 0 -- **the control failed, so the read was discarded** |

⛔ **LIMIT, stated because it is the half that would travel wrongly:** the column does not exist, so the
exercise ran against one I wrote myself. It validates **the consumer**. It says **nothing** about BD's
real semantics -- whether dim 436 asserts primacy per **ACCOUNT** (assumed) or per **PORTFOLIO** is
UNMEASURED and must be read off the first real pull before any partitioned figure is quoted.

---

## Corrections to my own lane's delivered record

1. **`declared_exclusions[1]` in `ADVI_BDPARITY.T2-DIMS_PROOF_OF_SPEC.json` was STALE** -- it read
   "THE S3 GOLD MINT of both tables -- Withheld deliberately" while **T2-1's PASS row in the same file
   said minted**. One file asserting both halves of a contradiction. The withhold was discharged
   2026-08-19 ~22:50Z, three minutes after `0.4.0_DS_ClientPlatform` minted the silver upstream at
   22:46:03Z. Corrected, with the live etags cited.
2. **The producer's artifact row was re-pinned.** It cited `8d746d7703`, which no longer carries the
   current file after this session's edit. Now `PENDING-THIS-COMMIT` rather than a vintage predating
   the change it describes.
3. **Checked and NOT a defect, recorded so nobody re-chases it:** both tables' `manifest.json` share an
   ETag. It is a RUN manifest with a `tables` key carrying each grain separately -- verified by sha256
   on both downloaded objects and by reading the content.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find --name` | `'*BDPARITY*'`, `'*ORACLE*'`, `'*DIMS*'`, `'*portfolio_group*'`, `'*bd_allocation*'` | PASS | Located both TO faces + both proof instances + the CRO keying scan. Denominators printed (42 of 42 on the BDPARITY census, single page). |
| `.tools/proof-of-spec-check.py` | `<T2 instance> T2-1,T2-2,T2-3,T2-4,T2-5` | **PASS after a real catch** | First run **rc=1**: it rejected my `PENDING-COMMIT` placeholder as "neither PENDING-THIS-COMMIT nor a 7-40 hex commit-ish". Fixed; re-run **VALID rc=0**, 5 rows, 0 violations, measured UNPIPED. |
| `.tools/commit-gate.sh` | on the edited producer | PASS | py_compile + ds-precommit + ruff py39 clean, 1 of 1. |
| `.tools/safe-commit.sh` | `--author ... -F <msgfile>` | PASS | `9b1946010a`; risk-reflex REFLEX CLEAN (3 files vs 1,662 danger nodes); `[msg-verify] MATCH len=6128`. |
| `.tools/aws` (s3api/s3 cp) | list + get on 49financial gold, assets silver/bronze, opal-data-bd catalog | PASS | All reads operational, own buckets. Zero vendor calls. |
| `comp-tool-hud` (Rule 21 gate) | fired on a raw `find` | PASS | Correctly DENIED a raw `find org -iname ...` and routed me to `comp-find`. Gate did its job; I complied rather than marking `# rail-checked`. |

**What worked.** The proof-of-spec checker earned its keep -- it caught a placeholder token I would
otherwise have committed, and the failure message named the exact accepted forms. The Rule-21 rail also
fired correctly on a raw `find`.
**What failed.** Nothing in the toolchain. The one dead instrument was the staged BD endpoint catalog,
and that is a data gap, not a tool fault -- **and my own positive control is what exposed it**, which is
the whole reason a control is run.
**Gap found.** `comp-find --name '*bd_allocation*'` does **not** locate
`data/assets/scripts/silver/bd49f_fact_allocation.py` -- the file is `bd49f_fact_allocation`, so the
`bd_allocation` substring misses it. The T2 proof's own `compiler_tools` section claims that exact
invocation located that exact file ("1 hit across 27,010 files"). Today it returns 4 hits, none of them
that script. **A basename-substring glob fails toward a plausible-looking wrong answer.** Not chased
(corpus default also moved tracked -> all since; either could explain it) -- recorded so the next seat
does not trust that row.

---

## MCP traffic

**5 handled.** 4 inbound were stale broker re-surfaces (`64962`, `65122`, `65463`, `71931`, dated
08-21/08-26) -- all read, all **ACKed** (the READ clock, which had never been recorded, which is why the
broker kept re-serving them). **None actioned, by scope:** `65122` asks this seat's availability for the
MDPF decomp cohort (ten days stale, different project); `71931`'s DS~B section is P4-EMIT / atom-8
`lineage_49f.json` (ADVI_INSURE scope). This spawn is **ADVI_BDPARITY ONLY** and I did not widen it.
1 outbound: **`91193`/`91194`/`91195`/`91196`** to COO / CRO~A / CTO / DE -- 2 DELIVERED, 2 QUEUED,
0 REFUSED (denominator 4).

---

## Files Modified

See commit message `9b1946010a` for per-file detail. Summary:
- `data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py` -- the dim-436 consumer arm,
  the partition assertion, the guard's reconciliation, docstring re-measurement.
- `org/tier2_senior/0.4.0_DS_ClientPlatform~B/deliverables/ADVI_BDPARITY_T2-3_DIM436_DENOMINATOR_20260901.md` (new).
- `org/tier2_senior/0.4.0_DS_ClientPlatform~B/deliverables/ADVI_BDPARITY.T2-DIMS_PROOF_OF_SPEC.json` -- stale
  exclusion corrected, T2-3 evidence refreshed (status unchanged FAIL), artifact rows re-pinned.

---

## Blockers

**ONE, evidence-cited, correctly gated, and NOT mine to clear.** T2-3's partition half needs
**one vendor-side act**: amend persisted template `390224` to select **dim 436 `Primary Portfolio
Group`** at the **Portfolio** level, then re-pull. That is **VENDOR EGRESS -> Andrew's explicit per-use
word** (availability is not authorization). Not taken, not requested by this seat.
**Everything else on this seat is either done or out of scope.** This is a condition, not a stall.

---

## What this seat did NOT do

- **No vendor call.** No template amendment, no re-pull, no BD egress of any kind.
- **No serving.** Gold only; the P4-class CTO gate is untouched and stamped in both manifests.
- **No re-mint** of the 08-18 gold -- the change is provably inert on the absent-column path, so
  re-minting would move a live artifact for three informational fields and zero data delta.
- **No heuristic `is_primary`.** The TO forbids it; the arm reads the vendor or reports ABSENT.
- **No push.** Nine local commits are unpushed and **eight are foreign to this seat**; pushing them is
  outside this scope and this fabric coordinates pushes through MSTR merge windows.

---

## Observation, surfaced not chased

The allocation export lands **DAILY** (66 objects, partitions through 2026-08-31, pulled today). The T2
gold tables exist at **date=2026-08-18 only**. That is **stale-BY-DESIGN** under the build-only fence --
T2-4 asserts 0 references in `chain_49f_entrypoint.py:_stage_list`, and the WP-2 absorption puts
scheduling under "P2's floor, NO new trigger machinery." Recorded because **"frozen at 08-18" and
"broken" look identical from outside**, and this is the first thing that must move when the serve gate
opens. No act taken.

---

## Next Steps

1. **[`4.0.0_SA_CRO~A`]** Re-derive the dim-436 existence claim under that seat's own standing
   read-scoped grant, and stage a catalog artifact that carries **dim ids**, not just counts. It is
   currently the single carrier for a fact load-bearing on a RULED basis.
2. **[`2.0.0_SA_COO`]** Escalate on the NARROWED sentence (no source in the daily feed; vendor-side
   existence unverified), not on "the ruled basis has no source" -- msg `91193`.
3. **[Andrew, via `2.0.0_SA_COO`/`1.0.0_SA_CTO`]** The per-use word for one template amendment +
   re-pull, if the partition half is wanted. On that pull T2-3 closes on a **re-run with no code
   change** -- and the vendor's per-ACCOUNT-vs-per-PORTFOLIO semantics must be read off it first.
4. **[`0.4.0_DE_ClientPlatform`]** Nothing owed. `is_primary` remains ALL-NULL; D3 `TO-D3.4` logic must
   keep treating it as CANNOT-ANSWER, never as false.

**Status: T2-DIMS 4 of 5. T1-ORACLE 4 of 4. Push state MEASURED: LOCAL @`9b1946010a`; origin/CLOUD at
`a29c2591ae` (ls-remote read).**
