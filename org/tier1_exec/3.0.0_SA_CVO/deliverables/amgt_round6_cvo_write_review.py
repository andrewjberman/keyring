"""Author CVO decisions and the two overdue per-round slugs from pinned evidence."""
import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = ROOT / 'org/missions/D5/AMGT/AMGT_RESAPP'
CHANNEL = PROJECT / 'surprise-channel'
SERIAL = '3.0.0_SA_CVO~Z'
COO = '2.0.0_SA_COO~ZZZ'
CTO = '1.0.0_SA_CTO~Z'
CRO = '4.0.0_SA_CRO~Z'
EVIDENCE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND6_CVO_EVIDENCE_20260911_Z.json'


def rows(path):
    out = []
    for block in re.findall(r'```json\s*(.*?)```', path.read_text(encoding='utf-8'), re.S):
        value = json.loads(block)
        out.extend(value if isinstance(value, list) else [value])
    return out


def write_doc(path, header, values):
    if path.exists():
        raise RuntimeError('Refuse to overwrite ' + str(path))
    path.write_text(header + '\n\n```json\n' + json.dumps(values, indent=2, ensure_ascii=True) + '\n```\n', encoding='utf-8')


# suffix, disposition, holder, standing, mechanism/decision, remedy
DECISIONS = [
 ('S23', 'GRADUATED', COO, 'ARMED',
  'rd8 used two insufficient instruments: a references-only no-emit check that examined no source, and a fixture render that did not exercise the page. These are different physical mechanisms with a shared evidence-coverage error. re-1 repairs the compiler invocation and renders the actual route tree, but only loading/empty query states; populated figures and chart layout remain outside that render. The old 56-of-136 mixed-plane count is not the original-item denominator.',
  'Keep the forced compiler build, source denominator and error mutant; add populated real-route and real Print consumer evidence with a discriminating failure control. Preserve rd8 AC2/AC4 FAIL. Do not substitute a literal word ban for proof of executed component/data flow.'),
 ('S24', 'DISMISSED_WITH_REASON', COO, 'INERT',
  'Accept the issuer\'s scoped audit of 15 mechanical criteria across five historical cells as supporting evidence, not a theorem that every other check or integration works. Four live-object reads, two negative reads, four pytest filters, three zero-result denominator checks and two store scans total 15. This does not discharge W7-S7\'s incomplete socket guard or certify a live HTTP boundary. No separate remedy follows from this corroborating census.',
  ''),
 ('S25', 'DISMISSED_WITH_REASON', CTO, 'INERT',
  'Accept the append-only correction: LIMB 6 sign-off enforcement is for newly added task orders, not every modified criterion or grant. Keep the original quotations as at-surfacing evidence. S25\'s present-state S18 premise is also superseded: C-S41 dismissed that current missing-lane false-green assertion; C-S24 retains the independently measured general legacy version fallback. This documentary correction does not authorize widening the gate or reopen a resolved lane signature. No additional repair is inferred solely from the gate\'s stated scope.',
  ''),
 ('W10-S1', 'GRADUATED', COO, 'ARMED',
  'The issued AC3 mutates types.ts then restores from the index, rather than the pre-test working bytes. The worker reports losing about 90 uncommitted lines mid-work, recovering them, then completing a clean post-commit control. The count of one TS2322 establishes detection but cannot establish preservation. This is an issuer instrument defect; no CVO destructive run was made.',
  'Recut the existing verification instrument to isolate the mutation in a scratch copy or snapshot and restore the exact pre-test bytes in a finally step; prove both error detection and byte identity on a deliberately dirty starting file. Do not alter the historical terminal criterion.'),
 ('W10-S2', 'GRADUATED', COO, 'ARMED',
  'Four requested combinations resolve to only two served partitions. Independent resolve_axis calls show FOUR OF FOUR falling back with movement_basis ABSENT: both Trending and Breakout use CHATTER or PRICE. The worker/packet\'s two-of-four statement has the wrong denominator. A static membership edit in a test demonstrates code selection, not producer availability; the available record does not prove the historical word ever.',
  'Make the existing producer/surface contract supply and validate the movement dimension, or obtain an explicit specification correction before claiming four distinct ranking products. Carry requested and served identities visibly; do not invent ranks in the browser. CTO reads the coverage implication and COO chooses the existing-cell recut or decomposition change.'),
 ('W10-S3', 'GRADUATED', COO, 'ARMED',
  'Eleven route declarations and a handler exist in lib/research/api, but the issued paths omit the infrastructure mount. Sixteen local fake-boundary tests pass; a missing X-Firm-Id yields 401 and a body firm cannot replace the header. Those tests do not validate an edge JWT, deployed origin isolation, handler package or served route. comp-iam finds no scoped_amgt service among 188 services/212 roles, so adapter permissions remain unmapped, not green.',
  'Give the existing read-adapter integration obligation an explicit permitted owner and complete grant for mount, packaging, data artifacts, trusted edge boundary and IAM. Exercise authenticated allowed/denied firm paths, actual data reads and Print through the composed consumer before calling it served. Respect the portal promotion freeze.'),
 ('W10-S4', 'GRADUATED', COO, 'INERT',
  'Pinned portal inspection corroborates six affected files, with TEN non-ASCII occurrences across those files, not six or eight characters. CVO\'s denominator is 19 tracked portal files at c6728146, distinct from the worker\'s 27-file mixed working-tree census. The six files are unchanged by the recut. Their presence conflicts with the issued ASCII bound; do-not-rebuild does not establish that replacing display punctuation requires a rebuild.',
  'Name a narrow existing-surface hygiene edit for the ten display-punctuation occurrences, preserving meaning and component behavior. Verify the explicitly named file set. This is an INERT code-conformance item, not a claim about unsafe AWS identifiers or production text rendering.'),
 ('S26', 'GRADUATED', COO, 'INERT',
  'Issuance 4352fe1c47 superseded rd8 and opened re-1 in the same commit before the round-5 slug and CTO analysis, keeping the project-wide L10 order census nonzero. Drain b2cd6e9ee7 now yields zero of 37; POSN and nonexistent-project controls discriminate. Accept the sequencing violation and its explicit nonprecedent ruling. Do not attribute the full claimed 93-minute interval to the 22:24 issuance: that interval begins at 21:41, before the inversion, and its endpoints are not the issuance-to-drain interval. Nor does the census prove that CVO performed no useful review while gated.',
  'The owner let re-1 drain without an override; CTO 3a00618246 recorded the ordering rule and BLOCKED-before-probe check. This slug restores the missing handoff. Preserve those facts, then wait for the CTO analysis before any next issuance. The completed recovery is not permission to repeat the inversion.'),
]


