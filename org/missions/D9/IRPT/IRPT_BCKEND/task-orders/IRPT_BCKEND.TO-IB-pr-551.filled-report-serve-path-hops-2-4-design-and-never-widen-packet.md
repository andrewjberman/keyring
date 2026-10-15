# TO IRPT_BCKEND.TO-IB-pr-551 -- WRITE the design and the never-widen packet for hops 2-4 of the filled-report serve path as ONE pair: the platinum publisher, the /report route and the export source kind; both halves UNSIGNED, READ ONLY (CTO ruling 076d @fd4c44fb48, msg 7974: XA-20261015T024033Z-ef7f ruled "one scope, one issuer: 2.0.0_SA_COO~P2")

<to_id>IRPT_BCKEND.TO-IB-pr-551</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~395</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_076D_IRPT_DASHBD_REPORT_SERVE_PATH_OWNERS_20261015.md` and msg 7974 | **Decomp cell:** `IB-pr-551` (decomposition section 192) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-395`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~395 <0.9.0_WK_IRPT_BCKEND~395@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, function names and file paths only in any tracked file; no account id, household id, client id, quantity, value or holding name. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch395/`).

**Cell `IB-pr-551` (inlined).** No code publishes or serves a filled report today (the F-SHIP round-114 read, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~502/RD_REPORT_SERVE_PATH_R114.json`, READ IT FIRST). The CTO ruled hops 2-4 are IRPT_BCKEND's, to be cut as ONE never-widen pair (a new served route and publication; WORLD), the filled report's document shape fixed by hop 1's owner (`2.0.0_SA_COO~D2`): `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` version 0.5.1, key `document` (sha256 prefix `0b515243b310`): one JSON object per household with exactly two keys, `household` and `values`; values keyed by member id; absent members print their reason; the publisher publishes and the route returns that object with no re-shaping. The first exercise is 49 Financial first. The three hops are:

- **Hop 2, the platinum publisher:** publish the filled report as a NEW platinum object per client, addressed by `lib/opal_naming.py address()` (never a typed address; a builder REFUSAL is a missing registry row to add under `infra/logic/registry/`), written by the `reporting-publish` schedule beside `series.json.gz`, `manifest.json` and `summary.json` (`infra/aws/lambda/investor-reporting/reporting-publish/handler.py` line 192 pattern; `publisher.py` lines 36-37 and 251).
- **Hop 3, the route:** `GET /api/scoped/investor-reporting/reporting/client/{client_id}/report` on the `irpt-49f-reporting-read` lambda (`infra/aws/lambda/investor-reporting/reporting/entry.py`: the summary route at line 92, the scope check at lines 332-345, the ROUTES map at line 373; declared in `infra/aws/terraform/investor-reporting/reporting-read/api.tf` lines 24-37). It refuses unless the viewer's scope covers EVERY account the document names.
- **Hop 4, the export source kind:** a filled-report source kind for the export (`infra/aws/lambda/investor-reporting/export/bundle.py` and `retained_export.py` freeze only retained-report and performance-source series today), pinning the filled object's version.

