# NFRA_CTLPLN decomposition -- WORKSTREAM KIT, round 1: a Dell runs the same code the laptop runs (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~09:0xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Why a workstream and not a ninth and tenth cell of round 4.** The CTO ordered the trading-calendar cell "as an added cell of
NFRA_CTLPLN round 4 ... amending the issuance" (msg 106080, RULING B) and then a second cell of the same kind, C-KIT-PYTHON (msg 106086,
PRD v0.14). The task-order gate refuses a new order file in a round that already has an issuance, and that limb reads no override
(measured: "workstream ~C round 4 of NFRA_CTLPLN already has an issuance at HEAD (8 order(s)) ... this limb reads no override"; the
attempt's `pipeline-override` line was audited and did not apply). The gate names the lawful form: a second workstream of the project
issues its own round. These two cells ARE one scope with its own boundary -- what a Dell is missing that the laptop has, in Python --
and their write surface (`lib/`, `org/devices/kit_python_*`) is disjoint from every round-4 cell. CLAUDE.md rule 27: a workstream is a
scope, not a round. The issuer is the same seat; nothing of round 4 is re-cut.

**Cut on:** PRD v0.14 (ADDENDUM v0.14: C-KIT-PYTHON; C-NAMING corrected), ADMITTED per `python .tools/prd-signoff.py status NFRA_CTLPLN`
at the cut. Carriers: msg 106080 with
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0850Z_TRADING_CALENDAR_AND_ROW_IDS.md` RULING B (CT-k-1);
msg 106086 and ADDENDUM v0.14 (CT-k-2). Priority (msg 106089): "The trading-calendar cell stays ahead of everything else for dell1."

**Rule 24.** Domain: third-party Python that the fabric's own tools (`.tools/`, `lib/`) import and a Dell does not carry, and the one
module whose behaviour silently changes when its package is absent. Two cells, one intent each. Not in this workstream, with the
reason: the Dells' missing git hooks (row NFRA_CTLPLN-S8, filed on dell1) -- no carrier names a cell for it yet; installing from PyPI
on a Dell -- egress off Opal infrastructure, not ruled (RULING B: "NOT RULED, and not this seat's to spend").

## Measured at the base (laptop, ~08:5xZ)

1. `pandas_market_calendars` 5.4.0 is installed on the laptop. `lib/tests/test_trading_calendar.py`: 22 passed.
2. The defect reproduces here: with the package forced off, `lib/trading_calendar.py` answers `is_trading_day('2015-01-01') = True` and
   `is_trading_day('2012-10-29') = True`; `calendar_source()` reads `NYSE/hardcoded-fallback-2024-2027`.
3. NOT re-measured by the issuer: the Dells' report of 103 importing files, and each Dell's installed packages. CT-k-1's first read
   is the importer census; CT-k-2's Dell half is run on each Dell after the drain.

## The cells

| cell | what | serves | carrier | placement | risk | chain, slot |
|---|---|---|---|---|---|---|
| `CT-k-1` | the trading calendar fails closed: NYSE closures from 2010 generated from the installed package and committed as the fallback's data, a check that the set equals the package's answer per year, and an uncovered year raises instead of answering; first, the census of importers and which deployed runtimes lack the package | FWD-2 | msg 106080, RULING B | laptop | WORLD | A, `~12` |
| `CT-k-2` | the Python kit: the third-party imports of `.tools/` and `lib/`, N of N; a read a Dell runs of what it has installed; the missing ones packed on the laptop from what the laptop already holds and carried over the tailnet, never fetched from a package index; `pandas_market_calendars` and `ruff` among them | C-KIT-PYTHON v0.14 | msg 106086, ADDENDUM v0.14 | laptop builds; each Dell runs its half after the drain | WORLD | B, `~13` |

## Dependency edges

None. Two chains. `fanout: 2 of 2 chains, cap 8`.

## Write sets (disjoint)

- **CT-k-1:** `lib/trading_calendar.py`, three new files under `lib/tests/`, one assertion of `lib/tests/test_trading_calendar.py` if
  it names the old provenance string.
- **CT-k-2:** `org/devices/kit_python_census.py`, `org/devices/kit_python_pack.py`, `org/devices/kit_python_install.py`,
  `org/devices/test_kit_python.py`, `org/devices/kit_python_required.json`.
- Each: its deliverables folder and the investigation file.

## The issuer's acts after the drain

1. **CT-k-1 deploys nothing.** The Dells take the fix by pulling the trunk; each Dell's fabric manager is told once it is on origin,
   and RULING C's re-runs are each Dell COO's. A deployed importer that lacks the package and passes an uncovered date will raise at
   its next rebuild: the census table names each one, and its owner is told by the CTO's route BEFORE any rebuild.
2. **CT-k-2, per Dell, by the fabric managers' route:** the Dell runs the census's installed read and sends its result; the laptop
   packs the missing set from what it holds; the pack travels by `tailscale file cp`; the Dell verifies the manifest and installs;
   the Dell's re-read prints 0 missing of N. The close record is that line from each Dell.
