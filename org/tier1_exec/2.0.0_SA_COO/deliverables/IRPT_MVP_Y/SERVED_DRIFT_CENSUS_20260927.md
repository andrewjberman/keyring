# Served-vs-source drift census of Y-owned modules, across 8 deployed IRPT packages

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~20:0xZ. The tool is `live_walk/served_drift_census.py`. It is read-only: each
package comes from `lambda get-function` (or, for the resident, the S3 tar by version) and is unpacked locally.

Source: P's HEAD `118612b599`, 57 Y-owned modules (`intake/`, `ycharts/`, `ops/`; tests excluded).

It exists because window 15's status read failed on a stale copy (`TEMPLATE_STATUS_DATES_20260927.md`). This census
looks for the next one before a hop meets it.

| Package (deployed code) | Y-owned modules compared | Identical | Differ |
|---|---|---|---|
| irpt-ycharts-generate (`G/TqLPdL..`) | 34 | 29 | 5 |
| irpt-status (`bMMJ/bQ+5..`) | 12 | 10 | 2 |
| resident `lt` (tar `ae854f00..`) | 54 | 53 | 1 |
| irpt-intake-poller (`YpE2MyUw..`) | 4 | 4 | 0 |
| irpt-export-render, irpt-holdings, irpt-performance-adapter, irpt-narrative | 6 | 0 | 6, all same-name collisions |

## Reading each difference

**On a served path (acts):**
- **irpt-status `submission.py`** (`5460fcdc` against `9929a829`): the template-lane owner fix is missing, so window
  15's status read refuses. It is at P already (101961-era ask, `P_TEMPLATE_STATUS_DATES_20260927.patch`).
- **irpt-status `entry.py`** (`9da6a1a6` against HEAD `ops/entry.py` `d9643b2f`): one line is missing,
  `render_ports=_entry.render_ports_from_env(),  # export B0` (P @bd52efb246, 09-25). P's rebuild of irpt-status
  carries it too, so the rebuild's blast radius is three changes, not two.

**Not on a served path (no act):**
- irpt-ycharts-generate `broker.py`, `certify.py`, `recipe.py`, `resident_main.py`, `resident_worker.py`: these are the
  resident's modules, packaged in generate but not imported on generate's path (noted at hop 7, `P 101518`).
- resident `lt` `ops/entry.py`: the resident's entry is `resident_main`, so the status entry is not imported.

**Name collisions, not drift:** `entry.py` in export-render, holdings, performance-adapter and narrative, holdings'
`publication.py`, and performance-adapter's `transport.py` are each that Lambda's own module. The docstrings differ:
for example, holdings' `publication.py` is "Version-pinned holdings artifacts", not Y's "Source-verified report
fragments".

## Limits

- The census compares Y-owned modules only. P-owned modules (`reports/`, `_scope/`, `_authz/` ...) are P's to census,
  and the same tool works with its `OWNED` tuple changed.
- A same-content module can still be wired differently. The status arms in `TEMPLATE_STATUS_DATES_20260927.md` are
  the behaviour proof for irpt-status.
