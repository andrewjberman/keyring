# TO NFRA_FIDUPL.TO-FU-s-3 -- the fetch of the six custom-export files inside the minted session

<to_id>NFRA_FIDUPL.TO-FU-s-3</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-3` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-2 (the minted session); same worker, hand-on after FU-s-2 is terminal

---

## WORKER FACE

### THE CELL

**FU-s-3** -- The fetch, inside the minted context: status list for the day, `downloadExport.do` for each of the six files into a handoff directory with `listing.json`; distinct failures `export not generated yet` and `download refused`. Contract row: C-PULL.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build `infra/aws/ec2/canonical-fidelity/fetch.py` and `tests/test_fetch.py` to reference sections 4, 5 and 9.

1. `fetch_day(session, date_string, out_dir, now=None)`: POST the status list (`/ssc/importexport/wc/channel/status/v1/status.json`, body `{"iEtype":"E","dateString":date_string,"startPage":"1","pageLength":300}`) with the `x-xsrf-token` header from `session.xsrf_token()`; keep only rows whose `fileName` is one of the six names and whose `fileStatusDescription` is `COMPLETED`; GET `/ssc/importexport/wc/channel/export/v1/downloadExport.do` for each with the four row values as parameters; write each file's bytes EXACTLY as served (binary, no decoding, no newline translation).
2. Write `listing.json` per the handoff contract (reference section 5) with `source: "automated"`, `rows` for the files present (with `bytes` and `sha256`), `missing` for the others, and `failure`. If no row is found for the day, or fewer than six, `failure` is `export not generated yet` and `missing` names each absent file; if any download returns a non-200 status, that file is not written, it is in `missing`, and `failure` is `download refused`. `fetch_day` returns the listing dict and does not raise for these; it never fabricates a file.
3. `PlaywrightSession` adapts a Playwright context (`context.request`) to the session surface; `xsrf_token()` reads the `XSRF-TOKEN` cookie from the context. Its live behaviour is proven only by FU-x-1.
4. CLI `python fetch.py --date YYYY-MM-DD --out DIR` opens a session through `signin.open_session` (from FU-s-2, on your branch) and runs `fetch_day`.
5. Tests with a fake session (no network): `test_lists_then_downloads_six`, `test_sends_xsrf_header`, `test_only_completed_rows_of_the_six_names` (a COMPLETED row of another name and a non-COMPLETED row of a listed name are not fetched), `test_missing_file_reported_not_silent`, `test_export_not_generated_yet_class`, `test_download_refused_class`, `test_bytes_written_exactly_as_served` (include a file with CRLF and non-ASCII bytes), `test_listing_has_sha256_and_contract_keys`.

### ACCEPTANCE

<criterion id="FU3-AC1" cell_refs="FU-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu3</invocation><expect>R1-FU3-OK passed=\d+</expect></criterion>
`FU3-AC1` -- the eight named tests exist and pass.

<criterion id="FU3-AC2" cell_refs="FU-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu3c</invocation><expect>R1-FU3C-OK rows=6 listing=fidelity-handoff/1</expect></criterion>
`FU3-AC2` -- the fetch's output meets the handoff contract the lander reads.

<expected_criteria>FU3-AC1,FU3-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU3-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU3-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/canonical-fidelity/signin.py` (FU-s-2, on your branch)
- `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` lines 324-450 (Schwab's list and download, for shape only)

<paths>
infra/aws/ec2/canonical-fidelity/fetch.py
infra/aws/ec2/canonical-fidelity/tests/test_fetch.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-3`.
<owned_cells>FU-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU3-AC1,FU3-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~1/NFRA_FIDUPL.TO-FU-s-3.fetch-six-files.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU3-AC1,FU3-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; no AWS call and no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-3; worker reference.
