# TO ADVI_COTBKF.TO-CB-a-1 -- round 1 CB-a-1: the bronze landing tool for the Commonwealth delivery (one zip, byte for byte, with its manifest)

<to_id>ADVI_COTBKF.TO-CB-a-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~1</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-a-1` (`decompositions/ADVI_COTBKF_DECOMP.md`) | **outcome_ref:** FWD-1
(FWD-2's first file) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-a-1`, hop 2 of the round-1 thread: the Commonwealth delivery's portfolio-accounting zip goes to Opal's bronze store exactly as it
was shipped, with a manifest beside it. You build the TOOL and prove it with a dry run on the real file. You write NOTHING to S3: the
`--apply` run is the issuer's act after your branch drains.

**The input, measured at the base.** `$HOME/Downloads/Files.zip` (Git Bash; on Windows `%USERPROFILE%\Downloads\Files.zip`), 3,218,239,946
bytes: the Box download, Andrew's only copy. READ IT, NEVER MOVE, RENAME OR WRITE IT. It holds five zips. The one this cell lands:
`Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip`, 23,833,956 bytes, SHA-256
`a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b`, with three members under
`CFN_SCTASK0548380_Portfolio_Accounting_Performance/` (Historical_Positions 48,610 bytes; Historical_Transactions 308,186,603;
Historical_Performance_TWR_Cumulative_NetofFees 8,513,299).

**Build `data/assets/scripts/bronze/commonwealth_landing.py`:**
1. CLI: `--source <path>` (the outer Box zip), `--member <name as shipped>` (the inner zip to land), `--table <bronze table>`
   (`portfolio_accounting` for this member), `--data-date 2026-06-23`, `--received-date 2026-10-06`, `--apply` (default OFF = dry run).
   Device-free: no path, user name or drive letter in the code (LD-0405); every path arrives as an argument.
2. Read the member's bytes out of the outer zip UNTOUCHED (never unpack the inner zip in bronze, doctrine R9). Compute its byte count and
   SHA-256, and list its own members (path and uncompressed bytes) from its central directory.
3. Keys come ONLY from the naming builder (rule 30; never type a bucket or key):
   `sys.path` the repo's `lib/`, then `from opal_naming import address`;
   `zip_prefix = address('commonwealth','cottonwood','bronze',<table>,'date=<data-date>')` and
   `manifest_prefix = address('commonwealth','cottonwood','bronze','manifest','date=<data-date>')`. The zip's key is
   `<zip_prefix>/<member name as shipped>`; the manifest's key is `<manifest_prefix>/manifest.json`.
4. The manifest (the decomposition's LINEAGE CONTRACT, exactly):
   `{"delivery": "commonwealth/cottonwood", "data_date": "2026-06-23", "received_date": "2026-10-06", "files": [{"name_as_shipped",
   "bytes", "sha256", "bronze_key", "members": [{"path", "bytes"}]}], "builder": {"zip_prefix", "manifest_prefix"}}`. A later run for
   another member of the same delivery ADDS its file to the existing manifest (read it first under `--apply`); it never drops one.
5. Dry run: print the plan (each key, bytes, sha256) and, as the LAST line, exactly
   `LANDING-PLAN bytes=<n> sha256=<hex> keys=2 builder=OK apply=False`.
6. `--apply` (written and unit-tested here, never run by you): `put_object` with `ChecksumAlgorithm='SHA256'`; before the put, `head_object`
   the key -- absent: put; present with the SAME size and SHA-256: SKIP with a line saying so; present and DIFFERENT: REFUSE with rc 2 and
   write nothing. After the put, read back size and checksum and REFUSE (rc 3) on any mismatch. The S3 client is injectable so the tests
   use a stub.
7. Tests `data/assets/scripts/bronze/tests/test_commonwealth_landing.py` (pytest; build a small outer zip holding an inner zip in `tmp_path`):
   manifest fields and SHA-256; keys equal `address()` output; the three `--apply` branches (absent -> put; same -> skip; different ->
   refuse rc 2, nothing put) and the read-back mismatch (rc 3) on a stubbed client; a second member ADDS to an existing manifest.

### ACCEPTANCE

<criterion id="CB1-AC1" cell_refs="CB-a-1"><invocation>python -m pytest -q data/assets/scripts/bronze/tests/test_commonwealth_landing.py</invocation><expect>passed</expect></criterion>
`CB1-AC1` -- the tool's behaviour on a fixture: manifest, keys from the builder, put / skip / refuse / read-back mismatch, manifest append.

<criterion id="CB1-AC2" cell_refs="CB-a-1"><invocation>python data/assets/scripts/bronze/commonwealth_landing.py --source "$HOME/Downloads/Files.zip" --member "Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip" --table portfolio_accounting --data-date 2026-06-23 --received-date 2026-10-06</invocation><expect>LANDING-PLAN bytes=23833956 sha256=a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b keys=2 builder=OK apply=False</expect></criterion>
`CB1-AC2` -- the seam with the real neighbour: the dry run on the real delivery plans the true bytes and SHA-256 under the builder's keys.

<expected_criteria>CB1-AC1,CB1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no AWS call of any kind** (the tests stub the client). The apply is the issuer's act under a ledger entry.
- **The input is read-only.** Never write into `Downloads` or copy the 3.2 GB file into the repo.
- **Rule 13:** a DS-lane script; your commit is a candidate, and no `safe-deploy` (a one-time backfill, run by hand).
- **Refusal clause.** If a criterion cannot be met as written (for example the measured bytes or SHA-256 differ), stop, write the reason in
  your report and a surprise row (id `ADVI_COTBKF-W1-S<k>`), and do not weaken the test or the expected value.

<paths>
data/assets/scripts/bronze/commonwealth_landing.py
data/assets/scripts/bronze/tests/test_commonwealth_landing.py
data/assets/scripts/bronze/tests/__init__.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (`lib/opal_naming.py` included).

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.md</decomp_doc> (round 1), cell `CB-a-1`.
<owned_cells>CB-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB1-AC1, CB1-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~1/ADVI_COTBKF.TO-CB-a-1.bronze-landing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB1-AC1,CB1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the tool's CLI and the manifest it would write (the dry run's full output), the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time backfill, run by hand (C-ONE-TIME); no schedule is created.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into a new prefix of opal-data-assets.
comp-adversary: RUN -- cross-firm (every key under the cottonwood scope from the builder, C-FIRM); no shadow pipeline (C-ONE-TIME); no-overwrite (a different object at the key refuses); the moratorium (no alert); device-specific code (paths are arguments); BLIND: whether any reader already lists opal-data-assets/commonwealth/ (none can: the source row landed today @8e39143feb).
lane: the <paths> block IS the grant (worker RULING 1); data/assets/scripts/bronze/ is a new DS-lane directory under rule 13.
</preflight>

Source: PRD v0.3 @5567e751f1 section 2 hop 2, C-RAW, C-DATE, C-SOURCE; decomposition @c10cf0c76a; row ADVI_COTBKF-S1 (one zip, not two).
