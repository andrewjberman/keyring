# The apply leg found the build input was wrong before it shipped — ETFS_INGEST.TO-9-AE — 0.7.0_AE_CloudOps~I

**Date:** 2026-08-28
**Task Order:** ETFS_INGEST.TO-9-AE
**Status:** COMPLETE
**Session:** 01:38Z - 02:30Z  (TWO applies)

## Objective

Deploy the `etf-positioning-producer` Lambda package carrying `ETFS_INGEST` TO-6 (gold emits
`industry_group`) and TO-8 (publisher serves it), gated on both having landed, ahead of the ~13:00Z
scheduled fire. Terraform only; `aws lambda update-function-code` banned.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "is the deployed Lambda running the same bytes as the package I built, and what is its CodeSha256"` | Near-tie across `comp-aws` / `comp-closure` / `comp-estate`; named `comp-closure` as the identity+support-closure compiler. Used it. |
| `comp-closure` | `comp-closure compile etf-positioning-producer --out <scratch>` | `equivalence=DIVERGENT`, `eq_deployed_commit=false` on 2 of 2 members, `live CodeSha256 != artifact_sha256`. **The verdict was right and the obvious reading of it was wrong** — the divergence was the SOURCE MAP being stale, not the deploy being drifted. |

**What worked:** `comp-closure` gave the four planes (SOURCE / DESIRED / APPLIED) and per-member
digests in one call, and its `last_deployed_commit` vs `repo_at_deployed_commit_sha256` disagreement
is precisely what exposed the stale map. It did the hardest read of this TO.

**What failed:** nothing failed, but `comp-closure` compares only against `last_deployed_commit` and
`HEAD`. The deployed package matched **neither**, so the tool could report DIVERGENT but could not
name the real vintage. That took a content-based sweep across history (deployed member sha256 ->
git blob) which no comp-tool does.

**Gap found:** no comp-tool (a) enumerates a Lambda package's zip members, (b) reads an S3 object's
user metadata, (c) enumerates a Lambda LAYER's contents, or (d) resolves a deployed blob to its
authoring commit by content. All four were load-bearing here and all four ran raw with
`# rail-checked:` markers.

## Deployment Sequence

| # | step | evidence |
|---|---|---|
| 1 | Gate measured at this seat, not relayed | `63a68942ae` (TO-6) + `39495cf260` (TO-8) both ANCESTOR-of-HEAD and ON `origin/SITEZ`. Negative control `is-ancestor(TO-8, TO-6)` -> FALSE. |
| 2 | Baseline read | S3 `Metadata.content-sha256` == live `CodeSha256` == `pQ76SKsr...`. No undeployed artifact pending; no half-state inherited. |
| 3 | **DEFECT FOUND** | Deployed zip has 3 members incl. `etf_classifications_dynamodb.py`, **no BUILD_MANIFEST**, 2020-01-01 stamps vs the builder's 1980-01-01 -> the committed builder had never shipped. Its PACKAGE list omits the module `publisher:66` imports at module scope. |
| 4 | Builder fixed, in lane | `ac7243103f`. PACKAGE := the handler's import closure: gold, publisher, `etf_classifications_dynamodb.py`. Dropped `trading_calendar.py` (layer supplies it) and `lambda_function.py` (never imported). |
| 5 | Ledger OPENED | `dd75f6bd64`, before the first world-touching act. |
| 6 | Built at pin | `--pin ac7243103f` -> 131255 B, sha256 `93f016ba7172b526...`, 4 zip entries. |
| 7 | Uploaded + verified on the primitive | `s3api put-object` with `--metadata content-sha256=k/AWunFy...`; `head-object` confirms 131255 B and the metadata. VersionId `.2FAC4L6xOys6F4yBB_5gmVN0KnC8cUR`. |
| 8 | Plan (read-only) | `0 to add, 1 to change, 0 to destroy`. |
| 9 | **APPLIED** | `.tools/safe-apply.sh` 02:04:47Z -> `0 added, 1 changed, 0 destroyed`. |
| 10 | Re-plan | `No changes. Your infrastructure matches the configuration.` |
| 11 | Tagged | `etfs-positioning-v1.1.0` annotated, peels to `ac7243103f`. LOCAL only. |
| 12 | Source map corrected + ledger CLOSED | `40c6b6f9d7`. |

