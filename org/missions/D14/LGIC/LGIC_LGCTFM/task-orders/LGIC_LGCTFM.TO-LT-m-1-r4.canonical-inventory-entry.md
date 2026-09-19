# TO LGIC_LGCTFM.TO-LT-m-1-r4 -- THE MISSING CANONICAL ENTRY: the estate has six tools for one question and no answer

<to_id>LGIC_LGCTFM.TO-LT-m-1-r4</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~2. AC2/AC3 PASS at the cell's pin; AC1 read FAIL there because THE ISSUER'S ARM WAS THE DEFECT (m1-entry demanded a status vocabulary the manifest has never admitted, intersection 0 of 127 -- LGIC_LGCTFM-W2-S35). Arm repaired @1d4df2c115; all mechanical criteria re-run by 2.0.0_SA_COO~G at the merged tree b238df04d5 and PASS. The pinned proof is NOT rewritten and still records AC1 FAIL at its own vintage (S32). AC4 judgment PASS at L9 (3.0.0_SA_CVO).</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-m-1` (decomposition v1.5 s.15) | **outcome_ref:** FWD-1 | **depends_on:** none -- the only order on slot `~2`

---

## WORKER FACE

### THE CELL

`LT-m-1`. Ruling R-81 (@`4443e7308e`): `comp-which` asked literally *"What AWS resources exist + how are they
typed/connected?"* returns **78 ranked rows with NO WINNER** -- comp-iam 1.60, comp-keys 1.55, comp-blast 1.52,
then comp-estate / comp-find --corpus aws / comp-kuzu tied at 1.50. By NFRA_GRAPHS AC1, *"exactly one
canonical entry per distinct graph use-case"*, **A SIX-WAY TIE ON THE INVENTORY QUESTION IS A MISSING
CANONICAL ENTRY** -- not a ranking problem. **The estate has six tools and no answer because nobody declared
which one answers this.**

Measured by the issuer at the cut (`87607a2a30`): `org/modules/graph/graph-call-manifest.yaml` carries **128
entries**, a **78-tool `tools_index`**, and **ZERO** ids beginning `cloud.inventory.`.

### WHAT YOU BUILD

**ONE entry**, id beginning `cloud.inventory.`, in the manifest's own shape:

- **The tool is R-81's assignment and not your judgment:** *which resources compose a subject ->*
  **`comp-find --corpus aws`** (src=full-derive 217 of 217; prints VINTAGE, DENOMINATOR and a per-node
  `drift_class` including `LIVE-no-DECLARED`). Its `canonical_call` must carry `comp-find --corpus aws`.
- **The 11 keys every entry carries:** `id`, `use_case`, `canonical_call`, `tool`, `mode`, `layer`, `cost`,
  `freshness`, `rebuild_trigger`, `anti_pattern`, `status`. 71 of the 128 entries carry exactly this shape and
  every other shape is a superset; read neighbours in the `cloud.*` namespace and match their register.
- **`status` must be an active one**, and `tool` must be a key of `tools_index`.
- **The `anti_pattern` field is where R-81's REFUSALS belong**: `comp-estate` (answers from a generated file
  whose regeneration is PARKED -- it cannot see a Lambda created since August), `comp-routes` (Terraform-plane
  only, ZERO AWS calls), and a DERIVE (`comp-aws`, deprecated for agent use by Andrew-direct: an agent reads
  the SERVED graph, never runs a derive).
- ⛔ **EXACTLY ONE `cloud.inventory.*` ENTRY.** Two would re-create the tie in the file meant to end it.
- ⛔ **EVERY PRE-EXISTING ENTRY IS BYTE-IDENTICAL.** `m1-untouched` re-computes a digest over the sorted
  `(id, sha1(canonical_call))` pairs of all 128 and requires it unchanged, and the count to be exactly 129.
- **Name the near-duplicates you considered.** Several entries mention AWS resources (e.g.
  `cloud.lookup.nodes_by_type`, `cloud.describe.resource`). Your record says which you compared and why each
  is a DIFFERENT use case. That list is what `LT-m-1`'s judgment criterion is graded on.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/R4_BASE.json`; this is a quotation of it)**

