🧭 Molecular Compass

An AI-Native Drug Discovery Engine

Overview

    Molecular Compass is an AI-native platform that reimagines how drug discovery should work in 2025. Inspired by the collapse of Pardes Biosciences’ lead antiviral candidate in Phase 2, our system is designed to prevent exactly that kind of failure by shifting the most expensive, risky steps of drug development into the virtual domain.

    Instead of years of trial-and-error in the lab, Molecular Compass uses multi-agent AI to design, evaluate, and optimize drug candidates in silico. It’s not just a tool for scientists -- it’s a Drug Design Copilot that democratizes molecular innovation for biopharma teams of all sizes.

Motivation

    Pardes Biosciences failed not because the science was wrong, but because the process was slow, costly, and blind to risks like toxicity until too late. This is the story of drug discovery as a whole:

    90% of drug candidates fail in clinical trials.

    Billions are wasted on molecules that were doomed from the start.

    AI offers a way out -- if we make it the foundation, not the afterthought. Molecular Compass is built as if AI were in the driver’s seat from day one.

Multi-Agent Architecture

🎯 Target & Goal Agent
    Users input a viral target (e.g. SARS-CoV-2 protease) and desired drug properties (oral, low toxicity, reversible-covalent binding).

🧪 Generative Chemist
    A structure-based generative AI that designs novel molecules from scratch. Instead of screening existing libraries, it tailors molecules to the protein’s 3D structure, incorporating binding-site constraints.

🔮 Predictor Agent
    Runs virtual assays to forecast:

    Binding Affinity (efficacy)

    Toxicity (safety)

    ADME (Absorption, Distribution, Metabolism, Excretion -- oral viability)

    This step directly tackles the failure point that ended Pardes’s candidate.

♻️ Optimizer Agent
    Feedback loop: molecules that score poorly are refined iteratively, balancing efficacy and safety at scale.

    This continuous optimization mimics the iterative cycles of medicinal chemistry, but at AI speed.

MVP Features

    Web App (Hugging Face / Vercel) – Input a target, instantly generate molecules.

    2D/3D Visualization – Interactive views of candidate structures.
    
    Property Dashboard – Tables of predicted binding, toxicity, and ADME scores.
    
    Looped Generation – Demonstrates optimization cycles in real-time.

Why Now

    AI-driven drug discovery is no longer speculative: companies like Insilico Medicine and Atomwise have validated the approach.

    Pharma giants (e.g. Lilly) are launching AI platforms to democratize discovery.

    Generative AI has matured enough to make de novo molecular design both feasible and defensible.

    Molecular Compass captures this momentum with a SaaS-first, B2B platform -- the “Copilot for Drug Discovery.”

Demo

Demo: [\[Hugging Face\]](https://huggingface.co/spaces/Jesse-Flores/molecular-compass)


Next Steps

    Expand from mock predictors → integrate pre-trained QSAR/QSPR models.

    Add structure-based generation tied to protein binding sites.

    Extend scope from drug discovery → clinical trial optimization (patient stratification).

Authors

Created by Jesse Flores at HackMIT 2025.