**This order WRITES THE DESIGN AND THE PACKET. It builds, changes and deploys NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Read the named files** at HEAD (Read, with the line numbers above; they may have moved a few lines: cite what you read) and `lib/opal_naming.py` (the address builder: `address()`, its tier and table constants, and whether a registry row for a `report` object kind exists under `infra/logic/registry/`; the builder's output for `client=<id>` is the address, so state it as the builder's OUTPUT with a placeholder id, never typed by hand), the Terraform for the read lambda's routes and its IAM (does a new GET route on the same lambda need any new permission? say yes or no with the file:line), and where the builder's document lands (read what `2.0.0_SA_COO~D2` has: contract file, its sample builders `deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py` and `~175/build_sample_inflection_r110.py`; if no landing address is named anywhere, say so as `claim` `inferred` or `absent` and name the question for the CTO).
3. **Write the design** `deliverables/0.9.0_WK_IRPT_BCKEND~395/IB199-3_serve_path_design.json`: `{"base_commit":"<40hex>","hops":{"2":{"what":"..","exists_today":false,"risk":"SERVED|WORLD","files":[{"path":"<repo path>","line":<n>,"identifier":"<a name ON that line>"},...],"address_builder_output":"<the naming builder's output for client=<id>>","registry_row_needed":true|false},"3":{"what":"..","exists_today":false,"risk":"WORLD","files":[...],"path_template":"/api/scoped/investor-reporting/reporting/client/{client_id}/report"},"4":{"what":"..","exists_today":false,"risk":"WORLD","files":[...],"source_kind":"<name>"}},"input_contract":{"document_shape":{"contract":"org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json","version":"0.5.1","key":"document","sha256_prefix":"0b515243b310"},"source":"<who writes the document and where it lands, 40+ characters>","claim":"measured|inferred|absent"},"scope_rule":"<the route refuses unless the viewer's scope covers EVERY account the document names, and how it reads the named accounts>","blast_radius":{"writes":["<each key or resource the pair creates>"],"reads":["<what the pair reads>"],"new_iam":true|false,"served_values_changed":false,"existing_routes_changed":false},"rollback_per_key":"<per created key and per declared route, 40+ characters>","first_exercise":{"firm":"49financial","order":"first"},"build_slices":[{"cell":"<name>","risk":"LOCAL","files":["<paths the slice writes>"],"depends_on":["<cell>"]},...],"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. Every `files` entry is a site the check reads at HEAD (path exists, line in range, the identifier on that line). `build_slices` are the LOCAL build cells the CTO will cut after the pair is signed (for example the publisher change with its tests, the route with its scope check and tests, the export source kind with its tests, the Terraform route declaration); at least two, each naming the files it writes.
4. **Write the packet** `deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md`, at least 6,000 characters, in the shape of the earlier packets (READ `deliverables/0.9.0_WK_IRPT_BCKEND~393/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-532_V3.md` for the sections: change set, blast radius, rollback per key, stop rule, the releasing seat's NEVER-2 ledger, what the packet does not measure, signatures). It must carry these phrases (case-insensitive): "never-widen", "hop 2", "hop 3", "hop 4", "blast radius", "rollback", "49 Financial", "stop rule", "opal_naming", "COO half", "CTO half"; the windowing of hop 5 (the render host, under `0.7.0_AE_CloudOps~IB2`, is a later act under the same window); and **both halves UNSIGNED**, the packet's sha256 LEFT for the signers (do not compute it). State what the pair does NOT touch: holdings, the summary route, any existing object, any served value.
5. **Notes and counters:** `notes` say what each fact rests on and what was not read (the live deployment is not read; no AWS call is needed).

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB199-3_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, packet and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB199-3-AC1" cell_refs="IB-pr-551"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-3-AC1</invocation><expect>IB199-3-AC1 PASS</expect></criterion>
<criterion id="IB199-3-AC2" cell_refs="IB-pr-551"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-3-AC2</invocation><expect>IB199-3-AC2 PASS</expect></criterion>
<criterion id="IB199-3-AC3" cell_refs="IB-pr-551"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py" . IB199-3-AC3</invocation><expect>IB199-3-AC3 PASS</expect></criterion>

<expected_criteria>IB199-3-AC1, IB199-3-AC2, IB199-3-AC3</expected_criteria>

What the checks grade: AC1 hops 2, 3 and 4 each with the files to change (each path, line and identifier read at HEAD), `exists_today` false, the hop 2 address stated as the naming builder's output for client=<id> with `registry_row_needed` stated, the hop 3 route template exactly as above, the hop 4 source kind named; AC2 the input contract naming contract 0.5.1, key `document` and sha256 prefix `0b515243b310` with a claim and the document's source, the scope rule (every account the document names), the blast radius (writes, reads, `new_iam`, and `served_values_changed` and `existing_routes_changed` both false), the rollback per key, the first exercise on 49financial first; AC3 the packet at least 6,000 characters with the phrases and both halves UNSIGNED, at least two LOCAL build slices each naming files, notes present, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is built, changed, deployed, written to AWS, invoked, signed or sent;** no AWS call is needed. A file outside the paths block is read only.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a client identifier in a tracked file; a need to type an object address by hand (that is a missing registry row: record it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W395-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~395/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 192 (round 1, workstream ~PS), cell `IB-pr-551`.
<owned_cells>IB-pr-551</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB199-3-AC1, IB199-3-AC2, IB199-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~395/IRPT_BCKEND.TO-IB-pr-551.filled-report-serve-path-hops-2-4-design-and-never-widen-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads repository files and writes one design record and one packet in the worker's deliverables; nothing is built or deployed and no AWS call is made, so no served byte moves; the pair the packet describes (a new platinum object kind, a new GET route, an export source kind) is a later act under two signed halves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order; whether the later pair needs one is a question the design answers with a file and line.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is declared or changed by this order; the design names the route the pair would add.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p199_cells.py IB199-3 dry-run at base on dell2 2026-10-15 ~03:2xZ: AC1, AC2, AC3 FAIL (no record, no packet). Positive control in a temp git root the run created itself (a synthetic record, a synthetic packet and a stub file for the file sites; removed): all three PASS; fourteen negatives across IB199-3, each failing its own arm: hop 4 missing, a hop that exists today, a file site with the wrong identifier, a wrong route template, an address typed by hand, the wrong contract version, no scope rule, existing routes changed, the first exercise on another firm, a packet too short, a packet with one half signed, one build slice only, a build slice that is not LOCAL, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~395` (worktree `C:/dev/wk-IRPT_BCKEND-395`). Class SERVED (a design for a new served route and publication; the order itself reads files and writes only the worker's records).
</preflight>
