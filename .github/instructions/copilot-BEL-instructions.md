---
name: copilot-BEL
description: Design guide for Soc Ops - Euphoria Dark Theme
applyTo: "**"
---

# Soc Ops Design System

I created this during a Python lab class at FIAP in partnership with Microsoft, using GitHub Copilot as the development tool.

This document defines the visual and interaction standards for the Soc Ops Social Bingo application with the Euphoria Dark theme. (Euphoria from the HBO series, haha)

ps: In the future, I will continue improving this project and create a comparison of episodes with comments from the AI ​​Agent.
---

## Color Palette

### Primary Colors

| Color | CSS Var | Hex | Usage |
|-------|---------|-----|-------|
| Background Dark | `--color-bg-dark` | `#0a0e27` | Page background |
| Background Darker | `--color-bg-darker` | `#050810` | Layers profundas |
| Neon Pink | `--color-neon-pink` | `#FF006E` | Primary CTA, active states |
| Neon Pink Bright | `--color-neon-pink-bright` | `#FF1493` | Hover states |
| Neon Cyan | `--color-neon-cyan` | `#00F5FF` | Secondary accents, borders |
| Neon Magenta | `--color-neon-magenta` | `#E81B8E` | Tertiary accents |
| Neon Magenta Bright | `--color-neon-magenta-bright` | `#FF10F0` | Peak emphasis |

### Text Colors

| Color | CSS Var | Hex | Usage |
|-------|---------|-----|-------|
| Text White | `--color-text-white` | `#FFFFFF` | Primary text |
| Text Gray | `--color-text-gray` | `#B0B8C1` | Secondary text |
| Text Muted | `--color-text-muted` | `#6B7280` | Tertiary text |

### Usage

Reference colors via CSS variables:

```css
background-color: var(--color-bg-dark);
color: var(--color-neon-pink);
border-color: var(--color-neon-cyan);
```

---

## Typography

### Font Stack

| Role | Font | Weight | Use Case |
|------|------|--------|----------|
| Display | Space Grotesk | 700, 600 | Hero text, headings |
| Body | Space Grotesk | 400, 500, 600 | Body copy, instructions |
| Mono | JetBrains Mono | 400, 500, 600 | Labels, details, UI text |

### Font Import

```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
```

### Scale

| Element | Size | Weight | Font | Example |
|---------|------|--------|------|---------|
| H1 | 3rem | 700 | Space Grotesk | "SOC OPS" |
| H2 | 1.875rem | 700 | Space Grotesk | "BINGO!" |
| Body | 0.875–1rem | 400–500 | Space Grotesk | Game text |
| UI Labels | 0.75rem | 500 | JetBrains Mono | Square text |

---

## Glow Effects

### Glow Variables

```css
--glow-pink: 0 0 20px rgba(255, 0, 110, 0.5), 0 0 40px rgba(255, 0, 110, 0.3);
--glow-cyan: 0 0 20px rgba(0, 245, 255, 0.5), 0 0 40px rgba(0, 245, 255, 0.3);
--glow-magenta: 0 0 20px rgba(232, 27, 142, 0.5), 0 0 40px rgba(232, 27, 142, 0.3);
```

### Text Glow

```css
h1 {
    text-shadow: 0 0 10px var(--color-neon-cyan), 0 0 20px rgba(255, 0, 110, 0.3);
}
```

### Border Glow

```css
.button {
    box-shadow: var(--glow-pink);
}

.button:hover {
    box-shadow: var(--glow-pink), 0 0 60px rgba(255, 0, 110, 0.6);
}
```

---

## Animations

### neon-glow-pulse

Text glow breathing effect for hero text and messages.

```css
@keyframes neon-glow-pulse {
    0%, 100% {
        text-shadow: 0 0 10px var(--color-neon-pink), 0 0 20px var(--color-neon-pink),
                     0 0 30px var(--color-neon-magenta), 0 0 40px var(--color-neon-magenta);
        filter: brightness(1);
    }
    50% {
        text-shadow: 0 0 20px var(--color-neon-pink), 0 0 30px var(--color-neon-pink),
                     0 0 40px var(--color-neon-magenta), 0 0 50px var(--color-neon-magenta);
        filter: brightness(1.2);
    }
}

animation: neon-glow-pulse 2s ease-in-out infinite;
```

Use: Start screen title, bingo indicator, modal heading

### celebrate-bounce

Victory bounce animation.

```css
@keyframes celebrate-bounce {
    0% {
        transform: scale(0.3) translateY(40px);
        opacity: 0;
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1) translateY(0);
        opacity: 1;
    }
}

animation: celebrate-bounce 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
```

Use: Modal appearance, victory emoji

### pulse-glow

Box-shadow breathing for marked elements.

```css
@keyframes pulse-glow {
    0%, 100% {
        box-shadow: var(--glow-pink);
    }
    50% {
        box-shadow: 0 0 40px rgba(255, 0, 110, 0.7), 0 0 60px rgba(255, 0, 110, 0.4);
    }
}

animation: pulse-glow 2s ease-in-out infinite;
```

Use: Marked bingo squares, hovered buttons

### neon-border-pulse

Border color shift between cyan and magenta.

```css
@keyframes neon-border-pulse {
    0%, 100% {
        border-color: var(--color-neon-cyan);
        box-shadow: 0 0 10px var(--color-neon-cyan), inset 0 0 10px rgba(0, 245, 255, 0.1);
    }
    50% {
        border-color: var(--color-neon-magenta);
        box-shadow: 0 0 20px var(--color-neon-magenta), inset 0 0 20px rgba(232, 27, 142, 0.1);
    }
}

animation: neon-border-pulse 1s ease-in-out infinite;
```

