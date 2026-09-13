"""Write CVO round-8 decisions with original bytes and old remedy text preserved."""

import datetime
import json
import re
from amgt_round8_cvo_intake import ROOT, HOME, PROJECT, records

SERIAL = "3.0.0_SA_CVO~Z"
COO = "2.0.0_SA_COO~ZZZ"
CTO = "1.0.0_SA_CTO~Z"
CRO = "4.0.0_SA_CRO~Z"
CHANNEL = ROOT / PROJECT / "surprise-channel"
PREFIX = "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
EVIDENCE = [
    PREFIX + "AMGT_RESAPP_ROUND8_CVO_" + s + "_20260913_Z.json"
    for s in ["INTAKE", "EVIDENCE", "PORTAL", "TYPES", "SUPPLEMENT"]
]
# suffix, disposition, holder, executed, observed world, action or disposition reason.
D = "DISMISSED_WITH_REASON"
G = "GRADUATED"
DECISIONS = [
    (
        "S46",
        D,
        COO,
        False,
        "The 30-item claim was superseded twice and combines original findings with CVO carriers while treating token-near disarms as current state. It is not an authoritative live-obligation count.",
        "Retain the correction history; use all canonical channel files, both JSON shapes, original IDs and actual remedy clocks. No separate new remedy follows from the withdrawn count.",
    ),
    (
        "S47",
        G,
        CTO,
        True,
        "The round closes with every portal-dependent result EXERCISED-NOT-REALIZED. a845a8be75 is preserved under refs/drains/rg-2-portal and is contained by zero of nine freshly listed remote heads; the gitlink remains e85f6eb84f.",
        "Condition (b) is met by this round's explicit object-scoped grades. No remote promotion or integration is inferred; S21/W11-S1 remain separate.",
    ),
    (
        "S48",
        D,
        COO,
        False,
        "The wider domain correction is valid, but 53 remains a historical candidate-field count, later corrected by S56; a complete file denominator does not prove a live obligation count.",
        "Apply the canonical all-file, per-fence census; retain the nine-row cut denominator as a different population. No new cell or duplicate remedy follows.",
    ),
    (
        "S49",
        G,
        COO,
        True,
        "A materialized clean portal can make its parent gitlink dirty before worker activity. S60 records the required same-sweep nested porcelain check at zero, attributing that dirt to the issuer.",
        "Accept that measured owner probe as the row's literal disarm. Preserve the nested-repository identity check and do not treat a dirty gitlink as production.",
    ),
    (
        "S50",
        D,
        CTO,
        False,
        "Owner parser repair 5661885 is corroborated: to-check now reads AMGT 0 and POSN 4, matching canonical 0/46 and 4/15; directive D5 reads 0 over its AMGT member.",
        "Advance existing S36/S42 remedy clocks once; this is recovery evidence, not a second parser task. Historical 0/43 remains its pinned vintage.",
    ),
    (
        "W14-S1",
        G,
        COO,
        True,
        "The prose abbreviation binds a bare function while the recorded invocation resolves the module attribute. Under a patch they yield wrong-scope 0 and 196 respectively. The worker compared both and also exercised the source predicate; CVO independently reproduced the binding distinction.",
        "The present invocation identity debt is discharged by the pinned executed string and both measured forms. Keep terminal text historical; a future identical rerun must cite the actual instance, not its abbreviation.",
    ),
    (
        "W14-S2",
        G,
        COO,
        True,
        "AC1's scopes.py cmp cannot validate the separate matcher source. Worker AC4 covers both modules and the additional matcher-file cmp/hash supplies the missing restoration evidence. CVO reproduces the in-process mutant without shared-file writes and verifies unchanged source hashes.",
        "Accept the explicit second instrument and exact mutated-file restoration for this run. Do not credit the wrong-file cmp as that guarantee or recut completed measurement merely to restate it.",
    ),
    (
        "S51",
        G,
        CTO,
        True,
        "S52 records each of the twelve candidates required by S51. That bounded read satisfies S51's literal condition; subsequent domain and block-shape omissions are separately carried by S53/S57.",
        "Close the twelve-item reading obligation only. Its historical count is not a complete current census and CVO carriers are not additional independent hazards.",
    ),
    (
        "S52",
        D,
        CTO,
        False,
        "The twelve-item read is real but the ten-live headline includes S51, which this same row disarms. Later seven omitted CVO carriers are handled in S59. Neither ten nor the original three is adopted as a current total.",
        "Retain the paired readings; close S51 once, and carry substantive conditions through their existing remediation IDs rather than new obligations for every carrier.",
    ),
    (
        "S53",
        G,
        CTO,
        False,
        "The reader was blind to multiple fences and to another project's candidates. S55/S57 correct the parser counts, but S59 still explicitly owes the POSN standing read. No proof of that completed read is in this intake.",
        "CTO completes the named POSN candidate-by-candidate read, with citing recovery or remaining condition, using both roots and both JSON block shapes. Coordinate this one read with S57; do not cut two cells or widen to other projects.",
    ),
    (
        "S54",
        D,
        COO,
        False,
        "The item/facet distinction is useful, but a unique CVO carrier ID and the original it adjudicates still describe one finding. Distinct IDs alone do not resolve those causal duplicates; S56 supersedes its row totals.",
        "Use original-to-adjudication-to-remedy relationships and actual states. Retain the structural observation without treating its field-count candidates as new work.",
    ),
    (
        "S55",
        D,
        CTO,
        False,
        "Per-fence parsing repaired the first-bracket/last-bracket failure. The claim of three malformed files was itself superseded by single-object admission in S56/S57; this CVO intake parses all 15 AMGT files with zero malformed JSON fences.",
        "Retain the correction as evidence under S53/S57. Do not repair valid object-per-fence documents or label them corrupt.",
    ),
    (
        "S56",
        D,
        COO,
        False,
        "ADJUDICATION_v5 has 28 valid single-object JSON fences. The CVO reader accepts them; the initial audit sees 20 array and 28 object JSON fences across 15 files. The 63 candidate IDs are not adopted as 63 outstanding remedies.",
        "The correct admission rule is applied in this review. Historical counts retain their vintages; no original or graded proof bytes are rewritten.",
    ),
    (
        "W13-S1",
        G,
        COO,
        True,
        "The worker build did not start, and an unpinned npx request is not the declared ~5.9.3 toolchain. CVO independently used the already-installed compiler with matching package/lock manifests in a disposable a845a8be75 source archive: 2072 files, rc0, zero errors; the planted component type error produced TS2322 and rc2.",
        "The current verification gap is now measured and closed at L9, not retroactively credited to the worker. Preserve the worker's absence and its FAIL judgment. No registry egress or grant widening was necessary for the CVO check.",
    ),
    (
        "W13-S2",
        G,
        COO,
        True,
        "The original vitest invocation was unavailable. The issuer amended the runner to plain node while retaining the 183/183, 13/13 and unresolved controls; CVO independently executes the actual checkFor and actual populated Thesis/ProvenanceLine, confirming the joins and refusal.",
        "Accept the amended runner and the independent consumer execution. Do not add an undeclared test runner or rewrite the initial failed instance.",
    ),
    (
        "W13-S3",
        G,
        COO,
        False,
        "scopes.py defines vocabulary; run_checks.figure_id composes identity. The order granted the former and the worker explicitly read the latter outside its named grant. Correct source grounding does not retroactively supply that grant.",
        "COO resolves the disclosed read-boundary defect in the existing identity-cell instruction: name the composition module as a read surface in any future applicable issuance and explicitly record the present exception disposition. No producer-ID rewrite or worker recut is inferred.",
    ),
    (
        "W13-S4",
        G,
        COO,
        True,
        "The two type declarations also drifted: fiscal_year scope was absent from all 196 figures, and 183 fiscal years are strings. The in-grant types.ts repair admits fiscal_year_line_item and string|number|null; CVO's full referenced-project build and populated consumer exercise now pass.",
        "Accept the executed adjacent type repair. It establishes the measured artifact domain, not every possible consumer or future schema.",
    ),
    (
        "W13-S5",
        G,
        COO,
        True,
        "The worker decision harness did not render RankedChart. At L9 CVO renders the actual pinned component with fresh offline adapter outputs: absent/partial/exhaust lengths 328/1554/775, three distinct hashes, unresolved denominator retained; the old component's absent/exhaust hashes collide.",
        "Close the bounded static-component gap with actual React rendering and signal-only control. Browser effects, full served route and publication remain outside this result and under their existing obligations.",
    ),
    (
        "W13-S6",
        G,
        COO,
        True,
        "The typecheck and its falsifier were both absent in the worker. CVO's isolated matching-toolchain build examines 2072 files and catches the deliberately planted string-to-number error in RankedChart; exact snapshot bytes are restored.",
        "The source coverage debt is completed at L9. Worker-absence judgments remain FAIL as historical readings; there is no outstanding reason to rerun this same check or amend terminal orders.",
    ),
    (
        "W13-S7",
        G,
        COO,
        True,
        "The old guarded snapshot/unconditional restore could create a wrong-path file from stale scratch bytes. S58's retirement of AC4's invocation removes that current rerun trigger. Removal of one stale file alone would not prevent future fixed-path reuse.",
        "Accept the structural retirement and attributed cleanup for this order. This differs from literally performing two of the three named menu arms; preserve that distinction and use guarded per-run snapshots prospectively.",
    ),
    (
        "S57",
        G,
        CTO,
        False,
        "S59 reads the seven omitted AMGT carriers, but S57's explicit disarm also requires finishing the POSN standing read. S59 says that remains owed, so the headline claiming S57 fully disarmed is not accepted.",
        "Finish the same bounded POSN paired read carried by S53; one action can close both residuals. Preserve the seven AMGT readings and do not count their CVO carriers as seven new implementation obligations.",
    ),
    (
        "S58",
        D,
        COO,
        False,
        "This owner recovery row self-dismissed before CVO review. Its invocation-retirement evidence is accepted for W13-S7; the claim of two literal menu arms is over-specific because retirement and one-time cleanup differ from path correction and unique per-run snapshots.",
        "Record the CVO disposition now without editing the original self-disposition. W13-S7 graduates as a real defect with a completed remedy; S58 is its evidence carrier, not a second task.",
    ),
    (
        "S59",
        D,
        CTO,
        False,
        "The seven omitted AMGT carrier readings are recorded, including S22's source correction at 2981c4bd72, which CVO reads back. The full S57 disarm remains incomplete because POSN is explicitly still owed.",
        "Advance existing S22 clocks on the corrected source; accept only the completed AMGT portion. Carry the POSN residual under S53/S57 and the integration freeze under existing S21.",
    ),
    (
        "S60",
        G,
        COO,
        True,
        "A reused worktree contains issuer staging and predecessor artifacts. This row's own measured sweep records the spawn window, one modified file attributable to the issuer, a 57-file wider-window control, and clean nested portal porcelain.",
        "Those observations satisfy its named probe condition. Close this measurement obligation without treating inherited presence as movement, inferring a stall, or changing any worker lifecycle.",
    ),
    (
        "W13-S8",
        G,
        COO,
        True,
        "With nonzero partial data, the pre-repair rule has one colliding pair, not a three-way collapse. The second amendment b05231914f names absent==exhausted and requires its equal hashes; the fresh worker run and CVO's actual old component both fire that negative control.",
        "Accept the repaired pair predicate, preserving all other bars. Keep the impossible previous wording and its failed proof historical; no new cell is needed.",
    ),
    (
        "S61",
        G,
        COO,
        False,
        "CTO attributes the PRD's first bar regime to c0b5636ea9 and distinguishes the later per-row expansion at 8019bf6433. The current explanation brief still says ninety-eight minutes at its headline; the stated original-to-issuance interval is 2h03m51s.",
        "The brief's author corrects that one figure or records a reasoned ruling that it stands, citing the birth and issuance pins. This is an existing-document correction, not a new product cell or a claim that outcome bars changed.",
    ),
    (
        "S62",
        D,
        COO,
        False,
        "The proposed unwired finding was withdrawn before being asserted. The pinned hook imports getThesisBundle and getRankTimeSeries from the endpoint adapter; the queryFn edge exists. A network-call grep in the component layer does not decide transport correctness or frontend completion.",
        "Retain the narrow/wider-layer lesson and actual edge evidence. Do not create an unwired-page cell from the withdrawn zero or promote the import edge into a served-route PASS.",
    ),
]