## Verification

    CodeSha256    pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=
               -> k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=    MOVED, direction recorded PRE-READ
    LastModified  2026-08-28T02:04:47.000+0000    State Active
    UNCHANGED     python3.11 | 512 MB | 120 s | handler etf_positioning_gold.lambda_handler
    CONTENT       live package re-downloaded AFTER the apply; sha256 93f016ba7172b526...
                  == the artifact built at the pin. `cmp` byte-identical.
    DID-NOT-MOVE  9 managed resources, 1 changed, 8 unchanged INCLUDING
                  aws_cloudwatch_event_rule.etf_positioning_producer_daily -- the 13:00Z schedule.

`1.0.0_SA_CTO~Z`'s bar (a)-(d): all PASS. (c)'s discriminator — the built layout MINUS the added
member — returned `rc=1, line 66, in <module>, ModuleNotFoundError`, reproducing the exact
deploy-breaking failure.

## Decisions Made

1. **The member set was chosen to MINIMISE DELTA against a package known to work**, not to tidy the
   builder. The resulting package differs from the live working one only by the two files TO-6/TO-8
   changed, plus the inert `BUILD_MANIFEST.json`.
2. **Refused to decide the `trading_calendar` drop alone, then removed the need to decide** by
   measuring it: the layer's copy is byte-identical to `lib/` at HEAD, and the live working package
   contains no such member. Dropping it reproduces the live configuration.
3. **Did not fix two cosmetic builder defects** (inert `ZIP_DEFLATED`; wrong `layers_expected` in the
   manifest) because both would have changed already-verified artifact bytes for no functional gain.
4. **Wore the `~I` letter** through the `~I`/`~P` crossing rather than blocking; the issuer settled it
   to `~I` within minutes.

## Files Modified

| file | commit |
|---|---|
| `infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py` | `ac7243103f` |
| `org/critical_paths/change_management/20260828T0200Z_etfs-ingest-to9-ae-producer-package-to6-to8_deploy.md` | `dd75f6bd64` (OPEN), `40c6b6f9d7` (CLOSED) |
| `infra/aws/lambda/ci/lambda-source-map.json` | `40c6b6f9d7` |

## Blockers

**NONE at this seat.** The apply landed with the issuer's GO (11796) after the CTO bar (11792).

**Owned elsewhere, listed so they are not read as mine:**
- ~~`industry_group_basis` is NOT in the deployed package ... a second apply is required.~~
  **SUPERSEDED BY THE ADDENDUM BELOW -- the second apply landed at 02:26:49Z.** Left struck rather
  than deleted: it was true when written, and this section is the record of that moment.
- ~~`industry_group` is not in `portal/.../etfAdapter.ts:77 toCurrentHolding`, so it will not
  RENDER even once served.~~ **FALSE AS OF portal `8c2ba9bb` -- CORRECTED 2026-08-28T03:5xZ.**
  Re-measured at this seat rather than relayed: `etfAdapter.ts:85-86` carries BOTH
  `industry_group` AND `industry_group_basis`; positive control `sub_asset_class` = 2
  occurrences, and my local portal submodule IS at `8c2ba9bb`, so the vintage is verified and
  not assumed. `0.4.0_DE_ClientPlatform~Z` has wired it, basis included.
  ⚠ **MY ERROR WAS NOT THE FACT, IT WAS THE MISSING VINTAGE.** I relayed a cross-lane status
  claim measured by another seat at ~01:5xZ and restated it as current, in a committed carrier,
  with no `@<vintage>` attached -- so nothing in the sentence could be checked for staleness.
  `1.0.0_SA_CTO~Z`'s 11487 ruling covers exactly this. **A relayed measurement decays fastest,
  because every re-send restates it as current.** Struck rather than deleted: it was true when
  written, and the expiry is the point.
  ⚠ NOT claimed, then or now: that the field RENDERS. The adapter passes it through; the render
  is a further step and it is `0.4.0_DE_ClientPlatform~Z`'s to score, not mine.

## Current State

Deployed, verified on the live plane, ledger CLOSED, nothing half-landed. The ~13:00Z fire will run
these bytes. **What that fire produces is not claimed here** — TO9-AC5 forbids it and the served
census is TO-8 AC2's.

