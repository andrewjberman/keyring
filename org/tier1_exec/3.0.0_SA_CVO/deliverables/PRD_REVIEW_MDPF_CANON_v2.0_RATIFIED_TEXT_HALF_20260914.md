# PRD REVIEW -- MDPF_CANON v2.0 @3514843a12 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96549.

**Read, UTC 2026-09-14 ~08:5xZ:**
- The PRD `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @`3514843a12`. The working copy is identical to the pin. The old path `docs/architecture/MDPF_CANON_PRD.md` is now a moved notice.
- The endpoint `ENDPOINT_FWD_D8_MDPF_CANON_MIGRATION_20260913.md` @`e2210bf34c`, its last commit, read whole: "FIVE THINGS THE CUT SURFACED" and the ~18:4xZ ruling stamp.
- `org/standards/NAMING_SCHEMA.json` v1.2's `key` block.
- `LGIC_NAMING` v1.2 S1.
- `LGIC_ENFORCE` v1.1: `key()`, `address()` and the fence.
- `infra/logic/02_DOCTRINE.md` R1, R4, R7, R21 and the ledger's X2 row.
- This PRD's DEC-3 (brief half), read only for where the final-step obligations land.
- `sequence-check.py --project MDPF_CANON`: stage 2; its hold is MET, because `LGIC_ENFORCE` v1.1 is admitted. No flags.

**Half hash reviewed:** ratified-text `aa9f141401d833e50c3a35f6934ded8266ebd0b6e4bc43e70dce7eef200e5f92`. It matches the
notifier's `aa9f141401d8`.

## VERDICT: REFUSE -- one change, R1, in CONTRACTS. The ENDPOINT holds.

## ENDPOINT -- 8 of 8 outcomes carried verbatim; every removed constraint lands in CONTRACTS

**Instrument:** a parser over both documents' FWD blocks, field by field, against the endpoint @`e2210bf34c`.
- **Title and ACCEPT:** EQUAL for FWD-1 through FWD-8.
- **DONE WHEN:** EQUAL for 7 of 8. FWD-8 differs only by the endpoint's inline marker *"⚠ INHERITS THE SIBLING'S DECOMMISSION STANDARD"*, which is an annotation.

**The four kinds of removal the preamble states are each right, and each operative constraint they carried survives in
this half:**

| removed from ENDPOINT | where the constraint now sits in this half |
|---|---|
| FWD-2's and FWD-6's `DEPENDS` (*"that firm's own storage existing and able to serve -- the sibling migration's delivery, per firm"*) | CONTRACTS *"each firm's bucket and its serving grants"*: consumed, produced by `ADVI_FIRMBKTS` per firm, and *"FWD-2 and FWD-6 wait on it for that firm"* |
| FWD-8's inheritance marker | CONTRACTS *"the decommission standard"*: 45 CONSECUTIVE days; a named instrument; no earlier than its observed-live stamp; any event restarts it; counted only once every reader is repointed. This agrees with the window ruling on `ADVI_FIRMBKTS`'s tree row @`9819855eda` (96488) |
| the `(s.N)` pointers | history -- rightly out of the section (`CANONICAL_FABRIC_WORKFLOW_20260901.md:165`) |
| the `PRD ACn` pointers | mapped in DEC-3; AC9 is KEPT as a control beneath FWD-5 |

**FWD-6's "word for word what it was before" is made precise in this half.** The separation-rule row requires no
exemption row, no carve-out, and the rule's bytes identical before and after the run. The dedicated-runner row names
its principals by `name()` (`mdpf-49f-runner-role`), so the scope slot carries the firm, which is what
`LGIC_ENFORCE`'s fence admits.

**Nothing ruled sits outside the outcome block unmet.** The endpoint's stamp closes the quiet window (card 2), approves
read logging (card 3), and rules the fence (card 1). All three are carried. *"Which project builds the runner's host"*
is still a question, not a constraint.

## CONTRACTS

### R1 (blocking) -- row 1 claims every string comes from the builders, and two of its own instances cannot

**The claim.** Row 1 (*"the canonical key string, MDPF's instances"*): *"Every string comes from `LGIC_ENFORCE`'s
`key()` and `address()`, never typed."*

**What the builders produce.** `LGIC_ENFORCE` v1.1 fixes them:
- `key(source, scope, tier, table, partition)` returns exactly `{source}/{scope}/{tier}/{table}/{partition}` -- five segments;
- `address(..., object)` returns `s3://{bucket}/{key}` with the object as the leaf.

**What the row lists, instance by instance:**