```json
{
  "entry": {"id": "<cloud.inventory.*>", "tool": "<the R-81-assigned instrument>", "near_duplicates_considered": [{"id": "<an existing entry>", "why_different": "<...>"}]},
  "repoint": {"legs": ["<leg>"], "authorization_instrument": "<comp-iam live|reconcile|simulate>", "hand_surfaces": [{"file": "<path>", "treatment": "GUARDED|DECLARED", "guard_or_declaration": "<the comp-lambdamap run, or date+owner+un_defers_when>"}]},
  "coverage_delta": {"by_node_type": {"<TYPE>": {"round3_involved": 0, "round4_involved": 0, "dropped": [{"name": "<node>", "old_leg": "<leg>", "why_not_reached": "<...>"}]}}},
  "run": {"run_id": "<the new run>", "registries_unchanged": true},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

**You fill the `entry` and `stale_proofs` blocks only** -- the other three belong to the cells on slot `~1`.
Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/MANIFEST_ENTRY_R4.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="M1R4-AC1" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py m1-entry</invocation><expect>PASS-M1-ENTRY</expect></criterion>

<criterion id="M1R4-AC2" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py m1-untouched</invocation><expect>PASS-M1-UNTOUCHED</expect></criterion>

<criterion id="M1R4-AC3" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_lt_r4.py r4-stale-proofs</invocation><expect>PASS-R4-STALE-PROOFS</expect></criterion>

<criterion id="M1R4-AC4" cell_refs="LT-m-1" judgment="true"/>

<expected_criteria>M1R4-AC1, M1R4-AC2, M1R4-AC3, M1R4-AC4</expected_criteria>

**AC1 AND AC2 READ FAIL AT THE CUT** (0 `cloud.inventory.*` entries; 128 where 129 is the bar).
⚠ **AC3 IS GUARD-SHAPED AND READS PASS AT THE CUT** -- the stale-proof bar's `git log` returns zero until a
fixed input moves; it measures nothing you build, and it is shared with the other round-4 orders.

**`M1R4-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the entry actually ENDS the tie --
that a reader with the inventory question lands on it and not on a neighbour -- and whether the
near-duplicates you named are genuinely different use cases rather than a list assembled to look thorough.

**THE CHECKER'S CONTROLS:** run `... check_lt_r4.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`
(21 arms, 8 positive-satisfiability). An arm a CORRECT entry cannot satisfy is a BLOCKING surprise row.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT ANY EXISTING ENTRY, the `tools_index`, the `contract` block or `retired_aliases`.** One addition, nothing else.
- ⛔ **YOU DO NOT TOUCH THE ENGINE** (`lib/opal_lgctfm.py`) -- that is `LT-e-6`'s, on the other slot, this round.
- ⛔ **NOTHING LIVE MOVES.** You may RUN comp-find/comp-which read-only to check your entry's call works.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged. Copy an existing row's field set exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **One other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/modules/graph/graph-call-manifest.yaml
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.5, round-4 cell `LT-m-1` (section 15).
<owned_cells>LT-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `M1R4-AC1` through `M1R4-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-m-1-r4.canonical-inventory-entry.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> M1R4-AC1,M1R4-AC2,M1R4-AC3,M1R4-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-m-1-r4.canonical-inventory-entry.md` BEFORE the `complete` flip.
Result file `canonical-inventory-entry.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`M1R4-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the entry as written, the near-duplicates you compared and why each differs, and the manifest's entry count and digest before and after.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut: no schedule is created or read.
comp-iam: RUN at the round-4 cut: no grant moves; the cell reads no IAM surface -- comp-iam appears only as a REFUSED discovery source named in the entry's anti_pattern.
comp-adversary: RUN at the round-4 cut: the adversarial control is m1-untouched paired with the exactly-one rule. The cheapest satisfying move for m1-entry is to widen or re-word a NEIGHBOURING entry so it appears to answer the inventory question; the digest refuses any edit to the 128 pre-existing entries, and the one-entry rule refuses a second cloud.inventory.* id. r4-stale-proofs is guard-shaped and disclosed.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~2/ by the tree convention. The manifest has ONE writer this round.
contention: the channel is shared with slot ~1 -- append-only, 14b's inversion applies, no slot isolates there.
</preflight>

Seating: slot `~2`, level 0, the only order on its slot. Round 4 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.5 s.15, from R-81's cell one as the L10 analysis re-affirmed it. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/` (`check_lt_r4.py`, `R4_BASE.json` pinning `87607a2a30`). Rulings carried: R-81, NFRA_GRAPHS AC1, S32.
