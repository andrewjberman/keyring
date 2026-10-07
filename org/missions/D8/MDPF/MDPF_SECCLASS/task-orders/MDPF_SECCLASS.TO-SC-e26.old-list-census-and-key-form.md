# TO MDPF_SECCLASS.TO-SC-e26 -- round 8 SC-e-26: FWD-17, FWD-15 -- the old list measured, and a key form for a security with neither ticker nor CUSIP

<to_id>MDPF_SECCLASS.TO-SC-e26</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~25</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-26` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-17, FWD-15 | **depends_on:** none. Slot ~25's queue: this order, then `TO-SC-e38`. Its two deliverables are
inputs to `TO-SC-e27` (slot ~24) and to `SC-e-32` later.

---

## WORKER FACE

### THE CELL

`SC-e-26`: the old list measured -- its rows partitioned (already in both lists; held today; the rest) and by key form (ticker,
`CUSIP:`, `NAME::<slug>`, none); and a proposed key form for a security with neither ticker nor CUSIP, with its four-postulate
record. A MEASUREMENT cell: read-only, no table write.

- FWD-17 (PRD v0.12): "Every security the old Black Diamond list holds has its entry in the shared list, placed again under the
  shared list's six classes." DONE WHEN: the count of old-list securities with no entry in the shared list reads zero.
- FWD-15: "A person filling the shared list can pull, for each firm, the held securities that have no entry."
- PRD ADDENDUM v0.10 contract notes: the whole old list, **held today first**, then the rest. The research seat's brief counts
  10,873 old rows, 2,378 already in both lists. **Key forms:** the old list keys some rows `NAME::<slug>`; the key form for a
  security with no ticker and no CUSIP (ADDENDUM v0.7) is declared before any such row is written, and it gates part of FWD-17,
  not only the 58 held.

**Inputs (measured by the issuer 2026-10-07, read-only; re-measure, do not copy):**
- **The old list:** DynamoDB `bd-securities`, us-east-1, hash key `ticker` (S). A consistent COUNT scan read **10,965** rows at
  ~07:5xZ 2026-10-07 -- not the brief's 10,873; report your own count and the difference. Sample keys: `DON` (ticker),
  `NAME::CRUISECAM INTERNATIONAL INC SHS` (name slug). Attributes seen: `asset_class`, `sub_asset_class`, `classified_by`
  (`gpt-4o-mini`, `gpt-5.4-mini`, ...), `confidence`, `needs_review`, `rationale`, `asset_name_raw`, `last_updated`.
- **The shared list:** DynamoDB `etf-classifications`, us-east-1, hash key `ticker`; 3,507 rows at the cut, including `CUSIP:`
  rows (key `CUSIP:<9 chars>`).
- **Held today:** the served Holdings builds per firm (cottonwood, inflection, 49financial). The issuer's held-dollars read of
  2026-10-07 (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/MULTI_ASSET_REMAP_B_HELD_20261007.json`) used
  each firm's build of date 2026-10-05 (cottonwood 27 parts); read that file to see the shape, find the served artifact it read
  (`comp-estate --resource holdings` or `comp-pipescript io`), and NAME the artifact and date you read in `held_source`.
- The ticker/CUSIP/name key rules already in code: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` and
  `org/standards/MDPF_SECCLASS_CONTRACT.json` (`identifier_namespace`: TICKER, CUSIP, BLOOMBERG at 0.4.0).

**Build:**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_census.py`: a consistent paginated scan of both
   tables plus the held read, and writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_CENSUS_<YYYYMMDD>.json`
   (UTC run date) in exactly this shape (the issuer's check reads it):
   `{"scanned_at": "<iso>", "table": "bd-securities", "denominator": N,
     "by_membership": {"in_both_lists": a, "held_today_not_in_shared": b, "rest": c},
     "by_key_form": {"ticker": w, "CUSIP:": x, "NAME::": y, "none_or_other": z},
     "held_source": "<artifact(s) and date>", "held_in_both": ..., "cross": {...}, "examples": {...}}`.
   `a+b+c == N` and `w+x+y+z == N`. `in_both_lists` means the same key (or its `CUSIP:` form) is in `etf-classifications`;
   state your match rule. `cross` is the membership x key-form table. Print the denominator.
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/KEY_FORM_PROPOSAL_<YYYYMMDD>.md`: exactly one line
   `PROPOSED KEY FORM: <form>` (e.g. a prefix and a slug rule), the count of old rows it would key, the four postulates by name --
   MECE, SAME GRAIN, INTENT COHERENCE, STATE COHERENCE -- and a word-boundary token census of the prefix over the repo
   (`comp-find`, denominator printed). It must not collide with `CUSIP:` or a valid ticker.
3. ASCII only.

### ACCEPTANCE

<criterion id="SC8-e26-AC1" cell_refs="SC-e-26"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e26.py census</invocation><expect>SC-E26-CENSUS ok=True</expect></criterion>
`SC8-e26-AC1` -- both partitions sum to the denominator, and the denominator is within 25 rows of a fresh count of the live table.

<criterion id="SC8-e26-AC2" cell_refs="SC-e-26"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e26.py keyform</invocation><expect>SC-E26-KEYFORM ok=True</expect></criterion>
`SC8-e26-AC2` -- the proposal names one key form and carries the four postulates.

<expected_criteria>SC8-e26-AC1,SC8-e26-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`no OLD_LIST_CENSUS_*.json`); AC2 FAIL as expected. Green arm (a census
file at the live count): `SC-E26-CENSUS ok=True denominator=10965 live=10965`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted. `R10_CHECKS/issuer_check_sc_e26.py` is READ-ONLY to you.
- **Read-only against AWS.** No table write, no S3 write, no deploy. No vendor or model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W25-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_CENSUS_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/KEY_FORM_PROPOSAL_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-26`.
<owned_cells>SC-e-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e26-AC1, SC8-e26-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~25/MDPF_SECCLASS.TO-SC-e26.old-list-census-and-key-form.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e26-AC1,SC8-e26-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the denominator and both partitions, the held source and date, the proposed key form and how many rows it keys, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): no armed gate names bd-securities' census. A read-only cell arms nothing.
comp-iam: RUN -- R8 battery: 0 gap lines name bd-securities or etf-classifications. Read with the worker's session credentials; no role declared.
comp-adversary: RUN -- R8 battery; cell-specific issuer reads 2026-10-07: bd-securities key schema (ticker HASH), consistent COUNT 10,965 (R8 held 10,873 from the brief), key forms seen (bare ticker, NAME::). BLIND: the held source's exact artifact (the worker names it).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (FWD-15, FWD-17, ADDENDUM v0.7, v0.10); DECOMP_R8 @495efa3c32.
