# AMGT_RESAPP round 22: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T07:3xZ at HEAD `4448891379`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND22_L8_PACKET_20260922.md` @`218ff3c994`; the six orders; the channel census
(37 carriers, 10 open before this document); read-only instruments from this seat over production code, live IAM and
the live bucket.

**Late, and why.** The packet arrived 05:52Z and was not read until ~07:05Z: this seat's inbox Monitor expired at
~01:0xZ and the session was not re-armed. `2.0.0_SA_COO~Z` (msg 24149) and `0.0.0_AB_MSTR~Z` both caught it.

## Round state

**6 of 6 terminal** (rk-87 Lusha silver writer, rk-88 SERP writer, rk-89 PROD promote, rk-90 M1, rk-91 M2, rk-92 M3).
Acceptance **PASS 47 / FAIL 0 / UNVERIFIABLE 0 of 47 over 6 orders**; the order files carry 47 criterion ids
(7+7+7+9+9+8); **judgment census 0 of 6.** The only open order in the project is rk-49 (held on the key rotation).

## The three moves retire their old paths -- measured on three planes, not taken from the packet

v0.17 C-FORMAT-SEQUENCE defines "retire": readers switched, writers stopped, read grant removed, no S3 delete.

| move | old path, live | new path, live | old read grant | production readers of the old path |
|---|---|---|---|---|
| M1 `raw/bloomberg/` | 119 objects, 0 delete markers | `bloomberg/harvest/bronze/` 110 (+ 9 state) | absent | 0 |
| M2 `filings/v1` `.source.json` | 194, 0 delete markers | `filing_source` silver | absent from the adapter | 0 (the writer `fetch.persist` routes to silver; `pool_key` survives only with suffix `analysis`, which stays at `filings/v1` by design) |
| M3 `raw/seekingalpha/` | 18, 0 delete markers | `seeking-alpha/harvest/bronze/` 18 | absent | 0 |

