import unittest
from style_snake import BODY, HEAD_RULE, PALETTES, style_svg


def fixture(palette, order=(2, 0, 3, 1)):
    variables = f"--cs:{BODY};--ce:{palette[0]};" + "".join(
        f"--c{i}:{color};" for i, color in enumerate(palette))
    css = ":root{" + variables + "}.s{fill:var(--cs);animation:none linear 2000ms infinite}"
    for i in range(4):
        css += f"@keyframes s{i}{{0%{{transform:translate({i * 16}px,0px)}}100%{{transform:translate({i * 16 + 16}px,0px)}}}}"
        css += f".s.s{i}{{transform:translate({i * 16}px,0px);animation-name:s{i}}}"
    rects = '<rect class="c s10" x="2" y="2"/>'
    rects += "".join(f'<rect class="s{i} s" width="12" height="12"/>' for i in order)
    return f'<svg xmlns="http://www.w3.org/2000/svg"><style>{css}</style>{rects}</svg>'


class StyleSnakeTests(unittest.TestCase):
    def test_only_adds_head_rule_preserving_geometry_grid_and_animation_bytes(self):
        for palette in PALETTES.values():
            original = fixture(palette)
            result = style_svg(original, palette)
            self.assertEqual(result.replace(HEAD_RULE, ""), original)
            self.assertEqual(result.count(HEAD_RULE), 1)
            self.assertEqual(style_svg(result, palette), result)

    def test_rejects_missing_duplicate_or_renamed_head(self):
        palette = PALETTES["github-snake.svg"]
        for order in [(1, 2, 3), (0, 0, 1, 2, 3), (10, 1, 2, 3)]:
            with self.assertRaises(ValueError):
                style_svg(fixture(palette, order), palette)

    def test_rejects_broken_motion_wrong_palette_and_style_overrides(self):
        palette = PALETTES["github-snake.svg"]
        svg = fixture(palette)
        for broken in [svg.replace("@keyframes s0", "@keyframes gone"),
                       svg.replace("animation-name:s0", "animation-name:s1"),
                       svg.replace(BODY, "purple"),
                       svg.replace(palette[3], "green"),
                       svg.replace('class="s0 s"', 'class="s0 s" fill="green"'),
                       svg.replace("</style>", "@media(prefers-color-scheme:dark){}</style>"),
                       svg.replace("</svg>", "<style></style></svg>")]:
            with self.assertRaises(ValueError):
                style_svg(broken, palette)


if __name__ == "__main__":
    unittest.main()
