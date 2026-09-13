"""Write the CVO's explicit round-5 decisions; never modify an original item or TO."""
import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = ROOT / 'org/missions/D5/AMGT/AMGT_RESAPP'
CHANNEL = PROJECT / 'surprise-channel'
DOC = CHANNEL / 'adjudications/ADJUDICATION_v5.md'
SERIAL = '3.0.0_SA_CVO~Z'
CTO = '1.0.0_SA_CTO~Z'
COO = '2.0.0_SA_COO~ZZZ'
CRO = '4.0.0_SA_CRO~Z'

# Original suffix, disposition, owner, standing, finding and the bounded decision.
DECISIONS = [
 ('S6', 'GRADUATED', CTO, 'ARMED', 'Legacy version fallback can admit changed brief bytes',
  'The actual evaluate() function still falls back to prd_version when half_hash is absent. The offline same-version/changed-bytes control returns SIGNED. Both current lane records are SIGNED; deleting them at current v0.5 returns STALE, so the defect is the general same-version fallback, not a current missing-lane false green. Holder: CTO, the existing sign-off gate owner; require byte-bound records and a red changed-bytes control.'),
 ('S7', 'DISMISSED_WITH_REASON', CRO, 'INERT', 'S7 is the instance disarm of S6, not removal of the fallback',
  'Accept the hash-bound CRO lane record as a dated instance correction. Current independent evaluate() reads both halves SIGNED. This does not remove S6\'s legacy code path; that remedy is retained in C-S24. No separate repair follows from this corroborating row.'),
 ('S8', 'DISMISSED_WITH_REASON', CRO, 'INERT', 'The pre-rename bucket probe is a dated supporting record',
  'Accept the recorded identity/configuration reads as support for the S5 obligation at their vintage. Do not infer all historical reads, object-body permission, table migration or present bucket identity from them. S20 is the post-rename bucket record; no separate remedy arises from S8.'),
 ('S9', 'GRADUATED', COO, 'ARMED', 'Two independently valid Terraform cuts shared singleton configuration',
  'rd1 and rd2 shared one root module but declared singleton backend/provider blocks independently; their individual VALID instances did not validate their union. Current committed amgt-resapp has two root .tf files and no table declarations; harvest has both renamed tables. Packet claims of unconsolidated state and a source header claiming consolidation are not a CVO state measurement. Holder: COO for the existing shared-module cut; CRO owns estate state. Require a union validation and state ownership evidence, preserving the new scheduler residual in C-S49.'),
 ('W1-S7', 'GRADUATED', COO, 'ARMED', 'Safe-apply required identity state outside the issued write grant',
  'The worker met HALT-GT by writing its own gitignored session identity outside the listed paths. That measured prerequisite is a grant defect, not evidence that all session writes are implicitly authorized. Holder: COO; carry the identity prerequisite and its permitted writer in the existing apply cell before issuance.'),
 ('S10', 'GRADUATED', COO, 'ARMED', 'A correct union repair was outside the draining seat grant',
  'The row\'s code-reconciled headline is qualified by its record: the COO edit was refused and reverted, then rd3 was routed and later superseded. The current moved declarations do not vindicate the reverted edit. Holder: COO for a complete reconciliation grant on the existing module; CRO for state. Consolidate its remedy with S9, without counting that temporary validation as closure.'),
 ('S11', 'GRADUATED', COO, 'INERT', 'The two-builder collision was resolved by superseding rd3 and rd4',
  'The identified collision was between CRO harvest ownership and the round-5 rd3/rd4 work. Both orders are now superseded; the stopped rd3 attempt had no commit or apply. The owner acted inside this round. Holder: COO; carry REMEDIATED/DISARMED at L10, with no new worker order and no invented proof instance for unexecuted orders.'),
 ('W2-S6', 'GRADUATED', COO, 'ARMED', 'Per-ticker computation lacked a canonical universe input contract',
  'The scheduled producer selected the ~4 worker universe and packaged a frozen copy. Independent controls find 89 rows in each of ~3/~4, with 32/34 measured distinct identities and no AAPL US placeholder; those checks do not establish a canonical publisher or the deployed ZIP vintage. Holder: COO for existing identity and rd5 cells. Name the source, update contract and package provenance; an existing cell needing a better grant is not automatically an absent cell or DECOMP_INVALIDATING.'),
 ('W2-S7', 'GRADUATED', COO, 'ARMED', 'Packaging exposed the same singleton-provider grant gap',
  'Adding archive to a second required_providers block was refused by Terraform; the worker used a static build_zip.py artifact instead. That alternative can work and no rule here mandates archive_file. Holder: COO for the existing rd5 packaging cell: give it a deterministic rebuild/hash contract and any required shared-file grant. The manual artifact must not be mistaken for a continuously rebuilt current deployment.'),
 ('S12', 'GRADUATED', CRO, 'ARMED', 'Rename closure must cover live consumers and executable check artifacts',
  'Use S13\'s corrected census: ten hard-coded bucket literals, five in live consumers and five in worker checks, plus one derived and one environment-based reference. Live source defaults were changed; pinned historical proofs stay historical. An env knob does not repair a check that never reads it. Holder: CRO for a current executable consumer/check map; preserve historical evidence without rewriting its bytes. C-S49 separately identifies live scheduler dependencies missed by a defaults-only review.'),
 ('W7-S6', 'GRADUATED', COO, 'ARMED', 'Tail filtering removed the search denominator required by AC3',
  'The issued tail -12 could discard the comp-find denominator; the worker\'s supplemental untruncated output supplied it (12 hits across 67 scanned files). Holder: COO for the existing rd7 instrument: retain the full bounded result or a machine-readable denominator. Do not turn a truncated display into a zero-results claim.'),
 ('W7-S7', 'GRADUATED', COO, 'ARMED', 'The socket negative control did not guard the entire test suite',
  'The worker disclosed an initial mutant opening example.com:80, reverted it, and did not claim the event never happened. Current five-test source applies the socket blocker to only three tests; the first two lack it. Production watchlist code has no outbound call, but the harness still leaves a mutation path unguarded. Holder: COO for existing rd7 test coverage; apply the blocker across all tests. CVO independently denied socket connections across all 37 offline tests, which passed.'),
 ('S13', 'DISMISSED_WITH_REASON', CRO, 'INERT', 'Accept the corrected S12 denominator',
  'S13 corrects the earlier 11/6 count to ten literals/five live consumers, with derived and environment references separate. Adopt that correction in C-S33; this supporting census does not need a second remedy.'),
 ('S14', 'GRADUATED', CTO, 'ARMED', 'Artifact identity cannot be inferred from a recent filesystem timestamp',
  'The known generated VINTAGEID fixture was repeatedly mistaken for a live peer artifact. Its existing exclusion is not a general output discriminator. Holder: CTO for compiler/artifact classification: distinguish generated fixtures from accountable deliverables using provenance and intended role. This is one measured fixture, not a claim that all generated output is disposable.'),
 ('S15', 'DISMISSED_WITH_REASON', COO, 'INERT', 'The identity and competing-builder disarms are corroborated within their scope',
  'Independent source controls corroborate ~3/~4 measured identities as 32/34 distinct values with zero AAPL US; rd3/rd4 are superseded. Accept those instance disarms. Neither result measures the deployed ZIP, and a nonempty MEASURED filter alone cannot reject a wrong-but-marked-MEASURED identity. Remaining input/package obligation is W2-S6; no duplicate remedy is opened here.'),
 ('S16', 'GRADUATED', CTO, 'ARMED', 'The portal artifact carries a promotion-base coupling',
  'The worker inherited 5b959f63 on top of DEV 30ca and the intervening IRPT commits. This demonstrates ancestry coupling, not that the AMGT code semantically depends on every intervening commit. Holder: CTO for preserved branch/base selection and later authorized integration. PROD and DEV remain frozen; CVO did not rebase, promote or move the recorded gitlink.'),
 ('S17', 'DISMISSED_WITH_REASON', CTO, 'INERT', 'The tracked check-face files are an instance repair already carried',
  'The blanket root lib ignore was removed at b750649397 and seven check-face files were tracked. A plain check-ignore on tracked files is not by itself the proof; the changed ignore source and tracked artifacts are. Accept the instance repair already covered by earlier adjudication, without treating all future generated-file identity questions as solved.'),
 ('S18', 'DISMISSED_WITH_REASON', CTO, 'INERT', 'Correct the current missing-lane false-green assertion',
  'The time-local stale half was real, but current hash-bound records read SIGNED. Removing current lane files independently yields STALE because old base versions differ from PRD v0.5. Therefore the unqualified claim that missing lane records currently yield SIGNED is false. The synthetic same-version fallback defect remains GRADUATED in C-S24; no second repair or overdue-resign claim follows from S18 now.'),
 ('S19', 'GRADUATED', CTO, 'ARMED', 'A worker-local portal object needed preservation before teardown',
  'There were no object alternates and no committed superproject gitlink to the worker head. The initial dangling-gitlink forecast had the wrong trigger; loss of the sole object store was the actual preservation risk. S21 records the successful fetch. Holder: CTO; preserve reachable objects before deleting their only checkout and resolve the separate integration hold. Do not claim a gitlink was advanced.'),
 ('S20', 'DISMISSED_WITH_REASON', CRO, 'INERT', 'Accept the new bucket read and old-name negative control as bucket evidence',
  'The post-rename bucket identity/configuration record and old-name 404 control support the scoped S5 read obligation after renaming. Listing and configuration reads do not prove object-body access, table migration equality or scheduler permissions. Those wider claims cannot close from this record; no separate bucket remedy is opened.'),
 ('W2-S8', 'GRADUATED', COO, 'ARMED', 'The issued bare npx command selected the wrong compiler package',
  'The measured executable was registry tsc 2.0.4 rather than TypeScript; the worker\'s same-node_modules comparisons eliminated several explanations without establishing a cache-poisoning cause. Graduate only the executable-identity defect. Holder: COO for existing rd8 instrument: bind the installed TypeScript executable/version and project selection; no speculative root cause is accepted.'),
 ('W2-S9', 'GRADUATED', COO, 'ARMED', 'The AC2 root no-emit check examined no source files',
  'Pinned tsconfig.json has files: [] and references; plain --noEmit does not perform the referenced project build. The worker\'s injected TS2322 error was missed by that check and caught by the build control. AC2 is FAIL as issued: AC1 alone is not an independent staleness control. Holder: COO for the existing rd8 check; use a clean/forced referenced-project check with a deliberately failing source control. Preserve the failed issued criterion.'),
 ('W2-S10', 'GRADUATED', CTO, 'ARMED', 'A migration message cited a different tree from the worker pin',
  'Old table reads failed and the worker recorded the renamed table with 42 rows; code citations were current in main but absent at the worker pin. S21 corrects the overly general no-such-code statement. Holder: CTO with CRO migration owner: carry path plus commit plus current resource identifier at the handoff. A current path without its tree does not update a pinned worker.'),
 ('S21', 'GRADUATED', CTO, 'ARMED', 'Object preservation succeeded while portal integration remains held',
  'e6057f26c57fc6ff6c223f1c73cc29be3c7f51d6 resolves in the main portal object store and is anchored by wk-amgt_resapp-5-8-portal; the recorded gitlink remains e85f6eb84f. The successful fetch disarms the immediate only-copy risk in S19. Holder: CTO for the remaining base/integration decision under the PROD+DEV freeze. Neither object presence nor 20 changed files proves an integrated or served route.'),
]

