#!/usr/bin/env python3
"""Convert kosmiczny-strzelec.bas into a ZX Spectrum .tap file (BASIC program, autostart at line 10)."""
import re
from pathlib import Path

TOKENS = {
    "RND": 165, "INKEY$": 166, "AT": 172, "INT": 186, "AND": 198,
    "THEN": 203, "TO": 204, "BEEP": 215, "INK": 217, "PAPER": 218,
    "BORDER": 231, "DIM": 233, "REM": 234, "FOR": 235, "GOTO": 236,
    "GOSUB": 237, "LET": 241, "PAUSE": 242, "NEXT": 243, "PRINT": 245,
    "RUN": 247, "IF": 250, "CLS": 251, "RETURN": 254,
}
INV = {v: k for k, v in TOKENS.items()}
KEYWORDS = sorted(TOKENS, key=len, reverse=True)
KW_RE = re.compile("(" + "|".join(re.escape(k) for k in KEYWORDS) + ")(?![A-Za-z0-9])")


def tokenize_line(text):
    out = bytearray()
    i = 0
    while i < len(text):
        c = text[i]
        if c == '"':
            j = text.find('"', i + 1)
            j = len(text) if j == -1 else j
            out += text[i:j + 1].encode("ascii")
            i = j + 1
            continue
        if i == 0 or not (text[i - 1].isalnum() or text[i - 1] == "$"):
            m = KW_RE.match(text, i)
            if m:
                kw = m.group(1)
                out.append(TOKENS[kw])
                i = m.end()
                if kw == "REM":
                    out += text[i:].encode("ascii")
                    i = len(text)
                continue
        out += c.encode("ascii")
        i += 1
    return bytes(out)


def parse_program(src):
    lines = []
    for raw in src.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        num, text = raw.split(None, 1)
        lines.append((int(num), tokenize_line(text)))
    return lines


def block(payload_with_flag):
    chk = 0
    for b in payload_with_flag:
        chk ^= b
    body = payload_with_flag + bytes([chk])
    return len(body).to_bytes(2, "little") + body


def build_tap(lines, name, autostart):
    prog = bytearray()
    for num, text in lines:
        rec = text + b"\x0d"
        prog += num.to_bytes(2, "big") + len(rec).to_bytes(2, "little") + rec
    header_payload = (
        b"\x00\x00"
        + name.encode("ascii").ljust(10, b" ")[:10]
        + len(prog).to_bytes(2, "little")
        + autostart.to_bytes(2, "little")
        + len(prog).to_bytes(2, "little")
    )
    return block(header_payload) + block(b"\xff" + bytes(prog))


def detokenize(data):
    return "".join(INV.get(b, chr(b)) for b in data)


def verify(tap, lines):
    n = int.from_bytes(tap[0:2], "little")
    hdr = tap[2:2 + n - 1]
    assert hdr[0] == 0x00 and hdr[1] == 0x00, "header flag/type"
    chk = 0
    for b in tap[2:2 + n]:
        chk ^= b
    assert chk == 0, "header checksum"
    assert int.from_bytes(hdr[12:14], "little") == int.from_bytes(hdr[16:18], "little"), "param1/param2"
    off = 2 + n
    n2 = int.from_bytes(tap[off:off + 2], "little")
    blk = tap[off + 2:off + 2 + n2 - 1]
    assert blk[0] == 0xFF, "data block flag"
    chk = 0
    for b in tap[off + 2:off + 2 + n2]:
        chk ^= b
    assert chk == 0, "checksum"
    prog = blk[1:]
    pos = 0
    got = []
    while pos < len(prog):
        num = int.from_bytes(prog[pos:pos + 2], "big")
        ln = int.from_bytes(prog[pos + 2:pos + 4], "little")
        got.append((num, detokenize(prog[pos + 4:pos + 4 + ln - 1])))
        pos += 4 + ln
    assert pos == len(prog), "trailing bytes in program"
    assert len(got) == len(lines), "line count"
    for (gn, gt), (en, et) in zip(got, lines):
        assert gn == en, (gn, en)
        assert gt.replace(" ", "") == detokenize(et).replace(" ", ""), (gt, et)
    return len(got)


def main():
    here = Path(__file__).parent
    src = (here / "kosmiczny-strzelec.bas").read_text(encoding="ascii")
    lines = parse_program(src)
    tap = build_tap(lines, "strzelec", autostart=10)
    out = here / "kosmiczny-strzelec.tap"
    out.write_bytes(tap)
    n = verify(tap, lines)
    print(f"wrote {out.name} ({len(tap)} bytes, {n} lines, verify OK)")


if __name__ == "__main__":
    main()
