#!/usr/bin/env python
"""WP-3 ledger engine -- the store, atomic batch admission, and the commit_seq envelope.

IMPLEMENTS the frozen model at WP3_LEDGER_DESIGN.md sec 2c (admission), 2d (references) and
2e (admission order + the replay anchor). It does NOT revise it: a contract defect found here is a
finding routed to the issuer for a NEW candidate (sec 0, WP3-mech-1).

ENGINE: single-file SQLite, local to the owning device (ENGINE_CHOICE.md, AC4) -- chosen because
the ledger store lives on the device that owns the work and no write to it is ferried across a
fabric boundary (Rule 26, CLAUDE_ANNEX.md:465).

THE THREE THINGS THIS FILE IS RESPONSIBLE FOR

1. A WRITE IS A BATCH, ADMITTED ATOMICALLY (sec 2c). Every reference in the batch must resolve
   against (store U batch) at the batch's FINAL STATE. Ordering inside a batch is irrelevant --
   there is no receipt-first vs entity-first, and the bootstrap pair {mint_receipt, entity} is one
   batch whose two references resolve against each other. Any failure rejects the WHOLE batch:
   nothing is written, and the commit_seq is not consumed.

2. commit_seq LIVES IN THE ENVELOPE, NEVER IN A RECORD (sec 2e). The frozen +38 bytes carry event
   time only; nothing in them carries ingestion order, and append-only permits a later batch to
   carry an earlier-dated record. So the STORE assigns a strictly increasing commit_seq per
   admitted batch and stores every record with the seq of the batch that admitted it. A record's
   own bytes are never touched to hold it -- that would be a contract change dressed as a ledger
   rule.

3. AN ANCHOR CUTS THE REPLAY SET BY commit_seq, TOTALLY AND DETERMINISTICALLY (sec 2e). All three
   anchor forms reduce to `commit_seq <= N`; publication and frontier anchors bind by looking up
   the batch that admitted the named record. A backfilled earlier-dated record is EXCLUDED from an
   anchor admitted before it and INCLUDED -- at its event-time position -- in one admitted after.
   The replay surface returns the anchor's commit_seq beside the estate so a reader can see which
   backfills it could not know about.

NOTE: WHAT A FALSE ACCEPT WOULD LOOK LIKE, so a reader can hunt it. (a) Resolution done record-by-record
as each is inserted rather than over the batch's final state -- the bootstrap pair then depends on
ORDER, and `L-02-forward-ref-within-batch` passes or fails by luck. (b) A dangling reference stored
without error: the observable that catches it is that admission REJECTS, so the arm's query never
runs; a resolver that merely logs would leave the store readable and the arm green. (c) commit_seq
assigned before validation, so a rejected batch consumes a number and the anchor arithmetic silently
shifts. Each is exercised by an arm rather than asserted here.
"""
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
ISCK = os.path.dirname(HERE)          # the ledger lives one level below the contract + design
SCHEMA_PATH = os.path.join(ISCK, "ISCK_CONTRACT.v0.schema.json")
DESIGN_PATH = os.path.join(ISCK, "WP3_LEDGER_DESIGN.md")

BS = chr(92)
ROW_SPLIT = re.compile('(?<!' + re.escape(BS) + ')' + re.escape('|'))
TICKED = re.compile('`([^`]+)`')
ID_SUFFIX = ("_id", "_serial")

# Reference-id prefixes, sec 2d: a value that PARSES as a record id starts with one of these.
ID_PREFIXES = ("ent:", "mat:", "matv:", "run:", "sf:", "sv:", "bind:", "ct:", "ctev:", "rel:",
               "br:", "obs:", "mr:", "mig:", "ce:", "lce:", "aep:", "bev:")

DERIVED_ONLY_FIELDS = ("superseded_by", "superseded_by_version")


class Rejected(Exception):
    """The ledger refused the write. The rule is named so an arm can say WHICH refusal it got."""

    def __init__(self, rule, reason):
        super().__init__("%s: %s" % (rule, reason))
        self.rule = rule
        self.reason = reason


def _load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


