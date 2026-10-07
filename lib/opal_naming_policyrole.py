#!/usr/bin/env python3
"""opal_naming_policyrole -- an inline policy takes its role's system (LGIC_BLANKFIX BF-e-2).

An inline policy (aws_iam_role_policy) belongs to the role it attaches to, so the system of its name is the system of that
role's name. Two policies of one root may share a name on different roles, so the key is (name, type, parent role): this module
keys on (name, where), where `where` is the file:line of the policy's resource block, the same string
opal_naming.census_tf_names() reports for it.

  policy_roles(root)               one dict per aws_iam_role_policy block of the root:
                                   name, where, role_ref, role_name, role_system, basis
  system_for(root, name, where)    the row for that declaration, or None

Command:
  python lib/opal_naming_policyrole.py root ROOT

role_system is the first hyphen-separated token of the canonical form of the role's own name (opal_naming.grade(name,
"IAM_ROLE")), None with a plain-words basis when the role cannot be resolved, grading raises, or the canonical carries a
{system} blank. Python 3.9 syntax; stdlib only; ASCII only.
"""
from __future__ import annotations

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import opal_naming  # noqa: E402

REPO = opal_naming.REPO
_ROLE_REF_RE = re.compile(r"^aws_iam_role\.([A-Za-z0-9_-]+)\.(?:name|id)$")
_POLICY_HEADER_RE = re.compile(r'^[ \t]*resource[ \t]+"aws_iam_role_policy"[ \t]+"[^"\n]*"[ \t]*\{', re.M)
_CACHE = {}


def _abs_root(root):
    r = str(root)
    return r if os.path.isabs(r) else os.path.join(REPO, *r.replace("\\", "/").split("/"))


def _rel(path):
    """Repo-relative forward-slash path when the file sits in the repository, else the path as given."""
    a = os.path.abspath(path)
    repo = os.path.abspath(REPO)
    if a == repo or a.startswith(repo + os.sep):
        return os.path.relpath(a, repo).replace("\\", "/")
    return a.replace("\\", "/")


def _tf_files(root):
    out = []
    for d, dirs, files in os.walk(_abs_root(root)):
        dirs[:] = sorted(x for x in dirs if x != ".terraform")
        out.extend(os.path.join(d, f) for f in sorted(files) if f.endswith(".tf"))
    return sorted(out)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().replace("\r\n", "\n")


def _blocks(root):
    """(role resources {label: literal name or None}, policy blocks [(where, name, role_ref)]) of the root's .tf files."""
    roles, pols = {}, []
    for path in _tf_files(root):
        text = _read(path)
        rel = _rel(path)
        for it in opal_naming._tf_items(text, 0, len(text)):
            if it[0] != "block" or it[1] != "resource" or len(it[2]) != 2:
                continue
            attrs = {a[1]: a for a in opal_naming._tf_items(text, it[4], it[5]) if a[0] == "attr"}
            if it[2][0] == "aws_iam_role":
                roles[it[2][1]] = opal_naming._tf_literal(attrs["name"][3]) if "name" in attrs else None
            elif it[2][0] == "aws_iam_role_policy":
                where = "%s:%d" % (rel, opal_naming._line_of(text, it[3]))
                name = opal_naming._tf_literal(attrs["name"][3]) if "name" in attrs else None
                ref = attrs["role"][3].strip() if "role" in attrs else None
                pols.append((where, name, ref))
    return roles, pols


def _role_system(role_ref, roles):
    """(role_name, role_system, basis) for a role expression."""
    if role_ref is None:
        return None, None, "the policy has no role attribute"
    m = _ROLE_REF_RE.match(role_ref)
    if not m:
        return None, None, "the role is %s, not a reference of the form aws_iam_role.X.name or .id" % role_ref
    label = m.group(1)
    if label not in roles:
        return None, None, "aws_iam_role.%s is not a resource of this root" % label
    rname = roles[label]
    if not rname:
        return None, None, "aws_iam_role.%s has no name that is one literal" % label
    try:
        verdict, canon = opal_naming.grade(rname, "IAM_ROLE")
    except Exception as exc:  # grade raises RaiseDefect for a name the rule cannot place
        return rname, None, "grading the role name %s raised: %s" % (rname, str(exc)[:160])
    if not canon:
        return rname, None, "the role name %s is %s: no canonical form" % (rname, verdict)
    first = canon.split("-", 1)[0]
    if "{" in first or "}" in first:
        return rname, None, "the canonical form %s of role %s carries a blank for the system" % (canon, rname)
    return rname, first, "system slot of %s, the canonical form of role %s (%s)" % (canon, rname, verdict)


def policy_roles(root):
    roles, pols = _blocks(root)
    out = []
    for where, name, ref in pols:
        rname, rsys, basis = _role_system(ref, roles)
        out.append({"name": name, "where": where, "role_ref": ref, "role_name": rname, "role_system": rsys, "basis": basis})
    return out


def system_for(root, name, where):
    key = (_abs_root(root), name, where)
    if "rows" not in _CACHE or _CACHE["rows"][0] != key[0]:
        _CACHE["rows"] = (key[0], policy_roles(root))
    for row in _CACHE["rows"][1]:
        if row["name"] == name and row["where"] == where:
            return row
    return None


def text_count(root):
    """The count of aws_iam_role_policy resource headers by plain text, independent of the block parser."""
    return sum(len(_POLICY_HEADER_RE.findall(_read(p))) for p in _tf_files(root))


def _main(argv):
    if len(argv) != 3 or argv[1] != "root":
        print("usage: python lib/opal_naming_policyrole.py root ROOT")
        return 2
    root = argv[2]
    rows = policy_roles(root)
    for r in rows:
        print("%s %s role=%s system=%s  [%s]  %s" % (r["name"], r["role_ref"], r["role_name"], r["role_system"], r["where"],
                                                    r["basis"]))
    n = len(rows)
    res = sum(1 for r in rows if r["role_system"])
    unres = n - res
    indep = text_count(root)
    ok = n == indep and res + unres == n
    print("POLICYROLE-ROOT ok=%s root=%s policies=%d resolved=%d unresolved=%d" % (ok, argv[2].replace("\\", "/"), n, res, unres))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
