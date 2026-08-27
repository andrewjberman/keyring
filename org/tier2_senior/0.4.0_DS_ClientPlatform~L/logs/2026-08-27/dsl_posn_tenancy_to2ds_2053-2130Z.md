# Session — `0.4.0_DS_ClientPlatform~L` — POSN_TENANCY TO-2-DS

**Serial:** `0.4.0_DS_ClientPlatform~L` (site Z, lane inbox `org/mcp/inbox/0.4.0_DS_ClientPlatform/~L/`)
**Window:** 2026-08-27 ~20:53Z – ~21:15Z
**Project:** `POSN_TENANCY` (Rule 27). GO from `2.0.0_SA_COO~Z` msg 10032; TO `<issued_to>` names this
lane correctly @`f1c83161bd`.
**Archetype:** MEASUREMENT (read-only substrate) + one LATENT-defect observation.

---

## Objective

Discharge `POSN_TENANCY.TO-2-DS`: establish Cottonwood's Positioning presence **at the served key**
with a complete listing and a positive control, and report whether the Positioning consumer
distinguishes a MISSING key from an EMPTY artifact. Read-only — no build, no S3 write.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | *"which S3 bucket and prefix is the served key … and how do I list a prefix completely"* | RUN — and it is **why raw `s3api` is legal here**. Returned a NEAR-TIE (`comp-kuzu`/`comp-parity`/`comp-whoread`) and printed its own *"TOP SCORES ARE TIED — THE ORDER IS NOT A RANKING"*. None lists an S3 prefix, so Rule 21's exception condition was **met, not assumed**; every raw `aws` call carries a `# rail-checked:` marker naming this. |
| `comp-routes` | `behaviors`; `trace` on 3 paths | RUN. **This produced the served key rather than my inferring it**: `/api/general/*` → `S3-opal-data-portal-v2-json`, rewrite `/api/general/ → json/`. Also **discriminated the `model.json` rival** by showing the same S3 origin as its neighbours. Declares its own plane **DESIRED**, so presence was then taken live. Caught an MSYS leading-slash mangle in my argument and reported the corrected read. |
| `comp-find` / `comp-estate` | `'positioning_data.json' --all`; `--resource positioning` | RUN, **orientation only, explicitly not evidence** — top hits were `compproof` records of past investigations with laptop paths naming `opal-data-portal-v2`, conflicting with the PRD's `opal-data-assets`. That conflict is *why* the key went through `comp-routes`. |
| `.tools/aws` (rail-checked exception) | `list-buckets`, `list-objects-v2` (manual pagination), `head-object` | RUN, read-only. 31 buckets; 5 listings totalling **19,403 keys over 28 pages**, every one terminating `IsTruncated=False`; 1 discriminating head-object pair. |
| `.tools/commit-gate.sh` | on `posn_probe.py` | RUN, rc=0 (Rule 14). |
| `proof-of-spec-check.py` | 4 ids, positional | RUN, **rc=1 INVALID** — cause in the TO, see Blockers. |

## Work Completed

### 1. The served key, resolved then measured on two planes

`comp-routes` (DESIRED) named `s3://opal-data-portal-v2/json/positioning/positioning_data.json`;
`s3api` (LIVE) measured it. **Three keys in the served Positioning prefix and no firm dimension in
any of them** — the artifact is a single unscoped object.

### 2. Complete listings, exhaustion PROVEN

Auto-paginate **merges pages and drops `IsTruncated`/`NextToken`** — it removes the exact field AC1
asks to see — and `KeyCount` reads absent for every prefix. So each page was fetched
`--no-paginate` and the loop terminates **only** on `IsTruncated == False`. `--max-items`/`head`
appear nowhere.

| prefix | pages | terminal `IsTruncated` | keys |
|---|---|---|---|
| `opal-data-portal-v2/json/positioning/` | 1 | False | 3 |
| `opal-data-portal-v2/json/` | 1 | False | 954 |
| `opal-data-cot/` | 7 | False | 6,599 |
| `opal-data-49financial/` | 12 | False | 11,847 |

### 3. Three positive controls, because the verdict is an ABSENCE

The decisive one: **Cottonwood's own home is NON-EMPTY** — one instrument reads **6,599** objects out
of `opal-data-cot` and **0** are Positioning. So the absence is neither an empty bucket nor a blind
credential, and both halves of `PT-b-3` are measured by the same probe.

### 4. Two traps caught, either of which would have moved the answer

- **GRAIN** — `position` matches **922 of 6,599** in Cottonwood's home (`positions_cube.py`,
  `canonical_positions.py`, `0_composition.json`): the **canonical positions** pipeline, a different
  grain from the portal's **Positioning** artifact. A naive census returns 922 and **inverts** AC2.
- **SUBSTRING** — `firm` returned 2 hits, both false; it matched inside
  `mullin-confirmation-hearing.json`.