Use: Winning squares, high-importance cards

### scale-fade-in

Fade-in with scale for entrances.

```css
@keyframes scale-fade-in {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

animation: scale-fade-in 0.6s ease-out;
```

Use: Game board on load

### slide-up-fade-in

Upward slide with fade.

```css
@keyframes slide-up-fade-in {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

animation: slide-up-fade-in 0.8s ease-out;
```

Use: Start screen entrance

---

## Component Standards

### Primary Button

```css
.primary-button {
    background: linear-gradient(135deg, var(--color-neon-pink) 0%, var(--color-neon-magenta) 100%);
    border: 2px solid var(--color-neon-pink-bright);
    box-shadow: var(--glow-pink);
    color: var(--color-text-white);
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: all 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.primary-button:hover {
    box-shadow: var(--glow-pink), 0 0 60px rgba(255, 0, 110, 0.6);
    transform: translateY(-2px);
}
```

### Secondary Button

```css
.secondary-button {
    color: var(--color-text-gray);
    border: 1px solid rgba(0, 245, 255, 0.3);
    padding: 0.375rem 0.75rem;
    transition: all 150ms ease-out;
}

.secondary-button:hover {
    color: var(--color-neon-cyan);
    border-color: var(--color-neon-cyan);
    box-shadow: 0 0 10px rgba(0, 245, 255, 0.3);
}
```

### Bingo Square

```css
.bingo-square {
    background: rgba(0, 245, 255, 0.03);
    border: 2px solid var(--color-neon-cyan);
    box-shadow: inset 0 0 10px rgba(0, 245, 255, 0.1);
    font-family: var(--font-mono);
}

.bingo-square:hover {
    border-color: var(--color-neon-pink);
    box-shadow: 0 0 15px rgba(0, 245, 255, 0.4);
}

.bingo-square.marked {
    background: rgba(255, 0, 110, 0.15);
    border-color: var(--color-neon-pink);
    box-shadow: 0 0 20px rgba(255, 0, 110, 0.4), inset 0 0 10px rgba(255, 0, 110, 0.1);
    animation: pulse-glow 2s ease-in-out infinite;
}

.bingo-square.winning {
    background: linear-gradient(135deg, rgba(255, 0, 110, 0.25) 0%, rgba(232, 27, 142, 0.25) 100%);
    border-color: var(--color-neon-pink-bright);
    box-shadow: 0 0 30px var(--color-neon-magenta), inset 0 0 15px rgba(255, 0, 110, 0.2);
    animation: neon-border-pulse 1s ease-in-out infinite;
}
```

### Modal

```css
.modal-content {
    background: linear-gradient(135deg, rgba(10, 14, 39, 0.95) 0%, rgba(26, 15, 53, 0.95) 100%);
    border: 2px solid var(--color-neon-pink);
    box-shadow: 0 0 40px var(--color-neon-pink), 0 0 80px var(--color-neon-magenta),
                inset 0 0 20px rgba(255, 0, 110, 0.1);
}

.modal-overlay {
    background: rgba(0, 0, 0, 0.9);
    backdrop-filter: blur(10px);
}
```

### Card

```css
.card {
    background: rgba(0, 245, 255, 0.05);
    border: 2px solid var(--color-neon-cyan);
    box-shadow: 0 0 20px rgba(0, 245, 255, 0.2), inset 0 0 20px rgba(0, 245, 255, 0.05);
    backdrop-filter: blur(10px);
}
```

---

## Background & Atmosphere

### Page Background

```css
body {
    background: linear-gradient(135deg, var(--color-bg-darker) 0%, var(--color-bg-dark) 50%, #1a0f35 100%);
}

#app::before {
    content: '';
    position: fixed;
    inset: 0;
    background: 
        radial-gradient(circle at 20% 50%, rgba(255, 0, 110, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(0, 245, 255, 0.05) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}
```

### Header

```css
header {
    background: rgba(10, 14, 39, 0.8);
    backdrop-filter: blur(10px);
    border-bottom: 2px solid rgba(0, 245, 255, 0.2);
}
```

---

## Responsive

### Mobile Breakpoints

```css
@media (max-width: 768px) {
    .start-container h1 {
        font-size: 2.5rem;
    }
    
    .bingo-square {
        font-size: 0.65rem;
    }
}
```

### Accessibility

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## Implementation Checklist

When adding new components:

- Use CSS variables for colors
- Apply neon glow for interactive elements
- Use Space Grotesk for headings, JetBrains Mono for details
- Add hover/focus states with enhanced glow
- Animate entrance with scale-fade-in or slide-up-fade-in
- Respect dark theme background
- Test on mobile (375px+)
- Verify animation smoothness
- Support prefers-reduced-motion

---

## File References

- CSS: `/app/static/css/app.css`
- Templates:
  - `/app/templates/base.html`
  - `/app/templates/components/start_screen.html`
  - `/app/templates/components/bingo_board.html`
  - `/app/templates/components/bingo_modal.html`
  - `/app/templates/components/game_screen.html`

---

## Design Philosophy

The Euphoria Dark & Dramatic aesthetic:

1. High Contrast: Dark background + neon colors create visual hierarchy
2. Neon Glow: Cyberpunk aesthetic with purposeful glows
3. Typography: Bold, geometric fonts command focus
4. Motion: Purposeful animations enhance engagement
5. Minimalism: Avoid clutter; let neon shine
6. Consistency: All interactive elements follow the same language

---

Last Updated: April 11, 2026
Theme Version: Euphoria Dark v1.0
