"""Prepare pinned round-3 review bytes and the exact LD-0562 exception record.

Preparation writes only this seat's deliverables. Publication is a separate,
explicit step after the immutable record is committed and the gate recognizes it.
"""

import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = "org/missions/D4/POSN/POSN_ASTTAX"
PREFIX = "org/tier1_exec/3.0.0_SA_CVO/deliverables/"
BASE = "ee0a2dbf829e99ce0ac9e37ddd975638818fb3f1"
ADJ = PROJECT + "/surprise-channel/adjudications/ADJUDICATION_v5.md"
REM = PROJECT + "/surprise-channel/remediations/REMEDIATION_v3.md"
EVIDENCE = PREFIX + "POSN_ASTTAX_ROUND3_RELEASE_EVIDENCE_20260913_Z.json"
PACKAGE = PREFIX + "POSN_ASTTAX_ROUND3_RELEASE_PACKAGE_20260913_Z.json"
EXCEPTION = PREFIX + "POSN_ASTTAX_ROUND3_ROUTING_EXCEPTION_20260913_Z.json"
AUTHORITY = (
    "org/tier1_exec/2.0.0_SA_COO~Z/deliverables/"
    "ANDREW_DIRECT_20260913T0408Z_POSN_ASTTAX_CARRY_FORWARD_YES_DEPLOY_CONDITIONAL_BRIEF_YES.md"
)
CTO = "1.0.0_SA_CTO~Z"
COO = "2.0.0_SA_COO~Z"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def text_blob(pin, path):
    return git("show", pin + ":" + path).decode("utf-8")


def write_json(path, data):
    (ROOT / path).write_text(
        json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )


def load_gate():
    spec = importlib.util.spec_from_file_location(
        "gate", ROOT / ".tools/surprise-row-gate.py"
    )
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    return gate


