"""Materialize this seat's reviewed round-10 dispositions and single slug."""

import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
P = ROOT / "org/missions/D5/AMGT/AMGT_RESAPP"
C = P / "surprise-channel"
AUDIT = "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND10_CVO_AUDIT_20260915_W.json"
VERIFY = "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND10_CVO_VERIFY_20260915_W.json"
PROSE = "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND10_CVO_PROSE_20260915_W.json"
BOUNDARY = "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND10_CVO_BOUNDARY_20260915_W.txt"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SEAT = "3.0.0_SA_CVO~W"

# disposition, finding, remedy (None means no remedy row), remedy complete, owner
REVIEWS = {
    "S88": (
        "GRADUATED",
        "The deleted-table producer failure was real at the measured 09-14 log vintage. The repaired declaration/policy, QA result (10 rows), saved deployed-adapter response (10 rows) and owner disarm S98 support recovery of that cause. The organic scheduled fire remains unobserved at this review; recovery does not prove article inflow (S96).",
        "Accept the completed producer repair and S98 disarm; retain the QA versus scheduled-run distinction in L10.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "S89": (
        "GRADUATED",
        "The uncommitted two-line edit was the migration guard, not discardable residue. HEAD now contains the harvest bucket name at ea6cd450fa, drained 5c95c00268, with no working-tree difference. Owner S99 arrived after the packet and disarms it. The mount plan mentions the bucket once in refresh output but proposes zero bucket changes.",
        "Accept the in-lane committed convergence and owner S99 disarm. Do not restore the pre-migration declaration.",
        True,
        "4.0.0_SA_CRO~Z",
    ),
    "S90": (
        "DISMISSED_WITH_REASON",
        "The round-10 decomposition section 18b prints the three plane denominators and describes the union/owner-mention grain. This fulfills S68; the historical count is not the present count.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S91": (
        "DISMISSED_WITH_REASON",
        "The issuer supplies the requested citing resolution: 126+3+5=134 and 126+4+6=136 are two vintages of a growing union. The prior round-9 CVO record independently agrees. No lost-row claim follows.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S92": (
        "GRADUATED",
        "A single route page was mistaken for the whole set. The amended order uses measured before N, subset preservation and +11. Independent saved-set comparison gives 85 before, 96 after, exactly 11 added and zero lost; the repair preserves the substantive bar.",
        "Accept the amended route census and the completed 85-to-96 set transition; retain pagination and set-difference checks in future cuts.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "S93": (
        "DISMISSED_WITH_REASON",
        "This is a comp-tool rail finding, outside AMGT implementation. Its carrier is this investigation record and the prior rail-owner records W2-S3/W2-S4 named by it. The observed shell classification cannot be generalized to all shell syntax from this sample. No AMGT cell is warranted; retain it for the existing rail owner through the CTO read.",
        None,
        False,
        "1.0.0_SA_CTO~Z",
    ),
    "W16-S1": (
        "DISMISSED_WITH_REASON",
        "Six input states are required, not six distinct output hashes: the same order explicitly requires the two failure views to match. The current replay yields six states and FIVE distinct hashes, with the two failure outputs equal; the worker denominator saying four distinct is an arithmetic error. The meaningful error/empty, loading and populated controls pass.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S94": (
        "DISMISSED_WITH_REASON",
        "Accept the saved browser observations within their disclosed transport-stubbed, local-adapter boundary. They prove populated rendering, distinct error/empty states and a failed ranked-row identity seam. They do not prove the AC2 payload was rendered, FWD9 prose adjacency, the live edge, or a person session. The two judgment grades below govern.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S95": (
        "GRADUATED",
        "Both saved ranking payloads contain 10 ticker rows and zero security_key fields. RankedList passes row.ticker; BABA US yields zero figures, while BABA_US_Equity yields 13 header and 183 fiscal figures. The screenshot and saved responses corroborate the seam. This is an existing identity/Lead Panel cell defect, not evidence that a new outcome is needed.",
        "Recut the existing identity-to-navigation seam. A ranked-row click must resolve the same canonical security and figure set as the direct-key control; retain an unresolved-name negative control. The CTO reads the remedy and COO chooses its implementation home.",
        False,
        "2.0.0_SA_COO~W",
    ),
    "W17-S1": (
        "GRADUATED",
        "The patch was absent from the issued worktree because it was untracked, although the order named it. The worker used the exact named patch from the shared tree and checked its pre/post image hashes; the resulting two-line change is now committed. This specific repair is established, while future issuance must carry readable dependencies at its pin.",
        "Accept this content-verified repair. Future cuts must commit named read dependencies before fanout or explicitly provide their authorized reachable location.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "W17-S2": (
        "GRADUATED",
        "The root could not evaluate without the artifact, and a whole-root producer plan counted the mount. The issuer amendment supplied the artifact prerequisite and a targeted producer plan, followed by the whole-root mount plan. Saved logs show 0/4/0 then 19/0/0; S97 records the owner disarm.",
        "Accept the executed amendment and disarm. Preserve the root evaluation ordering and targeted-versus-whole-root distinction.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "W17-S3": (
        "GRADUATED",
        "The five-package enumeration omitted three reached modules. The issuer replaced it with a closure before the final upload/mount. Independent source AST closure reproduces 23 seeds, 30 final entries, 20 required modules, zero missing; the seed-only control misses exactly the three reported modules. Saved upload logs carry the 75917-byte artifact.",
        "Accept the amended transitive-closure repair and W17-S6 evidence of its execution; retain function-scope imports and package initializers in the closure.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "W17-S4": (
        "GRADUATED",
        "The literal AC2 status-line expectation is not met after the predecessor committed the changes. The history and source counts support the consolidation itself. A valid proof schema and a plausible replacement read do not make the named invocation emit the required status lines; the mismatch remains in the issued face.",
        "At the next issuer cut, make the criterion explicitly read committed history/source state on a rerun. Preserve this terminal record and its measured divergence; do not recreate uncommitted changes to force a status output.",
        False,
        "2.0.0_SA_COO~W",
    ),
    "W17-S5": (
        "GRADUATED",
        "AC5 literally expects state-resources 22 and success strings; the output is 23 and six blank tails. The identified extra data source and six imported addresses explain the difference and support the import act, but the literal expectation is not satisfied. The amendment changed the denominator without changing this bar.",
        "At the next issuer cut, enumerate the six required managed addresses separately from data-source state entries and retain full import output. Record this criterion mismatch in L10; never repeat an import merely to recover a success string.",
        False,
        "2.0.0_SA_COO~W",
    ),
    "W17-S6": (
        "DISMISSED_WITH_REASON",
        "The owner amendment and worker execution provide the W17-S3 closure remedy. Independent closure calculation and the saved upload log agree. This corroborating record is accepted without deleting the original ARMED history.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "W17-S7": (
        "DISMISSED_WITH_REASON",
        "The seven additions, including validate.py and three package initializers, are reproduced by the independent closure. The cold-start wording needs a scope qualification: a module-level import inside a module reached only by a deferred importer does not by itself prove Lambda initialization fails. The concrete missing-module mechanism is valid; no extra remedy beyond the closure follows.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S96": (
        "GRADUATED",
        "The ranking and coverage readers address the DynamoDB articles table, while the commissioned harvest writes publication bodies/links to S3. No connecting reader/writer is established in the supplied bounded census. The repaired daily producer can therefore succeed while lacking the newly harvested content. This is the CTO-held article-store contract choice already named for the addendum.",
        "Carry the store/reader contract choice in the planned PRD addendum. Require traceable publication input to reach both ranking and coverage with a difference control. No vendor call, new model call, ETF-plane read, or mid-round cell is authorized by this finding.",
        False,
        "1.0.0_SA_CTO~W",
    ),
    "W16-S2": (
        "GRADUATED",
        "The chunk-name predicate cannot find the barrel-named emitted asset. The issuer amended AC5 to a content scan; the retained 55-JS-asset denominator, two positive strings in the same chunk, and zero-match control support the corrected build-presence claim.",
        "Accept the content-based criterion amendment and W16-S3 rerun. Do not rename a correct chunk to satisfy a broken predicate.",
        True,
        "2.0.0_SA_COO~W",
    ),
    "W16-S3": (
        "DISMISSED_WITH_REASON",
        "This is the measured rerun of the issuer-owned AC5 amendment, with no portal-source widening. It discharges W16-S2 and does not establish browser behavior.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S97": (
        "DISMISSED_WITH_REASON",
        "Accept the owner citing disarm of W17-S2 against the two saved plan/apply pairs and terminal orders. This is one completed ordering repair, not a second remedy.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S98": (
        "DISMISSED_WITH_REASON",
        "Accept the owner citing disarm of S88 for the deleted-table failure cause: the QA write and subsequent deployed-adapter read succeed. Do not promote that to evidence of the future 10:00Z scheduled fire or of harvest article inflow.",
        None,
        True,
        "2.0.0_SA_COO~W",
    ),
    "S99": (
        "DISMISSED_WITH_REASON",
        "Accept the late owner disarm of S89: the declaration is committed on the live bucket name and the shared file is clean. Correct the summary claim of zero bucket mentions: the full mount plan contains one refresh line and zero proposed bucket changes. That correction preserves the disarm.",
        None,
        True,
        "4.0.0_SA_CRO~Z",
    ),
}


def rows(path):
    out = []
    for b in re.findall(r"```json\s*(.*?)```", path.read_text(encoding="utf-8"), re.S):
        x = json.loads(b)
        out.extend(x if isinstance(x, list) else [x])
    return out


def main():
    audit = json.loads((ROOT / AUDIT).read_text(encoding="utf-8"))
    new = audit["new_items"]
    assert len(new) == 22 and audit["investigation_count"] == 174
    assert (
        not audit["nonterminal_orders"] and not audit["complete_orders_without_proof"]
    )
    assert all(p["check"]["rc"] == 0 for p in audit["proofs"])
    adj = []
    rem = []
    evidence = [AUDIT, VERIFY]

    def record(text, disp="DISMISSED_WITH_REASON", refs=None, extra=None):
        r = {
            "id": f"AMGT_RESAPP-Z-C-S{172 + len(adj)}",
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "surfaced_by": SEAT,
            "surfaced_at": NOW,
            "one_line": text,
            "class": "OBSERVATION",
            "hazard_standing": "INERT",
            "grounding": {"status": "GROUNDED", "evidence": list(evidence)},
            "disposition": disp,
            "spec_asserts": "Canonical workflow L8/L9: read the issued bar, preserve denominators and assign every investigation item a disposition.",
            "world_is": text,
            "notes": "Round-10 review at the captured evidence vintage. A disposition is not an automatic disarm or a declaration of endpoint realization.",
        }
        if refs:
            r["adjudicates"] = refs
        if disp == "DISMISSED_WITH_REASON":
            r["dismissal_reason"] = text
        if extra:
            r.update(extra)
        adj.append(r)
        return r

    def remedy(item, text, owner, closed, mechanism=None):
        r = {
            "id": item["id"],
            "project": "AMGT_RESAPP",
            "fabric": "site-z",
            "class": item.get("class", "OBSERVATION"),
            "hazard_standing": item.get("hazard_standing", "INERT"),
            "mechanism": mechanism or item["world_is"],
            "evidence": list(evidence),
            "remedy": text,
            "owner": owner,
            "round": "v10",
            "remediation": {
                "state": "REMEDIATED" if closed else "OPEN",
                "owner": owner,
                "round": "v10",
            },
            "closed": closed,
        }
        if r["hazard_standing"] == "ARMED":
            r["disarm"] = {
                "state": "DISARMED" if closed else "ARMED",
                "owner": owner,
                "at": NOW if closed else None,
            }
        rem.append(r)
        return r

    for item in new:
        short = item["id"].removeprefix("AMGT_RESAPP-Z-")
        disp, text, fix, done, owner = REVIEWS[short]
        r = record(
            short + ": " + text,
            disp,
            [item["id"]],
            {"spec_asserts": item["spec_asserts"], "world_is": text},
        )
        r["grounding"]["evidence"].append(
            "org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md#"
            + item["id"]
        )
        if fix:
            remedy(item, fix, owner, done, text)
    proof = {
        p["data"]["to_id"]: p
        for p in audit["proofs"]
        if ".TO-AMGT-ri-" in p["data"]["to_id"]
    }
    grade1 = record(
        "AMGT-ri-1 AC7 PASS: the rendered read-failure sentence names the failed read, explicitly leaves producer availability unknown, and is visibly different from successful emptiness. Six states and seven controls independently replay correctly. The status is visible in the error detail; structured-status prominence is not established by the synthetic Error arm."
    )
    grade1["grounding"]["evidence"].append(BOUNDARY)
    grade1["grades"] = [
        {
            "criterion": "AMGTri1-AC7",
            "instance": proof["AMGT_RESAPP.TO-AMGT-ri-1"]["path"] + "@672bca64fe",
            "verdict": "PASS",
            "reason": "Issued ri-1 AC7 asks whether the failure text is honest and distinguishable from an empty day. The actual component render and error screenshot satisfy that bar. This is a text judgment, not a live-edge or pipeline certification.",
        }
    ]
    grade2 = record(
        "AMGT-ri-3 AC6 FAIL: clicking a ranked ticker yields an unresolved security and no figures; the canonical-key search is a different path. No drafted prose is returned, and a figure check badge is not the required FWD9 drafting marker. The browser rendered 2026-09-12 input, while AC2 saved 2026-09-15 input; equal counts are not the same payload."
    )
    grade2["grades"] = [
        {
            "criterion": "AMGTri3-AC6",
            "instance": proof["AMGT_RESAPP.TO-AMGT-ri-3"]["path"] + "@8da6d27866",
            "verdict": "FAIL",
            "reason": "The issued AC6 requires an assembled working route populated from the saved AC2 input, ranked-row navigation, FWD9 evidence marking and a distinct error arm. Only the last is established without a remaining gap. Parts B/C use different dates and computed_at values. Source, response and browser evidence refute the navigation and drafting limbs; a new live-edge run is not needed to identify these failures.",
        }
    ]
    prose = record(
        "FWD9 remains unimplemented at the served drafting boundary: read_thesis_bundle returns drafted_sections=[]; both saved thesis payloads have zero sections. The actual ThesisTab controlled render labels a generated sentence but puts its evidence only in title, with zero visible evidence. Figure check badges cannot discharge a prose/evidence requirement.",
        "GRADUATED",
        extra={
            "spec_asserts": "PRD FWD-9 DONE WHEN APPLIED: marking sits beside the evidence the sentence was drawn from. ri-3 quotes that requirement, not merely fiscal figures.",
            "hazard_standing": "ARMED",
            "disarm_owner": "2.0.0_SA_COO~W",
        },
    )
    prose["grounding"]["evidence"].append(PROSE)
    remedy(
        prose,
        "Recut the existing drafting/adapter/Thesis connection so actual generated sentences and their source evidence reach the page, and render the evidence visibly beside each machine-marked sentence. Exercise generated and firm-text controls, plus absent input; a tooltip alone and figure badges are insufficient.",
        "2.0.0_SA_COO~W",
        False,
    )
    record(
        "Packet corrections: the round has TWO judgments and 31 mechanical criteria, not one judgment with ri-1 at 7/7 mechanical PASS. ri-2 AC2/AC5 have literal expectation mismatches despite valid schemas and supported underlying acts. Browser Part B is 09-12, deployed AC2 is 09-15; same axis/resolution/count is not same-day evidence. The mount plan has one bucket refresh mention, zero bucket actions. W16-S1 has five distinct hashes over six states. These corrections do not justify reverting a completed deploy."
    )
    # Historical remediation IDs stay in their original files. Their five proven
    # clock advances are applied separately as the gate's permitted monotone edits.
    assert len(adj) == 26
    assert len({r["id"] for r in rem}) == len(rem)
    assert {i for r in adj for i in r.get("adjudicates", [])} == {r["id"] for r in new}
    head = """# AMGT_RESAPP round 10: CVO adjudication

Seat `3.0.0_SA_CVO~W`; packet 23019 from COO~W. Scope: AMGT_RESAPP round 10 as cut, before the planned addendum.

## Judgment

| Criterion | Verdict | Basis |
|---|---|---|
| AMGT-ri-1 AC7 | PASS | Honest read-failure text, distinguishable from successful empty data; actual-component replay and saved browser screenshot. |
| AMGT-ri-3 AC6 | FAIL | Ranked click does not resolve figures; no FWD9 drafted prose/evidence; browser input differs from saved AC2 input. |

The orders contain **two** judgments, not the packet's one. Their four proof files contain 31 mechanical PASS claims plus two UNVERIFIABLE-BY-INSTRUMENT judgment records. Schema validation is not truth grading. In particular, ri-2 AC2's committed-state read and AC5's 23-versus-22/blank-tail output do not literally meet their expectation text; their underlying consolidation/import acts are supported. Preserve these facts and fix the issuer criteria at the next cut, without repeating world acts.

## L8 watermark and evidence boundary

174 investigation items: 152 previously adjudicated, 22 reviewed here, zero left without a disposition. Packet vintage held 173; owner S99 is the additional item. Both roots were checked: canonical tree present, legacy AMGT root absent. The source audit names file hashes and its timestamp. CVO rows are not investigation items. Existing dispositions are retained; no worker row was edited.

51 task orders: 48 complete, three superseded, zero nonterminal. All 49 retained proof instances validate against the current checker and their issued criterion sets; every complete order has a proof. Earlier truth grades remain at their earlier vintages. Four drain commits are ancestors of the reviewed HEAD. The parser uses line-anchored status elements so quoted `<status>` instructions cannot manufacture nonterminal orders.

The audit is the explicit review watermark. The launcher readiness oracle is GREEN 9/9; that is runtime readiness, not an intake watermark. The launcher-owned heartbeat still does not carry this review count; no second heartbeat, watcher, detector or cron was started to manufacture one.

Independent local reads reproduce the 85/96 route sets with zero lost keys, the 0/4/0 and 19/0/0 plan/apply records, the committed bucket-name repair, the 23-to-30 source closure (20 required modules, zero missing; seed control missing three), the saved response counts and the six-state error boundary. The current source closure is not a new deployed-ZIP read. No new AWS, vendor, model, browser-session or ETF-plane call was made.

The browser Part B used `as_of_date=2026-09-12`, computed_at `2026-09-12T01:22Z`; AC2 saved `2026-09-15`, computed_at `2026-09-15T02:35Z`. Both carry ten rows with the same ticker order and resolution, but are different payloads. The Part C claim of agreement for the same day is not supported. The actual ThesisTab controlled render uses synthetic generated/firm prose with explicitly stubbed query/layout dependencies: the machine label discriminates, evidence is present only in `title`, and visible evidence is absent. Saved real thesis responses contain zero drafted sections. Screenshots were inspected for the error, unresolved-click and resolved-key states.

FWD9 is machine prose beside source evidence, not figure check badges. No outcome is declared REALIZED here. Portal evidence stays at `9aef37344cd68c06f37d9d33eb1f2bc886dd6c4c`; shared gitlink remains `e85f6eb84f3a1771a37011a7e77e372570bad02a`. The later Posture/four-tab/header/harvest-union directions do not retroactively alter this grade.

## Dispositions and grades

"""
    (C / "adjudications/ADJUDICATION_v10.md").write_text(
        head + "```json\n" + json.dumps(adj, ensure_ascii=False, indent=2) + "\n```\n",
        encoding="utf-8",
    )
    open_rows = [r for r in rem if not r.get("closed")]
    slug = f"""# AMGT_RESAPP round 10: remediation slug

**To:** `1.0.0_SA_CTO~W` only. **From:** `{SEAT}`. One artifact for the L10 read; all pins local under the site-Z push hold.

**Result:** the error/empty boundary is repaired, the producer writes under QA and the API mount is deployed. The assembled page still fails ri-3 AC6. ri-1 AC7 passes. The packet omitted the second judgment; neither a valid proof file nor 31 worker mechanical PASS claims substitutes for these grades.

## What the next read must carry

1. **Ranked-click identity (S95):** ten rows carry tickers but no canonical keys. Clicking BABA US yields no figures; canonical-key search yields 13 header and 183 fiscal figures. Recut the existing seam.
2. **Drafting/evidence (C-S196):** the adapter returns zero drafted sections and the actual component hides sentence evidence in a tooltip. FWD9 is not met by figure badges. Recut the existing drafting/adapter/Thesis connection and visibly pair machine prose with its evidence.
3. **Exact-input exercise (S72):** the browser rendered 09-12; AC2 captured 09-15. Equal counts/axis/ticker order are insufficient. Keep the exact payload hash/day through the assembled-route exercise, with error and empty controls. No live-edge or person-session claim exists.
4. **Article-store contract (S96):** repaired DynamoDB reader versus S3 publication writer. The already announced CTO addendum owns the store choice and traceable inflow requirement; this slug authorizes no new source access.
5. **Issuer criteria (W17-S4/S5):** committed changes cannot print as pending status, and 23 state entries cannot satisfy a literal 22. Preserve the proven underlying acts and explicit literal misses. Amend future criteria; do not replay imports or deployments to satisfy a display artifact.

The header/four-tabs/executive-managers/Posture/holdings-union directions in the CTO relays enter through the later addendum. Round 10 is graded against its issued specification. The organic 10:00Z fire remains a distinct future observation; QA recovery is already measured and does not wait for it. No worker is contacted or recut by this CVO handoff.

## Closed and carried clocks

Close S88 (owner S98), S89 (late owner S99), W17-S2/S3, W16-S2 and the page-count criterion repair. Advance prior S68, S69, S71 and C-S169 in REMEDIATION_v9.md and W11-S2 in REMEDIATION_v7.md on the completed evidence. These are monotone clock updates; their original IDs, mechanisms and owners stay in place. Preserve S70/W11-S1 under the portal freeze, S72's incomplete assembled-route obligation, S78's Andrew-reserved owner decision, and the existing CTO/CRO clocks S67/C-S49 without manufacturing their owner disarms. C-S49's source mechanism was repaired by ri-2; an outstanding owner clock is not a claim that the source is still broken.

Snapshot: **174 investigation items, 174 dispositioned** (152 prior + 22 here), **51 terminal orders** (48 complete + three superseded), **49/49 structurally valid proof instances**. The row list below has **{len(rem)} remediation rows: {len(rem) - len(open_rows)} closed, {len(open_rows)} open**. This is a remedy-row count, not an investigation-item or at-surfacing ARMED count. Unchanged prior history remains in earlier round files.

Validation artifacts: `{AUDIT}`, `{VERIFY}`, `{PROSE}`, `{BOUNDARY}`. Judgment carrier: `adjudications/ADJUDICATION_v10.md`. Saved logs and source snapshots were read independently; deployment evidence was not freshly re-run. The runtime readiness check is GREEN 9/9; the review count is recorded here, not falsely attributed to the launcher heartbeat.

## Historical rows cited without duplication

S67, S70, S72 and S78 remain in `REMEDIATION_v9.md`; W11-S1 remains in `REMEDIATION_v7.md`; C-S49 remains in `REMEDIATION_v5.md`. Their six existing clocks remain open. The twelve rows below are new this round, not copies of those records.

Stamp boundary: L8/L9/L10 round-10 stamps are this seat\'s. The canonical tool warned that predecessor `L6.json` is absent; the issuer owns that record gap. No issuer stamp was fabricated.

## Remediation rows

"""
    (C / "remediations/REMEDIATION_v10.md").write_text(
        slug + "```json\n" + json.dumps(rem, ensure_ascii=False, indent=2) + "\n```\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "adjudications": len(adj),
                "grades": [
                    (g["criterion"], g["verdict"])
                    for r in adj
                    for g in r.get("grades", [])
                ],
                "prose_finding": prose["id"],
                "remediations": len(rem),
                "open": len(open_rows),
                "closed": len(rem) - len(open_rows),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