GRADE_REASONS = {
 1: ('PASS', 'AC4 asks for a genuinely separate article store with per-security/platform time lookup, not a news-table filter. The pinned table/shape record supplies the distinct key and both GSIs. This grades the issued storage design; an empty new store and a cached news ItemCount do not prove article coverage.'),
 2: ('PASS', 'AC4 asks for precomputed axis/rank rows retrievable without scan-and-rank. The pinned schema has axis_date/ticker keys and axis-rank-index with rank_sort, enabling ordered Query and point retrieval. It does not prove an HTTP adapter exists or prohibit every caller from scanning.'),
 5: ('PASS', 'AC4 asks for a scheduled producer, not a monitor, with the issued 30-day/0-100/top-10 semantics. The pinned worker instance, schedule source and producer controls meet that bar; zero article counts legitimately yield zero scores. This historical grade predates the migration residual in C-S49 and does not certify the currently deployed package, IAM or next scheduled run.'),
 6: ('PASS', 'AC4 asks for a boxside Bloomberg price engine, not a Lambda, with the specified window/ranking semantics. The pinned host record, blp_client use and price functions meet that bar; 32 measured results out of 34 attempted are recorded rather than relabelled 34 successes. No new Bloomberg call was made by CVO.'),
 7: ('PASS', 'AC4 asks for per-firm starred storage as a pure marker, without research/queue side effects. The pinned store keys by WATCHLIST#firm and writes/deletes one marker; offline tests corroborate shared-firm behavior and side-effect absence. This storage-level judgment does not certify a missing HTTP authentication boundary, pagination completeness or the uncovered test-harness mutation path in W7-S7.'),
 8: ('FAIL', 'AC4 and the inlined rd8 cell require the approved page shape and a read headless route render. At e6057f26 the persistent panel, three tabs and header Print location are present, but Trending/Breakout are mapped one-to-one to Chatter/Price instead of crossed controls; required /api/scoped/amgt adapters are not delivered; renderCheck.tsx renders fixture components and a PrintTriggerButtonReplica rather than the actual route/action. It cannot establish live ranking reads or renderer wiring. The StarredList iterates stored starred order, contrary to the report\'s producer-order filter claim; RankedChart is ticker-indexed and has no time-series implementation despite the stated automatic second-day behavior. Compile success cannot satisfy these clauses.'),
}