def main():
    evidence = json.loads((ROOT / EVIDENCE).read_text(encoding='utf-8'))
    assert evidence['orders']['AMGT_RESAPP'] == [[], 37, '']
    assert evidence['proof_structure']['rc'] == 0 and evidence['adapter_tests']['rc'] == 0
    assert all(evidence['source_matches_worker_pin'].values())
    assert len(evidence['thesis_response']['fiscal_year_figures']) == 0
    originals = {r['id']: r for r in rows(CHANNEL / 'investigations/INVESTIGATION_v1.md')}
    open_ids = {k for k, v in evidence['dispositions_before'][0].items() if v == 'UNDER_INVESTIGATION'}
    assert open_ids == {'AMGT_RESAPP-Z-' + d[0] for d in DECISIONS}
    utc = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    decisions = []
    remedies6 = {}
    for n, (suffix, disp, owner, standing, reason, remedy) in enumerate(DECISIONS, 52):
        target = 'AMGT_RESAPP-Z-' + suffix
        original = originals[target]
        row = {'id': f'AMGT_RESAPP-Z-C-S{n}', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
               'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': reason.split('. ')[0],
               'class': 'OBSERVATION', 'hazard_standing': standing,
               'grounding': {'status': 'GROUNDED', 'evidence': [EVIDENCE,
                   'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#' + target,
                   *original['grounding']['evidence']]},
               'disposition': disp, 'adjudicates': [target],
               'spec_asserts': original['spec_asserts'], 'world_is': reason, 'notes': remedy or reason}
        if standing == 'ARMED':
            row['disarm_owner'] = owner
        if disp == 'DISMISSED_WITH_REASON':
            row['dismissal_reason'] = reason
        else:
            remedies6[target] = (row, owner, remedy, suffix == 'S26')
        decisions.append(row)
    grade_reason = ('FAIL against the full issued AC6. Crossed control state, producer-order Starred filtering, and the date-based chart implementation are present at portal c6728146. '
                    'However, all four crossed requests fall back to two subject partitions; the handler is unmounted; and read_thesis_bundle returns zero fiscal figures from 183 fiscal_year_line_item figures because it filters fiscal_year. '
                    'Its model read also bypasses the corrected fiscal-price overlay. Thus the Model figures are not actually rehomed. The server render uses real route components but only loading/empty data; '
                    'Print calls the real request function with a fake fetch, not the rendered button or backend renderer; chart SVG/layout is not exercised. Sixteen passing fake-boundary tests do not meet these missing clauses. '
                    'This verdict separates delivered code and issuer grant gaps from implementation defects; it is not a judgment of worker honesty, a measured live outage, or an EXERCISED outcome grade.')
    decisions.append({'id': 'AMGT_RESAPP-Z-C-S60', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
      'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': 're-1 AC6 FAIL: the requested end-to-end shape and rehomed figures are incomplete',
      'class': 'OBSERVATION', 'hazard_standing': 'INERT', 'grounding': {'status': 'GROUNDED', 'evidence': [EVIDENCE]},
      'disposition': 'DISMISSED_WITH_REASON', 'dismissal_reason': 'Grade record only; no investigation item is dismissed by this carrier.',
      'spec_asserts': 'AMGT_RESAPP.TO-AMGT-re-1 AC6 requires all four gaps closed and Model figures actually rehomed.',
      'world_is': grade_reason,
      'grades': [{'criterion': 'AMGTre1-AC6', 'instance': evidence['proof_path'] + '@' + evidence['proof_commit']['stdout'].strip(), 'verdict': 'FAIL', 'reason': grade_reason}],
      'notes': 'AMGTre1-AC6 maps to the issued AMGT_RESAPP.TO-AMGT-re-1 / AC6. The existing carrier schema cannot encode bare AC6. The five mechanical outputs are read at their pinned instance; corrected build/listFiles/mutant controls support nonvacuous compilation but do not establish preservation by AC3 or close the route. No terminal order is rewritten.'})
    own = [
      (61, 'The Thesis adapter drops all 183 fiscal-year figures through a scope-token mismatch',
       'The issued AC6 requires the removed Model tab\'s figures actually rehomed into Thesis and the Security overlay.',
       'At source e83bdbe7c1, _figures(model, fiscal_year) matches zero rows. The actual BABA model holds 13 header figures and 183 fiscal_year_line_item figures. read_thesis_bundle returns 13 header figures and zero fiscal figures/checks for those fiscal rows. This is a measured composed local consumer failure, not inferred from the UI screenshot.',
       'Use the actual canonical scope contract and exercise the populated Thesis consumer against the landed artifact, requiring preservation of all fiscal figures and their checks. Add a wrong-scope negative control. Keep the real route data in the render test.'),
      (62, 'The new API model consumer bypasses the corrected fiscal-price overlay',
       'The existing fiscal consumer contract overlays corrected period prices and preserves unresolved/refusal and derivation identity before presentation.',
       'read_model_block reads only the historical raw model. Independent reads find ten raw fiscal PX_LAST rows and ten corrected rows from the existing Print load_model_block consumer; all ten values differ (for example FY2025 raw 146.58 versus corrected 132.23). The new adapter never calls the corrected-overlay contract. Currently the scope mismatch hides those fiscal rows; fixing that filter alone would expose stale values. This is a new consumer regression, not reopening the historical round-4 Print grade.',
       'Wire the API to the shared corrected-model consumer contract, preserving original vintage, observation date, derivation identity and unresolved refusal. Exercise both resolved and unresolved fiscal overlays through the new API and real populated Thesis route; do not rewrite historical model artifacts.'),
      (63, 'The time-series adapter silently treats unprocessed batch keys as absent data',
       'A chart claiming landed-day and point-count denominators must distinguish absent rows from reads not completed.',
       'The controlled processed response yields one point. A response returning the same requested key in UnprocessedKeys yields zero points with no completeness/error field and no retry; the fake records exactly one call. Sixteen existing tests pass because their fake never returns UnprocessedKeys. No live throttling event was measured.',
       'Handle unprocessed keys with a bounded retry policy or explicit incomplete-read refusal, preserve the unresolved denominator, and test processed, genuinely absent, partially processed and retry-exhausted responses. Do not describe a transport omission as a missing producer day.'),
    ]
    for n, title, bar, world, remedy in own:
        row = {'id': f'AMGT_RESAPP-Z-C-S{n}', 'project': 'AMGT_RESAPP', 'fabric': 'site-z',
          'surfaced_by': SERIAL, 'surfaced_at': utc, 'one_line': title, 'class': 'OBSERVATION',
          'hazard_standing': 'ARMED', 'disarm_owner': COO,
          'grounding': {'status': 'GROUNDED', 'evidence': [EVIDENCE, 'lib/research/api/scoped_amgt.py@e83bdbe7c1fd076f94e87ba6749836bd0eca5cf6']},
          'disposition': 'GRADUATED', 'spec_asserts': bar, 'world_is': world,
          'notes': 'Existing surface/read-adapter cell remedy, holder ' + COO + ': ' + remedy}
        decisions.append(row)
        remedies6[row['id']] = (row, COO, remedy, False)
    header6 = '''# AMGT_RESAPP round 6: CVO L8 compilation and L9 adjudication

Drain b2cd6e9ee7, packet 935d932bbf, messages 21778 and 21792. Independent evidence is in ''' + EVIDENCE + '''. Review head is ''' + evidence['head']['stdout'].strip() + '''; the source hash and worker-pin comparisons are retained. The new proof at 8d6c289dc8 is structurally VALID from the merged main tree. That corrects the packet's time-local premerge INVALID result; two portal artifacts require the separately verified portal object store. This review does not pretend to reproduce the deleted worker checkout.

The census is **64 original investigation items: 56 previously dispositioned, eight awaiting this review**. C-S52 through C-S59 dispose exactly those eight: six GRADUATED and two DISMISSED_WITH_REASON. C-S60 records the one new judgment; C-S61 through C-S63 add three independently grounded consumer findings. No original row is edited. **re-1 AC6 is FAIL.** Historical grades remain at their own pins, including rd8 AC2/AC4 FAIL.

Sixteen adapter tests pass with socket connections denied for the entire run. Compilation evidence at the worker pin prints 2069 examined files, including 18 surface files, and catches its TS2322 mutant. Those controls repair the specific compiler-vacuity defect; their restore command has a separate data-preservation defect. The route render uses actual components but empty/loading queries, a stubbed Print transport and no chart layout. It cannot cover the missing populated consumer flow found here.

The order census is independently zero open of 37, with POSN five of 15 and nonexistent-project zero of zero controls. All 35 cumulative proof instances are structurally VALID by the prior 34-instance audit plus this new merged instance. No new decomposition-invalidating finding is inferred merely from a missing grant or implementation. CTO reads coverage; COO chooses the recut after that analysis.

Corrections to the packet: four of four combinations fall back, not two; the four-row armed floor is not trustworthy because S19's immediate object-preservation hazard is already disarmed by the verified fetch; neither string mentions nor immutable at-surfacing standing are current clocks. Current obligations are the explicit remediation rows, with prior numbered slugs retained. The packet's 93-minute causal attribution is not adopted. The worker's future-dated row timestamps are preserved as reported and are not the CVO measurement clock.

The COO ACK attempt was refused by codex-send's CVO-to-COO guard; no ACK was delivered or retried through another route. The final handoff goes only to CTO. Both rounds now have terminal orders, but neither this grade nor the slug authorizes portal promotion, a gitlink move, an AWS act, a new task order or FWD-15 REALIZED.
'''
    write_doc(CHANNEL / 'adjudications/ADJUDICATION_v6.md', header6, decisions)

    def rem(rid, row, owner, remedy, closed, version):
        standing = row.get('hazard_standing', 'INERT')
        result = {'id': rid, 'project': 'AMGT_RESAPP', 'fabric': 'site-z', 'class': row['class'],
          'hazard_standing': standing, 'mechanism': row['world_is'],
          'evidence': row['grounding']['evidence'] + [EVIDENCE], 'remedy': remedy,
          'owner': owner, 'round': version,
          'remediation': {'state': 'REMEDIATED' if closed else 'OPEN', 'owner': owner, 'round': version}, 'closed': closed}
        if standing == 'ARMED':
            result['disarm'] = {'state': 'DISARMED' if closed else 'ARMED', 'owner': owner, 'at': utc if closed else None}
        return result

    v5 = rows(CHANNEL / 'adjudications/ADJUDICATION_v5.md')
    rem5 = []
    for row in v5:
        if row['disposition'] != 'GRADUATED':
            continue
        rid = (row.get('adjudicates') or [row['id']])[0]
        owner = row.get('disarm_owner', COO)
        remedy = row['notes']
        closed = rid in {'AMGT_RESAPP-Z-S11', 'AMGT_RESAPP-Z-S19', 'AMGT_RESAPP-Z-W2-S8', 'AMGT_RESAPP-Z-W2-S9'}
        if rid == 'AMGT_RESAPP-Z-S19':
            remedy = 'Immediate only-copy risk disarmed: both e6057f26 and c6728146 are preserved in the main portal object store before teardown, with the latter positive and bogus-object controls in the round-6 evidence. Do not merge or advance the gitlink. Remaining base/integration hold is S16/S21, not a reason to count S19 preservation as still unperformed.'
        elif rid == 'AMGT_RESAPP-Z-W2-S8':
            remedy = 'Existing compiler-selection defect corrected in issuance 4352fe1c47 using npx --package typescript; the forced-build proof 8d6c289dc8 reports 2069 source files and a detected TS2322. This closes this issued instrument instance, not a claim about every future npm resolution.'
        elif rid == 'AMGT_RESAPP-Z-W2-S9':
            remedy = 'Existing vacuous root no-emit criterion was replaced in re-1 by forced referenced-project build plus source-file and error-mutant controls, evidenced at 8d6c289dc8. Preserve the historical rd8 FAIL. The new restore hazard is separately OPEN as W10-S1.'
        elif rid == 'AMGT_RESAPP-Z-S11':
            remedy = 'The issuer superseded competing rd3/rd4 without an invented proof or apply. The 37-order terminal census corroborates that recovery. No further worker order is needed for this duplicate-builder collision.'
        elif rid == 'AMGT_RESAPP-Z-C-S49':
            remedy += ' Current comp-iam role read still lists the two old article ARNs; no deployed permission or module validation claim is made. This remains with CRO in place and is not assigned to the frontend worker.'
        elif rid == 'AMGT_RESAPP-Z-S22':
            remedy += ' At the round-6 read .claude/skills/canonical-flow/SKILL.md:222 still says a kill would destroy 189 KB of uncommitted work. Correct it to loss of in-flight context; on-disk files persist absent a separate deletion. New BLOCKED/output-plane source improvements do not repair this remaining sentence.'
        remedy = remedy.replace(' L10 has not been issued; a named remedy holder is not a worker assignment.', '')
        rem5.append(rem(rid, row, owner, remedy, closed, 'v5'))
    assert len(rem5) == 20
    header5 = '''# AMGT_RESAPP round 5 L10 remediation slug

From 3.0.0_SA_CVO~Z to 1.0.0_SA_CTO~Z only. This is the previously withheld round-5 slug, issued alongside the separately numbered round-6 slug in one handoff. Its vintage is its commit. The prior L9 is ADJUDICATION_v5.md@655c1a810e; its historical block statement is preserved. rd8 is now superseded, re-1 complete, and the actual project census is zero open of 37 after b2cd6e9ee7.

Round 5: five historical AC4 PASS, rd8 AC4 FAIL and rd8 AC2 FAIL. There were 25 newly dispositioned originals (18 graduated, seven dismissed), plus two CVO findings. The 20 formal rows below cover those 18 originals and C-S49/C-S50 exactly once. Four instance remedies are already executed and closed (S11, S19, W2-S8, W2-S9); 16 remain OPEN. Object preservation is distinct from frozen portal integration; corrected compiler verification is distinct from AC3's newly found destructive restoration.

Earlier numbered slugs retain their original rows and clocks; their IDs are not duplicated here. No previous open row is silently closed by this document. The continuing scheduler/IAM issue C-S49 is an in-place CRO obligation; compiler/gate/seat tooling obligations remain with their existing disarm owners. They do not authorize AMGT workers to modify another project's surfaces. CTO reads these findings under the spine's in-place-or-owning-project rule before the COO recuts.

The physical contract is route-free, as the current gate and spine require. Some schema descriptions retain retired routing vocabulary; this slug does not use it. The round-6 recut preceded this slug and the round-5 CTO analysis contrary to Rule 27, acknowledged in S26. Letting that cell drain has restored the order precondition; it is not a precedent or an override. The round-6 slug supplies its independently graded result and the remaining surface obligations. A drained queue is not a passed outcome. PROD/DEV remain frozen and FWD-15 is not declared REALIZED.
'''
    write_doc(CHANNEL / 'remediations/REMEDIATION_v5.md', header5, rem5)
    values6 = [rem(rid, *data, 'v6') for rid, data in remedies6.items()]
    header_rem6 = '''# AMGT_RESAPP round 6 L10 remediation slug

From 3.0.0_SA_CVO~Z to 1.0.0_SA_CTO~Z only; vintage is this file's commit. Read together with the overdue REMEDIATION_v5.md, delivered in the same message, and ADJUDICATION_v6.md. re-1 proof@8d6c289dc8 is structurally VALID; **AC6 FAIL**. Sixteen offline adapter tests pass. The 64-original census is fully dispositioned after the eight citing decisions, without changing originals. The order census is zero open of 37. Detailed controls, source pins and declared limitations are in ''' + EVIDENCE + '''.

Nine rows follow: six graduated originals plus three CVO consumer findings. S26's sequencing recovery is executed and closed; eight remedies remain OPEN. S24 and S25 are dismissed with explicit reasons in adjudication, not converted into invented repair work. No original ID appears in two remediation slugs.

The page now has independently crossed control state, producer-order Starred filtering and a date-indexed chart implementation. It still cannot support the full completion claim: four requested combinations use two subject partitions, the API is unmounted, the Thesis consumer drops 183 fiscal rows, its raw-model read bypasses corrected prices, and incomplete batch reads can masquerade as absent history. The empty-state server render and fake Print transport leave those paths unexercised. These are existing surface/producer/verification obligations needing correct contracts and grants; no absent-cell inference is made by default.

CTO: read both slugs and their judgments against outcome coverage, then issue the required analysis/addendum under L10. COO recuts only after that read, in one issuance. Keep C-S49 with CRO, preserve both portal objects, and retain the current PROD/DEV freeze. No worker receives this slug directly. No served-plane, deployment, permission or outcome-realization claim is inferred from committed code or a VALID proof.
'''
    write_doc(CHANNEL / 'remediations/REMEDIATION_v6.md', header_rem6, values6)
    print(json.dumps({'adjudication_rows': len(decisions), 'originals': len(DECISIONS), 'remediation5': len(rem5), 'remediation6': len(values6), 'open5': sum(not r['closed'] for r in rem5), 'open6': sum(not r['closed'] for r in values6)}))
    append_late_s27()


