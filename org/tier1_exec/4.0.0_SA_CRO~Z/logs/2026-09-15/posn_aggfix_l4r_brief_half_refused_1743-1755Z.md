# 4.0.0_SA_CRO~Z -- L4-R POSN_AGGFIX PRD v0.1: brief half REFUSED on one defect, 17:43-17:55Z 2026-09-15

**archetype:** VALIDATE

## Delivery

Msg 23189 came from 1.0.0_SA_CTO~Z at 17:43Z. It delivers POSN_AGGFIX PRD v0.1 @d6bee5693c (drained 2832fc7ce3) for L4-R:
- the ratified-text half to 3.0.0_SA_CVO~Z;
- the brief half to this seat.

`prd-signoff.py status` routes both halves to `~W` lanes alphabetically. POSN is `~Z`'s by Andrew's word, so the
delivery is correct. Earlier in the window, msg 23181 had confirmed L2 @acc47518c1: FWD-5 retired, FWD-9 added.

## What was reviewed, and with what

- **Pin.** The PRD's last touch equals the pin. The brief `half_hash` is `f044e8d31d...`, the same at the pin and on
  the working copy.
- **s.8 BRIEF COVERAGE.** The denominator matches: 31 heading lines in the brief @1e268c164e, 30 non-title, and
  every line reference in s.8 matches the census. Every row carries content, not a pointer.
- **Surface rows checked at source:**
  - producer lines for S6-S8 (`:1421`, `:1437-1451`, `:1461`, `:1525`, `:1811`, `OUTPUT_KEY` `:2529`, upload
    `:2618-2636`);
  - S9 `iam.tf` S3ReadWrite, bucket-wide;
  - the S10 module at `lambdas.tf:162-172`;
  - the standards file's keys against `dim_mdpf_aum_metrics.py:84-91`.
- **S4 scope, on a different instrument from the CTO's comp-find.** A native ripgrep over `infra/aws` finds tier
  references in `auth-validator-edge` and `shared-advisor-router`, and none in `public-data-router`. That is
  consistent with the row.

## The defect found

- **Source.** The producer writes every model book's `aum` from the same weight dict that the aggregate's weights
  come from (`lambda_function.py:1796-1798` @ec29ae6fae).
- **Served.** A full walk of the served `positioning_data.json` found exactly 6 values equal to a legacy AUM figure:
  5 book-level `aum` fields inside the five model books, plus `AGG/total_aum`.
- **The collision.** C-CURRENT-SOURCE re-points the weight read, so those 5 values must change. That contradicts
  C-FIVE-BOOKS-UNCHANGED's "byte-identical" (PRD `:176-177`), S6's bound (`:248`) and S8's bound (`:250`). The PRD
  as written binds the decomposition to an unsatisfiable pair, so the verdict is REFUSE rather than sign with a note.
- **Scope of the fix.** No Models-mode reader of a book-level `aum` shows up at portal origin/PROD edf85ce503, at
  text grain, with a positive control. So the ratified FWD-8 is probably unaffected, the fix is brief-half only,
  and the CVO's signature survives it.
- **Recommended fix,** which is the CTO's call: scope byte identity to every field except the five book-level `aum`
  values, and name those in C-NEVER-WIDEN's blast radius.

## Acts, each read back after it landed

| act | artifact | read-back |
|---|---|---|
| review record | `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/POSN_AGGFIX_PRD_v0.1_BRIEF_HALF_REVIEW_20260915_Z.md` @3cb4034158 | in HEAD; pure ASCII, LF |
| stamp | `prd-signoff.py refuse POSN_AGGFIX --half brief --review <record>@3cb4034158 --expect-half-hash f044e8d31d... --reason ...`; the tool committed `prd/signoff/4.0.0_SA_CRO~Z.json` @7ffc16301a under this serial | status: ratified-text SIGNED (CVO~Z, current), brief REFUSED (CRO~Z), PRD WITHHELD; the file carries verdict, half_hash, review_ref and reason |
| carrier | 1.0.0_SA_CTO~Z inbox, file 20260915T175253Z (send receipt: filesystem + broker + channel push) | receipt only in this log |

## Compiler Tools

| Tool | Result | What worked / what failed / gap |
|---|---|---|
| `python .tools/prd-signoff.py status POSN_AGGFIX` | before: both halves MISSING, owed by `~W`; after: ratified SIGNED, brief REFUSED, WITHHELD | Worked. **Gap:** it still routes the owed half to `~W` alphabetically. Known and recorded in memory; not this seat's to fix. |
| `prd_signoff_lib.half_hashes` (imported) | brief `f044e8d31d...` at the pin and on the working copy | Worked. It gave the exact value for `--expect-half-hash`. |
| `python .tools/prd-signoff.py refuse ... --expect-half-hash` | STAMPED, committed 7ffc16301a | Worked. The tool commits its own sign-off file through safe-commit under `OPAL_AGENT_SERIAL`. |
| native Grep over the producer and `infra/aws`; `git -C portal grep` at origin/PROD | line matches as above; 15 tier files; 0 Models-mode book-level `aum` readers | Worked. The portal grep ran at the PROD ref, not the stale local checkout. |
| python walk of the served JSON (scratch copy, gzip-aware) | 6 legacy-AUM values, 116 aum-named keys | Worked. This walk discriminated the defect. A reading of the PRD alone could not have. |
| `.tools/safe-commit.sh` (review record) | 3cb4034158, msg-verify MATCH | Worked. |

## Current State

POSN_AGGFIX PRD v0.1 is WITHHELD. The ratified-text half is SIGNED; the brief half is REFUSED by this seat on one
defect, with its fix recommended. All commits are LOCAL: origin/SITEZ reads 6f09a06dc9 by ls-remote at 17:52Z. This
lane holds 0 open task orders.

## Blockers

None at this seat. v0.2 is 1.0.0_SA_CTO~Z's.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** v0.2 answering the refusal by pinned line. A brief-half-only change leaves the CVO's
   signature current.
2. **[4.0.0_SA_CRO~Z]** Re-read the changed brief-half rows at v0.2, then sign or refuse again with
   `--expect-half-hash`. Event-driven off the inbox Monitor.
3. **[4.0.0_SA_CRO~Z]** Re-arm the inbox Monitor on its expiry notice, due about 18:02Z.
