"""Publish the CVO's review; no L10 carrier, order mutation, or peer-owned edit."""
import collections
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = 'org/missions/D4/POSN/POSN_ASTTAX'
INTAKE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json'
EVIDENCE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json'
CTO = '1.0.0_SA_CTO~Z'
COO = '2.0.0_SA_COO~Z'

# The disposition is about the demonstrated mechanism, not the sender or severity.
# A proposed DI remains pending under the measured terminality gate, never disguised as GRADUATED.
DECISIONS = {
 'S6': ('GRADUATED','INERT',CTO,
  'The old one-artifact safety boundary omitted the frontend and sibling consumers. The later four-clause bar widens the named boundary, resolving this specification instance; actual UI and producer defects remain separate findings. The current code read confirms allocation-summary READS holdings_attribution_data.json and writes allocation_summary.json: do not propagate the reversed producer attribution in earlier prose.',
  'Existing C-RETAG-SAFETY scope correction; preserve historical source vintages. No retag is admitted by the document change.'),
 'S7': ('GRADUATED','INERT',CTO,
  'The old claimed LIMB-6 fence did not cover M-only changes. The row reports two recuts and zero evaluator calls, not an observed unsigned issuance. The subsequent CLAUDE.md amendment ab642b92e5 relocates the mandatory signoff read; S36 supplies the owner closure record.',
  'The current law carrier was repaired inside the round. Keep the historical assertion and its correction distinct; do not credit the old hook with coverage it lacked.'),
 'S36': ('DISMISSED_WITH_REASON','INERT',None,
  'This is the closure report for S7, not a second implementation defect. Its doc/cron/retraction claims are attributed to the CTO record. A commit subject containing the fence is not proof that tick-25 ran the fence; no independent CVO runtime reenactment is claimed.',
  'S7 receives the grounded disposition; duplicate closure information needs no new remedy.'),
 'S8': ('GRADUATED','ARMED',COO,
  'The staged T6 binds an obsolete brief and assumes fresh generation where the downloaded deployed bytes raise on all 11 candidate targets. The current artifact could remain stale; absence of a fresh write is not measured blank UI. CTO 21814 explicitly forbids repinning, recutting or spawning T6 ahead of deployment/scope resolution.',
  'Existing T6 instrument and prerequisites need correction at an authorized recut. No pending order is changed. A fail-closed freshness criterion is possible; it cannot substitute for the missing deployment act.'),
 'W10-S1': ('GRADUATED','INERT',CTO,
  'At the issued source base 651ffd4f16, the raw allocation already carried 2.5 while the five-class label was Unknown and the class delta/spread were absent. This falsifies the no-else/source-zero mechanism at that pin. It does NOT make the deployed KeyError historical: T5 and CVO separately reproduce the exception on downloaded deployed bytes.',
  'The brief was corrected within the round at f9458a7e43; preserve separate source-code and deployed-code vintages. Code-before and registry-before are different controls.'),
 'W10-S2': ('GRADUATED','INERT',CTO,
  'The source benchmark ETF map covers cash, fixed_income and equity; those are not three independent ratified classes because cash/fixed income share one top-level class. Structured, Commodities and Alternatives lack an explicit benchmark choice. Available-only selection and cash fallback are source mechanisms, but a small current VXX weight does not prove universal safety.',
  'Settle the benchmark policy and unknown-class behavior at the existing generator comparison contract. CVO does not invent ETFs or declare zero benchmark weights wrong without that contract.'),
 'W10-S3': ('GRADUATED','INERT',COO,
  'The new generator normalizes case, spaces, hyphens and several aliases, while the staged registry writer has no settled raw spelling. The ratified labels are fixed; raw encoding is a distinct contract. Seven CVO source controls preserve the six recognized spellings/classes and expose an unknown-class warning control.',
  'The existing retag issuance must bind raw values to the generator contract, without minting a sixth ratified class or duplicating independent alias vocabularies.'),
 'W11-S1': ('GRADUATED','INERT',COO,
  'The superproject gitlink cannot be read as portal source and a sparse cone cannot supply absent files. T2 recovered through the portal object store at e85f6eb84f. CVO independently read the same consumer and both category callers there.',
  'Correct the existing measurement order instrumentation and exact repository/pin. Current read gap recovered; no portal write authorization follows.'),
 'W11-S2': ('DISMISSED_WITH_REASON','INERT',None,
  'The 14-commit portal vintage difference is disclosed and the subject files reportedly have no diff between the compared pins. A moving branch is not a defect once evidence is explicitly bound to e85f6eb84f.',
  'No remaining repair is demonstrated by this vintage observation. It is not evidence about the deployed bundle.'),
 'W11-S3': ('DISMISSED_WITH_REASON','INERT',None,
  'T2 reports 1201 tree entries: 1200 blobs and one nested archive/dashboard gitlink; 1113 text reads and 87 binary exclusions. The unread nested repository and binaries limit a whole-estate claim, but this row does not establish an omitted active frontend consumer.',
  'Accept the bounded source read and its exclusions. No all-runtime or transitive-repository closure is inferred.'),
 'W12-S1': ('DISMISSED_WITH_REASON','INERT',None,
  'The 93 occurrences on 67 lines and 49 occurrences on 32 lines are different units at the same source vintage, not evidence that the issuer read stale files.',
  'Retain occurrence-versus-line denominators. No code or scope change follows.'),
 'W12-S2': ('GRADUATED','ARMED',COO,
  'The sibling source passes an unfamiliar class through despite the stale folds-to-Equity comment. Its fixed benchmark map defaults the missing class policy weight to zero, so a 10.0 style weight produces a 10.0 bet. This is a measured fallback and a missing explicit policy, not proof that every zero benchmark is financially wrong.',
  'Recut the existing sibling measurement to bind and discriminate the benchmark policy; actual implementation repair outside this read-only cell is part of the pending missing-cell finding C-S64.'),
 'W12-S3': ('GRADUATED','ARMED',COO,
  'The two-class assumption survives in four different mechanisms: the len==2 tilt guard, two-name ordering, two-row fallback and a normalization gap assigned to the largest row. The worker reports 88 exercised hop-lines (80 five-class plus 8 control/error cases), not 88 independent production surfaces.',
  'Give each mechanism its own acceptance obligation within the sibling assessment; avoid replacing them with a blanket two-class claim. Missing repair acts are assessed separately in C-S64.'),
 'W13-S1': ('GRADUATED','ARMED',COO,
  'The instruction to measure uncommitted seed-etf-constituents edits named shared SITEZ state that was absent from the worker linked checkout. The preserved patch is a separate artifact, not those checkout bytes. Its cash canonicalization and empty-index-key repairs must not be inferred present from a clean git status.',
  'Bind the existing durability cell to the exact preserved patch/carrier and assess it before any later seeder act; preserve the other owner worktree.'),
 'W13-S2': ('GRADUATED','INERT',COO,
  'The historical producer encounters 16 empty sub_asset_class values in 136 tickers, with ACSG in the first batch; the worker measured the table index constraint and a paired conditional-request control. The new merge drops empty fields and preserves curated fields together. CVO normal/conflict/scan-denied controls confirm the new source paths, but do not repeat the live-table probe.',
  'The named seeder crash is repaired in the worker commit. Closing that crash alone on old overwrite code would arm a revert. The sibling patch and concurrent-curation risk remain separate.'),
 'W13-S3': ('DISMISSED_WITH_REASON','INERT',None,
  'The worker removed one unused import and three extraneous f-string prefixes within the granted script. These pre-existing lint defects were corrected in the delivered change.',
  'No remaining separate remediation is demonstrated; no claim is made that earlier historical commits passed the current linter.'),
 'W14-S1': ('UNDER_INVESTIGATION','ARMED',COO,
  'The downloaded Lambda source has 94164 bytes and md5 cc79aff7506f8c39e17453f386c69551. CVO independently reproduced 11/11 candidate AFTER exceptions against 11/11 successful repaired-source AFTER arms. This establishes an unsafe generation precondition; it does not demonstrate live page blanking or a performed retag. All seven decomposition cells were read; none deploys the repaired source.',
  'PROPOSED DECOMP_INVALIDATING: a deployment/effective-artifact verification act is absent. Formal disposition waits the measured L10 terminality gate: S2/S3/T6/T7 are staged. Round-2 exception is not reused. CTO 21814 holds T6; no deployment is performed.'),
 'W14-S2': ('GRADUATED','ARMED',COO,
  'The worker full-table subtraction is 285 minus 274 = 11 CANDIDATES, not eleven approved semantic decisions. The inherited seven-member hedge set omits UVXY, QBER and PDBC plus the separately named VXX. QBER/PDBC remain membership calls under C-MEMBERSHIP-AT-L5. The attribution artifact contains 31 rows for four candidates, so Models-only held status is not the whole blast radius.',
  'Settle and bind the candidate set in the existing retag cell before issuance. No candidate target in the CVO control is a new classification authorization.'),
 'W14-S3': ('GRADUATED','ARMED',COO,
  'CVO parsed all 57 CANONICAL_SECURITIES and verified the --upload --yang update_item path: four candidates intersect (QBER, UVXY, VXX, PDBC). Its SET asset_class replaces that field even though unrelated attributes are preserved. The named T4 seeder guard cannot govern this second writer. Automatic scheduling was not measured; the evidenced trigger is deliberate invocation.',
  'The existing registry-durability cell must include the second writer in its coverage/permission assessment. Do not run it or silently retag these four. Implementation across another owning surface needs the CTO scope decision.'),
 'W14-S4': ('GRADUATED','ARMED',CTO,
  'The additional ETF publisher is a positive counterexample to the closed two-sibling set. It copies gold holding class values and emits a four-key book allocation at source lines 469-472. The live artifact had 189 rows over four books and zero candidate members; its current bytes do not exercise post-retag loss for those absent members.',
  'The CTO must settle this existing owning surface coverage at the project boundary. No POSN worker is authorized to rewrite another project publisher; candidate reach is distinguished from a currently held row and from classifier use for non-class fields.'),
 'W14-S5': ('GRADUATED','INERT',CTO,
  'Code-before means new class on old source; registry-before means old class on a chosen source. Under the latter comparison CVO reproduced 0-to-weight movement in the raw target allocation on repaired source. This does not make a raw allocation interchangeable with the requested label-grouped weight or prove the rendering loop includes the group.',
  'Name both comparisons and their units in the existing bar. The earlier equal 2.5/2.5 example remains valid only for its code-change control.'),
 'W14-S6': ('GRADUATED','ARMED',COO,
  'The worker comp-find invocation disclosed 29824 unreadable files alongside 3655 scanned files. Its later object-store census read 33514 blobs plus two named gitlinks in 33516 entries. These are distinct domains/instruments. Printed token counts alone do not establish dataflow reach; the later exclusion of 118 code files on absent registry tokens is also not a proof of unreachable consumers.',
  'Repair the existing census criterion for sparse checkout and indirect reach. The tool disclosed its limit; the mistake is treating that limit as an exhaustive surface universe.'),
 'W14-S7': ('GRADUATED','INERT',CTO,
  'At the reported Models artifact only VXX of 11 candidates is held; ten have zero rows. NONZERO and equal to zero cannot both hold there. Attribution instead has four held candidates. A synthetic 0.025 control answers survival if held, not current live weight preservation.',
  'Make the existing bar surface- and held-status-specific. CVO does not adopt the suggested requirement to fabricate zero-weight rows for every absent ticker; that is an additional product decision.'),
 'W14-S8': ('DISMISSED_WITH_REASON','INERT',None,
  'The headline top-level-class override is falsified at e85f6eb84f. Full src search finds two getETFCategory callers; both consume category.segment as a sub-asset-class fallback, not category.assetClass. HoldingsTab groups by holding.asset_class from the artifact. Four stale map values and type unions therefore do not establish four live top-level overrides.',
  'Dismiss that causal claim. The independent two-class rendering loop and missing class/color coverage are real and remain in T2/T5 evidence and C-S64; widening the loop is not claimed to fix all UI behavior. No deployed DOM was exercised.'),
}