## Next Steps

- ~~Sequence the `industry_group_basis` follow-on.~~ **DONE -- see the addendum.** `2.0.0_SA_COO~Z`
  ruled (12038), and the second apply landed at 02:26:49Z.
- [`0.0.0_AB_MSTR~Z`] `etfs-positioning-v1.1.0` AND `v1.2.0` need an integrator push; `--follow-tags`
  is not mine.
- [`3.0.0_SA_CVO~Z`] Proof-of-spec instance filed alongside this log.

## Surprises (channel: `3.0.0_SA_CVO~Z`, class OBSERVATION, standing INERT — none chased)

1. **The committed builder had never shipped the live artifact** — a production Lambda whose serving
   package had no committed producer. Closed for THIS function only (the deployed zip now carries
   `BUILD_MANIFEST.json`); the general finding stands.
2. **`build_package.py`'s `ZIP_DEFLATED` is inert** — `writestr(ZipInfo(...))` honours the ZipInfo's
   own `compress_type`, default `ZIP_STORED`. Every entry is stored.
3. **The in-zip manifest's `layers_expected` is wrong** — names `mdpf-gold-calendar-deps`; the
   function attaches `opal-trading-calendar-layer:1`. Inert metadata, never read at runtime.
4. **A bare `git tag -a` records whoever committed last, not what you deployed** — my first tag cut
   landed on a peer's commit because HEAD moved under me in the shared tree. Caught while local-only.
5. **The halt gate is fail-closed on identity and this session had no serial file**, so the first
   `safe-apply` refused. Fixed by writing `org/mcp/sessions/<id>.serial` (gitignored) rather than
   overriding — the gate's own instruction, and the refusal text explains that a mis-identified
   pusher scans someone else's inbox.

---

# ADDENDUM -- THE SECOND APPLY (02:14Z - 02:30Z)

## Why there was a second one

    02:04:47Z   apply 1 lands at pin ac7243103f
    02:14:18Z   f0e2a05889 -- the publisher starts serving industry_group_basis
                DELTA 9m31s

`etf_positioning_publisher.py` is a package member, so the applied package could not contain it, and
`data/etfs/**` is not in the push gate's `CODE_TREES` -- the Lambda package is the only path.

**Found by `0.0.0_AB_MSTR~Z` from the CLOCK side** (they held the apply time and the commit time; no
other seat held both) and **independently by `0.4.0_DS_ClientPlatform~Q` from the RULING side.**
⭐ Those are not two confirmations of one finding -- neither checks the other. **This seat ran the
third and decisive instrument, CONTENT**, on a three-way discriminator DS~Q precomputed: the deployed
member hashed to the `39495cf260` blob, not `f0e2a05889`'s, and not to a third unposited state.

## Deployment Sequence (apply 2)

| # | step | evidence |
|---|---|---|
| 1 | Pin verified | `f0e2a05889` carries TO-6, TO-8 and the builder fix. gold + classifier byte-identical to the deployed members -- the delta is ONE file. |
| 2 | Built + full bar re-run | Not inherited: (a)(b)(c)(d) all re-executed on v2; (c)'s discriminator again returned `rc=1, line 66, ModuleNotFoundError`; (d) 32 edges, 0 unresolved; determinism byte-identical across two builds. |
| 3 | Content diff | `HOLDING_KEYS` arity 14 -> 15, `industry_group_basis` False -> True, removed members `[]`. Raw count 1 -> 3 (DS~Q forecast 1 -> 2 -- recorded as a discrepancy, and a live demonstration of why membership is the sound check). |
| 4 | Ledger 2 OPENED | `aac579ce42`, before the upload. |
| 5 | Uploaded + verified | 131900 B, `content-sha256 EiCjtNC...`, VersionId `hdlBjB6kFKqfZxQfYYheO1mse.nGH59.`. |
| 6 | **HELD AT THE GATE** | See below. The apply had NOT started. |
| 7 | **APPLIED** | 02:26:49Z -> `0 added, 1 changed, 0 destroyed`. |
| 8 | Verified + tagged + map advanced | Re-plan 0-diff; `etfs-positioning-v1.2.0` at `f0e2a05889`; source map advanced and cross-checked against the live plane. |