def primary_id_fields(schema=None):
    """record_type -> its primary id field, DERIVED from the schema, never typed.

    The primary id is the first id-ish property in the def's declaration order; every other id-ish
    property is a reference (sec 2d excludes primary ids by construction). The control below is the
    point: if the schema ever stops yielding exactly one required primary id per record type, this
    raises rather than guessing.
    """
    schema = schema or _load_schema()
    out = {}
    for _name, spec in (schema.get("$defs") or {}).items():
        props = spec.get("properties") or {}
        const = (props.get("record_type") or {}).get("const")
        if not const:
            continue
        ids = [p for p in props if p.endswith(ID_SUFFIX)]
        if not ids:
            raise RuntimeError("record type %s has no id-ish property" % const)
        if ids[0] not in (spec.get("required") or []):
            raise RuntimeError("primary id %s of %s is not required" % (ids[0], const))
        out[const] = ids[0]
    return out


def reference_fields():
    """(record, field) -> {policy, classes}, read from the design's sec 2d table beside this module.

    THE CLASS IS HALF THE RULE AND IT IS THE HALF A RESOLVER FORGETS. Sec 2d's STRICT reads "must
    resolve in (store U batch) at final state to a record OF THE NAMED CLASS". A resolver that only
    checks existence admits a binding whose `entity_serial` points at a materializer -- every
    reference resolves, nothing dangles, and the store is quietly wrong. The named class is column
    3; a union (an escaped-pipe list) is the whole allowed set, and "any record class" is an
    empty set meaning no constraint.
    """
    with open(DESIGN_PATH, "r", encoding="utf-8") as fh:
        text = fh.read()
    body = text.split("## 2d.")[1]
    cut = re.search(r'\n#{2,} ', body)
    body = body[:cut.start()] if cut else body
    out = {}
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ROW_SPLIT.split(line)]
        if len(cells) < 5:
            continue
        rec, fld = TICKED.findall(cells[1]), TICKED.findall(cells[2])
        if len(rec) == 1 and len(fld) == 1:
            policy = cells[4].split("(")[0].strip().strip("*").strip()
            classes = [c.split("[")[0].strip() for c in TICKED.findall(cells[3])]
            out[(rec[0], fld[0])] = {"policy": policy or "STRICT", "classes": classes}
    return out


def canonical(record):
    """Byte identity of a record. Sorted keys, LF, no spaces -- a digest needs its normalisation."""
    return json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")


