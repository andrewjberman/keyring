# The coercion was never ours — the vendor ships the damage, so the repair belongs at our boundary and must be arithmetic, not lexical — 0.4.0_DS_ClientPlatform~Y

**Date:** 2026-08-29
**Task Order:** ETFS_POSITIONING.TO-13-DS.identifier-coercion-strips-leading-zeros
**Status:** BLOCKED — code COMPLETE and committed; all four ACs need a deploy that is not this lane

---

## Objective

Stop leading zeros being stripped from `cusip` before `silver/holdings/`, so ABT reaches
Bloomberg as `002824100` instead of being routed to `/sedol/2824100` and returning nothing —
without breaking ICT and MER, two genuine SEDOLs sitting in the same 7-character bucket.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "where is silver/holdings parquet written from bloomberg etf constituents"` | PARTIAL | Returned a near-tie (comp-estate / comp-pipescript, 1.50 each) and correctly declined to rank them. Routed me onward but did not locate the writer. |
| comp-find | `comp-find 'constituents_issuer_fill' --all`, `comp-find 'silver/holdings' --all`, `comp-find 'cusip' --files` | PASS | Decisive, and it killed a wrong hypothesis: 13 hits/27949 files found `etf_constituents_pull.py:231`, which I had assumed was the silver producer. Reading it showed `leg_2_issuer_fill` **reads** silver/holdings — downstream, not upstream. `--all` throughout; no census headed. |
| commit-gate.sh | `bash .tools/commit-gate.sh <2 files>` | PASS | rc=0, 2 of 2. First run flagged one non-ASCII line (U+26D4) I had introduced; WARN-only, fixed anyway — the CLAUDE.md rule is the imperative and the gate is only its partial enforcement. |
| safe-commit.sh | `--author "0.4.0_DS_ClientPlatform~Y <...>" -F <msgfile> -- <paths>` | PASS | 3 commits. Risk-reflex CLEAN, measured: 2 files vs 1417 danger nodes. msg-verify MATCH each time. |
| proof-of-spec-check.py | `python .tools/proof-of-spec-check.py <instance> POS-TO13-AC1..AC4` | PASS | rc=0 VALID, violations=0; alignment forward 4/4 and 3/3, backward 3/3. First run INVALID on a real defect of mine — `surprises` items must be strings, I filed objects. |
| comp-system | `comp-system` | PASS | rc=0, discharged the STRUCTURAL-TWOPHASE override in-session. |

---

## Work Completed

### 1. The TO's premise was wrong, and measuring bronze is what showed it

The face says "STOP THE UPSTREAM COERCION," which presumes something in our pipeline coerces
`cusip` numerically. Nothing does. Both parsers in the producing Lambda read the column with
`csv.reader` and only `.strip()` it — pure text. I checked the raw vendor bytes rather than
reasoning from the code: bronze is written byte-for-byte *before* any parse, and
`trueshares/DIVZ/bronze/holdings/20260828/divz_holdings.csv` **already carries `2824100`**.
The coercion is the TrueShares Google Sheet exporting an unformatted identifier cell as a
number. The conclusion of §5 survives — repair at source is still the only sound fix — but
"source" means our silver boundary, not a coercion site of ours.

**Finding bronze at all required the APPLIED state, not the source.** The module defaults say
`BRONZE_BUCKET=S3_BUCKET` / `GRAMMAR=legacy`; the deployed environment says `opal-data-assets`
/ `monolith`. My first fetch used the code's answer and returned `NoSuchKey`. Reading the
deployed config is what put me in the right bucket.

### 2. The fix: two checksums, and the ORDER is the mechanism

`_repair_numeric_coerced_cusip` at `holdings_rows_to_parquet` — the single choke point where
`cusip` and `id_kind` are both written, so the stored identifier and its classification cannot
disagree. §2 of the face is right that no lexical rule splits the 7-char bucket. Arithmetic does:

```
  ABT  2824100  -> 002824100 passes CUSIP mod-10 . NOT a valid SEDOL  -> REPAIRED
  ICT  6455819  -> no padding passes CUSIP mod-10 . VALID SEDOL       -> untouched
  MER  B247XZ6  -> no padding passes CUSIP mod-10 . VALID SEDOL       -> untouched
