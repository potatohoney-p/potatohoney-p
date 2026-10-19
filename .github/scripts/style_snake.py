"""Style only the verified leading segment of the pinned Platane/snk SVG."""

from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

HEAD = "#D21F3C"
BODY = "#E06666"
PALETTES = {
    "github-snake.svg": ("#EBEEF5", "#C6D2FF", "#9AB0FF", "#6C8DFF", "#4565D6"),
    "github-snake-dark.svg": ("#1B2233", "#354779", "#5068BC", "#6C8DFF", "#A5B9FF"),
}
HEAD_RULE = f".s.s0{{fill:{HEAD}}}"
NS = "{http://www.w3.org/2000/svg}"


def style_svg(svg: str, palette: tuple[str, ...]) -> str:
    """Fail closed on a changed generator contract; preserve all original bytes.

    At snk d8f6715049803e982ee5ff501b6b9b7d5deeb09b:
    types/snake.ts getHeadX/Y read the first coordinate pair; nextSnake moves
    that pair and shifts the body. svg-creator/snake.ts maps those same indices
    to s0, s1, ... and their respective motion keyframes. Thus s0 is the head,
    irrespective of document order, position, direction, or segment size.
    """
    root = ET.fromstring(svg)
    if root.tag != NS + "svg":
        raise ValueError("Expected a namespaced SVG root")
    styles = list(root.iter(NS + "style"))
    if len(styles) != 1 or svg.count("</style>") != 1:
        raise ValueError("Expected exactly one generator style block")
    css = styles[0].text or ""
    if "@media" in css:
        raise ValueError("Expected separate light and dark palettes, without overrides")
    variables = dict(re.findall(r"(--[a-z0-9]+)\s*:\s*([^;}]+)", css))
    expected = {"--cs": BODY, "--ce": palette[0]}
    expected.update({f"--c{i}": color for i, color in enumerate(palette)})
    if any(variables.get(key, "").strip().upper() != value for key, value in expected.items()):
        raise ValueError("Generator body or contribution palette does not match")
    segments = []
    for element in root.iter():
        classes = element.get("class", "").split()
        if "s" in classes:
            if element.tag != NS + "rect" or "style" in element.attrib or "fill" in element.attrib:
                raise ValueError("Unexpected snake segment markup")
            ids = [name for name in classes if re.fullmatch(r"s\d+", name)]
            if len(ids) != 1:
                raise ValueError("Expected one motion identity per snake segment")
            segments.append(ids[0])
    # The pinned action uses snake4. Never guess after an upstream format change.
    if sorted(segments) != ["s0", "s1", "s2", "s3"]:
        raise ValueError("Expected exactly the four pinned snake segments")
    if not re.search(r"\.s\s*\{[^}]*fill:\s*var\(--cs\)", css):
        raise ValueError("Expected shared body color")
    for segment in segments:
        if not re.search(rf"@keyframes\s+{segment}\s*\{{", css):
            raise ValueError(f"Missing animation for {segment}")
        if not re.search(rf"\.s\.{segment}\s*\{{[^}}]*animation-name:\s*{segment}(?:[;}}])", css):
            raise ValueError(f"Missing motion binding for {segment}")
    if HEAD_RULE in css:
        if css.count(HEAD_RULE) != 1 or not css.endswith(HEAD_RULE):
            raise ValueError("Unexpected duplicate head styling")
        return svg
    return svg.replace("</style>", HEAD_RULE + "</style>", 1)


def main(directory: Path) -> None:
    # Validate both before writing either, so a failed check cannot publish a pair
    # with mixed styles. read_bytes avoids changing newline bytes.
    outputs = [(directory / name, style_svg((directory / name).read_bytes().decode("utf-8"), palette))
               for name, palette in PALETTES.items()]
    for path, svg in outputs:
        path.write_bytes(svg.encode("utf-8"))
        print(f"Verified {path.name}: one crimson head, three rose body segments, five blue levels")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "dist"))
