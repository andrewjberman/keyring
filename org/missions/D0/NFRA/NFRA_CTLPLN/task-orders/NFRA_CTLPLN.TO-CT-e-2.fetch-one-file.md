# TO NFRA_CTLPLN.TO-CT-e-2 -- round 5 CT-e-2: the fetch of ONE exact file into the holding folder, with its record written at the time

<to_id>NFRA_CTLPLN.TO-CT-e-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~14</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-e-2` (`decompositions/NFRA_CTLPLN_DECOMP.round5.md`) | **outcome_ref:** FWD-15, FWD-19 |
**depends_on:** none (the record contract below is the seam; no cell waits on another's code)

---

## WORKER FACE

### THE CELL

`CT-e-2`, C-INTAKE clauses 2 and 3, and FWD-19 ("Andrew can ask what a box downloaded and get an answer from a record").
The laptop is the one box that may fetch a package, one named file for one approved line, with no dependency resolution, into a
holding folder where it waits unchecked. Every fetch, successful or not, writes a record at the time. CTO msg 106372: "the
fetch-one-exact-file tool, the holding folder ... The tool takes a platform tag, because site Z's files are Linux builds for a
Lambda." You build the tool and prove it against a fake index on loopback. YOU FETCH NOTHING REAL.

### THE SEAM

THE RECORD CONTRACT (fixed here so the four cells share FILES and never wait on each other's code).
All records are JSON, UTF-8, ASCII-only, one file per event, under `org/devices/intake/records/<batch>/`:
- FETCH record `<file name>.fetch.json`, written by the fetch tool AT THE TIME OF THE FETCH, also when the fetch fails:
  `schema` ("intake-fetch/1"), `batch`, `requested` {`name`, `version`, `python_tag`, `abi_tag`, `platform_tag`, `file_name`},
  `index_base`, `requests` (a list, one entry per HTTP request made: `url`, `method`, `status`, `bytes`, `at` UTC),
  `published` {`sha256`, `size`, `upload_time`, `yanked`, `requires_python`} (as the index states them for that exact file name),
  `project` {`release_count`, `first_release_at`, `this_release_at`}, `attestation` ("present" | "absent" | "unread", with the
  URL asked), `held_path` (relative to the holding root, never absolute), `held_sha256`, `held_bytes`, `outcome`
  ("held" | "refused" | "failed") with `reason`, `fetched_by` (the serial), `at`.
- CHECK record `<file name>.check.json`, written by the check tool: `schema` ("intake-check/1"), `batch`, `file_name`,
  `held_sha256`, `checks` (a list of exactly eight, in the brief's order, each `n`, `name`, `verdict`
  ("passed" | "failed" | "not_applicable" | "unsigned"), `evidence`, `rules_out`, `leaves` -- the last two the brief's own
  words for that check), `verdict` ("checked" only when checks 1 to 7 are each passed or not_applicable WITH a reason and
  check 8 reads "passed" with a signer and a file path; otherwise "not_checked"), `checked_by`, `at`.
- RECEIPT record `<file name>.receipt.<device>.json`, written on the receiving box: `schema` ("intake-receipt/1"), `device`,
  `python`, `file_name`, `received_sha256`, `check_record_sha256`, `install` {`command`, `rc`}, `imports` (per top-level module:
  `module`, `rc`, `first_error_line`), `outcome` ("installed_imported" | "installed_import_failed" | "refused" | "install_failed")
  with `reason`, `at`.
The HOLDING ROOT is outside every git tree: `<drive>/opal-intake/` (derive the drive prefix: `/cygdrive/c` if it exists, else
`/c`; on Windows Python resolve it from the workspace root's drive), with `holding/<batch>/` for fetched files and
`release/<batch>/` for files whose check record reads "checked". A file moves from holding to release ONLY by the check tool.

### BUILD

1. `org/devices/intake/intake_fetch.py`:
   - `fetch --batch <id> --name <dist> --version <v> --python-tag <t> --abi-tag <t> --platform-tag <t> [--index-base <url>]`:
     builds the ONE exact wheel file name from those five values (name normalised as the wheel specification states) and gets
     that file and nothing else. The default index base is the public Python package index's own JSON interface
     (`https://pypi.org`); `--index-base` exists so a test can point it at loopback. The sequence, each request recorded:
     (a) GET `<base>/pypi/<name>/<version>/json`: find the entry in `urls` whose `filename` equals the built name EXACTLY; if
         none, outcome "refused", reason "no such file for this release", and list the file names the release does have (so a
         person can see a near miss) -- never pick another file;
     (b) GET `<base>/pypi/<name>/json`: the project's release list (count, first release time, this release's time);
     (c) GET the attestation address for that file (the index's integrity interface,
         `<base>/integrity/<name>/<version>/<file name>/provenance`): 200 -> "present", 404 -> "absent", anything else -> "unread";
     (d) GET the file's own `url` from (a), streamed to `holding/<batch>/<file name>.part`, hashed while written; rename to
         `<file name>` ONLY when the SHA-256 and the size equal what (a) published for that file; a mismatch deletes the part
         file and the outcome is "refused", reason "digest mismatch".
     HOST RULE: every request's host must be in a closed set derived from the index base: for the public base exactly
     `pypi.org` and `files.pythonhosted.org`; for a loopback base exactly that loopback host and port. A file `url` on any
     other host, a redirect to any other host, a non-HTTPS URL on the public base, or a URL whose final path segment is not the
     exact file name -> "refused" before the request is made. Redirects are followed manually and each hop is checked.
     Standard library `urllib` only; a 30-second timeout per request; no retry loop that could hammer the index (one retry on a
     connection error, recorded).
     It writes the FETCH record of THE SEAM on every path, including a refusal before any request. It never installs, never
     unpacks, never imports the file. LAST line
     `INTAKE-FETCH batch=<id> file=<file name> requests=<n> outcome=<held|refused|failed> sha256=<12 hex|-> bytes=<b> attestation=<present|absent|unread>`.
   - `list --batch <id>`: what the holding folder and the records hold for a batch (the FWD-19 read): one line per file with its
     outcome, time and requester, and LAST `INTAKE-HELD batch=<id> records=<r> held=<h> refused=<x> failed=<f>`.
   - It REFUSES to run a `fetch` against the public base unless `--approved-by <path>` names an existing file (the CTO's signed
     batch approval) whose text contains the exact `name==version`; the path and the file's SHA-256 go in the record. Against a
     loopback base the flag is not required.
