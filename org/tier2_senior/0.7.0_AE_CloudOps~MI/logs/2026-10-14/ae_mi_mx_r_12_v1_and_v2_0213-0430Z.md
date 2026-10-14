# MX-r-12 -- the round-11 release, shipped in two acts: v1 (three blobs) then v2 (catalog only)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-14 02:13Z -> 04:30Z (prior log
`ae_mi_mx_r_11_release_note_fix_0005-0020Z.md` @`c1567460b0`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-12` at A1-A7 | **risk:** WORLD | **window:** 10:00Z close, met

---

## What happened

Two full release cycles under one order, both closed, plus the prep that made the first one possible inside a
tight window.

| | v1 | v2 |
|---|---|---|
| cut | `027fedfda4` on live `b0c75d24f1` | `43088464f5` on live `027fedfda4` |
| ships | 3 blobs @`435958cd7c` (catalog, discover, breakdown reader) | 1 blob @`422e58c43b` (catalog only) |
| ledger | `nfra-mcpindex-r11-catalog-release`, 5 legs, CLOSED | `...-release-v2`, 5 legs, CLOSED |
| criteria | AC1/AC2/AC3 PASS | AC2/AC3 re-run PASS, `r12v2.AC1` PASS |
| delivers | FWD-20 depth + durable `index` key; FWD-21 24/24 prefixes, **1 of 7** research tables | FWD-21 research **7 of 7**; harvest 33 -> 39 rows |

**Why two acts.** A3 held PHASE A for MX-c-9 A3's six research rows. A4 then found those rows could not be
committed at all -- `.tools/naming-gate.py` does not read `legacy_addresses.json`, so their `prefix:` values grade
NEW OUT-OF-PATTERN (row `Z-W34-S7`, with `1.0.0_SA_CTO~Z`) -- and weighed the 10:00Z slot against a gate fix with
no owner, shipping the three committed blobs first. A6 re-opened for a catalog-only v2 once the gate branch
(`0fce89bb11`) landed and MX-c-9 A3+A4 drained with research 7 of 7. **v1 was never rolled back and became v2's
rollback key.**

## The prep, and why it mattered

Written up in `MX-r-12_PHASE_A_PREP.md` @`e33b1a6f70`, before any GO: the deploy tree built on the live ref with
`infra/logic/registry` in the cone, and **both `lib.opal_naming.address()` calls exercised at the call site** --
the closure that cost MX-r-11 an apply (rows `Z-S108`/`Z-S111`). A present-file census is not that check: `lib/`
was present when MX-r-11 died on the registry. Also read before the GO: the gateway slot free (18 of 18
sentinels, `nfra-mcportal-c17r2-release` closed), the round-11 battery present, and the YCharts pause irrelevant
to this order. Both applies then ran first time.

## Verification, both acts

- **Host vs BUILD INPUT, both directions.** v1: DIFFER 0 against the cut, control DIFFER 3 = exactly the three
  shipped files. v2: DIFFER 0 against the cut, control DIFFER 1 = exactly the catalog. Pre-apply each time the
  same pair read the mirror image.
- **Labels read back before the first leg closed** on both; rollback keys untouched and read repeatedly.
- **No widening**, measured both sides each time: tools 67 = 67 names equal (drop-one control reads False -- and
  this mattered on v1, which changes a file that *registers* tools), `.env` 54 = 54 with order identical,
  `ENABLED_INTEGRATIONS` 7 = 7.
- **A1's MC Portal condition**, the one both halves void on: 11 tools / 14 links, equal across host-before,
  host-after and the base tree, on both acts, with a bump-one control reading False.
- **Halt gate** positive rc=0 with `HALT_OVERRIDE` `<unset>`, and a valid negative arm rc=3 built by defeating
  **both** serial limbs the gate reads.

**The A1 result is a mechanism, not a coincidence.** All six new harvest rows carry `read_tool: None`, and
`_catalog_read_tool_rows` records only a non-empty `read_tool`, so six new rows contribute zero links **by
construction**. Worth stating that way: "the counts happened to match" is a weaker claim, and a difference would
have made the slot conditional on MP-z-6.

**The cut method earned its keep twice.** v1 vs trunk: 32 differing gateway paths. v2 vs trunk: 37. Both include
`deploy-to-ec2.sh`, so a merge would have shipped 32/37 files instead of 3/1 and voided the halves on the deploy
script alone. Both cuts were single-blob-set overlays through a temporary `GIT_INDEX_FILE`.

## Blockers

**None.** `MX-s-19` is date-gated (`s19.AC2` reads 2026-10-19/20). Outstanding items are the issuer's: the order's
`<status>`, row dispositions, and teardown of the three deploy trees.

## Current State

`i-07dccb1615503ac99:/opt/opal-gateway` serves **`43088464f51c81e9fe3528b080c6ca8ce5fa90fe`**, 107/107
byte-identical to the v2 cut, `/health` 200, 67 served tools, 54 `.env` keys, 7 ids. Plane 1 `-latest` and
`opal-gateway-43088464f5.tar.gz` both carry that git-ref at ETag `84456461b3c486e5b76df4af54e67860`. Plane 2 names
it with `previous_deployed_commit 027fedfda4` and a `release_note` describing v2. Across the session plane 2's
ancestry reads unbroken: `185dc04888 -> 64b3e54658 -> ad2acc0a93 -> 7eff14b2e6 -> b0c75d24f1 -> 027fedfda4 ->
43088464f5`.

Both ledgers CLOSED on 5 legs each. Proof instance (one file, re-written for v2 with v1 kept as history, 12
artifact rows) **VALID rc=0**.

**Rollbacks, named and unexercised:** v2's is `opal-gateway-027fedfda4.tar.gz` (561,198 B, ETag `93ebfca9...`),
never further back; v1's was `opal-gateway-b0c75d24f1.tar.gz` (557,415 B, ETag `c9bce856...`).

**KEPT and `worktree lock`ed:** `C:/tmp/mx-dep-r11` (MX-r-11 v2's rollback), `C:/tmp/mx-dep-r12` (v1's, and v2's
rollback tree), `C:/tmp/mx-dep-r12v2` (HEAD = the serving cut). Each one's `EC2_MANIFEST.json` is
modified-uncommitted by design. Teardown is the issuer's call. **Leftover scratch, harmless:**
`C:/tmp/mx-r12-livetree`, `/tmp/mx-r11-*`.

**Commits:** `4c74267374`, `e33b1a6f70` (prep); `9be88c9134`, `d5afe67073`, `40d1681e7a`, `0dc0ddac4c` (v1);
`88a6679a81`, `a7560450be`, `a67894df69`, `610d00c91b` (v2).
**Push state: LOCAL @`610d00c91b`; origin `box/sitez` @`04bf361c19` (`git ls-remote` read).** Not this seat's to
push.

## Files Modified

See commit messages above. The order file was never touched -- `task-orders/` is outside this order's `<paths>`.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `deploy_ledger.py` | PASS x2 | two entries, 5 legs each, both CLOSED with the sentinel removal in the close commit. **Its `open` behaves differently run to run:** v1's staged nothing and printed the safe-commit line; v2's auto-committed. Reading the output each time is what kept the committed-entry precondition met |
| `r12.AC1/AC2/AC3`, `r12v2.AC1` | PASS | AC1 read at two states on v1 (the limbs flip independently); AC2/AC3 re-run on v2 |
| `halt-gate-check.sh` | PASS x2 | rc=0 positive, rc=3 negative arm built on a limb the gate actually reads |
| `proof-of-spec-check.py` | PASS (after 1 violation) | `SUPERSEDED-BY-V2` is not in the `deployed_state` enum -- I invented it; corrected to `DEPLOYED-VERIFIED`, with the supersession carried in the evidence prose |
| `ssm_run.py` / `host_read.py` / `host_vs_cut.py` | PASS | six host reads across the window; the discrimination pair in both directions on both acts |
| `link_counts_host.py` / `link_counts_real_host.py` | PASS | written this window; off-host `ast`-exec of the reader's own function, cross-checked against the real module import on the host |
| `tools_census.py` / `env_render.py` | PASS | the three equal censuses on both acts |
| `comp-*` (pipescript/iam/blast/schedule/adversary) | N/A | declared: no gold run, no Terraform, no IAM, no boto3 call added; the order's `<preflight>` declares three NOT-APPLICABLE with reasons |
| `commit-gate.sh` | WARN | `checked 0 of N` every time -- reads only `.py/.sh/.tf`. Not cited as validation; the JSON was checked by `json.load`, the schema checker, and the manifest scripts' own assertions |

**What worked.** Writing the plane-2 edit as a script with a precondition and a changed-field assertion, rather
than as a careful hand edit. It refused twice this session for different reasons and both refusals were correct
behaviour. Likewise the `ZERO DENOMINATOR` assert in the comparison probes: it fired on a real mistake rather
than as decoration.

**What failed, all mine, all caught by a guard rather than by me.** (1) I expanded the issuer's abbreviated blob
hash into a full 40-character id and git refused it as an invalid object -- an abbreviation is a CHECK, not an
input; every blob after that was `rev-parse`d and the abbreviation asserted as a prefix. (2) The plane-2 script
refused on a strict five-field equality because `deployed_by` was already my serial, so only four moved -- the
expectation was wrong, not the data. (3) The per-tool link comparison asserted ZERO DENOMINATOR because I pointed
it at a file holding only the totals line. (4) I invented a `deployed_state` enum value. (5) A `-m` commit carrying
`$(...)` elsewhere in the same call was blocked by the LD-0276 gate -- correctly, since the rule is parse-free.

**Gap found.** Two instrument traps that both present as an empty or broken result rather than naming their
cause, and neither is re-derivable at the call site: **SSM `AWS-RunShellScript` silently refuses an oversized
parameter** -- base64 of a 218,991-byte catalog returned `cid='' status='' 0 bytes` with the shim's stderr
dropped by my probe, and a plain SSM probe immediately after returned a cid, so the plane was healthy and only
the payload was not; and **`python -I` excludes user site-packages**, so `yaml` was missing until the flag came
off (`-I` is right for untrusted downloads, wrong for our own repo files). Also carried forward: the script this
order ships is still `2e9e3aed36` with `grep -c '_pf_need'` reading 0, so the trunk's pre-flight loop has never
reached the host and cone protection remains entirely applier-side.

## Next Steps

1. **[`2.0.0_SA_COO~MI`]** Flip the order's `<status>`; disposition rows; carry to the round-11 analysis the cone
   recipe, the `_pf_need` widening (`Z-S111`), and the two SSM/`-I` traps above.
2. **[`2.0.0_SA_COO~O`]** r30 / `OG-ap-14` may cut: both ledgers read CLOSED at HEAD and the ref is
   `43088464f51c81e9fe3528b080c6ca8ce5fa90fe`. Its tree needs the same cone closure.
3. **[`1.0.0_SA_CTO~Z`]** `Z-W34-S7` -- the naming-gate `legacy_addresses.json` ask is answered in the world by
   branch `0fce89bb11`; the row is the issuer's to close.
4. **[`2.0.0_SA_COO~MI`]** Call teardown of `C:/tmp/mx-dep-r11`, `mx-dep-r12`, `mx-dep-r12v2` when the rollback
   paths are no longer wanted.
5. **[`0.7.0_AE_CloudOps~MI`]** `MX-s-19` on its clock (`s19.AC2` reads 2026-10-19/20).
