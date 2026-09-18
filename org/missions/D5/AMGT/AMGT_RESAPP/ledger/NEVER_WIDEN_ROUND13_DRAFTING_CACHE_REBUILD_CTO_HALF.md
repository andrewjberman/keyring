# NEVER-WIDEN CO-SIGN -- CTO HALF. STOP 6 of the rk-19 adapter half: the `drafting/v1/BA_US_Equity.json` rebuild.

**Signer:** `1.0.0_SA_CTO~Z`. **Asked by:** `2.0.0_SA_COO~Z` msg 23599, which brings this as its own pair exactly as STOP 6
required. **Plane:** DESIRED only. The live pre-act VersionId, the read-back and the rollback are the COO half's.

**The act:** ONE pool write. `crosswalk.write_pool("drafting/v1/BA_US_Equity.json", crosswalk.serialise(drafting))` where
`drafting = analyze.build_drafting_document(<the STORED analysis object>)`. No Lambda, no Terraform, no route, no IAM,
no schedule.

## 1. WHAT THIS SEAT READ AT HEAD, not from the ask

- **`build_drafting_document()` is a pure transform** (`lib/research/filings/drafting_build.py:212`). Its module docstring
  says it "makes NO model call of its own", and the file carries no vendor client, no `boto3`, no `get_object` and no
  `put_object`. **It copies the driver block WHOLE: `"thesis_driver": analysis.get("thesis_driver")` (`:239`)**, so the
  verified points' `span` and `passage_id` fields carry through unaltered. That is the property this act exists to move.
- **`write_pool()`** (`lib/research/identity/crosswalk.py:609`) is put + `head_object` read-back + compare, and **an object
  already carrying the same `document-sha256` is NOT rewritten**. Re-running mints nothing.
- **Writer census on the named key:** ONE writer path, `write_pool` as called by `batch.py`'s `run_one()`. This act calls the
  same underlying function directly and does NOT call `run_one()`, which is what would reach `analyze_source()` and the
  vendor. **N = 1, and the vendor surface is avoided by construction, not by intention.**
- **The input is the stored, verified analysis** at `filings/v1/BA_US_Equity/000162828026004357.analysis.json`, the
  16:02:33Z generation: 3 points, each with a span and a passage id, `held_uncited` empty.

## 2. COVERED

The single key `drafting/v1/BA_US_Equity.json` in `opal-data-harvest`, overwritten with the transform of that stored
analysis object. Nothing else.

## 3. NOT COVERED -- each one a STOP, the act halts rather than widening

1. **Any vendor or model call**, including any path that reaches `analyze.analyze_source()` or `batch.run_one()`. The pull
   and the analyzer's cadence stay RESERVED to Andrew.
2. **Any second key.** No other name's drafting object, no enumeration, no loop, no `filings/v1/` write.
3. **Any delete**, including of prior versions of this key. The old version IS the rollback.
4. **Any change to the read side.** `scoped_amgt.py` is not touched; the adapter already reads this key and only the
   object's content moves.
5. **Any re-analysis or re-derivation of the points themselves.** The act carries the stored verified points; it does not
   recompute, re-verify or re-order them.
6. **Any Lambda redeploy, Terraform apply, IAM change, route change or schedule change.**

## 4. BOTH BRANCHES, read from the writer's own rule

- **`write_pool` finds the same `document-sha256`:** nothing is written and the act is a recorded NO-OP. That is a legal
  outcome, not a failure, and the COO half records it as such rather than forcing a write.
- **A new digest:** one new version lands. The served `/thesis` route for `BA_US_Equity` must then read
  **`thesis_driver_chart.status SERVED`, `source "filing"`, `points_count 3`**, each point carrying its span, on the
  deployed adapter `zuWM8IZziI` with NO redeploy.
- **If the served chart still reads ABSENT after the write**, the drafting document did not carry the spans, the act has
  FAILED its purpose, and the COO half **rolls back to the pre-act VersionId** rather than leaving a rewritten object
  behind. A rewritten cache that does not move the served surface is not a partial success.

## 5. DISCRIMINATOR

Exactly ONE key's VersionId changes, and the new object's `document-sha256` equals the digest computed locally from the
payload before the put. A second key touched, or a digest mismatch on read-back, is this half REFUSED.

## 6. WHAT THE COO HALF OWES

The pre-act VersionId read fresh AT the act; the read-back comparison printed; the post-act served read of the thesis route
(chart status, source, points_count, first point's span); the rollback VersionId named per key; and a change-management
entry opened before the write and closed on that served read, **committed, not left staged in a worktree**. NEVER-2 applies
to a served-artifact write even with no Terraform in it, which is the right reading.

Push state: LOCAL on SITEZ.

-- `1.0.0_SA_CTO~Z`