## ⛔ The hold, which is the part worth keeping

Between the build and the apply, `1.0.0_SA_CTO~Z` withdrew the AUTHORITY basis of ruling 11832 --
adding an AC to a frozen TO is the issuer's act under Rule 27, and they had taken it. Three legitimate
outcomes were named and **one of them, "rule the basis out", would have made my staged artifact the
wrong one.**

>> **I held.** The apply had not started -- the halt gate had blocked the un-acked run at `rc=1` --
so the decision was still genuinely ahead of the act and therefore cheap.

⚠ **Two seats were reasoning from "an apply is RUNNING", read off my own "STARTING NOW".** It was not
running. **Correcting that premise (msg 12056) was the load-bearing act:** it turned an
expensive-looking emergency into a one-line question. `0.4.0_DS_ClientPlatform~Q`'s instruction not to
stop was explicitly conditional on being mid-apply, so its conclusion did not apply to me.

**RESOLVED** by `2.0.0_SA_COO~Z` 12038 -- *"I AMEND `ETFS_INGEST.TO-8`. The basis field STAYS."*
`1.0.0_SA_CTO~Z` 12046 clarified they withdrew their AUTHORITY, never the SUBSTANCE, which is
CLAUDE.md law and not theirs to withdraw. **The staged artifact was correct and applied unchanged.
Nothing reverted, nothing wasted; the hold cost ~2 minutes against a ~10.5h margin.**

## Verification (apply 2)

    CodeSha256    k/AWunFytSaEsCs7p0HXCKZP3UntUbtMnA16HRkglIA=
               -> EiCjtNChLCKXRY/yUHrAVh3QXBsGfn2i3qHbsJN7QXI=    MOVED, predicted BEFORE the build
                  and independently pre-recorded by 0.4.0_DS_ClientPlatform~Q (11939), so the
                  prediction is on the record from a seat OTHER than the applier
    LastModified  2026-08-28T02:26:49.000+0000    State Active
    CONTENT       live package re-downloaded after the apply == the built artifact, cmp identical
    STALENESS     deployed publisher 23705449... == blob @f0e2a05889, NO LONGER == @39495cf260
                  -> 0.0.0_AB_MSTR~Z's finding discharged on the instrument that found it
    RE-PLAN       "No changes. Your infrastructure matches the configuration."

## Additional surprises from the second half

6. **`proof-of-spec-check.py` cannot see this decomp's cell ids.** `CELL_ID_RE:185` requires a
   lowercase tier segment, so all 37 `INGEST-Tn-m` ids are invisible; it reported an id space of 4
   (incidental refs to another decomp) and raised three FABRICATED-CITATION violations against
   citations that literally appear in the file. Positive control: `ETFS-d-1`/`STI-b-4` match.
   `2.0.0_SA_COO~Z` measured the blast radius at 2 of 7 TOs. **Ruling 12034: file the true citations,
   accept the INVALID, never edit a cell_ref to satisfy a grammar.** Filed under that ruling.
7. **Same tool prints `INVALID` and exits `rc=0`.** The verdict line is the oracle; rc is not.
8. **A ruling's AUTHORITY and its SUBSTANCE are separable** -- and only the first was ever in
   question. Withdrawing the first does not touch the second when the second is standing law.
9. **`TO8-AC6` attached a RUN-LEVEL clause to a PER-ROW cell** (`INGEST-T4-1`) and named no plane.
   Raised by `0.4.0_DS_ClientPlatform~Q` at 02:28:36Z -- after my apply -- and ruled by
   `2.0.0_SA_COO~Z` 12090: the gold manifest is correct, nothing moves, and the same answer moves
   `TO-6 AC6`. **No third apply.** The timing cost nothing: had it gone the other way it would have
   needed a publisher edit and a further apply whether or not I had already applied.

## Final state

Deployed at pin `f0e2a05889`, verified on the live plane, **both** ledgers CLOSED, source map
agreeing with the live plane, `v1.1.0` and `v1.2.0` tagged (local; tags are the integrator's push).
⛔ **The ~13:00Z fire will run these bytes. What it produces is still not claimed here** -- AC5, and
the served census is `TO-8 AC2`'s.
