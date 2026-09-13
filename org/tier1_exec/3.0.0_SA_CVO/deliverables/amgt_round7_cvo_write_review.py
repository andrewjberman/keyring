"""Write the exact round-7 CVO decisions; never edit original investigations."""

import datetime
import json
import re
import subprocess
from amgt_round7_cvo_supplement import rows, ROOT, PROJECT

SERIAL = "3.0.0_SA_CVO~Z"
COO = "2.0.0_SA_COO~ZZZ"
CTO = "1.0.0_SA_CTO~Z"
CRO = "4.0.0_SA_CRO~Z"
CHANNEL = ROOT / PROJECT / "surprise-channel"
PREFIX = "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
EVIDENCE = [
    PREFIX + "AMGT_RESAPP_ROUND7_CVO_" + s + "_20260912_Z.json"
    for s in ["INTAKE", "EVIDENCE", "SUPPLEMENT", "PORTAL"]
]
# suffix, disposition, holder, closed, finding, bounded remedy
DECISIONS = [
    (
        "S28",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "The reported observer reads and matching commit/reflog dates establish a visibility-versus-stamp distinction. They do not independently establish that every Git timestamp is taken at process start or prove a safe-commit defect; the row itself falsifies date pinning by that wrapper.",
        "Retain source hashes and observed visibility windows. No new compiler or timing repair is justified by this observation.",
    ),
    (
        "S29",
        "DISMISSED_WITH_REASON",
        CTO,
        False,
        "Additional evidence for existing S6: eight no-hash records in the reported 14-record/five-project census; four IRPT version matches, with no measured byte drift. evaluate still uses version equality when half_hash is absent. Current AMGT lane records are current and win newest-record selection; a version decrement alone need not activate an older base record.",
        "Carry the evidence under S6; do not duplicate its remedy, silently certify older records, or change another project. Existing fallback repair remains open with its gate owner and the required scope decision.",
    ),
    (
        "S30",
        "DISMISSED_WITH_REASON",
        CRO,
        False,
        "Accept the owner disarm of S18 only. Independent prd-signoff status is ADMITTED, both lane halves current, and all 43 orders terminal. The earlier stale-brief blocking condition is absent. This does not repair the separate S6 version fallback.",
        "Record current admission and preserve the historical stale observation. No new work item follows from recovered admission.",
    ),
    (
        "S31",
        "DISMISSED_WITH_REASON",
        CRO,
        False,
        "Accept the named owner executable-consumer map as the S12 recovery: five remaining DEF matches are frozen worker checks, while the live defaults and the separately missed seekingalpha CONFIG value were corrected at the cited commits. A DEF-only census would not have justified this decision; the owner supplies the missing CONFIG repair.",
        "Advance S12 clocks on its existing remediation row. Preserve historical proofs and keep scheduler/IAM obligation C-S49 separate; no claim that every historical occurrence should disappear.",
    ),
    (
        "W12-S1",
        "GRADUATED",
        COO,
        False,
        "An unmaterialized portal directory lets Git walk up and successfully answer from the superproject. Later materialization in this worker checkout does not fix the next spawn face. This is distinct from W11-S1, which concerns the recorded gitlink.",
        "At the existing spawn/checkout step require a materialized portal or a top-level identity probe that distinguishes the nested repository from the parent. Show an empty-directory negative and genuine portal positive; no new cell is inferred.",
    ),
    (
        "W12-S2",
        "GRADUATED",
        COO,
        True,
        "The worker-only object preservation hazard is discharged by the issuer fetch in S32. The shared portal store resolves 83cc87f2 and its c67281460a parent, with local anchors and a missing-object negative control. Local object presence does not publish the object.",
        "Accept the executed local preservation remedy only. Keep remote reachability and frozen gitlink integration under S34, W11-S1 and S21.",
    ),
    (
        "W12-S3",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "Missing local dependencies were disclosed and overcome using matching package and lockfile manifests and already-installed dependencies. The worker then examined 2069 compiler files and caught an error; this is not a zero-file build. The CVO also used the retained local dependency set without installation.",
        "Retain dependency provenance and the source denominator. No outstanding repair or authorization to fetch packages follows from this resolved environment observation.",
    ),
    (
        "W12-S4",
        "GRADUATED",
        COO,
        True,
        "The unsafe only-private-object instruction is retained as issued evidence. S32 subsequently copied the object to the shared portal store before teardown; CVO independently resolves it. This closes immediate preservation, not the original instruction grant or a remote publication.",
        "Record executed local preservation. Future pointer decisions still require their existing grant and remote-plane evidence; no grant is retroactively inferred from the recovery.",
    ),
    (
        "S32",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "This is corroborating recovery evidence for W12-S2 and W12-S4, accepted within that local-object scope. It neither establishes remote reachability nor authorizes the frozen portal integration.",
        "Close those two original remedies once. Do not mint a second task for the same completed fetch.",
    ),
    (
        "S33",
        "GRADUATED",
        COO,
        True,
        "The shared gitlink could serialize otherwise disjoint file work. All five rf-1 through rf-5 drains report no portal pointer change and the project queue is now zero of 43 open, satisfying original condition (a). Independently 83cc87f2 descends c67281460a; they are not divergent siblings.",
        "Accept the completed no-gitlink-change drain branch of the original condition. Do not force a pointer merge to close a hazard whose alternative condition already held.",
    ),
    (
        "S34",
        "GRADUATED",
        COO,
        False,
        "Local fetch repaired object preservation, and the attempted pointer was backed out before the held superproject push. No published dangling-pointer incident is established. The named durable remote-reachability check in the drain procedure remains unproved.",
        "Add or execute the named remote-plane reachability step in the existing drain procedure before a future authorized pointer publication. A documented bounded step suffices; this does not authorize new approval machinery or portal promotion.",
    ),
    (
        "W11-S1",
        "GRADUATED",
        COO,
        False,
        "The AC4 portal evidence is at a separately preserved object while the superproject still records e85f6eb84f, which contains zero SecurityAnalysis files. The original remedy concerns that recorded carrier, not the empty-directory spawn defect the packet substitutes for it.",
        "Keep the recorded-gitlink/integration decision with the existing owner under the freeze. Cite the exercised portal object explicitly until an authorized carrier update; do not treat materializing a checkout as disarming this row.",
    ),
    (
        "S35",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "This states the existing grant and publication fence behind W11-S1. Source-object availability does not establish an integrated or served page. It adds context, not a distinct repair mechanism.",
        "Retain the context with W11-S1 and S21 without duplicating the portal decision.",
    ),
    (
        "S36",
        "GRADUATED",
        CTO,
        False,
        "CVO reproduced six ACTIVE results from to-check against six literal complete record faces and zero actual open orders. _extract_tag starts at the bare inline <status> in completion instructions and consumes through the later closing tag, so _classify_status grades prose.",
        "Repair the existing status parser in place to select the record element, with this six-order positive case and a genuinely active negative control. Preserve the authoritative 0/43 census; no worker recut is required for this tool defect.",
    ),
    (
        "S37",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "Issuer evidence corroborates W11-S2 grant omissions and their amendment. Package and source-map paths were added at 545ee5ee82. The separately required artifact upload was not executed.",
        "Use W11-S2 for the remaining obligation rather than creating a duplicate grant-repair item.",
    ),
    (
        "S38",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "This corroborates the rf-3 criterion defects. Corrected invocation gives 13 headers and 183 fiscal rows. The original spaced key gave 0/0; the old scope matcher on the correct key gave 13/0. Their fiscal-zero symptom agrees, but the complete failure signatures are not identical.",
        "Retain the bounded instrument lesson with W11-S4 and W11-S5. Do not broaden the measured failure signature or invent a new governance gate.",
    ),
    (
        "S39",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "This distinguishes a repair check from a regression guard and supports W11-S5. Counting 183 selected rows out of 196 establishes present selectivity; it does not execute the stipulated loosened-matcher mutant.",
        "Retain this distinction in the W11-S5 decision; no duplicate work item.",
    ),
    (
        "W11-S2",
        "GRADUATED",
        COO,
        False,
        "The amended grant includes the package entrypoint and source map, and comp-iam now names three adapter sites. The worker explicitly did not build/upload the artifact or deploy. The original disarm condition includes artifact upload, so the full condition remains unmet.",
        "Finish the existing packaging/artifact and served-route obligation under the applicable grants and deploy contract. Preserve the source-plane repair; CVO neither uploads an artifact nor authorizes an AWS act through this row.",
    ),
    (
        "W11-S3",
        "GRADUATED",
        COO,
        True,
        "rf-2 AC2 literally FAILS: its route-bearing .tf is HEAD in the printed tool vocabulary, not CONFIG or DEF; the sole CONFIG hit is the source map, not a route_key declaration. Sixteen hits over a nonzero infra denominator and the actual eleven routes demonstrate the intended source existence.",
        "The owed issuer referral is completed by this L9 literal FAIL and explicit instrument-versus-world distinction. Use an executable declaration predicate in a future cut; do not edit this terminal criterion, relocate valid Terraform, or relabel the compiler to manufacture PASS.",
    ),
    (
        "W11-S4",
        "GRADUATED",
        COO,
        True,
        "The exact security key was amended at 5dc02a83d5 and rerun. CVO independently obtains HEADER=13 FISCAL=183 TOTAL=196 from BABA_US_Equity and 0/0 from the old spaced key. This meets the repaired nonzero artifact condition.",
        "Accept the executed criterion repair and disarm this invocation defect. Keep the distinct consumer check-join and W11-S5 mutation obligations open.",
    ),
    (
        "W11-S5",
        "GRADUATED",
        COO,
        False,
        "The amended direct-model control measures POSITIVE=183 WRONG_SCOPE=0, fixing the old absent model_block-key vacuity. However, the original disarm condition explicitly requires a deliberately loosened matcher to make the wrong-scope arm nonzero. Neither proof nor CVO run executes that mutant. S40 overstates closure.",
        "Retain ARMED standing pending the named discriminating matcher mutation in an authorized isolated working copy, followed by exact-byte restoration. A scope-token mutation and an import sentinel are different controls. No new retrospective rule is being added.",
    ),
    (
        "S40",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "Accept its disarm of W11-S4 and reject its disarm of W11-S5 for the unexecuted named condition. Also correct the packet association: W12-S1 is the empty-checkout hazard; W11-S1 is the recorded-gitlink mismatch.",
        "The citing CVO decisions are authoritative for this review. Preserve the issuer row as historical evidence, without converting its overstated closure into another duplicate repair.",
    ),
    (
        "S41",
        "DISMISSED_WITH_REASON",
        COO,
        False,
        "Issuer evidence corroborates W11-S6 and a bounded six-order invocation sweep. The corrected price predicate names the underscore key, exact mnemonic, fiscal scope and a positive denominator. A present-world sweep does not prove every instrument can fail.",
        "Retain the amendment and bounded lesson with W11-S6. Do not rewrite quoted historical commands or infer a general clean bill from the sweep.",
    ),
    (
        "W11-S6",
        "GRADUATED",
        COO,
        True,
        "The f5461c6884 amendment removes both the empty-key vacuity and the broad PX_LAST substring population. Independent BABA reads find 183 fiscal figures, exactly ten fiscal PX_LAST values, all corrected and carrying provenance; the unresolved arm retains raw value with explicit refusal.",
        "Accept the executed criterion repair and disarm this invocation defect. The portal refusal join is separately broken and does not undo the backend overlay repair.",
    ),
    (
        "W11-S7",
        "GRADUATED",
        COO,
        True,
        "rf-5 AC2 literally FAILS because CODE is not a comp-find band. Nine hits are five SURFACED plus four TEST in the bounded adapter scope; independent execution establishes the actual retry behavior. This is a criterion vocabulary error, not missing retry code.",
        "Complete the requested adjudication with literal FAIL and the substantive PASS recorded separately. Future cuts should ask for the source behavior with the tool actual vocabulary; do not mutate this proof or source layout to satisfy an imaginary band.",
    ),
    (
        "S42",
        "GRADUATED",
        CTO,
        False,
        "directives-check.open_tos consumes to-check ACTIVE/PENDING/BLOCKED/UNKNOWN totals, propagating the same six false ACTIVE counts into D5. The earlier D4-versus-one-POSN comparison used different domains and is retracted, not promoted into a second defect.",
        "With S36, repair the existing producer/consumer count contract in place and verify D5 against the same 43-order domain. Do not open work on D4 based on the withdrawn comparison.",
    ),
    (
        "S43",
        "DISMISSED_WITH_REASON",
        CTO,
        False,
        "Accept the S16 present-state disarm. CVO independently reads live portal refs/heads/DEV at 5b959f63ca5e51214fe1e605b04b82b2bbf60ef4. This does not determine when DEV advanced or prove the original observation false. e6057f26 remains a separately local Lead Panel object.",
        "Advance S16 clocks only. Keep S21, remote durability and portal promotion decisions open; no fetch, rebase or publication follows from the read.",
    ),
]