class Store:
    """A single-file SQLite ledger. Fixtures only: the path is whatever the caller opens."""

    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript(
            "CREATE TABLE IF NOT EXISTS batches ("
            "  commit_seq INTEGER PRIMARY KEY AUTOINCREMENT, actor TEXT);"
            "CREATE TABLE IF NOT EXISTS records ("
            "  record_id TEXT PRIMARY KEY, record_type TEXT NOT NULL, body TEXT NOT NULL,"
            "  body_sha TEXT NOT NULL, commit_seq INTEGER NOT NULL);")
        self.db.commit()
        self.primary = primary_id_fields()
        self.refs = reference_fields()

    # -- reads -------------------------------------------------------------------------------
    def get(self, record_id):
        row = self.db.execute("SELECT body FROM records WHERE record_id=?", (record_id,)).fetchone()
        return json.loads(row[0]) if row else None

    def estate(self, upto=None):
        """Every record at or before an anchor's commit_seq. No anchor = the whole store."""
        if upto is None:
            rows = self.db.execute("SELECT body, commit_seq FROM records").fetchall()
        else:
            rows = self.db.execute("SELECT body, commit_seq FROM records WHERE commit_seq<=?",
                                   (upto,)).fetchall()
        return [(json.loads(b), s) for b, s in rows]

    def head_commit_seq(self):
        row = self.db.execute("SELECT MAX(commit_seq) FROM batches").fetchone()
        return row[0] or 0

    # -- the model ---------------------------------------------------------------------------
    def _primary_of(self, record):
        rt = record.get("record_type")
        if rt not in self.primary:
            raise Rejected("not-a-record", "record_type %r is not in the frozen catalog -- a "
                                           "projection is NOT a record (sec 2)" % rt)
        field = self.primary[rt]
        value = record.get(field)
        if not value:
            raise Rejected("no-primary-id", "%s has no %s" % (rt, field))
        return value

    def _reference_values(self, record):
        """Every (field, value, policy) this record asserts as a reference, per sec 2d.

        Sec 2d names three field SHAPES and a resolver that reads only the first silently ignores
        the other two -- a dangling reference inside an array is exactly the value nobody checks:
          `field`                 a scalar
          `field[]`               every item of a list       (consequence_refs, output_surface_ids)
          `container[].sub`       a sub-field of every item  (source_frontier.entries[].source_serial)
        The field name is kept VERBATIM from the table, because it is also the arm id's suffix.
        """
        rt = record.get("record_type")
        out = []
        for (rec, fld), spec in self.refs.items():
            if rec != rt:
                continue
            policy, classes = spec["policy"], spec["classes"]
            if "[]." in fld:
                container, sub = fld.split("[].", 1)
                for item in record.get(container) or []:
                    if isinstance(item, dict) and item.get(sub):
                        out.append((fld, item[sub], policy, classes))
                continue
            key = fld[:-2] if fld.endswith("[]") else fld
            if key not in record:
                continue
            value = record[key]
            for v in (value if isinstance(value, list) else [value]):
                if v:
                    out.append((fld, v, policy, classes))
        return out

    def delete(self, record_id):
        """There is no delete. Append-only is a property of the API, not a promise in a comment."""
        raise Rejected("L-03-delete", "the ledger has no delete: retention is append-only "
                                      "(sec 3 row 3); 'close' is an event, not a removal")

    def admit(self, records, actor=None):
        """Admit a batch ATOMICALLY. Returns its commit_seq. Raises Rejected, writing nothing."""
        if not isinstance(records, (list, tuple)) or not records:
            raise Rejected("empty-batch", "a batch is one or more records")

        # -- final state = store U batch, built BEFORE any check, so order cannot matter
        batch = {}
        for record in records:
            rid = self._primary_of(record)
            if rid in batch:
                raise Rejected("duplicate-in-batch", "%s appears twice in one batch" % rid)
            batch[rid] = record

        for rid, record in batch.items():
            stored = self.get(rid)

            # row 3 -- derived-only fields are refused on any write after creation
            if stored is not None:
                for field in DERIVED_ONLY_FIELDS:
                    if record.get(field) and not stored.get(field):
                        raise Rejected("L-03-%s-written" % field.replace("_", "-"),
                                       "%s is derived-only: it is a projection of the store, and "
                                       "populating it on a later write is a semantic mutation "
                                       "(sec 2b, sec 3 row 3)" % field)

            # row 3 -- in-place mutation vs idempotent rewrite
            if stored is not None and canonical(stored) != canonical(record):
                raise Rejected("L-03-inplace-mutation",
                               "%s already exists with different bytes: append-only forbids "
                               "in-place semantic mutation (sec 3 row 3)" % rid)

            # row 1 -- global serial uniqueness across batches AND fabrics
            if record.get("record_type") == "mint_receipt":
                serial = record.get("entity_serial")
                for other, seq in self.estate():
                    if (other.get("record_type") == "mint_receipt"
                            and other.get("entity_serial") == serial
                            and self._primary_of(other) != rid):
                        raise Rejected("L-01-dup-serial",
                                       "serial %s is already minted by receipt %s (commit_seq %d);"
                                       " a second fabric must mint `provisional` and reconcile by "
                                       "relation, never re-mint (sec 3 row 1)"
                                       % (serial, self._primary_of(other), seq))

            # row 6 (admission half) -- an entity needs a receipt in (store U batch)
            if record.get("record_type") == "entity":
                serial = rid
                receipted = any(
                    r.get("record_type") == "mint_receipt" and r.get("entity_serial") == serial
                    for r in list(batch.values()) + [o for o, _s in self.estate()])
                if not receipted:
                    raise Rejected("L-06-entity-without-receipt",
                                   "entity %s has no mint_receipt in (store U batch) at final "
                                   "state (sec 2c, sec 3 row 6)" % serial)

            # row 2 -- every reference resolves at FINAL STATE
            for field, value, policy, classes in self._reference_values(record):
                if policy.startswith("EXTERNAL"):
                    continue
                parses = str(value).startswith(ID_PREFIXES)
                if policy.startswith("PARSE-STRICT") and not parses:
                    continue                       # stored OPAQUE (migration), sec 2d
                if not parses and not policy.startswith("STRICT"):
                    continue
                target = batch.get(value) or self.get(value)
                if target is None:
                    raise Rejected("L-02-unresolved-%s.%s" % (record["record_type"], field),
                                   "%s does not resolve in (store U batch) at final state "
                                   "(sec 2d policy %s)" % (value, policy))
                if classes and target.get("record_type") not in classes:
                    raise Rejected("L-02-unresolved-%s.%s" % (record["record_type"], field),
                                   "%s resolves to a %s, but sec 2d names %s: a reference that "
                                   "resolves to the WRONG CLASS is not resolved -- it is a "
                                   "dangling reference wearing a valid id"
                                   % (value, target.get("record_type"), " | ".join(classes)))

        # -- commit_seq is consumed ONLY after every check passes
        cur = self.db.execute("INSERT INTO batches (actor) VALUES (?)", (actor,))
        seq = cur.lastrowid
        for rid, record in batch.items():
            blob = canonical(record)
            self.db.execute(
                "INSERT OR IGNORE INTO records (record_id, record_type, body, body_sha, commit_seq)"
                " VALUES (?,?,?,?,?)",
                (rid, record["record_type"], blob.decode("utf-8"),
                 hashlib.sha256(blob).hexdigest(), seq))
        self.db.commit()
        return seq

    # -- anchors and replay (sec 2e) ---------------------------------------------------------
    def anchor(self, kind, value):
        """Bind an anchor to a commit_seq. Every form reduces to `commit_seq <= N`."""
        if kind == "commit_seq":
            n = int(value)
            if n < 0 or n > self.head_commit_seq():
                raise Rejected("L-12-anchor-unbindable",
                               "commit_seq %s is not an admitted batch (head is %d)"
                               % (value, self.head_commit_seq()))
            return n
        wanted = {"publication": "surface_version", "frontier": "source_frontier"}.get(kind)
        if wanted is None:
            raise Rejected("L-12-anchor-unknown-kind", "no anchor kind %r (sec 2e names three)"
                           % kind)
        for record, seq in self.estate():
            if record.get("record_type") != wanted or self._primary_of(record) != value:
                continue
            if kind == "publication" and record.get("publication_state") != "published":
                raise Rejected("L-12-replay-publication",
                               "surface_version %s is not published: an `as_of publication` "
                               "anchor binds the batch that admitted a PUBLISHED version "
                               "(sec 2e)" % value)
            return seq
        raise Rejected("L-12-replay-%s" % kind,
                       "%s %s was never admitted, so it names no commit_seq and the replay set "
                       "cannot be cut; a replay whose anchor differs from the recorded state is "
                       "refused rather than answered (sec 2e, sec 3 row 12)" % (wanted, value))

    def replay(self, kind, value):
        """The estate as of an anchor, WITH the anchor's commit_seq beside it (sec 5.6)."""
        seq = self.anchor(kind, value)
        records = [r for r, _s in self.estate(upto=seq)]
        records.sort(key=lambda r: (event_time(r) or "", self._primary_of(r)))
        return {"anchor_kind": kind, "anchor_value": value, "anchor_commit_seq": seq,
                "estate": records, "counted": len(records)}


    def replay_expecting(self, kind, value, expect_ids):
        """A replay CLAIM, checked against the recorded state at that commit_seq.

        Row 12's refusal is "a replay as of an anchor that DIFFERS from the state recorded at that
        commit_seq". A replay is a read, so the refusable act is the CLAIM about it: a caller that
        asserts a record is in the anchored estate when the anchor predates its admission is
        refused rather than quietly answered. This is what makes the backfill rule observable --
        without it, "excluded" and "the caller never looked" are the same picture.
        """
        result = self.replay(kind, value)
        have = {self._primary_of(r) for r in result["estate"]}
        missing = [i for i in expect_ids if i not in have]
        if missing:
            raise Rejected("L-12-replay-mismatch",
                           "the claim names %s, which is NOT in the estate recorded at "
                           "commit_seq %d (a backfill admitted after an anchor is excluded from "
                           "it -- sec 2e)" % (", ".join(missing), result["anchor_commit_seq"]))
        return result


EVENT_TIME_FIELDS = ("occurred_at", "asserted_at", "minted_at", "published_at", "observed_at")


def event_time(record):
    for field in EVENT_TIME_FIELDS:
        if record.get(field):
            return record[field]
    return None