2. `org/devices/intake/test_intake_fetch.py`: a fake index you start on 127.0.0.1 (standard library `http.server`) serving
   synthetic JSON and a tiny synthetic wheel. Cases: the happy path leaves exactly one file in holding with the published digest
   and a record with four requests; a release that lacks the exact file name is refused and the record lists the names it has;
   a file whose bytes differ from the published digest is refused and no file remains (no `.part` either); a file `url` on
   another host is refused BEFORE any request to it (the test's second listener on another port counts zero requests); a
   redirect to another host is refused; a 404 attestation reads "absent"; `--platform-tag manylinux2014_x86_64` with
   `--python-tag cp311` builds the Linux name; a `fetch` on the public base without `--approved-by` is refused with ZERO
   requests (assert by pointing name resolution nowhere: the refusal must happen before any socket is opened; prove it by
   patching the opener to raise if called); `list` reads the batch back. LAST line `INTAKE-FETCH-TEST cases=<k>/<n> ok=<True|False>`.
3. `org/devices/intake/README.md`, short: the route in six lines (request, assessed, decided, fetched and held, checked and
   released, sent and received), which tool is each hop, and where each record lives.

### RULES FOR THIS CELL

**No request leaves this machine from anything YOU run.** No `pip install`, `pip download`, `pip index`, no `curl`, `wget`,
`npm`, `bun`. Every HTTP request your code makes in a test goes to a listener you start on 127.0.0.1. You never run your tool
against the public index: the first real fetch is the issuer's act, after the drain, on the CTO's signature.
No non-ASCII in any file you write. Standard library only unless the order names a package. Bake no absolute path and no user name.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CT5e2-AC1" cell_refs="CT-e-2"><invocation>python org/devices/intake/test_intake_fetch.py</invocation><expect>INTAKE-FETCH-TEST cases=</expect></criterion>
`CT5e2-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CT5e2-AC2" cell_refs="CT-e-2"><invocation>python org/devices/intake/intake_fetch.py fetch --batch selfcheck --name pyyaml --version 6.0.3 --python-tag cp314 --abi-tag cp314 --platform-tag win_amd64</invocation><expect>outcome=refused</expect></criterion>
`CT5e2-AC2` -- the public base without an approval file is refused with `requests=0`: the same line must read `requests=0`. (This is the difference control: the tool cannot reach the index on a bare call.)
</proof_of_spec>

<expected_criteria>CT5e2-AC1,CT5e2-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/NFRA_CTLPLN.TO-CT-e-2.fetch-one-file.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CT5e2-AC1,CT5e2-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round5.md</decomp_doc>
<owned_cells>CT-e-2</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_fetch.py
org/devices/intake/test_intake_fetch.py
org/devices/intake/README.md
org/devices/intake/records/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the tool runs when a seat runs it.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- the test of the fetcher being the fetch (loopback only; the bare public call is refused before a socket opens, and that is a criterion); a near-name or wrong-version file taken (exact file name or refusal, the near misses listed); a file altered in transit kept (digest and size against what the index published, the part file deleted); the index sending the tool elsewhere (closed host set, each redirect hop checked); a fetch with no record (the record is written on every path, a refusal before any request included); dependency resolution by the back door (one file, no resolver, nothing installed or unpacked); BLIND: an index that publishes a bad file under a true digest (checks 3 to 7 and the limits the brief states).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.17 @301f06300d (ADMITTED), ADDENDUM v0.15 and v0.16, contract C-INTAKE; brief
`docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md` @adc8997f1b Part V.1; CTO msgs 106327, 106363, 106372,
106424, 106436, 106445.