def append_late_s27():
    """S27 arrived during validation; preserve the initial eight-item audit vintage."""
    original = next(r for r in rows(CHANNEL / 'investigations/INVESTIGATION_v1.md') if r['id'] == 'AMGT_RESAPP-Z-S27')
    adj_path = CHANNEL / 'adjudications/ADJUDICATION_v6.md'
    rem_path = CHANNEL / 'remediations/REMEDIATION_v6.md'
    adj = rows(adj_path)
    assert not any(r['id'] == 'AMGT_RESAPP-Z-C-S64' for r in adj)
    utc = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    reason = ('The issuer prescribed a comp-iam rerun without first establishing coverage of the new library adapter. '
              'CVO independently found no scoped_amgt service match; the issuer\'s full rerun reports no adapter call site while finding 37 infra/aws/lambda lines. '
              'These scoped results do not certify adapter permissions. Unchanged aggregate totals alone are not proof of unchanged membership; the path-level negative and positive controls are the relevant evidence. '
              'The three Terraform roots describe policy-source coverage, so that line alone is not a complete Python-call corpus proof. The measured remedy gap is the absent adapter-to-role/call-site mapping, not a proven IAM denial or a claim that libraries can never be analyzed transitively.')
    remedy = ('For the existing adapter integration and preflight obligation, require the actual adapter call sites and their role binding to appear in the instrument denominator, '
              'then evaluate action AND resource grants against the actual package/mount. Carry explicit OUT-OF-CORPUS/UNMAPPED when absent. '
              'Coordinate with W10-S3; merely adding a mount or repeating unchanged totals cannot close the coverage obligation.')
    row = {'id': 'AMGT_RESAPP-Z-C-S64', 'project': 'AMGT_RESAPP', 'fabric': 'site-z', 'surfaced_by': SERIAL, 'surfaced_at': utc,
           'one_line': 'Late S27: a rerun without adapter call-site and role coverage cannot resolve the IAM gap', 'class': 'OBSERVATION',
           'hazard_standing': 'ARMED', 'disarm_owner': COO, 'grounding': {'status': 'GROUNDED', 'evidence': [EVIDENCE,
           'org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S27', *original['grounding']['evidence']]},
           'disposition': 'GRADUATED', 'adjudicates': ['AMGT_RESAPP-Z-S27'], 'spec_asserts': original['spec_asserts'], 'world_is': reason, 'notes': remedy}
    remrow = {'id': 'AMGT_RESAPP-Z-S27', 'project': 'AMGT_RESAPP', 'fabric': 'site-z', 'class': 'OBSERVATION', 'hazard_standing': 'ARMED',
              'mechanism': reason, 'evidence': row['grounding']['evidence'], 'remedy': remedy, 'owner': COO, 'round': 'v6',
              'remediation': {'state': 'OPEN', 'owner': COO, 'round': 'v6'}, 'disarm': {'state': 'ARMED', 'owner': COO, 'at': None}, 'closed': False}
    for path, newrow in [(adj_path, row), (rem_path, remrow)]:
        text = path.read_text(encoding='utf-8')
        current = rows(path)
        current.append(newrow)
        header = text.split('```json', 1)[0]
        header += ('\nLate intake during validation: **S27** raises the final census to **65 originals**, with **nine newly adjudicated (seven graduated, two dismissed)**. '
                   'C-S64 is its citing decision. The round-6 slug now has **ten remediation rows: nine OPEN, one REMEDIATED**, '
                   'including the explicit adapter IAM coverage obligation. The initial eight-item evidence snapshot is retained at its measured vintage.\n\n')
        path.write_text(header + '```json\n' + json.dumps(current, indent=2, ensure_ascii=True) + '\n```\n', encoding='utf-8')
    print('Late S27 appended as C-S64 and remediation S27; no original row edited.')


if __name__ == '__main__':
    main()