| instance, as row 1 writes it | can the builders produce it? |
|---|---|
| gold `s3://opal-data-mdpf/mdpf/{scope}/gold/{artifact}/date={YYYY-MM-DD}/data.parquet` | yes -- five segments plus the object |
| bronze `s3://opal-data-assets/mdpf/{scope}/bronze/{feed}/...` | yes |
| state `s3://opal-data-mdpf/mdpf/{scope}/state/...` | yes, as the tier `state` (R21) |
| a firm's served slice `s3://opal-data-{firm}/mdpf/{firm}/platinum/{leaf}.json` | **NO.** Four key segments; the builders emit five, then the object. `address()` would return `.../mdpf/{firm}/platinum/{table}/{partition}/{leaf}.json` -- a different path from the one this row names |
| the combined slice `s3://opal-data-portal-v2/platinum/mdpf/global/...`, "unchanged" | **NO.** It is TIER-FIRST, which doctrine R1 supersedes everywhere (`02_DOCTRINE.md:88-95`), and `key()` never produces a tier-first string |

**No upstream text defines the platinum form.**
- `LGIC_NAMING` S1 says only that *"a platinum leaf is a kebab `.json`"*.
- `NAMING_SCHEMA.json` lists the partition as *"date=YYYY-MM-DD"* or *"a named leaf"*.
- `LGIC_ENFORCE` gives no platinum example.

So nothing ratified says how `key()` spells a four-segment served leaf.

**Why it blocks.** These are SERVED keys: the portal reads them, and row 3 requires the served JSON byte-unchanged across
every cutover. Either:
- a builder-derived path moves served output away from the path this contract promises; or
- the path is typed, and the row's own rule is broken on the first key that matters.

Both are the same contradiction `LGIC_ENFORCE` v1.0's R2 was refused for.

**Fix, touching only this row:**
- **(i) The firm's served slice.** State the exact `key()` / `address()` call that yields the path, naming which argument carries `{table}` and which `{partition}`. Or, if the grammar cannot express a four-segment served leaf, write the builder's real output here, and note that the served-path move is covered by the never-widen sign-off DEC-5 and M9 already carry for the home move. Either way, the row and the builder must agree on one string.
- **(ii) The combined slice.** Take it out of the "every string from the builders" claim, and name it as what it is: a legacy tier-first key this project deliberately leaves untouched (the SURFACE MANIFEST excludes it). It stands under the ledger's X2 row, which must then cover its key order as well as its portal-v2 home.

### Also checked -- these rows hold

- **The gold artifact, the served platinum JSON and the combined slice's basis:** produced, and coherent with FWD-1, FWD-4 and FWD-3.
- **The scoped route:** the router's firm map is `LGIC_ENFORCE`'s generated view, and that project lists the edge router among its generated views.
- **The separation rule:** it matches `LGIC_ENFORCE`'s fence row (a scope-derived Deny; a principal whose name carries the firm is admitted).
- **The decommission standard:** it matches 96488.
- **Inherited law:** every cited canon rule (R4-R7, R11, R12, R16-R19, R21) exists in the doctrine.
- **The firm's bucket and grants:** NOT EVALUATED -- `ADVI_FIRMBKTS` has no PRD yet.

### N1 (non-blocking) -- the three final-step obligations are not named in this half

Andrew's ~20:5xZ 08-25 obligations are quoted in the preamble:
1. the silver-to-gold seams;
2. the publisher repoint;
3. the code homes.

They are carried in the brief half: DEC-3 keeps AC9 as a control beneath FWD-5, and cells M4, M5 and M6 carry the
rest. FWD-4's and FWD-5's ACCEPT lines cover (2) and (3) in substance. Adding (1) to FWD-5's ACCEPT would change
ratified text, so carrying it as a control is right. Naming the three in the inherited-law row would put them in the
half this seat signs; it is not required.

### N2 (non-blocking, and not this project's to fix) -- the law still spells platinum homes tier-first

Rule 17b (`CLAUDE_ANNEX.md:415-416`) and doctrine R7 (`02_DOCTRINE.md:155`) still write the platinum homes as
`opal-data-{firm}/platinum/` and `opal-data-portal-v2/platinum/`. That is tier-first, against `LGIC_NAMING` S1's
source-first rule for every bucket. It is how R1's combined-slice instance comes to look lawful. It is the law
surface's to reconcile: 17b's text moves only on Andrew's word, and doctrine R7 is `4.0.0_SA_CRO`'s.

## NOT CLAIMED

- **The brief half** -- DEC-1 onward, the cells, paths, coverage and surface manifest. That half is `4.0.0_SA_CRO`'s.
- **That the four-segment platinum form is wrong.** Only that this PRD and the builders do not yet agree on it.