def write_doc(path, intro, rows):
    assert not path.exists(), f"Refuse to overwrite existing review {path}"
    path.write_text(
        intro
        + "\n\n```json\n"
        + json.dumps(rows, indent=2, ensure_ascii=True)
        + "\n```\n",
        encoding="utf-8",
    )


def main():
    intake = json.loads(
        (HOME / "AMGT_RESAPP_ROUND8_CVO_INTAKE_20260913_Z.json").read_text()
    )
    supplement = json.loads(
        (HOME / "AMGT_RESAPP_ROUND8_CVO_SUPPLEMENT_20260913_Z.json").read_text()
    )
    originals = {r["id"]: r for r in supplement["all_originals"]}
    utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    decisions, remedies = [], []

    def carrier(n, title, world, bar, disposition=D, hazard="INERT", owner=None):
        row = {
            "id": f"AMGT_RESAPP-Z-C-S{n}",
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "surfaced_by": SERIAL,
            "surfaced_at": utc,
            "one_line": title,
            "class": "OBSERVATION",
            "hazard_standing": hazard,
            "grounding": {"status": "GROUNDED", "evidence": EVIDENCE},
            "disposition": disposition,
            "spec_asserts": bar,
            "world_is": world,
        }
        if disposition == D:
            row["dismissal_reason"] = world
        if hazard == "ARMED":
            row["disarm_owner"] = owner
        return row

    def remediate(rid, row, owner, remedy, closed):
        value = {
            "id": rid,
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "class": "OBSERVATION",
            "hazard_standing": row["hazard_standing"],
            "mechanism": row["world_is"],
            "evidence": row["grounding"]["evidence"],
            "remedy": remedy,
            "owner": owner,
            "round": "v8",
            "remediation": {
                "state": "REMEDIATED" if closed else "OPEN",
                "owner": owner,
                "round": "v8",
            },
            "closed": closed,
        }
        if value["hazard_standing"] == "ARMED":
            value["disarm"] = {
                "state": "DISARMED" if closed else "ARMED",
                "owner": owner,
                "at": utc if closed else None,
            }
        return value

    for n, (suffix, disp, owner, closed, world, remedy) in enumerate(DECISIONS, 103):
        rid = "AMGT_RESAPP-Z-" + suffix
        original = originals[rid]
        row = carrier(
            n,
            suffix + ": " + world.split(". ")[0],
            world,
            original["spec_asserts"],
            disp,
            original["hazard_standing"],
            owner,
        )
        row["adjudicates"] = [rid]
        row["notes"] = remedy
        row["grounding"]["evidence"] = EVIDENCE + [original["source"] + "#" + rid]
        decisions.append(row)
        if disp == G:
            remedies.append(remediate(rid, row, owner, remedy, closed))
    grade_reasons = [
        (
            1,
            1,
            "FAIL",
            "The requested judgment is of the worker's lost typecheck coverage: no compiler ran there. That absence and its reason are upheld, not converted to a worker PASS. Separate CVO L9 verification now fills the source gap: pinned a845a8be75 archive, matching retained package/lock dependencies, tsc 5.9.3, 2072 files, rc0/no errors; mutated RankedChart produces TS2322/rc2 and exact-byte restore. No repeated build or terminal-order rewrite is owed.",
        ),
        (
            1,
            5,
            "PASS",
            "The actual canonical identity joins 183/183 fiscal and 13/13 header rows from fresh local adapter output. Actual populated ThesisTab and real ProvenanceLine render 196 rows, preserve the unresolved REFUSE, hide its raw 146.58 and keep a PASS value visible. The old key control joins zero fiscal rows. Producer IDs remain unchanged. The disclosed ungranted producer-module read is separately W13-S3; a successful behavior grade does not grant it retroactively. EXERCISED-NOT-REALIZED at a845a8be75.",
        ),
        (
            2,
            2,
            "FAIL",
            "The worker's amended criterion explicitly refers its absent typecheck to CVO; zero files from an unstarted compiler is not a vacuous successful build. CVO's separate L9 source build now passes with 2072 examined files and zero errors. This closes the verification remedy without falsely saying the worker ran the compiler.",
        ),
        (
            2,
            4,
            "FAIL",
            "The worker could not run the typed mutant; node stripping is not a semantic typechecker. The literal worker coverage remains absent. At L9 the retained actual TypeScript compiler catches CVO_R8_TYPE_MUTANT in the real pinned RankedChart, rc2/TS2322 against baseline rc0, with exact snapshot-byte restore. The current falsifier debt is now discharged.",
        ),
        (
            2,
            5,
            "PASS",
            "The real static RankedChart at a845a8be75, driven by fresh actual offline adapter outputs, yields absent/partial/exhaust lengths 328/1554/775 and three different hashes. The actual old component has identical absent/exhaust hashes. Changing only completeness signals switches the rendered state; the unresolved denominator, partial caption and producer series order survive. This is actual component rendering, beyond the worker decision harness, but not a browser effect, full served route or promotion. EXERCISED-NOT-REALIZED.",
        ),
        (
            3,
            5,
            "PASS",
            "The recorded module-attribute matcher invocation fires under actual loosening: 196/196, restores to 183/0 on a 196-figure block. Worker also records a source-predicate mutation and correct-file byte restoration; CVO independently reproduces the object-binding difference and restored identity without shared-source writes. All 47 current API tests pass with sockets denied. The wrong-file cmp is not credited as matcher-file restoration; sibling AC4 and the explicit correct-file cmp cover it. W11-S5's named debt is paid; this does not regrade rf-3.",
        ),
    ]
    for n, (cell, ac, verdict, reason) in enumerate(grade_reasons, 130):
        proof = next(p for p in intake["round_proofs"] if f".TO-AMGT-rg-{cell}." in p)
        row = carrier(
            n,
            f"rg-{cell} AC{ac} {verdict}",
            reason,
            f"Issued round-8 rg-{cell} judgment criterion AC{ac}, including its amendments.",
        )
        row["grades"] = [
            {
                "criterion": f"AMGTrg{cell}-AC{ac}",
                "instance": proof + "@" + intake["pin"],
                "verdict": verdict,
                "reason": reason,
            }
        ]
        row["notes"] = (
            "Grade carrier only; no investigation item dismissed. Worker instances are immutable. FAIL absence grades and completed later verification remedies describe different observations."
        )
        decisions.append(row)
    reason = "rg-2 AC1 still requires a fixture of REAL captured adapter bytes. Its own _provenance and harness disclose that only read_completeness blocks were directly produced; the series arrays are constructed/transcribed. The output therefore cannot satisfy the literal provenance bar even though its decision checks pass. CVO independently supplies real offline adapter responses through the actual component; the runtime repair passes on that different evidence."
    row = carrier(
        136,
        "rg-2 AC1: the fixture provenance does not meet the issued bar",
        reason,
        "A criterion is graded against its full expectation, including fixture provenance, not only printed ratios.",
        G,
        "INERT",
        COO,
    )
    proof = next(p for p in intake["round_proofs"] if ".TO-AMGT-rg-2." in p)
    row["grades"] = [
        {
            "criterion": "AMGTrg2-AC1",
            "instance": proof + "@" + intake["pin"],
            "verdict": "FAIL",
            "reason": reason,
        }
    ]
    row["notes"] = (
        "Literal proof claim corrected here; independent actual adapter-to-component evidence closes the present behavioral verification gap. Keep the historical fixture/proof bytes; no recut merely to launder its provenance. The harness's ordering comparison is also self-comparison, not an independent ordering witness; CVO checks the actual emitted legend order."
    )
    decisions.append(row)
    remedies.append(remediate(row["id"], row, COO, row["notes"], True))
    advances = {
        "v5": {"S22"},
        "v7": {"W12-S1", "S34", "S36", "W11-S5", "S42", "C-S98", "C-S99"},
    }
    row = carrier(
        137,
        "Eight existing remedy clocks advance on their bounded conditions",
        "S22 closes on the corrected causal sentence; S36/S42 on actual 0/46 and 4/15 controls plus D5=0. W12-S1 closes on the issued materialization/identity probe with both controls; S34 on the documented bounded remote-plane drain step. W11-S5 closes on the measured matcher mutant and restoration. C-S98/C-S99 close on actual populated consumer execution. No old remedy text or original ARMED-at-surfacing field changes.",
        "Completed remedies advance only existing monotone clocks; evidence planes do not substitute for publication.",
    )
    row["adjudicates"] = [
        "AMGT_RESAPP-Z-" + s for names in advances.values() for s in sorted(names)
    ]
    row["notes"] = (
        "C-S49 scheduler/IAM, W11-S2 deployment, W11-S1 integration freeze and other older residuals remain with their existing holders. Documented tracking-ref checks do not alone prove current remote reachability; the CVO also measures all nine current remote heads here."
    )
    decisions.append(row)
    row = carrier(
        138,
        "CRO's current consumer/check map satisfies C-S33's deliverable half",
        "The owner map at 27403502ca names 14 source sites, explicitly distinguishes inherited binding and JSON configuration, and identifies five frozen old-bucket checks. CVO independently parses all five: old literal present and zero environ attribute reads. This satisfies the named map deliverable, not applied-state validation. Its estate-wide zero-check-coverage sentence is not established by five frozen scripts; its own 14-site table also has inherited/config exceptions to the all-env-overridable headline.",
        "C-S33 asks CRO for a current executable consumer/check map while preserving historical evidence; C-S49 separately carries scheduler dependencies.",
    )
    row["adjudicates"] = ["AMGT_RESAPP-Z-C-S33"]
    row["notes"] = (
        "Accept and bound the completed map; S12's existing clocks already closed last round and are unchanged. C-S49 remains OPEN/ARMED. No frozen worker scripts or map-owner text is edited; no new estate-wide zero-coverage claim is made."
    )
    decisions.append(row)
    header = f"""# AMGT_RESAPP round 8: CVO L8/L9 review

Packet ROUND8_PACKET.md@790607c9ef; intake {intake["pin"]}; late channel snapshot {supplement["pin"]}. All 46 orders are terminal (43 complete, 3 superseded). All 44 proofs are structurally VALID: 41 prior rc0 results inherited only after exact pinned proof AND task-order byte comparisons, three new checker runs rc0. Working text equivalence normalizes CRLF only. The initial 119 originals contain 24 pending and one new self-disposed owner row S58. Late S61/S62 bring the review to 121 originals: 94 previously reviewed, 27 reviewed here including S58. The packet's 22 and its word 'two' for three typecheck referrals are not adopted.

Basis for disposition: the issued condition, measured mechanism and denominator, discriminating controls, source/evidence pin, and actual remedy holder. A real defect graduates even when its remedy is already executed; its remedy then carries REMEDIATED and, where applicable, DISARMED. Corroboration and superseded counts are dismissed with a specific reason. An implementation or grant gap in an existing cell is not automatically DECOMP_INVALIDATING. The CVO makes no missing-cell finding in this round. Original investigation and worker-proof bytes are immutable.

Six judgment grades: rg-1 AC1 FAIL/AC5 PASS; rg-2 AC2 FAIL/AC4 FAIL/AC5 PASS; rg-3 AC5 PASS. The three FAILs grade the explicitly referred WORKER COVERAGE ABSENCE, accurately disclosed by the orders. Independent CVO verification subsequently fills that source-coverage gap: retained TypeScript 5.9.3, matching package/lock manifests, 2072 files, zero errors; a deliberate RankedChart type error is caught, with exact-byte restore in a disposable pinned source copy. A completed verification remedy does not rewrite who ran which instrument. Separately rg-2 AC1 is literal FAIL because the worker's mixed constructed/captured fixture does not meet the full provenance bar. Its runtime behavior passes on independent actual adapter-to-component evidence.

Independent evidence: 47/47 API tests with sockets blocked; real matcher 183/0 -> 196/196 -> 183/0 on 196 figures, unchanged shared source. Actual populated ThesisTab with the data hook supplied offline adapter outputs renders 196 rows; actual canonical join is 183/183 fiscal, 13/13 header, and unresolved 1/1 with raw value hidden. Actual RankedChart static outputs distinguish absent, partial and exhausted reads, preserving signal, denominator and series order; the actual pre-repair component reproduces the one-pair collision. No browser layout/effects, full served JWT/Print route, or deployed transport is claimed.

The source portal object a845a8be75 is anchored at refs/drains/rg-2-portal. A fresh remote listing contains NINE heads, with nine explicit ancestry rc1 results; it is contained by none. The packet's earlier ten is a different vintage. The gitlink is still e85f6eb84f. Every portal result here is EXERCISED-NOT-REALIZED. No portal checkout, push, gitlink update, deployment or worker teardown was performed; both round-8 worktrees and retained round-7 dependencies remain.

Current-channel method: both canonical roots, each JSON fence independently parsed as array or object, malformed admission fails closed. Initial audit 15 files/298 rows/222 distinct IDs, 20 array and 28 object JSON fences, zero malformed; the plain prose fence is not JSON. Those are corpus grains, not a live-obligation count. S53/S57 still owe the same POSN paired read; S59 does not close the explicitly unfinished half. C-S33's map is accepted within its actual source/check scope; C-S49 remains separate and open. Eight existing remedy clocks advance only their allowed fields.

Messages 22188 and 22203 from MSTR were read as relayed work/scope direction: preserve the no-promote boundary; backfill brief belongs to CRO and current build/issuance decisions to their owners. They do not turn this CVO review into a vendor call, model invocation, worker dispatch or a new PRD bar. The unresolved ownership wording and four carried POSN orders are not inferred away. Only the CTO L10 handoff is sent by this seat.
"""
    write_doc(CHANNEL / "adjudications/ADJUDICATION_v8.md", header, decisions)
    slug = f"""# AMGT_RESAPP round 8 L10 remediation slug

From {SERIAL} to {CTO} only. All 46 project orders terminal, all 44 cumulative proofs structurally VALID, all 121 original investigations dispositioned after 27 CVO reviews including owner self-disposition S58 and late S61/S62. Read ADJUDICATION_v8 and its five evidence artifacts before outcome coverage analysis. This completes the round handoff, not the project or an outcome's REALIZED bar.

Six judgment grades are 3 PASS and 3 FAIL for honestly disclosed worker typecheck absences. The CVO separately fills those gaps at L9 with a real 2072-file typed build and a firing typed mutant. One additional literal FAIL is rg-2 AC1's constructed-series fixture. Actual consumer execution independently verifies the behavior; no recut is requested merely to rewrite proof provenance or repeat completed verification.

{len(remedies)} new remedy rows: {sum(r["closed"] for r in remedies)} REMEDIATED, {sum(not r["closed"] for r in remedies)} OPEN. The open set is W13-S3 (issuer's disclosed read-boundary disposition), S53/S57 (one shared POSN standing read, not two cells), and S61 (one explanation-brief timing correction). Eight existing clocks advance in v5/v7; their mechanism/evidence/remedy/owner remain data-identical. Existing older obligations remain in their own numbered slugs, especially C-S49 scheduler/IAM, W11-S2 deployed integration and W11-S1/S21's frozen portal carrier. Do not infer 63 separate current tasks from immutable ARMED fields or CVO carriers.

CTO: perform the canonical L10 per-outcome DONE_WHEN/artifact coverage analysis and decide any required addendum. Preserve the now-measured populated consumer repairs and loosened-matcher control. The latest relayed no-promote work direction keeps upstream work with its proper owners; it does not weaken outcome bars or publish portal. Source object a845a8be75 has zero of nine freshly listed remote heads and a retained local drain ref; recorded gitlink e85f6eb84f is unchanged. All portal results EXERCISED-NOT-REALIZED. No teardown, broad stage, push or production act occurred.
"""
    write_doc(CHANNEL / "remediations/REMEDIATION_v8.md", slug, remedies)
    for version, names in advances.items():
        path = CHANNEL / "remediations" / f"REMEDIATION_{version}.md"
        text = path.read_text(encoding="utf-8")
        rr = records(text)
        for r in rr:
            if r["id"] not in {"AMGT_RESAPP-Z-" + n for n in names}:
                continue
            assert not r["closed"], r["id"]
            r["closed"] = True
            r["remediation"]["state"] = "REMEDIATED"
            if r.get("disarm", {}).get("state") == "ARMED":
                r["disarm"].update(state="DISARMED", at=utc)
        blocks = list(re.finditer(r"```json\s*(.*?)```", text, re.S))
        assert len(blocks) == 1
        b = blocks[0]
        path.write_text(
            text[: b.start()]
            + "```json\n"
            + json.dumps(rr, indent=2, ensure_ascii=True)
            + "\n```"
            + text[b.end() :],
            encoding="utf-8",
        )
    report = {
        "utc": utc,
        "intake_pin": intake["pin"],
        "supplement_pin": supplement["pin"],
        "originals": 121,
        "reviewed_originals": ["AMGT_RESAPP-Z-" + d[0] for d in DECISIONS],
        "adjudication_rows": len(decisions),
        "new_remedies": len(remedies),
        "open_remedies": [r["id"] for r in remedies if not r["closed"]],
        "clock_advances": {k: sorted(v) for k, v in advances.items()},
        "grades": [g for r in decisions for g in r.get("grades", [])],
    }
    (HOME / "AMGT_RESAPP_ROUND8_CVO_COMPILE_20260913_Z.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                k: v
                for k, v in report.items()
                if k not in ["grades", "reviewed_originals"]
            }
        )
    )


if __name__ == "__main__":
    main()
