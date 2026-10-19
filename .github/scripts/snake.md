# Contribution snake maintenance

The workflow runs daily at 00:23 UTC, on relevant source changes, or manually.
It reads GitHub's contribution calendar using the repository's ephemeral
`GITHUB_TOKEN`; no PAT, extra secret, or account setting is needed. Only the
generation job has `contents: write`, to publish two SVG files on `output`.
It retains existing output files and appends commits without force pushes.
Dates, counts, and contribution levels are those returned by GitHub. Private
contributions can differ from the signed-in profile because token visibility
and the user's private-contribution settings affect the calendar.

| Theme | Empty | Level 1 | Level 2 | Level 3 | Level 4 |
| --- | --- | --- | --- | --- | --- |
| Light | #EBEEF5 | #C6D2FF | #9AB0FF | #6C8DFF | #4565D6 |
| Dark | #1B2233 | #354779 | #5068BC | #6C8DFF | #A5B9FF |

The head is #D21F3C; all three body segments are #E06666. Light mode uses
increasingly deep blues; dark mode uses increasingly luminous blues. Empty
cells stay subdued. README's picture element selects the appropriate SVG.

## Why s0 is the head

The action is pinned to Platane/snk commit
`d8f6715049803e982ee5ff501b6b9b7d5deeb09b` (v3, version 3.5.0), including its
prebuilt SVG bundle. It supports `color_snake`, not a separate head option.

- [types/snake.ts](https://github.com/Platane/snk/blob/d8f6715049803e982ee5ff501b6b9b7d5deeb09b/packages/types/snake.ts):
  `getHeadX/Y` reads coordinate pair zero. `nextSnake` advances that pair and
  shifts each body segment to its predecessor's position.
- [svg-creator/snake.ts](https://github.com/Platane/snk/blob/d8f6715049803e982ee5ff501b6b9b7d5deeb09b/packages/svg-creator/snake.ts):
  the same indices become `s0` through `s3`, each with matching keyframes.
- [generator](https://github.com/Platane/snk/blob/d8f6715049803e982ee5ff501b6b9b7d5deeb09b/packages/generate-snake-animation/generateSnakeAnimation.ts):
  selects `snake4` and computes the route from the returned contribution grid.

`style_snake.py` validates this contract, the animation bindings, body color,
and all five palette entries before appending exactly `.s.s0{fill:#D21F3C}`.
It does not reserialize XML or modify grid rectangles, geometry, or keyframes.
Tests cover reordered elements, preservation, idempotence, missing/duplicate
heads, broken animation, wrong colors, and unexpected overrides. When updating
the action pin, recheck both TypeScript and `svg-only/dist/578.index.js` and
visually verify several frames of both actual generated SVGs.

## Dependency review

- actions/checkout is pinned to `11d5960a326750d5838078e36cf38b85af677262`;
  its [LICENSE](https://github.com/actions/checkout/blob/11d5960a326750d5838078e36cf38b85af677262/LICENSE)
  is MIT.
- The inspected Platane/snk commit has no root license file or package license
  declaration. Its README explicitly documents this GitHub Actions use. We
  invoke the published action and retain its generated attribution; no upstream
  source is copied into this repository. Do not assume it is MIT licensed.
- Publication and postprocessing use Git and Python's standard library.

Reference layout: [lidge-jun's workflow](https://github.com/lidge-jun/lidge-jun/blob/main/.github/workflows/snake.yml).
