# Better Design Evaluation

This file is binding. Read all of it before you design or build any interface,
and again before you ship. Tell the user you have read it and will audit the
finished work against every point; then do exactly that, on the rendered
result, and fix every failure before calling anything done.

Everything here is a default. A specific, unambiguous instruction from the
user overrides any rule below: their direction wins, 100%. Absent that, follow
this file over your instincts.

Slop is generic, low-effort, look-the-same AI output. The cure is making real
choices. The sections below cover the recognizable defaults (components,
copy and labels, shadows and glass, color, type, layout, motion), the
execution failures that read as broken, mobile screens, why dodging the list
is not design, what premium actually is, how a signature gets made, and how
to handle a redesign.

## Component and decoration tells

- **Pill / eyebrow badge.** The small capsule above a hero headline: tiny icon
  plus short text. Default hero decoration.
- **Glowy pill buttons.** Fully rounded, gradient-filled, with a soft glow or
  blurred drop shadow underneath. The blurred under-shadow on buttons and
  cards is a signature tell.
- **The default CTA pair.** A gradient-filled primary with dark text, a
  trailing arrow icon and a glow, beside an outlined ghost secondary ("See how
  it works"). The preset recurs even when the colors change; style buttons
  with intent.
- **Oversized icon in a colored tile.** One big icon centered in a filled
  rounded square or circle as a hero visual or feature bullet.
- **Any icon or logo with a box behind it.** The rule behind the tile: an
  icon, brand mark, social glyph or integration logo parked on a filled or
  bordered container reads as a component kit, not a designed mark. Strip the
  container; get separation from the mark's own weight, color and spacing.
- **Lucide, and any uniform icon pack.** lucide-react is the default icon
  library: clean thin-stroke SVG line icons (Sparkles, Coffee, MapPin), no
  brand logos, browsable at lucide.dev. The uniform thin-stroke look on every
  project is the giveaway.
- **Redrawn line icons, and the sun-moon toggle.** Hand-drawing the usual
  icon-pack shapes (document with checkmark, shield with tick, linked circles)
  does not make them yours. Bespoke iconography needs a real point of view: an
  unusual construction, an invented detail, a weight that belongs to the
  brand. If an icon could sit on any other product unchanged, it is slop. The
  sliding sun-moon theme pill is the stock switch; a theme toggle can be
  almost anything else.
- **The kitchen-sink card.** One card stacking icon-in-tile, category pill,
  tag pills, hairline divider, big price and a glowy button. No piece is
  wrong; the pile is the clearest slop signature there is.
- **Fake macOS / app window mockup.** A CSS "product screenshot": red/yellow/
  green traffic-light dots, dark panel, mock kanban or avatars inside.
  Standard hero filler. (A fully populated, real product UI is the premium
  opposite; see field notes.)
- **The fake code-snippet window.** Traffic lights, a `quickstart.ts` tab, a
  toy SDK call, purple-keyword syntax colors, JetBrains Mono. One canned unit.
- **Gradient pill with icon and text.** Rounded box or pill, blue-purple
  gradient fill, small icon, short (often uppercase) label. The worst stack.
- **Testimonial / quote card.** Big quote-mark icon, centered quote, avatar
  with name and job title, a fake metric ("velocity jumped 32%"). Sibling
  tell: decorative oversized quote marks around any line. If a line needs
  emphasis, give it type and space, not ornamental quotes.
- **Gradient-circle initials avatar.** Two letters on a gradient circle
  standing in for a photo. Worse when the gradient is blue-purple.
- **Logo lockup.** An icon in a small gradient squircle beside the name in a
  generic geometric font: the instant made-by-AI logo. Its luxury twin is the
  letterspaced all-caps serif wordmark (usually Cormorant) as the whole brand.
- **Missing or faked logos.** Real recognizable marks (a social row, a "works
  with" strip, a customer wall) add legitimacy where warranted, and leaving
  them out can read thin. Inventing logos or faking customers is worse. If
  marks are not needed, use none; if they are, use the real SVGs from official
  sources, one size, one quiet treatment.
- **Floating tag pinned to an image.** The little info chip ("28°C & clear")
  stuck to a corner of a visual to make it feel alive. Same family: any pill
  or label overlaid on a photo ("Plate · Brand", "Field notes - journal"),
  and the fake photo credit under a stock image ("Field study no. 12 · Ines
  Caetano", "Frame XII · 35mm"). Let the image stand alone or caption it
  below in one plain line. Credit only a real photographer for a real photo.
- **Locale, time and weather strips.** "LIS 14:23 · 18°C" in the nav,
  "Lisbon, working with founders" in the hero, a timezone row in the footer.
  Agency-portfolio decoration. Allowed only when place is the product (a
  venue, a travel brand, a studio whose timezones matter). One contact
  address in the footer is fine.
- **Accent-bar card.** A plain box with one straight bright line down an edge
  to "add interest". (The premium version invents the geometry; see bespoke
  geometry below.)
- **Hairline light border on every box.** The faint 1px light outline (plus
  soft inner highlight) as default card styling. (Premium: self-colored
  borders, below.)
- **Countdown timer.** DAYS / HRS / MIN / SEC boxes faking urgency. Its
  siblings: the live-stock counter ("Reservation 412 of 800") and the
  version stamp. "V0.6", "BETA", "INVITE-ONLY PREVIEW" as a hero eyebrow is
  allowed only when the brief is a launch; "v1.4.2", "Build 0048", "last
  sync 4s ago · main" in a marketing footer or inside a fake screenshot is a
  devtool fixture pasted onto a landing page.
- **Metadata as tinted pill chips, everywhere.** Every tag, status and
  distance wrapped in a colored pill reads as a component-kit dashboard. Rank
  information with type; reserve a chip for a rare genuine status.
- **The eyebrow tick.** A ~30px rule (often a fading gradient) beside a kicker
  label. Ornament, not structure. Drop it; if the label needs presence, use
  type, weight, color or spacing.
- **Section-number eyebrows.** "00 / INDEX", "001 · Capabilities", "06 · how
  it works", "01 / 4" pagination on tiles, "Scroll · 001" cues, "Index of
  Work, 2018 - 2026" range labels. If a label must exist it names the topic
  in plain words; it never counts.
- **The middle-dot chain.** "foo · bar · baz · qux" as the default separator
  for every metadata line. One dot per line at most; past that use line
  breaks, columns or spacing.
- **Decoration text strips and scroll cues.** A mono-caps strip across the
  hero foot ("BRAND. MOTION. SPATIAL.", "DESIGN · BUILD · SHIP", "ESTD. 2018
  · LISBON") and any "Scroll", "↓ scroll to explore" or bobbing mouse icon.
  The viewer is looking at the hero; they know what scrolling is. A bottom
  strip is allowed only when it carries real links or real status.
- **Unrounded hairline rules as decoration.** A bare square-capped line faking
  structure (a divider beside a paragraph, a rail down a list). If a line must
  exist, round its caps, build it into an invented shape, or use spacing and
  hierarchy instead. Two compound forms: a border above AND below every row
  of a long list or spec table (pick one edge, use it sparsely, or change the
  component; see layout), and crosshair or hairline grid lines drawn across a
  section to make it "feel designed" when they organize nothing.
- **The dot under the active nav item.** Decoration standing in for an active
  state. Mark the current page in the type (weight or color shift), not with a
  mark bolted underneath. (A real sliding tab indicator is fine; a stray dot
  is not.)
- **Decorative status dots.** A colored dot before every nav link, list row,
  badge or label ("● ONE Q4 SLOT OPEN") is the same tell multiplied. A dot
  earns its place only when it reports real state (a live server, an
  availability flag), and then once per section at most.
- **Filled-track progress bars as comparison.** A gray track with a partial
  fill to show "X of Y" on a marketing page is dashboard clutter. Use the
  number, or a tiny inline bar with no background track.
- **Grid / graph-paper backgrounds.** Faint thin grid lines behind a hero or
  the whole page, even subtle, even radially masked: still graph paper. The
  blueprint look earns its place only sparing and specific (a few ruler
  ticks, corner crop or registration marks, dashed 1px guides, one actual
  technical drawing), never a full-bleed sheet. The premium form is a tight,
  small, textured module grid that reads as a printed substrate, usually
  behind one panel or footer; buildable with repeating-linear-gradient plus
  small SVG tick and bracket marks. When in doubt, no grid.
- **Crude CSS/SVG "illustrations".** Bar charts made of rounded divs, floating
  spheres, dashed orbit rings, mock stat cards: generated placeholders. (A
  crafted, layered, carefully lit SVG object is the premium opposite, and one
  of the strongest things a page can have.)

## Copy and label tells

Copy is part of the interface, and generated copy has its own tells. Before
shipping, re-read every visible string: headlines, eyebrows, button labels,
captions, alt text, placeholder text, footer lines, error messages.

- **Em and en dashes in copy.** A classic AI writing tell, in headlines,
  body, captions and attributions alike. Use a hyphen, a comma, a colon, or
  two sentences. Ranges ("2018-2026", "€40-80k") take a plain hyphen too.
- **Poetic section labels.** "From the field", "Field notes", "Currently on
  the bench", "On our desks", "Loose plates" over a quotes, blog or sidebar
  section read as performed craftsmanship. Use the plain label
  ("Testimonials", "Latest writing", "Now working on") or none.
- **"Quietly trusted by."** And "quietly in use at", "humbly powering".
  Write "Used at" or "Customers include", or let the logos speak.
- **Micro-meta sentences under headings.** "Each of these is a feature we
  ship today, not a roadmap promise. The list will stay short on purpose."
  A sentence explaining the section's own restraint is clutter. Heading and
  body are enough.
- **Mock-humble asides.** "We respect the French ones", "we are biased, but"
  and similar cute industry winks in body copy. Cut.
- **Generic step labels.** "Step 1 / Step 2 / Step 3", "Phase 01", "Pass One".
  The step's verb is the label: "Install", "Configure", "Ship".
- **Filler verbs and slogans.** "Elevate", "seamless", "unleash", "next-gen",
  "revolutionize", "unlock your potential", "transform your day", "smarter
  than ever". Say what the thing does in concrete words.
- **Placeholder people, brands and numbers.** "John Doe", "Sarah Chan", the
  SVG egg avatar; "Acme", "Nexus", "NovaCore", "Flowbit", "Cloudly";
  "99.99%", "50%", "1234567". Use realistic, locale-appropriate names, a
  believable invented brand with its own mark, and organic values ("47.2%").
  Invented precision cuts the other way too: a "5.8 mm" or "13.4 lb" spec
  the brand never claimed is fake engineering. Numbers come from real data,
  are labeled as sample, or are absent.
- **Broken or over-clever strings.** Grammar that does not parse ("free on
  its past"), referents with no antecedent, forced wordplay, passive
  humility. If a string might not make sense, replace it with a plain
  functional sentence. Boring copy beats cute wrong copy.
- **Headline stunts.** A headline broken with a forced line break and an
  italic tail ("for thirty<br><em>years.</em>") and text rotated 90 degrees
  down a margin are portfolio clichés. A headline reads naturally first.
- **One copy register.** Technical mono ("47 tasks · 0.6 ctx-switches/day"),
  editorial prose and marketing punch in one composition fight each other
  unless the brand voice asks for the mix.
- **Duplicate CTA intent.** "Get in touch", "Let's talk", "Start a project"
  and "Reach out" on one page are four labels for one action. One label per
  intent, used identically in nav, hero and footer. Same for "Try free" /
  "Get started" / "Sign up free". A primary CTA label is one to three words
  and fits on one line at desktop; a wrapped button is broken.
- **Quotes that run long.** A testimonial is a snippet: three lines at most,
  attributed with name and role, never a bare first name.

## Shadow, glow and glass tells

- **The default all-around shadow.** A soft symmetric bloom on every side of
  everything, added by reflex: the float-it-on-a-cloud look. Depth, when
  needed, is a decision: a tight, low-offset, small-blur shadow tinted to the
  surface or the element's own color, cast from one light source. Better
  still, get depth from tone and a self-colored edge with no shadow at all.
- **The traceable shadow.** If you can see the shadow's border (a hard-edged
  rounded rectangle parked behind the element), it is a box, not a shadow.
  Soften the falloff, tighten the offset, carry the blur all the way out.
- **The blurred-silhouette bloom.** A glow that is just a blurred copy of the
  element's own outline, offset behind it: no shadow at the edges, color
  pooling to the sides, the silhouette visibly repeated. A real shadow is
  cast, directional, and never traces the shape.
- **Faking a shadow with a second box.** Told to avoid a big shadow, do not
  drop an offset rectangle or duplicate element behind the thing instead.
  Never reproduce an effect with clumsy geometry to dodge a rule; do the
  restrained, correct version of the effect.
- **Background glow.** The radial accent blob bleeding from a corner or center
  of a dark section for "atmosphere". Its clipped cousin, the cut-off glow,
  ends in a hard line at a section edge or overflow: hidden. A dead giveaway.
- **Radial halo behind a hero object.** Concentric glow rings behind the focal
  object read as slop in any color; warmth does not rescue symmetry. Light an
  object with a directional source (a rake, a single beam) with real falloff.
- **The inner-glow box.** A pill, chip or badge lit from within, or a pulsing
  glow ring behind a "live" status dot. Boxes do not light up from inside;
  give a badge an honest solid surface and a real border.
- **Botched glass.** Blur pixelation or banding over a flat backdrop with
  nothing to refract, a shadow leaking out below as a smear, a resting halo
  behind the shape, a blur that pops on hover or press. A bad blur is worse
  than none: if glass cannot blend seamlessly, do not ship glass. The gloss
  (the specular sheen across the top lip) is the part that works; keep it and
  fix the blur and shadow around it.
- **Glass with no material logic.** Translucency carries hierarchy, so treat
  it as a material with weight. Never stack a light translucent surface on
  another light translucent surface; legibility collapses. Bigger surfaces
  read thicker: more blur and a deeper shadow than a small chip. Over a
  blurred surface, text goes heavier and higher-contrast with a touch more
  tracking, and color sits on a solid layer, not the frosted one. Where
  content scrolls under floating chrome, no 1px divider: a short blur or
  gradient fade at the seam, only where the overlap happens. Glass arrives
  by animating blur and scale together, not by an opacity fade. Under
  prefers-reduced-transparency, raise the fill opacity and drop the blur.

## Color and surface tells

- **Purple, and blue-to-purple gradients.** The default AI palette. The soft
  blue-to-purple wash is the single most recognizable slop move, and any glowy
  gradient of two adjacent hues reads machine-made. Pick a considered palette.
- **The cool blue-charcoal dark theme.** The default "serious dark product"
  base: slate-indigo ink around #0c0e15, a slightly bluer panel, a lilac or
  periwinkle accent. Night-mode slop. A dark UI does not have to be blue:
  warm it, neutralize it, or push it to a chosen hue (green-black, warm
  charcoal, oxblood-black).
- **The pastel candy gradient.** Butter-yellow into peach into strawberry-milk
  (the #ffe6a8 to #ffc0da family), mint-to-lavender, sherbet-to-cream: the
  sunset-sorbet wash that could sit behind any product.
- **Drifting soft-blend blobs (the candy aurora).** A few big blurred radial
  blobs at ~50% opacity with mix-blend-mode: multiply, melting into a pastel
  aurora. Muting the hexes just makes tidier slop. If the background needs
  life, author it: directional light with falloff, a crafted illustration, a
  grained one-color gradient.
- **Cream / beige "editorial" backgrounds.** The default "tasteful premium"
  surface, overused to the point of slop. Reaching for cream is reaching for
  the blue-purple gradient: a non-choice. Dark, cool, saturated or odd can
  all be more premium than another sheet of oat milk.
- **The slop gray.** The UI-kit neutral (the gray-100/200 family: #f3f4f6,
  #eceef2, #e7ecf3) as footer band, section divider, card fill or page base
  reads like a wireframe left at default. Pick a brand-specific surface tone:
  a tinted off-white, a deepened or warmed neutral. The gray is a non-decision
  wearing the costume of restraint.
- **Saturated accent everywhere.** One vivid mid-saturation swatch on the
  headline word, the eyebrow dot, the button fill and the label makes a
  template; saturation and contrast are the tell, not the hue. The premium
  accent is TONAL: a value pushed much lighter or darker than its
  surroundings, usually desaturated, like the dim gray of a code comment.
  This bounds the two-tone headline too: emphasis is a tonal shift, never a
  saturated color pop.
- **Colliding colors, and hard seams between sections.** Two failures. Hues
  that fight, an accent belonging to no system, or a muddy wash laid under a
  fine component (the color envelope is the problem, not the element). And
  hard color walls where one section's gradient or glow cuts off dead at the
  next section's edge. Hold one disciplined palette, let adjacent sections
  share or hand off their tone, and lean on real color relationships. Reserve
  a hard break for the rare deliberate place (a footer stepping onto its own
  darker floor), and do not put a seamless blend on every edge either.
- **The mid-page theme flip.** A warm-paper light section sandwiched between
  dark ones, or the reverse, reads as walking into a different site
  mid-scroll. One theme per page (light, dark, or system), locked at the
  root. Tints within the same family are fine; a full inversion is allowed
  once, as a deliberate color-block move with a strong transition, never as
  alternation.
- **Pure black and pure white.** #000000 and #ffffff as surfaces kill depth.
  Use an off-black or off-white that belongs to the palette.
- **Gradient-filled headline text.** background-clip: text pouring a
  magenta-purple-cyan or blue-cyan gradient into the type itself.
- **Banded gradients.** Any large color transition should carry fine grain or
  noise. A smooth gradient that stripes reads cheap; a grained one reads
  physical.
- **Grain over content.** Premium grain sits BEHIND text and controls, at an
  opacity you feel rather than see. A noise layer over type, icons or panels
  muddies them. One deliberate exception: grain masked into a single display
  word or heading can be lovely; a blanket sheet over everything is not.
- **Hard image seams.** A full-bleed image butting a flat section with a
  visible line reads as a band pasted on. What verifiably works (after two
  failed tries): feather the image's own pixels, with all four conditions at
  once, or it still bands.
  1. Mask, not overlay. A color-gradient overlay leaves the image at full
     opacity and the eye catches the join. Fade the image itself:
     mask-image: linear-gradient(to bottom, transparent 0%, ... #000 31%,
     #000 65%, ... transparent 100%).
  2. Long and finely eased: fades over ~30% of the section at each end, with
     10+ stops. A short or three-stop fade still reads as a faint line.
  3. Tall section (~116vh) so a full-opacity strip survives both feathers.
  4. Same background color above and below, so the masked edges reveal one
     unbroken surface.
  And never end a text-contrast scrim at a section boundary at partial
  opacity; it becomes its own band. Any darkening sits only behind the text
  and fades out before both edges; carry the rest with a strong text-shadow.

## Type tells

- **The rejected list.** Nearly every free Google font reads as slop the
  moment it carries the brand, across every category. Sans/grotesque: Inter,
  Space Grotesk, Sora, Syne, Archivo, Onest, Darker Grotesque, Geologica,
  Hanken Grotesk, Spline Sans, Schibsted Grotesk, Gabarito, Figtree,
  Quicksand (the friendly-rounded sans are not a cheerful exception), plus
  the fat bubbly novelty displays (Bagel Fat One, Baloo, Fredoka, Chewy,
  Lobster), whose pairing with a system-ui body is the tell doubled. Serif:
  Fraunces, Cormorant, Bodoni Moda, Didot, Playfair and the Didones, Petrona,
  Hedvig Letters Serif, Brygada 1918, Young Serif (the free "warm antique"
  voice). Mono: JetBrains Mono, IBM Plex Mono, Spline Sans Mono, Fragment
  Mono (lifted from a premium site and still slop; pulling a font off a good
  site is not choosing one for this brief). The known pairings are tells too:
  Fraunces with Work Sans, Space Grotesk or Sora with Inter for "techy SaaS",
  Syne for "edgy creative", Archivo shown solid/outlined/accented as fake
  variety, Cormorant with one italic word as instant elegance. A Didone is
  not automatically luxury, Inter as body is the most common slop font of
  all, and heavier or more "designy" is not more distinctive.
- **Two hard rules.** First: stop cycling Google fonts hunting for the safe
  one, and know that the "tasteful designer alternative" (Big Shoulders,
  Newsreader, Instrument Serif, Bricolage, IBM Plex Mono) is the same tell;
  picking type by reputation instead of for the brief is the problem. The
  signature face must be genuinely distinctive, which usually means licensed
  or self-hosted. A plain neutral may sit quietly in body text; the signature
  line cannot rest on the Google shelf. Second: never reuse a face or a
  serif-plus-clean-sans pairing you already shipped on another site. A house
  pairing repeated across briefs is itself a tell.
- **Licensed type is the premium norm.** The least-slop sites license or
  self-host real faces (Perfectly Nineties from Pangram Pangram, Matter from
  Displaay, Soehne, GT America, Tiempos, the Klim families) over a neutral
  workhorse and a mono. Lift exact families from source, never from memory.
- **The free path: Fontshare, and past it.** Fontshare is free,
  licensed-quality and off the Google rotation (download the woff2,
  self-host via next/font/local). But its famous faces (Clash Display,
  General Sans) now read startup-generic too; reach further for character
  (Pally, Gambarino, Sentient, Tanker, the Velvetyne faces). Pair the
  display with a TRUE neutral body: system-ui is genuinely neutral and safe.
  View candidates rendered before picking.
- **Mono as the house voice.** Mono is correct for actual data: timestamps,
  codes, prices, real tables. Spread across eyebrows, captions, labels and
  the copyright line it is a costume, not a decision.
- **One label treatment, everywhere.** The identical tracked-out caps (or
  mono) on the eyebrow, the buttons, the figure numbers, the nav action and
  the footer colophon reads as a template, not a voice. Give different roles
  different treatments, or cut the labels entirely.
- **Cramped display type.** Negative tracking until glyphs nearly touch (a
  stat like "0·fail" with the separator buried). Big type needs air: loosen
  the tracking, give separators space. The larger the type, the more spacing
  decides whether it reads composed or squeezed.
- **One tracking and leading value for every size.** Type changes shape with
  size. Display wants slightly negative tracking (around -0.02em, never to
  the point above) and tight leading (1.0 to 1.1); body sits near 0 tracking
  at 1.5 leading; small labels want a touch of positive tracking. A fixed
  letter-spacing is wrong somewhere. Build hierarchy from weight, size and
  leading together, and emphasize with weight before scale. Set spacing in
  rem or em so a user's larger text size scales the layout instead of
  breaking it.
- **Text too small.** Labels and captions shrunk to fit more UI. If the
  type feels small, the design is not finished: cut content, add space,
  split the screen. Readable beats dense and beats decorative.
- **The off-center strike.** A line through text (strike-through, redaction
  bar) must run through the true optical center of the letterforms, measured
  against the real x-height, not floating near the baseline or the caps.

## Layout tells

A recolored layout is still slop; the skeleton is the tell, not any one
piece. Before shipping, ask: have I used this layout or this font before? If
yes, change it.

- **The default hero stack.** Eyebrow, headline, subline, primary button plus
  secondary text link, stacked down the middle. A slop layout even in fine
  type, because it is the composition everyone ships. Break the stack: change
  the axis, split or offset the pieces, drop the secondary link, let the
  signature artifact carry the space.
- **The hero stack with a panel on the right.** The most over-shipped hero:
  the same stack in a left column, a product panel, image or card floating on
  the right. The skeleton is the slop regardless of what the panel holds.
- **The split hero.** The "premium brand" twin: letterspaced uppercase
  kicker, big serif headline emphasizing one word, quiet subline, two
  buttons, a stat row under a hairline, and a framed visual card with a
  caption and floating tag. Reused across every category with only the
  colors changed.
- **The kicker over the heading.** Any section opening as
  small-label-over-big-heading (uppercase or mono kicker above the H2, serif
  or not) is the template for starting a section. Vary the openings: drop
  the label, change the scale, open with an image, a number, a full
  sentence, or nothing. Mechanical check: count the tracked-caps or mono
  micro-labels above headings across the page. More than one per three
  sections (the hero counts) fails.
- **Hero stack overload.** The hero is one moment, not a feature list: at
  most four text elements (one small label OR brand strip OR neither, a
  headline of one or two lines, a subline under twenty words, one primary
  action with at most one differentiated secondary). No tagline under the
  buttons ("Works with GitHub, GitLab and self-hosted"), no trust micro-strip,
  no pricing teaser, no avatar row, no feature bullets; those get their own
  section below. Plan the type scale and the asset together: a four-line
  headline is a font-size error. Top padding stays under about 6rem at
  desktop, or the content floats halfway down the viewport and reads as a
  bug.
- **The two-line or towering nav.** Desktop navigation renders on one line
  at 1024px or it condenses, drops items or collapses to a menu. Height
  stays under 80px; the agency bar that eats 15% of the viewport is a tell.
- **The zigzag run.** Left-image-right-text, then right-image-left-text,
  then again. Two in a row at most; the third consecutive split breaks with
  a full-width section, a stack, a marquee or another family. More broadly,
  each layout family appears once per page; eight sections need at least
  four families.
- **Bento with holes, or six white cards.** A bento grid has exactly as many
  cells as there is content (three items, three cells), never a blank tile
  to square it off. And at least two or three cells carry real visual
  variation (an image, a pattern, a tinted surface); a cream-on-cream grid of
  typography-only tiles is the default wearing a grid.
- **The floating corner paragraph.** A giant left headline with a small
  explainer stranded in the top-right of the same header, aligned to
  nothing. Stack headline and body, or build an honest two-column header
  where the right column holds a real visual or aligned body.
- **Mixed radius systems.** Pill buttons in a sharp-cornered layout, or
  square cards on a pill-button page, is broken, not eclectic. One radius
  system per page (all sharp, all soft, all pill), or a written rule
  ("buttons full, cards 16, inputs 8") followed everywhere.
- **Long lists as hairline rows.** More than five items in a bulleted list
  or a divide-y table is the lazy component, worst as a ten-row spec sheet.
  Group into two or three chunks with one soft divider each, feature the
  top three as display tiles with the rest behind a disclosure, or move to
  a card grid, tabs, or a scroll-snap row. On a landing page, three to five
  highlights and a "view all" link beat a twenty-row table.
- **The big serif statement block.** Kicker plus one large serif sentence
  with a single italic-accent word as the "philosophy" beat. A reflex, not a
  composition.
- **The multi-line headline, and the dangling accent.** Three or more stacked
  display lines is a staircase with no rhythm, and a lone accent word
  stranded at the foot of it reads as a random color splash. Hold display
  lines to one or two, with any emphasis inside the phrase it belongs to.
- **The filled-plus-outlined button pair.** One solid primary beside one
  ghost secondary is a preset, full stop, in any color or radius; arrows and
  underlines only make it louder. One clear action, or two differentiated
  some other way.
- **The three-tier pricing block.** Free/Pro/Enterprise cards, pill above
  the heading, big price with "/mo", checkmark lists, and the glowing
  gradient-bordered "MOST POPULAR" middle card.
- **Numbered steps on a rail.** 01/02/03 beside a vertical rule, text to the
  right. Compose a sequence some other way, and never lean on a bare line to
  carry it.
- **The pre-footer CTA slab.** The full-width gradient box with a centered
  headline, a "free to start, no credit card required" byline, and two
  buttons.
- **The inset island as the default closer.** The rounded, margin-all-sides
  panel holding kicker, serif headline, lead and a form was a premium move
  once; as the closing section of every site it is a prefab. Same for the
  email-pill form (a pill input beside a pill button), the single most
  repeated component of all. A signup does not have to be a pill next to a
  pill.
- **The image card with overlay caption.** Portrait tile, bottom scrim, small
  uppercase meta label, serif name, place line, link arrow. The image inside
  is fine; the wrapper is the same template every time.
- **The standard footer.** Big wordmark, one-line tagline, full-width rule,
  four link columns under uppercase mono labels, another rule, cute
  copyright line. Tidy, readable, expected: the "correct" footer with no
  idea in it.
- **A hero that does not own the first screen.** If the next section peeks in
  under a too-short hero, the page reads sloppy before the first scroll.
  Size the hero to the viewport or deliberately control exactly what crosses
  the fold, and compose that first frame.
- **A flat fill under everything after the hero.** A stunning full-bleed hero
  and then one flat dark or cream field with boxes: the atmosphere stops at
  the fold. A page is not premium because its hero is; carry imagery,
  texture and depth down the whole scroll.
- **Content flung to the far edges.** Two clusters jammed at opposite rims
  with a dead gulf between (the classic footer split) reads unplaced, not
  composed. Absent a deliberate asymmetry, default to a real grid, shared
  margins and balanced weight.
- **Stacking slop layouts compounds.** Any one block might be argued in
  isolation; a run of them multiplies into something unmistakably generated.
  A page is not the sum of individually acceptable blocks. When a block
  matches this list, that means change it, not "the pieces are fine".
- **The whole SaaS meta-skeleton.** The Stripe/Linear/Vercel clone: two-column
  hero with a shadowed panel, three icon-tile feature cards, a tabbed
  switch, pricing cards, FAQ accordion, full-width CTA slab, multi-column
  footer. The most generated layout on the internet, and the most dangerous,
  because it feels safe and professional while being pure slop. Recoloring
  changes nothing. If this is the page you are about to build, stop and
  decide a real signature first.
- **Recycling your own house style.** The same five section shapes reskinned
  per brief is a theme, not design, even when each piece was once premium. If
  the last site and this one share their skeletons, you reskinned. Compose
  each site's sections from its brief.

## Motion and interaction tells

- **The hover boop.** A button that lifts or scales on hover is a template
  reflex; buttons do not move on hover at all. Change state cleanly: a fill
  or color shift, an icon sliding, an honest tonal change. Reserve any lift
  for cards at most, tonal and grounded, never bouncy.
- **Underline-fill hovers.** A link or nav item whose underline grows, wipes
  or travels in is the reflexive "look, it's interactive" flourish. Do not
  animate underlines.
- **The card hover-lift.** Translate-up plus an even blooming shadow plus a
  glowing accent border, bolted onto every card grid.
- **Floating cards.** Decorative bobbing over the hero, purposeless parallax
  and hover lifts. Motion with no job.
- **Botched fill animations.** Caps flipping from sharp to round mid-motion
  (the giveaway of animating scaleY on a rounded shape), a fill stopping
  short of its track, stuttering easing. Animate a clip or a width/height
  with stable caps, fill the FULL track, ease smoothly. Half-built motion is
  worse than none.
- **The fixed background that trails the scroll.** One position: fixed sheet
  dragged behind every section including the nav, twinkling in place, is a
  static texture in a costume. A signature background must actually do
  something (move, react, relate to the content) and integrate; otherwise do
  not lean on it.
- **Dead controls.** A tab, accordion, slider, toggle or button that looks
  interactive and does nothing is broken, the worst slop of all. Every
  control must work, confirmed by a real click, and no static prop may dress
  as a live control that invites a click it cannot answer.
- **Feedback on release instead of press.** A button that only changes on
  click feels dead. Respond on pointer-down (a scale to 0.97 or a tonal
  shift within 100ms), commit on pointer-up, allow cancel by dragging away.
  Audit every debounce, timer and transition wait on the input path; lag
  is where directness falls off a cliff. During a drag, slider or sheet,
  update 1:1 with the pointer the whole way, never only at the end.
- **Transitions that lock or jump.** A closing sheet the user grabs again
  must follow the finger, not finish closing and reopen. Every animation is
  interruptible: never block input while something moves, and on interrupt
  start the new animation from the element's live on-screen value, not its
  logical target (starting from the target is the visible jump). Springs do
  this by default, which is why anything gesture-driven uses a spring, not
  a CSS transition or keyframe. Split 2D motion into independent X and Y
  springs so they do not desync.
- **Bounce on things that were not thrown.** Default UI springs are
  critically damped: no overshoot. Bounce belongs only where the gesture
  carried momentum (a flick, a throw, a drag release). Reference values:
  move or reposition at damping 1.0, response 0.4s; rotation 0.8 / 0.4;
  drawer or sheet 0.8 / 0.3. In Motion: type spring, bounce 0, duration 0.4
  as the house default; bounce around 0.2 only after momentum.
- **Stock easing.** linear and ease-in-out are the defaults nobody chose.
  Use a spring, or an authored curve such as cubic-bezier(0.32, 0.72, 0, 1)
  or cubic-bezier(0.16, 1, 0.3, 1), and mirror it on the return path of a
  reversible transition.
- **Enter one way, leave another.** A panel that slides in from the right
  dismisses to the right. A menu, popover or sheet originates from the
  element that opened it (transform-origin at the trigger), not from the
  center of the screen. Intermediate frames point at the outcome.
- **Hard stops and snapped grabs.** A dragged element keeps the offset
  where it was grabbed (no snapping to its center), uses setPointerCapture,
  and tracks a short position history so release velocity is known. On
  release the spring continues at the finger's velocity (pass it as the
  initial velocity; if the API wants a relative value, divide by the
  remaining distance). Snap to the target nearest the PROJECTED resting
  point, not the release point:
  project(v) = (v / 1000) * d / (1 - d), with d about 0.998 (0.99 snappier).
  At a boundary, rubber-band instead of stopping dead:
  offset * dim * c / (dim + c * |offset|), with c about 0.55. Decide commit
  versus cancel by velocity sign at release, not position.
- **Scroll listeners and state-driven motion.** window scroll listeners,
  scrollY in React state, and useState for pointer or scroll values
  re-render every frame and die on mobile. Use motion values, useScroll and
  useTransform, IntersectionObserver, or CSS animation-timeline. Animate
  transform and opacity only, never top, left, width or height; will-change
  only on things about to move; every effect has a cleanup.
- **Slow loops and brightness jumps.** A full-viewport background
  oscillating near one cycle per five seconds is a vestibular trigger, and
  a theme switch that snaps from dark to light is a flash. Ease theme
  changes, make large moving surfaces semi-transparent while they travel,
  and keep ambient motion small and slow.

## Execution failures: verify these on the rendered page

These read as bugs, not style choices, and they hide at normal zoom. Check
each one on the final rendered result, zoomed in.

- **Never hide content behind an entrance animation.** The single most
  damaging motion mistake: content starting at opacity 0 (or translated
  away) waiting for a reveal. When the reveal fails to fire (backgrounded
  tab, unsupported timeline, throttled engine, hydration hiccup, screenshot
  pass) the content is simply GONE. This applies to CSS animation-timeline:
  view(), to IntersectionObserver class toggles, AND to a Framer/Motion
  initial={{opacity:0}} stranded at its first frame; all three have shipped
  blank sections and empty search bars. CONTENT IS VISIBLE BY DEFAULT.
  Animate things already on screen (hovers, marquees, a sliding indicator, a
  counting number, parallax on visible elements). An entrance reveal is
  acceptable only when the no-JS fallback still shows everything. A static
  readable page beats a beautifully animated one that renders empty.
- **Clear the cut.** Whenever you add a clip-path, a notch, an overflow:
  hidden or a fixed height, prove the content sits fully inside the visible
  region: sliced cap heights, shaved descenders and half-cropped controls
  read as broken, and you will not spot them at normal zoom. Pad clear by
  more than the cut removes, then zoom into the exact clipped edge and check
  pixel by pixel. Same where sections overlap: a rising panel or sheet must
  never guillotine content that continues beneath the seam; keep continuing
  content on the layer that stays visible and clear it past the boundary.
- **Nothing is actually centered.** The most repeated failure: the number
  floating high in its circle, the glyph sitting low in its tile, the label
  off-axis in its pill, because centering was assumed instead of proven.
  Verify it mathematically AND optically, zoomed in, every time. SVG traps:
  text-anchor: middle needs dominant-baseline: central (or a measured dy)
  for the vertical; a glyph's optical center is not its bounding box; a
  rotated, stroked or padded shape moves where center actually is.
- **Ragged comparison grids.** Items set side by side to be compared
  (pricing tiers, plans, before/after) must align every corresponding row on
  one shared horizontal grid: title, price, body, list start, and above all
  the buttons. Alignment never depends on content length: equal-height
  cards, buttons anchored to the bottom, reserved space for variable copy,
  held slots for missing values. The longest string in one cell never
  decides where its neighbors' content lands.
- **Text jammed against an edge.** Copy kissing the viewport or container
  rim looks overflowed, not placed. Every text block gets a deliberate,
  generous, consistent gutter from every edge it nears. The only exception
  is a purposeful composition, like an oversized wordmark cropped on
  purpose.
- **Text you cannot read.** Ink too close in value to its background: the
  words are there and the eye fights for them. On a filled button this is
  unforgivable. Every string clears its background by a real value gap;
  when in doubt, push contrast further, not less. Forms are where this hides:
  placeholder text, helper text, focus rings and error text all clear WCAG
  AA (4.5:1 for body, 3:1 for large text) against the section they sit on,
  and a ghost button over a photograph gets a scrim, a stroke or a backdrop.
- **Clipped italic descenders.** An italic display word containing y, g, j,
  p or q set at line-height 1 loses its descender to the next line or the
  container edge. Give it at least 1.1 leading and reserve space below;
  check every italic word in a headline before shipping.
- **Wrapped labels.** A CTA or nav label that breaks onto two lines at
  desktop is broken. Shorten the label or widen the control; never cap a
  button's width and hope.
- **The system preferences you ignored.** prefers-reduced-motion replaces
  slides, springs and parallax with short cross-fades (feedback stays,
  vestibular motion goes); prefers-reduced-transparency makes glass solid;
  prefers-contrast: more gets near-solid surfaces with a defined border.
  Infinite loops, scroll-hijack and magnetic physics collapse to static.
  Verify each one is wired, not assumed.
- **Missing states.** A component shipped in its success state only.
  Loading shows a skeleton in the final layout's shape, not a spinner.
  Empty states are composed and say how to fill them. Errors are inline for
  forms and contextual elsewhere; toasts only for transient news.
- **Repaint traps.** Grain and noise live on a fixed, pointer-events-none
  layer, never on a scrolling container. backdrop-filter belongs on fixed
  or sticky chrome only, never on large scrolling areas. Full-height
  sections use min-height 100dvh, never 100vh or h-screen (the iOS address
  bar jumps). z-index comes from a small documented scale (nav, overlay,
  modal, tooltip), never z-50 and z-9999 scattered.
- **Viewed in one state only.** Before calling it done, look at it in both
  themes, at phone, tablet and desktop widths, with reduced motion on, and
  with keyboard focus walked through every control. A page seen in one mode
  has not been checked.

## Mobile screens and screen sets

A mobile screen is not a website squeezed into a phone frame. These apply to
built app UI and to generated screen imagery alike.

- **Safe areas and system regions.** Status bar, title region, tab bar, home
  indicator, sheet docking zone and gesture space are real. Critical content
  and controls never sit in them; a screen composed edge to edge like a
  poster with no functional logic reads as a mockup, not an app.
- **Navigation that could be real.** A tab bar for major sections (never
  overloaded), stack navigation for drill-down, sheets for secondary tasks,
  segmented controls for local switching. One clear primary path through
  the app; not every action equally loud.
- **The first screen.** One focal point, a short headline, one obvious next
  action. No pile of stats, chips, tags or pills above the fold; no wall of
  onboarding copy; no rating prompt on first run. Three onboarding screens
  that differ only by icon and headline are one screen cloned.
- **Box in box in box.** Nested card stacks, five levels of framing,
  floating surfaces everywhere, widgets fighting for attention, fake chart
  dashboards and repeated stat cards with no product reason. Fewer, clearer
  containers; flatter structure; one strong structural move per screen.
- **Screens that drift apart.** In a set, lock a design bible before screen
  two: platform feel (iOS, Android or neutral, never mixed), palette, type
  scale, spacing, radius, icon style, imagery treatment, texture, nav model,
  card and button styling, shadows. Vary composition, density, image
  placement and tempo from screen to screen; never vary identity. The set
  follows a believable order (onboarding to auth to home; browse to detail
  to cart) and each screen answers why it follows the last.
- **Generated mockup framing.** One device style and scale across the set,
  even margins on all four sides, the phone never touching the canvas edge,
  a visible clean frame that supports the screen without dominating it.
  Never crop a detail out of an earlier board; render it fresh and readable.

## The deeper tell: dodging this list is still slop

Everything above is surface. You can avoid every item and still ship slop,
because the output reads as generated when nothing was invented. The proven
traps: swapping to the known "tasteful" font, rebuilding the same skeleton in
new colors, ruling instead of bordering, and stripping every icon to play
safe (zero icons is as lazy as Lucide on everything; the answer is your own
icons). Design is a point of view about who this is for and why it should
look this way, applied with conviction. A checklist can only make work less
wrong; it cannot make it good.

## What premium actually looks like

Most slop techniques are the lazy default version of a real tool. Glass,
accent edges, light, borders and motion all appear in premium work too; the
difference is craft, restraint and above all uniqueness: clearly made on
purpose for this one screen.

- **Real translucency.** Glass is a material, not a semi-transparent panel:
  it sits over a backdrop worth showing through, refracts and bends it,
  carries faint chromatic dispersion at the edges, a bright inner highlight
  along the top lip, a light frost, and tightly tuned inner and drop
  shadows. It reacts to what is behind it.
- **The liquid-glass recipe.** Reference values from a working glass-button
  spec (two variants, over a photographic backdrop so refraction has
  something to bend). Shared base: fill #2575FF (thick variant at 50%
  opacity so the background reads through); white label and icon, Geist
  Medium 20, icon gap 8; padding 20 x 14; two hairline strokes at 20%
  opacity in near-surface colors (#22BBFD and #FFFFFF), self-colored edges,
  not an outline; inner top highlight #FFFFFF at 20%, offset-Y 1, blur 32;
  drop shadow tinted to the FILL color #2575FF at 6%, offset-Y 3, blur 3 (a
  tight color-matched shadow is the premium move; a soft black bloom is the
  slop one). Glass parameters: thin pill: light -45deg at 80%, refraction
  80, depth 2, dispersion 40, frost 6, splay 0. Thick pill: light -50deg at
  60%, refraction 64, depth 44, dispersion 67, frost 2, splay 20. (Light =
  specular direction and strength; refraction = how hard the backdrop
  bends; depth = apparent thickness; dispersion = chromatic edge split;
  frost = blur; splay = how far refraction spreads past the shape.) CSS
  approximation: backdrop-filter blur plus saturate/contrast, an inset
  white box-shadow for the lip, the two low-opacity strokes via layered
  border or box-shadow, the tight color-matched drop shadow, and fake
  dispersion with a 1px cyan/magenta edge offset; SVG feDisplacementMap
  gives true refraction if it earns the cost.
- **Self-colored borders and tonal elevation.** Define a container without
  drawing a line: shift its surface a hair lighter or darker than the
  background, add a 1px stroke in the surface's OWN color at low opacity
  and a soft inner highlight on the top edge. An edge you feel as a lip
  catching light, not an outline you see.
- **Bespoke geometry.** Uniqueness is the biggest premium signal, and shape
  is its cheapest carrier: a marker that cuts in on a diagonal and kicks
  back out, a chamfer, a notch, a custom bracket. Apply to dividers,
  corners, connectors, container edges, underlines: invent the geometry
  instead of accepting the rectangle.
- **Bare icons, and say less.** Strip icons to the mark: no tile, no chip.
  Cut copy to few words and short lines; hierarchy, spacing and visuals
  carry the meaning. Confidence is shown by how much you leave out.
- **Custom in-house iconography.** Icons drawn as individual designed
  objects in one house style, consistent in stroke, corner and grid. One of
  the clearest signals a person designed this.
- **Authored micro-interactions.** Motion written for this one element: a
  line that travels and fills with a slightly over-extended popped cap and
  deliberately tuned easing, any shadow tight and intentional. Not the
  global fade-and-translate.
- **Considered light.** When light or glow is used, choose its color,
  direction and falloff: a warm volumetric amber wash, a single directional
  ray. Art-directed, not the reflexive blue-purple bloom.
- **Premium noise.** A fine film grain or perlin texture at very low opacity
  breaks up flat fills, kills banding, and makes surfaces feel physical.
  The entire point is subtlety: felt, not seen.
- **Full-page composition.** Premium screens are art-directed as one frame,
  not stacks of sections: oversized headlines, an enormous wordmark
  bleeding off an edge as a watermark, generous negative space, scale far
  past the timid default.
- **Real logo walls.** Recognizable customer marks ("used in production
  by"), single color, even sizing, quiet. Only real brands you can honestly
  claim; invented logos are their own slop.
- **Inset island sections.** A section floated as a rounded panel with
  consistent margin on ALL sides, on a subtly different surface plus grain,
  reads as a detached, deliberate object. The all-sides breathing room is
  the whole cue. (Just not as the default closer every time; see layouts.)
- **Crafted SVG renders.** A product or illustration hand-built in SVG with
  real care (correct proportions, layered detail, considered light) is the
  opposite of the crude-CSS tell. When a bespoke SVG object is the
  strongest thing on the page, you did it right.
- **Scroll-authored motion.** Content that settles or shifts as it enters
  the viewport, quiet parallax between layers: subtle, fast, tied to scroll
  position, gated behind prefers-reduced-motion. animation-timeline: view()
  does most of it without JavaScript. (And never via opacity-0 reveals:
  animate y, not existence.)
- **The oversized footer wordmark, done right.** The giant brand word works
  only as a composition: generous letter-spacing, a deliberate case, real
  room above and below so no cap or ascender is shaved, a color or texture
  that belongs to the brand, anchored flush to the very bottom edge
  (usually bleeding slightly off) with links and colophon above it, sitting
  on the layer ABOVE the background texture or grid. Crooked, clipped,
  gradient-fighting-gradient, or flat default type pasted large is the slop
  version. Do the composed one or none.
- **Professional does not mean lifeless.** A page can pass every rule here
  and still fail by doing nothing: correct spacing, one tasteful image,
  quiet type and zero authored moments is unfinished work wearing restraint
  as an alibi. Clean is the FLOOR, never the achievement. Calm is a
  deliberate style and can be gorgeous; dead is a miss. The bar is
  professional with a heartbeat: crafted hover states, a drifting
  signature, a scroll-driven reveal, one kinetic detail built with
  conviction.

## The signature: how uniqueness is made

The reference sites (Craft, Paper, Podqi, Droppable, Portal) look nothing
alike, yet they make uniqueness the same way. A flat background with boxes
and a neutral grotesque scores zero on every line below, which is exactly
why it reads as boring.

1. **One signature artifact.** One custom, high-effort focal object that
   could not be pasted into any other site: a torn-paper collage sky, a
   painted dusk landscape with a tiny robot, a flowing silk render, a
   starfield with a bold wordmark, a layered design-tool canvas. Decide it
   FIRST; everything else supports it. Offline it is a crafted SVG scene, a
   detailed product mockup, or a pre-generated image asset, never a flat
   fill.
2. **Atmosphere, not a flat fill.** The background is a composed environment
   with depth and mood (illustration, render, texture, scene). Even the dark
   references carry a starfield; even the bright ones are a painted sky.
3. **Layered depth.** Foreground copy, a midground focal object, a
   background scene, with at least one element crossing a layer boundary.
   Overlap and bleed make depth; one flat plane reads as a template.
4. **The product as a real, populated artifact.** A detailed, filled-in UI
   floated and tilted with depth, usually clipped at the bottom edge. Empty
   placeholder boxes are what boring is made of.
5. **Character in the display type.** The headline face has personality and
   is set large. Body can be neutral; the identity never rests on a neutral
   grotesque.
6. **One bespoke silhouette.** A single custom-cut shape signs the page: a
   pricing card shaped like a receipt with a torn zigzag edge, a contained
   pill nav, a notch. One unmistakable geometry beats ten rectangles.
7. **A treated nav.** The menu bar is a decision, not a flush row of links:
   contain it in a pill, center it, give it real presence, thread brand
   marks into it. Something deliberate.
8. **Real specificity.** Real logos, real names and data inside the product,
   real copy. Generic placeholders read as a stock template.

uniqueness = signature artifact + atmosphere + layered depth + character
display face + bespoke silhouette + treated nav + real specifics. Miss the
artifact and no amount of clean spacing rescues the page.

## A kit of premium moves

Tools for the right context, never a checklist to run top to bottom, and
that disclaimer covers this whole file. Two equal failures: using everything
(a serif headline AND an ascii field AND glass AND a gradient icon AND a
full-bleed scene is noise), and using nothing when the page calls for a
signature. Above both sits cohesion: never use an element that does not
complement the others. A technique that fights the page is worse than
absent.

- **The signature serif headline.** An elegant, characterful, slightly
  high-contrast serif set very large, often with ONE word italic or in a
  single accent color (a violet, an indigo, a brand hue) against neutral
  ink. The single biggest driver of premium feel, and the practical form of
  character display type. One emphasis per headline, never a rainbow.
- **Full-bleed atmospheric hero.** One photographic, rendered or painted
  scene filling the entire hero edge to edge, headline centered over it,
  nav floating on top. The background IS the art: signature artifact and
  atmosphere at maximum, serene and immersive. Offline: a crafted SVG
  scene, grained layered gradients, or a pre-generated asset.
- **Animated character-field background.** Scattered monospace glyphs
  drifting and twinkling over a soft iridescent gradient in a slow seamless
  loop: a data/code atmosphere without literal illustration. Low-contrast,
  behind the content, reduced-motion gated. Strong fit for dev, data, AI
  and security products. (The lazy version is the fixed twinkling sheet
  from the motion tells; the difference is authorship and integration.)
- **Gradient-filled icons.** A multi-stop gradient INSIDE one small custom
  mark, like an enamel jewel: the contained opposite of the background
  gradient. Use on the brand mark or a single eyebrow icon, sparingly.
- **Sweat the arrow.** The default horizontal right arrow reads as a stock
  component; an up-right diagonal arrow, drawn specifically, with stroke
  and corners matched to the system, signals care. Every glyph is part of
  the identity, not filler.
- **One cohesive visual language.** Nav, buttons, arrows, radius, borders
  and background speak one system: sharp corners everywhere, one specific
  arrow reused, one gradient threaded through icon and button. Cohesion is
  itself a premium signal; mismatched fine parts read as cheap. The nav
  especially must belong to the system.
- **The glass CTA, when it earns it.** Glossy, softly blurred glass over a
  rich background, executed clean: gloss highlight, blur that blends, no
  leak, no pop. Over a flat fill it is pointless. (See the recipe.)

## Redesigns

Misreading the mode is the biggest source of bad redesign output. Decide it
first: preserve (modernize without breaking the brand), overhaul (new visual
language over existing content and structure), or greenfield (the brand
itself is changing). If the brief does not say, ask once.

- **Audit before touching.** Write down the current brand tokens (colors,
  type, logo treatment, radii), the page tree and primary nav, which content
  blocks do work and which are filler, the signature patterns worth keeping,
  the tells worth retiring, and the SEO baseline (ranking pages, titles,
  structured data). Migration breakage is the top redesign risk.
- **A brand that is already purple stays purple.** Extract the brand's
  colors before applying the color rules above; the palette tells are about
  defaults, not about a client's real identity. Preserve copy voice unless a
  rewrite was asked for.
- **Levers, in order of lift per unit of risk.** Type refresh, then spacing
  and rhythm, then color recalibration (unify neutrals, keep the brand
  accent), then a motion layer on existing components, then hero and key
  section recomposition, then full block replacement only where a block is
  unsalvageable. Stop when the brief is satisfied. Sound IA, content and
  SEO mean targeted evolution; broken IA, no system, or broken mobile means
  full redesign with strict content preservation.
- **Never silently change** URL slugs, primary nav labels, form field names
  or order (analytics and autofill depend on them), the logo or wordmark,
  legal or consent copy, existing accessibility wins (focus states, alt
  text, keyboard paths, contrast), or section IDs that tracking uses.

## Libraries and tooling

Hand-rolling every button, toggle and nav reproduces the slop defaults and
ships broken controls. On a real framework, take accessible, functioning
primitives from tested libraries and art-direct hard on top. The standing
toolkit, all free:

- **Motion** (motion.dev; npm i motion, import from motion/react). The
  animation engine, and the one piece that needs no Tailwind, so it works
  in any project. Springs, gestures, scroll-linked transforms (useScroll,
  useTransform), animated numbers, text effects, marquees, layout
  animation. (The Motion AI Kit is a paid Motion+ MCP; skip it without a
  token.)
- **shadcn/ui** (ui.shadcn.com). React + Radix + Tailwind copy-paste
  primitives: button, dialog, tabs, accordion, form, table, command
  palette. The accessible foundation layer; add via its CLI.
- **tailark** (tailark.com). Tailwind + shadcn marketing blocks and full
  pages: heroes, features, pricing, testimonials, FAQ, CTAs, bento grids,
  footers.
- **motion-primitives** (motion-primitives.com). Motion + Tailwind animated
  components: text effects, infinite slider/marquee, animated tabs,
  accordion, cursor, morphing dialog.
- **kokonut UI** (kokonutui.com). Tailwind v4 + Motion, 100+ components
  including useful AI states (AI input search, loading/text states, voice),
  particle/magnet buttons, flip/liquid-glass/bento cards, morphic navbars.
  Add via the shadcn CLI with the kokonut registry.

In a project without Tailwind, install Motion for the animation and adapt
the others' structure into the project's own styling; never bolt global
Tailwind onto a large existing codebase for one block, it can regress every
other page. And de-slop everything prebuilt: these libraries ship
blue-purple gradients, glowy pills, fill-plus-outline pairs, sun-moon
toggles and tracked caps on their defaults. Keep the accessible behavior
and structure, replace the generic styling, and run every prebuilt block
through this whole file exactly like your own work.

## Field notes: what actually landed

Distilled from builds accepted only after earlier ones were rejected. These
sit on top of everything above; when in doubt, they win.

- **Cohesion is the whole game.** The loudest failure was not a slop tell,
  it was incoherence: individually fine parts that did not belong together
  ("every small good part from a hundred feet away, made into the ugliest
  thing"). The fix that landed every time: pick ONE world and make every
  element serve it. One palette held with discipline (monochrome or
  tightly-related beats "blue AND green AND a warm accent"). One type voice
  (a single family across weights and optical sizes, or one display plus
  one quiet neutral, nothing else). One signature artifact decided first.
  Decide the world, then compose the sections from it.
- **"Creative" is not "realistic".** When the brief asks for creative or
  maximal, photoreal stock (a real lake, real water) reads as the opposite.
  Use an authored treatment in ONE consistent medium: cyanotype, riso,
  pixel art, one illustration style, a painted sky. A limited-palette
  medium also makes every image cohere with the page for free (a
  cyanotype's blue became the page's blue: zero seams).
- **The product-as-artifact is a signature, not the slop window.** A faux
  app window is a tell only when it is empty and generic. A detailed, fully
  populated, real-feeling product UI (the actual editor, real diffs,
  working controls), floated with depth and clipped at an edge, is one of
  the strongest signatures there is. Build it as real interactive UI, not a
  picture. And only when a product UI exists: if the product is literally a
  file, show the file. Design from what the thing IS, not from a reference
  site.
- **Take the language from references, never the content.** From "this
  vibe" examples, lift the palette mood, type energy, motion, the kind of
  hero and footer; then design original copy, layout and artifact for THIS
  product. A reproduced headline or product window is copying, and it
  shows. Reference is direction, not a stencil.
- **Dead-looking is a fail on its own.** "Boring, static, the menu has no
  animation" is a real rejection even with zero slop present. Put authored,
  purposeful motion on the page: a nav that enters and responds, a
  signature that drifts, scroll-linked parallax, crafted hovers. Calm is
  allowed; dead is not.