Code census: 3,074 production `.py` files; the four hits on the old prefixes are a help string (`batch.py`, about
`.analysis.json`), a provenance string (`crosswalk.py`), a dead constant (`roster.py` `FILINGS_PREFIX`, used nowhere
else) and `fetch.pool_key`, documented as never dereferenced for source. The served adapter reads no `filings/v1` path
(`scoped_amgt.py` reads `filing_source` silver through the generated `_harvest_prefixes`), so removing its grant denies
no served read. **The old objects remain as inert data -- no reader, no grant -- so no duplicate path serves beside the
new one**, which is what Andrew's shadow-pipeline veto forbids.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S370",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "L9 GRADE RECORD for round 22: 6 of 6 terminal, acceptance 47/0/0 of 47, no judgment criterion; moves M1-M3 retire their old paths on every plane (no production reader, no read grant, no delete) and the adapter reads no filings/v1 path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 4448891379: 47 criterion ids over 6 orders; parser reads the same; judgment=\"true\" in 0 of 6; --acceptance --round 22: PASS 47 / FAIL 0 / UNVERIFIABLE 0 of 47.",
        "Live S3: raw/bloomberg/ 119 and 0 delete markers, bloomberg/harvest/bronze/ 110; raw/seekingalpha/ 18 and 0, seeking-alpha/harvest/bronze/ 18; filings/v1/ .source.json 194 and 0.",
        "iam get-role-policy: neither reader policy grants raw/bloomberg, filings/v1 or raw/seekingalpha; the scoped-api policy grants bloomberg/harvest/bronze, sec/harvest/silver, seeking-alpha/harvest/bronze and filing_attempt.",
        "Code census over 3,074 production .py files: no reader of the three old prefixes; scoped_amgt.py reads filing_source silver via _harvest_prefixes (:123, :1954-1960)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "v0.17 C-FORMAT-SEQUENCE: a move copies with vintage, then switches readers, stops writers and removes the read grant in one window, with no S3 delete.",
    "world_is": "Measured so for all three moves.",
    "notes": "Grade carrier only.",
    "dismissal_reason": "Grade record: this row carries the round-22 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S371",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "GRADUATED: the PRINT route serves a 500 for all three validation names (CAT, CSL, 6861) -- render_pack sorts model-block fiscal years stored as a mix of str and int; pre-existing, not caused by M3.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S215 (2.0.0_SA_COO~Z): /api/scoped/amgt/security/{key}/print returns 500 for CAT, CSL, 6861 and 200 for BA and COST; render_pack.py:264 sorts historical years stored as str ('2016'..'2025') with forecast years as int (2026, 2027).",
        "Reproduced box-side on pre-M3 code @a74268ba4d (packet s.2 item 4)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Every served route answers for the validation names.",
    "world_is": "The print route fails for exactly the three names managers will open first.",
    "notes": "Remedy, round 23's first cell (pre-ruled by 1.0.0_SA_CTO~Z): sort on a normalised key in render_pack, an adapter redeploy under a pair with the binding closure check; producer-side string normalisation rides chain G. Manager-visible.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S215"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S372",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "GRADUATED: the SERP primitive's records carry no per-page tag, so a multi-page harvest cannot give each silver row its exact page_bronze_key.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W88-S1 (worker ~88): harvest_serp's per-row page_bronze_key (order item 5e) cannot be set exactly when more than one page is fetched."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Every silver row carries the bronze key it came from.",
    "world_is": "True for one page; unknowable per row across several.",
    "notes": "Remedy, holder 2.0.0_SA_COO~Z: the cell that wires the SERP writer uses max_pages=1 or refuses; rk-88 is code-only and off, so nothing has been written wrongly.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W88-S1"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S373",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "GRADUATED: GATE 5 resolves a command's target repository with a no-whitespace pattern, so on this device -- whose workspace path contains a space -- it can mis-resolve the repo a DT command targets.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S209 (from the rk-89 DT promote): GATE 5 reads `git -C <p>` / `cd <p> &&` with a no-whitespace pattern; this workspace is C:/Users/Opal Bloomberg/Desktop/ajb_workspace."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A gate reads the repository a command actually targets.",
    "world_is": "A quoted path with a space defeats the pattern on this box.",
    "notes": "Remedy, holder 1.0.0_SA_CTO~Z (the gate): parse the quoted argument, not a whitespace-free token. The path-with-a-space class is a known device trap here; a gate that silently mis-reads it applies the wrong rule, which is worse than refusing.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S209"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S374",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "DISMISSED: seven round-22 rows remedied or recorded in-round -- two issuer-text invocation defects, a DT order licensing an act its gate refuses, a row-id shape, an artifact-version count, a disarmed test clash, and AC7's false-positive closure check.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W90-S1 (a nonexistent deploy_ledger flag) and W90-S4 (safe-apply refuses `plan`): issuer-text defects, amended per 1.0.0_SA_CTO~Z msg 24133 and re-graded with no live act re-run.",
        "W90-S2: disarmed by W90-S5 (paths widened by exactly the one test file). W92-S1: disarmed by W92-S2 (the closure check's runtime package set corrected @081792416a; AC7 then passed 4 of 4 before any deploy).",
        "S208: rk-89 licensed a DEV sync as a PULL that GATE 5 admits only as a PUSH; the promote completed (PROD 6dfc33909e = tag portal-v2.1.182). S210: a row-id shape the gates refuse, recorded in S211. S212: three artifact versions against one named; the 'one or more builds' wording is now standard."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row's named defect.",
    "world_is": "Each is remedied, amended or recorded at HEAD.",
    "notes": "W90-S1/S4 and S208 are the bar-authored-without-measuring class (C-S335) applied to invocations and licences.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W90-S1",
      "AMGT_RESAPP-Z-W90-S4",
      "AMGT_RESAPP-Z-W90-S2",
      "AMGT_RESAPP-Z-W92-S1",
      "AMGT_RESAPP-Z-S208",
      "AMGT_RESAPP-Z-S210",
      "AMGT_RESAPP-Z-S212"
    ],
    "dismissal_reason": "Remedied, amended or recorded in-round; no standing hazard."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S375",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T07:35Z",
    "one_line": "L9 GRADE of M2's incidents: the adapter served live 500s twice (S214, W91-S3) and one exposure never fired (S213). The seat's own DISMISSED is upheld -- a served 500 leaves no stored state to re-open, and the guard is built.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S214: 4 live 500s at CodeSha256 ZZ4/pEXN from a lib.opal_naming import outside the adapter closure; W91-S3: a second 500 window from the fix itself; S213: a grant add and redeploy before the copy, 0 invocations. PROD gated to Andrew, third-party traffic 0 (packet s.2 item 2).",
        "Guard: the adapter imports GENERATED new-grammar constants (_harvest_prefixes.py, built from address()), and a pre-deploy closure check binds every adapter order (1.0.0_SA_CTO~Z ruling (c)); rk-92's AC7 ran that check 4 of 4 before its deploy."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Rule 22's negative mirror: an INCIDENT needs the guard built AND whatever the gap admitted re-opened.",
    "world_is": "The guard is built and binding; a served 500 writes nothing, so nothing was admitted to re-open.",
    "notes": "Recorded because an incident is graded at L9, not closed by the seat that filed it; the self-set disposition is upheld on the merits, not superseded.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S214",
      "AMGT_RESAPP-Z-W91-S3",
      "AMGT_RESAPP-Z-S213"
    ],
    "dismissal_reason": "Incident with no persisted admission; guard built and exercised."
  }
]
```