GRADE_REASONS = {
    1: (
        "PASS",
        "Producer repair passes in the source and controlled-execution scope: the actual chatter and price producer paths emit crossed identities, all four resolutions preserve requested=served, and two invalid-domain controls refuse. Source availability is PRODUCER_DECLARED, not a dated live DynamoDB landing. No browser rank is invented. This closes the implemented producer remedy but does not establish deployed producer freshness or FWD-15 realization.",
    ),
    2: (
        "FAIL",
        "The full AC5 explicitly owns SERVED-plane exercise. Eleven Terraform routes, an entrypoint and source-map binding exist; fake-header tests and three named comp-iam sites improve source coverage. No uploaded package, applied mount, edge-JWT/origin-isolation exercise or served Print path is established. comp-iam still reports three unresolved-resource UNGRANTED sites and does not census transitive watchlist writes or the new resource-style batch call. The source fix is credited; this is neither an outage claim nor permission to deploy.",
    ),
    3: (
        "FAIL",
        "The API scope repair passes: 13 headers, 183 fiscal rows and 196 checks, with a wrong-scope zero control. The full cell also requires the populated real consumer and its checks. Executing the actual pinned ThesisTab checkFor against the actual bundle matches 13/13 header checks but 0/183 fiscal checks because fyYEAR:MNEMONIC differs from fiscal_year_line_item:MNEMONIC:YEAR. W11-S5 also lacks its named matcher mutant. Passing backend counts do not meet the whole cell.",
    ),
    4: (
        "FAIL",
        "The shared overlay repair passes locally for ten corrected fiscal prices and a preserved unresolved/refusal arm. The full cell requires both arms through the real populated Thesis route. Its actual checkFor drops the unresolved fiscal REFUSE, and ProvenanceLine displays a raw value when verdict is undefined. Thus a concrete downstream defect remains in addition to the missing full route-render proof. No historical model artifact was rewritten.",
    ),
    5: (
        "PASS",
        "The bounded adapter repair passes independently: processed, genuine absence, mixed processed/unprocessed and exhausted cases retain distinct completeness and unresolved denominators. A 105-key control returns all 105 points in batches 100,99,5. Worker behavior-mutant failures are attributed separately from CVO calls. The old adapter omission is repaired; the separately measured portal consumer still ignores the new fields, so this is not an end-to-end outcome PASS.",
    ),
    6: (
        "PASS",
        "The named INERT display edit passes at portal 83cc87f2: 18 files, ten punctuation occurrences reduced to zero, and a six-file diff containing only the named display substitutions. The worker compiler sees 2069 source files and catches its type-error control with byte-identical restoration. The CVO independently reads both objects and the complete diff. This is an object-scoped hygiene grade, not publication at the recorded e85f6eb84f gitlink.",
    ),
}


