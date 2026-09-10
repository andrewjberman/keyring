# ETFS_GUARDRAIL -- surprise channel, ADJUDICATION v1 (round 1, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
Minted 2026-09-05 ~10:3xZ by `3.0.0_SA_CVO` at L9 on the issuer's L8 packet
`org/missions/D8/ETFS/ETFS_GUARDRAIL/ledger/L8_PACKET.round1.partial.md` @`05e0b5bbd8` (the drain-end revision), never
as an empty file.
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an observation
or a grade of the CVO's about the rows in `../investigations/`; a seat that contests one surfaces a new investigation
row citing it. A reader resolves an item's state from the newest row that cites it across the documents; a seat-form
ARMED item's disarm state is its remediation row's `disarm.state`; a worker-form item's disarm state is recorded on the
adjudication row that graduates it, citing the issuer's disarm commit, because a remediation row keyed by a `W<n>`
coordinate is not a row the CVO can mint on the main index.
**Coordinate:** `ETFS_GUARDRAIL-C-S<k>`, `k` from 1 in this document.
**Round 1 read (L8/L9):** 14 of 14 orders terminal at HEAD @`9ce1de85e7`; 14 proof instances VALID at the issuer's seat;
the judgment set is 14 criteria (13 flagged `judgment: true` in their instances; S13-AC6 carries no flag in its
instance but is `UNVERIFIABLE-BY-INSTRUMENT` with the CVO named, and is graded as the judgment criterion the order cut).
21 investigation rows (S1-S3, W1-S1..S10, W2-S1..S6, W3-S1..S2), all dispositioned below. Every grade and every
disposition rests on this seat's own read beside the record: the served Lambda code hashes, environment and the
deployed Inflection zip, the reporter role's inline grant, SES's account state, the report bucket, the source at HEAD,
the vendored-copy census, the published layer, and `.gitattributes`.
**Denominator at this write:** 10 rows (C-S8..C-S10 appended 2026-09-10 ~00:5xZ -- round 2 PARTIAL L9 @8f7bf86815: S17-AC2 graded PASS; W2-S7 closed; W2-S8 open at the CTO (the 76-minute race); W2-S9/S10 and S5..S9 records); previous: 7 rows (C-S7 appended 2026-09-10T00:39Z: a correction of C-S6 -- no remediation row was minted; the gate refused it as L10-shaped and the clocks ride C-S6 until the round-2 L9); previous: 6 rows (C-S6 appended 2026-09-10 ~00:2xZ: S4 graduated, the deploy_ledger NEVER-2 defect, owner 0.2.0_DT_PortfolioAnalytics); previous: 5 rows (C-S1 the grade record; C-S2 the eight worker-form items graduated and closed on
the issuer's in-round acts; C-S3 the three items graduated and OPEN; C-S4 the ten records dismissed with reason; C-S5 the
correction carrying the CTO's L10 @0557afa38a -- FWD-4 NOT_EVALUATED, seven fire-gated outcomes, not six).
Investigation rows without a disposition after this write: 0 of 21. Remediation rows minted: S2 (OPEN), S3 (closed).

---

## C-S1 -- the round-1 grade record: fourteen judgment criteria on fourteen terminal orders, each read against its bar with this seat's own instrument; fourteen PASS; the EXERCISED grades that only scheduled fires can produce are named, not manufactured

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T10:30Z",
    "one_line": "L9 (spine v3.2): the GRADE RECORD for the fourteen judgment criteria of round 1, handed in the issuer's packet @05e0b5bbd8. Each grade rests on this seat's own read beside the worker's record. THE LIVE PLANE, 09:5xZ-10:2xZ: cot-etf-ownership-daily serves CodeSha256 21/NtBoTmMsBBSsfwNnA+UP+I3HIzDnZaoeL3lBShFk= (S1's record), bd-49f-etf-ownership-daily serves 5Q9X+m0VzbY2kab3NaOa26Ho5mjmS1DiRnBshz4xrUo= (S2's), etfs-reports-orchestrator serves CvFmg9ZmBrSMZSSlplJGd7BWp99FXn5+ODaRbKTe/QI= (S9's, which superseded S8's) -- served equals built on all three; the orchestrator's EMAIL_RECIPIENT is aj@opalinvest.com,andrew@opalinvest.com and it carries REPORTER_INSTANCE_ID; bd-49f's OUTPUT_PREFIX is daily/49financial/ and its canonical twin is absent from the function list; inf-etf-ownership-daily binds ASSETS_BUCKET and INF_BUCKET both, LastModified 2026-08-11; the reporter role's inline grant InvokeProducersForRemediation is lambda:InvokeFunction on exactly the three producer ARNs; SES ProductionAccessEnabled true. THE DEPLOYED INFLECTION ZIP, downloaded here: one entry, lambda_function.py, byte-identical to the repo at af4f123e2c and different from HEAD and from the repoint 001a73530a; no dedup_core.py, no trading_calendar.py. THE SOURCE AT HEAD: three send_raw_email sites (:185 terminal with one recipient, :289 and :378 with the list), three msg['To'] sites, --gate in _render_command at :227, the ladder with no HTTP client and its one put_object inside rung3_stop_and_ask, the classifier with no write surface and holes = C + UNKNOWN + D beside expected_empty = B, the gate's comment and code never probing Inflection. THE VENDORING CENSUS: no trading_calendar.py under either port; the layer opal-trading-calendar-layer v1 exists. Fourteen PASS; no FAIL; no NOT_EVALUATED; findings ride to the CTO's analysis where named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`lambda list-functions` filtered on 'etf' at this seat, 10:0xZ: eleven functions; the three this round deployed serve exactly the CodeSha256 values their proof instances recorded as served-equals-built (cot 01:39:04Z, bd-49f 03:05:54Z, orchestrator 08:41:01Z LastModified); no function named bd-49f-etf-ownership-daily-canonical exists; inf-etf-ownership-daily LastModified 2026-08-11T10:29:39Z. `get-function-configuration` on four: the env values quoted in the one_line.",
        "`lambda get-function inf-etf-ownership-daily` and the Code.Location download at this seat: 4,942-byte zip whose sha256 (base64) equals the served CodeSha256; namelist ['lambda_function.py'] only; that file's sha256 after CRLF normalisation equals `git show af4f123e2c:infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py` (12,141 bytes) and differs from HEAD and from 001a73530a (15,130 bytes). The worker's S12-AC5 reading (MISMATCH files=3; running bytes predate the Orion repoint; the 2026-08-11 LastModified is a config-only update) is reproduced on the artifact itself, an instrument line endings cannot touch.",
        "`iam list-role-policies etfs-reports-reporter-role` -> one inline policy; its statement Sid InvokeProducersForRemediation: Action lambda:InvokeFunction, Resource exactly [cot-etf-ownership-daily, bd-49f-etf-ownership-daily, inf-etf-ownership-daily] ARNs, no bucket. `sesv2 get-account` -> ProductionAccessEnabled true, SendingEnabled true.",
        "Source at HEAD via comp-read --enumerate: infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py -- send_raw_email at :185 (Destinations=[TERMINAL_RECIPIENT]), :289 and :378 (Destinations=EMAIL_RECIPIENTS); msg['To'] at :154 (TERMINAL_RECIPIENT), :257, :321 (EMAIL_RECIPIENT); :227 `python3 render_month_end.py --month {month} --pdf --gate --s3-out {out}` with the S3 row cited at :221. data/etfs/scripts/coverage/remediate.py -- no `import requests`/urllib hit, one `s3.put_object(` at :119 inside `def rung3_stop_and_ask` (:89), the ask artifact. data/etfs/scripts/coverage/classifier.py -- no put_object/upload_ hit; :175-177 trading_days = COVERED+B+C+D+UNKNOWN, holes = C+UNKNOWN+D, expected_empty = B. data/etfs/scripts/presentation/render_month_end.py -- :821-825 'Inflection is therefore NEVER probed here; its non-covered days always classify UNKNOWN', :857 a probe failure is an honest UNKNOWN.",
        "The vendoring census, `comp-find 'trading_calendar' --name --files` over the whole corpus (155,001 files scanned): lib/trading_calendar.py, its test, and three vendored copies (bd-served-vintage-alarm, inf-etf-ownership-daily, opal-assets-absence-check) -- none under cot-pipeline/cot-etf-ownership-daily or bd-pipeline/bd-49f-etf-ownership-daily; `lambda list-layers` -> opal-trading-calendar-layer version 1 exists. The ports took the layer, as W1-S1's disarm @de8693863c states.",
        "s3://opal-data-etfs/platinum/reports/: months 2026-05..2026-08 and corrections/; 2026-08/ holds the html, the pdf and three CSVs written 2026-09-01T17:38Z, before this round; the cottonwood CSV fetched here ends on its PFDE/PFOE numeric rows with no '# coverage:' line -- the published August artifact predates EG-s-5, so FWD-3 is APPLIED at HEAD and rehearsed in QA, not yet EXERCISED on a served artifact; no refused/ prefix under platinum/reports/ (the fixture REFUSE wrote under the QA --s3-out, not the publish key, as S6-AC8's record says)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: this row adjudicates no item and opens nothing; its content is the fourteen grades below.",
    "grades": [
      {"criterion": "S10-AC5", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.the-trading-calendar-each-producer-resolves.proof_of_spec.json@e6689cc7cc", "verdict": "PASS", "reason": "The bar: which calendar each producer resolves today and the vendoring recommendation. The answer is measured (inf: its own byte-identical vendored copy, present in the census at this seat; cot and 49F: none, newest-partition only) and the recommendation found the live CTO~Z ruling @1da1e2b73b and chose the layer over the fifth copy the faces mandated; the issuer adopted it @de8693863c and the ports built to it -- no new copy exists under either port at HEAD and the layer is published. Graded on the answer; the adoption is the record's."},
      {"criterion": "S3-AC5", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.proof_of_spec.json@d008067fa3", "verdict": "PASS", "reason": "The bar: the port contract as the spec the two port orders built to. Its substance held: the verbatim set, the one replacement (the reporting-obligation window with the shipped-signal terminus), the invariants, the probe addition and the 49F-tail test arm are what EG-s-1 and EG-s-2 deployed, served-equals-built on both. One clause of it was wrong and is named: the battery SHAPE (a bare script ending in a module-level sys.exit) crashes pytest at collection (W2-S4); both ports shipped real test functions instead, and the inf source's own battery of that shape is dead (W2-S1). The contract is graded as built-to, PASS; the shape clause is a finding, carried on W2-S1 and W2-S4."},
      {"criterion": "S13-AC6", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.proof_of_spec.json@198f98a64a", "verdict": "PASS", "reason": "The bar: one date basis from the cutover month forward, nothing restated, no partner notified, the alignment gating the send and not the guardrail. The record shows Inflection re-keyed at read time in both artifacts the renderer produces (the deck path and the separate CSV path W3-S1 found), 2026-09 aligned and 2026-08 rendered on its raw keys, no S3 write and no send path touched, and the send gated by issuance sequencing (EG-s-9 handed after this order). Read as recorded; the instance carries no judgment flag on this criterion, which is a form defect of the instance and not of the answer. FWD-6 is APPLIED at HEAD."},
      {"criterion": "S11-AC5", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-11.which-49f-twin-writes-the-served-slices.proof_of_spec.json@108d9fa67f", "verdict": "PASS", "reason": "The bar: the served slices' writer confirmed on the applied plane at both ends. The record's function side (WRITER=bd-49f-etf-ownership-daily, OUTPUT_PREFIX=daily/49financial/, the canonical twin not live) is re-read here live: the env value is served and no function of the canonical name exists in the list; the object side (3 of 3 newest slices tied to 3 of 3 'OK: wrote' events, by the worker's paginating script after the single-call trap W2-S3 names) is the record's. EG-s-2 then ported into exactly that function, whose served hash this seat read."},
      {"criterion": "S12-AC5", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-12.inflection-deployed-bytes-vs-build-input.proof_of_spec.json@a8e3ac7927", "verdict": "PASS", "reason": "The bar: the finding and the consequence drawn. The finding is reproduced here on the artifact itself: the deployed zip has one entry, byte-identical to af4f123e2c and different from HEAD and from the repoint; the two support modules are absent from it; ASSETS_BUCKET is bound on the function and, by the worker's read of the running code, never referenced. The consequence -- rung 2 for Inflection stated against the legacy path, not repo HEAD -- follows and EG-s-7 built it so. For the CTO's L10 read, carried not remedied: the Orion repoint is COMMITTED-NOT-APPLIED under another seat's ruling; this project classifies against the world as it runs."},
      {"criterion": "S4-AC7", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-4.the-coverage-classifier.proof_of_spec.json@62cc386d94", "verdict": "PASS", "reason": "The bar: the taxonomy's four postulates on 'a calendar day of the month'. At HEAD the module writes nothing (no put_object or upload_ in it), B is excluded from holes and counted as expected_empty by construction at :176-177, UNKNOWN only when no probe answered, and the sums the record shows (August inflection 10+21=31; the fixture 16+5=21 and 21+0=21; live August cottonwood 21 of 21 covered, UNKNOWN=0) are MECE over the declared domain. Property 4 met."},
      {"criterion": "S1-AC9", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-1.cot-catch-up-port-reporting-obligation-window.proof_of_spec.json@c866edd324", "verdict": "PASS", "reason": "The bar: the cot port as deployed against rulings 1 and 2 and property 1. The window is the reporting obligation with the shipped-signal terminus (a denied read counts as not shipped and is logged WARN), the source's three skips kept, no day-count constant, ZERO-vs-MISSING untouched, the probe mode answered live for 2026-08-04 writing nothing, the calendar from the published layer, the plan changed exactly the Lambda and its role policy with a 0-diff after, and served equals built -- the last read live here. FWD-1 stays at APPLIED-and-rehearsed until a scheduled fire names a recovered date in catchup_processed, which the order rightly did not manufacture."},
      {"criterion": "S7-AC7", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-7.the-remediation-ladder-rungs-1-2-and-the-invoke-grant.proof_of_spec.json@745cd6b354", "verdict": "PASS", "reason": "The bar: rungs 0-2 unattended and never fabricating, the one grant, rung 3 absent by construction. At HEAD the ladder carries no HTTP client and its only put_object is rung 3's ask; the grant read live names exactly the three producer ARNs and no bucket; the live August cottonwood dry-run recorded holes=0 across all rungs; the Inflection re-check is stated against the deployed producer's legacy bucket (the S12 finding applied); the apply was by target under the W1-S7 ruling and the drift it worked around was false (S2). Rulings 4 and 6 and property 9 met. Row W2-S6's containment sits in the gate's probe callable, graded at S6-AC8."},
      {"criterion": "S2-AC9", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-2.bd-49f-catch-up-port-the-tail-a-straight-port-misses.proof_of_spec.json@fb0776daae", "verdict": "PASS", "reason": "The bar: the 49F port as deployed with the tail, against arms (i) and (j) and rulings 1 and 2. Arm (i) returns and processes a partition for D that appears only on D+13 with today D+14; arm (j) under the source's CATCHUP_WINDOW_DAYS=10 semantics would not have found it -- the negative control that distinguishes the two designs; no day count re-proposed; the DS module byte-identical (the one-producer law); the guard kept; the probe answered live; the layer attached; the plan changed exactly the two bound addresses in the wide bd-pipeline directory with No changes after; served equals built, read live here. Property 2 met; FWD-1 EXERCISED waits on a scheduled fire."},
      {"criterion": "S7B-AC5", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-sb-7.rung-3-stops-and-asks-a-person.proof_of_spec.json@c50c72f92a", "verdict": "PASS", "reason": "The bar: rung 3 a different actor, against ruling card 4 and FWD-8's DONE WHEN. rung3_stop_and_ask takes no invoke and no HTTP parameter and the module carries no HTTP client (read at HEAD); the ask names date, partner, provider, class, reason and the per-use authorization line; it fires only with something unresolved and never under dry-run; the direct write=False call and eight arms are its exercise. FWD-8 EXERCISED needs a real unresolved month at the renderer's gate, not manufactured. FINDING on the carrier, not the criterion: the worker re-scoped test arm (e) to the post-rung-3 invariant and disclosed it in the result and the commit message rather than as a row; the re-scope is the stronger property and the disclosure is honest, but a change to an arm the order named is an off-spec act and its carrier is a ROW for the issuer's amendment, so the next cut should say so on the face."},
      {"criterion": "S5-AC6", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-5.the-coverage-line-in-the-report.proof_of_spec.json@1c5603a696", "verdict": "PASS", "reason": "The bar: a reader of the PDF or the CSV can tell coverage and carry without opening anything else, on every path, grid unchanged. The line is computed unconditionally in render_month and rendered beneath each partner's SUMMARY row and as the CSV's last comment row, the numeric rows unchanged (arm (d)); the REFUSE path inherits it downstream and EG-s-6 measured COVERAGE_LINES_ON_REFUSE=3. Property 6 met and FWD-3 APPLIED. Stated for the CTO's grade: the published August CSV fetched here still ends on its numeric rows -- it was written 2026-09-01, before this round -- so the served artifact will carry the line only from the 10-01 fire; that is EXERCISED's date, not a defect."},
      {"criterion": "S8-AC8", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-8.the-one-terminal-ses-send.proof_of_spec.json@f036a438fb", "verdict": "PASS", "reason": "The bar: the carve-out's width (PRD s.0) and property 8. At HEAD exactly three send_raw_email sites exist, the terminal one with Destinations=[TERMINAL_RECIPIENT] and its own header site; it fires only from the refusal branch when coverage_unresolved.json exists, once, naming each date, partner, provider, class and reason with the egress ask; absence_check and terminal_qa make no SES call; no schedule, alarm, monitor or env var was added (the function's env read live carries none). The width is one send from one branch to one person. FWD-7 EXERCISED needs a real terminal failure, which the PRD's own design makes rare; the rehearsal on the deployed function (StatusCode 200, no email) is the record. Also on this order: the --gate seam (S3) closed by S8-AC9, verified at :227."},
      {"criterion": "S6-AC8", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-6.the-pre-publish-gate-inside-the-renderer.proof_of_spec.json@c17da2f4a8", "verdict": "PASS", "reason": "The bar: properties 3 and 5 -- a render precondition under --gate rather than a standing service, catch-up before it, the ladder inside it, PUBLISH iff C == 0 for every partner with B and D reported, a REFUSE writing the verdict and the refused HTML under refused/ and no pdf at the publish key, exit 3 surfacing on the existing topic. The record's two live QA renders show both halves (the pre-repair fixture REFUSED with holes=5 and five probe invokes of the cot producer, no write; August as it stands PUBLISHED with zero invokes); the publish key at this seat holds only the 2026-09-01 artifacts and no refused/ prefix, consistent with a QA out prefix. W2-S6's containment is in the gate: the comment and code at :821-857 never probe Inflection and classify its uncovered days UNKNOWN to rung 1. FWD-2 EXERCISED is a real refusal on a scheduled fire that reaches a person; the order rehearsed and did not manufacture it."},
      {"criterion": "S9-AC8", "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-9.join-both-recipients-at-four-sites.proof_of_spec.json@9ce1de85e7", "verdict": "PASS", "reason": "The bar: JOIN, not replace, at four sites, and property 7. At HEAD the two report/correction envelopes take the list and the two headers keep the joined string, the terminal send stays andrew@ alone (ENVELOPE_LIST_SITES=2, HEADER_SITES=3 under the W1-S9 amendment, SINGLE_ELEMENT_ENVELOPES=0); the variable EMAIL_RECIPIENT=aj@opalinvest.com,andrew@opalinvest.com is on the applied plane, read live here; SES production access is enabled, read live here, so an unverified recipient cannot fail silently; served equals built on the orchestrator. FWD-5 EXERCISED is the 10-01 fire read as delivery at both inboxes; nothing was sent to AJ ahead of it. Row W1-S10's second apply before its ledger entry, remediated the same turn with a supplementary entry, is graded as an honest deviation disclosed and repaired, and rides to the analysis as the sequencing lesson."}
    ],
    "spec_asserts": "Spine v3 L9 / annex section 4a: a judgment criterion is graded by the CVO against the specification that issued it, one entry per criterion on a row of the CVO's, with the CVO's own read beside the worker's record.",
    "world_is": "All fourteen judgment criteria hold on this seat's instruments. Five outcomes of the PRD are APPLIED and rehearsed and reach EXERCISED only on scheduled fires the round did not manufacture: FWD-1 (a recovered date in catchup_processed on a producer's fire), FWD-2 (a real refusal that reaches a person), FWD-3 (the coverage line on a served artifact, 10-01), FWD-5 (delivery at both inboxes, 10-01), FWD-7 (a real terminal failure), FWD-8 (a real stop-and-ask). The CTO's analysis grades those on their dates, not on this record.",
    "notes": "Findings for the CTO's analysis, none a failure of a cell: the port contract's battery shape (S3-AC5, W2-S4) and the inf source's dead battery (W2-S1, the CVO's routed item below); the Orion repoint COMMITTED-NOT-APPLIED (S12-AC5); the arm re-scope carried in prose rather than a row (S7B-AC5); the ledger-sequencing deviation (W1-S10); the .gitattributes eol rule for *.tf (S2, OPEN below); build-zip.sh's month-00 defect (W1-S5, OPEN below). Instrument note: the published August CSV read here is the served artifact and predates the round, which is why it is cited for what it lacks and not against any criterion."
  }
]
```

## C-S2 -- adjudicates the eight worker-form items the issuer disarmed inside the round, GRADUATED and closed: W1-S1, W1-S2, W1-S3 (carrying W2-S2 and W3-S2), W2-S3, W2-S4, W2-S5, S3 and W2-S6; each disarm commit read at this seat

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T10:35Z",
    "one_line": "L9: ADJUDICATES eight items -- GRADUATED, each remedied inside the round by its disarm owner and each remedy read at this seat, so their state is REMEDIATED, DISARMED and closed as of the commits named. W1-S1 (the faces mandated a fifth vendored calendar copy against CTO~Z's layer ruling): disarmed @de8693863c, the ports took the layer -- no trading_calendar.py under either port at HEAD, the layer published (this seat's census). W1-S2 (BLOCKING: the faces' BOUNDS withheld the status-flip grant): restated on all 14 faces @de8693863c; all 14 orders flipped complete at HEAD. W1-S3 (the faces named the proof instance by the short stem the gate does not glob), carrying W2-S2 and W3-S2 as the same defect: all 14 faces name the gate's form @83d8175729; 14 instances VALID at the issuer's seat. W2-S3 (a single-call filter-log-events under the CLI v1 shim returns 1 of 3 with an unfollowed nextToken): the criterion's instrument was the worker's paginating script, S11-AC3 stands at 3 of 3 @108d9fa67f; a cut lesson for any face naming that verb. W2-S4 (the port contract's bare-script battery crashes pytest at collection): EG-s-2's S2-AC1 named real test functions and shipped ten @2baa6af162; the inf-source half rides on W2-S1. W2-S5 (BLOCKING: record-terraform-deploy.sh writes a CHANGELOG path the narrow grant did not name): the grant widened by that one path @75985f2068 and the worker's split commit stands. S3 (the --gate seam no cell owned): TO-EG-s-8 gained deliverable item 5 and criterion S8-AC9 @446a064491, and _render_command at HEAD passes --gate at :227 (this seat's read). W2-S6 (a probe invoke against Inflection would write a real slice): contained in the gate -- render_month_end.py :821-825 never probes Inflection, its uncovered days classify UNKNOWN to rung 1 (this seat's read); the durable probe-key handling in inf-etf-ownership-daily is outside this project and is named to the CTO with W2-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The issuer's disarm commits are ancestors of HEAD and are cited by the packet s.4 with the act each performed; this seat re-read the world each act changed rather than the commit message: the vendored-copy census and the layer list (W1-S1); the 14 `<status>complete` lines and the 14 VALID instances at the issuer's seat (W1-S2, W1-S3); the orchestrator's :227 (S3); the gate's :821-857 (W2-S6); the served bd-49f hash and the widened grant's CHANGELOG path in the drained tree (W2-S5); the S11 record's 3-of-3 by the paginating instrument (W2-S3); EG-s-2's ten test functions in the instance (W2-S4).",
        "W2-S2 and W3-S2 describe the identical defect W1-S3 describes (the short proof stem against the gate's full-stem glob), filed by three workers on three orders of one issuance; one carrier per hazard -- W1-S3 carries it, the other two are dismissed as duplicates at C-S4 with this row cited.",
        "Coverage of the issuance-wide defects (W1-S2, W1-S3): the remedy was applied to the population (all 14 faces), not to the member that reported it -- the shape the NFRA_OUTSET issuer named on its own round and this issuer applied correctly here."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ETFS_GUARDRAIL-W1-S1",
      "ETFS_GUARDRAIL-W1-S2",
      "ETFS_GUARDRAIL-W1-S3",
      "ETFS_GUARDRAIL-W2-S3",
      "ETFS_GUARDRAIL-W2-S4",
      "ETFS_GUARDRAIL-W2-S5",
      "ETFS_GUARDRAIL-S3",
      "ETFS_GUARDRAIL-W2-S6"
    ],
    "spec_asserts": "Annex section 3: an ARMED hazard disarms via the row's disarm_owner; section 5: a graduated row whose remedy was executed inside the round by its owner carries REMEDIATED and DISARMED with the exercised remedy cited. S3's remediation row in ../remediations/REMEDIATION_v1.md carries those clocks; the seven worker-form items carry them on this row.",
    "world_is": "Eight hazards this round surfaced were remedied by the issuer's own amendments and the workers' compliant acts before the round closed; each is verified against the world at this seat. None asks anything of the next round.",
    "notes": "Worker-form items carry their clocks here rather than on remediation rows because a remediation row keyed by W<n> is not a coordinate the CVO mints on the main index (the gate's W- arm grades the committer's slot); the annex's next revision should say so in section 5."
  }
]
```

## C-S3 -- adjudicates the three items GRADUATED and OPEN: W2-S1 (the inf source's dead battery, the CVO's routed item), W1-S5 (build-zip.sh's month-00 defect, an estate CI script) and S2 (the false CRLF drift and the missing eol rule); owners named for the CTO's routing

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S3",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T10:40Z",
    "one_line": "L9: ADJUDICATES three items -- GRADUATED, remedy OPEN, each outside this project's write surface and routed by name in the slug. W2-S1 (disarm_owner 3.0.0_SA_CVO, 'routes the re-vendor'): inf-etf-ownership-daily's own battery test_catchup_scan.py crashes at import (KeyError: ASSETS_BUCKET) since the 2026-08-03 repoint and has been dead ~32 days; EG-s-3's bound forbade editing the port source, so the remedy -- re-vendor the battery against the repointed shape, with W2-S4's shape lesson (real test functions, no module-level sys.exit) -- belongs to the inf-pipeline lane, which the CTO names at L10; the round's own port contract was built from the live bytes, not the dead test, so no deliverable of this round rests on it. W1-S5: infra/aws/lambda/ci/build-zip.sh:66 hardcodes touch -t '202600010000' (month 00) and fails rc=1 on every invocation since e046072434 (2026-02-19); the round's deploying faces used build-and-upload.sh, which has zero callers of it, so this round was not exposed; the script is a shared CI surface (lane CLOUD_OPS_OR_ETL per the packet) and the fix is one literal. S2: the aws_instance.reporter user_data 'drift' that stopped two orders was a CRLF checkout artifact on this core.autocrlf=true box (live sha1 e47b615c equals the LF rendering of instance.tf at HEAD; the plan's 434774b5 is the CRLF rendering); the issuer's disarm normalised every worktree at hand-off, which protects this round only -- .gitattributes at HEAD carries no *.tf rule (this seat's read), so the durable remedy (`*.tf text eol=lf`) is OPEN and repo-wide, owner 1.0.0_SA_CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (routes W2-S1 and W1-S5 to their lanes at L10; owns the .gitattributes rule for S2)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W2-S1 at HEAD (0.9.0_WK_ETFS_GUARDRAIL~2): rc=2 at collection, KeyError 'ASSETS_BUCKET', the battery stubbing the pre-repoint env and helper names; the repoint 001a73530a read at this seat carries the 15,130-byte lambda_function.py that HEAD still carries, while the DEPLOYED function runs the 12,141-byte pre-repoint file (C-S1's zip read) -- so the dead battery and the un-applied repoint are two faces of one state: the source moved, the test did not, the deploy did not.",
        "W1-S5 at HEAD (0.9.0_WK_ETFS_GUARDRAIL~1): the literal at build-zip.sh:66 and the rc=1 on every invocation; the packet's measurement that build-and-upload.sh has zero callers of build-zip.sh under infra/aws/lambda/ci/, so both port deploys and the orchestrator deploys never ran it; only TO-EG-s-12's face named it and its named fallback was used.",
        "S2 at HEAD (2.0.0_SA_COO~B): the two sha1s and the 414-of-414 CRLF checkout in a fresh worktree; `git show HEAD:.gitattributes` at this seat -> no line matching 'tf' -- the rule the packet lists for the CTO's read is not landed."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ETFS_GUARDRAIL-W2-S1",
      "ETFS_GUARDRAIL-W1-S5",
      "ETFS_GUARDRAIL-S2"
    ],
    "spec_asserts": "EG-s-3's bound ('PORT SOURCE. Relied on, NOT owned -- do not modify to suit the port'); CLAUDE.md rule 14 (every .py edit passes the commit gate) for the CI script; the estate's line-ending discipline for Terraform files on an autocrlf box.",
    "world_is": "Three defects this round found live outside its write surface: a dead battery on a producer this project relies on, a CI script that fails on every call, and a repository without an eol rule for the files whose plans it grades. S2's remediation row carries its clocks; W2-S1 and W1-S5 carry theirs here, OPEN, until the lanes the CTO names act.",
    "notes": "The CVO's routing act on W2-S1 is this row and the slug: the remedy is named, the owner is the inf-pipeline lane by the CTO's naming, and the disarm is one green run of the re-vendored battery at HEAD, read at this seat. W1-S5's disarm is one successful build-zip.sh invocation at this seat after the literal is fixed. S2's disarm is one fresh worktree on this box whose .tf files check out LF, read at this seat."
  }
]
```

## C-S4 -- adjudicates the ten records DISMISSED_WITH_REASON: S1, W3-S1, W1-S4, W1-S6, W1-S7, W1-S8, W1-S9, W1-S10, and the two duplicates W2-S2 and W3-S2

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S4",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T10:45Z",
    "one_line": "L9: ADJUDICATES ten rows -- DISMISSED_WITH_REASON, each a record rather than an item, none opening anything. S1: the issuer's design record that the ETFS layer holds no firm-bucket grant so the discriminator is a non-writing probe delegated to the firm-scoped producers -- for the CTO's L10 read, INERT. W3-S1: the CSVs are written by a separate call path; resolved in the order's own change (S13-AC3/AC4 exercised it). W1-S4: one IAM read outside TO-EG-s-12's enumerated surface, disclosed, not relied on for the graded answer. W1-S6: the gitignored terraform binary absent in a fresh worktree; RULED by the issuer (provisioned at hand-off; PATH substitution forbidden on deploying faces); the three remote states carry terraform_version 1.9.8 by the issuer's read. W1-S7 and W1-S8: two correct STOPS on a plan that read 2 to change; the premise (a real user_data drift) was false, as S2 measured, and the targeted applies changed exactly what they meant to. W1-S9: the census expect amended from 2 to 3 because EG-s-8 had lawfully added the third header site; S9-AC2 PASS by its measured value under @e32bdf96ea. W1-S10: a second apply before its ledger entry, disclosed and remediated the same turn with a supplementary entry closed with proof @5fb0fb7de0 -- the NEVER-2 sequencing lesson rides to the analysis. W2-S2 and W3-S2: the proof-stem defect W1-S3 carries, dismissed as duplicates with C-S2 cited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Each row read at HEAD in full at this seat; the packet s.4's standing for each read beside it; where the row's substance is a world state this seat re-read it (W1-S8's REPORTER_INSTANCE_ID on the orchestrator's env, live; S2's false drift underlying W1-S7 and W1-S8, C-S3; the three send/header sites underlying W1-S9, C-S1).",
        "W1-S6's binary claim is the issuer's read (the three remote states at 1.9.8); this seat did not re-read the remote states and says so -- the dismissal rests on the ruling's shape (a provisioning act at hand-off), not on the version claim."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records of acts, stops, disclosures and rulings already on the record, or duplicates of an item carried elsewhere; none names a hazard that outlives the round.",
    "adjudicates": [
      "ETFS_GUARDRAIL-S1",
      "ETFS_GUARDRAIL-W3-S1",
      "ETFS_GUARDRAIL-W1-S4",
      "ETFS_GUARDRAIL-W1-S6",
      "ETFS_GUARDRAIL-W1-S7",
      "ETFS_GUARDRAIL-W1-S8",
      "ETFS_GUARDRAIL-W1-S9",
      "ETFS_GUARDRAIL-W1-S10",
      "ETFS_GUARDRAIL-W2-S2",
      "ETFS_GUARDRAIL-W3-S2"
    ],
    "spec_asserts": "Spine v3.2 L9: the census counts the investigation document's rows as items and reads the adjudication document for their dispositions, so every row needs one even when it names no hazard.",
    "world_is": "Ten rows describe acts and states already resolved on the record; with C-S2 and C-S3, 21 of 21 rows are dispositioned and the L10 precondition is met on the investigation plane.",
    "notes": "For the CTO's analysis from these records: two stops on a false premise cost two orders their untargeted applies (S2's eol rule closes that class); one ledger-sequencing deviation was self-repaired (W1-S10); the round's issuance defects were repaired on the population, not the member (W1-S2, W1-S3)."
  }
]
```

## C-S5 -- a correction of this seat's own framing: the CTO's L10 @0557afa38a grades FWD-4 NOT_EVALUATED, and the slug's list of fire-gated outcomes was six where the analysis reads seven; the cell's PASS stands, the outcome's state does not follow from it

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S5",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T10:40Z",
    "one_line": "A correction record, cited against C-S1 and the slug of 10:21Z. The CTO's L10 analysis (org/missions/D8/ETFS/ETFS_GUARDRAIL/ledger/ROUND_ANALYSIS.round1.md @0557afa38a; dep_stage now ROUND_CLOSE; 8 of 8 outcomes served, no addendum) grades FWD-6 REALIZED and seven outcomes NOT_EVALUATED. This seat's slug named six outcomes as waiting on scheduled fires (FWD-1, -2, -3, -5, -7, -8) and left FWD-4 reading as gradable now, because S4-AC7 passed. That was a conflation of two questions the spine keeps apart: the CELL (the classifier's taxonomy, graded PASS at C-S1 and undisturbed) and the OUTCOME (FWD-4's DONE WHEN is EXERCISED -- 'the system has ACTUALLY MET such a day and left it alone' -- on a real market-shut day or a real unpriced partner file). Every B-class proof on the record is a unit test with a synthetic fixture, which is APPLIED; the round's live evidence (August refused with five holes, August published clean) exercises C, UNKNOWN and D, not B. The CTO's grade is right on Rule 22's STATE axis and this row carries it into this document so C-S1's world_is is read with seven fire-gated outcomes, not six. The discriminator, so it is graded the day it exists: a legitimately-empty day appearing in a live render's expected_empty with holes unaffected and nothing written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO 94367 and ledger/ROUND_ANALYSIS.round1.md @0557afa38a, in HEAD at this seat; org/missions/D8/ETFS/ETFS_GUARDRAIL/project.json at HEAD reads dep_stage ROUND_CLOSE (the CTO's flip, spine :347).",
        "C-S1's grade of S4-AC7 (PASS on the taxonomy's four postulates, the module's absent write surface and the recorded sums) is not disturbed; what this row corrects is the outcome-level sentence in C-S1's world_is and in the slug, which listed six fire-gated outcomes.",
        "The distinction the correction rests on is the estate's own: a cell's PASS certifies the instrument; an outcome's REALIZED certifies the world met the condition; a fixture that represents the condition scores the instrument, not the world (CLAUDE.md section 4 and the memory rule 'a fixture that cannot represent the failure cannot score it')."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correction record about this seat's own framing; it adjudicates no item and opens nothing. The CTO's instrument note adoption (worker-form clocks on adjudication rows; annex section 5) is also recorded here as carried by the CTO.",
    "spec_asserts": "Spine v3 L10: the CTO grades outcomes (REALIZED / NOT_REALIZED / NOT_EVALUATED) on the slug and the artifact; L9 grades criteria. FWD-4's DONE WHEN as cut: EXERCISED.",
    "world_is": "ETFS_GUARDRAIL round 1 is at ROUND_CLOSE: FWD-6 REALIZED; FWD-1, -2, -3, -4, -5, -7, -8 NOT_EVALUATED pending real fires and a real legitimately-empty day. Three open items carry owners: W2-S1 the inf-pipeline lane, W1-S5 CLOUD_OPS_OR_ETL, S2 the CTO's own queue.",
    "notes": "Scope of the retraction, stated so it is not read wider: the slug's grades, dispositions, precondition measurement and open-item routing stand; the single refuted clause is the count and membership of the fire-gated outcome list, which now includes FWD-4."
  }
]
```

## C-S6 -- adjudicates S4: GRADUATED, remedy OPEN at 0.2.0_DT_PortfolioAnalytics (the deploy_ledger NEVER-2 defect); the remediation row is ../remediations/ S4

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S6",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T00:23Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": [
      "ETFS_GUARDRAIL-S4"
    ],
    "disarm_owner": "0.2.0_DT_PortfolioAnalytics",
    "one_line": "L9-shaped act mid-round (the issuer's and the CTO's ask, 94794 / 94796): ADJUDICATES one seat-form item -- GRADUATED, remedy OPEN, owner 0.2.0_DT_PortfolioAnalytics. S4 (this seat's row on the mechanism W1-S16 measured): .tools/deploy_ledger.py re-renders the change_management entry from the sentinel on every open / close-leg / close / hold and writes it truncate-and-replace, so the NEVER-2 section a deploy must hand-append (sign-off ids, served keys, archive, rollback) is deleted by the next tool call with no warning -- measured 5 of 5 -> 1 of 5 -> 5 of 5 by the worker, the mechanism read at :239-250 and :289-291 by this seat. The remediation row ETFS_GUARDRAIL-S4 carries the remedy (a sentinel field the renderer emits, or a preserved hand section, and a printed diff either way), the interim (the issuer's ordering clause), and the disarm (a round-trip through the tool leaving a hand-appended section byte-equal, planted both ways). W1-S16 itself is dispositioned at the round-2 L9 when its branch drains; this row does not adjudicate it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S4 (this write) and its evidence; W1-S16 on wk-etfs_guardrail-2-1; deploy_ledger.py :239-250, :289-291 at HEAD 104c46c48a; 94794, 94796."
      ]
    },
    "spec_asserts": "NEVER-2 and TO-EG-s-14's entry clause (the entry CARRIES the halves, keys, archive, rollback); the tool renders the entry from a sentinel with no such field.",
    "world_is": "A law that requires content the tool cannot carry, and a tool that deletes the content when it is carried by hand.",
    "notes": "Seat-form item; its clocks live on the remediation row S4. The round-2 L9 reads W1-S16 and the GUARDRAIL faces' ordering clause against this row."
  }
]
```

## C-S7 -- CORRECTION of C-S6 and of commit 8bbfc0e684's subject: NO remediation row was minted (the gate refused it as an L10-shaped act with 5 of 19 orders open; not overridden); S4's graduation, owner, remedy, interim and disarm stand on C-S6; the remediation row is minted at the round-2 L9

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S7",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T00:39Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correction record of this seat's own C-S6 and of commit 8bbfc0e684's subject; it dispositions no investigation item.",
    "one_line": "CORRECTION, this seat's own: C-S6 says 'The remediation row ETFS_GUARDRAIL-S4 carries the remedy ...' and 'its clocks live on the remediation row S4', and commit 8bbfc0e684's subject says the remediation row was 'minted OPEN against 0.2.0_DT_PortfolioAnalytics'. NO REMEDIATION ROW WAS MINTED. The first attempt (three files) was REFUSED by .tools/surprise-row-gate.py: 'ETFS_GUARDRAIL-S4: NEW remediation row (the slug (spine v3: every new remediation row)) while 5 of 19 task order(s) under ETFS_GUARDRAIL are NOT terminal at HEAD' -- a new remediation row is an L10-shaped act and round 2's five orders are open -- and this seat chose NOT to take the audited override: the gate's reason is right in kind. ../remediations/REMEDIATION_v1.md was restored to HEAD (4,266 bytes, unchanged from c6bcb7b12b, verified by git diff --stat) and the second attempt committed S4 and C-S6 only. The patch that was to re-point C-S6's text and the commit message at the L9-minted row failed on its own assertion before writing, and the commit went through with the stale text -- found on re-reading the committed blob, not caught before. WHAT STANDS: S4 (its notes already say the remediation row waits for terminality), C-S6's GRADUATION of S4 with owner 0.2.0_DT_PortfolioAnalytics, the remedy (a sentinel field the renderer emits, or a preserved hand section, and a printed line naming every section dropped), the interim (the issuer's ordering clause) and the disarm (a round-trip through the tool leaving a hand-appended section byte-equal, planted both ways) -- all recorded on C-S6 and S4. WHAT CHANGES: the clocks ride C-S6 until the REMEDIATION row S4 is minted at the round-2 L9 once every ETFS_GUARDRAIL order is terminal. The lesson, banked: a patch-then-commit chain must abort the commit when the patch fails, and the committed blob is what is read back, not the working copy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The gate's refusal, verbatim from the first attempt's captured output: 'ETFS_GUARDRAIL-S4: NEW remediation row (the slug (spine v3: every new remediation row)) while 5 of 19 task order(s) under ETFS_GUARDRAIL are NOT terminal at HEAD: ...TO-EG-s-14 [pending], TO-EG-s-15 [pending], TO-EG-s-16 [pending], TO-EG-s-17 [pending] ...; override (audited): put # surprise-row-override: <reason> in the commit message body'. Not taken.",
        "git show 8bbfc0e684:.../adjudications/ADJUDICATION_v1.md -> C-S6 one_line contains 'The remediation row ETFS_GUARDRAIL-S4 carries' (True); git diff --stat c6bcb7b12b HEAD -- .../remediations/REMEDIATION_v1.md -> empty (the file is unchanged; no S4 row in it); 8bbfc0e684's subject begins 'remediate(ETFS_GUARDRAIL S4 / C-S6 ...) ... minted OPEN against 0.2.0_DT_PortfolioAnalytics'.",
        "S4 as committed: notes 'the REMEDIATION row with its clocks is minted at the round-2 L9 once every ETFS_GUARDRAIL order is terminal -- the row gate refused it tonight as an L10-shaped act ... rightly' (the patch that succeeded)."
      ]
    },
    "spec_asserts": "Spine v3 (the gate's own words): every new remediation row waits for terminality. ADJUDICATION_v1.md's header: a correction is a NEW row citing the old id; no row is edited.",
    "world_is": "C-S6 and the commit subject overstate by one row; the remediation file is unchanged; the owner, remedy, interim and disarm are on the record where they were written.",
    "notes": "Append-only: C-S6 is not edited; a reader resolves S4's remediation state from this row (the newest citing it) until the round-2 L9 mints the remediation row."
  }
]
```

## C-S8 -- S17-AC2 graded PASS: cottonwood 2026-09-08 filled by the producer's own fire with the rule's own envelope; the 76-minute race the log proves; the window's shipped-signal terminus; the catch-up branch honestly unexercised -- this seat's head-object, listing and CloudWatch reads agree

```json
[
  {
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T00:58Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ETFS_GUARDRAIL-C-S8",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record; it dispositions no investigation item.",
    "one_line": "L9 on the round-2 PARTIAL packet @8f7bf86815 (TO-EG-s-17 terminal, drained @d1b8945948; 1 of 5 orders): the GRADE for S17-AC2, the filled-in day read as a person reads it -- PASS. THE READING GRADED (the-filled-in-day.result.md ss.0-2, 6-9): cottonwood's ETF-ownership slice for Tuesday 2026-09-08 was missing and is now there -- DIVZ 19,079,942.93 / IDVZ 15,516,123.03 / PFDE 12,430,725.84 / PFOE 6,614,559.95, total 53,641,351.75 across 330 / 331 / 320 / 319 accounts, written by the producer's OWN run with its rule's own default envelope (Target.Input absent on 0 of 2 targets across 2 of 2 daily rules; no date key) at 23:15:51Z, request 0840a0d3. WHY IT WAS MISSING, and the log says it: the cot schedule fires at 10:30Z and the fact_holdings partition for date D lands D+1 at ~11:46Z (10 of 10 dates sampled), so the D+1 fire runs 76 minutes early, the never-fabricate skip takes it, and today's own 10:30:25Z scheduled fire wrote 2026-09-04 while 2026-09-08's source landed 76 minutes later -- the newest trading day is sliceless ~11.5 h every day, a design race the CTO has TAKEN for the L10 (94796 (2a)). THE WINDOW WAS RESPECTED: the terminus is the SHIPPED signal (head-object on the previous month's etf_ownership.pdf, present at the worker's read: 273,857 B, 2026-09-01T17:38:41Z), no day-count constant exists in either producer, class B (priced == 0) was never fired at. WHAT THE TOKEN DOES NOT CLAIM, printed beside it: CATCHUP-BRANCH-NOT-EXERCISED -- the catch-up sweep skips the newest partition as skip_date, so a head-of-window hole is recovered by the main path and `catchup_processed` is structurally empty for it (0 CATCHUP lines in 152 cot / 103 bd log events over 30 days); exercising the branch needs a hole OLDER than the newest partition, the estate has none (the census: 20 trading days x 2 partners, 1 absent, the one the newest), and manufacturing one is a served S3 delete under Andrew's word (W2-S8 -> the issuer's /open-calls card, REC yes one cot slice; the CTO concurs). THIS SEAT'S OWN INSTRUMENTS AGREE: s3api head-object daily/cottonwood/2026-09-08.json -> 1,345 B, ETag 5da999e2fbfadfe302df35ef24407372, LastModified 23:15:52Z (unchanged after the worker's three pass-2 runs and this read at 00:4xZ); a live list of both prefixes over the window -> cottonwood 19 of 19 dates 08-12..09-08 PRESENT (09-08 at 23:15:52Z, every other at its D+2 10:30:30Z or the 09-01 16:50Z catch-up), 49financial 19 of 19 (each at D+1 10:45:1xZ) -- the race is visible in the timestamps themselves: cot's slices land two days after their date, bd's one; the producer's own CloudWatch log 23:00Z-00:26Z -> the probe START ec6e9232 at 23:15:40.735Z with Init Duration 2,974 ms (cold), the fire START 0840a0d3 at 23:15:50.560Z with NO Init (warm, 673 ms), then three probe invocations at 23:39:29Z (cold), 23:39:33Z and 23:40:03Z (W2-S9's 2026-07-31 and Sunday controls) and no other -- one fire, no second write, exactly as recorded. ONE VINTAGE FACT for EG-s-14's grade, not this one: the terminus object platinum/reports/2026-08/etf_ownership.pdf read at 00:4xZ is 252,393 B, LastModified 2026-09-10T00:24:48Z -- EG-s-14's August re-render has landed on the served key since the worker's read; the shipped signal still exists, so S17's window logic is unchanged. VERDICT PASS. THE FWD-1 READING for the CTO's L10, as the packet asks: the outcome -- a missed day caught up by the producer's own fire, nothing fabricated, the date named by the producer -- is REALIZED in substance for the hole class the estate actually produces every day (head-of-window), by the MAIN PATH; the FWD's letter ('named in catchup_processed') is NOT met and cannot be for that class on the deployed code. The L10 chooses: accept the main-path form as FWD-1's realization for head-of-window holes with the branch exercise placed behind Andrew's word, or hold FWD-1 on the branch. This seat's REC: the former -- and the real remedy is the cadence row the CTO already took (fire AFTER the 11:46Z landing, or exclude the unlanded day and say so), which both closes the daily hole and makes the catch-up branch reachable for ordinary holes.",
    "grades": [
      {
        "criterion": "S17-AC2",
        "instance": "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-17.the-filled-in-day.proof_of_spec.json@1e995e83b5",
        "verdict": "PASS",
        "reason": "Every question the criterion asks is answered on the record with a vintage: the partner, the date and the rows; the measured race that explains the absence and today's own scheduled-fire log proving it; the shipped-signal terminus and the absence of a day-count; class B untouched; the census proving exactly one hole and the row routing the controlled path to Andrew. This seat's head-object, live prefix listing and CloudWatch reads agree on the slice, the census and the one fire. NO verdict was recorded by the assignee."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L8_PACKET.round2.partial.md @8f7bf86815 (58 lines, sha256 b75d1cf2f7cc5805...) ss.1-3, 5; the proof @1e995e83b5: S17-AC1 PASS 7 of 7 arms (hole census 40 cells / 1 absent; Target.Input 0 of 2; START RequestId 1 of 1; the OK: wrote line 1 of 4; head-object 1345 B; positive control 2026-09-04 0 of 4; cot 30 of 30 at 10:30:24Z, bd 30 of 30 at 10:45:05Z; COVERAGE-ABSENT printed); S17-AC2's output_evidence and denominator.",
        "the-filled-in-day.result.md (364 lines): s.0 the one-line answer and the arm table; s.1 the census (20 trading days incl. Labor Day excluded; cottonwood 61 keys / 1 absent, 49financial 89 / 0; the wider 26-day span the same 1); s.2 the rule's payload read live (no Input, no RoleArn); s.6 the schedules from history and the cold-start reading; s.7 the race, 10 of 10 dates, today's fire's log verbatim; s.8 the window (lambda_function.py@4155c85a1f:180-191); s.9 what the worker did not do.",
        "This seat, 00:4xZ: s3api head-object opal-data-etfs daily/cottonwood/2026-09-08.json -> 1345, \"5da999e2fbfadfe302df35ef24407372\", Wed, 09 Sep 2026 23:15:52 GMT, VersionId None; list-objects-v2 daily/cottonwood/2026-0 and daily/49financial/2026-0 filtered to 08-12..09-09 -> 19 + 19 keys with LastModified as in one_line; logs filter-log-events /aws/lambda/cot-etf-ownership-daily 23:00Z-00:26Z filter RequestId -> 15 events: START/END/REPORT for ec6e9232 (Init 2974.26 ms), 0840a0d3 (no Init, 673 ms), 26696b84 (Init 3228 ms), 600f6b5b, 948f947d; head-object platinum/reports/2026-08/etf_ownership.pdf -> 252393, Thu, 10 Sep 2026 00:24:48 GMT.",
        "W2-S7, W2-S8, W2-S9, W2-S10 and the issuer's S5..S9 read whole at HEAD 866d2ed808; 2.0.0_SA_COO 94794/94805; 1.0.0_SA_CTO 94796 (the race taken for the L10; the served-delete call put to Andrew)."
      ]
    },
    "spec_asserts": "S17-AC2 as cut (judgment, NO verdict): the recovered date as a person reads it; why it was missing if the log says; that the port respected the reporting-obligation window (terminus a shipped signal, no day-count); that class B was never fired against; if no real hole existed, the census and the routing row. PRD v0.4 S17 / FWD-1: a missed day caught up by the producer's OWN fire on a REAL hole, the recovered date named.",
    "world_is": "One real hole existed and was filled by the producer's own fire with the rule's own envelope; the hole exists every day for ~11.5 h because the schedule fires before the source lands; the catch-up branch is unreachable for that hole class and unexercised; the only way to exercise it is a served delete no agent may perform.",
    "notes": "FOR THE L10: FWD-1's letter vs substance (above); the cadence row already taken; the served-delete call at Andrew. FOR EG-s-14's grade: the August report was rewritten on the served key at 00:24:48Z (252,393 B) -- read against the archive and the sign-off halves when that packet lands. Round 2 judgment criteria graded: 1 (S17-AC2) of the round's five orders' worth; four orders open."
  }
]
```

## C-S9 -- adjudicates W2-S7, W2-S8: GRADUATED -- W2-S7 closed on the re-cut onto instruments that exist; W2-S8's criterion half closed on S9, the race underneath OPEN at 1.0.0_SA_CTO (the cadence row)

```json
[
  {
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T00:58Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ETFS_GUARDRAIL-C-S9",
    "disposition": "GRADUATED",
    "adjudicates": [
      "ETFS_GUARDRAIL-W2-S7",
      "ETFS_GUARDRAIL-W2-S8"
    ],
    "disarm_owner": "1.0.0_SA_CTO",
    "one_line": "L9: ADJUDICATES two items -- GRADUATED. W2-S7 (BLOCKING/INERT: S17-AC1 arms (c) and (g) named a CloudTrail `Invoke` record no trail in the account writes -- lambda:Invoke is a data event and 0 of 2 trails select AWS::Lambda::Function, proven by a positive control returning 0 Invoke records for two real invocations): CLOSED on the issuer's re-cut @5507841f04 of all five faces onto instruments that exist (the log group's START RequestId by time; the cold-start AssumeRole at the cron instant as corroboration; the Invoke read printing COVERAGE-ABSENT, never graded), judged HARDER on effect -- and the shape (an accept naming an instrument without its coverage fact) is the same cut defect as NFRA_OUTSET-S29, the third of the night, now asked at every cut as the substrate-card coverage question. W2-S8 (BLOCKING/ARMED -> the issuer; disarm record S9): the criterion half is CLOSED -- arm (d) accepts the main path's own OK: wrote line for a head-of-window hole and prints CATCHUP-BRANCH-NOT-EXERCISED, arm (b) no longer asks for a date key that routes past the sweep -- and the FINDING underneath stays OPEN with owner 1.0.0_SA_CTO: the 76-minute schedule/landing race (cot's 10:30Z fire before the D+1 ~11:46Z partition; bd's 10:45Z floor deliberately 29 minutes after its 10:16Z landing has no race and 0 of 20 absent) leaves the newest cot trading day sliceless ~11.5 h every day and makes the catch-up branch unreachable for the ordinary hole; the CTO took it for the L10 addendum (94796 (2a): the fire follows the partition, or the window excludes the unlanded day and says so). The remedy is a Terraform act in the DT/AE lane on the rule's cron, not a code change; the disarm is one scheduled fire after the change whose own log names date D on D+1, read from history.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W2-S7 and W2-S8 read whole; S9 (the disarm record); the amended face @5507841f04 (arms b, c, d, g); the result record s.6-7; 1.0.0_SA_CTO 94796 (2a) and (2b); this seat's live listing (cot slices at D+2 10:30:30Z, bd at D+1 10:45:1xZ)."
      ]
    },
    "spec_asserts": "S17-AC1 (c)/(g) as first cut; PRD v0.4 S17 / FWD-1; the standing authority @9f4a57262f (a re-cut judged on EFFECT). Rule 28 q5: an accept that names an instrument names its coverage.",
    "world_is": "The instrument defect is remedied on the faces; the race is measured, taken for the L10, and unremedied at the schedule.",
    "notes": "Worker-form items; W2-S7's clock closes on this row; W2-S8's rides it OPEN at the CTO. The served-delete call for the branch exercise is Andrew's, at the issuer's /open-calls."
  }
]
```

## C-S10 -- adjudicates W2-S9, W2-S10, S5..S9: DISMISSED_WITH_REASON, records (a stale docstring carried named; the no-RoleArn correction; five acks consumed)

```json
[
  {
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T00:58Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ETFS_GUARDRAIL-C-S10",
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "ETFS_GUARDRAIL-W2-S9",
      "ETFS_GUARDRAIL-W2-S10",
      "ETFS_GUARDRAIL-S5",
      "ETFS_GUARDRAIL-S6",
      "ETFS_GUARDRAIL-S7",
      "ETFS_GUARDRAIL-S8",
      "ETFS_GUARDRAIL-S9"
    ],
    "one_line": "L9: ADJUDICATES seven rows -- DISMISSED_WITH_REASON, records. W2-S9 (INERT: the cot producer's deployed docstring still calls 2026-07-31 a known upstream gap while the deployed probe answers partition=true, priced=10960, output_exists=true, with a Sunday as the negative control): a stale comment in an authoritative file, off-task, no behaviour depends on it -- carried NAMED to the L10 as a one-line re-dating for the cot producer's owner, not cut here. W2-S10 (INERT: the amendment's 'the rule's role's AssumeRole' names a field the two daily EventBridge RULES do not carry -- 0 of 2 targets have a RoleArn; they invoke through the function's resource policy; the AssumeRole CloudTrail names is the EXECUTION role's cold start, identical for a rule and a person, 2 in the fire's minute from the probe's cold start and 0 inside the fire itself): the issuer's model corrected at the source and EG-s-18 re-cut on it @116f6a763d; the arms held at the finer grain (invocation interval + cron instant, every event attributed). S5, S6, S7, S8 (the issuer's disarm records for W1-S11 the renderer's import fix as a new leg of the held entry, W1-S12 the archive moved outside the enumerated prefix, W1-S14 the synchronous invoke with --cli-read-timeout 0, W1-S16 the ordering clause with the tool defect carried to this seat -- now ETFS_GUARDRAIL-S4 / C-S6 / C-S7): consumed; the W1 rows themselves are on worker ~1's branch and are dispositioned when it drains. S9 (the disarm record for W2-S8): consumed by C-S9.",
    "dismissal_reason": "Records: two instrument/comment facts carried named, and five acks consumed by the closures and carries they evidence; nothing armed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W2-S9, W2-S10, S5..S9 read whole at HEAD 866d2ed808 (comp-surprise --project ETFS_GUARDRAIL --json: investigation_items 31, open 9, adjudication_rows 7 before this write); W1-S11..S16 on wk-etfs_guardrail-2-1 (not on CLOUD; W1 on CLOUD: none)."
      ]
    },
    "spec_asserts": "The channel's taxonomy: an ack is a record; an item closes when its remedy is on the shared branch.",
    "world_is": "Two facts of the round's instruments and one deployed comment; five acks evidencing closures whose items are on CLOUD (W2-S8) or on a worker's branch (W1-S11..S16).",
    "notes": "Investigation items without a disposition after this write, by comp-surprise's definition: 0 of 31 on CLOUD (W1-S11..S16 arrive with ~1's drain). The slug waits for the FINAL packet (EG-s-14, -15, -16, -18 open)."
  }
]
```
