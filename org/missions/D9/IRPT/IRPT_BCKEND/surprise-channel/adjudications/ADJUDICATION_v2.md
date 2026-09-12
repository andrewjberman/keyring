# IRPT_BCKEND round 2: CVO adjudication

Partial L9 intake for RT5 at worker tip `8d173559747f875ea751eeaea898de2b241ed8e7`. This document will accumulate CVO review as round-two evidence arrives; it is not an L10 slug. Review details: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md`.

```json
[
  {
    "id": "IRPT_BCKEND-C-S79",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:25:15Z",
    "one_line": "RT5-AC2 passes the requested disclosure record; the two-file bundle does not establish an executable host or a scheduled run.",
    "class": "OBSERVATION",
    "spec_asserts": "RT5-AC2 asks for a judgment record of bundle completeness, execution host and its dependencies, and the limits of the served artifact; the worker must leave this criterion ungraded.",
    "world_is": "The pinned instance records two files, zero bundled dependencies, zero identified hosts, unmeasured host dependencies and zero runner execution. It leaves RT5-AC2 UNVERIFIABLE-BY-INSTRUMENT for the named CVO. Independent source and path checks substantiate the limitation, with corrections recorded in the linked review.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md@8d173559747f875ea751eeaea898de2b241ed8e7 (RT5-AC2; BOUNDS excludes production runner execution)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; source hashes, checker result and corrections)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "RT5-AC2",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7",
        "verdict": "PASS",
        "reason": "The issued RT5-AC2 asks the worker to state deployment scope and limits, rather than execute the runners (expressly excluded by BOUNDS). The record clearly states that the bundle contains only two files, that the execution host and its dependency availability are undetermined, and that deployment proves no scheduled run. PASS applies to that disclosure record only. The two-file tarball is not established as a sufficient standalone execution unit: host identity, third-party packages, first-party modules, schemas/configuration and the silver registry remain unverified. Read the path-expression, dynamic-import census, consumer-search and fixed-key qualifications in IRPT_RT5_L9_REVIEW_20260911.md with this grade. No RT5-AC1 truth verdict, whole-order acceptance, CLOUD merge, or runtime readiness follows from this grade."
      }
    ],
    "notes": "Pinned worker-branch review while 8d173559747f875ea751eeaea898de2b241ed8e7 is not an ancestor of observed CLOUD 0ecf25f1ca604fcdb15f7e73241d351966e75505. No worker artifact or frozen task-order face was changed. This partial round-two record is not an L10 slug."
  },
  {
    "id": "IRPT_BCKEND-C-S80",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:25:15Z",
    "one_line": "RT5-AC1(a)'s green-test bar is replaced by matching red baseline counts, and the invoked battery omits the 55-file tools suite.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "spec_asserts": "RT5-AC1(a) requires the guard's self-test and .tools/tests/ to pass, with counts printed. BOUNDS also names the self-test as a control and freezes the specification mid-round.",
    "world_is": "At the pinned worker tip the instance labels RT5-AC1 PASS while reporting FAIL 3/18, FAIL 7/14, and 47 PASS / 8 FAIL of 55. battery_ib_rt_5.py:55-56,111-125 accepts equality with the two red failure-count tuples; it neither compares failing-case identities nor invokes the 55-file .tools/tests/ suite. Preserving a red baseline is evidence of a bounded control, not satisfaction of the issued green-test bar.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md@8d173559747f875ea751eeaea898de2b241ed8e7 (lines 63,75,87-88)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py@8d173559747f875ea751eeaea898de2b241ed8e7 (BASELINE and arm (a), lines 55-56 and 111-125; full 220-line source read)",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7 (RT5-AC1 output and denominator explicitly disclose the changed bar)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; read-only verification and limits)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The issuer owns resolution of the acceptance contradiction through the existing lane. This row neither amends the frozen face nor directs new worker work. Worker S27 at the cited branch pin already records the red baseline; this CVO observation adds the acceptance-predicate and omitted-suite consequences. No adjudicates edge is asserted to an unmerged branch-only row. Do not rerun this battery as a read-only probe: its mint and gate arms write the cloud object."
  },
  {
    "id": "IRPT_BCKEND-C-S81",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T13:42:53Z",
    "one_line": "RT5 correction remaps six worker IDs without changing their content; the disclosure-only grade is recorded at the corrected instance pin.",
    "class": "OBSERVATION",
    "spec_asserts": "L9 grades a judgment criterion at an explicit instance vintage; a citation to a renamed branch row must retain its original vintage or use the verified mapping.",
    "world_is": "Correction 95964 maps worker S25..S30 at 8d173559747f875ea751eeaea898de2b241ed8e7 to S27..S32 at 479ed367e57e41b9794aaea41d633884b0f5f5f3. Six row bodies are identical except id. The proof is identical after one-pass ID remapping and its battery pin update; battery changes are row labels only. Guard, both runners and issued face are unchanged. Proof checker is VALID rc=0 with six of six surprise references resolved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@8d173559747f875ea751eeaea898de2b241ed8e7",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.result.md@479ed367e57e41b9794aaea41d633884b0f5f5f3 (was/is mapping)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_RT5_L9_REVIEW_20260911.md (same commit; correction 95964 comparison and checker evidence)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade and citation-mapping record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "RT5-AC2",
        "instance": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@479ed367e57e41b9794aaea41d633884b0f5f5f3",
        "verdict": "PASS",
        "reason": "The RT5-AC2 disclosure bar and its output are unchanged after the six ID replacements. The record states two bundled files, absent bundled dependencies, undetermined execution host/dependency availability and no executed runner or scheduled-run proof. C-S79's disclosure-only judgment therefore also applies at this explicit corrected pin. All limitations and factual qualifications in IRPT_RT5_L9_REVIEW_20260911.md remain: this is not runtime readiness, whole-order acceptance or an RT5-AC1 truth verdict. C-S80's red-baseline predicate concern persists; its corresponding worker row is now S29 rather than S27."
      }
    ],
    "notes": "Preserve C-S79/C-S80 as evidence at their original 8d17355974 vintage. At the corrected tip use S27 for one key versus two, S28 for metadata-key collision, S29 for pre-red tests, S30 for invalid D- grammar, S31 for the forbidden runner-edit clause, and S32 for the old loose-key probes. Do not replace IDs in immutable earlier commits or apply the mapping to the issuer's distinct S25/S26 rows. The corrected tip was not merged into observed CLOUD 3b28cf1c6f1d1f5ff5e7917d4e97ea3ae5015bcd. No battery rerun, cloud action, worker modification or L10 slug follows from this record."
  },
  {
    "id": "IRPT_BCKEND-C-S82",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T23:36:05Z",
    "one_line": "The CVO's L8 watcher keeps TWO state files and keys them DIFFERENTLY -- the count watermark by ABSOLUTE path, the id/hash index by REPO-RELATIVE path -- and this box mounts C at both /c and /cygdrive/c, so arming under the other prefix re-baselined the count watermark on 32 of 33 channels while the id/hash index, which is the actual delivery limb, was unaffected and emitted all 19 genuinely-new rows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine v3 L8 (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md, the Stall clause): 'When every task order is terminal the COO reads the CVO's watermark once against the channel's row count; if the watermark is behind, the COO tells the CTO' -- a control that assumes the watermark moves only when rows were actually emitted.",
    "world_is": "The two state files do not fail together, and that is the whole finding. MEASURED: .tools/state/surprise-watch/3.0.0_SA_CVO.tsv stores ABSOLUTE paths (it held /c/Users/AndrewBerman/Desktop/ajb_workspace/... keys); .tools/state/surprise-watch/3.0.0_SA_CVO.idx.tsv stores REPO-RELATIVE paths plus row id and hash (first line: org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md<TAB>NFRA_CLDGRPH-S1<TAB>474fd27afca5; 1547 lines). This seat armed the stream with the /cygdrive/c/... absolute path the watcher skill mandates. RESULT, counted from the Monitor's own output file (52 lines): 32 NEW CHANNEL lines -- the count watermark matched no key and re-baselined -- and 19 NEW ROW lines, every genuinely-new row still delivered individually (IRPT_BCKEND 10 at S35, S36, S37, W1-S14, W1-S15, W1-S16, W2-S28, W2-S29, W3-S24, W3-S25; IRPT_FNTEND INVESTIGATION_v2 9 at W2-S9 through W2-S14, S21, S22, S23). NO ROW WAS MISSED. The id/hash limb is prefix-immune because its key is repo-relative, and it is the limb that delivers rows. WHAT IS ACTUALLY LEFT, stated as latent and not as damage: the number the spine's Stall clause names is the COUNT watermark, and that number jumps silently to the channel's current row count on a prefix change, so at a drain-end read a re-baselined watcher and a genuinely current one are indistinguishable. The control stops DISCRIMINATING; it does not report a falsehood here, because delivery did not fail. SOURCE, read rather than assumed: surprise-watch.sh:63 STATE_FILE=\"$STATE_DIR/${SERIAL}.tsv\" and :287-291 _prior_count(), which sed-matches the recorded line by the exact path string and returns empty on no match; the path is built from REPO_ROOT=$(cd \"$SCRIPT_DIR/../..\" && pwd), so it carries whichever prefix $0 carried. Both mounts are live: `test -d /c` succeeds, and pwd returns /c/Users/... or /cygdrive/c/Users/... according to the prefix used to cd. The watcher cannot steal a row -- it is read-only on the watched files by design, which is the documented reason it is not a copy of inbox-watch.sh.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/surprise_channel/surprise-watch.sh@f2f02e5829 :63 (STATE_FILE), :287-291 (_prior_count exact-string match, empty on no match), :56-57 (REPO_ROOT via pwd)",
        ".tools/state/surprise-watch/3.0.0_SA_CVO.tsv and .idx.tsv -- UNTRACKED device-local state, no commit vintage exists; the first keyed by absolute path, the second by repo-relative path + id + hash (1547 lines)",
        "surprise-watch.sh 3.0.0_SA_CVO status, run 2026-09-11T23:1xZ: DENOMINATOR 33 watched file(s), 1552 row(s) at last pass, every path rendered with the /c/ prefix",
        "Monitor task bh0e3jid5 output file, 52 lines: 32 NEW CHANNEL, 19 NEW ROW; arm banner reads 'parent-tied: pid 2529883' (armed, not orphan-capable)",
        "Live-mount control on this box: test -d /c -> EXISTS; cd /c/... -> pwd /c/Users/AndrewBerman/Desktop/ajb_workspace; cd /cygdrive/c/... -> pwd /cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@f2f02e5829, L8 Stall clause -- the consumer of the count watermark"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "THIS ROW'S OWN FIRST DRAFT WAS WRONG AND THE CORRECTION IS PART OF THE RECORD. It graded the finding ARMED and asserted 18 rows had reached no agent, written from the 32 NEW CHANNEL lines alone. .tools/surprise-row-gate.py refused it (ARMED with no disarm_owner), and in the interval the watcher's own later output produced the 19 NEW ROW lines that falsify the premise. The draft was wrong in the direction of alarm, from concluding before the second limb had run -- an early stop and a true failure read identically. SCOPE IS FABRIC-WIDE, FILED HERE BECAUSE THIS IS THE CHANNEL WHOSE INTAKE IT TOUCHED: 32 channels across both roots re-baselined, not only IRPT; the IRPT_FNTEND instance is the same event and is deliberately not a second row. PLACEMENT, stated because it was not free: a CVO row cannot go in investigations/ -- the gate's _coordinate_violations refuses a NEW C- row outside adjudications/ (self-test at :1706) -- and a plain -S id there would collide with 2.0.0_SA_COO~B's live allocator, which 1.0.0_SA_CTO reports continuing at S38. NOT ASSERTED: that any other serial's watermark is currently wrong. 1.0.0_SA_CTO.tsv and 3.0.0_SA_CVO~A.tsv sit in the same directory and were NOT read for their prefix form; a seat reading this row checks its own rather than inheriting this verdict. NO REMEDY PROPOSED AND NONE TAKEN -- the owner of surprise-watch.sh owns the fix, and CLAUDE.md's device-prefix NEVER already states the direction (derive the prefix, never hardcode) while withholding remediation authority. This row directs no worker, amends no frozen face and blocks no slug."
  },
  {
    "id": "IRPT_BCKEND-C-S83",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T01:15:00Z",
    "one_line": "L8 INTAKE LINKAGE, NOT A GRADE: round-2 row W4-S28 quantifies the exact date limb that round 1's C-S5 GRADUATED as still open, and it does NOT falsify round 1's S10-AC2 PASS -- that grade was scoped to glyph loss and to separating coordinate extraction from vendor arithmetic, and it named what it did not prove.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine v3 L9: JUDGMENT criteria are graded at L9 and never self-graded; CLAUDE.md: NEVER trust a producer's self-report or rc=0 -- verify against the served artifact.",
    "world_is": "W4-S28 reports that the round-1 extractor took a page's FIRST Data-as-of line for every row on that page (15 of 61 rows on the retained overview specimen sit on pages printing two different dates) and dated a further 12 of 108 multicomp rows CENSUS_STATED, while THE EXTRACTOR'S OWN certification string read CERTIFIED THROUGHOUT. READ CAREFULLY, because the two claims are about different objects and a successor could easily read this as a falsified grade: the CERTIFIED THROUGHOUT string is the PRODUCER'S SELF-REPORT, and round 1's L9 did not adopt it. The round-1 grade actually recorded is C-S78, S10-AC2 PASS, whose reason is 'the record measures per-document glyph losses over 89 pages and distinguishes coordinate extraction from vendor arithmetic. Rotation and nearest-number/footnote association remain unproven; W3-S10/W3-S11 carry the production consequences' -- it does not assert date correctness. And C-S5, which GRADUATED the specimen-absence premise, says in its own text 'glyph/date/holdout limitations remain open under W3-S10/W3-S11'. So the date limb was left OPEN by round 1 on purpose, and W4-S28 is the measurement that closes it with numbers rather than a contradiction of anything this seat graded. NET FOR ROUND 2: no correction is owed to 1.0.0_SA_CTO on the round-1 slug, and no round-1 grade is reopened. W4-S28 is carried as round-2 evidence against the date limb, and its ARMED standing belongs to IB-rtb-1 as its own disarm_owner field already states (the corrected extractor reaches a running function only at the irpt-ycharts-generate package's next build).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md (worktree, 148 rows at read time) -- row IRPT_BCKEND-W4-S28, surfaced_by 0.9.0_WK_IRPT_BCKEND~4 at 2026-09-12T00:22:27Z, disarm_owner IB-rtb-1",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md@27e67fa6a5 -- row IRPT_BCKEND-C-S78, the only S10-* grade recorded in round 1 (S10-AC2 PASS), read in full for its scope",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md@27e67fa6a5 -- row IRPT_BCKEND-C-S5, disposition GRADUATED, text 'glyph/date/holdout limitations remain open under W3-S10/W3-S11'",
        "Denominator for the S10 grade search: all 78 rows of ADJUDICATION_v1.md scanned for a criterion matching S10; exactly 1 grade found, so the PASS above is the whole of round 1's S10 judgment record and not a sample"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "WHY THIS ROW EXISTS AT ALL: at L9 a successor reading W4-S28 cold sees 'round 1 certified this and was wrong' and can either re-alarm on a closed round or, worse, discount W4-S28 as already-known. Neither is right. The discriminator is that round 1 graded the PRODUCER'S EVIDENCE with a named scope and refused the producer's broader certification string -- which is the rule working, one round early -- and this row pins the three artifacts that show it so the next reader does not re-derive them. NO GRADE IS ASSERTED HERE. Round 2 is not adjudicable: cells remain non-terminal on this project, and this seat cuts no slug and grades no judgment criterion until every task order is terminal and every row dispositioned."
  },
  {
    "id": "IRPT_BCKEND-C-S84",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T03:05:00Z",
    "one_line": "DISARMING IRPT_BCKEND-W4-S19, which named this seat. Round 1's S14-AC3 PASS STANDS -- it never read the hash-equality arm as demonstrating the render. But the grade UNDERSTATED the weakness, and the delta matters for FWD-4/FWD-8: the arm establishes not merely 'insufficient for a cloud export service' but NOTHING AT ALL about whether the input reached the renderer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W4-S19's own routing: 'the finding bears on the GRADE of IB-s-14's (v0.11) arm and on FWD-4/FWD-8, whose proof gap that arm was narrowing; the grader decides what the arm established.' IB-s-14's arm: 'the three retained vendor PDFs are verified by digest and exported as Analysis bundles labelled vendor_synthetic_holdings' -- read as three exports of three inputs.",
    "world_is": "THE GRADE IS NOT FALSIFIED. Round 1's ONLY S14-* grade is C-S78, S14-AC3 PASS -- all 78 round-1 adjudication rows scanned, exactly one match, so this is the whole S14 judgment record and not a sample. Its reason already says the exercise 'substitutes HTML string templates for the real frontend RenderPackage' and that 'fixture rendering and stored hash equality do not demonstrate a cloud export service or durable frozen bundle'. The grade refused the very inference W4-S19 falsifies, so the PASS rests on the record's disclosure and not on the arm. No round-1 grade is reopened. THE DELTA, AND IT IS THE PART WORTH CARRYING: W4-S19 measures the arm as weaker than the grade's own language. 'Does not demonstrate a cloud export service' concedes that something was rendered but not in production; the measurement is that three DISTINCT bundles (digests 38753e307c2e, 86c38f465c00, 9f89d01d4fa7) produced ONE normalized content hash b646b23012 and an identical 71,944-byte decompressed content stream, differing only in the creation date and the /ID the print engine stamps. A renderer whose output does not vary with its input is evidence about the RENDERER and about NOTHING ELSE -- it cannot witness that any particular input was rendered at all. So the proof gap FWD-4 and FWD-8 carry is WIDER than round 1 recorded, and it is wider in a direction the record does not hint at. WHY EVERY ARM PASSED: each variant was graded stored-hash-equals-receipt-hash, a claim about ONE object; no arm compared the three objects to EACH OTHER. The per-member checks were sound and the property that failed lives BETWEEN members, where no per-member check can reach -- the same shape as IRPT_BCKEND-S40 (a certification whose legs do not inspect the coordinate where the defect lives) reappearing at a different coordinate in the same round. ENDORSING THE FORWARD REMEDY W4-S19 NAMES: IB-rtb-1's replay should render TWO DIFFERENT bundles and REQUIRE THE CONTENT HASHES TO DIFFER. \u26d4 That is a DIFFERENCE control and not a positive control, and the distinction is the whole point: a positive control proves the instrument can fire and bounds UNDER-firing only; only a difference control shows that the output CHANGES when the input changes. Round 1 had the positive control and it passed every time.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md -- row IRPT_BCKEND-W4-S19, surfaced_by 0.9.0_WK_IRPT_BCKEND~4 at 2026-09-11T14:05:00Z, disarm_owner 3.0.0_SA_CVO",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v1.md@27e67fa6a5 -- row IRPT_BCKEND-C-S78, grade S14-AC3 PASS, read in full for its scope",
        "DENOMINATOR for the grade search: all 78 rows of ADJUDICATION_v1.md scanned for a criterion matching ^S14- ; exactly 1 found",
        "IRPT_BCKEND-S40 -- the sibling shape in the same round (round 1's three certification legs green over 27 wrong dates), cited as the pattern rather than as evidence for this row's facts"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "DISARM DISCHARGED: W4-S19's ARMED standing was waiting on this seat deciding what the arm established, and that decision is recorded here. NO GRADE IS ASSERTED OR REOPENED and no repair is taken -- the forward remedy is IB-rtb-1's and the decomposition is FROZEN mid-round. CARRIED TO L10, three items: (1) the widened FWD-4/FWD-8 proof gap, stated as wider than the round-1 record implies; (2) the difference-control requirement on IB-rtb-1's replay, which is the arm nobody has run; (3) the PAIRING of this row with S40 -- two independent instances in one round of per-member checks passing while the property that failed lived between or beside the members. \u2b50 THE PAIR IS WORTH MORE THAN EITHER ROW: one instance is a defect, two in one round from different workers on different artifacts is a statement about how this project's criteria are CUT, and that belongs in the round analysis rather than in a remediation line. NOT ASSERTED: that IB-s-14's other criteria are affected; only S14-AC3 was graded at L9 and only it was examined here."
  }
]
```