def write_doc(path, header, values):
    if path.exists():
        raise RuntimeError("Refusing overwrite " + str(path))
    path.write_text(
        header
        + "\n\n```json\n"
        + json.dumps(values, indent=2, ensure_ascii=True)
        + "\n```\n",
        encoding="utf-8",
    )


def main():
    intake = json.loads((ROOT / EVIDENCE[0]).read_text())
    audit = json.loads((ROOT / EVIDENCE[1]).read_text())
    portal = json.loads((ROOT / EVIDENCE[3]).read_text())
    originals = {r["id"]: r for r in intake["pending"]}
    assert set(originals) == {"AMGT_RESAPP-Z-" + r[0] for r in DECISIONS}
    assert intake["original_count"] == 92 and intake["orders"]["AMGT_RESAPP"] == [
        [],
        43,
        "",
    ]
    assert len(intake["proof_checks"]) == 41 and all(
        x["rc"] == 0 for x in intake["proof_checks"].values()
    )
    assert audit["tests"]["rc"] == 0 and portal["chart_absent_equals_exhaust"]
    utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    decisions = []
    remedies = []

    def carrier(
        n, title, world, bar, disp="DISMISSED_WITH_REASON", standing="INERT", owner=COO
    ):
        r = {
            "id": f"AMGT_RESAPP-Z-C-S{n}",
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "surfaced_by": SERIAL,
            "surfaced_at": utc,
            "one_line": title,
            "class": "OBSERVATION",
            "hazard_standing": standing,
            "grounding": {"status": "GROUNDED", "evidence": EVIDENCE},
            "disposition": disp,
            "spec_asserts": bar,
            "world_is": world,
        }
        if standing == "ARMED":
            r["disarm_owner"] = owner
        if disp == "DISMISSED_WITH_REASON":
            r["dismissal_reason"] = world
        return r

    def remediate(rid, row, owner, remedy, closed):
        r = {
            "id": rid,
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "class": "OBSERVATION",
            "hazard_standing": row["hazard_standing"],
            "mechanism": row["world_is"],
            "evidence": row["grounding"]["evidence"],
            "remedy": remedy,
            "owner": owner,
            "round": "v7",
            "remediation": {
                "state": "REMEDIATED" if closed else "OPEN",
                "owner": owner,
                "round": "v7",
            },
            "closed": closed,
        }
        if r["hazard_standing"] == "ARMED":
            r["disarm"] = {
                "state": "DISARMED" if closed else "ARMED",
                "owner": owner,
                "at": utc if closed else None,
            }
        return r

    for n, (suffix, disp, owner, closed, world, remedy) in enumerate(DECISIONS, 65):
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
        row["grounding"] = {
            "status": "GROUNDED",
            "evidence": EVIDENCE
            + [PROJECT + "/surprise-channel/investigations/INVESTIGATION_v1.md#" + rid],
        }
        decisions.append(row)
        if disp == "GRADUATED":
            remedies.append(remediate(rid, row, owner, remedy, closed))
    for cell, (verdict, reason) in GRADE_REASONS.items():
        ac = 4 if cell == 6 else 5
        proof = next(p for p in intake["round_proofs"] if f".TO-AMGT-rf-{cell}." in p)
        row = carrier(
            91 + cell,
            f"rf-{cell} AC{ac} {verdict}",
            reason,
            f"The full issued rf-{cell} cell and judgment criterion AC{ac}.",
        )
        row["dismissal_reason"] = "Grade carrier only; no investigation item dismissed."
        row["grades"] = [
            {
                "criterion": f"AMGTrf{cell}-AC{ac}",
                "instance": proof + "@" + intake["pin"],
                "verdict": verdict,
                "reason": reason,
            }
        ]
        if cell in (2, 5):
            suffix = "W11-S3" if cell == 2 else "W11-S7"
            literal = next(r[4] for r in DECISIONS if r[0] == suffix)
            row["grades"].append(
                {
                    "criterion": f"AMGTrf{cell}-AC2",
                    "instance": proof + "@" + intake["pin"],
                    "verdict": "FAIL",
                    "reason": literal,
                }
            )
        row["notes"] = (
            "Judgment belongs to CVO. Proof instance stays structurally VALID and immutable; criterion prefix maps to its exact issued task order."
        )
        decisions.append(row)
    own = [
        (
            98,
            "The chart suppresses the adapter incomplete-read distinction",
            "The actual RankedChart at 83cc87f2 produces byte-identical static HTML for the actual adapter absent and retry-exhausted control payloads. It reads points and point_count but never read_completeness or unresolved_point_count; both payloads describe zero landed days. The backend now preserves the distinction, but the consumer loses it. This is an exercised static component boundary, not a measured production throttle or browser layout.",
            "A chart must distinguish genuinely absent history from a read that has not completed.",
            "In the existing chart/client cell carry and render or refuse incomplete reads with the unresolved denominator. Exercise the actual component with absent, partial and exhausted adapter payloads and require distinct output. Preserve producer ordering and the portal freeze.",
        ),
        (
            99,
            "The Thesis consumer drops fiscal check verdicts at its identity join",
            "At 83cc87f2 the actual extracted checkFor expects fy2025:PX_LAST while the actual adapter emits fiscal_year_line_item:PX_LAST:2025. It matches 13/13 header figures and 0/183 fiscal figures. The unresolved control fiscal REFUSE also matches 0/1. A deliberately matching legacy-shaped key returns REFUSE and the empty-check control returns undefined, demonstrating that the extracted function executes. ProvenanceLine receives undefined and its source therefore displays the raw value without the refusal marker. Full DOM and deployed transport were not exercised.",
            "The rehomed fiscal figures must preserve their check-face verdict and unresolved refusal at the actual consumer.",
            "Repair the existing portal consumer join to use the canonical figure identity shared with the check-face producer. Exercise the populated Thesis component with all 183 fiscal rows and the unresolved-price control; require the REFUSE presentation to survive. Do not rewrite canonical artifact IDs to satisfy the stale UI pattern.",
        ),
    ]
    for n, title, world, bar, remedy in own:
        row = carrier(n, title, world, bar, "GRADUATED", "ARMED", COO)
        row["notes"] = remedy
        decisions.append(row)
        remedies.append(remediate(row["id"], row, COO, remedy, False))
    advances = {"v5": {"S12", "S16"}, "v6": {"W10-S2", "W10-S4", "C-S63"}}
    closure = carrier(
        100,
        "Five existing remedy clocks advance on measured recovery",
        "S12 closes on its owner executable/config map; S16 closes on the independent live DEV read. W10-S2 closes the source producer repair, W10-S4 the ten-character hygiene edit, and C-S63 the bounded adapter-read repair. C-S61/C-S62 remain open because the populated consumer loses fiscal checks; W10-S3 and S27 remain open because served integration and full grant analysis are incomplete. The new chart defect is C-S98, not a silent reversal of the repaired adapter.",
        "A completed remedy advances its existing row clocks once; broader unperformed conditions stay open.",
    )
    closure["adjudicates"] = [
        "AMGT_RESAPP-Z-" + x for names in advances.values() for x in sorted(names)
    ]
    closure["notes"] = (
        "Only remediation.state, disarm.state/at and closed change on the existing rows. All evidence, mechanism, owner and remedy text remain byte-equal as parsed data. Historical adjudications and grade pins remain intact."
    )
    decisions.append(closure)
    header = """# AMGT_RESAPP round 7: CVO L8 compilation and L9 adjudication

Packet ROUND7_PACKET.md@6a50ce1832, last drain a8659e8baa, source intake d359728e66b294dc77149c1a4749237606638b01. The source intake contains 92 original investigation items: 65 already dispositioned and 27 pending, including late S43. The packet's earlier 91/26 is a time-local adjudication census, not a count of live hazards. C-S65 through C-S91 dispose those 27; C-S92 through C-S97 grade six judgments and two referred mechanical criteria; C-S98/C-S99 add two composed consumer findings; C-S100 records five existing remedy-clock advances. No original investigation bytes change.

Judgments: rf-1 AC5 PASS; rf-2 AC5 FAIL; rf-3 AC5 FAIL; rf-4 AC5 FAIL; rf-5 AC5 PASS; rf-6 AC4 PASS. Separately rf-2 AC2 and rf-5 AC2 are literal FAIL for issued band predicates. These do not erase the actual routes or retry implementation. Six structurally VALID instances are not six substantive passes. All 41 cumulative proofs validate structurally with their actual criterion IDs; all 43 project orders are terminal. POSN has four open of 15, and the nonexistent-project control zero of zero. L10 is available for this round without declaring the project complete.

Basis: the issued condition, the actual mechanism and denominator, a discriminating control, the evidence plane and pin, and the permitted remedy holder. Severity and disposition are separate. Existing-cell grant or implementation gaps are not automatically DECOMP_INVALIDATING. Duplicate corroboration is dismissed with its reason; actual defects graduate even when their owner repaired them inside the round. Completed remedies carry REMEDIATED and, where applicable, DISARMED clocks. Immutable original ARMED fields and a search for the word DISARM are both inadequate current-state censuses.

Independent evidence: 107 selected tests pass with Python socket connections denied throughout; 24 source files match the intake pin and remain unchanged. Actual BABA reads return 13 headers, 183 fiscal rows and 196 checks. Ten fiscal prices are corrected with provenance; the unresolved control retains refusal. Four batch-response shapes and a 105-key mixed case validate the repaired adapter. Actual pinned RankedChart static rendering nevertheless collapses absence and exhaustion to identical HTML. The actual extracted Thesis checkFor matches zero of 183 fiscal checks, including zero of one unresolved control, while matching 13 headers and a positive legacy-key control. These concrete composition defects explain why backend greens do not close the populated-consumer obligations.

The issuer amendments repair invocation keys, missing positive denominators and granted paths; they do not lower the original semantic bar. W11-S5 is an exception to the claimed disarms: its specifically named loosened-matcher control is unexecuted, so S40's disarm is not accepted. The old spaced-key failure was 0/0, whereas the wrong scope on the correct key was 13/0; calling their entire signatures identical loses a discriminating fact. The packet confuses W11-S1's recorded pointer with W12-S1's empty checkout; both original conditions are preserved here. Newer criterion rules are not applied retroactively to this cut.

The six false ACTIVE orders are reproduced at their actual parser: the inline <status> instruction starts a multiline capture that swallows prose before the record face. directives-check propagates the same count. These are existing CTO tool repairs, not six reopened worker orders. comp-iam now sees three adapter sites but labels their resources unresolved/UNGRANTED and remains blind to additional call shapes; source enumeration is not permission verification.

Portal evidence is object-scoped: e85f6eb84f has no SecurityAnalysis files; c67281460a and 83cc87f2 have 18. The latter descends the former and removes exactly ten non-ASCII display characters in six files. A live remote read corroborates DEV=5b959f63ca, disarming S16's present base condition without rewriting its history; S21's separate local-object integration remains open. No portal pointer, deployment, remote publication or task order is changed by this review. Both retained worker worktrees remain in place. COO messages 22017/22019 provide standing and count caveats; they do not supply a new Go.

The repository sendguard refused the attempted COO ACK, so none was delivered or bypassed. The sole completed-round handoff is REMEDIATION_v7 to CTO. The prior nine carried obligations are not silently retired: their unperformed conditions remain with their existing holders. A source repair does not establish APPLIED, served, browser layout or REALIZED evidence.
""".replace("COO messages 22017/22019", "CTO message 22017 and COO message 22019")
    write_doc(CHANNEL / "adjudications/ADJUDICATION_v7.md", header, decisions)
    remhead = f"""# AMGT_RESAPP round 7 L10 remediation slug

From {SERIAL} to {CTO} only. Vintage is this file's commit. Read ADJUDICATION_v7 and its four independent evidence artifacts before outcome coverage analysis. All 43 task orders are terminal, 41 cumulative proofs structurally VALID, and all 92 original investigations have CVO dispositions after the 27 decisions in this round. Six judgment grades: three scoped PASS and three whole-criterion FAIL; two additional literal mechanical FAIL grades are retained. This closes the round handoff, not FWD-15 or the project.

There are {len(remedies)} new remedy rows: {sum(r["closed"] for r in remedies)} executed and REMEDIATED, {sum(not r["closed"] for r in remedies)} OPEN. IDs are not duplicated from prior numbered slugs. Five prior rows advance their own clocks only: v5 S12/S16; v6 W10-S2/W10-S4/C-S63. Their historical text stays fixed. Other older open clocks are carried, not reconstructed from the immutable investigation standing.

The next coverage read must preserve the repaired producer, fiscal scope, shared overlay and batch reader while addressing actual composition: zero of 183 fiscal check joins and identical chart output for absent versus incomplete reads. The full served mount/identity/package/Print path remains unproved. The explicitly requested W11-S5 matcher mutant is still owed. These are existing integration, consumer and verification obligations; none requires inventing a new project cell merely because its grant or exercise is missing.

CTO: perform the L10 coverage analysis/addendum; the COO then chooses the next authorized cut in one issuance. S36/S42 belong to existing status-count tools in place. S6's general fallback and C-S49's scheduler/IAM scope remain with the existing holders and decisions. W11-S3/W11-S7 are closed as completed adjudication referrals, with their literal FAIL recorded; future invocation repair does not justify rewriting the terminal order or the tool vocabulary. The portal integration/promotion freeze stands. No worker receives this slug directly, no AWS act is requested of CVO, and no outcome is called REALIZED. Retained worker worktrees have not been removed.
"""
    write_doc(CHANNEL / "remediations/REMEDIATION_v7.md", remhead, remedies)
    for version, names in advances.items():
        path = CHANNEL / "remediations" / f"REMEDIATION_{version}.md"
        text = path.read_text(encoding="utf-8")
        records = rows(path)
        for record in records:
            if record["id"] not in {"AMGT_RESAPP-Z-" + x for x in names}:
                continue
            assert record["closed"] is False, record["id"]
            record["closed"] = True
            record["remediation"]["state"] = "REMEDIATED"
            if record.get("disarm", {}).get("state") == "ARMED":
                record["disarm"].update(state="DISARMED", at=utc)
        blocks = list(re.finditer(r"```json\s*(.*?)```", text, re.S))
        assert len(blocks) == 1
        block = blocks[0]
        path.write_text(
            text[: block.start()]
            + "```json\n"
            + json.dumps(records, indent=2, ensure_ascii=True)
            + "\n```"
            + text[block.end() :],
            encoding="utf-8",
        )
    for stage in ["L8", "L9"]:
        subprocess.run(
            [
                "python",
                ".tools/prd-stamp.py",
                "stamp",
                PROJECT + "/prd/AMGT_RESAPP_PRD.md",
                "--stage",
                stage,
                "--round",
                "7",
                "--note",
                "Round-7 intake: 92 originals, 27 decisions; 43 terminal orders and 41 VALID proofs. ADJUDICATION_v7 and evidence carry the measurement.",
            ],
            cwd=ROOT,
            check=True,
        )
    print(
        json.dumps(
            {
                "decisions": len(decisions),
                "new_remedies": len(remedies),
                "open": sum(not r["closed"] for r in remedies),
                "closed": sum(r["closed"] for r in remedies),
                "clock_advances": advances,
            },
            default=list,
        )
    )


if __name__ == "__main__":
    main()