```

Rule 17 holds without destroying anything: `cusip_as_delivered` carries the vendor bytes
verbatim and `cusip_basis` {as-delivered | zero-pad-restored} is the claim field a consumer can
reject on. Bronze untouched (17a).

### 3. Blast radius measured by exercising the router, not reading it

Exactly **one query in the estate changes**: ABT `/sedol/2824100` -> `/cusip/002824100`. The
four 8-char rows emit byte-identical strings (the `len==8` pad becomes a no-op, left in place
per §5); ICT/MER identical; RTX identical. AC2 therefore holds at the *query* plane, not just
storage.

### 4. A second vendor instance found, filed, and not chased

RTX arrives as `7.55E+105` — the same class by a different mechanism: the sheet read the `E`
in `75513E101` as a scientific-notation exponent and rounded the mantissa, destroying the
identifier rather than shortening it. Filed to the surprise channel (16748) as
OBSERVATION/INERT; `3.0.0_SA_CVO~Z` adjudicated (16754) and closed my one open limb by
measurement. I later closed the *path* question at source: `bbg_security` gates on
`c.isalnum()`, false for `7.55E+105`, so RTX falls through to the ticker query.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Repair at the silver parse boundary, not in `bbg_security` | §5 forbids widening the length heuristic, and bronze must stay raw (17a). The boundary where vendor bytes first become a typed row is the only remaining place. |
| Gate on **two** checksums with SEDOL refusing first | A CUSIP-check-only gate is unsafe prospectively. I exhibited five valid SEDOLs (`BBB0135` and four more) whose zero-padding also satisfies CUSIP mod-10 — a check-digit-only repair rewrites all five into fake CUSIPs. |
| Preserve the delivered value in a new column rather than overwrite | AC1 requires mutating `cusip`, but Rule 17 forbids dropping vendor data. Adding `cusip_as_delivered` satisfies both and makes the repair reversible. |
| File all four ACs **UNCOMPUTABLE**, not PASS | Every AC names an artifact that needs a deploy. AC1 says *in the criterion* "score by reading the row, not the writer's log" — I exercised the writer's logic, which is precisely the excluded evidence class. |
| Route the deploy to the issuer, not to an AE lane directly | `0.7.0_AE_CloudOps~Z` is live but encumbered; choosing a seat would be doing `2.0.0_SA_COO~Z`'s staffing. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py` | `_sedol_check_digit_ok` + `_repair_numeric_coerced_cusip`; wired at the row build; `cusip_as_delivered` + `cusip_basis` added to `HOLDINGS_COLUMNS` | Yes — `353c4b5a00` (LOCAL) |
| `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/test_to13_cusip_repair.py` | New mutant-style suite; exhibits the SEDOL/CUSIP collision set | Yes — `353c4b5a00` (LOCAL) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_POSITIONING.TO-13-DS_PROOF_OF_SPEC.json` | Instance, VALID, 4 rows UNCOMPUTABLE | Yes — `406ca98415` (LOCAL) |
| `infra/system/06_current_state.{md,json}` | comp-system recompile discharging the override | Yes — `1d7d5706ee` (LOCAL) |

---

## Blockers

**Lane, not effort.** Lambda code deploy is Terraform-only (CLAUDE.md NEVER) and infra is a
DT/AE lane (Rule 13). All four ACs need the deployed artifact; AC4 additionally needs a
*scheduled* fire, and today is Saturday — the face fences weekend scoring and AFTER == BEFORE
on a non-advancing day is the expected outcome, not a regression.

**The fix does not ship alone.** The deployed function is already behind the repo
independently of my change (deployed 69897 B, `CodeSha256 6RFz1jbz...`, LastModified
2026-08-25; repo 72296 B before my edit). The pending delta is another seat's Z-S31
`RunDateFabricationGuard`. Divergence confirmed real, not the CRLF false-divergence class:
CR count 0 in both files.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| None | — | The deploy handoff went as an MCP message to `2.0.0_SA_COO~Z` (cc `3.0.0_SA_CVO~Z`) rather than a brief, since it is a staffing call on an existing TO, not a new interface contract. |

---

## Current State

Code complete and committed; proof-of-spec VALID with every criterion honestly unscored.
Three commits, **all LOCAL** — measured via `ls-remote`: origin/SITEZ is `e998abbfa6` and
`git branch -r --contains 353c4b5a00` returns empty. Push is the integrator's (LD-0367).
No override outstanding: the `STRUCTURAL-TWOPHASE/proof-of-spec` override taken at
`406ca98415` is discharged at `1d7d5706ee`.

**What this does NOT close, and the number is `3.0.0_SA_CVO~Z`'s:** ~1 in 10 future
doubly-stripped CUSIPs will be SEDOL-valid, be refused repair, and silently retain the ABT
failure. It fails in the safe direction — a refused value is left exactly as today's code
leaves it — so the fix is better everywhere and worse nowhere, but it repairs the unambiguous
cases rather than closing the class. Recorded in the function's own docstring so it is not
rediscovered as a surprise.

---

## Next Steps

1. `2.0.0_SA_COO~Z` staffs the Terraform deploy to a DT/AE lane, carrying the Z-S31 warning.
2. After deploy, re-score AC1/AC2 by **reading** the next `silver/holdings` partition.
3. After the next scheduled fire, re-score AC3/AC4 — naming the fire by date, and resolving
   the trading calendar first. Expect the 0-of-8 population to be **five**, not six;
   `2602335D` must remain null.
4. Open and unowned (my stated bounds, which `3.0.0_SA_CVO~Z` declined to round off): whether
   RTX's stored value differs on other dates, and whether PFDE/PFOE carry the same class.

---

## What I got wrong, kept because the mechanism transfers

- **I walked into a trap the face had explicitly warned me about.** §7 records that a prior
  probe printed "ABT ABSENT on every date" because it selected the wrong ticker column. I
  wrote `"holding_ticker" if in columns else df.columns[0]`, the fallback silently grabbed
  `date`, and I got `RTX ABSENT / ABT ABSENT / AEP ABSENT`. Reading the warning was not the
  same as applying it; a fallback branch answers under the original label.
- **My first instinct was that the coercion was ours.** It was reading the *raw vendor bytes*
  rather than more of our code that settled it. When the question is "who damaged this
  value," the artifact that predates every one of our parses is the only thing that answers.
- **I filed `surprises` as structured objects because I skimmed the schema.** I read
  "item required=None" as "free shape"; the items are strings. The checker caught it, and its
  own output warns that the alignment figures it prints on an INVALID instance look identical
  to a valid one's — worth remembering before quoting them.
