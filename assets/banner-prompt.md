# Banner generation record

## Revision 3: retitled for Always-On Personal Intelligence

- Final asset: `banner.png`
- Tool: Codex CLI 0.154.0, built-in image generation in edit mode
- Date: 2026-10-05
- Dimensions: 2172 × 724 pixels (3:1)
- Edit target: the Revision 2 `banner.png`; only the three title lines changed
- Title: "Always-On Personal Intelligence:" / "A Roadmap Towards" / "Continuing, Self-Evolving Loops", following the survey's current title
- Inspection: one attempt; every word, the colon, the comma, and both hyphens visually checked; no old text remains and nothing overlaps the drawing
- Processing: copied the generated PNG without raster editing

### Exact revision prompt

```text
Use case: text-localization.
Asset type: research reading-list README banner.
Input image: banner.png is the EDIT TARGET, not a style reference.
Edit this existing image. Change ONLY the three title lines at the upper center. Preserve the illustration, composition, all objects, their positions, colors, shapes, and the warm ivory background as closely as possible. Keep the friendly hand-drawn scientific cartoon style, the person with smart glasses and an earbud at the left, the open notebook, memory cards and laptop in the center, the domestic robot and person at a computer on the right, the looping arrow, and muted sage, dusty blue, clay pink and ochre palette. Keep the existing ochre underline.
Completely remove the old title text "Always-On Personal AI:", "A Roadmap towards a", and "Continuing and Self-Evolving Loop".
Replace it with exactly these three centered lines, without quotation marks:
Line 1: Always-On Personal Intelligence:
Line 2: A Roadmap Towards
Line 3: Continuing, Self-Evolving Loops
Typography: Line 1 large bold clean lettering matching the original first line's style, weight and dark navy color. Fit the longer line on ONE line within the clear upper-center space, reducing lettering size as needed while retaining prominent, legible weight. Lines 2 and 3 smaller tasteful cursive handwriting matching the original subtitle. Keep all three lines centered, with clear space around them, without overlap with any drawing. Title must be clearly legible at 850 pixels display width.
Exact spelling and punctuation are critical: "Always-On" has a hyphen; "Personal"; "Intelligence:" ends with a colon; "A Roadmap Towards" has capital A, R and T and no trailing "a"; "Continuing," ends with a comma; "Self-Evolving" has a hyphen and capital S and E; "Loops" is plural with capital L. Do not duplicate or omit words.
Output one wide 3:1 landscape PNG, preferably 2172 x 724 pixels. Preserve full framing. No other text, labels, logos, badges, numbers or watermarks. Only the title lettering may change.
```

## Revision 2 — paper illustration style and complete title

- Final asset: `banner.png`
- Tool: built-in `image_gen.imagegen` in edit mode
- Date: 2026-09-15
- Dimensions: 2172 × 724 pixels (3:1)
- Edit target: `banner.png`
- Style reference: `survey-framework.png`
- Motif reference: manuscript `fig/domain_icons_v1/glasses.png`
- Inspection: full title, colon, both hyphens, `towards`, and all words in the cursive subtitle visually checked.
- Processing: copied generated PNG without raster editing.

### Exact revision prompt

```text
Use case: style-transfer.
Asset type: final illustrated GitHub README banner, approximately 3:1 landscape aspect ratio, ideally 2400 × 800.
Input images and roles: Image 1 (existing banner.png) is the EDIT TARGET: replace its watercolor/pastoral style and its old subtitle. Image 2 (survey-framework.png) is the PRIMARY STYLE REFERENCE: match the friendly hand-drawn scientific cartoon illustrations in its application scenes and its sensing, memory, and action objects. Image 3 (glasses.png) is only a simple sensing motif reference.
Primary request: redesign the banner to look like it belongs to the reference research paper. Preserve the overall purpose of an airy scholarly banner about ongoing personal assistance, but completely redraw the picture with clean bold dark navy/charcoal outlines, lightly hand-drawn shapes, restrained soft flat color fills and only slight pencil shading. Use the original banner merely for its wide composition and title prominence. Remove the detailed outdoor city/travel scenery, photographic watercolor textures and romantic pastoral mood.
Exact complete title, preserving every word and both hyphens: "Always-On Personal AI: A Roadmap towards a Continuing and Self-Evolving Loop".
Typography layout: at the upper center show line 1, exact text "Always-On Personal AI:" in large, bold, clean, clearly readable lettering inspired by the strong scholarly headings of the survey figure. Under it show line 2 exact text "A Roadmap towards a" and line 3 exact text "Continuing and Self-Evolving Loop". These two subtitle lines must be noticeably smaller tasteful cursive handwriting, clearly connected handwritten/cursive strokes, elegant but highly readable, without excessive flourishes. Use dark navy or charcoal for all title text. The title must remain legible at 850 pixels display width. Spell "Self-Evolving" with the hyphen, and spell "towards" with its final s. Do not shorten, replace or omit any word. Do not include the old "Sensing · Memory · Action" subtitle.
Illustration composition: light warm white/ivory background with abundant negative space around all title lines. Along the lower band and outer sides, create a coherent little research illustration panorama: at left a friendly cartoon person wearing smart glasses and a small earbud; lower center a compact open personal notebook with an inset small memory-card stack, paired with a simple laptop showing abstract UI cards; at right a friendly compact domestic assistant robot alongside a person at a computer workspace. Connect the motifs with one restrained graceful looping arrow or ribbon to convey continuing observation, personal memory and useful action. The flow should feel like a small looping journey through everyday support, never intersecting letters. Faces, clothes, objects and outlines should closely match the hand-drawn cartoon character style in the application scenes of the paper's framework image. Include only a few large readable objects.
Color palette: muted sage green, soft dusty blue, blush/pale clay pink, warm ochre yellow, cream, and dark navy outlines. Soft flat fills with modest hand-rendered shading. Keep these colors consistent across motifs.
Invariants: one finished wide banner; all exact title words included; 3:1 or close landscape; no reproduction of the dense diagram, framework labels or logos. Avoid tiny labels, category names, badges, numbered steps, statistics, watermarks, neon, gradients, glowing effects, thin faint watercolor strokes, ornate flourishes, clutter, detailed landscapes, or decorative borders. The full manuscript title and the smaller cursive subtitle treatment are the most important requirements.
```