def rows(path):
    result = []
    for block in re.findall(r'```json\s*(.*?)```', path.read_text(encoding='utf-8'), re.S):
        value = json.loads(block)
        result.extend(value if isinstance(value, list) else [value])
    return result


def main():
    if DOC.exists():
        raise RuntimeError('Refuse to overwrite an existing adjudication')
    evidence_path = HOME / 'AMGT_RESAPP_ROUND5_CVO_EVIDENCE_20260911_Z.json'
    evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
    source_path = HOME / 'AMGT_RESAPP_ROUND5_CVO_SOURCE_CONTROLS_20260911_Z.json'
    source = json.loads(source_path.read_text(encoding='utf-8'))
    originals = {r['id']: r for r in rows(CHANNEL / 'investigations/INVESTIGATION_v1.md')}
    assert set(evidence['intake']['new_ids']) == {'AMGT_RESAPP-Z-' + d[0] for d in DECISIONS}
    assert len(DECISIONS) == 24
    utc = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    references = [str(evidence_path.relative_to(ROOT)).replace('\\', '/'),
                  str((HOME / 'AMGT_RESAPP_ROUND5_CVO_CONTROLS_20260911_Z.json').relative_to(ROOT)).replace('\\', '/'),
                  str(source_path.relative_to(ROOT)).replace('\\', '/')]
    result = []
    for number, (suffix, disposition, owner, standing, title, reason) in enumerate(DECISIONS, 24):
        target = 'AMGT_RESAPP-Z-' + suffix
        original = originals[target]
        row = {'id': f'AMGT_RESAPP-Z-C-S{number}', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
               'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': title, 'class': 'OBSERVATION',
               'hazard_standing': standing,
               'grounding': {'status': 'GROUNDED', 'evidence': [
                   'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#' + target,
                   *original.get('grounding', {}).get('evidence', []), *references]},
               'disposition': disposition, 'adjudicates': [target],
               'spec_asserts': original.get('spec_asserts', 'L9 requires an evidence-based disposition of this investigation item.'),
               'world_is': reason, 'notes': reason + ' L10 has not been issued; a named remedy holder is not a worker assignment.'}
        if standing == 'ARMED':
            row['disarm_owner'] = owner
        if disposition == 'DISMISSED_WITH_REASON':
            row['dismissal_reason'] = reason
        result.append(row)
    grades = []
    for rd, (verdict, reason) in GRADE_REASONS.items():
        proof = next(p for p in evidence['proofs'] if p['to_id'] == f'AMGT_RESAPP.TO-AMGT-rd-{rd}')
        instance = proof['path'] + '@' + proof['last_commit']['stdout'].strip()
        grades.append({'criterion': f'AMGTrd{rd}-AC4', 'instance': instance, 'verdict': verdict, 'reason': reason})
        if rd == 8:
            grades.append({'criterion': 'AMGTrd8-AC2', 'instance': instance, 'verdict': 'FAIL',
                           'reason': 'AC2 requires an independent clean no-emit staleness check. The issued root --noEmit invocation examines zero source files and misses the positive-control TS2322 error. The worker\'s -b/--force evidence diagnoses the instrument, but AC1 alone does not meet the independent control as issued. FAIL is the criterion/instrument verdict, not an accusation against the worker who correctly refused a false PASS. A corrected invocation and its cold/mutant controls require the issuer\'s existing-cell recut.'})
    result.append({'id': 'AMGT_RESAPP-Z-C-S48', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
                   'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': 'Round 5 grade record: five historical AC4 passes; rd8 AC4 and AC2 fail',
                   'class': 'OBSERVATION', 'hazard_standing': 'INERT',
                   'grounding': {'status': 'GROUNDED', 'evidence': references},
                   'disposition': 'DISMISSED_WITH_REASON', 'dismissal_reason': 'Grade record only; this row adjudicates no investigation item.',
                   'spec_asserts': 'Every executed judgment is graded against the issued bar and its pinned proof; rd8 also requests an AC2 instrument ruling.',
                   'world_is': 'Six executed round-5 orders supply six AC4 judgments; rd3 and rd4 were superseded without execution. All 34 cumulative proof instances are structurally VALID.',
                   'grades': grades,
                   'notes': 'Carrier defect retained from prior rounds: the schema cannot encode bare AC4/AC2 although its description requires exact issued IDs. AMGTrdN-ACk maps explicitly to AMGT_RESAPP.TO-AMGT-rd-N / ACk; proof paths and commits are exact. Historical passes do not recertify post-migration integration. No outcome is marked REALIZED.'})
    result.append({'id': 'AMGT_RESAPP-Z-C-S49', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
                   'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': 'Current chatter scheduler retains old IAM targets and a reference to a removed local table resource',
                   'class': 'OBSERVATION', 'hazard_standing': 'ARMED', 'disarm_owner': CRO,
                   'grounding': {'status': 'GROUNDED', 'evidence': [references[2],
                       'infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf@' + source['head'] + ':68,69,76',
                       'infra/aws/terraform/harvest/dynamodb.tf@' + source['head']]},
                   'disposition': 'GRADUATED',
                   'spec_asserts': 'The existing rd5 scheduled producer must read the article store and write precomputed metrics after the harvest migration.',
                   'world_is': 'At the pinned HEAD, both root .tf files contain zero aws_dynamodb_table declarations, but scheduler IAM references aws_dynamodb_table.security_metrics.arn and two old opal-amgt-articles ARNs. The renamed tables are in another Terraform root. These are source-level unresolved/stale dependencies.',
                   'notes': 'CRO owns the harvest migration; CTO reads this row and COO owns any existing-cell recut. Remedy: reconcile scheduler resource/IAM dependencies with the new estate, validate the whole module, and establish deployed ZIP/universe/table vintage before claiming a future run works. No AWS read, terraform init/validate/apply or live invocation was performed by CVO; this is not a claim that a scheduled production run has already failed. Keep historical RD5 AC4 grade pinned. No new-cell inference is needed: the scheduled producer is an existing cell.'})
    result.append({'id': 'AMGT_RESAPP-Z-C-S50', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
                   'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': 'The rd8 completion narrative exceeds the portal source and route evidence',
                   'class': 'OBSERVATION', 'hazard_standing': 'ARMED', 'disarm_owner': CTO,
                   'grounding': {'status': 'GROUNDED', 'evidence': references + [
                       'portal:e6057f26c57fc6ff6c223f1c73cc29be3c7f51d6:src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx',
                       'org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/AMGT-rd-8.design-decisions-and-rehomed-figures.md']},
                   'disposition': 'GRADUATED',
                   'spec_asserts': 'The existing rd8 cell requires crossed controls, precomputed reads, rehomed figures, landed Print wiring and a read headless render of the route.',
                   'world_is': 'The source implements a partial presentation, while the check substitutes static fixtures and a Print replica. Missing API connections, collapsed controls and source/report inconsistencies remain. This is sufficient to fail AC4 without inventing a runtime outage measurement.',
                   'notes': 'Holder CTO for the grade and integration decision; COO recuts the existing surface cell with the necessary adapter ownership/grants, actual route evidence and any artifact corrections. A missing implementation or grant for work already named in rd8 is not by itself proof that the decomposition lacks a cell. No automatic DECOMP_INVALIDATING disposition, portal promote, task-order mutation or worker message.'})
    late = originals['AMGT_RESAPP-Z-S22']
    result.append({'id': 'AMGT_RESAPP-Z-C-S51', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
                   'surfaced_by': SERIAL, 'surfaced_at': utc,
                   'one_line': 'The late S22 classification defect has a source repair, with a false kill premise still to correct',
                   'class': 'OBSERVATION', 'hazard_standing': 'ARMED', 'disarm_owner': CTO,
                   'grounding': {'status': 'GROUNDED', 'evidence': [
                       'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md@651ffd4f16477b632b593a5e8db69aaca05eacec#AMGT_RESAPP-Z-S22',
                       '.claude/skills/canonical-flow/SKILL.md@652ca9e2dd:154,199,200,224',
                       'integrations/bloomberg/research/tests/test_vintage_derivation_identity.py:37-42',
                       'CVO evidence checkpoint 11a1461029a1edfa4ac8684db20103606cc20c3e',
                       'MSTR correction 21664, exact file 20260911T213059Z_0.0.0_AB_MSTR_Z_CORRECTION_to_my_21657___a_recycle_takes.md']},
                   'disposition': 'GRADUATED', 'adjudicates': ['AMGT_RESAPP-Z-S22'],
                   'spec_asserts': late['spec_asserts'],
                   'world_is': 'Two reported runs on one active round lacked an IN-PROGRESS class; CVO\'s own evidence creation and checkpoint directly corroborate work in progress. CTO commit 652ca9e2dd adds the class, output-plane probe, stalled-test qualifier and report field. The test producer explicitly defines SEC_KEY=VINTAGEID_US_Equity, so the separate unsubstituted-placeholder conjecture is rejected.',
                   'notes': 'The class/probe source remedy is executed by its owner; no full post-edit operational run was performed by CVO. This is one uncovered state, not a proof that every former class assumed absence or a complete state census. Residual correction owed to CTO: the new skill prose and 21672 repeat that killing the process destroys 189 KB of uncommitted files. That is false, already corrected by MSTR 21664: process termination loses in-flight context, not on-disk bytes. Correct that causal claim while retaining the output-plane probe. Hazard remains ARMED for that misleading recovery premise; no seat lifecycle action was taken.'})
    header = '''# AMGT_RESAPP round 5: CVO L8 compilation and L9 adjudication

The packet at ecd494a2a7 reports 55 undispositioned items. The effective append-only census is **55 originals: 31 already dispositioned, 24 awaiting this review**. This document adds exactly one citing decision for each of those 24; it does not rewrite the previous 31 or their grades. Two new CVO observations and one grade record are not original investigation items.

During validation, **S22 arrived at 651ffd4f16**. It is additionally adjudicated in C-S51, including the source repair at 652ca9e2dd and its remaining inaccurate kill premise. The final bounded census is **56 original items: 31 prior plus 25 newly adjudicated; zero undispositioned**. Of the new originals, 18 graduate and seven are dismissed with reason.

Basis: the issued specification, attributed mechanism, measured denominator, named remedy holder, and explicitly bounded evidence vintage. GRADUATED means grounded, not repaired. DISMISSED_WITH_REASON means the stated reason disposes this row, not that every related hazard is gone. Existing cells with incomplete grants or implementations do not automatically justify DECOMP_INVALIDATING.

All **34 cumulative proof instances are structurally VALID** after correcting the CVO audit's initial expected-ID lookup (the retained evidence explains the four instrument errors). Structure is not truth. **37 offline tests pass** with socket connections denied. Round 5 contributes six executed AC4 judgments: **five PASS, one FAIL**, plus **rd8 AC2 FAIL as issued**. rd3 and rd4 were superseded without execution and receive no invented instance or grade.

The table/store/producer grades below are tied to their historical proof commits. They do not certify current migrated infrastructure, the deployed package, a served portal route or an EXERCISED outcome. C-S49 records a newly measured current-source regression; C-S50 records the incomplete surface and evidence substitutions.

**L10 remains blocked.** The production gate's read at the source-control pin sees 1 of 36 orders nonterminal: rd8 is staged. This adjudication is not a status flip or terminal exception. No remediation slug, worker seating, rebase, gitlink move, PROD/DEV promote, AWS act or FWD-15 REALIZED claim is made here. The issuer must consume the two FAIL verdicts and resolve its record; formal remedies follow only when the round's terminal precondition holds.

The L8 census is a bounded compilation snapshot. It makes no unmeasured live-watcher or seat-readiness claim. Original 21642 remains the active packet until this act is committed.

'''
    body = header + '\n\n'.join('## ' + r['id'] + '\n\n```json\n' + json.dumps(r, indent=2, ensure_ascii=True) + '\n```' for r in result) + '\n'
    DOC.write_text(body, encoding='utf-8')
    print(json.dumps({'path': str(DOC.relative_to(ROOT)), 'rows': len(result), 'new_originals_adjudicated': 25,
                      'graduated_originals': 1 + sum(d[1] == 'GRADUATED' for d in DECISIONS),
                      'dismissed_originals': sum(d[1] == 'DISMISSED_WITH_REASON' for d in DECISIONS), 'grades': len(grades)}))


if __name__ == '__main__':
    main()