def main():
    gate = load_gate()
    pin = git("rev-parse", "HEAD").decode().strip()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tracked = (
        git("ls-tree", "-r", "--name-only", pin, "--", PROJECT).decode().splitlines()
    )
    channel = [p for p in tracked if "/surprise-channel/" in p and p.endswith(".md")]
    files = []
    originals = {}
    existing_rem = []
    for path in channel:
        body = text_blob(pin, path)
        rows, malformed = gate._rows(body, False)
        assert not malformed, path
        if "/remediations/" in path:
            existing_rem.extend(rows)
        else:
            files.append((path, rows))
            if "/investigations/" in path:
                originals.update((r["id"], r) for r in rows)
    # The legacy root is a second domain, even when its result is empty.
    legacy, error = gate._index_paths(
        str(ROOT), [p % "POSN_ASTTAX" for p in gate.INVESTIGATION_PATTERNS]
    )
    assert legacy is not None, error
    assert all(p in channel for p in legacy), legacy
    current, unknown = gate._resolve_latest(files, [r["id"] for r in existing_rem])
    assert not unknown, unknown
    pending = sorted(
        k for k, value in current.items() if value == "UNDER_INVESTIGATION"
    )
    expected = ["POSN_ASTTAX-Z-W14-S1"] + [f"POSN_ASTTAX-Z-S{n}" for n in range(37, 45)]
    assert pending == sorted(expected), pending
    old_adj = dict(files)[
        PROJECT + "/surprise-channel/adjudications/ADJUDICATION_v4.md"
    ]
    assert len(old_adj) == 29
    assert text_blob(
        BASE, PROJECT + "/surprise-channel/adjudications/ADJUDICATION_v4.md"
    ) == text_blob(pin, PROJECT + "/surprise-channel/adjudications/ADJUDICATION_v4.md")
    cached_proofs = {}
    if (ROOT / EVIDENCE).exists():
        cached_proofs = {
            p["path"]: p for p in json.loads((ROOT / EVIDENCE).read_text())["proofs"]
        }
    proofs = []
    for path in tracked:
        if not path.endswith(".proof_of_spec.json"):
            continue
        order = (
            PROJECT
            + "/task-orders/"
            + Path(path).name.replace(".proof_of_spec.json", ".md")
        )
        proof_bytes, order_bytes = (
            git("show", pin + ":" + path),
            git("show", pin + ":" + order),
        )
        assert proof_bytes == git("show", BASE + ":" + path), path
        assert order_bytes == git("show", BASE + ":" + order), order
        assert (ROOT / path).read_text(encoding="utf-8") == proof_bytes.decode(
            "utf-8"
        ), path
        ids = re.findall(r'<criterion\s+id="([^"]+)"', order_bytes.decode("utf-8"))
        assert ids, order
        cached = cached_proofs.get(path)
        if cached and (
            cached["sha256"],
            cached["order_sha256"],
            cached["criteria"],
            cached["structure_rc"],
        ) == (sha(proof_bytes), sha(order_bytes), ids, 0):
            proofs.append(cached)
            continue
        check = subprocess.run(
            [sys.executable, ".tools/proof-of-spec-check.py", path, ",".join(ids)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert check.returncode == 0, (path, check.stdout, check.stderr)
        proofs.append(
            {
                "path": path,
                "sha256": sha(proof_bytes),
                "order": order,
                "order_sha256": sha(order_bytes),
                "criteria": ids,
                "structure_rc": check.returncode,
                "stdout": check.stdout,
                "unchanged_since_review": BASE,
            }
        )
    assert len(proofs) == 11
    orders = []
    total_orders = [p for p in tracked if "/task-orders/" in p and p.endswith(".md")]
    for path in total_orders:
        body = text_blob(pin, path)
        status = gate.TO_STATUS_RE.search(body).group(1).lower()
        if status not in gate.TERMINAL_TO_WORDS:
            orders.append(
                {
                    "path": path,
                    "open_label": Path(path).name + " [" + status + "]",
                    "sha256": sha(body.encode("utf-8")),
                }
            )
    assert len(total_orders) == 15 and len(orders) == 4
    assert sorted(
        re.search(r"TO-([ST][0-9]+-1)", x["path"]).group(1) for x in orders
    ) == ["S2-1", "S3-1", "T6-1", "T7-1"]
    assert text_blob("b75f5a805a", AUTHORITY) == text_blob(pin, AUTHORITY)
    old_evidence_path = PREFIX + "POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
    assert text_blob(BASE, old_evidence_path) == text_blob(pin, old_evidence_path)
    old_evidence = json.loads(text_blob(pin, old_evidence_path))
    assert old_evidence["summary"] == {
        "candidate_source_after_carried": 11,
        "candidate_downloaded_after_raises": 11,
        "candidate_denominator": 11,
    }
    rows = []

    def add(
        n,
        target,
        disposition,
        mechanism,
        remedy,
        owner=None,
        standing="INERT",
        evidence=None,
    ):
        row = {
            "id": f"POSN_ASTTAX-Z-C-S{n}",
            "project": "POSN_ASTTAX",
            "fabric": "site-z",
            "surfaced_by": "3.0.0_SA_CVO~Z",
            "surfaced_at": now,
            "one_line": mechanism,
            "class": "OBSERVATION",
            "hazard_standing": standing,
            "disposition": disposition,
            "grounding": {
                "status": "GROUNDED",
                "evidence": evidence or [EVIDENCE + "#intake=" + pin],
            },
            "spec_asserts": originals[target]["spec_asserts"]
            if target
            else "L9 preserves issued conditions, measured artifact vintages, named owners and the authorized carry-forward scope.",
            "world_is": mechanism,
            "notes": remedy,
        }
        if target:
            row["adjudicates"] = [target]
        if owner:
            row["disarm_owner"] = owner
        if disposition == "DISMISSED_WITH_REASON":
            row["dismissal_reason"] = remedy
        rows.append(row)
        return row

    add(
        65,
        "POSN_ASTTAX-Z-W14-S1",
        "DECOMP_INVALIDATING",
        "The pinned downloaded generator raises in 11/11 candidate AFTER controls while repaired source carries 11/11. The round has no deploy/effective-artifact cell. LD-0562 now permits round-3 carry-forward of the four named open orders, releasing C-S52's pending disposition. This does not establish a performed retag or live page blanking.",
        "COO recut after CTO analysis: include the separately authorized deployment and effective-artifact verification act. Deployment remains conditional on the two-seat never-widen sign-off with blast radius and per-key rollback. Retag remains NO-GO until its bar is met. Keep all four carried order statuses and bytes unchanged.",
        COO,
        "ARMED",
        [old_evidence_path + "@" + BASE, AUTHORITY + "@b75f5a805a"],
    )
    add(
        66,
        None,
        "DECOMP_INVALIDATING",
        "C-S64's missing-repair-cell proposal is released on the same named carry-forward ruling. The seven-cell decomposition measures frontend and sibling failures but contains no corresponding implementation repair. A source measurement cell is not a repair cell; C-S60's correction of the old W4-S2 category remains valid.",
        "Supersedes the pending C-S64 proposal, without rewriting it. CTO records coverage and the unchanged portal freeze; COO prices and sequences only authorized repairs. No portal edit, gitlink move or foreign publisher write is authorized by this row.",
        COO,
        "ARMED",
        [
            old_evidence_path + "@" + BASE,
            PROJECT + "/decompositions/POSN_ASTTAX_DECOMP_round3.md@" + pin,
            AUTHORITY + "@b75f5a805a",
        ],
    )
    add(
        67,
        "POSN_ASTTAX-Z-S37",
        "GRADUATED",
        "The owner acknowledges omitted adjudication-plane obligations. Its initial 39 ARMED ids and later S41 join are candidate screens, not a verified live-obligation census. Absence of a later citation is not sufficient to prove a remedy unexecuted: W10-S1's already-corrected mechanism is a concrete counterexample elsewhere in the same channel.",
        "COO completes the bounded per-obligation read, joins originals to adjudications, and records each remedy's current condition and evidence. Preserve historical counts with their pins; do not subtract citation counts into a live verdict. S41 refines this same task and receives no duplicate remedy.",
        COO,
        "ARMED",
    )
    add(
        68,
        "POSN_ASTTAX-Z-S38",
        "GRADUATED",
        "The CTO's S39 reads the nine uncited cases to conditions and S40 reads the eight cited pairs. That completes S38's stated reading task; it does not complete the underlying remedies. The record itself acknowledges candidate versus live standing.",
        "REMEDIATED in round by S39/S40's actual per-id reasoning. Accept the completed read only. S40's printed reconciliation adds to 27, not 26 (8+9+7+1+2); it cannot serve as an audited total. In addition, W10-S1 already has the corrected PRD allocation-dict paragraph and must not be recut merely because the read called it undone.",
        CTO,
    )
    add(
        69,
        "POSN_ASTTAX-Z-S39",
        "DISMISSED_WITH_REASON",
        "This is the first half of S38's completed reading task plus two proposed follow-ups. The source-weight correction already appears in PRD s.4, as the prior C-S40 review recorded; the C-S55 boundary decision is subsequently made by S42. S42 explicitly retains its PRD landing obligation.",
        "No additional remedy: the read closes under S38, the already-corrected sentence is not reissued, and the remaining scope-disclosure landing is carried by S42. Underlying tooling and constituent-seeder remedies stay on their existing carriers; calling them parked does not close them.",
    )
    add(
        70,
        "POSN_ASTTAX-Z-S40",
        "DISMISSED_WITH_REASON",
        "Explicit adjudicates links support the fact that some investigation and adjudication rows describe the same obligation. The eight pairs are substantively read. They do not support the universal claim that every row-id census is an obligation count, or the stated 26-total arithmetic.",
        "Accept S38's completed read; reject the numerical closure claim. The row's own six terms sum to 27. The original and its adjudication are different records; equivalence of remedies requires a read and cannot be inferred from any citation or blindly subtracting edges.",
    )
    add(
        71,
        "POSN_ASTTAX-Z-S41",
        "DISMISSED_WITH_REASON",
        "The 55-minus-21 calculation is a reported reduction of owner-tagged row ids using links, at a later vintage that includes the census row itself. It openly states the per-obligation standing read is still owed.",
        "This refines S37's grain and does not discharge it. Carry the actual unfinished owner read once, under S37; neither 34 nor 40 is independently accepted here as a current live count.",
    )
    add(
        72,
        "POSN_ASTTAX-Z-S42",
        "GRADUATED",
        "The CTO settles the C-S55 boundary decision: the additional ETF publisher is outside POSN write scope and inside disclosure scope. Its measured 189 rows/four books/zero candidate members is a pinned state whose expiry is any candidate appearing. The decision is made; the PRD disclosure sentence remains to land.",
        "CTO lands the disclosed non-owned reader and its state/expiry at the authorized L10 PRD pass, with normal ratified-text review if that half changes. Do not create a POSN implementation cell for the foreign publisher. C-S55's decision is completed; this remaining document act is separate.",
        CTO,
    )
    add(
        73,
        "POSN_ASTTAX-Z-S43",
        "GRADUATED",
        "The conditional deployment requires a writer census of the exact property and blast radius named by the act. The row's N>=3 is a proposed floor, not a finished census, and repeats the PRD's swapped producer attribution: allocation-summary reads holdings_attribution_data.json and writes allocation_summary.json. Registry writers and output producers are distinct sets.",
        "CTO sign-off half must name the exact act/property, count every writer of that property, read each rule and print per-key rollback; reconcile the producer mapping. Do not count the unrelated ETF publisher as a writer of positioning_data.json merely because it copies a class elsewhere. Preserve S42 disclosure and the separate second registry writer. No signature or deploy is issued by this review.",
        CTO,
        "ARMED",
    )
    add(
        74,
        None,
        "DISMISSED_WITH_REASON",
        "COO message 22263 infers an unnotified mv failure from message 22245 remaining at the inbox root. This seat actually received the hard-nudge, read the exact body, reproduced the gate refusal and deliberately retained the file pending completion. The cited consuming inbox-watch.sh is not this Codex seat's runtime.",
        "The mv-failure diagnosis is falsified by the received turn and actual reads. No detector repair, duplicate helper or broker poll is required from this observation. Message state alone is not evidence that the recipient has not read it.",
    )
    add(
        75,
        None,
        "GRADUATED",
        "At this intake pin the terminality gate implements only the row-and-order-pinned round-2 exception. An actual read-only call still refuses the four LD-0562-carried orders in round 3. The sovereign exception is approved but not yet represented by the instrument.",
        "Represent only the named round-3 case using the existing immutable-record mechanism: exact project, round, paths, row hashes and four unchanged order blobs; retain every other gate limb and fail closed on unreadable or altered evidence. No general override, terminal-status change or standing carry-forward rule.",
        CTO,
        "ARMED",
    )
    add(
        76,
        "POSN_ASTTAX-Z-S44",
        "DISMISSED_WITH_REASON",
        "The row's non-application is the actual case. This Codex seat received hard-nudges 22245 and 22263, read their exact bodies and began the named L10 work; both files were retained until the act finishes. Its runtime is the launcher-owned bridge/detector, not inbox-watch.sh. MSTR 22270 separately confirms that architectural distinction. This review package is an actual CVO artifact citing LD-0562 and therefore also meets S44's explicit disarm arm.",
        "Dismiss the missing-notification mechanism and the resulting undemonstrable-arrival claim. Preserve the useful limitation of broker QUEUED as a receipt oracle and the author's mtime corrections. No replacement watcher, restart, helper, broker ACK fabrication or peer inbox move follows. C-S74 records the earlier re-send inference; this row resolves the later formal original.",
    )

    # A new remediation uses the CVO decision's coordinate, as the prior slug did.
    closed_targets = {
        "POSN_ASTTAX-Z-S6",
        "POSN_ASTTAX-Z-S7",
        "POSN_ASTTAX-Z-W10-S1",
        "POSN_ASTTAX-Z-W11-S1",
        "POSN_ASTTAX-Z-W13-S2",
        "POSN_ASTTAX-Z-W14-S4",
    }
    rems = []
    prior_ids = {r["id"] for r in existing_rem}
    for row in old_adj + rows:
        if (
            row["disposition"] not in {"GRADUATED", "DECOMP_INVALIDATING"}
            or row["id"] in prior_ids
        ):
            continue
        targets = set(row.get("adjudicates", []))
        closed = bool(targets & closed_targets) or row["id"] in {
            "POSN_ASTTAX-Z-C-S60",
            "POSN_ASTTAX-Z-C-S68",
            "POSN_ASTTAX-Z-C-S75",
        }
        owner = row.get("disarm_owner", COO)
        remedy = row["notes"]
        if targets == {"POSN_ASTTAX-Z-W14-S4"}:
            remedy = "REMEDIATED decision: S42 settles outside-POSN write scope and mandatory disclosure. The still-unlanded PRD sentence is carried separately by C-S72, and zero current candidates is not permanent safety."
        if row["id"] == "POSN_ASTTAX-Z-C-S75":
            remedy = "PROPOSED RELEASE STATE ONLY: REMEDIATED when the exact round-3 mechanism and its rejection controls pass before publication. Evidence: POSN_ASTTAX_ROUND3_RELEASE_VALIDATION_20260913_Z.json. Publication must stop if those checks fail. No general override or change to carried order bytes."
        rem = {
            "id": row["id"],
            "project": "POSN_ASTTAX",
            "fabric": "site-z",
            "class": row["class"],
            "hazard_standing": row["hazard_standing"],
            "mechanism": row["world_is"],
            "evidence": row["grounding"]["evidence"] + [EVIDENCE],
            "remedy": remedy,
            "owner": owner,
            "round": "v3",
            "remediation": {
                "state": "REMEDIATED" if closed else "OPEN",
                "owner": owner,
                "round": "v3",
            },
            "closed": closed,
        }
        if rem["hazard_standing"] == "ARMED":
            rem["disarm"] = {
                "state": "DISARMED" if closed else "ARMED",
                "owner": owner,
                "at": now if closed else None,
            }
        rems.append(rem)
    assert len({r["id"] for r in rems}) == len(rems)
    for row in rows:
        assert not gate._check_row(
            row, "INVESTIGATION", gate._schema(str(ROOT), "INVESTIGATION")
        ), row
    for row in rems:
        assert not gate._check_row(
            row, "REMEDIATION", gate._schema(str(ROOT), "REMEDIATION")
        ), row
    latest, unknown = gate._resolve_latest(
        files + [(ADJ, rows)], [r["id"] for r in existing_rem + rems]
    )
    assert not unknown, unknown
    assert not [k for k, v in latest.items() if v == "UNDER_INVESTIGATION"]
    refusal = gate._route_precondition_violations(
        str(ROOT), ADJ, rows[0], "POSN_ASTTAX", route_word="proposed round-3 DI"
    )
    assert refusal, "Reassess: the gate changed while preparing this release"
    proof_summary = {
        "count": len(proofs),
        "valid": sum(p["structure_rc"] == 0 for p in proofs),
    }
    producer_path = "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py"
    producer_body = text_blob(pin, producer_path)
    producer_lines = [
        {"line": n, "text": line}
        for n, line in enumerate(producer_body.splitlines(), 1)
        if any(
            term in line
            for term in (
                "holdings_attribution_data.json",
                "allocation_summary.json",
                "put_object(",
            )
        )
    ]
    assert (
        "holdings_attribution_data.json" in producer_body
        and "allocation_summary.json" in producer_body
    )
    result = {
        "pin": pin,
        "utc": now,
        "status": "PREPARED_NOT_ISSUED",
        "channel_files": channel,
        "originals": len(originals),
        "pending_before": pending,
        "pending_after_proposed": [],
        "proofs": proofs,
        "proof_summary": proof_summary,
        "orders": orders,
        "total_orders": len(total_orders),
        "new_rows": rows,
        "late_originals": [originals[k] for k in pending],
        "gate_refusal_before": refusal,
        "authority_path": AUTHORITY,
        "authority_pin": "b75f5a805a",
        "prior_evidence_path": old_evidence_path,
        "prior_evidence_sha256": sha(text_blob(pin, old_evidence_path).encode()),
        "carry_existing_remediations": existing_rem,
        "judgment_grades": next(r["grades"] for r in old_adj if "grades" in r),
        "producer_mapping": {
            "path": producer_path,
            "pin": pin,
            "sha256": sha(producer_body.encode()),
            "lines": producer_lines,
        },
        "limits": "Prior behavioral controls and eleven proof/order pairs retained at their explicit pins; fresh structural checks only. No fresh vendor call, AWS act, live DOM, retag, deploy, gitlink change or FWD realization claim.",
    }
    write_json(EVIDENCE, result)
    header = (
        "# POSN_ASTTAX round 3 - L9 completion under LD-0562\n\n"
        f"Intake {pin}. {len(originals)} original items, all dispositioned by the combined proposed review. "
        "Fifteen orders: eleven terminal and four explicitly carried unchanged under LD-0562. "
        "This exception changes only the named round's terminality precondition. Retag NO-GO, portal freeze and deployment sign-off conditions remain.\n\n"
        "The five judgment grades in ADJUDICATION_v4 C-S61 remain two scoped PASS, two FAIL and one NOT_EVALUATED. "
        "All eleven proof instances were freshly checked structurally against their unchanged issued criteria; no historical proof was rewritten. "
        "The new rows release the two previously pending missing-cell findings and review all late originals.\n\n"
    )
    adj_body = header + "```json\n" + json.dumps(rows, indent=2) + "\n```\n"
    rem_header = (
        "# POSN_ASTTAX REMEDIATION v3 - round 3, site Z\n\n"
        "One round-3 slug, read by CTO at L10. Four orders S2-1/S3-1/T6-1/T7-1 are carried unrun under LD-0562; "
        "their status and content are not made terminal. Existing v1/v2 remedies remain on their carriers, "
        "including their explicit supersessions; a row census is not a count of independent work.\n\n"
        f"This round adds {len(rems)} remediation records, {sum(r['closed'] for r in rems)} completed and "
        f"{sum(not r['closed'] for r in rems)} open. The gate-mechanism row closes only after its exact controls and the canonical commit pass.\n\n"
        "The deployment gap and missing frontend/sibling implementation are distinct from measurement. "
        "The additional ETF publisher receives disclosure only, with its pinned zero-candidate state and expiry. "
        "The portal remains frozen. No retag or deployment is authorized by this document. No FWD is claimed REALIZED.\n\n"
        f"Review/evidence: `{ADJ}`, `{EVIDENCE}`. The prior C-S61 judgment grades remain binding.\n\n"
    )
    rem_body = rem_header + "```json\n" + json.dumps(rems, indent=2) + "\n```\n"
    package = {
        "pin": pin,
        "status": "PREPARED_NOT_ISSUED",
        "files": {ADJ: adj_body, REM: rem_body},
    }
    write_json(PACKAGE, package)
    authorized_rows = [
        {"path": ADJ, "id": r["id"], "sha256": gate._canon_hash(r)}
        for r in rows
        if r["disposition"] == "DECOMP_INVALIDATING"
    ]
    authorized_rows += [
        {"path": REM, "id": r["id"], "sha256": gate._canon_hash(r)} for r in rems
    ]
    record = {
        "schema_version": 1,
        "project": "POSN_ASTTAX",
        "round": 3,
        "authority_message_id": 22245,
        "authority_sender": COO,
        "authority_record": AUTHORITY,
        "authority_pin": "b75f5a805a",
        "authority_record_sha256": sha(text_blob("b75f5a805a", AUTHORITY).encode()),
        "authority_record_verbatim": text_blob("b75f5a805a", AUTHORITY),
        "recorded_by": "3.0.0_SA_CVO~Z",
        "scope": "LD-0562 round 3 only; terminality limb only; exact filing paths, canonical row hashes and four unchanged order blobs. No general waiver or terminal-status authority.",
        "expected_total_orders": 15,
        "orders": orders,
        "rows": authorized_rows,
        "package": PACKAGE,
        "package_sha256": sha((ROOT / PACKAGE).read_bytes()),
    }
    write_json(EXCEPTION, record)
    print(
        json.dumps(
            {
                "pin": pin,
                "originals": len(originals),
                "review_rows": len(rows),
                "remediations": len(rems),
                "completed": sum(r["closed"] for r in rems),
                "proofs": proof_summary,
                "pending_proposed": [],
                "prepared_paths": [EVIDENCE, PACKAGE, EXCEPTION],
            }
        )
    )


if __name__ == "__main__":
    main()