### 5. AC3 answered from source at a re-derived vintage

`MISSING → throw` (`portal-proxy.ts:94`→`:112`) vs `EMPTY → resolves` (`:115`→`:1133`→`:42`
`if (!rec) return rec`). **They differ, but incidentally** — a byproduct of `!response.ok`, not a
contract, and the MISSING branch collapses into one `Error` string shared with auth failure.

## Decisions Made

1. **Resolve the served key on the rail, not from records.** Two records disagreed; a third
   instrument settled it.
2. **Manual pagination over auto-paginate** — the criterion asks for the field auto-paginate deletes.
3. **Did not make my instance match the broken extraction.** Adding a backtick would satisfy the
   string-compare and still fail resolution — loosening a gate that fires correctly.
4. **Demoted my own best finding.** The `model.json` 404 looked like a live breakage until the caller
   check returned zero.
5. **`PT-c-2` left PARTIALLY OBSERVED** though all four criteria passed — criterion verdicts are not
   cell states.

## Files Modified

| Path | Change |
|---|---|
| `.../deliverables/POSN_TENANCY.TO-2-DS_MEASUREMENT_20260827.md` | NEW — the measurement record + `cell_status` |
| `.../deliverables/POSN_TENANCY.TO-2-DS_PROOF_OF_SPEC.json` | NEW — 4 rows |
| `.../deliverables/posn_probe.py` | NEW — the probe, committed so every count is re-derivable |

`2be92878c0` (3 files, 441 insertions) + `56b22c36a7` (placeholder fix).

## Briefs Written

The measurement deliverable above, carrying the `cell_status` block the schema has no slot for.

## Blockers

**One, not mine to clear, and it did not block the measurement.** `proof-of-spec-check` → **rc=1
INVALID**, 2 violations. The instance is **structurally valid** (jsonschema, 4 rows); both violations
say the instance and the TO disagree about the decomp path — **because the checker extracts the TO's
path with a leading backtick.** Proven by a one-variable test on the extractor, same path both times:

| `<decomp_ref>` notation | extracted | resolves |
|---|---|---|
| prose + backticks (this TO) | `` `workflows/…/DECOMP.md `` | **False** |
| bare path (`TO-F3-DS` precedent) | `workflows/…/DECOMP.md` | **True** |

**Same class as the `<issued_to>` prose-notation defect in `org/XXX.md`.** Fix is one notation change
in the TO — `2.0.0_SA_COO~Z`'s write. **Second time today a machine-read field on a TO addressed to
this lane was written as prose**; different field, same author-side cause. TO-2-DS's own
`<issued_to>` names me correctly, so that half did not repeat.

## Current State

**TO-2-DS DELIVERED.** AC1–AC4 PASS; reported to `2.0.0_SA_COO~Z` (10170) cc `3.0.0_SA_CVO~Z`
(10171), `1.0.0_SA_CTO~Z` (10172), `0.0.0_AB_MSTR~Z` (10173) — **4 DELIVERED / 0 QUEUED / 0 REFUSED,
denominator 4.**

**Push state:** `2be92878c0` **ON ORIGIN**, `56b22c36a7` **LOCAL** — read `2026-08-27T21:14:19Z`
against `origin/SITEZ=2be92878c0e39e9b9c5222840236dc6c5e9cd946`, negative control fires.

⚠ **The shared checkout moved under me twice mid-task** — workspace HEAD between two consecutive
calls, and portal `8b8a2cc775` → `4a52439cbe` between reading `portal-proxy.ts` and citing it. Every
`file:line` in AC3 was **re-derived at the current commit**, not carried forward.

Nothing held by me. Nothing owed to me.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<decomp_ref>` notation fix, then re-run the checker; and the TO close.
2. **[`3.0.0_SA_CVO~Z`]** The four OBSERVATION/INERT items if the channel wants them carried.

## Surprise-channel items — OBSERVATION / INERT, to `3.0.0_SA_CVO~Z` cc `2.0.0_SA_COO~Z`

**(a) A served key referenced by client code does not exist — LATENT, not live.**
`portal-proxy.ts:1381` fetches `positioning/model.json`; `head-object` 404 against a 200 control.
**I almost filed it as a live breakage** — `getModelData` has **zero call sites** (2 code occurrences
across 1,069 tracked portal files, both in `portal-proxy.ts`; every other hit a doc), and the
portal's own docs record the call being **deliberately removed** for performance. The docstring's
*"Lambda: checks X-User-Tier"* would have explained the 404 benignly — **that rival was checked and
excluded via `comp-routes`, not assumed away.**

**(b) The TO mandates `cell_status`; the schema forbids it** (`additionalProperties:false`, no slot).
Same class the schema's own `:41` comment documents for `decomp_ref`.

**(c) The shared checkout moved under me twice.** See Current State.

**(d) `PT-b-4`'s two prefixes** were traversed by the AC2-b sweep. Seen, not acted on.