def main():
    intake = json.loads((ROOT / INTAKE).read_text(encoding='utf-8'))
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    rows = []
    originals = {x['row']['id'].split('-Z-')[1]:x for x in intake['new_originals']}
    assert set(originals) == set(DECISIONS)
    def make(n, text, disposition, standing='INERT', owner=None, spec='', evidence=None, notes=''):
        row = {'id':'POSN_ASTTAX-Z-C-S'+str(n), 'project':'POSN_ASTTAX','fabric':'site-z',
               'surfaced_by':'3.0.0_SA_CVO~Z','surfaced_at':now,'one_line':text,'class':'OBSERVATION',
               'hazard_standing':standing,'disposition':disposition,
               'grounding':{'status':'GROUNDED','evidence':evidence or [EVIDENCE,INTAKE]},
               'spec_asserts':spec,'world_is':text,'notes':notes}
        if owner:
            row['disarm_owner'] = owner
        if disposition == 'DISMISSED_WITH_REASON':
            row['dismissal_reason'] = notes or text
        return row
    for number, key in enumerate(sorted(originals),36):
        original = originals[key]
        disposition, standing, owner, assessment, remedy = DECISIONS[key]
        row = make(number,assessment,disposition,standing,owner,original['row']['spec_asserts'],
                   [INTAKE+'#'+original['row']['id'],EVIDENCE],remedy)
        row['adjudicates'] = [original['row']['id']]
        rows.append(row)
    row = make(60,'Correction to C-S18/C-S31: W4-S2 proved an incomplete read of an already specified frontend contract, not a missing decomposition cell. The S7 order explicitly names that hop in THE ACT lines 31-34. The correct category is a grounded measurement/instrument failure in the existing cell.',
               'GRADUATED','INERT',COO,
               'DECOMP_INVALIDATING requires a remedy needing a cell the decomposition does not contain.',
               [PROJECT+'/task-orders/POSN_ASTTAX.TO-S7-1.verify-the-five-class-chain.md:31', PROJECT+'/surprise-channel/adjudications/ADJUDICATION_v3.md#POSN_ASTTAX-Z-C-S31'],
               'Supersedes only the W4-S2 DI category by a new citing row, preserving the old record. Round-3 T2 has now recovered the source read; it has not fixed or exercised the deployed frontend. A new read-only cell was a COO workflow choice, not proof that the original decomposition lacked this obligation.')
    row['adjudicates'] = ['POSN_ASTTAX-Z-W4-S2']
    rows.append(row)
    grades = [
      ('T1-AC6','PASS','Within the issued SOURCE CHANGE ONLY boundary, the real generator output carries all five classes, including cash/fixed-income spellings, with populated labels, weights and class delta/spread. CVO independently exercised six recognized raw classes and an unknown control, plus 11 candidate before/after inputs. This passes the generator output contract only; it does not pass deployment, benchmarks not specified by the order, sibling consumers or DOM safety.'),
      ('T2-AC5','PASS','The specific unread frontend-contract gap is now closed at SOURCE-AT-PIN: 42/42 reported frontend consumer files read, 1113 text blobs plus 87 binary exclusions and one named nested gitlink. CVO checked the actual grouping loop and category call sites. The result is a demonstrated source collapse, not a successful UI. No all-runtime closure, portal change, deployment or DOM exercise is passed.'),
      ('T3-AC4','FAIL','The two measured siblings are not the whole producer set. The data/etfs positioning publisher is a positive additional consumer/producer identified by W14-S4; its distinct served artifact and four-key payload were read. A 290-file/20-token-carrier sweep that classifies only two does not close the remainder. The local two-function measurements remain useful.'),
      ('T4-AC5','FAIL','The default named seeder improves: CVO normal arm writes 136 rows, conflict arm refuses with rc3/0 writes and Scan-denied arm fails closed rc2/0 writes. But a CVO controlled curation between the scan and batch put is lost (curator_note B becomes old A, rc0); the snapshot merge is not concurrent durability. The 57-entry second writer overlaps four candidates, and explicit override flags also bypass preservation. No live concurrent edit is claimed.'),
      ('T5-AC8','NOT_EVALUATED','The universal surface-set claim is not established: absent registry tokens exclude 118 code files without proving transitive dataflow absence, runtime/deployed consumers remain unread, and 132/836 reported cells are NOT-MEASURABLE-HERE. A4 has zero candidate members; R5/R6 claim a class override their call sites do not perform. The concrete generator counterexample nevertheless supports safety NO-GO. Completion of this measurement does not pass its universal property or all its table entries.'),
    ]
    row = make(61,'Five round-3 judgment grades: two scoped PASS, two FAIL, one NOT_EVALUATED. Retag remains NO-GO.',
               'DISMISSED_WITH_REASON',spec='L9 grades each judgment against the specification that issued it, separately from structural proof validity.',
               notes='Grade carrier; the mechanical checker is not the truth grader. Six older proof instances retain their prior CVO grades; five new instances are freshly structure-checked against criterion IDs read from the issued orders. No historical source result is promoted to a current deployed claim.')
    row['grades'] = []
    for criterion, verdict, reason in grades:
        p = next(p for p in intake['proofs'] if any(a['criterion_id']==criterion for a in p['proof']['acceptance']))
        row['grades'].append({'criterion':criterion,'instance':p['path']+'@'+p['commit']['stdout'].strip(),
                              'verdict':verdict,'reason':reason})
    rows.append(row)
    rows.append(make(62,'The T5 836-cell table repeats some source inferences as per-member exercised failures. A4-b/d are marked MEASURED-EXERCISED for 11 candidates despite zero candidate rows in that live artifact. R5/R6 assign top-level override failures even though the only callers read segment. Its 473 FAIL count is not an independently verified count of post-retag regressions.',
                     'GRADUATED','ARMED',COO,'A cell labeled exercised must carry a control that actually exercises the stated member, surface and clause.',
                     [EVIDENCE,PROJECT+'/deliverables/0.9.0_WK_POSN_ASTTAX~14/t5_bar_table.py'],
                     'Repair the existing bar instrument and evidence-grain labels. Preserve the valid NO-GO counterexample. The table mixes source files, stores and rendered surfaces; summing its rows is not a count of independent product surfaces. No DOM result is claimed.'))
    rows.append(make(63,'The repaired seed_table scans a snapshot and later performs full-item batch puts without comparing the current item. In a paired actual-function control, normal preserves curator_note A; concurrent curation to B after scan is overwritten back to A, rc0 and 136 writes. Conflict and Scan-denied controls correctly refuse before writing.',
                     'GRADUATED','ARMED',COO,'AT3-s-4 asks whether the registry survives a re-seed rather than only the simulation supplied.',
                     [EVIDENCE+'#reseed_controls','infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py@8adab5748d2b58091bb0a19ebf16e15e27846e47'],
                     'Existing registry-durability cell: measure and bind the concurrent-update contract, then prevent lost curation or explicitly enforce an exclusive writer window. This is a controlled possibility, not a report of live concurrent activity. No additional permissions or production write was used.'))
    rows.append(make(64,'The seven-cell round-3 cut repairs generator source and one seeder, measures frontend/sibling/bar paths, then retags/reconciles. It contains no frontend repair or sibling implementation repair act, while actual HoldingsTab source groups only Fixed Income/Equity and omits a new class from orderedGroups but includes it in grandTotal. The frontend measurement cell is present; the distinct repair act is absent.',
                     'UNDER_INVESTIGATION','ARMED',COO,'The declared decomposition domain is everything needed to make step (2) true, before the retag; measurement and repair are distinct acts.',
                     [EVIDENCE+'#portal_snippets',PROJECT+'/decompositions/POSN_ASTTAX_DECOMP_round3.md'],
                     'PROPOSED DECOMP_INVALIDATING, pending the L10 terminality gate, separate from the corrected historical W4-S2 misclassification. Scope/freeze decisions belong to CTO/Andrew; the COO recut follows the authorized L10 route. Do not edit portal or expand another owner project. Deployment is separately pending on the original W14-S1.'))
    counts = collections.Counter(r['disposition'] for r in rows[:24])
    header = f'''# POSN_ASTTAX - ADJUDICATION v4, round 3, site Z

L8 review of all 24 new original investigation items is recorded below; 49 original items exist across both roots. Of the 24 newly reviewed items: {dict(counts)}. W14-S1 remains formally pending; the CVO's own missing-repair-cell proposal C-S64 is also pending. L9 is therefore not fully disposition-complete and no L10 slug is issued.

Whole-project terminality: 15 orders, 11 terminal, four staged (S2-1, S3-1, T6-1, T7-1). Five new proof instances are freshly structurally VALID against their issued criterion IDs; six earlier proof instances retain their prior reviewed grades. No order status is changed. CTO 21814's T6 hold remains; the named round-2 exception is not generalized. The gate source at check_file explicitly subjects new DECOMP_INVALIDATING rows to L10 preconditions.

Evidence: `{INTAKE}` (intake row/proof snapshot) and `{EVIDENCE}` (new offline controls and source reads). Source pin 3ce0c0e372; portal object pin e85f6eb84f; seed source pin 8adab5748d2b58091bb0a19ebf16e15e27846e47. Evidence records worker proof commit IDs rather than accepting their PENDING-THIS-COMMIT placeholder as a hash. No downloaded pickle is executed. No live AWS call, retag, deployment, portal build or DOM exercise is performed by these CVO controls.

Basis: graduation requires an attributed mechanism, denominator and remedy holder; dismissal requires a stated counterexample, bounded non-defect or resolved instance. Severity and sender identity do not determine disposition. A missing read/grant in an existing cell does not itself invalidate the decomposition. A genuinely absent repair/deployment act is a separate proposed DI and remains pending while the repository gate bars it. C-S60 explicitly corrects the old W4-S2 category without rewriting its history.

C-S61 holds the five judgment grades. A scoped code-output PASS is not a served-system safety PASS. The bar remains NO-GO on the reproduced deployed-code exception, regardless of the rejected overclaims in W14-S8 and the matrix. Eleven tested candidate targets are not eleven approved membership decisions. No FWD is claimed REALIZED.

```json
'''
    out = ROOT / PROJECT / 'surprise-channel/adjudications/ADJUDICATION_v4.md'
    out.write_text(header+json.dumps(rows,indent=2,ensure_ascii=True)+'\n```\n',encoding='utf-8')
    print(json.dumps({'rows':len(rows),'new_original_dispositions':dict(counts),'pending_originals':['POSN_ASTTAX-Z-W14-S1'],'pending_own':['POSN_ASTTAX-Z-C-S64']}))


if __name__ == '__main__':
    main()
